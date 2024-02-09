import cv2
cam = cv2.VideoCapture(0)
i = 0
while i <= 200:
    ret,img = cam.read()
    cv2.imshow("Webcam",img)
   
    mypic = "./samples/img"+str(i)+".png"
    cv2.imwrite(mypic,img)
    i += 1

cam.release()
cv2.destroyAllWindows()