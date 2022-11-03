"""
Converts images from/to BMP, JPG, PNG, and WEBP.

To do:
    - refactor codes
    - proper variable names
    - readme.md file for instructions
    - improve converting image to jpeg file
"""
import os
import sys
from time import sleep
from pathlib import Path
from pathlib import PurePath

from PIL import Image

from utility import TextColor as tc


def clr_scr():
    if os.name in ('nt', 'dos'):
        os.system('cls')
    if os.name in ('linux', 'osx', 'posix', 'unix'):
        os.system('clear')


os.system('color')

IMG_EXTENSION = {
    '1': ['.bmp', 'bmp', 'BITMAP'],
    '2': ['.jpg', 'jpg', 'JPEG'],
    '3': ['.png', 'png', 'PNG'],
    '4': ['.webp', 'webp', 'WEBP'],
}

# 'Images' directory.
home_path = Path.home()
home_folders = [
    PurePath(item).name for item in home_path.glob('*') if item.is_dir()]

# If 'Images' directory not existing, create 'Images' directory.
if 'Images' not in home_folders:
    Path(home_path / 'Images').mkdir()
    print(f"\n{tc.GREEN}INFO: Images directory created in {home_path}.{tc.END}")

# Images folder.
img_folder = home_path / 'Images'

# Files inside 'Images' directory.
img_folder_files = [
    PurePath(item).name for item in img_folder.glob('*') if item.is_file()]

# Instructions
print(
    f"""
Convert your image files to a variety of formats.
Supported formats: {tc.YELLOW}BMP JPG PNG WEBP{tc.END}

Please make sure that the image file is in:
{tc.GREEN}{img_folder}{tc.END}
"""
)

# Image file name.
img_file = input(f"Enter '{tc.RED}q{tc.END}' anytime to quit."
                 f"\nImage file(with extension): ")

if img_file == 'q':
    sys.exit()

img_ext_name = [item[0] for item in IMG_EXTENSION.values()]

# Check img_file if valid file.
img_extension = PurePath(img_file).suffix.lower()
if img_extension == '':
    # Show error message if there is no file extension.
    print(f"{tc.RED}ERROR{tc.END}: Please check file extension.\n")
elif img_extension not in img_ext_name:
    # Show error message if file not supported by program.
    print(f"{tc.RED}ERROR{tc.END}: File format not supported. "
          f"Supported formats: {tc.YELLOW}BMP JPG PNG WEBP{tc.END}\n")
else:
    # File name is valid.
    convert_to_format = None
    # Check if file in 'Images'.
    if img_file in img_folder_files:

        while True:
            # Show options.
            print(f"\nConvert {tc.GREEN}{img_file}{tc.END} to:")
            for key, val in IMG_EXTENSION.items():
                print(f"[{key}: {val[1]}]", end=' ')
            # Ask user to convert image to what format.
            format_choice = input(f"\n\nEnter your choice from above(1 - 5): ")

            if format_choice == 'q':
                sys.exit()

            if format_choice not in IMG_EXTENSION.keys():
                clr_scr()
                print(
                    f"{tc.RED}ERROR{tc.END}: Invalid input [{tc.RED}{format_choice}{tc.END}].")

            else:
                convert_to_format = IMG_EXTENSION[format_choice][1]
                convert_to_format_name = IMG_EXTENSION[format_choice][2]
                format_extension = IMG_EXTENSION[format_choice][0]
                break

        # Convert image to file format of choice.
        with Image.open(img_folder / img_file) as im:
            rgb_im = im.convert('RGB')
            rgb_im.save(
                f"{img_folder / Path(img_file).stem}{format_extension}", convert_to_format_name)
                
            print(f"\n{tc.GREEN}INFO{tc.END}: {img_file} successfully converted to {convert_to_format_name}."
                  f"\n      {tc.GREEN}{Path(img_file).stem}{format_extension}{tc.END} saved to {tc.GREEN}{img_folder}{tc.END}.\n")

    else:
        print(f"{tc.RED}ERROR{tc.END}: File {tc.RED}{img_file}{tc.END} not "
              f"found in {tc.GREEN}{img_folder}{tc.END}.\n")
