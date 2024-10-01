#!/bin/bash

#folder_path="/home/ec2-user/scratch"

for file in /home/ec2-user/scratch/MDA/*
do
	echo "Running script with file: $file"
	sh ./run_wsi.sh "$file"
	echo "Finished run with file: $file"
done
