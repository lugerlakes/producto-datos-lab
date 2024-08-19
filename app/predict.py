import joblib
import numpy as np

def predict_taxi_trip(features_trip, model_path, confidence = 0.5):
    '''Recibe un vector de características de un viaje en taxi en NYC y predice si el pasajero dejará o no una propina alta.
    
    Argumentos:
        features_trip (array): Características del viaje, vector de tamaño 11.
        model_path (str): Ruta donde se encuentra el modelo.
        confidence (float, opcional): Nivel de confianza. Por defecto es 0.5.
    '''
    
    model = joblib.load(model_path)
    pred_value = model.predict_proba(features_trip.reshape(1,-1))[0][1]
    return 1 if pred_value >= confidence else 0 