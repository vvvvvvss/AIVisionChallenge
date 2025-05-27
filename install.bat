@echo off
set PYTHON_EXE=C:\Python311\python.exe
set PIP_EXE=C:\Python311\Scripts\pip.exe

if exist "%PYTHON_EXE%" (
   echo Installing requirements...
   "%PIP_EXE%" install -r labelImg\requirements\requirements-linux-python3.txt
   "%PIP_EXE%" install ultralytics
   start "" "%PYTHON_EXE%" labelImg\labelImg.py --autosave --nosplash --flags=classes.txt images/ labels/
) else (
   echo Python not found at %PYTHON_EXE%
   echo Check installation path or update this script
)
pause
start labelImg