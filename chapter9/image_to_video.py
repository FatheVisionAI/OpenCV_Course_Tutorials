# FatheVision AI  code
import cv2
import os


def main():
    image_dir = 'images'

    image_name = os.listdir(image_dir)

    fps = 15
    size = (500, 500)
    out = cv2.VideoWriter("test.mp4", cv2.VideoWriter_fourcc(*'mp4v'), fps, size)  # video writer instance

    for name in image_name:
        image_path = image_dir + '/' + name  # image path
        image = cv2.imread(image_path)  # image read
        image_resize = cv2.resize(image, size)  # resized the image for saving the image
        out.write(image_resize)  # saving the resized image
    out.release()


if __name__ == "__main__":
    main()
