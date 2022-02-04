from ctypes import windll

dc= windll.user32.GetDC(0)

def getpixel(x,y):
    return windll.gdi32.GetPixel(dc,x,y)

for i in range(5):
	# WAIT FOR THE GAME TO START (BLUE SCREEN)
	while(getpixel(300, 300) != 13731627):
		pass
	pyautogui.click((300, 300)) # Click on the blue screen

	# WAIT FOR THE END OF RED COLOR TO CLICK (BLUE SCREEN)
	while(getpixel(300, 300) == 3548878):
		pass
	pyautogui.click((300, 300)) # Click on the green screen