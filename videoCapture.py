import cv2

video = cv2.VideoCapture("nvideo.mp4")
print(video.isOpened())
while True:
    ret,frame = video.read()
    print(ret)
    if not ret:
        break
    cv2.imshow("Video Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()