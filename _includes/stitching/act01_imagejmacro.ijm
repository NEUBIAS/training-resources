#@ File (style="directory") imageFolder

run("Close All");

tile_overlap = 5 
// Align with
run("Grid/Collection stitching", "type=[Grid: snake by rows] order=[Right & Down                ] grid_size_x=2 grid_size_y=2 tile_overlap="+tile_overlap+" first_file_index_i=1 directory="+imageFolder+
	" file_names=xyc_16bit__hoechst_phalloidin_tile_{ii}.tif output_textfile_name=TileConfiguration.txt fusion_method=[Max. Intensity] regression_threshold=0.30 max/avg_displacement_threshold=2.50 absolute_displacement_threshold=3.50 computation_parameters=[Save memory (but be slower)] image_output=[Fuse and display]");
rename("5p overlap")

tile_overlap = 10
// Align with
run("Grid/Collection stitching", "type=[Grid: snake by rows] order=[Right & Down                ] grid_size_x=2 grid_size_y=2 tile_overlap="+tile_overlap+" first_file_index_i=1 directory="+imageFolder+
	" file_names=xyc_16bit__hoechst_phalloidin_tile_{ii}.tif output_textfile_name=TileConfiguration.txt fusion_method=[Max. Intensity] regression_threshold=0.30 max/avg_displacement_threshold=2.50 absolute_displacement_threshold=3.50 computation_parameters=[Save memory (but be slower)] image_output=[Fuse and display]");
rename("10p overlap")

tile_overlap = 15
// Align with
run("Grid/Collection stitching", "type=[Grid: snake by rows] order=[Right & Down                ] grid_size_x=2 grid_size_y=2 tile_overlap="+tile_overlap+" first_file_index_i=1 directory="+imageFolder+
	" file_names=xyc_16bit__hoechst_phalloidin_tile_{ii}.tif output_textfile_name=TileConfiguration.txt fusion_method=[Max. Intensity] regression_threshold=0.30 max/avg_displacement_threshold=2.50 absolute_displacement_threshold=3.50 computation_parameters=[Save memory (but be slower)] image_output=[Fuse and display]");
rename("15p overlap")


// Optimal overlap
tile_overlap = 10
run("Grid/Collection stitching", "type=[Grid: snake by rows] order=[Right & Down                ] grid_size_x=2 grid_size_y=2 tile_overlap="+tile_overlap+" first_file_index_i=1 directory="+imageFolder+
	" file_names=xyc_16bit__hoechst_phalloidin_tile_{ii}.tif output_textfile_name=TileConfiguration.txt fusion_method=[Max. Intensity] regression_threshold=0.30 max/avg_displacement_threshold=2.50 absolute_displacement_threshold=3.50 compute_overlap computation_parameters=[Save memory (but be slower)] image_output=[Fuse and display]");
rename("optimal")

// Optimal overlap
tile_overlap = 10
run("Grid/Collection stitching", "type=[Grid: snake by rows] order=[Right & Down                ] grid_size_x=2 grid_size_y=2 tile_overlap="+tile_overlap+" first_file_index_i=1 directory="+imageFolder+
	" file_names=xyc_16bit__hoechst_phalloidin_tile_{ii}.tif output_textfile_name=TileConfiguration.txt fusion_method=[Linear Blending] regression_threshold=0.30 max/avg_displacement_threshold=2.50 absolute_displacement_threshold=3.50 compute_overlap computation_parameters=[Save memory (but be slower)] image_output=[Fuse and display]");
rename("optimal linear blending")