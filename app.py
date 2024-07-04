import pyautogui
from time import sleep
pyautogui.moveTo(750,471, duration=2)
for i in range (100):
    sleep(.5)
    pyautogui.click()