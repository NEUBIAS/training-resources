# !First start Napari and drag and drop the image (https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz_16bit_calibrated__dna_metaphase.tif) in the Napari viewer.

# Access the 3D array in the image layer
d = viewer.layers[0].data # assuming the image is in the first layer
shape = d.shape
print("Image shape:", shape)

# Compare the non-scaled non-scaled image to the scaled image. You can also use the 3D view to better appreciate the dimensions.
voxel_dims = (0.300, 0.1377745, 0.1377745) # original voxel dimensions in µm, in order ZYX
scaled_voxel_dims = [1 / voxel_dims[0] * v for v in voxel_dims]  # rescaling the voxel dimensions to maintain proportions but display with a z-step of 1.
print("New voxel dimensions scaled relative to original", scaled_voxel_dims)
viewer.add_image(d, name="Scaled to physical world dimensions", scale=scaled_voxel_dims) # Note that the scaled image layer contains the exact same data as the non-scaled image, but is only visualized differently to show the correct proportions.

# Create 2D slices (YX, ZX, and ZY)
mid_z_slice_ind = shape[0] // 2
mid_y_slice_ind = shape[1] // 2
mid_x_slice_ind = shape[2] // 2

viewer.add_image(d[mid_z_slice_ind], name=f"z={mid_z_slice_ind}")
viewer.add_image(d[mid_z_slice_ind], name=f"scaled: z={mid_z_slice_ind}", scale = scaled_voxel_dims[1:])
viewer.add_image(d[:, mid_y_slice_ind, :], name=f"y={mid_y_slice_ind}")
viewer.add_image(d[:, mid_y_slice_ind, :], name=f"scaled: y={mid_y_slice_ind}", scale = [scaled_voxel_dims[0], scaled_voxel_dims[2]])
viewer.add_image(d[:, :, mid_x_slice_ind], name=f"x={mid_x_slice_ind}")
viewer.add_image(d[:, :, mid_x_slice_ind], name=f"scaled: x={mid_x_slice_ind}", scale = scaled_voxel_dims[:2])

# View in grid mode side by side
viewer.grid.stride = 1
viewer.grid.shape = (-1, 2)
viewer.grid.enabled=True
