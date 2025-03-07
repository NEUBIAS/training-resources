In this section, we will demonstrate how to make a custom container available for interactive analysis, using the CellPose container as an example from the [previous excercise](../containers/). We have built and tested our CellPose container locally. To deploy it to BARD, we need to modify the Dockerfile by adding the necessary configurations.

**Steps**
1. Modify the Dockerfile
- Open [this Dockerfie](https://github.com/embl-cba/bard-containers/blob/main/cellpose/Dockerfile)
- Have look at the added lines:
    - `LABEL`:  Since BARD is a desktop environment, it needs to know where to display applications and how to launch them when users click on them. To achieve this, we embed the necessary functions using the `LABEL` instruction in the Dockerfile.
        - The `oc.icon` and `oc.icondata` labels tell BARD which logo image to use for the application. 
        - The `oc.icondata` label requires a base64-encoded string of the image file(cellpose.svg). To generate this string, use `cat cellpose.svg |base64`
        - The `oc.keyword` label is used by the web application search engine.
        - The `oc.cat` label defines the category of the application in BARD. This helps organize applications within the BARD desktop environment.BARD has these categories 'development', 'office', 'education', 'utilities'.
        - The `oc.template` label specifies the name of the template to use in BARD. It corresponds to the base image used in the FROM statement of the Dockerfile. If the value is incorrect, it won't prevent the container from running, but the application may not function as expected in the BARD environment.
        - The `oc.name` label specifies the name of the application. 
        - The `oc.displayname` label defines the name displayed in the BARD desktop.
        - The `oc.launch` label is a unique X11 window class name that BARD uses to identify the application window. To find out the name, run `wmctrl -lx`
        - The `oc.path` label specifies the path to the application's binary executable inside the container. This tells BARD where to find and launch the application.
        - The `oc.args` label specifies any additional arguments that should be passed to the command defined in oc.path when launching the application.
        - The `oc.app` label must be always set to `app`
        - The `oc.showinview` label instructs BARD to place an icon of the application in its dock.

    - Make app icon images available. Line 66,67
        ```
        RUN  if [ -d /usr/share/icons ];   then cd /usr/share/icons;    /composer/safelinks.sh; fi 
        RUN  if [ -d /usr/share/pixmaps ]; then cd /usr/share/pixmaps;  /composer/safelinks.sh; fi 
        ```

    - `ENV` variables. Line 69-72
        - `ENV APPNAME`: The name of the application.
        - `ENV APPBIN`: The binary executable of the application. In the CellPose example, we launch CellPose within a Konsole terminal (/usr/bin/konsole) to monitor the output in real-time.
        - `ENV APP`: This is the same as `APPBIN`
        - `ENV ARGS`: This specifies the arguments for `APPBIN`.

    - To start container as the current logged-in user. Line 89-98
        ```
        RUN mkdir -p /run/user && chmod 777 /run/user

        RUN mkdir -p /etc/localaccount && \
            for f in passwd shadow group gshadow ; do if [ -f /etc/$f ] ; then  cp /etc/$f /etc/localaccount; rm -f /etc/$f; ln -s /etc/localaccount/$f /etc/$f; fi; done
        
        CMD ["/composer/appli-docker-entrypoint.sh" ]
        ```

        - BARD Desktop allows users to log in via LDAP or OIDC, so the Docker container must run as the logged-in user. The commands above store the LDAP information and ensure that the logged-in user is available inside the container.

2. Deploy to BARD
    - As contributors:
        - Go to [BARD containers repository](https://github.com/embl-cba/bard-containers)
        - Fork the repository to your own user.
        - Create a branch for your container.
        - Open a pull request(PR).

    - As administrator (To deploy apps to your own BARD instance)
        - Build and test your container locally. 
        - Push your container image to a registry, for example, dockerhub, quay.io etc.
        - Pull the image from the registry.
        - Extract the metadata from image using the below command, (replace with the actual image ID)
            ```
            docker inspect  CELLPOSE_IMAGE_ID > cellpose.json
            ```
        - In a terminal,
            ```
            curl -X PUT -H 'Content-type: text/javascript https://YOUR_BARD_URL/API/manager/image -d@cellpose.json
            ```