import cv2
import time
from hands.TrackingModule import HandDetector

def main():
  capture = cv2.VideoCapture(0)

  hand_detector = HandDetector()

  currTime = 0
  prevTime = 0

  while True:
    success, imageBGR = capture.read()

    if success:
      # Proccess the current frame
      result = hand_detector.detect_hand(imageBGR)

      hand_detector.process_hands_detected(imageBGR, result, True)

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
      cv2.putText(imageBGR, str(fps_counter), (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, color_fps_counter, 2)

      cv2.imshow("Image", imageBGR)

    cv2.waitKey(1)

    # Check for X button
    if cv2.getWindowProperty("Image", cv2.WND_PROP_VISIBLE) != 1:
      cv2.destroyWindow("Image")
      break

if __name__ == '__main__':
  main()
