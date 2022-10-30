# FatheVision AI  code
import cv2


def get_keypoint_and_descriptor(img, sift_obj):
    """
    getting the features and descriptor for the input image through SIFT algorithm
    Args:
        img: input image for which we want to get the keypoint and descriptor
        sift_obj: SIFT object

    Returns:
        keypoint and descriptor for the input image
    """

    image_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    kps, descriptor = sift_obj.detectAndCompute(image_gray, None)
    return kps, descriptor


def main():
    sift = cv2.SIFT_create()

    image_path = "../data/horse.jpg"
    image = cv2.imread(image_path)  # reading the image

    keypoint, descriptor = get_keypoint_and_descriptor(image, sift)
    # print("length of keypoint ", len(keypoint))
    # print("shape of descriptor is ", descriptor.shape)
    # print('keypoint are ', keypoint)
    # print('descriptor is ', descriptor)

    image_feature = cv2.drawKeypoints(image, keypoint, None)  # plotting the keypoint on the input image

    cv2.imshow("SIFT image", image_feature)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
