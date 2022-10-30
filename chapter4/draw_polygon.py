# FatheVision AI  code
import cv2
import numpy as np


def draw_polygon(img):
    """
    draw polygon on the image

    Args:
        img: input image
    Returns:
        image with polygon drawn
        """
    pts = np.array([[289, 20], [460, 110],
                    [460, 267], [298, 337],
                    [143, 267], [143, 110]], np.int32)

    pts = pts.reshape((-1, 1, 2))
    is_closed = True
    color = (255, 0, 0)
    thickness = 2
    img = cv2.polylines(img, [pts], is_closed, color, thickness)
    return img


def main():
    image_path = "../data/horse.jpg"
    image = cv2.imread(image_path)
    image = draw_polygon(image)
    cv2.imshow("Image", image)
    cv2.waitKey(0)


if __name__ == "__main__":
    main()
