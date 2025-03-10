To build a batch analysis workflow in Galaxy, we will use [this tutorial](https://training.galaxyproject.org/training-material/topics/imaging/tutorials/imaging-introduction/tutorial.html). We will not repeat the steps but instead just describe the steps needed to run this workflow.

- We will use the Galaxy's Training Infrastructure as a Service(TIaaS) in the Galaxy EU instance for this course. 

- Access the Galaxy
    - Go to **[https://usegalaxy.eu/join-training/tim-bioimage-tools/](https://usegalaxy.eu/join-training/tim-bioimage-tools/)** and join the training group. By joining the group, your Galaxy jobs are submitted to a special queue for fast execution.
    - You could also go directly go https://usegalaxy.eu without joing the group. This way your Galaxy job will be in the public queue.
    - Register an account in usegalaxy.eu if you are using it.Some tools are only available for registered users. 
    - Once you get to the Galaxy main page, on the left pane is the tool menu,where you will find all tools available in Galaxy EU.
    - You could also search for a particular tool using the search box on top.
    - Follow this **[tutorial](https://training.galaxyproject.org/training-material/topics/imaging/tutorials/imaging-introduction/tutorial.html/)** and complete all the steps in it.
    - After completing all the steps in the tutorial, we will extract the workflow from our Galaxy history. 
        - Click `History Option` on the top right corner of your history.
        - Select `Extract workflow`, tick all the steps in the main panel, and click `Create workflow`.
        - When the workflow is created, click `run` workflow. This will automatically run all of the previous steps.

- Upload data to Galaxy
    - Ensure you logged in to Galaxy
    - On the `History` pane, click the `+` sign to create a new history.
    - Click `Upload` at the top of the tool panel
    - Select either `Choose local files`, `Choose remote files` or `Paste/Fetch Data`
        - `Choose local file` : use this to upload from your local computer.
        - `Choose remote files`: use this if your files are in cloud storage, such s S3. Note the cloud storage need to preconfigured in Galaxy.
        - `Paste/Fetch Data`: use this if you need to get data from URL.
    - Press Start, wait for the upload to finish, then close the window.