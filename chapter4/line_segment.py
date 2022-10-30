# FatheVision AI  code
import cv2


def draw_lines(img):
    """
    draw line on the image

    Args:
        img: input image
    Returns:
        image with line drawn
    """
    pt1 = (485, 302)
    pt2 = (200, 302)
    thickness = 5
    color = (0, 0, 255)
    image = cv2.line(img, pt1, pt2, color, thickness)
    return image


def main():
    image_path = "../data/horse.jpg"
    image = cv2.imread(image_path)
    image = draw_lines(image)
    cv2.imshow("Image", image)
    cv2.waitKey(0)


if __name__ == "__main__":
    main()
