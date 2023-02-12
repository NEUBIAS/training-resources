- Open Fiji
- Add the MoBIE update site and restart
- Open a MoBIE project containing correlative data:
  - `[ Plugins › MoBIE › Open › Open MoBIE Project... ]`
    - `Project Location` https://github.com/mobie/clem-example-project/
- Explore the transformation from viewer to global space:
  - Log the current transform from the global to the viewer space (g2v):
    - BDV: `Right click` and choose `Log Current View`
  - Add another image:
    - MoBIE UI: `tomogram` `tomo_37_hm` click `[ view ]`
  - Appreciate that is is hard to know where the new image is and that some navigation tools are handy.
  - Focus on the added image:
    - MoBIE UI: `tomo_37_hm` click `[ F ]`
  - Again log the g2v transform (s.a.)
  - Appreciate that the first component is bigger, corresponding to the higher zoom level.
- Explore the different voxel sizes of the image data:
  - Toggle off interpolation:
    - BDV: Keyboard `I`
    - It should say "nearest neighbor interpolation"
  - Zoom in a bit more:
    - BDV: Keyboard `Arrow up`
  - Move to the edge of the `tomo_37_hm`
    - BDV: Mouse `right button drag`
  - As an alternative to the above two steps:
    - Copy and paste `{"normalizedAffine":[0.4963397000728218,0.0,0.0,-108.59369157880992,0.0,0.4963397000728218,0.0,-152.83843100300004,0.0,0.0,0.4963397000728218,3.865989923867204E-4],"timepoint":0}` into the `location` field and click `[ move ]`
  - Appreciate that the voxels of the `em-overview` are visible (and are much larger the voxels of `tomo_37_hm`)
  - This information is encoded in the transformations from data space to global space (d2g), it can be found here:
    - [em-overview calibration](https://s3.embl.de/yeast-clem/hela/images/ome-zarr/em-overview.ome.zarr/.zattrs)
    - [tomo_37_nm calibration](https://github.com/mobie/clem-example-project/blob/66064176fa39b9f7d0e94f855f1c4b7d226812d4/data/hela/images/bdv-n5-s3/tomo_37_hm.xml#L38)






