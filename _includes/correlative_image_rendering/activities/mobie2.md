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

- open the EM data in Fiji
- add the volume to MoBIE under the selection group "EM" (make new selection group) to the same dataset. The format conversion can take a couple of minutes.