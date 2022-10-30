# FatheVision AI  code
import cv2


def draw_ellipse(img):
    """
    draw ellipse on the image

    Args:
        img: input image
    Returns:
        image with ellipse drawn
    """
    center_coordinates = (300, 190)
    axes_length = (180, 130)
    angle = 0
    start_angle = 0
    end_angle = 360
    color = (0, 0, 255)
    thickness = 5
    image = cv2.ellipse(img, center_coordinates, axes_length,
                        angle, start_angle, end_angle, color, thickness)
    return img


def main():
    image_path = "../data/horse.jpg"
    image = cv2.imread(image_path)
    image = draw_ellipse(image)
    cv2.imshow("Image", image)
    cv2.waitKey(0)


if __name__ == "__main__":
    main()
