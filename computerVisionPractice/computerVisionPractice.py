import cv2
#read webcam
webcam = cv2.VideoCapture(0) # the argument is the number of the webcam you want to access. most likely to be 0

while True: # unlike video reading, with a webcam there is no end to the number of frames. we decid whent eh video/webcam is over
  ret, frame = webcam.read()
  cv2.imshow('frame', frame)
  if cv2.waitKey(40) & 0xFF == ord('q'): # when we past 40 miliseconds and when the user presses q
    break


webcam.release
cv2.destroyAllWindows()