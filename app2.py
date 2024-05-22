import requests
import json

data={ "model": "llama2",
    "prompt":"¿Eres un gato malo?",
    "system": "Responde como si fueras Garfield",
    "stream": False
}


response = requests.post(' http://localhost:11434/api/generate', json=data)
response=json.loads(response.text)
print(response['response'])