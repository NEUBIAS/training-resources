In this activity, we will explain how to make your container available as an Interactive Tool in a public Galaxy instance. While building a Galaxy Interactive Tool requires some knowledge of XML and server administration, which are beyond the scope of this exercise, we will walk you through the essential steps to complete the process.

**Things to know**
- Refer to [Galaxy tutorial](https://training.galaxyproject.org/training-material/topics/dev/tutorials/interactive-tools/tutorial.html), if you would like to lear how to build and configure an interactive tool. 
- Galaxy EU instance (https://usegalaxy.eu)

**Steps**
- Galaxy Interactive Tools require certain dependencies. To simplify the setup, we recommend using one of the base images available [here](https://github.com/jlesage/docker-baseimage-gui). These images come pre-configured with all necessary dependencies, making the process more efficient and reducing setup complexity.
    1. Have a look at this [example](https://github.com/sunyi000/docker-napari/tree/main), the first line uses one of the base image mentioned.
        
        > _FROM jlesage/baseimage-gui:ubuntu-22.04-v4.5.2 AS build_
        
    2. Add the main installation steps to your own Dockerfile.
    3. Create a startup script for the container `startapp.sh`. While not always required, it depends on how your Galaxy XML is structured..
    4. Add the following lines to your Dockerfile

        > _EXPOSE 5800_
        >
        > _COPY startapp.sh /startapp.sh_
        >
        > _RUN chmod +x /startapp.sh_
        >
        > _ENV APP_NAME="Napari"_
        >
        > _ENV KEEP_APP_RUNNING=0_
        >
        > _ENV TAKE_CONFIG_OWNERSHIP=1_
        >
        > _WORKDIR /config_
        
    5. Build and test your Dockerfile locally. You could refer to [this module](../containers/) for building containers.
    6. Create a public repository for your docker recipe, e.g., Github(https://github.com), and make the repository public.
    7. Push your image to a public container registry, such as [quay.io](quay.io)
    8. If you would like to make your interactive tool available in Galaxy EU, visit the [Galaxy EU repository](https://github.com/usegalaxy-eu/usegalaxy-eu-tools) submit a pull request(PR).