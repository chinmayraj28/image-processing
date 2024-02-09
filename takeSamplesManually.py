import cv2
cam = cv2.VideoCapture(0)
i = 0
while True:
    ret,img = cam.read()
    cv2.imshow("Webcam",img)
   
    mypic = "./samples/images"+str(i)+".png"
    if cv2.waitKey(1) == ord("e"):
        i += 1
        
        cv2.imwrite(mypic,img)
    if cv2.waitKey(1) == ord("q"):
        break
cam.release()
cv2.destroyAllWindows()