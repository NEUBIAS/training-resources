1. Open the [Dockerfile](https://git.embl.de/grp-cbbcs/abcdesktop-apps/-/blob/main/cellpose3d/Dockerfile?ref_type=heads)
    - The first 2 lines starts from a base image. The keyword `FROM` tells Docker Engine where to look for the base image, and it must be the first instruction in a Dockerfile.
    ```
    ARG TAG=3.2
    FROM abcdesktopio/oc.template.ubuntu.22.04:$TAG
    ```
    
    - For Mac users using Podman, you will need to use the full URL, i.e. append `docker.io` at the begining.
    ```
    FROM docker.io/abcdesktopio/oc.template.ubuntu.22.04:$TAG
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
    
    - The `CMD` specifies the default command to run when container starts. It executes at runtime.
        ```
        CMD ["/composer/appli-docker-entrypoint.sh" ]
        ```

        This runs the script inside the container to start the cellpose module.

    - The `USER` sets the user under which the container runs. By default, if no `USER` is specified in Dockerfile, the container runs as `root`. Note that running as `root` is risky, but sometimes required.

2. The statements in Dockerfile are translated from the [instructions](https://github.com/MouseLand/cellpose?tab=readme-ov-file) for installing CellPose.
3. Finally, we have a recipe for CellPose.