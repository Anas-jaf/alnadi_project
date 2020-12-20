#!/usr/bin/bash

folder = "move_here"
mkdir $folder

for file in {436..439}
do
	echo "$file"
	#mv "$file.txt" "$file_*.txt" move_here

done

echo all done
