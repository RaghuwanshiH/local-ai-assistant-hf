@echo off
echo Choose mode:
echo 1. Web UI
echo 2. CLI Terminal
set /p choice=Enter 1 or 2: 

ollama serve

if %choice%==1 python python/app.py
if %choice%==2 python python/test.py

pause
