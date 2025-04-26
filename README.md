# masscompress
A simple python script that makes compressing of many images fairly easy.
Usefule, when images can't be over a certain size.

This project was made, when i needed to upload many pictures to wordpress
and the max images size there was 2 mb.

Usage:
```bash
compress -s images -d compressed_images -m 2_000_000
```

This example compresses all the images in the `images` folder to under 2 mb
and puts the results in the `compressed_images` folder.

> [!WARNING]
> Currently, the program overwrites existing images without checking for
> name conflicts!
