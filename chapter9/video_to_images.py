# FatheVision AI  code
import cv2
import os


def main():
    image_directory_path = "images"
    video_path = "../data/lion_video.mp4"
    count = 0

    if not os.path.exists(image_directory_path):
        os.makedirs(image_directory_path)

    cap = cv2.VideoCapture(video_path)
    while True:
        ret, frame = cap.read()
        if ret is True:
            cv2.imwrite(image_directory_path + "/" + str(count) + ".jpg", frame)
            count = count + 1
            cv2.imshow("video_reading", frame)
        else:
            break
        if cv2.waitKey(1) == ord("q"):
            break
    cv2.destroyAllWindows()
    cap.release()


if __name__ == "__main__":
    main()
