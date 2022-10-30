# FatheVision AI  code
import sys

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


def main():
    image_path = "../data/ballon.jpg"
    image = cv2.imread(image_path)
    contours = find_contours(image)
    cnt = contours[0]
    cv2.drawContours(image=image, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2,
                     lineType=cv2.LINE_AA)
    while True:
        print("****************")
        print("Enter the point")
        x = int(input("Enter the x value "))
        y = int(input("Enter the y value "))

        result = cv2.pointPolygonTest(cnt, (x, y), True)
        if result > 0:
            print("Points is inside and distance from the contour is : ", result)
        elif result < 0:
            print("Points is outside and distance from the contour is : ", result)
        else:
            print("Points is on the contour: ", result)
        img = cv2.circle(image.copy(), (x, y), 1, (0, 0, 0), 2)
        cv2.imshow('Image contours', img)
        cv2.waitKey(0)
        if input("Quit-->(y/n)") == "y":
            break
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()



