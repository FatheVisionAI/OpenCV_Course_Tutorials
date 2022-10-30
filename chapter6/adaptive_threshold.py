# FatheVision AI  code
import cv2


def apply_adaptive_threshold(img):
    """
    convert a gray scale image into binary image based variable threshold for a given region
    
    Args:
        img: gray scale input image

    Returns:
        binary image
        """
    thresh_img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                    cv2.THRESH_BINARY, 199, 10)
    return thresh_img

def main():
    image_path = "../data/document.jpg"
    image = cv2.imread(image_path)
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh_image = apply_adaptive_threshold(image_gray)

    cv2.namedWindow("original_image")        # Create a named window
    cv2.moveWindow("original_image", 0, 0)
    cv2.namedWindow("threshold_image")        # Create a named window
    cv2.moveWindow("threshold_image", 800, 0)

    cv2.imshow('original_image', image)
    cv2.imshow('threshold_image', thresh_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
