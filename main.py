#!/usr/bin/env python


from PIL import Image
import os
import shutil

source_folder = "./camera"
dest_folder = "./compressed"
maxSize = 2000000

ERROR = '\033[91mError:\033[0m'

def compress_image(image_name, size):
    '''
    Compresses an image to the specfied size or less via bruteforce trial and error
    '''
    global source_folder
    global dest_folder

    qual = 60

    # the image's name get's passed, without path
    source_image = f"{source_folder}/{image_name}"
    dest_image = f"{dest_folder}/{image_name}"
    
    if not os.path.isfile(source_image):
        raise Exception(f"{source_image} doesn't exist")

    currSize = os.stat(source_image).st_size

    if currSize <= size:
        shutil.copyfile(source_image, dest_image)
        print(f"Image {source_image} is already {currSize/1000}kb, copied to {dest_image}")
        return


    while currSize > size and qual > 0:
        try:
            pic = Image.open(source_image)

            pic.save(dest_image, optimize=True, quality=qual)

            currSize = os.stat(dest_image).st_size

            qual -= 20
        except Image.UnidentifiedImageError:
            print(f"{ERROR} {source_image} is not an image")
            return

    if currSize > size:
        os.remove(dest_image)
        print(f"{dest_image} could not be compressed to under {size} bytes")
    else:
        print(f"Image {source_image} compressed to {currSize/1000}kb at {dest_image}")


if __name__ == '__main__':
    if not os.path.isdir(source_folder):
        print(f"{ERROR} {source_folder} is not a directory")
        exit(1)
    if not os.path.isdir(dest_folder):
        print(f"{ERROR} {dest_folder} is not a directory")
        exit(1)
    for dirpath, dirnames, filenames in os.walk(source_folder):
        for file in filenames:
            compress_image(file, maxSize)
