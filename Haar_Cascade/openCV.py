import cv2 as cv

cap = cv.VideoCapture(0)

face_cascade = cv.CascadeClassifier( cv.data.haarcascades + "haarcascade_frontalface_default.xml")
eyes_cascade = cv.CascadeClassifier( cv.data.haarcascades + "haarcascade_eye.xml")                                                            
mouth_cascade = cv.CascadeClassifier( cv.data.haarcascades + "haarcascade_smile.xml")                                                            

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed the Capture")
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    for (x,y,w,h) in faces:
        cv.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 2)
        cv.putText(frame, "Detected Face", (x, y-10), cv.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2, cv.LINE_AA)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        eyes = eyes_cascade.detectMultiScale(roi_gray, scaleFactor=1.3, minNeighbors=10)
        mouth = mouth_cascade.detectMultiScale(roi_gray, scaleFactor=1.3, minNeighbors=10)

        for (ex,ey,ew,eh) in eyes:
            cv.rectangle(frame, (x+ex, y+ey), (x+ex+ew, y+ey+eh), (0,255, 0), 2)
            cv.putText(frame, "Eye", (x+ex, (y+ey)-10), cv.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2 , cv.LINE_AA)

        for (mx, my, mw, mh) in mouth:
            cv.rectangle(frame, (x+mx, y+my), (x+mx+mw, y+my+mh), (0, 200, 0), 2)
            cv.putText(frame, "Mouth",(x+mx , (y+my)- 10), cv.FONT_HERSHEY_SIMPLEX, 1, (100,0,0), 2)
    cv.imshow("Video Frame", frame)
    if cv.waitKey(1) & 0xFF == ord('d'):
        break

cap.release()
cv.destroyAllWindows()
   