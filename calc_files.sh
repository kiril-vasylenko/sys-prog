#!/bin/bash

if [[ $EUID -ne 0 ]]; then
   echo "Error: run this script as root"
   exit 1
fi

TARGET_DIR="/etc"

if [ -d "$TARGET_DIR" ]; then
    files=$(find "$TARGET_DIR" -type f | wc -l)
    echo "Number of files in $TARGET_DIR: $files"
else
    echo "Directory $TARGET_DIR does not exist."
    exit 1
fi
