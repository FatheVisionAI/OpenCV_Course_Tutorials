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
    contours, hierarchy = cv2.findContours(image=image_edges, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_NONE)
    return contours


def perimeter_contour(cnt):
    """
    find the perimeter of the contour
    Args:
        cnt: input contour

    Returns:
        perimeter of the given contour
    """
    perimeter = cv2.arcLength(cnt, True)
    return perimeter


def area_contour(cnt):
    """
    find the area of the contour
    Args:
        cnt: input contour

    Returns:
        area of the given contour
    """
    area = cv2.contourArea(cnt)
    return area


def main():
    image_path = "../data/ballon.jpg"
    image = cv2.imread(image_path)
    contours = find_contours(image)
    cv2.drawContours(image=image, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2,
                     lineType=cv2.LINE_AA)

    perimeter = perimeter_contour(contours[0])
    area = area_contour(contours[0])

    cv2.putText(image, 'perimeter: ' + str(round(perimeter, 2)), (10, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color=(0, 0, 255),
                thickness=1)
    cv2.putText(image, 'area: ' + str(round(area, 2)), (10, 35), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color=(0, 0, 255),
                thickness=1)

    cv2.imshow('Image contours', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()



