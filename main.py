# Import required libraries
import cv2
import numpy as np
import dlib
from pyfirmata2 import Arduino #import library from pyfirmata2 to detect Arduino
import time #time library to be able setup lenght of led lighting

class AnalogPrinter:

    def __init__(self):
        # sampling rate: 10Hz
        self.samplingRate = 10
        self.timestamp = 0
        self.board = Arduino(PORT)

    def start(self):
        self.board.analog[0].register_callback(self.myPrintCallback)
        self.board.samplingOn(1000 / self.samplingRate)
        self.board.analog[0].enable_reporting()
        return self.board.analog[0].read()

    def myPrintCallback(self, data):
        # print("opana")
        # print("%f,%f" % (self.timestamp, data))
        self.timestamp += (1 / self.samplingRate)

    def stop(self):
        self.board.samplingOff()
        self.board.exit()

ALCOHOL_LIMIT = 0.4
PORT = Arduino.AUTODETECT 
analogPrinter = AnalogPrinter()


# Connects to your computer's default camera
cap = cv2.VideoCapture(0)
 
 
# Detect the coordinates
detector = dlib.get_frontal_face_detector()
 
 
# Capture frames continuously
while True:
 
    # Capture frame-by-frame
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
 
    # RGB to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
 
    # Iterator to count faces
    i = 0
    for face in faces:
 
        # Get the coordinates of faces
        x, y = face.left(), face.top()
        x1, y1 = face.right(), face.bottom()
        cv2.rectangle(frame, (x, y), (x1, y1), (0, 255, 0), 2)
 
        # Increment iterator for each face in faces
        i = i+1
 
        # Display the box and faces
        cv2.putText(frame, 'face num'+str(i), (x-10, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        # print(face, i)
    alco = analogPrinter.start()
    if i == 1 and alco is not None and alco < ALCOHOL_LIMIT and alco != 0:
      analogPrinter.board.digital[5].write(1) # green light
      analogPrinter.board.digital[6].write(0) # red light
    else:
      analogPrinter.board.digital[5].write(0)
      analogPrinter.board.digital[6].write(1)
 
    # Display the resulting frame
    cv2.imshow('frame', frame)
 
    # This command let's us quit with the "q" button on a keyboard.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 
 
# Release the capture and destroy the windows
cap.release()
cv2.destroyAllWindows()
analogPrinter.stop()