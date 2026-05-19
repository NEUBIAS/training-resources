1. Open the [Dockerfile](https://git.embl.de/grp-cbbcs/abcdesktop-apps/-/blob/main/cellpose3d/Dockerfile?ref_type=heads)
    - The first 2 lines starts from a base image. The keyword `FROM` tells Docker Engine where to look for the base image, and it must be the first instruction in a Dockerfile.
    
   > _ARG TAG=3.2_
   >
   > _FROM abcdesktopio/oc.template.ubuntu.22.04:$TAG_
    
    - For Mac users using Podman, you will need to use the full URL, i.e. append `docker.io` at the begining.
    
    > _FROM docker.io/abcdesktopio/oc.template.ubuntu.22.04:$TAG_
    

    - The `RUN` statements in the Dockerfile executes commands inside the container at build time. It often used for installing dependencies.For example, the below statement updates the package list and installs `curl`.
    
    > _RUN apt update -y && apt install -y curl_
    

    - The `ENV` sets environemnt variables inside the container. These variables persist at runtime. For example, the below statement sets the NVIDIA GPU capabilities inside the container.
     
    > _ENV NVIDIA_DRIVER_CAPABILITIES "compute,utility"_
     

    
    - The `WORKDIR` sets the working directory inside the container. All subsequent commands run from this directory.
    
    > _WORKDIR /tmp_
        
    
    - The `CMD` specifies the default command to run when container starts. It executes at runtime. For example, the below statement runs the script inside the container to start the cellpose module.
       
    >  _CMD ["/composer/appli-docker-entrypoint.sh" ]_
       


    - The `USER` sets the user under which the container runs. By default, if no `USER` is specified in Dockerfile, the container runs as `root`. Note that running as `root` is risky, but sometimes required.

2. The statements in Dockerfile are translated from the [instructions](https://github.com/MouseLand/cellpose?tab=readme-ov-file) for installing CellPose.
3. Finally, we have a recipe for CellPose.