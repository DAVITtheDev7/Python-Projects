import pyautogui
import random

for i in range(500):
    x = random.randint(1,2000)
    y = random.randint(1,2000)
    pyautogui.moveTo(x,y)
    pyautogui.click()



