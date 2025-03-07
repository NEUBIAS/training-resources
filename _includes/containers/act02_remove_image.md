Over time, your machine can accumulate a large number of images, some of which may be very large. To free up space, it's a good practice to remove unwanted images when they are no longer needed.

**Things to know**
- For mac users using podman, simply replace `docker` with `podman` in all the following commands.

**Steps**
1. The command `docker rmi <IMAGE ID>` is used to remove unwanted images.
    - Find the image ID using `docker images`
    - Remove the image with:
    ```
    docker rmi 692eb4a905c0
    Deleted: 692eb4a905c074054e0a35d647671f0e32ed150d15b23fd7bc745cfb2fdeddbd
    Untagged: docker.io/library/ubuntu:22.10
    ```

    - Alternatively, we can delete images by tag instead of IMAGE ID. The following achieves the same result:
    ```
    docker rmi ubuntu:22.10
    ```

2. We can also remove all unused images, meaning images that are not referenced by any container, be careful before using `-a`.
    ```
    docker image prune -a
    ```
    - Refer to [Docker Docs](https://docs.docker.com/reference/cli/docker/image/prune/) for more options for the above command.

3. A shortcut for removing **all** images from your system:
    ```
    docker rmi $(docker images -a -q)
    ```

4. To check if the images are removed, run `docker images` again. 
```
docker images
REPOSITORY                                                  TAG                  IMAGE ID       CREATED        SIZE
registry.git.embl.de/grp-cbbcs/abcdesktop-apps/cellpose3d   latest               1f5da5b9ba0c   7 days ago     12.8GB
```