# FatheVision AI  code
import cv2


def saved_image(img, filename):
    """
    save the image
    Args:
        img: input image
        filename: name to saved image
    Returns:

    """
    cv2.imwrite(filename, img)


def main():
    image_path = "../data/horse.jpg"
    image = cv2.imread(image_path)
    saved_image(image, "horse_saved.jpg")


if __name__ == "__main__":
    main()
