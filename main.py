# Cezary Gromulski 109390
from fastapi import FastAPI, Query
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get("/api/v1.0/predict")
def predict(x1: Optional[float] = Query(default=0), x2: Optional[float] = Query(default=0)):
    x1 = x1 or 0
    x2 = x2 or 0
    total = x1 + x2
    prediction = 1 if total > 5.8 else 0
    return {
        "prediction": prediction,
        "features": {"x1": x1, "x2": x2, "sum": total}
    }
