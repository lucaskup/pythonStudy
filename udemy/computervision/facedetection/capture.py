import cv2,time

face_cascade = cv2.CascadeClassifier('Files/haarcascade_frontalface_default.xml')
video=cv2.VideoCapture(0)
a=0
while True:
    a+=1
    check, frame = video.read()
    #print(check)
    #print(frame)
    #time.sleep(3)
    gray_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray_img,
    scaleFactor=1.1,
    minNeighbors=5)
    #print(faces)
    for x, y, w, h in faces:
        #print(x,y,w,h)
        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),3)


    cv2.imshow("Capt",frame)
    key = cv2.waitKey(1)


print(a)
video.release()
cv2.destroyAllWindows
