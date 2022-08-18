import pyautogui
import keyboard
import time


while not keyboard.is_pressed('q'):

    pic = pyautogui.screenshot()
    time.sleep(0.2)
    r,g,b = pic.getpixel((752, 560))
    time.sleep(0.2)

    if (r == 28 or r == 29 or r == 30 or r == 31 or r == 33 ) and (g == 35 or g == 36 or g == 37 or g == 38) and  (b == 40 or b == 41 or b == 42):
        pyautogui.click(752, 560)

    time.sleep(2)


# import pyautogui
# pyautogui.displayMousePosition()