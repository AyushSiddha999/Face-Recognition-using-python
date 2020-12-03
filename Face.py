import cv2 #pip install opencv-python
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface.xml')
cap = cv2.VideoCapture(0)
img2 = cv2.imread('Test.jpg')
while True:
    _,img = cap.read(img2)
    font =cv2.FONT_HERSHEY_SIMPLEX
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1,4)
    for (x,y,w,h) in faces:
        cv2.circle(img,(x+w-105,y+h-110),130,(225,225,0),2)
        cv2.putText(img, "Ayush Parimal Siddha", (x+w-280,y+h-250),font,1,(225,0,225),2)
    cv2.imshow('Ayush Face test', img)
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
cap.releaseAll()