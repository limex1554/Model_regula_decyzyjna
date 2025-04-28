Projekt zrealizowany jako zadanie w ramach przedmiotu RTA na SGH.
Stworzony przez: Cezary Gromulski 109390

# Model_regula_decyzyjna
⚙️ Technologie:

- Python 3.11
- FastAPI
- Uvicorn
- Docker

Jest to prosty serwis API, który przyjmuje dwie liczby i zwraca decyzję na podstawie reguły:
- Jeśli suma dwóch liczb > 5.8, predykcja = 1
- W przeciwnym razie predykcja = 0

## Endpoint

`GET /api/v1.0/predict?x1=<float>&x2=<float>`

## Przykład użycia

### 1. Sklonuj repozytorium

### 2. Zbuduj obraz Dockera

### 3. Uruchom kontener

### 4. Wejdź w przeglądarce na:
http://localhost:8000/docs

```bash
git clone https://github.com/limex1554/decision-rule-api.git
cd decision-rule-api
docker build -t decision-rule-api .
docker run -p 8000:8000 decision-rule-api
```

