run("MRI Stack");
run("Scale...", "x=3 y=3 z=20 interpolation=Bilinear average process create");
run("Export Current Image as XML/N5", "  subsampling_factors=[{ {1,1,1}, {2,2,2}, {4,4,4} }] n5_chunk_sizes=[{ {64,64,64}, {64,64,64}, {64,64,64} }] compression=[raw (no compression)] default export_path=/Users/tischer/Desktop/export.xml");
