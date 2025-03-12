For mac users using podman, simply replace `docker` with `podman` in all the following commands.

**Steps**

To run containers localy, we'll first need to pull some images to local computer.
1. Start a terminal.On a fresh Docker(Podman) installation, we should have no images. To verify, we run `docker images` (`podman images` for mac users):

    ```
    $ docker images
    REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
    ```

2. Let's pull an image. By default, Docker and Podman retrieve images from [Docker Hub](https://hub.docker.com). You can see all the containers available in Dockerhub by going to its website. 

3. Go to **[https://hub.docker.com](https://hub.docker.com)** and search for `ubuntu`. You should see `ubuntu` appear at the top of the results. Click on it, by default, you will be redirected to the `Overview` page. Click `Tags` to see its available tags. Search `22.10` in `Filter tags` box.

4. To pull `ubuntu 22.10` image from Docker Hub
    ```
    docker pull ubuntu:22.10
    ```

5. Once we pull the image, we can run a container from it.
    ```
    $ docker run ubuntu:22.10 /bin/echo 'Hello world!'
    3ad6ea492c35: Download complete 
    692eb4a905c0: Download complete 
    Hello world!
    ```

    - The `/bin/echo` command is a simple application that prints whatever input is provided to the terminal.When we passed `Hello world!`, it prints `Hello world!` to the terminal.
    - When you run the `docker run` command, Docker/Podman creates a new container from the specified image and then runs the given command inside that container. 
    - Note that when you run `docker run`, Docker/Podman first checks if the specified image exists locally. If the image is not found, it automatically pulls it from Docker Hub(or another configured registry) before creating the container.

6. To check which containers are currently running after executing the previous command
    ```
    $ docker ps
    CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
    ```

    - No containers shown because the `docker ps` command  only lists running containers by default. 
    - To see all containers, including stopped ones, use the `-a` flag.
    
    ```
    docker ps -a
    CONTAINER ID   IMAGE                          COMMAND                  CREATED         STATUS                     PORTS     NAMES
    eb35afb7e7e0   ubuntu:22.10                   "/bin/echo Hello wor…"   4 minutes ago   Exited (0) 4 minutes ago           pedantic_proskuriakova
    ```
    - Our container shows the status **Exited**. 
    - Docker containers only run as long as the command it starts is running. Once the command completes or exits, the container stops automatically.
    - In our example, the container ran `/bin/echo` successfully, printed the output, and then exited with status code 0 (indicating no errors). Since Docker only run as long as their primary command is active, Docker stopped the container as soon as the command completed.

7. During development, if a container is stopped, we often need to inspect and debug what went wrong. To do this, we can run the container interactively with a shell session. To start a container interactively:
    ```
    docker run -it ubuntu:22.10 /bin/bash
    root@cfb8305b8b00:/#
    ```
    - The `-it` enables Docker start a container in interactive mode.
    - This will you a interactive [BASH](https://tiswww.case.edu/php/chet/bash/bashtop.html) session inside the Ubuntu container. 
    - By default, you are running as `root`  user inside the container.
    - You can now use this like a normal Linux shell. Try `pwd` and `ls` to look at the file system.

8. Exit the container by pressing `Ctrl+D`, then we are on our host terminal again.

9. To remove this container, we use the `docker rm` command.
    ```
    docker rm eb35afb7e7e0
    ```
    
10. We have removed the container, but the container image still exist on our computer. To free up space, it's a good practice to remove unwanted images. The command `docker rmi <IMAGE ID>` is used to remove unwanted images.

    - Find the image ID using `docker images` and remove the image with:
    ```
    docker rmi 692eb4a905c0
    Deleted: 692eb4a905c074054e0a35d647671f0e32ed150d15b23fd7bc745cfb2fdeddbd
    Untagged: docker.io/library/ubuntu:22.10
    ```

    - Alternatively, we can delete images by tag instead of IMAGE ID. The following achieves the same result:
    ```
    docker rmi ubuntu:22.10
    ```

    - If you see error about image is being used by container, add the `-f` flag to the `docker rmi <IMAGE ID>` command.
    - We can also remove all unused images, meaning images that are not referenced by any container, be careful before using `-a`.
    ```
    docker image prune -a
    ```
    - Refer to [Docker Docs](https://docs.docker.com/reference/cli/docker/image/prune/) for more options for the above command.

