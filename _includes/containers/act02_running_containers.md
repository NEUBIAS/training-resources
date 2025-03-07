Once we have downloaded the images, we can run a container from them,using the Ubuntu image as an example.

**Things to know**
- For mac users using podman, simply replace `docker` with `podman` in all the following commands.

**Steps**
1. Run the container

    ```
    $ docker run ubuntu:22.10 /bin/echo 'Hello world!'
    Unable to find image 'ubuntu:22.10' locally
    3ad6ea492c35: Download complete 
    692eb4a905c0: Download complete 
    Hello world!
    ```

    - The `/bin/echo` command is a simple application that prints whatever input is provided to the terminal.When we passed `Hello world!`, it prints `Hello world!` to the terminal.
    - When you run the `docker run` command, Docker/Podman creates a new container from the specified image and then runs the given command inside that container. 
    - Note that when you run `docker run`, Docker/Podman first checks if the specified image exists locally. If the image is not found (as displayed in the output above), it automatically pulls it from Docker Hub(or another configured registry) before creating the container.
    - Since we previously removed the `ubuntu:22.10` image, running `docker run` will automatically download the image from Docker Hub again.

2. To check which containers are currently running after executing the previous command
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

3. During development, if a container is stopped, we often need to inspect and debug what went wrong. To do this, we can run the container interactively with a shell session. To start a container interactively:
    ```
    docker run -it ubuntu:22.10 /bin/bash
    root@cfb8305b8b00:/#
    ```
    - The `-it` enables Docker start a container in interactive mode.
    - This will you a interactive [BASH](https://tiswww.case.edu/php/chet/bash/bashtop.html) session inside the Ubuntu container. 
    - By default, you are running as `root`  user inside the container.
    - You can now use this like a normal Linux shell. Try `pwd` and `ls` to look at the file system.

4. By default, your terminal session remains attached to the container when you run `docker run`. If you don't want to remain attached, you can run the container in detached mode using the `-d` flag.
    ```
    $ docker run -d ubuntu:22.10 /bin/sleep 3600
    be730b8c554b69383f30f71222b9ac264367c7454790dc2a4eb0cda33c0baa2a
    ```

    - By adding the `-d` flag, the container will continue to run as long as the command is active, but it won't print output to the terminal. The above command will run the container idly for 1 hour:

    - If we check the container again, we can see it's running the `/bin/sleep` command.

    ```
    $ docker ps
    CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
    cfb8305b8b00        ubuntu:22.10      "/bin/sleep 3600"    41 seconds ago      Up 40 seconds                           jovial_goldstine
    ```

5. Now that the container is running in the background, what if we want to reattach to it?

    ```
    $ docker exec -it cfb /bin/bash
    root@cfb8305b8b00:/#
    ```

   - Note that we only used the first 3 characters as the container ID when referencing it. Docker allows you to use a partial container ID, as long as it is unique among running containers.
   - The container ID appearing at the front of the BASH prompt indicates that you're inside the running container.
   - Once inside a session, we can interact with the container like any SSH session again.

6. To stop the container immediately instead of waiting for 1 hour, we can use either `docker stop` or `docker kill`. The prior is a graceful stop, while the latter is a forceful stop.

    ```
    docker stop cfb8305b8b00
    cfb8305b8b00
    ```

    Then checking with `docker ps -a `

    ```
    docker ps -a
    CONTAINER ID   IMAGE                          COMMAND                  CREATED              STATUS                          PORTS     NAMES
    cfb8305b8b00   ubuntu:22.10                   "/bin/sleep 3600"        About a minute ago   Exited (137) 29 seconds ago               nostalgic_bose

    ```
    We can see that the container exited with code [137](https://medium.com/javarevisited/understanding-and-resolving-docker-exit-code-73ff617230cf), which indicates that the process was terminated.