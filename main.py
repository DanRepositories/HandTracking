import cv2
from hands.TrackingModule import HandDetector
from utils.FpsCounter import FPSCounter

def main():
  capture = cv2.VideoCapture(0)

  hand_detector = HandDetector()
  fps_counter = FPSCounter()

  while True:
    success, imageBGR = capture.read()

    if success:
      # Proccess the current frame
      result = hand_detector.detect_hand(imageBGR)
      hand_detector.process_hands_detected(imageBGR, result, True)

      # FPS things
      fps_counter.update_times()
      fps_counter.draw_fps(imageBGR)

      cv2.imshow("Image", imageBGR)

    cv2.waitKey(1)

    # Check for X button
    if cv2.getWindowProperty("Image", cv2.WND_PROP_VISIBLE) != 1:
      cv2.destroyWindow("Image")
      break

if __name__ == '__main__':
  main()

