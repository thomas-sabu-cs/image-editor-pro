@echo off
REM Run Image Editor Pro using the virtual environment (avoids "module not found" errors)
cd /d "%~dp0"

if exist ".venv\Scripts\python.exe" (
    REM Ensure dependencies are installed (safe to run every time)
    ".venv\Scripts\pip.exe" install -r requirements.txt -q
    ".venv\Scripts\python.exe" main.py
) else (
    echo No .venv found. Creating it and installing dependencies...
    python -m venv .venv
    call .venv\Scripts\activate.bat
    pip install -r requirements.txt -q
    python main.py
)

if errorlevel 1 pause
