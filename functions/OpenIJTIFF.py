import tifffile, requests, os, tempfile
from pathlib import Path



def get_ijtiff(fpath):
    """ Return a tifffile.TiffFile object from a tiff file.
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

def open_ij_tiff(fpath):
    """
    What it does:
        Imports the binary data and the metadata from an ImageJ-created tiff file.
    Takes:
        fpath: either a local path or url to a tiff file.
    Returns
        image_array: A numpy array with the binary image data
        ax_names: The available axes, can be any combination of t, c, z, y, x
        ax_scales: Voxel scales along each dimension. Float for t, z, y and x and 'na' for channel.
        ax_units: Voxel scale units along each dimension ('na' for channel)
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
            print('Z scale is missing from the ImageDescription metadata !!!!!')
            print("Z scale was assigned '1' and Z scale unit was assigned 'Slice'")
            voxel_sizes['z'] = 1
            voxel_units['z'] = 'Slice'
    # get time information
    if 'T' in ax_names: ### imagej metadata does not seem to store time increment unit other than seconds ?!
        if 'finterval' in image_metadata:
            finterval = image_metadata['finterval']
            if 'fps' in image_metadata:
                timeunit = 'sec'
            else:
                print('Time unit is missing from the ImageDescription metadata !!!!!')
                print("Time unit was assigned 'Frame'")
                timeunit = 'Frame'
        elif 'fps' in image_metadata:
            finterval = 1 / image_metadata['fps']
            timeunit = 'sec'
        else:
            print('Time scale is missing from the ImageDescription metadata !!!!!')
            print("Time scale was assigned '1' and time scale unit was assigned 'Frame'")
            finterval = 1
            timeunit = 'Frame'
        voxel_sizes['t'] = finterval
        voxel_units['t'] = timeunit  ### imagej metadata does not seem to store time increment unit other than seconds ?!
    # get channel information
    if 'C' in ax_names:
        voxel_sizes['c'] = 'na'
        voxel_units['c'] = 'na'

    # third, parse x and y
    tags = tiff.pages[0].tags
    if 'YResolution' in tags:
        num_pixels, units = tags['YResolution'].value
        voxel_sizes['y'] = units / num_pixels
        voxel_units['y'] = image_metadata['unit']
    else:
        print("Y scale is missing from the tiff file !!!!!")
        print("Y scale was assigned '1' and y scale unit was assigned 'Pixel'")
        voxel_sizes['y'] = 1
        voxel_units['y'] = 'Pixel'
    if 'XResolution' in tags:
        num_pixels, units = tags['XResolution'].value
        voxel_sizes['x'] = units / num_pixels
        voxel_units['x'] = image_metadata['unit']
    else:
        print("X scale is missing from the tiff file !!!!!")
        print("X scale was assigned '1' and x scale unit was assigned 'Pixel'")
        voxel_sizes['x'] = 1
        voxel_units['x'] = 'Pixel'
    ax_scales = [voxel_sizes[i] for i in ax_names.lower()]
    ax_units = [voxel_units[i] for i in ax_names.lower()]
    out = {
        'array': image_array,
        'axes': ax_names,
        'scales': ax_scales,
        'units': ax_units
    }
    return image_array, ax_names, ax_scales, ax_units

class IJTIFF:
    # TODO: extend this class with update and write methods.
    def __init__(self, read_path = None):
        if read_path is not None:
            self.read(read_path)
    def read(self, read_path):
        self.array, self.axes, self.scales, self.units = open_ij_tiff(read_path)
        self.scales_dict = {key: self.scales[i] for i, key in enumerate(self.axes)}
        self.units_dict = {key: self.units[i] for i, key in enumerate(self.units)}