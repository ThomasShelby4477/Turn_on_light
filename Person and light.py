import cv2
import math
import serial
from ultralytics import YOLO

ser = serial.Serial('COM4', 9600, timeout=1)

def turn_relay(state):
    ser.write(b'1' if state else b'0')  # Send '1' to turn relay ON, '0' to turn relay OFF
    print("Turning relay ON" if state else "Turning relay OFF")

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

model = YOLO("../Yolo-Weights/yolov8n.pt")

while True:
    success, img = cap.read()
    results = model(img, stream=True)
    persons_count = sum(1 for r in results for box in r.boxes if int(box.cls[0]) == 0 and box.conf[0] > 0.5)

    cv2.putText(img, f'Persons: {persons_count}', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    turn_relay(persons_count >= 1)
    cv2.imshow("Image", img)
    cv2.waitKey(1)