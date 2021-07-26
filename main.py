import mediapipe as mp
import cv2
import time

capture = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1)
mpDraw = mp.solutions.drawing_utils

currTime = 0
prevTime = 0

while True:
  success, image = capture.read()

  # Proccess the current frame
  imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
  result = hands.process(imageRGB).multi_hand_landmarks

  if result:
    for handLms in result:
      mpDraw.draw_landmarks(image, handLms, mpHands.HAND_CONNECTIONS)

  # FPS things
  currTime = time.time()
  fps_counter = int(1 / (currTime - prevTime))
  prevTime = currTime

  # Set the color of fps counter
  if fps_counter >= 30:
    color_fps_counter = (0, 255, 0)
  elif fps_counter >= 10: 
    color_fps_counter = (0, 255, 255)
  else:
    color_fps_counter = (0, 0, 255)

  # Set the text of fps counter in the screen
  cv2.putText(image, str(fps_counter), (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, color_fps_counter, 2)

  cv2.imshow("Image", image)
  cv2.waitKey(1)

  # Check for X button
  if cv2.getWindowProperty("Image", cv2.WND_PROP_VISIBLE) != 1:
    cv2.destroyWindow("Image")
    break
