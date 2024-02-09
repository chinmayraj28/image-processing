import cv2
import matplotlib.pyplot as plt

img = cv2.imread("./imgs/face.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

face_cascade = cv2.CascadeClassifier("./xml/freshOrange.xml")
faces = face_cascade.detectMultiScale(img)

for x,y,w,h in faces:
    cv2.putText(img, "Fresh Orange", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)

plt.imshow(img)
plt.show()