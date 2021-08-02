import mediapipe as mp
import cv2

class HandDetector():
  def __init__(self, max_hands=1):
    self.max_hands = max_hands
    self.mpHands = mp.solutions.hands
    self.hands = self.mpHands.Hands(max_num_hands=self.max_hands)
    self.mpDraw = mp.solutions.drawing_utils


  def detect_hand(self, imageBGR):
    # Proccess the entered frame
    imageRGB = cv2.cvtColor(imageBGR, cv2.COLOR_BGR2RGB)
    result = self.hands.process(imageRGB).multi_hand_landmarks

    return result


  def process_hands_detected(self, imageBGR, result_processed_frame, draw_hands=False):
    if result_processed_frame:
      height, width, channel = imageBGR.shape

      for handLms in result_processed_frame:

        if draw_hands:
          self.draw_hand_detected(imageBGR, handLms)

        for index, landmark in enumerate(handLms.landmark):
          coord_x, coord_y = int(landmark.x * width), int(landmark.y * height)
          print(index, coord_x, coord_y)


  def draw_hand_detected(self, imageBGR, hand_landmarks):
    self.mpDraw.draw_landmarks(imageBGR, hand_landmarks, self.mpHands.HAND_CONNECTIONS)

