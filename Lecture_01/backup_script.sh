#!/bin/bash

# Function to display help message
display_help() {
    echo "Usage: $0 [-o OUTPUT_FOLDER] [-h|--help] FOLDER_OR_FILE_TO_BACKUP"
    echo "Options:"
    echo "  -o OUTPUT_FOLDER  Specify the output folder for the backup. If not provided, the backup will be saved in the current folder."
    echo "  -h, --help        Display this help message."
    exit 1
}

# Initialize variables with default values
output_folder="."
date_today=$(date +%Y%m%d)
backup_name="backup_$date_today.tar.gz"

# Parse command-line options
while [[ $# -gt 0 ]]; do
    case $1 in
        -o)
            shift
            output_folder="$1"
            shift
            ;;
        -h|--help)
            display_help
            ;;
        *)
            source_path="$1"
            shift
            ;;
    esac
done

# Check if a source path is provided
if [ -z "$source_path" ]; then
    echo "Error: Please provide a folder or file to backup."
    display_help
fi

# Check if the source path exists
if [ ! -e "$source_path" ]; then
    echo "Error: The specified source folder or file does not exist."
    exit 1
fi

# Create the backup
backup_path="$output_folder/$backup_name"
tar -czvf "$backup_path" "$source_path"

echo "Backup completed. The backup is saved as $backup_path"
