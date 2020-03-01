import cv2


capture = cv2.VideoCapture(0)
while True:
    ret, frame = capture.read()
    cv2.imshow("frame",frame)
    if cv2.waitKey(50) & 0xFF == ord("Q"):
        break

capture.release()
cv2.destroyAllWindows()
