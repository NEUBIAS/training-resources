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

- View image with the Napari interactive tool
    - Click `Tools` from the menu on the left. 
    - Search `napari` in the `search tools` box, and click `Run Napari interactive tool`
    - In the Galaxy center pane, select the uploaded image from the `Image` dropdown, and click `Run tool` .
    - Monitor the blue info box on the next page, which will inform you when the Interactive Tool is accessible and provide you with a link to access it. This could take a while.
    - If you navigate away from this page, you can view your running Interactive Tools from the `Interactive Tools` menu item in the menu of the left.
    - Click the link to display napari in a new browser tab.
    - In the Napari window, go to `File -> Open Files`, go to the `input` folder, select the image and click open.
    - You should see your image is displayed in your Napari interactive tool.
    - To stop the Napari interactive tool, go back to the Galaxy browser tab, in your history, click the `Delete` button next to `Run Napari on data 1`.

- Using the CellProfiler interactive tool
    - Download the [Example](https://cellprofiler-examples.s3.amazonaws.com/ExampleHuman.zip) to your host computer.
    - Extract the `ExampleHuman.zip` on your local computer. You should have the following images and `cppipe` after extraction.
        - AS_09125_050116030001_D03f00d0.tif
        - AS_09125_050116030001_D03f00d1.tif
        - AS_09125_050116030001_D03f00d2.tif
        - ExampleHuman.cppipe
    - Upload the above files to Galaxy. (Refer to `Upload image to Galaxy` for details)
    - Click `Tools` in the left menu. 
    - Search for `CellProfiler` in the `search tools` box, and click `Run CellProfiler interactive tool`.
    - In the Galaxy center pane, select all the three uploaded images from the `Image` dropdown.
    - Choose `Modify an existing project`, then select `ExampleHuman.cppipe` from the dropdown list.
    - Click `Run Tool` and monitor the blue info box on the next page for a link to access the Interactive Tool. This could take some time.
    - If you navigate away, you can find your running Interactive Tools in the `Interactive Tools` menu on the left.
    - Click the `Open` link to display CellProfiler in a new browser tab. Ignore and close the warnings.
    - In CellProfiler, go to `File -> Import -> Pipeline from File`, navigate to `/home/output` , select the `ExampleHuman.cppipe` file and click `Open`.
    - Right-click the area `Drop files and folders here`, and select `Browse For Images`, go to `/home/input` folder, select all three images and click `Open`.
    - Click `Start test Mode` to test the process, you should see the results displayed on your browser.
    - Close the browser tab when finished, to return to the Galaxy main panel.
