# FatheVision AI  code
import cv2
from sift_algo import get_keypoint_and_descriptor


def bf_matchers(disp1, disp2, bf_obj):
    """
    brute force matcher function matches the feature's between the image1 and image2
    Args:
        disp1: descriptor of first images from the sift
        disp2: descriptor of second images from the sift
        bf_obj: brute force object

    Returns:
        sorted matches from the brute force matcher
    """
    matches = bf_obj.match(disp1, disp2)
    matches = sorted(matches, key=lambda x: x.distance)
    return matches


def main():
    sift = cv2.SIFT_create()
    bf = cv2.BFMatcher()

    image_path1 = "../data/horse_face.jpg"
    image_path2 = "../data/horse.jpg"

    image1 = cv2.imread(image_path1)  # reading the image
    image2 = cv2.imread(image_path2)  # reading the image

    keypoint1, descriptor1 = get_keypoint_and_descriptor(image1, sift)
    keypoint2, descriptor2 = get_keypoint_and_descriptor(image2, sift)

    matches = bf_matchers(descriptor1, descriptor2, bf)
    image_matcher = cv2.drawMatches(image1, keypoint1, image2, keypoint2, matches, None)  # plot matches on the images

    cv2.imshow("image matching", image_matcher)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
