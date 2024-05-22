import json
import requests

URL = "http://localhost:11434"

# Función para consumir la API
def consume_api(endpoint, data):
    response = requests.post(f"{URL}/{endpoint}", json=data)
    if response.status_code == 200:
        print('Solicitud exitosa')
        print('Data:', response.json())
    else:
        print('Error en la solicitud, detalles:', response.text)

# Ejemplo de uso
if __name__ == "__main__":
    endpoints = ["api/generate"]
    data = {"model": "llama2",
            "prompt": "¿Que son las llamas?",
            "stream": False}

    for endpoint in endpoints:
        consume_api(endpoint, data)

