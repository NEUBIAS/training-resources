<h4 id="act01_ref"><a href="#act01_ref">Stitch tiles</a></h4>
Download the compressed image tiles [xyc_16bit__hoechst_phalloidin_tiles.zip](https://github.com/NEUBIAS/training-resources/raw/master/image_data/shading_tiling/xyc_16bit__hoechst_phalloidin_tiles.zip). The images are ordered in a regular pattern left-right, top-down (snake), we will estimate the overlap by trial and error (simulating the case where some metadata is lost). Starting with the correct value of overlap is important to get the best optimal alignment. Stitching errors are better observed when the fusion method uses a maximum or minimum. 

 - Perform a stitching by using an overlap of 5%, 10%, and 15%, use maximum blending option. Do not compute the overlap.
 - Inspect the images, inp particular at the overlap between tiles, and notice that some of the overlaps gives better, but not perfect, results
 - Perform a stitching using the optimal overlap and allow for compute overlap. This will optimize the overlap for every tile pair
 - Try different options for the blending of the tiles


