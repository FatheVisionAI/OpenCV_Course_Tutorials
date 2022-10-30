# FatheVision AI  code
import cv2


def cropped_image(img, crop_list):
    """
    crop the image
    Args:
        img: input image
        crop_list: crop list with [x1, y1, x2, y2]

    Returns:
        crop image
    """
    crop_img = img[crop_list[1]:crop_list[3], crop_list[0]:crop_list[2]]  # y1:y2, x1:x2
    return crop_img


def main():
    image_path = "../data/horse.jpg"
    image = cv2.imread(image_path)

    crop_list = [193, 44, 472, 310]  # x1, y1, x2, y2
    crop_image = cropped_image(image, crop_list)
    cv2.imshow("original image", image)
    cv2.imshow("crop image", crop_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
