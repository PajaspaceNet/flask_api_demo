


## Flask API Demo

Toto je demonstrační aplikace vytvořená pomocí frameworku **Flask**, která slouží jako ukázka jednoduchého API. Projekt byl vytvořen s důrazem na snadnost nasazení na platformu **Koyeb**.
https://quaint-ailey-paja-1dcf4297.koyeb.app/    ... zde je link 

## Funkce
- **Flask Framework**: Lehké a flexibilní řešení pro vývoj webových aplikací.
- **API Demonstrace**: Jednoduché rozhraní s jednou základní routou (`/`).
- **Snadné nasazení**: Optimalizováno pro použití na platformě Koyeb.

## Struktura projektu
```
Flask API Demo/
├── api_demo.py          # Hlavní soubor s Flask aplikací <br>
├── requirements.txt     # Seznam závislostí <br>
├── Procfile             # Konfigurace pro Gunicorn a Koyeb <br>
├── templates/  <br>
    └── index.html       # Ukázková šablona <br>
```

## Jak spustit aplikaci lokálně
1. Klonujte repozitář:
   ```bash
   git clone https://github.com/vase-uzivatelske-jmeno/flask_api_demo.git
   cd flask_api_demo
   ```

2. Vytvořte virtuální prostředí a nainstalujte závislosti:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Na Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Spusťte Flask aplikaci:
   ```bash
   python api_demo.py
   ```

4. Aplikace bude dostupná na `http://127.0.0.1:5000`.

## Jak nasadit na Koyeb
1. Přihlaste se do [Koyeb Dashboard](https://app.koyeb.com/).
2. Vytvořte novou službu a propojte ji s tímto GitHub repozitářem.
3. Zvolte hlavní větev (`master` nebo `main`) a potvrďte nasazení.
4. Po dokončení nasazení bude vaše aplikace dostupná na URL, kterou Koyeb vygeneruje.

## Požadavky
- Python 3.9+
- Flask
- Gunicorn (pro produkční nasazení)



