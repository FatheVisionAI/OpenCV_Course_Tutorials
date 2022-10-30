# FatheVision AI  code
import sys

import cv2


def read_image(path, image_type=1):
    """
    reading the image from path

    Args:
        path: image path
        image_type: flag to read different image, gray, rgb, rgba

    Returns:
        read image
    """
    img = cv2.imread(path, image_type)
    return img


def main():
    image_path = "../data/opencv_logo.png"
    while True:
        print("****** Option ******")
        print("1: Gray image 1 channel image")
        print("2: Color image 3 channel image")
        print("3: color with alpha channel 4 channel image")
        print("q: press q for Quit.")
        choice = input("Enter your choice: ")
        if choice == "1":
            flag = 0
        elif choice == "2":
            flag = 1
        elif choice == "3":
            flag = -1
        elif choice == "q":
            sys.exit(0)
        else:
            print("wrong choice please enter again")
            continue
        image = read_image(image_path, flag)
        print("image shape in Height x Width x Channel ", image.shape)
        cv2.imshow("image window", image)
        cv2.waitKey(0)


if __name__ == "__main__":
    main()
