In [previouse exercise](../containers/), we built a CellPose container, which can be used for batch bioimage analysis. In this section, we will demonstrate how to utilize this container for automated batch processing.

- Open a terminal and create a directory called `testimage`,e.g. /tmp/testimage
- Download the example image [here](https://github.com/embl-cba/bard-containers/blob/main/cellpose-nobard/MAX_pg6-3CF1_20--t1-3.jpg) and store it into `/tmp/testimg`
- Check your CellPose container still exists, if not, refer to [previous exercise](../containers/act03.md)
    ```
    docker images
    REPOSITORY                               TAG                 IMAGE ID      CREATED        SIZE
    cellpose                                 01                  9055a7c1a1ef  24 hours ago   12.7 GB
    ```

- Perform segmentation on the example image using the `cyto` model
    ```
    docker run -v /tmp/testimage:/testimage cellpose:01 --dir /testimage --pretrained_model cyto --save_png
    ```

    - Note the `-v` flag which makes your test image on your local computer available inside container.
    - The `/testimage` after the colon is the target directory inside container. You example image will be available under this direcotry inside container.
    - The arguments after the container `cellpose:01` are standard cellpose command options. You could refer to them [here](https://cellpose.readthedocs.io/en/latest/command.html)
    - After the run finished, your output images are saved in the same /testimage directory.