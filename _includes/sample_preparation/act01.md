<h4 id="sample_prep"><a href="#sample_prep">Asses sample preparation</a></h4>

Compare different fixation protocols with respect to integrity of the structure and dimensions of the structure. Use orthogonal views if necessary. All samples have been stained for DNA (Hoechst, 405 excitation), Microtubules (primary and secondary antibody, 488nm excitation), Actin (Phalloidin, 561 nm excitation). 
1. Methanol fixation [xyzc_16bit__DNA_MT_actin_methanol.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/sample_preparation/xyzc_16bit__DNA_MT_actin_methanol.tif)
2. Formaldehyde fixation [xyzc_16bit__DNA_MT_actin_FA.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/sample_preparation/xyzc_16bit__DNA_MT_actin_FA.tif)
3. Formaldehyde and Glutaraldehyde fixation [xyzc_16bit__DNA_MT_actin_FA_GA.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/sample_preparation/xyzc_16bit__DNA_MT_actin_FA_GA.tif)

    > ## What you expect to see
    >   1. Methanol fixation 
    >    - Observation: Good staining of channel 1 (DNA), good staining in channel 2 (MTs) with nearly no background, no clear staining in channel 3 (actin). Along Z one can observe that the cell is flattened compared to the other protocols
    >   - Explanation: Alcohols (like ethanol and methanol) are coagulant fixatives that preserve cells by dehydrating them and precipitating proteins. This causes a collapse of the cell that is visible by comparing the nuclei along Z for the different protocols. Phalloidin only binds to the native structure of actin filaments and alcohols dissolve F-actin, therefore no actin labelling is visible
    >
    >   2. Formaldehye fixation
    >    - Observation: Good staining of channel 1 (DNA), MTs appear disturbed and broken, good staining of actin
    >    - Explanation: In this sample the fixation via formaldehyde may have been too slow causing a deoplymerization of MTs. This image shows an extreme example, typically the disruption of MTs is much more subtle. 
    >
    >    3. Formaldehye and Glutaraldehyde fixation
    >    - Observation: All 3 structures look as expected. There seems to be more cytoplasmic background in the MTs channel than for the other fixation protocols. 
    >    - Explanation: This protocol uses a small amount of Glutaraldehyde, a fixative also used in electron microscopy. GA crosslinks proteins faster (2-aldehydes groups) and so better fixes structures before they disassemble. It can create more autofluorescence with insufficient quenching. This may explain the observed background in the MTs channel. 
    {: .solution}
