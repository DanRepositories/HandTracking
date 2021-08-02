import time
import cv2

GOOD_FPS_QUANTITY = 30
ACEPTABLE_FPS_QUANTITY = 15

class FPSCounter():
  def __init__(self):
    self.curr_time = 0
    self.prev_time = 0
    self.current_fps = 0


  def update_times(self):
    self.curr_time = time.time()
    self.current_fps = int(1 / (self.curr_time - self.prev_time))
    self.prev_time = self.curr_time


  def draw_fps(self, imageBGR):
    # Set the color of fps counter
    if self.current_fps >= GOOD_FPS_QUANTITY:
      color_fps_counter = (0, 255, 0)
    elif self.current_fps >= ACEPTABLE_FPS_QUANTITY:
      color_fps_counter = (0, 255, 255)
    else:
      color_fps_counter = (0, 0, 255)

    # Set the text of fps counter in the screen
    cv2.putText(imageBGR, str(self.current_fps), (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, color_fps_counter, 2)

