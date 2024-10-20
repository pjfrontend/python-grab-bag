from PIL import Image


def create_gif(image_filenames, output_filename):
    # Open images and create a list
    images = [Image.open(filename) for filename in image_filenames]

    # Save the images as an animated GIF
    images[0].save(
        output_filename,
        save_all=True,
        append_images=images[1:],
        duration=500,  # duration of each frame in milliseconds
        loop=0,  # loop forever
    )


if __name__ == "__main__":
    images = ["p1.png", "p2.png"]
    create_gif(images, "p.gif")
