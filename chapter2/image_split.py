# FatheVision AI  code
import cv2
import numpy as np


def split_image(img):
    """
    split image into 3 channel image
    Args:
        img: input image
    Returns:
        blue, green, red image
    """
    blue, green, red = cv2.split(img)
    return blue, green, red


def main():
    image_path = "../data/horse.jpg"
    image = cv2.imread(image_path)
    height, width, channel = image.shape
    b, g, r = split_image(image)
    zero_image = np.zeros((height, width), dtype=np.uint8)
    merge_b = cv2.merge((b, zero_image, zero_image))
    merge_g = cv2.merge((zero_image, g, zero_image))
    merge_r = cv2.merge((zero_image, zero_image, r))
    cv2.imshow('blue', merge_b)
    cv2.imshow('green', merge_g)
    cv2.imshow('red', merge_r)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
