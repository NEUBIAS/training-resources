### Watershed shape 2

- Open [xy_8bit__several_touching_nuclei.tif](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__several_touching_nuclei.tif)
  - Using the watershed transform try to segment the nuclei.
    - Hints:
      - Directly applying a watershed on the inverted image will likely fail as there are too many intensity maxima even within one nucleus.
      - Thus, one will need to binarise the image and perform a watershed on the distance transform.
