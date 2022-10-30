# FatheVision AI  code
import cv2


def find_contours(img):
    """
    find the contour in the image
    Args:
        img: input image

    Returns:
        tuple of contours
    """
    image_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    image_edges = cv2.Canny(image_gray, 100, 200, L2gradient=True)
    contours, hierarchy = cv2.findContours(image_edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    return contours


def main():
    image_path = "../data/ballon.jpg"
    image = cv2.imread(image_path)

    contours = find_contours(image)

    cv2.drawContours(image=image, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2,
                     lineType=cv2.LINE_AA)

    cv2.imshow('Image contours', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()


