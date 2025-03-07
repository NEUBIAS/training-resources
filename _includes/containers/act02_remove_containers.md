After working with Docker containers, you might want to delete old, obsolete ones. In this exercise, we will show you how to do these tasks.

**Things to know**
- For mac users using podman, simply replace `docker` with `podman` in all the following commands.

**Steps**
1. Check old, exited or obsolete containers.
    ```
    docker ps -a
    CONTAINER ID   IMAGE                 COMMAND                  CREATED       STATUS                           PORTS   NAMES
    cfb8305b8b00   ubuntu:22.10          "/bin/sleep 3600"        2 hours ago   Exited (137) About an hour ago             nostalgic_bose
    ```
    From the output above, we can see that we have a container hanging around with status **Exited**.
    
2. To remove this container, we use the `docker rm` command.
    ```
    docker rm cfb8305b8b00
    ```

3. Typically, containers has these status: **Created, Restarting, Running, Removing, Paused, Exited, or Dead**. We use the `--filter` flag in `docker ps -a` command to list containers by their status.
    ```
    docker ps -a --filter "status=Exited"
    ```
    
    This lists all **Exited** containers. To remove them at once
    ```
    docker rm $(docker ps -aq --filter "status=dead")
    ```

    The `--filter` flag can be specified multiple times

    ```
    docker rm $(docker ps -aq --filter "status=Exited" --filter "status=Dead")
    ```

4. To make this even simpler, i.e. to remove all stopped containers.
    ```
    docker container prune -f
    ```
    - This will remove all stopped containers.
    - The `-f` flag forces removal without a confirmation prompt.
    - This command does not remove running containers.

5. But what if we want to remove everything, including the running containers?
    ```
    docker rm -f $(docker ps -aq)
    ```
    This force-deletes all containers, even those are still running.