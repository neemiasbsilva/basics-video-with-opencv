#using videos Files

import cv2
import time

cap = cv2.VideoCapture(
    '/Users/neemiasbsilva/Downloads/Computer-Vision-with-Python/DATA/video_capture.mp4')

if cap.isOpened() == False:
    print('ERRO FILE NOT FOUND OR WRONG CODEC USED!')


while cap.isOpened():

    ret, frame = cap.read()

    if ret == True:

        # writer 20 FPS
        time.sleep(1/20)
        cv2.imshow('frame', frame)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    else:
        break


cap.release()
cv2.destroyAllWindows()
