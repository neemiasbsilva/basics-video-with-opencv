# Drawing on Video

import cv2

cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

x = width // 2
y = height // 2

# width and height of RECTANGLE
w = width // 4
h = height // 4

# Bottom right x+w, y+h

while True:

    ret, frame = cap.read()

    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 4)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
