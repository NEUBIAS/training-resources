1. Once we created the Dockerfile, we can build the container image locally. Start a terminal and enter the commands below.

    ```
    podman build -t cellpose:01 .
    ```

    - The flag `-t` specifies the image tag. The above command must run in the same directory where Dockerfile resides. Note the `.` is important.
    - If Dockerfile is located at a different directory. use the `-f` flag to specify the location.
    - By default, docker recipe is named `Dockerfile`, but it can be named differently. 

    ```
    podman build -t cellpose:01 -f /home/ballonn/cellpose_recipe.d
    ```
    
2. Verify the image exists locally.

    ```
    podman images
    REPOSITORY                       TAG                  IMAGE ID       CREATED          SIZE
    moby/buildkit                    buildx-stable-1      f210b5f94e18   13 days ago      209MB
    cellpose                         01                   9055a7c1a1ef  51 minutes ago  12.7 GB
    ```

3. Test the container locally.

    - **Test in batch mode.**

    ```
    podman run --rm cellpose:01 --help
    ```

    - You should see the Help contents displayed on your terminal. 
    - This is to test CellPose in batch mode. You could specify any CellPose argument here.
    - By default, if we don't specify any argument, i.e. just to run `podman run --rm cellpose:01` , the CellPose GUI starts, however, it requires extra configuration which we will do in the next step.


    - **Test in GUI mode.**
        - Configure XQuartz
            1. Open XQuartz from your Mac.
            2. Go to Settings, on the Security tab, make sure "Allow connections from networkclients" is checked
            3. In XQuartz, open a terminal (XQuartz terminal) window and run the below command
            
        ```
        xhost +
        ```

        You will see this text appear in your XQuartz terminal 
         
        ```
        access control disabled, clients can connect from any host
        ```

        - Run CellPose GUI.
            1. In Mac Terminal (not XQuartz terminal), Set the `DISPLAY` environment variable to point to your Mac’s X11 server. This tells the container where to send the GUI output.

            ```
            export DISPLAY=host.docker.internal:0
            ```
                 
            2. Verify the value is set correctly

            ```
            echo $DISPLAY
            host.docker.internal:0
            ```

            3. Start CellPose

            ```
            podman run -e DISPLAY=host.docker.internal:0 --rm cellpose:01
            ```

            - The `-e DISPLAY=host.docker.internal:0` tells the container where to send the GUI output.
            - The `--rm` flag removes the container after exit.
            - If `host.docker.internal:0` doesn’t work, try: `export DISPLAY=$(ipconfig getifaddr en0):0`


4. Making data available inside container. 
   We will use the `-v` flag in the `podman run` command, which mounts directory to container. We will use this flag to make data available inside container. 
    - Create a directory on you host computer, you may use your own directory.
        
    ```
    mkdir /home/ysun/testdata
    ```

    - Download test images into the directory
    - Mount the directory and run CellPose again
        
    ```
    podman run -e DISPLAY=host.docker.internal:0 --rm -v /home/ysun/testdata:/mnt/testdata cellpose:01
    ```

    - `/home/ysun/testdata` is the directory on you host computer.
    - `/mnt/testdata` is the target directory in your container. Docker will automatically creates it for you.