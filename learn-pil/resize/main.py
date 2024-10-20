from PIL import Image


def resize(im1: Image.Image, scale) -> Image.Image:
    im = im1.resize([int(scale * s) for s in im1.size])
    return im


if __name__ == "__main__":
    im1 = Image.open("p1.png")
    im2 = resize(im1, 2)
    im2.save("p1x2.png")
