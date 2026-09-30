@echo off
REM Gym Management System - Quick Start Script for Windows

echo.
echo ===================================
echo  Gym Management System Setup
echo ===================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH
    echo Please install Python 3.7+ from https://www.python.org/
    pause
    exit /b 1
)

echo [✓] Python found
echo.

REM Create virtual environment if it doesn't exist
if not exist "venv" (
    echo [*] Creating virtual environment...
    python -m venv venv
    echo [✓] Virtual environment created
) else (
    echo [✓] Virtual environment already exists
)

echo.
echo [*] Activating virtual environment...
call venv\Scripts\activate.bat

echo.
echo [*] Installing dependencies...
pip install -r requirements.txt

if errorlevel 1 (
    echo [ERROR] Failed to install dependencies
    pause
    exit /b 1
)

echo [✓] Dependencies installed
echo.
echo ===================================
echo   Setup Complete!
echo ===================================
echo.
echo Starting the application...
echo.
echo Navigate to: http://localhost:5000
echo.
echo Default Credentials:
echo   Username: admin
echo   Password: admin123
echo.

python app.py

pause
