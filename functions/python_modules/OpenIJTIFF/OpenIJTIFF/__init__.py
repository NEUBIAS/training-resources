import tempfile
from pathlib import Path
from typing import Any, Dict, Optional, Sequence, Tuple, Union

import numpy as np
import numpy.typing as npt
import requests
import tifffile
from skimage.io import imread
import napari


def _fetch_data(uri: str) -> Path:
    """Downloads a given file from a uri to a temporary directory

    Creates a directory safely via tempfile.mkdtemp for each downloaded
    files. Note: files are not cleaned up.

    Args:
        uri: uri pointing to a file

    Returns:
        Path to downloaded file in temporary directory
    """
    fname = uri.rsplit("/")[-1]

    tmpdir = Path(tempfile.mkdtemp())

    localpath = tmpdir / fname
    r = requests.get(uri)
    r.raise_for_status()
    localpath.write_bytes(r.content)

    return localpath


def get_ijtiff(fpath: Union[str, Path]) -> tifffile.TiffFile:
    """Open TiffFile object from url or path

    Args:
        fpath: URL or path to a tiff file. If fpath is a url, the file
          is first downloaded to a local temporary path.

    Returns:
        tifffile.TiffFile object.

    Raises
        TypeError if the file is not an ImageJ-created tiff.
    """
    if isinstance(fpath, str) and (fpath.startswith("https://") or fpath.startswith("http://")):
        fpath = _fetch_data(fpath)
    else:
        fpath = Path(fpath)

    tiff = tifffile.TiffFile(fpath)

    if not tiff.is_imagej:
        raise TypeError(
            "This module is intended to parse from ImageJ-created tiff files. This tiff file was apparently not created by ImageJ."
        )
    return tiff


def escape_unicode(text: str) -> str:
    return bytes(text, "utf-8").decode("unicode_escape")


def encode_unicode(text: str) -> str:
    # TODO: On windows this does not encode properly in IJ.
    # The returned value for micron is \xb5 and IJ does not read it as micron.
    return text.encode("unicode_escape").decode("utf-8")


_open_ij_tiff_returns = Tuple[npt.ArrayLike, str, Sequence[Union[float, str]], Sequence[str]]
_open_ij_tiff_returns_extra = Tuple[npt.ArrayLike, str, Sequence[Union[float, str]], Sequence[str], Dict[str, Any]]
open_ij_tiff_returns = Union[_open_ij_tiff_returns, _open_ij_tiff_returns_extra]


def open_ij_tiff(
    fpath: Union[str, Path],
    fetch_extra_metadata: bool = False,
) -> open_ij_tiff_returns:
    """
    What it does:
        Imports the binary data and the metadata from an ImageJ-created tiff file.
    Args:
        fpath: Either a local path or url to a tiff file.
        fetch_extra_metadata: Whether to extract any ImageJ display metadata from the input tiff file.
          If False, only the pixel calibration metadata are extracted.
          Should be true to extract any ImageJ display metadata from the tiff file.
    Returns
        image_array: A numpy array with the binary image data.
        ax_names: The available axes, can be any combination of T, C, Z, Y, X.
        ax_scales: Voxel scales along each dimension. Float for T, Z, Y and X and 'na' for channel.
        ax_units: Voxel scale units along each dimension ('na' for channel).
        extra_metadata, optional (returned only if fetch_extra_metadata is True).
          Extra ImageJ-specific metadata, such as LUTs, brightness-contrast adjustments, etc.
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
    if "Z" in ax_names:
        if "spacing" in image_metadata:
            voxel_sizes["z"] = image_metadata["spacing"]
            voxel_units["z"] = image_metadata["unit"]
        else:
            print("Z scaling missing or is exactly 1 spatial unit; Setting to 1 pixel.")
            voxel_sizes["z"] = 1
            voxel_units["z"] = "Slice"
    # get time information
    if "T" in ax_names:  ### imagej metadata does not seem to store time increment unit other than seconds ?!
        if "finterval" in image_metadata:
            finterval = image_metadata["finterval"]
            if "fps" in image_metadata:
                timeunit = "sec"
            else:
                print("Time unit missing; Setting to 'Frame'.")
                timeunit = "Frame"
        elif "fps" in image_metadata:
            finterval = 1 / image_metadata["fps"]
            timeunit = "sec"
        else:
            print("Time scale missing; Setting to '1 Frame'.")
            finterval = 1
            timeunit = "Frame"
        voxel_sizes["t"] = finterval
        voxel_units["t"] = (
            timeunit  ### imagej metadata does not seem to store time increment unit other than seconds ?!
        )
    # get channel information
    if "C" in ax_names:
        voxel_sizes["c"] = 1
        voxel_units["c"] = "na"

    # third, parse x and y
    tags = tiff.pages[0].tags
    if "YResolution" in tags:
        num_pixels, units = tags["YResolution"].value
        voxel_sizes["y"] = units / num_pixels
        voxel_units["y"] = image_metadata["unit"]
    else:
        print("Y scaling missing; Setting to 1 pixel.")
        voxel_sizes["y"] = 1
        voxel_units["y"] = "Pixel"
    if "XResolution" in tags:
        num_pixels, units = tags["XResolution"].value
        voxel_sizes["x"] = units / num_pixels
        voxel_units["x"] = image_metadata["unit"]
    else:
        print("X scaling missing; Setting to 1 pixel.")
        voxel_sizes["x"] = 1
        voxel_units["x"] = "Pixel"
    ax_scales = [voxel_sizes[i] for i in ax_names.lower()]
    ax_units = [escape_unicode(voxel_units[i]) for i in ax_names.lower()]
    ################### Return either with or without extra metadata #################################
    if fetch_extra_metadata:
        extra_metadata = {}
        extra_metadata["dtype"] = tiff.pages[0].dtype
        extra_metadata["bitspersample"] = tiff.pages[0].bitspersample
        for key in image_metadata:
            if key not in ["spacing", "unit", "finterval", "fps"]:
                extra_metadata[key] = image_metadata[key]
        return image_array, ax_names, ax_scales, ax_units, extra_metadata
    else:
        return image_array, ax_names, ax_scales, ax_units


def save_ij_tiff(
    tiffdest: Union[str, Path],
    image_array: np.ndarray,
    ax_names: Optional[Sequence[str]] = None,
    ax_scales: Optional[Sequence[float]] = None,
    ax_units: Optional[Sequence[str]] = None,
    extra_metadata: Optional[dict] = None,
) -> Dict[str, Any]:
    """
    Args:
        tiffdest: location to save tiff file to.
        image_array: image data to write
        ax_names: Axis names in as uppercase letters, e.g. ["Z", "Y", "X"]
        ax_scales: Real numbers that specify scale per axis e.g. [5.0, 1.0, 1.0]
        ax_units: String denoting the unit of the data. See
          https://imagej.net/ij/docs/guide/146-28.html#toc-Subsection-28.4
          for possible values.
        extra_metadata: Contains further metadata, such as display metadata.
          This can be used, for instance, to update, or keep the existing display
          information in the tiff metadata.

    Returns
        Metadata dictionary
    """

    _full_axes = 'TCZYX'
    _full_units = ['Frame', 'na', 'Slice', 'Pixel', 'Pixel']

    if ax_names is None:
        ax_names = _full_axes[-image_array.ndim:]
    if ax_units is None:
        ax_units = _full_units[-image_array.ndim:]
    if ax_scales is None:
        ax_scales = [1] * image_array.ndim
    ax_names = ax_names.upper()
    assert len(ax_names) == image_array.ndim, f"The length of 'ax_names' must match the number of dimensions, which is {image_array.ndim}"
    assert len(ax_units) == image_array.ndim, f"The length of 'ax_units' must match the number of dimensions, which is {image_array.ndim}"
    assert len(ax_scales) == image_array.ndim, f"The length of 'ax_scales' must match the number of dimensions, which is {image_array.ndim}"

    metadata = {
        "axes": ax_names,
    }

    if image_array.dtype == np.dtype(bool):
        image_array = image_array.astype(np.uint8) * 255

    if "Y" in ax_names:
        y_idx = ax_names.index("Y")
        metadata["unit"] = ax_units[y_idx]
    if "X" in ax_names:
        x_idx = ax_names.index("X")
        metadata["unit"] = ax_units[x_idx]
    if "Z" in ax_names:
        z_idx = ax_names.index("Z")
        if ax_units[z_idx] != "Slice":  ### TODO: This checkpoint might be improved
            metadata["spacing"] = ax_scales[z_idx]
    if "T" in ax_names:
        t_idx = ax_names.index("T")
        if ax_units[t_idx] != "Frame":  ## TODO: This checkpoint might be improved
            metadata["finterval"] = ax_scales[t_idx]
        if (ax_units[t_idx] == "sec") | (ax_units[t_idx] == "s"):
            metadata["fps"] = image_array.shape[t_idx] / ax_scales[t_idx]

    if extra_metadata is not None:
        assert isinstance(extra_metadata, dict), " 'extra_metadata' must be of type 'dict' "
        for key in extra_metadata:
            if key not in ["images", "slices", "frames", "hyperstack", "bitspersample"]:
                metadata[key] = extra_metadata[key]
        image_array = image_array.astype(metadata["dtype"])
        bitspersample = "".join(
            tuple([i for i in str(metadata["dtype"]) if i.isnumeric()])
        )  ### TODO: This can be improved
        if len(bitspersample) > 0:
            metadata["bitspersample"] = int(bitspersample)
    else:
        metadata["dtype"] = image_array.dtype

    tifffile.imwrite(
        tiffdest,
        image_array,
        imagej=True,
        dtype=metadata["dtype"],
        resolution=(1 / ax_scales[x_idx], 1 / ax_scales[y_idx]),
        metadata=metadata,
    )
    return metadata




