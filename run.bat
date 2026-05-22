@echo off
title Local AI Assistant - HF Version
echo ================================
echo  TinyLlama 1.1B - Transformers
echo ================================
echo.

echo Installing requirements...
pip install -r python/requirements.txt

echo.
echo Starting Web UI at http://127.0.0.1:7860
echo First run downloads ~2GB model - be patient
python python/app.py

pause
