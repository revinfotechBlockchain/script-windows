import pyautogui
import random
import time

data = True

while(data):

    t = random.randint(1,20)
    # print(t)
    x = random.randint(0, 1600)
    y = random.randint(0, 900)
    pyautogui.moveTo(x, y)

    if t > 10:
        pyautogui.keyDown("alt")
        pyautogui.press("tab")
        pyautogui.keyUp("alt")
    else:
        pyautogui.keyDown("ctrl")
        pyautogui.press("tab")
        pyautogui.keyUp("ctrl")
    time.sleep(t)