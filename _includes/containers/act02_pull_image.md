**Things to know**
- For mac users using podman, simply replace `docker` with `podman` in all the following commands.

**Steps**

To run containers localy, we'll first need to pull some images to local computer.
1. Start a terminal.
2. On a fresh Docker(Podman) installation, we should have no images. To verify, we run `docker images` (`podman images` for mac users):

    ```
    $ docker images
    REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
    ```

3. Let's pull an image. By default, Docker and Podman retrieve images from [Docker Hub](https://hub.docker.com), You can pull images directly from Docker Hub using their tags. These commands follow the format:

    ```
    # Official Docker images 
    <repo>:<tag> 
    # ubuntu:22.10
    ```

    To pull `ubuntu 22.10` image from Docker Hub
    ```
    docker pull ubuntu:22.10
    ```

    We can also pull images from a private registry by specifying the full URL. For example, to pull the CellPose3D image from our [container registry at EMBL](https://registry.git.embl.de/grp-cbbcs/abcdesktop-apps/cellpose3d). 
    
    ```
    docker pull registry.git.embl.de/grp-cbbcs/abcdesktop-apps/cellpose3d
    Using default tag: latest
    c7322280ec71: Download complete 
    9266759a1867: Download complete 
    .....
    1f5da5b9ba0c: Download complete 
    registry.git.embl.de/grp-cbbcs/abcdesktop-apps/cellpose3d:latest

    ```

    Then when we run `docker images`, we should get:

    ```
    docker images
    REPOSITORY                                                  TAG                  IMAGE ID       CREATED         SIZE
    ubuntu                                                      22.10                692eb4a905c0   20 months ago   72.8MB
    registry.git.embl.de/grp-cbbcs/abcdesktop-apps/cellpose3d   latest               1f5da5b9ba0c   7 days ago      12.8GB
    ```
