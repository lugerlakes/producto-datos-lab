import streamlit as st
import requests

# Page configuration
st.set_page_config(
    page_title="NYC-Taxi-Tip-Prediction 🗽🚖",
    page_icon="🚖",
    layout="wide",
)

# Language selection
language = st.selectbox("Select Language 🌐", ["English", "Español"])

# Text content based on selected language
if language == "English":
    title = "🚖 Predict NYC Taxi Tips 🗽"
    description = """
    This application predicts whether a taxi passenger in New York City will leave a high or low tip. 
    Please enter the trip details below.
    """
    button_text = "Predict Tip"
    success_message = "Prediction: High Tip"
    error_message = "Prediction: Low Tip"
    labels = {
        "pickup_weekday": "Day of the Week (0=Monday, 6=Sunday)",
        "pickup_hour": "Pickup Hour (24-hour format)",
        "work_hours": "Work Hours (0=No, 1=Yes)",
        "pickup_minute": "Pickup Minute",
        "passenger_count": "Passenger Count",
        "trip_distance": "Trip Distance (in miles)",
        "trip_time": "Trip Time (in minutes)",
        "trip_speed": "Average Trip Speed (in mph)",
        "PULocationID": "Pickup Location ID",
        "DOLocationID": "Dropoff Location ID",
        "RatecodeID": "Rate Code ID",
        "confidence": "Confidence Threshold for Prediction",
    }
    help_texts = {
        "pickup_weekday": "Select the day of the week the trip took place.",
        "pickup_hour": "Select the hour the passenger was picked up.",
        "work_hours": "Indicate if the trip occurred during typical work hours (9am - 5pm).",
        "pickup_minute": "Select the minute the passenger was picked up.",
        "passenger_count": "Number of passengers in the trip.",
        "trip_distance": "Enter the total trip distance in miles.",
        "trip_time": "Enter the total trip time in minutes.",
        "trip_speed": "Enter the average speed of the trip in miles per hour.",
        "PULocationID": "ID of the location where the passenger was picked up.",
        "DOLocationID": "ID of the location where the passenger was dropped off.",
        "RatecodeID": "Code that identifies the type of fare for the trip.",
        "confidence": "Select the confidence level required to classify the tip as high.",
    }
else:
    title = "🚖 Predecir Propinas de Taxi en NYC 🗽"
    description = """
    Esta aplicación predice si un pasajero de taxi en la ciudad de Nueva York dejará una propina alta o baja. 
    Por favor, ingresa la información del viaje a continuación.
    """
    button_text = "Predecir Propina"
    success_message = "Predicción: Propina Alta"
    error_message = "Predicción: Propina Baja"
    labels = {
        "pickup_weekday": "Día de la Semana (0=Lunes, 6=Domingo)",
        "pickup_hour": "Hora de Recogida (Formato 24 horas)",
        "work_hours": "Horas Laborales (0=No, 1=Sí)",
        "pickup_minute": "Minuto de Recogida",
        "passenger_count": "Cantidad de Pasajeros",
        "trip_distance": "Distancia del Viaje (en millas)",
        "trip_time": "Tiempo del Viaje (en minutos)",
        "trip_speed": "Velocidad Media del Viaje (en mph)",
        "PULocationID": "ID de Ubicación de Recogida",
        "DOLocationID": "ID de Ubicación de Destino",
        "RatecodeID": "ID del Código de Tarifa",
        "confidence": "Umbral de Confianza para la Predicción",
    }
    help_texts = {
        "pickup_weekday": "Selecciona el día de la semana en que se realizó el viaje.",
        "pickup_hour": "Selecciona la hora en que se recogió al pasajero.",
        "work_hours": "Indica si el viaje ocurrió durante las horas laborales típicas (9am - 5pm).",
        "pickup_minute": "Selecciona el minuto en que se recogió al pasajero.",
        "passenger_count": "Número de pasajeros en el viaje.",
        "trip_distance": "Ingresa la distancia total del viaje en millas.",
        "trip_time": "Ingresa el tiempo total del viaje en minutos.",
        "trip_speed": "Ingresa la velocidad media del viaje en millas por hora.",
        "PULocationID": "ID del lugar donde se recogió al pasajero.",
        "DOLocationID": "ID del lugar donde se dejó al pasajero.",
        "RatecodeID": "Código que identifica el tipo de tarifa del viaje.",
        "confidence": "Selecciona el nivel de confianza requerido para clasificar la propina como alta.",
    }

# Display the app title and description
st.title(title)
st.write(description)

# User inputs
pickup_weekday = st.selectbox(
    labels["pickup_weekday"],
    options=[0, 1, 2, 3, 4, 5, 6],
    format_func=lambda x: ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"][x] 
    if language == "English" else 
    ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"][x]
)
pickup_hour = st.slider(
    labels["pickup_hour"], 
    min_value=0, max_value=23, step=1,
    help=help_texts["pickup_hour"]
)
work_hours = st.slider(
    labels["work_hours"], 
    min_value=0.0, max_value=1.0, step=0.1,
    help=help_texts["work_hours"]
)
pickup_minute = st.slider(
    labels["pickup_minute"], 
    min_value=0, max_value=59, step=1,
    help=help_texts["pickup_minute"]
)
passenger_count = st.slider(
    labels["passenger_count"], 
    min_value=1, max_value=8, step=1,
    help=help_texts["passenger_count"]
)
trip_distance = st.number_input(
    labels["trip_distance"], 
    min_value=0.0, step=0.1,
    help=help_texts["trip_distance"]
)
trip_time = st.number_input(
    labels["trip_time"], 
    min_value=0.0, step=1.0,
    help=help_texts["trip_time"]
)
trip_speed = st.number_input(
    labels["trip_speed"], 
    min_value=0.0, step=0.1,
    help=help_texts["trip_speed"]
)
PULocationID = st.number_input(
    labels["PULocationID"], 
    min_value=0, step=1,
    help=help_texts["PULocationID"]
)
DOLocationID = st.number_input(
    labels["DOLocationID"], 
    min_value=0, step=1,
    help=help_texts["DOLocationID"]
)
RatecodeID = st.number_input(
    labels["RatecodeID"], 
    min_value=0, step=1,
    help=help_texts["RatecodeID"]
)
confidence = st.slider(
    labels["confidence"], 
    min_value=0.0, max_value=1.0, step=0.1,
    value=0.5,
    help=help_texts["confidence"]
)

# Prediction button
if st.button(button_text):
    features = {
        "pickup_weekday": pickup_weekday,
        "pickup_hour": pickup_hour,
        "work_hours": work_hours,
        "pickup_minute": pickup_minute,
        "passenger_count": passenger_count,
        "trip_distance": trip_distance,
        "trip_time": trip_time,
        "trip_speed": trip_speed,
        "PULocationID": PULocationID,
        "DOLocationID": DOLocationID,
        "RatecodeID": RatecodeID,
    }
   
    # Request to the backend
    response = requests.post(
        "https://lugerlakes--nyc-taxi-tip-prediction-fastapi-app.modal.run    /predict", # Modal URL
        json=features, 
        params={"confidence": confidence}
    )
      
    # Display the response
    if response.status_code == 200:
        prediction = response.json().get("predicted_class")
        st.success(success_message if prediction == 1 else error_message)
    else:
        st.error(f"Error: {response.status_code}")
