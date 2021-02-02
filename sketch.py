#imports
import cv2
import numpy as np

# This is the sketch generator function
def sketch(img):
    # Convert BGR into Grayscale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Clean the picture with Gaussian blur
    img_gray_blur = cv2.GaussianBlur(img_gray, (7,7), 0)
    
    # Extract edges with Canny
    canny_edge  =cv2.Canny(img_gray_blur, 10, 50)
    
    # Invert the image and binarize for sketch
    ret, mask = cv2.threshold(canny_edge, 70, 255, cv2.THRESH_BINARY_INV)
    return mask

# Initialize the webcam, capture is the object from video capture
# It has a boolean indicating the incoming stream
# It also has the image frames collected from the stream of cam

capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()
    cv2.imshow("The Live Sketch", sketch(frame))
    if cv2.waitKey(1) == 27: # Press Escape key to close
        break
        
# Releive camera and close windows
capture.release()
cv2.destroyAllWindows()
