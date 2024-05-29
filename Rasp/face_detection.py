import cv2
import time

# Load the cascade
face_cascade = cv2.CascadeClassifier('/home/ducchung/Desktop/haarcascade_frontalface_default.xml')

# To capture video from webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)   # set Width
cap.set(4, 480)   # set Height

while True:
    # Read the framed
    _, img = cap.read()
    
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 6)
    
    nfaces = len(faces)
    
    # Draw the rectangle around each face
    for n in range(nfaces):
        (x, y, w, h) = faces[n]
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 1)

    # Display
    cv2.imshow('img', img)
    time.sleep(.05)

# Release the VideoCapture object
cap.release()
