@echo off
echo Starting TinyLlama 1.1B CPU version...

echo Choose mode:
echo 1. Web UI  
echo 2. CLI Terminal
set /p choice="Enter 1 or 2: "

if "%choice%"=="1" (
    python python/app.py
) else if "%choice%"=="2" (
    python python/app.py --cli
) else (
    echo Invalid choice
    pause
)
