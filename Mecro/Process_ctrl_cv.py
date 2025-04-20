"""
    Config
"""
import os
import pyautogui
import pyperclip
import asyncio
import json

"""
    사용자설정
"""

base_dir = os.path.dirname(os.path.abspath(__file__))  
target_path = os.path.join(base_dir, '..', 'Dictionary')  

usercount = 10  # 개수 ( 가로 1줄 : 22개)

temp=[]

"""
    함수
"""
async def get_unicode_auto():
    pyautogui.moveTo(1730, 323)
    pyautogui.doubleClick()

    pyautogui.hotkey('ctrl', 'c')

    await asyncio.sleep(0.1) 

    copied_text = pyperclip.paste()

    pyautogui.moveTo(1775, 417)
    pyautogui.doubleClick()

    return copied_text

async def main_macro(file):

    await asyncio.sleep(2)  
    
    cnt=0
    while True:

        await asyncio.sleep(0.1)  

        code = await get_unicode_auto()
        print(code)

        if cnt == usercount: 
            break

        temp.append(code)

        await asyncio.sleep(0.1)

        pyautogui.press('right')

        cnt+=1


    def clean_code(code):
        try:
            return {
                "code": code,
                "char": chr(int(code, 16))
            }
        except:
            return None

    json_data = list(filter(None, [clean_code(c) for c in temp]))

    for i in range(0, len(json_data), 5):
        line = json_data[i:i+5]
        
        print(' '.join(f"{item['code']:>5}" for item in line))
        print(' '.join(f"{item['char']:>5}" for item in line))
        print() 

    with open(os.path.join(target_path, f"{file}.json"), 'w', encoding='utf-8') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    asyncio.run(main_macro("Temp"))