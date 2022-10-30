# FatheVision AI  code
import cv2


def draw_rectangle(img):
    """
    draw rectangle on the image

    Args:
        img: input image
    Returns:
        image with rectangle drawn
    """
    top_left = (193, 44)
    bottom_right = (472, 310)
    color = (0, 0, 255)
    thickness = 3
    img = cv2.rectangle(img, top_left, bottom_right, color, thickness)
    return img


def main():
    image_path = "../data/horse.jpg"
    image = cv2.imread(image_path)
    image = draw_rectangle(image)
    cv2.imshow("Image", image)
    cv2.waitKey(0)


if __name__ == "__main__":
    main()
