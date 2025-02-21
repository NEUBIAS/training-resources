# Big image data formats (SPIM Data course)

## Location

Uni Bern, February 2025

## Topics

- Chunking
- Multi-resolution
- Remote storage 
- OME-Zarr

## Requirements

[Example big image data](https://zenodo.org/api/records/14857764/files-archive) (~10 GB)

[Fiji with MoBIE](https://github.com/mobie/mobie-viewer-fiji/tree/main?tab=readme-ov-file#install)

[NGFF Converter](https://www.glencoesoftware.com/products/ngff-converter/)

## Speaker

Christian Tischer (EMBL)

## Schedule

45 minutes live demo

## Training modules

1. [Big image data formats](https://neubias.github.io/training-resources/big_image_file_formats/index.html)
    - Lazy load TIFF stack in Fiji
    - Lazy load BDV XML/HDF5 in Fiji
1. [Remote (image) data access](https://neubias.github.io/training-resources/remote_data_access/index.html)
    - Discuss main figure to motivate why for standard cloud protocols it is a good idea for each chunk to be a stand-alone object
1. [OME-Zarr](https://neubias.github.io/training-resources/ome_zarr/index.html)
    - S-BSST410
        - Open OME-Zarr BioImage Archive website 
            - https://uk1s3.embassy.ebi.ac.uk/bia-integrator-data/pages/S-BSST410/IM2.html
            - Explore data using ViZarr
            - Read metadata 
        - Fiji 
            - Open same S3 URL with N5 BDV
            - Observe that looking at this dataset "from the side" is not performant
        - Use S3 URL to inspect the chunking with the NGFF Validator
            - Observe that the chunking is like in a TIFF file
            - See that one can load individual chunks
        - (Optional) Copy S3 URL and use minio CLI to inspect the data
    - Platy EM data
        - https://s3.embl.de/i2k-2020/platy-raw.ome.zarr
        - Open in Fiji
        - Open in Validator
        - Open in Neuroglancer
    - Create an OME-Zarr using Fiji
        - Use `xyz_uint8__em_platy.tif`
    - Convert an image to OME-Zarr using the NGFF Converter
        - Use `xyz_uint8__em_platy.tif`
        - Mention limitation of no z-chunking
    - Optional:
        - Open image, labels and table in MoBIE
