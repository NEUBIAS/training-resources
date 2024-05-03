**Requirements:** Fiji with MoBIE update site

- retreive the original data

  EM: https://www.ebi.ac.uk/empiar/EMPIAR-11537/ (Downscaled (20nm) aligned FIB SEM stack resliced to match the Airyscan dataset)

  LM: https://www.ebi.ac.uk/biostudies/files/S-BSST1075/EM04480_05_4G_Hoechst_GFP-TGN46_agglutinin_mitotracker.czi


- open the LM data in Fiji using the BioFormats Importer plugin
- Currently, the MoBIE project creator only supports single channels, so split the fluorescence stack into separate channels using `Image > Hyperstacks > Make Subset...` and choose the channel number. Do this with each of the 4 channels active.

- create a new MoBIE project: `Plugins > MoBIE > Create > Create New MoBIE project...`

  name the project as you like and create it in a local directory.
- add a new dataset, name it as you like
- select the first channel image in Fiji
- add a new source `current displayed image`, do not tick `make view exclusive`
- call it appropriately (channels are sorted inverse) and choose the `selection group name` as "fluorescence" or "FM"
- open the MoBIE project to see how the scaling and LUT are transferred 

- open the other channel views using the MoBIE UI and explore the multi-channel volume
- right click into the multi-channel viewer and `Save current view`
- `Save as new view`, save to `projcect`
- Call the view something like "all channels" and make it part of the "FM" group
- close MoBIE

- open the EM data in Fiji
- add the volume to MoBIE under the selection group "EM" (make new selection group) to the same dataset. The format conversion can take a couple of minutes.
- open the MoBIE project and view your multichannel FM and EM together
- switch off all fluorescence channels but the Hoechst by clicking on `S`
- change contrast and transparency settings for the relevant sources (`B`)

![multiview.png](../../../figures/correlative_image_rendering/multiview.png)


- right click the image "registration manual", select the EM image as we want to keep the multi-channles where they are, `Start manual transform` drag the image around.
- click `cancel manual Transform` to undo the translation and bring the image back to its original position.

- use the mouse wheel to translate in `z`, make sure rotations are around the viewing axis and press the `z` key. Use the right and left arrow keys to rotate and the up and down to scale (dangerous)
- click `Accept manual Transform` to make it permanent and store the view into the project. This will only save the transformed EM source. Create a new selection group "Registration"