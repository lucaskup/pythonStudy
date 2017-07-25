import cv2,time

face_cascade = cv2.CascadeClassifier('Files/haarcascade_frontalface_default.xml')
video=cv2.VideoCapture(0)
first_frame=None

while True:
    check, frame = video.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(21,21),0)


    if first_frame is None:
        first_frame = gray
        continue

    delta_frame=cv2.absdiff(first_frame,gray)
    thresh_frame=cv2.threshold(delta_frame,30,255,cv2.THRESH_BINARY)[1]
    thresh_frame=cv2.dilate(thresh_frame,None,iterations=2)

    (cnts,_)=cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    #for countour in cnts:
    #    if cv2.contourArea(countour) <1000:
    #        continue
    #    (x,y,w,h)=cv2.boundingRect(countour)
    #    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)

    cv2.imshow('first_frame',first_frame)
    cv2.imshow('blury',gray)
    cv2.imshow('delta_frame',delta_frame)
    cv2.imshow('thresh_frame',thresh_frame)

    #faces = face_cascade.detectMultiScale(gray_img,
    #scaleFactor=1.1,
    #minNeighbors=5)
    #for x, y, w, h in faces:
    #    cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),3)


    #cv2.imshow("Capt",frame)
    key = cv2.waitKey(1)


print(a)
video.release()
cv2.destroyAllWindows
