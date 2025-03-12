To build a batch analysis workflow in Galaxy, we will use [this tutorial](https://training.galaxyproject.org/training-material/topics/imaging/tutorials/imaging-introduction/tutorial.html). We will not repeat the steps but instead just describe the steps needed to run this workflow.

- We will use the Galaxy's Training Infrastructure as a Service(TIaaS) in the Galaxy EU instance for this course. 

- Access the Galaxy
    - Go to **[https://usegalaxy.eu/join-training/tim-bioimage-tools/](https://usegalaxy.eu/join-training/tim-bioimage-tools/)** and join the training group. By joining the group, your Galaxy jobs are submitted to a special queue for fast execution.
    - You could also go directly go https://usegalaxy.eu without joing the group. This way your Galaxy job will be in the public queue.
    - Register an account in usegalaxy.eu if you are using it.Some tools are only available for registered users. 
    - Once you get to the Galaxy main page, on the left pane is the tool menu,where you will find all tools available in Galaxy EU.
    - You could also search for a particular tool using the search box on top.
    - Follow this **[tutorial](https://training.galaxyproject.org/training-material/topics/imaging/tutorials/hela-screen-analysis/tutorial.html)** and complete all the steps in it.
 
 - Share Galaxy workflows
    - After completing all the steps in the tutorial above, you will have a workflow in Galaxy. But what if you want to share it with others to make it reusable?
        - Click `Workflow` on the left side of the Galaxy screen. All available workflows under your account are listed in the main panel.
        - Find the workflow you want to share, and click the `Share` button.
        - By default, the workflow is only accessible to the the users listed under `Share Workflow with Individual Users`.
        - To grant access to additional users, enter their email addresses in the provided text box and click `Save`. These users will then see the workflow under `Workflow shared with me` in their own accounts.
        - To generate a shareable URL that allows anyone with the link to view and import the workflow, toggle `Make Workflow accessible` at the top section.
        - If you want to make the workflow publicly available - so it appears in `Public workflows` and is searchable by anyone - toggle `Make Workflow publicly available in published workflows`.

- Import/Export Galaxy workflows
    - Currently the workflow is in the Galaxy EU instance, but what if we need to move it to another instances?
        - Log in to the Galaxy EU and click `Workflows` in the left menu.
        - Find the workflow you want to transfer.
        - Click `Download workflow in .ga format`. This will download a `.ga` file to your host computer. You can then use the file in several ways as listed below. In this exercise, will will focus on importing it to another instance.
            - **Import it to another Galaxy innstance.**
            - Upload it to [workflowhub.eu](https://workflowhub.eu)
            - Publish it to [Zenodo](https://zenodo.org) and obtain a DOI.
        - Log in to another Galaxy instance, such as [usegalaxy.org](https://usegalaxy.org)
        - Click the `Workflows` in the left menu.
        - In the top right corner of the centre pane, click `Import`.
        - If your `.ga` file has an accessible URL, paste it into `Archived Workflow URL`.
        - If your `.ga` file is stored on your computer, click `Browse` under `Archived Workflow File`, and select your file.
        - Click `Import workflow` to complete the process.
