# FatheVision AI  code
import cv2


def draw_circle(img):
    """
    draw circle on the image

    Args:
        img: input image
    Returns:
        image with circle drawn
    """
    color = (0, 0, 255)
    org = (300, 195)
    thickness = 5
    radius = 160
    img = cv2.circle(img, org, radius, color, thickness, cv2.LINE_AA)
    return img


def main():
    image_path = "../data/horse.jpg"
    image = cv2.imread(image_path)
    image = draw_circle(image)
    cv2.imshow("Image", image)
    cv2.waitKey(0)


if __name__ == "__main__":
    main()
