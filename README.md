## Ponowne uruchomienie

Jeśli środowisko zostało już wcześniej skonfigurowane, ponowne uruchomienie sprowadza się do wykonania tego samego skryptu startowego (skrypt wykryje gotowe środowisko i pominie instalację):

- **Linux / macOS:** `./run.sh`
- **Windows:** `run.bat`

LUB ręcznie z poziomu terminala:

```bash
source venv/bin/activate  # Windows: venv\Scripts\activate
streamlit run app.py
```
