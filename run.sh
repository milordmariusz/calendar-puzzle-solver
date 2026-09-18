#!/bin/bash
set -e

if [ ! -d "venv" ]; then
    echo "[1/2] Creating virtual environment and installing packages..."
    python3 -m venv venv
    source venv/bin/activate
    pip install --upgrade pip --quiet
    pip install -r requirements.txt --quiet
else
    source venv/bin/activate
fi

echo "[2/2] Starting the application..."
streamlit run app.py