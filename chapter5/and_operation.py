# FatheVision AI  code
import cv2


def operation_and(img1, img2):
    """
    Perform AND operation on pair of image bitwise
    Args:
        img1: input image 1
        img2: input image 2

    Returns:
        image with AND operation on given image
    """
    img = cv2.bitwise_and(img1, img2)
    return img


def main():
    image_path = "../data/horse.jpg"
    mask_path = "../data/mask.jpg"

    image = cv2.imread(image_path)
    mask = cv2.imread(mask_path)

    image = operation_and(image, mask)

    cv2.imshow('Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
