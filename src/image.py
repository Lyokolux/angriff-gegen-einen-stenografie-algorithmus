import math
from PIL import Image as PILImage
from collections import defaultdict


class Image:
    """
        coords: (x, y)
        position: (x * self.width + )
    """

    def __init__(self, pathToImage):
        self.im = PILImage.open(pathToImage)
        self.pix = self.im.load()
        self.width = self.im.size[0]
        self.height = self.im.size[1]
        self.colorsMap = self._getColorsMap()

    def getPixelAtCoord(self, coords):
        (x, y) = coords
        return self.pix[x, y]

    def getCoordsFromPosition(self, position):
        (x, y) = divmod(position, self.height)
        return (x, y)

    def getPositionFromCoords(self, coords):
        [x, y] = coords
        return (x * self.height) + y

    def getGreyValueInPixel(self, position):
        coords = self.getCoordsFromPosition(position)
        return self.getPixelAtCoord(coords)[0]

    def getEncryptionTable(self):
        return self.colorsMap

    def getDecryptionTable(self):
        return {position: code for code,
                positions in self.colorsMap.items() for position in positions}

    def _getColorsMap(self):
        colorMap = defaultdict(lambda: [])
        for position in range(self.width * self.height):
            greyColor = self.getGreyValueInPixel(position)
            colorMap[greyColor].append(position)
        return colorMap


if __name__ == "__main__":
    from pathlib import Path
    imageMinimal = Image(Path("src/assets/grey_test.png"))
    imageGrey = Image(Path("src/assets/26_nuances_de_grey.png"))
    imageVert = Image(Path("src/assets/vert.png"))
    imageCoin = Image(Path("src/assets/cover_image_coin.png"))
