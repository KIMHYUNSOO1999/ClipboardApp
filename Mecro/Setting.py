import pyautogui
import time
from PIL import ImageGrab

def mouse():
    try:
        while True:
            x, y = pyautogui.position()
            print(f"현재 마우스 위치: X={x}, Y={y}", end='\r') 
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\n종료됨.")

def show():
    UNICODE_BOX = (1692, 316, 1729, 332)
    image = ImageGrab.grab(bbox=UNICODE_BOX)
    image.save("screenshot.png") 

if __name__ == '__main__':
    mouse()