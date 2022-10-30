# FatheVision AI  code
import cv2


def vertical_stitch(img1, img2):
    """
    Stitch images vertical
    Args:
        img1: input image1
        img2: input image2

    Returns:
        vertical stitch image
    """
    stitch_image = cv2.vconcat([img1, img2])
    return stitch_image


def horizontal_stitch(img1, img2):
    """
    Stitch images vertical

    Args:
        img1: input image1
        img2: input image2

    Returns:
        horizontal stitch image
    """
    stitch_image = cv2.hconcat([img1, img2])
    return stitch_image


def main():
    image_path1 = "../data/horse.jpg"
    image_path2 = "../data/horse1.jpg"

    image1 = cv2.imread(image_path1)
    image2 = cv2.imread(image_path2)

    height, width, _ = image1.shape
    image2 = cv2.resize(image2, (width, height))

    horizontal_stitch_image = horizontal_stitch(image1, image2)
    vertical_stitch_image = vertical_stitch(image1, image2)

    cv2.imshow('Horizontal Stitch Image', horizontal_stitch_image)
    cv2.imshow('Vertical Stitch Image', vertical_stitch_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
