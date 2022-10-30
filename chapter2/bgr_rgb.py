# FatheVision AI  code
import cv2


def bgr_rgb(img):
    """
    covert bgr to rgb image
    Args:
        img: input image

    Returns:
        converted image
    """
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img


def main():
    image_path = "../data/horse.jpg"
    image = cv2.imread(image_path)
    rgb_image = bgr_rgb(image)
    cv2.imshow('original image', image)
    cv2.imshow('RGB image', rgb_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
