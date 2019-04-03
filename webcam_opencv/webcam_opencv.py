import cv2

faceCascade = cv2.CascadeClassifier('data/haarcascades/haarcascade_frontalface_default.xml')
video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()

    grayImg = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        grayImg,
        scaleFactor=2.7,
        minNeighbors=5,
        minSize=(30, 30),
    )
    
    found = False

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        found = True

    cv2.imshow('Video', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    if found and int(faces.shape[0]) == 1:
        print('Detected', str(faces.shape[0]), 'face')
    elif found and int(faces.shape[0]) > 1:
        print('Detected', str(faces.shape[0]), 'faces')
    elif not found:
        print('Detected 0 faces')
    

video_capture.release()
cv2.destroyAllWindows()