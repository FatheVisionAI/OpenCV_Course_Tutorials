# FatheVision AI  code
import cv2


def resize_image(img, shape):
    """
    resized the image
    Args:
        img: input shape
        shape: new shape of image
    Returns:
        resized image
    """
    resized_img = cv2.resize(img, shape)
    return resized_img


def main():
    image_path = "../data/horse.jpg"
    image = cv2.imread(image_path)
    height, width, channel = image.shape
    print("image shape in Height x Width x Channel ", image.shape)
    new_height = height//2
    new_width = width//2
    resized_image = resize_image(image, (new_width, new_height))
    print("resized image shape in Height x Width x Channel ", resized_image.shape)
    cv2.imshow("original image", image)
    cv2.imshow("resized image", resized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
