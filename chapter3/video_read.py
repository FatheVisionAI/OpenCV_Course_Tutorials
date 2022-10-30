# FatheVision AI  code
import sys

import cv2


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
            cv2.imshow('Video Play', frame)
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
    print("**** video complete ****")


if __name__ == "__main__":
    main()
