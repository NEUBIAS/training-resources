<h4 id="spots"><a href="#spots">Build your own container</a></h4>
In this activity, we will demonstrate how to build our own container and test it locally. 

**Things to know**
- We will use CellPose as an example. The Dockerfile for CellPose has already been prepared and can be found [here](https://github.com/embl-cba/bard-containers/blob/main/cellpose-nobard/Dockerfile).
- We will iteratively add necessary statements to construct a valid and functional Dockerfile for the CellPose tool.
- For mac users, since docker is fully compatible with podman, you can use podman with Dockerfile. 

**Steps**
1. Open the [Dockerfile](https://github.com/embl-cba/bard-containers/blob/main/cellpose-nobard/Dockerfile)
    - The first line starts from a base image. The keyword `FROM` tells Docker Engine where to look for the base image, and it must be the first instruction in a Dockerfile.
    ```
    FROM abcdesktopio/oc.template.ubuntu.22.04:3.2
    ```
    
    - By default, Docker looks for the image from Docker Hub. If you would like to use other base image that in other registry, you will need to specify the full URL. `<REGISTRY_URL>:<IMAGE_TAG>` For example,
    ```
    FROM registry.git.embl.de/grp-cbbcs/abcdesktop-apps/base-image:ubuntu22-cuda-11-8
    ```
    
    - For Mac users using Podman, you will need to use the full URL, i.e. append `docker.io` at the begining.
    ```
    FROM docker.io/abcdesktopio/oc.template.ubuntu.22.04:3.2
    ```

    - The `RUN` statements in the Dockerfile executes commands inside the container at build time. It often used for installing dependencies.
        ```
        RUN apt update -y && apt install -y curl
        ```

        This updates the package list and installs `curl`.

    - The `ENV` sets environemnt variables inside the container. These variables persist at runtime.
        ```
        ENV NVIDIA_DRIVER_CAPABILITIES "compute,utility"
        ```

        This sets the NVIDIA GPU capabilities inside the container.
    
    - The `WORKDIR` sets the working directory inside the container. All subsequent commands run from this directory.
        ```
        WORKDIR /tmp
        ```

        Now, any commands will execute inside /tmp in the container.
    
    - The `ENTRYPOINT` specifies the default command to run when container starts. It executes at runtime.
        ```
        ENTRYPOINT ["/opt/conda/envs/cellpose/bin/python3","-m","cellpose" ]
        ```

        This runs the python3 command inside the container to start the cellpose module.

    - The `USER` sets the user under which the container runs. By default, if no `USER` is specified in Dockerfile, the container runs as `root`. Note that running as `root` is risky, but sometimes required.

2. The statements in Dockerfile are translated from the [instructions](https://github.com/MouseLand/cellpose?tab=readme-ov-file) for installing CellPose.
3. Finally, we have a recipe for CellPose.


