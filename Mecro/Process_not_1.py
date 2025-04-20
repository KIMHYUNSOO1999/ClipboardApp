"""
    Config
"""

import pyautogui
import pytesseract
import asyncio
from PIL import ImageGrab
import cv2
import numpy as np

"""
    사용자설정
"""

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
UNICODE_BOX = (1692, 316, 1729, 332) # 좌표
usercount = 20  # 개수 (가로 1줄 : 22개)

temp = []

"""
    함수
"""

# 이미지 인식 (전처리 포함)
def get_unicode_cv2():

    image = ImageGrab.grab(bbox=UNICODE_BOX)

    open_cv_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    gray = cv2.cvtColor(open_cv_image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    scale = 2
    thresh = cv2.resize(thresh, (0, 0), fx=scale, fy=scale, interpolation=cv2.INTER_LINEAR)
    blur = cv2.medianBlur(thresh, 3)
    text = pytesseract.image_to_string(blur, config='--psm 7')
    
    return ''.join(filter(str.isalnum, text))

# 이미지 인식 (기본)
def get_unicode():

    image = ImageGrab.grab(bbox=UNICODE_BOX)
    text = pytesseract.image_to_string(image, config='--psm 7')
    
    return ''.join(filter(str.isalnum, text))

# 메인
async def main_macro():

    await asyncio.sleep(2)  
    
    cnt=0
    while True:

        await asyncio.sleep(0.1)  

        code = get_unicode_cv2()
        print(code)

        if cnt == usercount: 
            break

        temp.append(code)

        await asyncio.sleep(0.1)

        pyautogui.press('right')

        cnt+=1

    print('[') 
    for i in range(0, len(temp), 5):
        print('  ', ', '.join(f"'{item}'" for item in temp[i:i+5]) + ',')
    print(']')  

if __name__ == '__main__':
    asyncio.run(main_macro())

