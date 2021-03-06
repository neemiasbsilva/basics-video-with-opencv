# Drawing on Video

import cv2

# CALLBACK FUNCTION RECTANGLE


def draw_rectangle(event, x, y, flags, param):

    global pt1, pt2, topLeft_clicked, botRight_clicked

    if event == cv2.EVENT_LBUTTONDOWN:

        # RESET THE RECTANGLE (IT CHECKS IF THE RECT THERE)
        if topLeft_clicked and botRight_clicked:
            pt1 = (0, 0)  # top left
            pt2 = (0, 0)  # right left
            topLeft_clicked = False
            botRight_clicked = False

        if topLeft_clicked == False:
            pt1 = (x, y)
            topLeft_clicked = True
        elif botRight_clicked == False:
            pt2 = (x, y)
            botRight_clicked == True


# GLOBAL VARIABLE
pt1 = (0, 0)  # top left
pt2 = (0, 0)  # right left
topLeft_clicked = False
botRight_clicked = False

# CONNECT TO THE CALLBACK

cap = cv2.VideoCapture(0)

cv2.namedWindow('Test')
cv2.setMouseCallback('Test', draw_rectangle)

while True:

    ret, frame = cap.read()

    # DRAWING ON THE FRAME BASED OFF THE GLOBAL VARIABLES
    if topLeft_clicked:
        cv2.circle(frame, center=pt1, radius=5,
                   color=(0, 0, 255), thickness=-1)

    if topLeft_clicked and botRight_clicked:
        cv2.rectangle(frame, pt1, pt2, (0, 0, 255), 3)

    cv2.imshow('Test', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
