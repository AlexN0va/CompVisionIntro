import cv2
from PIL import Image
import numpy as np

from util import get_limits

cam = cv2.VideoCapture(0) #make our camera instance
yellow = [0,255,255]  # Yello win bgr color space

while True: # we want to stream from out camera continuously
    #grab frame
    ret, frame = cam.read() #lets grab our frame

    #Filter Creation
    #Before you stary any project consider what kind of project you are making. what color space we want to use
    #Since we are trying to detect color lets use the HSV color space ( Hue, Saturation, Value)
    # Essientally what is happening is that we get the whole Hue region of the wanted color and compare the pixels of our camera to that range of values
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # Turn our frames in HSV

    lowerLimit, UpperLimit = get_limits(yellow) #Get the yellow value ranges

    filter = cv2.inRange(hsvImage, lowerLimit, UpperLimit) # Apply a filter than whill make our image binary. yellow HUE values will appear white

    #Draw bounding box for yellow objects
    filter_ = Image.fromarray(filter)# converting our image form a nparray to a pillow image

    bbox = filter_.getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox

        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 5)





    #display frame
    cv2.imshow("window name", frame) # display that frame 
    if cv2.waitKey(40) & 0xFF == ord('q'): # when we past 40 miliseconds and when the user presses q
        break


cam.release() # release the camera's memory
cv2.destroyAllWindows()