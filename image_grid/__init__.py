from typing import Union, List, Tuple, Sequence, Iterable, Callable
from pathlib import Path
import random
import math
from functools import partial

import numpy as np
from PIL import Image
from natsort import humansorted

P = Union[str, Path]
ImageGetter = Tuple[any, Callable[[], Image.Image]]


class Interpolation:
    AUTO = 'auto'
    NEAREST = 'nearest'
    BILINEAR = 'bilinear'
    BICUBIC = 'bicubic'
    LANCZOS = 'lanczos'
    ALL = (AUTO, NEAREST, BILINEAR, BICUBIC, LANCZOS)


def image_getters_from_img_paths(img_paths: Iterable[P]) -> List[ImageGetter]:
    img_getters = [(fp, partial(Image.open, fp)) for fp in img_paths]
    return img_getters


def image_getters_from_folder(folder: P, file_types=('jpg', 'jpeg', 'png')):
    img_paths = [fp for fp in Path(folder).glob('*') if str(fp).split('.')[-1] in file_types]
    return image_getters_from_img_paths(img_paths)


def image_getters_from_ndarray(images: np.ndarray, keys=None):
    assert len(images.shape) in (3, 4), "image array must take shape (N, H, W, C) or (N, H, W)"
    N = images.shape[0]
    keys = keys or range(N)
    assert images.dtype == np.uint8, "images must have dtype uint8"
    return [(key, lambda: Image.fromarray(img)) for key, img in zip(keys, images)]


def image_grid(inp: Union[P, Sequence[P], Sequence[ImageGetter]],
               sort=True, shuffle=False, n: int = None, aspect_ratio: float = None,
               rows: int = None, columns: int = None,
               width: int = None, height: int = None,
               fill=False, interpolation='auto',
               border_size=2, border_size_around=0, border_color: Sequence[int] = (0, 0, 0, 0)):
    img_getters = None
    if isinstance(inp, np.ndarray):
        img_getters = image_getters_from_ndarray(inp),
    if isinstance(inp, (str, Path)):
        img_getters = image_getters_from_folder(inp)
    elif isinstance(inp, Sequence):
        if isinstance(inp[0], Tuple):
            img_getters = inp
        elif isinstance(inp[0], (str, Path)):
            img_getters = image_getters_from_img_paths(inp)
    assert img_getters, "incorrect type of input to image_grid"

    assert not (shuffle and sort), "shuffle and sort are mutually exclusive, only provide one"
    if shuffle:
        img_getters = list(img_getters)
        random.shuffle(img_getters)
    elif sort:
        img_getters = humansorted(img_getters)

    n = n or len(img_getters)
    assert 0 < n <= len(img_getters)

    if rows and not columns:
        columns = math.ceil(n / rows)
    elif columns and not rows:
        rows = math.ceil(n / columns)
    elif not columns and not rows:
        columns = math.ceil(math.sqrt(n))
        rows = math.ceil(n / columns)
    assert columns * rows >= n, "not enough rows and columns to include all images"

    assert 0 <= border_size
    assert 0 <= border_size_around

    def get_color_arg(inp: Sequence[int]):
        inp = list(inp)
        if len(inp) == 1:
            inp = inp * 3
        if len(inp) == 3:
            inp.append(255)
        assert len(inp) == 4
        inp = np.array(inp)
        assert np.all(0 <= inp) and np.all(inp <= 255), 'color range [0-255]'
        return inp

    border_color = get_color_arg(border_color)

    border_total_w = (columns - 1) * border_size + 2 * border_size_around
    border_total_h = (rows - 1) * border_size + 2 * border_size_around

    first_img = np.array(img_getters[0][1]())
    if not aspect_ratio:
        aspect_ratio = first_img.shape[1] / first_img.shape[0]

    assert not (height and width), "height and width are mutually exclusive, only provide one"
    if height:
        img_h = round((height - border_total_h) / rows)
        img_w = round(img_h * aspect_ratio)
    elif width:
        img_w = round((width - border_total_w) / columns)
        img_h = round(img_w / aspect_ratio)
    else:
        img_h = first_img.shape[0]
        img_w = round(img_h * aspect_ratio)
    height = img_h * rows + border_total_h
    width = img_w * columns + border_total_w

    img_grid = np.empty((height, width, 4), dtype=np.uint8)
    img_grid[:, :, :] = border_color

    def minmax(*inp):
        return min(*inp), max(*inp)

    for row in range(rows):
        for col in range(columns):
            i = row * columns + col
            if i >= n:
                break
            img = img_getters[i][1]()
            if img.mode == "I":  # support 16bit .png single channel
                img = (np.array(img) // 256).astype(np.uint8)
                img = Image.fromarray(img)
            h, w = img.height, img.width
            ar = w / h
            rmi, rma = minmax(img_h / h, img_w / w)
            scale = rma if fill else rmi
            _h, _w = round(scale * h), round(scale * w)
            inter = interpolation
            if inter == Interpolation.AUTO:
                if _h < img_h:
                    inter = Interpolation.LANCZOS
                else:
                    inter = Interpolation.BICUBIC
            img = img.resize((_w, _h), resample=getattr(Image, inter.upper()))
            img = np.array(img)
            # crop image (fill)
            if _h > img_h:
                h_start = (_h - img_h) // 2
                img = img[h_start:h_start + img_h]
                _h = img_h
            if _w > img_w:
                w_start = (_w - img_w) // 2
                img = img[:, w_start:w_start + img_w]
                _w = img_w
            # define offsets (fit)
            off_h = (img_h - _h) // 2
            off_w = (img_w - _w) // 2
            # insert image in img_grid
            x = border_size_around + col * (border_size + img_w) + off_w
            y = border_size_around + row * (border_size + img_h) + off_h
            img = img.reshape((*img.shape[:2], -1))
            if img.shape[2] == 1:
                img = np.tile(img, (1, 1, 3))
            if img.shape[2] == 3:
                img = np.concatenate((img, np.ones((_h, _w, 1), dtype=np.uint8) * 255), axis=2)
            assert img.shape[2] == 4
            img_grid[y:y + _h, x:x + _w] = img
    return img_grid
