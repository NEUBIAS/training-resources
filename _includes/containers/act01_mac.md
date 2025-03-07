**Things to know**
- The instructions have been tested on macOS Sequoia and should also work on Ventura and later versions.
- To work with Docker on macOS, we recommend installing [Podman Desktop](https://podman.io).Podman Desktop provides a graphical interface for managing containers, offering an easy way to build, run, and control them. It is fully Docker-compatible and runs containers in a rootless, daemonless environment, enhancing security.
- Alternatively, you can use [Docker Desktop](https://www.docker.com/products/docker-desktop/) but mindful of its license agreement.
- Since macOS lacks native [X Window System,Version 11 (X11)](https://en.wikipedia.org/wiki/X_Window_System) support, which is required for running GUI applications inside containers, you will need to install [XQuartz](https://www.xquartz.org/) - an X11 server for macOS that enables GUI applications from containers to display properly.

**Install Podman Desktop**

- Download Podman Desktop from [podman.io](https://podman.io/docs/installation)
- You can also install podman via `brew` in terminal
    ```
    brew install podman
    ```

- After installation, create and start your first Podman machine.
    - **Option 1**: Follow the instructions on the prompt window to init and start your podman machine.
    - **Option 2**: In a terminal, type
    ```
    podman machine init
    podman machine start
    ```

- Verify the installation information using:
    ```
    podman info
    ```

- Once the Podman machine is started, you should see its status as `Running` in the Podman Desktop GUI interface.
- On the left-hand side of the Podman Desktop GUI, you can explore `Images`, `Containers`, `Volumes`, and `Pods` currently available on your host machine.

**Install XQuartz**
- **Option 1:** Install via XQuartz official website
    - Download XQuartz .pkg file from [here](https://xquartz.org)
    - Once downloaded the package, install it by double clicking the pkg file, and follow the instructions on-screen to complete the installation.
        - Introduction: `Continue`
        - Read Me: `Continue`
        - License: `Continue`
        - Installation Type: `Install`
            - Username: Enter your name
            - Password: Enter your password
        - Summary: Once installation was successful, click `Close`
        - Reboot your Mac
- **Option 2**: Install via brew command
    - Install Homebrew using the instruction from [brew.sh](https://brew.sh/)
    - Start a `Terminal` on your Mac, and type the below command
        ```
        brew install --cask xquartz
        ```

        - The flag `--cask` is used to install GUI applications on macOS that are distributed as `.dmg`, `.pkg` or `.app` bundles.
        - You should see `xquartz was successfully installed!` after installation finishes.
    - Reboot your Mac.        