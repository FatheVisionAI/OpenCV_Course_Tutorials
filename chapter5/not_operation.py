# FatheVision AI  code
import cv2


def operation_not(img):
    """
    Perform NOT operation on image bitwise
    Args:
        img: input image

    Returns:
        image with NOT operation
    """
    img_not = cv2.bitwise_not(img, mask=None)
    return img_not


def main():
    image_path = "../data/mask.jpg"
    image = cv2.imread(image_path)
    image = operation_not(image)
    cv2.imshow('Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
