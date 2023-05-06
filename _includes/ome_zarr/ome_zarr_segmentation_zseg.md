**Examine the dataset that is to be segmented:**
```
mc tree -d 2 s3/ome-zarr-course/data/ZARR/$USER/23052022_D3_0002_positiveCTRL.ome.zarr
```

```
mc cat s3/ome-zarr-course/data/ZARR/$USER/23052022_D3_0002_positiveCTRL.ome.zarr/0/.zarray
```

**Also view the data**
```
napari --plugin napari-ome-zarr https://s3.embl.de/ome-zarr-course/data/ZARR/$USER/23052022_D3_0002_positiveCTRL.ome.zarr;
```

**Perform threshold segmentation on each channel**
```
zseg threshold -r -m otsu -c 1 -ch 0 -n otsu-c1-ch0 --colormap viridis ome-zarr-course/data/ZARR/$USER/23052022_D3_0002_positiveCTRL.ome.zarr;
```
In this command, the `-r` flag ensures that the input path is searched at the s3 bucket. The `-m` option specifies the thresholding algorithm, which in this case is the Otsu algorithm. The `-c` is a coefficient that is multiplied with the found threshold value to get the effective threshold. The `-ch` species the channel 0 for segmentation. The `-n` option specifies the name of the label path created. 

**Now also segment the other channel:**
```
zseg threshold -r -m otsu -c 1 -ch 1 -n otsu-c1-ch1 --colormap viridis ome-zarr-course/data/ZARR/$USER/23052022_D3_0002_positiveCTRL.ome.zarr;
```
Note that the `-ch` argument has been changed.

**Have a look at the segmented data** 
```
napari --plugin napari-ome-zarr https://s3.embl.de/ome-zarr-course/data/ZARR/$USER/23052022_D3_0002_positiveCTRL.ome.zarr;
```

**Apply mathematical morphology to the label image**
```
zseg postprocess -r -m binary_opening -f 1,1 -l otsu-c1-ch1 --colormap viridis ome-zarr-course/data/ZARR/$USER/23052022_D3_0002_positiveCTRL.ome.zarr;
```
Here the `-m` specifies the postprocessing method; the `-f` determines the footprint shape. Depending on the shape of the input data, it can be 2 or 3-dimensional. The `-l` can be used to decide on the name of the label image, that is subjected to the postprocessing. 

**Now examine the OME-Zarr data:**
```
mc tree -d 2 s3/ome-zarr-course/data/ZARR/$USER/23052022_D3_0002_positiveCTRL.ome.zarr
```
```
ome_zarr info https://s3.embl.de/ome-zarr-course/data/ZARR/$USER/23052022_D3_0002_positiveCTRL.ome.zarr
```
**Also visualise the data:**
```
napari --plugin napari-ome-zarr https://s3.embl.de/ome-zarr-course/data/ZARR/$USER/23052022_D3_0002_positiveCTRL.ome.zarr;
```
