#!/bin/bash
# Gym Management System - Quick Start Script for Mac/Linux

echo ""
echo "==================================="
echo "  Gym Management System Setup"
echo "==================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "[ERROR] Python 3 is not installed"
    echo "Please install Python 3.7+ from https://www.python.org/"
    exit 1
fi

echo "[✓] Python found: $(python3 --version)"
echo ""

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "[*] Creating virtual environment..."
    python3 -m venv venv
    echo "[✓] Virtual environment created"
else
    echo "[✓] Virtual environment already exists"
fi

echo ""
echo "[*] Activating virtual environment..."
source venv/bin/activate

echo ""
echo "[*] Installing dependencies..."
pip install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "[ERROR] Failed to install dependencies"
    exit 1
fi

echo "[✓] Dependencies installed"
echo ""
echo "==================================="
echo "   Setup Complete!"
echo "==================================="
echo ""
echo "Starting the application..."
echo ""
echo "Navigate to: http://localhost:5000"
echo ""
echo "Default Credentials:"
echo "   Username: admin"
echo "   Password: admin123"
echo ""

python3 app.py
