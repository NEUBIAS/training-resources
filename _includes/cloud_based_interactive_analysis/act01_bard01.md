We will use the BARD desktop EMBL instance.

- Access the BARD Desktop
    - Go to the [BARD](https://bard-external.embl.de)
    - Click `Connect with EMBL Guest Account`.
        - You will be given login details beforehand.
        - Username is `trainingXX`, replace XX with your own number.
        - Default password is `tim2025`.
    - After successful log in, you should see your desktop in your browser.
        - At the bottom of your desktop is the application dock. We keep multiple versions of software on BARD, but only the latest is shown in this dock.
        - To access older versions, click the application menu on the top right corner. `Application -> Development`
        - Each application is in its own container and independent of each other.
        - All applications start as the current logged-in user.
        - Your home directory is shared among all containers, which means if you need data accessible for all applications, you will need to store them in your own home folder.

- Segmentation using CellPose on BARD
    - Start Firefox from the bottom dock on your BARD desktop.
    - Go to the [Bioimage archive AI Gallery](https://www.ebi.ac.uk/bioimage-archive/galleries/ai-galleries/) and click on `Analysed datasets`.
    - Select the first dataset `S-BIAD1026`, and scroll down to the `Model predictions` section.
    - For illustration purpose, we will download the first image for 2D nucleus segmentation task. 
    - Click `Download` under the `Original image` to download it. The image will be saved in /home/YOURNAME/Downloads
    - Click `CellPose 1.1.1.1 (2D)` to launch CellPose in 2D mode. A `konsole` terminal will open first,keep it open for logs and debugging.
    - In the CellPose window, go to `File -> Load image`, and select the downloaded image `5215c722-0e4d-58a9-a52b-478194c5bab0.png`.
    - Click the `run cyto3` button to start the segmentation. You can experiment with different parameters and pre-trained models using the CellPose GUI.
  
