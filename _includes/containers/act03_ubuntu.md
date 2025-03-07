1. Once we created the Dockerfile, we can build the container image locally. Start a terminal and enter the commands below.
    ```
    docker build -t cellpose:01 .
    ```

    - The `-t` flag specifies the image tag, allowing you to name and version the built image.
    - The command must run in the same directory where Dockerfile is located. The **.** at the end of the command is important as it tells Docker to use the current directory as the build context.
    - If Dockerfile is located at a different directory, use the `-f` flag to specify its path.
    - By default, the Docker recipe is named Dockerfile, but you can name it differently and specify the custom name when building the image using the `-f` flag. 

        ```
        docker build -t cellpose:01 -f /home/ballonn/cellpose_recipe.d
        
        ```
    where `/home/ballonn/cellpose_recipe.d` is the path to the Docker recipe.
    - You may see a `WARNING` after the build is finished.

        ```
        WARNING: No output specified with docker-container driver. Build result will only remain in the build cache. To push result image into registry use --push or to load image into docker use --load 
        ```

        This is caused by [BuildKit](https://docs.docker.com/build/buildkit/). For newer Docker version, BuildKit is enabled by default. The build result is stored only in the cache, meaning it won’t be available as a usable image unless explicitly saved. 
        Now we load the image from cache to local machine:

        ```
        docker buildx build --load -t cellpose:01 .
        ```


2. Verify the image exists locally.

    ```
    docker images
    REPOSITORY                       TAG                  IMAGE ID       CREATED          SIZE
    moby/buildkit                    buildx-stable-1      f210b5f94e18   13 days ago      209MB
    cellpose                         01                   9055a7c1a1ef  51 minutes ago  12.7 GB
    ```

3. Test the container locally.

    - Test in batch mode.

        ```
        docker run --rm cellpose:01 --help
        ```

        - You should see the `Help` contents displayed on your terminal. 
        - This command runs CellPose in batch mode. You could specify any CellPose argument here.
        - By default, if we don't specify any argument, i.e. just to run `docker run --rm cellpose:01` , the CellPose GUI starts, however, it requires extra configurations which we will do in the next step.


    - Test in GUI mode.
        - Configure X11 to allow local processes (including Docker containers) to access the [X server](https://en.wikipedia.org/wiki/X_Window_System) for running GUI applications.

        ```
        xhost +localhost
        ```
        
        Now run the container:

        ```
        docker run -it --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix cellpose:01
        ```

        The CellPose GUI should start.

4. Making data available inside the container. 
   You may noticed the `-v` flag in the previous command, which mounts the directory /tmp/.X11-unix to container. We will use this flag to make data available inside container. 
    - Create a directory on you host computer, you may use your own directory.
        
        ```
        mkdir /home/ysun/testdata
        ```

    - Download test images into the directory
    - Mount the directory and run CellPose again
        
        ```
        docker run -it --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix -v /home/ysun/testdata:/mnt/testdata cellpose:01
        ```

        - `/home/ysun/testdata` is the directory on you host computer.
        - `/mnt/testdata` is the target directory in your container. Docker will automatically creates it for you.