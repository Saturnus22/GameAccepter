import time

import pyautogui


while True:
    time.sleep(1)
    loc = pyautogui.locateOnScreen('img.png',confidence=.5)
    if loc:
        time.sleep(3)
        pyautogui.click(loc)



