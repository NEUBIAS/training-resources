## Connect to the BAND cloud computer

In this practical we are using the [BAND](https://band.embl.de/#/eosc-landingpage) cloud computing.


#### Connect the first time

To connect to the BAND, please follow these steps:

- Go to the [BAND](https://band.embl.de/#/eosc-landingpage) web site
- Read the [user guide](https://docs.google.com/document/d/1TZBUsNIciGMH_g4aFj2Lu_upISxh5TV9FBMrvNDWmc8/edit?usp=sharing)
- Accept the terms of usage, to activate the login button
- `[ Login ]`
  - Please use your Google account
- Choose 4 CPU and 8 GB memory
- `[ Launch ]`
- On the same page below, now `[ Go to Desktop ]`

#### Re-connect to a session

If you did not stop the recent session you can simply

- Go to the [BAND](https://band.embl.de/#/eosc-landingpage) web site
- `[ Go to Desktop ]`

## Software installation

For this practical we need several software to be installed:

+ **napari_viewer** environment containing the napari package along with dependencies/plugins to support OME-Zarr format.

+ **bf2raw** environment containing the bioformats2raw package, which can be used to convert images into OME-Zarr format.

+ **minio** environment containing the minio client mc, which enables interaction with s3 buckets.

+ **fiji** exectuable containing a plugin for opening the OME-Zarr format.

To install the software you will need to launch your BAND cloud computer (see above) and use Firefox and the terminal window.

![Image](docs/BAND_Terminal_Firefox.png)


Please follow those steps:

1. Launch the BAND cloud computer (see instructions above)
1. Open a Terminal window (see screenshot above)
1. Open Firefox (see screenshot above) on the BAND.
1. In Firefox browse to the Google Doc that has been shared with you (it is the same Google Doc that brought you to this page; you need to type the address starting with `tinyurl...` into the Firefox search bar and press enter)
1. Copy the command (starting with `cd ~ ...`) from the Google Doc into the Terminal window and press enter
1. This can take about 10 minutes.
1. It should finish saying: `Added s3minio successfully.`
