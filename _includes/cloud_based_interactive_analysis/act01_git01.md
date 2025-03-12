We will use the Galaxy's Training Infrastructure as a Service(TIaaS) in the Galaxy EU instance for this course. 

- Access the Galaxy Interactive Tool
    - Go to https://usegalaxy.eu/join-training/tim-bioimage-tools/ and join the training group. By joining the group, your Galaxy jobs are submitted to a special queue for fast execution.
    - You could also go directly go https://usegalaxy.eu without joing the group. This way your Galaxy job will be in the public queue.
    - Register an account in usegalaxy.eu .Some tools are only available for registered users. 
    - Once you get to the Galaxy main page, on the left pane from the tool menu, scroll down and click the section `Interactive tools`. Here you will find all interactive tools available in Galaxy EU.
    - You could also search for a particular tool using the search box on top.
    - Search `napari` in the search box, and click `Run napari interactive tool`
    - In the Galaxy center pane, select image from the `Image` dropdown.
    - Click `Run tool` 
    - Monitor the blue info box on the next page, which will inform you when the Interactive Tool is accessible and provide you with a link to access it.
    - If you navigate away from this page, you can view your running Interactive Tools from the Active InteractiveTools menu item in the User menu.
    - Click the click here to display link.

- Upload data to Galaxy
    - Ensure you logged in to Galaxy
    - On the `History` pane, click the `+` sign to create a new history.
    - Click `Upload` at the top of the tool panel
    - Select either `Choose local files`, `Choose remote files` or `Paste/Fetch Data`
        - `Choose local file` : use this to upload from your local computer.
        - `Choose remote files`: use this if your files are in cloud storage, such s S3. Note the cloud storage need to preconfigured in Galaxy.
        - `Paste/Fetch Data`: use this if you need to get data from URL.
    - Press Start, wait for the upload to finish, then close the window.
