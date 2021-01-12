import nose2
from pathlib import Path
from image import Image

PROJECT_PATH = Path('./src/assets')
PATH_IMG_MINIMAL = PROJECT_PATH.joinpath('grey_test.png')
PATH_IMG_GREY = PROJECT_PATH.joinpath('26_nuances_de_grey.png')
PATH_IMG_COIN = PROJECT_PATH.joinpath('cover_image_coin.png')
PATH_IMG_VERT = PROJECT_PATH.joinpath('vert.png')


def test_img_initialized():
    assert Image(PATH_IMG_MINIMAL)
    assert Image(PATH_IMG_GREY)
    assert Image(PATH_IMG_VERT)
    assert Image(PATH_IMG_COIN)


def test_img_right_color_map():
    assert Image(PATH_IMG_MINIMAL).colorsMap == {
        125: [0, 1, 2, 3, 4, 5, 6, 7],
        69: [8, 9, 10, 12, 13, 14],
        1: [11, 15]
    }
    assert Image(PATH_IMG_GREY).colorsMap == {97: [0], 98: [1], 99: [2], 100: [3], 101: [4], 102: [5], 103: [6], 104: [7], 105: [8], 106: [9], 107: [10], 108: [
        11], 109: [12], 110: [13], 111: [14], 112: [15], 113: [16], 114: [17], 115: [18], 116: [19], 117: [20], 118: [21], 119: [22], 120: [23], 121: [24], 122: [25]}
