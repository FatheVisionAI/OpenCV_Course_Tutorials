# FatheVision AI  code
import cv2


def put_text(img):
    """
    put Text on the image

    Args:
        img: input image
    Returns:
        image with text on it
    """

    font = cv2.FONT_HERSHEY_SIMPLEX
    org = (214, 44)
    font_scale = 1
    color = (0, 0, 255)
    thickness = 2
    img = cv2.putText(img, 'Horse', org, font, font_scale, color, thickness, cv2.LINE_AA)
    return img


def main():
    image_path = "../data/horse.jpg"
    image = cv2.imread(image_path)
    image = put_text(image)
    cv2.imshow("Image", image)
    cv2.waitKey(0)


if __name__ == "__main__":
    main()
