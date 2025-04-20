@echo off
setlocal

set ENV_NAME=deploy_env

echo [1/4] Creating
python -m venv %ENV_NAME%

if not exist "%ENV_NAME%\Scripts\activate.bat" (
    echo Failed
    pause
    exit /b
)

echo [2/4] Activating
call %ENV_NAME%\Scripts\activate

echo [3/4] Installing 
pip install --upgrade pip
pip install pyqt5 pyinstaller

echo [4/4] Building 
pyinstaller --noconsole --onefile ^
--add-data "Dictionary;Dictionary" ^
--add-data "public;public" ^
--icon=public/icon.ico App.py

echo Complete

pause
