# FatheVision AI  code
import cv2


def blend_image(img1, img2):
    """
    blend two input image to make single image

    Args:
        img1: input image 1
        img2: input image 2

    Returns:
        blended image
    """
    img = cv2.addWeighted(img1, 0.5, img2, 0.5, 2)
    return img


def main():
    image_path1 = "../data/horse.jpg"
    image_path2 = "../data/horse1.jpg"

    image1 = cv2.imread(image_path1)
    image2 = cv2.imread(image_path2)

    height, width, _ = image1.shape
    image2 = cv2.resize(image2, (width, height))
    print(image1.shape, image2.shape)
    image = blend_image(image1, image2)
    cv2.imshow("Image", image)
    cv2.waitKey(0)


if __name__ == "__main__":
    main()
