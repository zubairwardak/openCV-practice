from ultralytics import YOLO
import cv2

model = YOLO("best.pt")
capture = cv2.VideoCapture("hcopter1.mp4")

while True:
    ret, frame = capture.read()
    if not ret:
        break
    # results = model.track(frame, persist=True, tracker='botsort.yaml', verbose=False)
    results = model.track(frame, persist=True, tracker='bytetrack.yaml', verbose=False)
    annotated_frame = results[0].plot()  # ✅ THIS is a numpy image

    cv2.imshow("Camera", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
