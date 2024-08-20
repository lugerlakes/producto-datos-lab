import modal
from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import os

from app.predict import predict_taxi_trip

web_app = FastAPI()

model_path = os.path.abspath('model/random_forest.joblib')

image = modal.Image.debian_slim().pip_install(
    'fastapi', 'pydantic', 'joblib', 'numpy', 'uvicorn', 'scikit-learn'
).copy_local_file(
    model_path, '/model/random_forest.joblib'
)

app = modal.App('NYC-Taxi-Tip-Prediction')

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

@modal.asgi_app()
@app.function(image=image)
def fastapi_app():
    @web_app.get('/ping')
    async def ping():
        return 'pong'
    
    @web_app.post('/predict')
    async def handle_prediction(item: Item, confidence: float = 0.5):
        features_trip = np.array([
            item.pickup_weekday, item.pickup_hour, item.work_hours, item.pickup_minute, item.passenger_count, 
            item.trip_distance, item.trip_time, item.trip_speed, item.PULocationID, item.DOLocationID, 
            item.RatecodeID
        ])    
        pred = predict_taxi_trip(features_trip, '/model/random_forest.joblib', confidence)
        return {'predicted_class': pred}
    
    return web_app

if __name__ == '__main__':
    app.deploy('NYC-Taxi-Tip-Prediction')
