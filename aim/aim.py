import pyautogui
from time import sleep
import mouse


for i in range(31):
    coord = None
    while coord is None:
        coord = pyautogui.locateOnScreen(
            'cible.png', grayscale=True, confidence=0.6)

    pyautogui.click(coord)
