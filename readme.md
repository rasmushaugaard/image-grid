# image-grid
python module to make image grids

#### install
```
$ git clone https://github.com/RasmusHaugaard/image-grids.git
$ cd image-grid
$ pip install -e .
```
Installing the module registers a script `image-grid` which can be run from any folder.
#### usage
```
$ image-grid --folder ./images --n 4 --rows 1 --width 1000 --fill
saved image-grid.jpg, (166, 998, 3), 27.1KiB
```
![](media/image-grid.jpg)

```
$ image-grid -f images -n 14 -r 2 -w 1000 --aspect-ratio 1 --out image-grid.png
saved image-grid.png, (284, 999, 4), 338.7KiB
```
![](media/image-grid.png)

```
$ image-grid -f images -n 16 --fill -a 1 -w 400 -bs 0 -o square.png
saved square.png, (400, 400, 4), 263.1KiB
```
![](media/square.png)


```
$ image-grid -h
usage: image-grid [-h] (-f FOLDER | -i IMAGES [IMAGES ...]) [-o OUT] [-y]
                  [-q JPEG_QUALITY] [-t FILE_TYPES] [-a ASPECT_RATIO] [--fill]
                  [--interpolation {auto,nearest,bilinear,bicubic,lanczos}]
                  [-n N] [--no-sort] [--shuffle] [-w WIDTH | -H HEIGHT]
                  [-r ROWS] [-c COLUMNS] [-bs BORDER_SIZE]
                  [-bsa BORDER_SIZE_AROUND]
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
                        aspect ratio of grid cells (width/height). if not
                        defined, it will be chosen from the first image
  --fill                fill the grid cell instead of fitting the whole image
                        in the cell
  --interpolation {auto,nearest,bilinear,bicubic,lanczos}
  -n N, --n N           limit the amount of pictures to include
  --no-sort             don't sort images by path
  --shuffle             shuffle image order
  -w WIDTH, --width WIDTH
                        approx width of image grid in px
  -H HEIGHT, --height HEIGHT
                        approx height of image grid in px
  -r ROWS, --rows ROWS  number of rows in image grid
  -c COLUMNS, --columns COLUMNS
                        number of columns in image grid
  -bs BORDER_SIZE, --border-size BORDER_SIZE
                        border size in px
  -bsa BORDER_SIZE_AROUND, --border-size-around BORDER_SIZE_AROUND
                        border around image grid in px
  -bc BORDER_COLOR [BORDER_COLOR ...], --border-color BORDER_COLOR [BORDER_COLOR ...]
                        rgba color [0-255]
```
