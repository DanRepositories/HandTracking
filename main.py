import mediapipe as mp
import cv2
import time

capture = cv2.VideoCapture(0)

while True:
  success, image = capture.read()

  cv2.imshow("Image", image)
  cv2.waitKey(100)

  # Check for X button
  if cv2.getWindowProperty("Image", cv2.WND_PROP_VISIBLE) != 1:
    cv2.destroyWindow("Image")
    break

