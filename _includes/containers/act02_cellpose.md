Now we will run a more complex container, CellPose, on your local computer. [CellPose](https://www.cellpose.org/) is a deep learning-based tool designed for robust and automated cell segmentation in microscopy images. This is the same CellPose container used on BARD. 

For mac users using podman, simply replace `docker` with `podman` in all the following commands.

**Steps**

1. Pull the container image.
    
    ```
    $ docker pull registry.git.embl.de/grp-cbbcs/abcdesktop-apps/cellpose3d
    Using default tag: latest
    c7322280ec71: Download complete 
    9266759a1867: Download complete 
    .....
    1f5da5b9ba0c: Download complete 
    registry.git.embl.de/grp-cbbcs/abcdesktop-apps/cellpose3d:latest

    ```

2. Verify the image exists.
    ```
    $ docker images
    REPOSITORY                                                  TAG                  IMAGE ID       CREATED         SIZE
    ubuntu                                                      22.10                692eb4a905c0   20 months ago   72.8MB
    registry.git.embl.de/grp-cbbcs/abcdesktop-apps/cellpose3d   latest               1f5da5b9ba0c   7 days ago      12.8GB
    ```

3. Run CellPose locally in batch mode.
    - Open a terminal and create a directory called `testimage`,e.g. `~/testimage`
    ```
    $ mkdir ~/testimage
    ```

    - Download the example image from [here](https://raw.githubusercontent.com/embl-cba/bard-containers/refs/heads/main/cellpose-nobard/MAX_pg6-3CF1_20--t1-3.jpg) and store it into `~/testimge`
    ```
    $ cd ~/testimage
    $ wget https://raw.githubusercontent.com/embl-cba/bard-containers/refs/heads/main/cellpose-nobard/MAX_pg6-3CF1_20--t1-3.jpg
    ```

    - Perform segmentation on the example image using the `cyto` model
    ```
    $ docker run -v ~/testimage:/testimage 1f5da5b9ba0c --dir /testimage --pretrained_model cyto --save_png
    ```

    - Note the `-v` flag which makes your test image on your local computer available inside container.
    - The `/testimage` after the colon is the target directory inside container. You example image will be available under this direcotry inside container.
    - The arguments after the container ID `1f5da5b9ba0c` are standard cellpose command options. You could refer to them [here](https://cellpose.readthedocs.io/en/latest/command.html)
    - After the run finished, your output images are saved in the same /testimage directory.


4. Run CellPose locally in GUI mode.
    - **Linux (Ubuntu)**
        - Configure X11 to allow local processes (including Docker containers) to access the [X server](https://en.wikipedia.org/wiki/X_Window_System) for running GUI applications.

        ```
        $ xhost +localhost
        ```
        
        Now run the CellPose GUI container:

        ```
        $ docker run -it --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix 1f5da5b9ba0c
        ```

        - Similar to the batch mode, to make data available inside the container, we use the `-v` again.
        ```
        $ docker run -it --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix -v /home/ysun/testdata:/mnt/testdata 1f5da5b9ba0c
        ```
            - `/home/ysun/testdata` is the directory on you host computer.
            - `/mnt/testdata` is the target directory in your container. Docker will automatically creates it for you.
    
    - **macOS**
        - Configure XQuartz
            - Open XQuartz from your Mac.
            - Go to Settings, on the Security tab, make sure "Allow connections from networkclients" is checked
            - In XQuartz, open a terminal (XQuartz terminal) window and run the `xhost +` command. You will see this text appear in your XQuartz terminal 
         
        >   _access control disabled, clients can connect from any host_
        
        - Run CellPose GUI.
            - In Mac Terminal (not XQuartz terminal), Set the `DISPLAY` environment variable to point to your Mac’s X11 server. This tells the container where to send the GUI output.

            ```
            $ export DISPLAY=host.docker.internal:0
            ```
                 
            - Verify the value is set correctly

            ```
            $ echo $DISPLAY
            host.docker.internal:0
            ```

            - Start CellPose container with GUI

            ```
            $ podman run -e DISPLAY=host.docker.internal:0 --rm 1f5da5b9ba0c
            ```

            - The `-e DISPLAY=host.docker.internal:0` tells the container where to send the GUI output.
            - The `--rm` flag removes the container after exit.
            - If `host.docker.internal:0` doesn’t work, try: `export DISPLAY=$(ipconfig getifaddr en0):0`