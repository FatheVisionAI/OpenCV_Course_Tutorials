# FatheVision AI  code
import sys

import cv2
import numpy as np


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


def rectangle(img, cnt):
    """
    fit rectangle in contour
    Args:
        img: input image
        cnt: input contour

    Returns:
        image with rectangle drawn over the contour.
    """
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
    return img


def rotated_rectangle(img, cnt):
    """
    fit rotated rectangle in contour
    Args:
        img: input image
        cnt: input contour

    Returns:
        image with rotated rectangle drawn over the contour.
    """
    rect = cv2.minAreaRect(cnt)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    cv2.drawContours(img, [box], 0, (0, 0, 255), 2)
    return img


def ellipse(img, cnt):
    """
    fit ellipse in contour
    Args:
        img: input image
        cnt: input contour

    Returns:
        image with ellipse drawn over the contour.
    """
    elp = cv2.fitEllipse(cnt)
    cv2.ellipse(img, elp, (0, 0, 255), 2)
    return img


def line(img, cnt):
    """
    fit line in contour
    Args:
        img: input image
        cnt: input contour

    Returns:
        image with line drawn over the contour.
    """
    rows, cols = img.shape[:2]
    [vx, vy, x, y] = cv2.fitLine(cnt, cv2.DIST_L2, 0, 0.01, 0.01)
    left_y = int((-x * vy / vx) + y)
    right_y = int(((cols - x) * vy / vx) + y)
    cv2.line(img, (cols - 1, right_y), (0, left_y), (0, 0, 255), 2)
    return img


def circle(img, cnt):
    """
    fit circle in contour
    Args:
        img: input image
        cnt: input contour

    Returns:
        image with circle drawn over the contour.
    """
    (x, y), radius = cv2.minEnclosingCircle(cnt)
    cv2.circle(img, (int(x), int(y)), int(radius), (0, 0, 255), 2)
    return img


def main():
    image_path = "../data/ballon.jpg"
    image = cv2.imread(image_path)

    contours = find_contours(image)
    cnt = contours[0]
    cv2.drawContours(image, contours, -1, (0, 255, 0), 2, cv2.LINE_AA)

    while True:
        print("****************")
        print("Enter your choice")
        print("1: Rectangle")
        print("2: Rotated Rectangle")
        print("3: Ellipse")
        print("4: Line")
        print("5: Circle")
        print("q: quit")
        choice = input("Enter your choice ")

        if choice == "1":
            img = rectangle(image.copy(), cnt)
        elif choice == "2":
            img = rotated_rectangle(image.copy(), cnt)
        elif choice == "3":
            img = ellipse(image.copy(), cnt)
        elif choice == "4":
            img = line(image.copy(), cnt)
        elif choice == "5":
            img = circle(image.copy(), cnt)
        elif choice == "q":
            sys.exit(0)
        else:
            print("****  wrong choice  ****")
            continue
        cv2.imshow('Image contours', img)
        cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
