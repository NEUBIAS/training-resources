run("MRI Stack");
run("Scale...", "x=10 y=10 z=1.0 width=1860 height=2260 depth=27 interpolation=Bilinear average process create");
run("Export Current Image as XML/N5", "  subsampling_factors=[{ {1,1,1}, {2,2,2}, {4,4,4}, {8,8,8}, {16,16,16} }] n5_chunk_sizes=[{ {64,64,64}, {64,64,64}, {64,64,64}, {64,64,64}, {64,64,64} }] compression=[raw (no compression)] default export_path=/Users/tischer/Desktop/export.xml");
