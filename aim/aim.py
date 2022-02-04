import numpy as np
import cv2 as cv
from PIL import ImageGrab, Image
import pyautogui
import time
import mouse

cible = cv.imread('cible.png')
cible_cv = cv.cvtColor(np.array(cible), cv.COLOR_BGR2GRAY)

for i in range(31):
	img = ImageGrab.grab()
	img_cv = cv.cvtColor(np.array(img), cv.COLOR_BGR2GRAY)
	pt = cv.matchTemplate(img_cv, cible_cv, cv.TM_CCOEFF_NORMED)
	min_val, max_val, min_loc, max_loc= cv.minMaxLoc(pt)
	pyautogui.click(max_loc)
