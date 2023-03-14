import os
from PIL import Image
import pillow_heif
from os import listdir
from os.path import isfile, join


def convert_folder_heic2jpg(file_folder_path, file_format):
    # Convert single file
    if isfile(file_folder_path):
        folder_path = os.path.split(file_folder_path)[0] + "/"
        print("Converting single file...")
        heic_files = []
        if file_folder_path[-4:].upper() == "HEIC":
            heic_files.append(file_folder_path)
    # Convert files in folder
    else:
        folder_path = file_folder_path
        if not folder_path[-1] == "/":
            folder_path += "/"
        print("Converting folder", folder_path)
        files_in_folder = [f for f in listdir(folder_path) if isfile(join(folder_path, f))]
        # remove non HEIC files
        heic_files = [folder_path + file for file in files_in_folder if file[-4:].upper() == "HEIC"]

    # create output folder if it doesn't exist
    output_folder = folder_path + "output/"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open files and save in jpg format
    for file_path in heic_files:
        print("Opening", file_path)
        heif_file = pillow_heif.read_heif(file_path)
        image = Image.frombytes(
            heif_file.mode,
            heif_file.size,
            heif_file.data.tobytes(),
            "raw",
        )
        filename = os.path.basename(file_path)
        if file_format in ["jpg", "jpeg"]:
            output_filename = filename + ".jpg"
            save_file_format = "jpeg"
        elif file_format == "png":
            output_filename = filename + ".png"
            save_file_format = file_format

        output_filepath = output_folder + output_filename
        image.save(output_filepath, save_file_format)
        print("Image saved to", output_filepath)

    print(f"{len(heic_files)} file(s) converted!")

