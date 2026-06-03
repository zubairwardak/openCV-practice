import cv2

video = cv2.VideoCapture("nvideo.mp4")

fourcc = cv2.VideoWriter_fourcc(*'mp4v')

width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

out = cv2.VideoWriter("./output_new.mp4", fourcc, 30, (width, height))

while True:
    ret, frame = video.read()
    if not ret:
        break
    frame = frame + 40
    out.write(frame)
    #cv2.imshow("Video Frame", frame)

out.release()
video.release()
cv2.destroyAllWindows()