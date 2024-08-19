import joblib
import numpy as np
import io
import uvicorn
import nest_asyncio
from enum import Enum
from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np

from predict import predict_taxi_trip

app = FastAPI(title='NYC Taxi Tip Prediction API')

class Item(BaseModel):
    pickup_weekday: float
    pickup_hour: float
    work_hours: float
    pickup_minute: float
    passenger_count: float
    trip_distance: float
    trip_time: float
    trip_speed: float
    PULocationID: float
    DOLocationID: float
    RatecodeID: float
    
@app.get("/")
def home():
    return "¡Felicitaciones! Tu API está funcionando según lo esperado. Anda ahora a http://localhost:8000/docs."

@app.post("/predict")
def prediction(item: Item, confidence: float):
    features_trip = np.array([item.pickup_weekday, item.pickup_hour, item.work_hours, item.pickup_minute, item.passenger_count, item.trip_distance,
                    item.trip_time, item.trip_speed, item.PULocationID, item.DOLocationID, item.RatecodeID])
    model_path='./model/random_forest.joblib'
    pred = predict_taxi_trip(features_trip, model_path, confidence)
    return {'predicted_class': pred}


