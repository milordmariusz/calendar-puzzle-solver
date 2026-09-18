@echo off
if not exist "venv" (
    echo [1/2] Creating virtual environment and installing packages...
    python -m venv venv
    call venv\Scripts\activate.bat
    python -m pip install --upgrade pip >nul 2>&1
    pip install -r requirements.txt
) else (
    call venv\Scripts\activate.bat
)

echo [2/2] Starting the application...
streamlit run app.py
pause