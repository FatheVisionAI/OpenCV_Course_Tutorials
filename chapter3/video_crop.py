# FatheVision AI  code
import sys

import cv2


def crop_image(img, crop_list):
    """
    crop the frame
    Args:
        img: input frame
        crop_list: crop list with [x1, y1, x2, y2]
    Returns:
        crop frame
    """
    cropped_frame = img[crop_list[1]:crop_list[3], crop_list[0]:crop_list[2]]
    return cropped_frame


def video_read(file_name):
    """
        video read function
        Args:
            file_name: video file path
        Returns:
    """
    cap = cv2.VideoCapture(file_name)
    if cap.isOpened() is False:
        print("Error opening video  file")
        sys.exit(0)
    while cap.isOpened():
        ret, frame = cap.read()
        if ret is True:
            crop_list = [600, 300, 1000, 700]
            frame_crop = crop_image(frame, crop_list)
            cv2.imshow('Crop Video Play', frame_crop)

        else:
            break
        if cv2.waitKey(1) == ord('q'):
            break
    cap.release()


def main():
    print("*****  Playing video *******")
    print("Press q: Quit")
    video_filename = "../data/lion_video.mp4"
    video_read(video_filename)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
