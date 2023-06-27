#!/bin/bash

# target directory
dir_path=$1

for file in "$dir_path"/*.bmp; do
    base_name=$(basename "$file" .bmp)
    
    ./pic2maze.py --classic "$file" > "$dir_path/$base_name.txt"
done
