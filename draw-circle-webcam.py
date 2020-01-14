import cv2

# Create a function on a cv2 event (left button click)


# mouse callback function
def draw_circle(event, x, y, flags, param):
    global center, clicked
    
    # get mouse click on down and track center
    if event == cv2.EVENT_LBUTTONDOWN:
        center = (x, y)
        clicked = False
    if event == cv2.EVENT_LBUTTONUP:
        clicked = True
        
        
    # Use boolean variable to track if the mouse has ben released
    
    
# Haven't draw anything yet!
center = (0, 0)
clicked = False

# Capture Video
cap = cv2.VideoCapture(0)
cv2.namedWindow('Test',)

# Create a named window for connections

# Bind draw_circle function to mouse clicks
cv2.setMouseCallback('Test', draw_circle)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Use if statement to see if clicked is true
    if clicked:
        # Draw circle
        cv2.circle(frame, center=center, radius=50, color=(255, 0, 0), thickness=5)
    
    # Display the resulting frame
    cv2.imshow('Test', frame)
    
    # This command Let's us quit with the 'q'button on a keyboard.
    # Simply pressing X on the window won't wokr!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()