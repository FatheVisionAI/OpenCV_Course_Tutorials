# FatheVision AI  code
import cv2
from image_read import read_image


def gray_scale(img):
    """
    convert BGR image to gray scale image

    Args:
        img: input image

    Returns:
        gray scale image
    """
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return gray_img


def main():
    image_path = "../data/horse.jpg"
    image = read_image(image_path)
    gray_image = gray_scale(image)
    cv2.imshow("original BGR image", image)
    cv2.imshow('Gray image', gray_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()

