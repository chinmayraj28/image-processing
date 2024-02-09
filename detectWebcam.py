import cv2

face_cascade = cv2.CascadeClassifier("./xml/face.xml")
eye_cascade = cv2.CascadeClassifier("./xml/eye.xml")

webcam = cv2.VideoCapture(0)

while True:
    ret, frame = webcam.read()
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    faces = face_cascade.detectMultiScale(rgb_frame) 
    eyes = eye_cascade.detectMultiScale(rgb_frame)
    
    i = 0

    for x, y, w, h in faces:
        cv2.putText(frame, "Face", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        # print(f'(x, y) {x}, {y}')
        # print(f'(x+w, y+h) {x+w}, {y+h}')
    for x, y, w, h in eyes:
        cv2.putText(frame, "Eyes", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv2.imshow('Face Detection', frame)
    if cv2.waitKey(1) == ord("q"):
        break

webcam.release()
cv2.destroyAllWindows()