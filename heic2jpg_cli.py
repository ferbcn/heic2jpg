import sys
import os
from heic2jpg import convert_folder_heic2jpg

default_folder_path = os.getcwd() + "/input/"
default_file_format = "jpg"     # ".png"

if __name__ == "__main__":
    args = sys.argv
    # No args, looking for file in default folder and saving to jpg format
    if len(args) <= 1:
        print("Opening default folder", default_folder_path, "and converting to JPG")
        convert_folder_heic2jpg(default_folder_path, default_file_format)
    else:
        file_folder_path = args[1]
        # One argument: folder path
        if len(args) == 2:
            print("Opening folder", file_folder_path, "and converting to", default_file_format)
            convert_folder_heic2jpg(file_folder_path, default_file_format)
        # Two arguments: folder path and file format: jpg or png
        if len(args) == 3:
            file_folder_path = args[1]
            file_format = args[2].lower()
            print("Opening folder", file_folder_path, "and converting to", file_format.upper())
            convert_folder_heic2jpg(file_folder_path, file_format)

