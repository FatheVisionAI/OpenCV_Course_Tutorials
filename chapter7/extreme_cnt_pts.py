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


def draw_points(img, cnt):
    """
    get the leftmost_pt, rightmost_pt, topmost_pt and bottommost_pt of the cnt and plot on the image
    Args:
        img: input image
        cnt: input contour

    Returns:
        image with point drawn on it
    """
    leftmost_pt = tuple(cnt[cnt[:, :, 0].argmin()][0])
    rightmost_pt = tuple(cnt[cnt[:, :, 0].argmax()][0])
    topmost_pt = tuple(cnt[cnt[:, :, 1].argmin()][0])
    bottommost_pt = tuple(cnt[cnt[:, :, 1].argmax()][0])

    for pt in [leftmost_pt, rightmost_pt, topmost_pt, bottommost_pt]:
        img = cv2.circle(img, pt, 1, (255, 0, 0), 2)
    return img


def main():
    image_path = "../data/ballon.jpg"
    image = cv2.imread(image_path)

    contours = find_contours(image)
    cnt = contours[0]
    cv2.drawContours(image=image, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2,
                     lineType=cv2.LINE_AA)

    image = draw_points(image, cnt)
    cv2.imshow('Image contours', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()


