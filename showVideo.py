import cv2

if __name__ == '__main__':
    cap = cv2.VideoCapture('short_drone_video.avi')

    while cap.isOpened():
        (ret, frame) = cap.read()

        if ret:
            cv2.imshow('frame', frame)

        if cv2.waitKey(1) == ord('q') or cv2.getWindowProperty('frame', 0):
            break

    cap.release()
    cv2.destroyAllWindows()
