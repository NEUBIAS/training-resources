- Open image [xyt_8bit_polyp](https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyt_8bit_polyp.tif)
- Make a maximum intensity projection to create a background image:
  **[Image › Stacks › Z Project...]**
- Use the image calculator function **[ Process › Image Calculator...]** to subtract the maximum intensity projection from the original:

    - Image1: xyt_8bit_polyp
    - Operation: Subtract
    - Image2: MAX_xyt_8bit_polyp
        and tick 'create new window' and '32-bit float result'. Say 'yes' to the 'Process entire stack'-message.
