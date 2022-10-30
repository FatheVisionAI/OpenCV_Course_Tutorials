# FatheVision AI  code
import cv2
import sys


def averaging_blur(img):
    """
    blur the image with averaging blur

    Args:
        img: input image

    Returns:
        blur image
    """
    avg_img = cv2.blur(img, (5, 5))
    return avg_img


def gaussian_blur(img):
    """
    blur the image with gaussian blur

    Args:
        img: input image

    Returns:
        blur image
    """
    gaus_img = cv2.GaussianBlur(img, (5, 5), 0)
    return gaus_img


def median_blur(img):
    """
    blur the image with median blur

    Args:
        img: input image

    Returns:
        blur image
    """
    med_blur = cv2.medianBlur(img, 5)
    return med_blur


def bilateral_blur(img):
    """
    blur the image with bilateral blur

    Args:
        img: input image

    Returns:
        blur image
    """
    bil_img = cv2.bilateralFilter(img, 9, 75, 75)
    return bil_img


def main():

    image_path = "../data/ballon.jpg"
    image = cv2.imread(image_path)

    while True:
        print("****** Option ******")
        print("1: averaging blur...")
        print("2: gaussian blur")
        print("3: median blur")
        print("4: bilateral blur")
        print("q: press q for Quit.")
        choice = input("Enter your choice: ")
        if choice == "1":
            blur_image = averaging_blur(image)
        elif choice == "2":
            blur_image = gaussian_blur(image)
        elif choice == "3":
            blur_image = median_blur(image)
        elif choice == "4":
            blur_image = bilateral_blur(image)
        elif choice == "q":
            cv2.destroyAllWindows()
            sys.exit(0)
        else:
            print("wrong choice please enter again")
            continue

        cv2.imshow('Original Image', image)
        cv2.imshow("Blur Image", blur_image)
        cv2.waitKey(0)


if __name__ == "__main__":
    main()
