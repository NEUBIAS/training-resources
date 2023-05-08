import numpy as np
import tifffile, requests, os, tempfile
from pathlib import Path



def get_ijtiff(fpath: [str, Path]):
    """ Returns a tifffile.TiffFile object from a tiff file.
        If fpath is a url, first download the file to a local temporary path.
        Throw an error if the file is not an ImageJ-created tiff.
    """
    fname = fpath.rsplit('/')[-1]
    tiff = None
    try:
        if fpath.startswith('https:') or fpath.startswith('http:'): # then fpath is a url, download it to the current directory
            with tempfile.TemporaryDirectory() as tempdir:
                localpath = Path(os.path.join(tempdir, fname))
                r = requests.get(fpath)
                with open(os.path.join(localpath), "wb") as f:
                    f.write(r.content)
                tiff = tifffile.TiffFile(localpath)
        else:
            tiff = tifffile.TiffFile(fpath)
    except:
        if tiff is None:
            raise ValueError("tiff file could not be found in the given path:\n{}".format(fpath))
    if not tiff.is_imagej:
        raise TypeError("This module is intended to parse from ImageJ-created tiff files. This tiff file was apparently not created by ImageJ.")
    return tiff

def escape_unicode(text: str):
    return bytes(text, 'utf-8').decode('unicode_escape')
    
def encode_unicode(text: str):
    # TODO: On windows this does not encode properly in IJ. 
    # The returned value for micron is \xb5 and IJ does not read it as micron.
    return text.encode('unicode_escape').decode('utf-8')

def open_ij_tiff(fpath: [str, Path],
                 fetch_extra_metadata: bool = False # Should be true to extract any ImageJ display metadata from the tiff file.
                 ):
    """
    What it does:
        Imports the binary data and the metadata from an ImageJ-created tiff file.
    Takes:
        fpath: Either a local path or url to a tiff file.
        fetch_extra_metadata: Whether to extract any ImageJ display metadata from the input tiff file.
                              If False, only the pixel calibration metadata are extracted.
    Returns
        image_array: A numpy array with the binary image data
        ax_names: The available axes, can be any combination of t, c, z, y, x
        ax_scales: Voxel scales along each dimension. Float for t, z, y and x and 'na' for channel.
        ax_units: Voxel scale units along each dimension ('na' for channel)
        extra_metadata (returned only if fetch_extra_metadata is True): Extra ImageJ-specific metadata, such as LUTs, brightness-contrast adjustments, etc.
    """
    ############################# download the image if path is a url ###############################
    tiff = get_ijtiff(fpath)
    ############################ Parse the data and metadata #########################################
    voxel_sizes, voxel_units = {}, {}
    # First get the image array and axes  tags
    image_array = tiff.asarray()  ### Image data parsed as numpy array
    ax_names = tiff.series[0].axes.upper()  ### This gives the axis order
    # Second, parse, time, channel and z
    image_metadata = tiff.imagej_metadata  ### ImageJ metadata object
    # get z informtion
    if 'Z' in ax_names:
        if 'spacing' in image_metadata:
            voxel_sizes['z'] = image_metadata['spacing']
            voxel_units['z'] = image_metadata['unit']
        else:
            print("Z scaling missing or is exactly 1 spatial unit; Setting to 1 pixel.")
            voxel_sizes['z'] = 1
            voxel_units['z'] = 'Slice'
    # get time information
    if 'T' in ax_names: ### imagej metadata does not seem to store time increment unit other than seconds ?!
        if 'finterval' in image_metadata:
            finterval = image_metadata['finterval']
            if 'fps' in image_metadata:
                timeunit = 'sec'
            else:
                print("Time unit missing; Setting to 'Frame'.")
                timeunit = 'Frame'
        elif 'fps' in image_metadata:
            finterval = 1 / image_metadata['fps']
            timeunit = 'sec'
        else:
            print("Time scale missing; Setting to '1 Frame'.")
            finterval = 1
            timeunit = 'Frame'
        voxel_sizes['t'] = finterval
        voxel_units['t'] = timeunit  ### imagej metadata does not seem to store time increment unit other than seconds ?!
    # get channel information
    if 'C' in ax_names:
        voxel_sizes['c'] = 1
        voxel_units['c'] = 'na'

    # third, parse x and y
    tags = tiff.pages[0].tags
    if 'YResolution' in tags:
        num_pixels, units = tags['YResolution'].value
        voxel_sizes['y'] = units / num_pixels
        voxel_units['y'] = image_metadata['unit']
    else:
        print("Y scaling missing; Setting to 1 pixel.")
        voxel_sizes['y'] = 1
        voxel_units['y'] = 'Pixel'
    if 'XResolution' in tags:
        num_pixels, units = tags['XResolution'].value
        voxel_sizes['x'] = units / num_pixels
        voxel_units['x'] = image_metadata['unit']
    else:
        print("X scaling missing; Setting to 1 pixel.")
        voxel_sizes['x'] = 1
        voxel_units['x'] = 'Pixel'
    ax_scales = [voxel_sizes[i] for i in ax_names.lower()]
    ax_units = [escape_unicode(voxel_units[i]) for i in ax_names.lower()]
    ################### Return either with or without extra metadata #################################
    if fetch_extra_metadata:
        extra_metadata = {}
        extra_metadata['dtype'] = tiff.pages[0].dtype
        extra_metadata['bitspersample'] = tiff.pages[0].bitspersample
        for key in image_metadata:
            if key not in ['spacing', 'unit', 'finterval', 'fps']:
                extra_metadata[key] = image_metadata[key]
        return image_array, ax_names, ax_scales, ax_units, extra_metadata
    else:
        return image_array, ax_names, ax_scales, ax_units


def save_ij_tiff(tiffdest: [str, Path],
                 image_array: np.ndarray,
                 ax_names: list,
                 ax_scales: list,
                 ax_units: list,
                 extra_metadata: dict = None # Contains further metadata, such as display metadata. This can be used, for instance, to update, or keep the existing display information in the tiff metadata.
                 ):

    metadata = {
        'axes': ax_names,
        }

    if 'Y' in ax_names:
        y_idx = ax_names.index('Y')
    if 'X' in ax_names:
        x_idx = ax_names.index('X')
        metadata['unit'] = encode_unicode(ax_units[x_idx])
    if 'Z' in ax_names:
        z_idx = ax_names.index('Z')
        if ax_units[z_idx] != 'Slice': ### TODO: This checkpoint might be improved
            metadata['spacing'] = ax_scales[z_idx]
    if 'T' in ax_names:
        t_idx = ax_names.index('T')
        if ax_units[t_idx] != 'Frame': ## TODO: This checkpoint might be improved
            metadata['finterval'] = ax_scales[t_idx]
        if (ax_units[t_idx] == 'sec') | (ax_units[t_idx] == 's'):
            metadata['fps'] = image_array.shape[t_idx] / ax_scales[t_idx]

    if extra_metadata is not None:
        assert isinstance(extra_metadata, type({})), " 'extra_metadata' must be of type 'dict' "
        for key in extra_metadata:
            if key not in [ 'images', 'slices', 'frames', 'hyperstack', 'bitspersample' ]:
                metadata[key] = extra_metadata[key]
        image_array = image_array.astype(metadata['dtype'])
        bitspersample = ''.join(tuple([i for i in str(metadata['dtype']) if i.isnumeric()])) ### TODO: This can be improved
        if len(bitspersample) > 0:
            metadata['bitspersample'] = int(bitspersample)
    else:
        metadata['dtype'] = image_array.dtype

    tifffile.imwrite(
        tiffdest,
        image_array,
        imagej = True,
        dtype = metadata['dtype'],
        resolution = (1 / ax_scales[x_idx], 1 / ax_scales[y_idx]),
        metadata = metadata
        )
    return metadata



