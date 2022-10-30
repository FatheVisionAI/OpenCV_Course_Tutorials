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
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, 30.0, (1920, 1080))

    if cap.isOpened() is False:
        print("Error opening video  file")
        sys.exit(0)

    while cap.isOpened():
        ret, frame = cap.read()
        if ret is True:
            cv2.imshow('Video', frame)
            out.write(frame)

        else:
            break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()


print("*****  Playing video *******")
print("Press q: Quit")
video_filename = "../data/lion_video.mp4"
video_read(video_filename)
cv2.destroyAllWindows()
print("**** video saved complete ****")

