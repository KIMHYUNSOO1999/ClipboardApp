## 프로젝트 명
특수문자 클립보드 GUI 프로그램
</p>

## 개발목표
- 특수문자 클릭 시 클립보드에 복사되는 **유니코드 문자표 GUI 프로그램** 구현
- JSON 구조로 **사용자 사전 확장** 가능
- **OCR** 과 **복사/붙혀넣기** 기반 문자표 데이터 수집
- Deploy.bat 스크립트로 **빌드 및 배포 자동화**

## 프로젝트 구조

<pre lang="markdown">
ClipboardApp/ 
├── Dictionary/ (사용자사전) 
│   ├── 그리스.json
│   └── 라틴확장A.json 
├── Exe/ (실행)
│   └── App.exe  
├── Mecro/ (수집)
│   ├── Setting.py 
│   ├── Process_not_1.py (OCR)
│   ├── Process_not_2.py (OCR)
│   └── Process_ctrl_cv.py (CTRL+C,V)
├── Public/ (아이콘)
│   └── icon.ico 
├── App.py (GUI) 
└── Deploy.bat (BAT)
</pre>

## JSON 구조
<pre lang="markdown">
  {
    "code": "1F00",
    "char": "ἀ"
  }
</pre>

●  char 데이터가 '﹧' 또는 공백일 경우, code를 유니코드 문자 직접 변환 </p>

## 결과 
![image](https://github.com/user-attachments/assets/0d39222e-6ed8-42ec-8d0c-4f961341924e)
