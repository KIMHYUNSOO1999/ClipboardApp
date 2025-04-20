"""
    Config
"""

import json
import os

"""
    사용자설정
"""

base_dir = os.path.dirname(os.path.abspath(__file__))  
target_path = os.path.join(base_dir, '..', 'Dictionary')  

"""
    함수
"""

# 코드 검수 후 저장
def solution2(file):

    codes = ['1F49']

    def clean_code(code):
        try:
            code = code.upper().replace('O', '0')
            return {
                "code": code,
                "char": chr(int(code, 16))
            }
        except:
            return None

    json_data = list(filter(None, [clean_code(c) for c in codes]))

    for i in range(0, len(json_data), 5):
        line = json_data[i:i+5]
        
        print(' '.join(f"{item['code']:>5}" for item in line))
        print(' '.join(f"{item['char']:>5}" for item in line))
        print() 

    with open(os.path.join(target_path, f"{file}.json"), 'w', encoding='utf-8') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    solution2("temp")
