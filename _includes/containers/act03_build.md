Once we created the Dockerfile, we can build the container image locally. For mac users, replace `docker` with `podman`. 
1. Start a terminal and enter the commands below.
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
    - For Linux users, you may see a `WARNING` after the build is finished.

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

4. Now we have the cellpose container locally, we can run it by using the steps in previous activity `Run CellPose container`.