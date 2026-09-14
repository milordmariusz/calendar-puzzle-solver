#!/bin/bash
set -e

if [ ! -d "venv" ]; then
    echo "[1/2] Tworzenie venv i instalacja pakietów..."
    python3 -m venv venv
    source venv/bin/activate
    pip install --upgrade pip --quiet
    pip install -r requirements.txt --quiet
else
    source venv/bin/activate
fi

echo "[2/2] Uruchamianie aplikacji..."
streamlit run app.py