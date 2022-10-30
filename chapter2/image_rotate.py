# FatheVision AI  code
import sys

import cv2
from image_read import read_image


def rotate_image(img, angle_code):
    """
    rotate image 90 180, 270
    Args:
        img: input image for rotation
        angle_code: rotation angle code

    Returns:
        rotated image
    """
    img = cv2.rotate(img, angle_code)
    return img


def main():
    image_path = "../data/horse.jpg"
    image = read_image(image_path)
    while True:
        print("*********")
        print("1: 90 rotation")
        print("2: 180 rotation")
        print("3: 270 rotation")
        print("q: Quit")
        rotation = input("Enter the rotate choice: ")
        print("*********")

        if rotation == "1":
            rotated_image = rotate_image(image, cv2.ROTATE_90_CLOCKWISE)
        elif rotation == "2":
            rotated_image = rotate_image(image, cv2.ROTATE_180)
        elif rotation == "3":
            rotated_image = rotate_image(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
        elif rotation == "q":
            sys.exit()
        else:
            print("wrong choice... please enter again")
            continue
        window_name = "Rotate_image"
        cv2.imshow(window_name, rotated_image)
        cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
