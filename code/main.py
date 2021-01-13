from os import listdir
from os.path import isfile, join
import re
import random
import pathlib
from PIL import Image


def parentPath():
    p = pathlib.Path(pathlib.Path().absolute())
    return str(p.parent.absolute()).replace("\\", "/")


def maxImageNum():
    onlyfiles = [f for f in listdir(parentPath() + "/images") if isfile(join(parentPath() + "/images", f))]
    for i, x in enumerate(onlyfiles):
        onlyfiles[i] = int(re.search(r"[0-9]+", x).group(0))
    return max(onlyfiles)


def getRandomUrl():
    x = random.randint(1, maxImageNum())
    s = f"/images/beaverpicture ({x}).jpg"
    return parentPath() + s


def showImage(url):
    im = Image.open(url)
    im.show()


showImage(getRandomUrl())
