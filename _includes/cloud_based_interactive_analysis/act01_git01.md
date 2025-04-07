We will use the Galaxy's Training Infrastructure as a Service(TIaaS) in the Galaxy EU instance for this course. 

- Access the Galaxy Interactive Tool
    - Go to **[https://usegalaxy.eu/join-training/tim-bioimage-tools/](https://usegalaxy.eu/join-training/tim-bioimage-tools/)** and join the training group. By joining the group, your Galaxy jobs are submitted to a special queue for fast execution.
    - You could also go directly go **[https://usegalaxy.eu](https://usegalaxy.eu)** without joing the group. This way your Galaxy job will be in the public queue.
    - Register an account in usegalaxy.eu .Some tools are only available for registered users. 
    - Once you get to the Galaxy main page, on the left pane from the tool menu, scroll down and click the section `Interactive tools`. Here you will find all interactive tools available in Galaxy EU.
    - You could also search for a particular tool using the search box on top.

- Upload image to Galaxy
    - Download an example image from **[here](https://raw.githubusercontent.com/embl-cba/bard-containers/refs/heads/main/cellpose-nobard/MAX_pg6-3CF1_20--t1-3.jpg)**
    - Ensure you logged in to Galaxy
    - On the `History` pane, click the `+` sign to create a new history.
    - Click `Upload` at the top of the tool panel of the left of your screen.
    - Select `Choose local files`, and choose the dowloaded image.
    - Press Start, wait for the upload to finish, then close the window.
    - On the right hand side of your browser, in your `History` pane, wait for the image name to turn green.


- Segmentation with CellPose Interactive tool
    - We will be using an image from Bioimage Archive AI Gallery.
    - Click `Upload` from the Galaxy tools menu.
    - Select `Paste/Fetch data` in the pop up window, paste the url **https://www.ebi.ac.uk/bioimage-archive/galleries/assets/example-images/5215c722-0e4d-58a9-a52b-478194c5bab0.png**, start the upload and close the window.
    - Click `Tools` again from the menu on the left. 
    - Search `CellPose` in the `search tools` box, and click `CellPose interactive`
    - Select the uploaded image as input to the `Images` dropdown,and click `Run Tool`,
    - Monitor the blue info box on the next page, which will inform you when the Interactive Tool is accessible and provide you with a link to access it. This could take a while.
    - If you navigate away from this page, you can view your running Interactive Tools from the `Interactive Tools` menu item in the menu of the left.
    - Click the `Open` link to display CellPose in a new browser tab.
    - Once you are in CellPose, go to `File->Load image`, navigate to `/home/cp_working_dir` and select the image.
    - Click the `run cyto3` button to start the segmentation. You can experiment with different parameters and pre-trained models using the CellPose GUI.
    <img src="{{ site.baseurl }}/figures/gxit_cellpose.png" alt="CellPose GxIT" style="display: block; margin: 2px 0;" /><br><br>

- View image with the Napari interactive tool
    - Click `Tools` from the menu on the left. 
    - Search `napari` in the `search tools` box, and click `Run Napari interactive tool`
    - In the Galaxy center pane, select the uploaded image from the `Image` dropdown, and click `Run tool` .
    - Monitor the blue info box on the next page, which will inform you when the Interactive Tool is accessible and provide you with a link to access it. This could take a while.
    - If you navigate away from this page, you can view your running Interactive Tools from the `Interactive Tools` menu item in the menu of the left.
    - Click the `Open` link to display napari in a new browser tab.
    - In the Napari window, go to `File -> Open Files`, go to the `input` folder, select the image and click open.
    - You should see your image is displayed in your Napari interactive tool.
    - To stop the Napari interactive tool, go back to the Galaxy browser tab, in your history, click the `Delete` button next to `Run Napari on data 1`.

