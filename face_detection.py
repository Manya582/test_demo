import cv2

face = cv2.CascadeClassifier("test.xml")

def image(gray, img):
    faces=face.detectMultiScale(gray,1.2,4)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    return img


video_capture = cv2.VideoCapture(0)


while True:
    _, img = video_capture.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    canvas = image(gray, img)
    cv2.imshow('Video', canvas)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()