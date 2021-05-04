import pyautogui
import keyboard
from pynput.mouse import Button, Controller

mouse = Controller()

# Use pyautogui to determine the X and Y mouse position.
xPos = [733, 875, 1015, 1160]
y = 725

darknessVal = 2.36

# Columns
lock = [False, False, False, False]

while keyboard.is_pressed('q') == False:

  for col, x in enumerate(xPos):

    rgb = pyautogui.pixel(x, y)

    # Calculate the darkness value
    blackVal = ( rgb[0] * 0.3 ) + ( rgb[1] * 0.59 ) + ( rgb[2] * 0.11 )
    
    if lock[col]:
      if blackVal > darknessVal:
        lock[col] = False
      else:
        continue

    # How dark the pixel color is
    if blackVal <= darknessVal:
      mouse.release(Button.left)
      mouse.position = (x, y)
      lock[col] = True
      mouse.press(Button.left)
      
mouse.release(Button.left)
print("Exit successfully!")