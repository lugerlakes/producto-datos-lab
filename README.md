# NYC Taxi Tip Prediction 🗽🚖

## Descripción

Este proyecto transforma el repositorio existente `producto-datos-lab` en una aplicación completa que predice si un pasajero de taxi en la ciudad de Nueva York dejará una propina alta o baja. La aplicación consta de un backend implementado con FastAPI, una interfaz gráfica de usuario (GUI) desarrollada en Streamlit, y un despliegue serverless en la nube utilizando Modal.

### Características Principales

- **Backend con FastAPI**: Un API que recibe las características del viaje en taxi y devuelve la predicción de si la propina será alta o baja.
- **Interfaz de Usuario con Streamlit**: Una GUI intuitiva que permite a los usuarios ingresar los detalles del viaje y visualizar la predicción.
- **Despliegue Serverless en Modal**: La aplicación está desplegada en un entorno serverless para garantizar escalabilidad y fácil acceso desde cualquier lugar.

## Tabla de Contenidos

- [Instalación](#instalación)
  - [Requisitos Previos](#requisitos-previos)
  - [Configuración del Entorno Local](#configuración-del-entorno-local)
  - [Despliegue en Modal](#despliegue-en-modal)
- [Uso](#uso)
  - [Interacción a través de Streamlit](#interacción-a-través-de-streamlit)
  - [Acceso al API](#acceso-al-api)
- [Documentación del Código](#documentación-del-código)
- [Licencia](#licencia)

## Instalación

### Requisitos Previos

Asegúrate de tener instalados los siguientes elementos en tu máquina:

- Python 3.8 o superior
- pip
- Cuenta en [Modal](https://modal.com)

### Configuración del Entorno Local

1. **Crear un nuevo repositorio** en GitHub y clonarlo localmente:
    ```bash
    git clone https://github.com/tu-usuario/nuevo-repo.git
    cd nuevo-repo
    ```

2. **Realizar un fork del repositorio `producto-datos-lab`** y clonar el fork en tu máquina:
    ```bash
    git clone https://github.com/tu-usuario/producto-datos-lab.git
    cd producto-datos-lab
    ```

3. **Crear o editar `requirements.txt`** para asegurar que todas las dependencias necesarias están listadas.

4. **Crear un nuevo ambiente virtual en Python**:
    ```bash
    python -m venv .venv
    ```

5. **Activar el nuevo entorno virtual**:
    ```bash
    .\.venv\Scripts\activate
    ```

6. **Instalar las dependencias**:
    ```bash
    pip install -r requirements.txt
    ```

7. **Eliminar la carpeta `model` redundante en `app/`** si existe.

8. **Crear el archivo `predict.py`** en la carpeta `app/` con la lógica de predicción.

9. **Crear el archivo `main.py`** en la carpeta `app/` para definir el API de FastAPI.

10. **Crear un archivo `__init__.py`** en la carpeta `app/` para definirla como un módulo Python.

11. **Crear el archivo `deploy.py`** en la carpeta `app/` para configurar el despliegue en Modal.

12. **Crear el archivo `frontend/app.py`** para definir la interfaz de usuario en Streamlit.

13. **Probar la API localmente**:
    ```bash
    uvicorn app.main:app --reload
    ```

14. **Probar la interfaz de usuario localmente**:
    ```bash
    streamlit run frontend/app.py
    ```

### Despliegue en Modal

1. **Configurar Modal con `modal token new`** y autorizar la conexión con tu cuenta.

2. **Desplegar la aplicación en Modal**:
    ```bash
    modal deploy app/deploy.py
    ```

3. **Obtener la URL del servicio** proporcionada por Modal al desplegar la API. Reemplazar la URL en el archivo `frontend/app.py`:
    ```python
    response = requests.post(
        "https://lugerlakes--ntc-taxi-tip-prediction-fastapi-app.modal.run/predict", # URL de Modal
        json=features,
        params={"confidence": confidence}
    )
    ```

4. **Ejecutar la interfaz de usuario de Streamlit de manera serverless**:
    ```bash
    streamlit run frontend/app.py
    ```
   Esto permitirá acceder a la interfaz desde cualquier dispositivo conectado a Internet, utilizando la URL local proporcionada por Streamlit (por ejemplo, `https://192.168.1.149:8502`).

## Uso

### Interacción a través de Streamlit

- **Desde cualquier navegador**, ingresa a la URL proporcionada por Streamlit.
- Ingresa los detalles del viaje en taxi.
- Haz clic en "Predecir Propina" para recibir una predicción.

### Acceso al API

Puedes interactuar directamente con el API usando herramientas como `curl` o `Postman` enviando una solicitud POST con el siguiente formato:

```json
{
    "pickup_weekday": 2,
    "pickup_hour": 15,
    "work_hours": 1.0,
    "pickup_minute": 30,
    "passenger_count": 2,
    "trip_distance": 5.3,
    "trip_time": 20.0,
    "trip_speed": 16.0,
    "PULocationID": 100,
    "DOLocationID": 200,
    "RatecodeID": 1
}
```

La respuesta indicará si se espera una propina alta o baja.

## Documentación del Código
El código fuenta está organizado de la siguiente manera:
- 'app/': Contiene la lógica del backend con FastAPI y el script de despliegue en Modal.
- 'frontend/': Contiene la GUI desarrollada con Streamlit.
- 'model/': Almacena el modelo de machine learning utilizado para las predicciones.

Cada archivo y función está documentado para facilitar la comprensión y modificación.

## Licencia
Este proyecto está licenciado bajo la Licencia MIT.