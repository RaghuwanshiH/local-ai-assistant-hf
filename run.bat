@echo off
title Local AI Assistant - TinyLlama
color 0A

echo ================================================
echo   Local AI Assistant - TinyLlama 1.1B
echo   100%% Offline ^| No API Keys ^| Always Free
echo ================================================
echo.

python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python not found!
    echo Download Python 3.10+ from https://python.org
    echo Make sure to check "Add Python to PATH" during install.
    echo.
    pause
    exit /b
)

echo [1/3] Checking Python... OK
echo.

echo [2/3] Installing requirements...
pip install -q gradio
echo Done.
echo.

echo [3/3] Choose how to run:
echo.
echo   1. Web UI  - Opens in browser automatically
echo   2. CLI     - Terminal chat only  
echo.
set /p choice="Enter 1 or 2: "

if "%choice%"=="1" (
    echo.
    echo Starting Web UI at http://127.0.0.1:7860
    echo Browser will auto-launch when ready.
    echo Keep this window open to run the server.
    echo Press Ctrl+C here to stop.
    echo.
    python python/app.py
) else if "%choice%"=="2" (
    echo.
    echo Starting CLI chat... Type 'exit' to quit
    echo.
    python python/test.py
) else (
    echo Invalid choice.
    pause
    exit /b
)
