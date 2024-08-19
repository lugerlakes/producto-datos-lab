import streamlit as st
import requests

# Titulo de la app
st.title('🚕 Predict NYC Taxi Tips')

# Descripción de la aplicación
st.write("""
Esta aplicación predice si un pasajero de taxi en la ciudad de Nueva York dejará una propina alta o baja. 
Por favor, ingresa la información del viaje a continuación.
""")

# Inputs del usuario con explicaciones
pickup_weekday = st.selectbox(
    "Día de la semana del viaje (0=Lunes, 6=Domingo)",
    options=[0, 1, 2, 3, 4, 5, 6],
    format_func=lambda x: ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"][x]
)
pickup_hour = st.slider(
    "Hora de recogida (Formato 24 horas)", 
    min_value=0, max_value=23, step=1,
    help="Selecciona la hora en la que se recogió al pasajero"
)
work_hours = st.slider(
    "Horas de trabajo (0=No, 1=Sí)", 
    min_value=0.0, max_value=1.0, step=0.1,
    help="Indica si el viaje ocurrió durante las horas de trabajo típicas (9am - 5pm)"
)
pickup_minute = st.slider(
    "Minuto de recogida", 
    min_value=0, max_value=59, step=1,
    help="Selecciona el minuto en el que se recogió al pasajero"
)
passenger_count = st.slider(
    "Cantidad de pasajeros", 
    min_value=1, max_value=8, step=1,
    help="Número de pasajeros en el viaje"
)
trip_distance = st.number_input(
    "Distancia del viaje (en millas)", 
    min_value=0.0, step=0.1,
    help="Ingresa la distancia total del viaje en millas"
)
trip_time = st.number_input(
    "Tiempo del viaje (en minutos)", 
    min_value=0.0, step=1.0,
    help="Ingresa el tiempo total del viaje en minutos"
)
trip_speed = st.number_input(
    "Velocidad media del viaje (en mph)", 
    min_value=0.0, step=0.1,
    help="Ingresa la velocidad media del viaje en millas por hora"
)
PULocationID = st.number_input(
    "ID de ubicación de recogida", 
    min_value=0, step=1,
    help="ID del lugar donde se recogió al pasajero"
)
DOLocationID = st.number_input(
    "ID de ubicación de destino", 
    min_value=0, step=1,
    help="ID del lugar donde se dejó al pasajero"
)
RatecodeID = st.number_input(
    "ID del código de tarifa", 
    min_value=0, step=1,
    help="Código que identifica el tipo de tarifa del viaje"
)
confidence = st.slider(
    "Umbral de confianza para la predicción", 
    min_value=0.0, max_value=1.0, step=0.1,
    value=0.5,
    help="Selecciona el nivel de confianza requerido para clasificar la propina como alta"
)

# Botón de predicción
if st.button("Predecir Propina"):
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
   
    # Solicitud al backend
    response = requests.post(
        "https://lugerlakes--nyc-taxi-tip-prediction-fastapi-app.modal.run", 
        json=features, 
        params={"confidence": confidence}
    )
      
    # Mostrar la respuesta  
    if response.status_code == 200:
        prediction = response.json().get("predicted_class")
        st.success("Predicción: Propina Alta" if prediction == 1 else "Predicción: Propina Baja")
    else:
        st.error(f"Error: {response.status_code}")
