@echo off
if not exist "venv" (
    echo [1/2] Tworzenie venv i instalacja pakietow...
    python -m venv venv
    call venv\Scripts\activate.bat
    python -m pip install --upgrade pip >nul 2>&1
    pip install -r requirements.txt
) else (
    call venv\Scripts\activate.bat
)

echo [2/2] Uruchamianie aplikacji...
streamlit run app.py
pause