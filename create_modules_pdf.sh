#!/bin/bash

# Array of file names
figures=("pixels.jpg" "ome-zarr.png") 

# Temporary directory for modified images
tmp_dir=$(mktemp -d)

counter=0 # needed for correct sorting of the tmp image files

# Process each file
for file in "${figures[@]}"; do
  title=$(basename "$file" .${file##*.}) 
  echo $title
  convert "./figures/$file" -gravity north -splice 0x40 -pointsize 20 -annotate +0+10 "$title" "$tmp_dir/$(printf "%03d" $counter)-$title-annotated.png"
  ((counter++))
done

# Convert all annotated images in the temporary directory into one PDF
convert "$tmp_dir/*-annotated.png" module_figures.pdf

# Cleanup
rm -rf "$tmp_dir"

open module_figures.pdf
