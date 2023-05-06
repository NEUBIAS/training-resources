- Open Google Chrome on BAND (for some reason vizarr does not work with Firefox on BAND).
Google Chrome can be found under the Applications menu at the top left corner of the screen: \
`[Applications > internet > Google Chrome]` 

- To visualise a self-created OME-Zarr via vizarr, replace the $USER in the following link with your user name, copy-paste the link
into the Google Chrome's search bar and press enter: \
https://hms-dbmi.github.io/vizarr/?source=https://s3.embl.de/ome-zarr-course/data/ZARR/$USER/xyzct_8bit__mitosis.ome.zarr 
    - Note: you can find your user name by entering `echo $USER` in the BAND terminal.

- Optional: visualise the following in the same way:
    - 3D EM data: https://hms-dbmi.github.io/vizarr/?source=https://s3.embl.de/ome-zarr-course/data/ZARR/$USER/xyz_8bit_calibrated__fib_sem_crop.ome.zarr&viewState={%22zoom%22:2.165780801688033,%22target%22:[105.91092950205365,86.16246275029124]}
    - A well from an HCS plate: https://hms-dbmi.github.io/vizarr/?source=https://s3.embl.de/eosc-future/EUOS/testdata.zarr/A/1&viewState={%22zoom%22:-1.851458204797617,%22target%22:[1627.5,1627.5]}


Optional: practise vizarr with other self-created OME-Zarrs. 
