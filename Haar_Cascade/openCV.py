import cv2 as cv

cap = cv.VideoCapture(0)

face_cascade = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_default.xml")
                                                            
while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed the Capture")
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    for (x,y,w,h) in faces:
        cv.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 3)
        cv.putText(frame, "Detected Face", (x, y), cv.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 5)

    cv.imshow("Video Frame", frame)
    if cv.waitKey(1) & 0xFF == ord('d'):
        break

cap.release()
cv.destroyAllWindows()
   