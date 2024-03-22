import cv2
from playsound import playsound

fire_cascade = cv2.CascadeClassifier('cascade.xml')

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    fires = fire_cascade.detectMultiScale(gray, 1.1, 5)

    for (x, y, w, h) in fires:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        playsound('alarm_sound.m4a') 

    cv2.imshow('Fire Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
