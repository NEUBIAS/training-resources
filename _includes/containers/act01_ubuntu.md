You can install Docker Engine using different methods. This guide provides step-by-step instructions for installing Docker from Docker's APT repository. For alternative installation methods, refer to the [official Docker documentation](https://docs.docker.com/engine/install/ubuntu/)
- Set up Docker's APT repository
    ```
    $ sudo apt-get update
    $ sudo apt-get install ca-certificates curl
    $ sudo install -m 0755 -d /etc/apt/keyrings
    $ sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
    $ sudo chmod a+r /etc/apt/keyrings/docker.asc
    ```
- Add the repository to apt sources
    ```
    $ echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo "$VERSION_CODENAME") stable"
    $ sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    $ sudo apt-get update
    ```
    **Note**: If you use an Ubuntu derivative distribution, such as Linux Mint, you may need to use UBUNTU_CODENAME instead of VERSION_CODENAME.
- Install the latest Docker packages
    ```
    $ sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
    ```
- Verify that the installation is successful by running the ```hello-world``` image:
    ```
    $ sudo docker run hello-world
    ```
    This command downloads a test image and runs it in a container. When the container runs, it prints a confirmation message and exits.