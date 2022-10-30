# FatheVision AI  code
import cv2
import numpy as np
from PIL import Image


def main():
    image_path = "../data/horse.jpg"
    image = Image.open(image_path)  # reading the image through PILLOW

    # image.show()

    image = np.asarray(image)  # converting the PILLOW image to numpy array
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)  # color conversion from RGB to BGR

    cv2.imwrite('xyz.jpg', image)


if __name__ == "__main__":
    main()
