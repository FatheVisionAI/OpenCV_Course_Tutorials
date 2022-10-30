# FatheVision AI  code
import cv2


def detect_edge(img):
    """
    detect edge on image

    Args:
        img: input image

    Returns:
        edge image
    """
    edges = cv2.Canny(img, 100, 200, L2gradient=True)
    return edges


def main():
    image_path = "../data/ballon.jpg"
    image = cv2.imread(image_path)
    thresh_image = detect_edge(image)
    cv2.imshow('Original Image', image)
    cv2.imshow("Blur Image", thresh_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()


