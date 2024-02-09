import cv2
import matplotlib.pyplot as plt

img = cv2.imread("./imgs/face.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

face_cascade = cv2.CascadeClassifier("./xml/face.xml")
faces = face_cascade.detectMultiScale(img)

for x,y,w,h in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)

plt.imshow(img)
plt.show()