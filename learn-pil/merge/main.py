from PIL import Image


def merge(im1: Image.Image, im2: Image.Image) -> Image.Image:
    w = im1.size[0] + im2.size[0]
    h = max(im1.size[1], im2.size[1])
    im = Image.new("RGBA", (w, h))

    im.paste(im1)
    im.paste(im2, (im1.size[0], 0))

    return im


if __name__ == "__main__":
    im1 = Image.open("p1.png")
    im2 = Image.open("p2.png")
    im3 = merge(im1, im2)
    im3.save("p3.png")
