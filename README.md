# Model_regula_decyzyjna

Prosty serwis API, który przyjmuje dwie liczby i zwraca decyzję na podstawie reguły:
- Jeśli suma dwóch liczb > 5.8, predykcja = 1
- W przeciwnym razie predykcja = 0

## Endpoint

`GET /api/v1.0/predict?x1=<float>&x2=<float>`

## Przykład użycia

```bash
curl "http://localhost:8000/api/v1.0/predict?x1=3.1&x2=3.0"
