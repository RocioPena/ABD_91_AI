import base64
import requests
import json

def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
        return encoded_string.decode('utf-8')

# Ruta de la imagen que quieres convertir a base64
ruta_imagen = "../img/vaca.jpg"

# Convertir la imagen a base64
base64_image = image_to_base64(ruta_imagen)

print("Imagen en Base64: listo")
#print(base64_image)

# Datos para la solicitud a la API
data = {
    "model": "llava",
    "prompt": "Describe la imagen",
    "system": "Responde como si fueras un profesional de artes pero quiero que me lo respondas en español",
    "stream": False,
    "images": [base64_image]  
}

# Realizar solicitud a la API local
response = requests.post('http://localhost:11434/api/generate', json=data)
response_data = json.loads(response.text)
print(response_data['response'])
