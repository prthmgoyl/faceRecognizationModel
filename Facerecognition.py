import cv2

face_cap = cv2.CascadeClassifier("C:/Users/asd/AppData/Local/Programs/Python/Python311/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")

video_cap  = cv2.VideoCapture(0)
while 1:
    ret , videodata = video_cap.read()
    col = cv2.cvtColor(videodata , cv2.COLOR_BGR2GRAY)

    faces = face_cap.detectMultiScale(
        col,
        scaleFactor = 1.1,
        minNeighbors =5,
        minSize = (30,30),
        flags = cv2.CASCADE_SCALE_IMAGE
    )
    for(x,y,w,h) in faces:
        cv2.rectangle(videodata,(x,y),(x+w,y+h),(0,255,0),2)

    cv2.imshow("Live",videodata)
    if cv2.waitKey(10) == ord("c"):
        break

video_cap.release()