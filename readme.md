# collage
Python module to make collages.

#### install
```
$ git clone https://github.com/RasmusHaugaard/collage.git
$ cd collage
$ pip install -e .
```
Installing the module registers a script `collage` which can be run from any folder.
#### usage
```
$ collage --folder ./images --n 4 --rows 1 --width 1000 --fill
saved collage.jpg, (166, 998, 3), 27.1KiB
```
![](media/collage.jpg)

```
$ collage -f images -n 14 -r 2 -w 1000 --aspect-ratio 1 --out collage.png
saved collage.png, (284, 999, 4), 338.7KiB
```
![](media/collage.png)

```
$ collage -f images -n 16 --fill -a 1 -w 400 -bs 0 -o square.png
saved square.png, (400, 400, 4), 263.1KiB
```
![](media/square.png)


```
$ collage -h
usage: collage [-h] (-f FOLDER | -i IMAGES [IMAGES ...]) [-o OUT] [-y]
               [-q JPEG_QUALITY] [-t FILE_TYPES] [-a ASPECT_RATIO] [--fill]
               [--interpolation {auto,nearest,bilinear,bicubic,lanczos}]
               [-n N] [--no-sort] [--shuffle] [-w WIDTH | -H HEIGHT] [-r ROWS]
               [-c COLUMNS] [-bs BORDER_SIZE] [-bsa BORDER_SIZE_AROUND]
               [-bc BORDER_COLOR [BORDER_COLOR ...]]

optional arguments:
  -h, --help            show this help message and exit
  -f FOLDER, --folder FOLDER
                        path to folder with images
  -i IMAGES [IMAGES ...], --images IMAGES [IMAGES ...]
                        image file paths
  -o OUT, --out OUT     output file path
  -y, --override        if set, it will override the output file
  -q JPEG_QUALITY, --jpeg-quality JPEG_QUALITY
                        jpeg quality [1-100]
  -t FILE_TYPES, --file-types FILE_TYPES
  -a ASPECT_RATIO, --aspect-ratio ASPECT_RATIO
                        aspect ratio of images in collage (width/height). if
                        not defined, it will be chosen from the first image
  --fill                fill the available area instead of fitting the whole
                        image
  --interpolation {auto,nearest,bilinear,bicubic,lanczos}
  -n N, --n N           limit the amount of pictures to include
  --no-sort             don't sort images by path
  --shuffle             shuffle image order
  -w WIDTH, --width WIDTH
                        approx width of collage in px
  -H HEIGHT, --height HEIGHT
                        approx height of collage in px
  -r ROWS, --rows ROWS  number of rows in collage
  -c COLUMNS, --columns COLUMNS
                        number of columns in collage
  -bs BORDER_SIZE, --border-size BORDER_SIZE
                        border size in px
  -bsa BORDER_SIZE_AROUND, --border-size-around BORDER_SIZE_AROUND
                        border around collage in px
  -bc BORDER_COLOR [BORDER_COLOR ...], --border-color BORDER_COLOR [BORDER_COLOR ...]
                        rgba color [0-255]
```
