# LLM

Un modelo de lenguaje grande o LLM, también llamado modelo de lenguaje de gran tamaño, es un modelo de lenguaje que consta de una red neuronal con muchos parámetros, entrenados en grandes cantidades de texto sin etiquetar mediante aprendizaje autosupervisado o aprendizaje semisupervisado.​

¿Porque el cielo es azul? -> hola mundo 

## Instalacion de ollama
```
 curl -fsSL https://ollama.com/install.sh | sh 
 ```

 ## Correr el server de ollama
 ```
 ollama serve
 ```

 ## Lista de los modelos de ollama
 ```
 ollama list <-> es para ver los modelos de ollama
 ```
 (Se necesita correr primero el serve y depues abrir otro consola)

 ## Descargar un modelo de ollama (tinyllama)
 ```
 ollama pull tinyllama

 ollama pull llama2
 ```

 ## Corre ollama -> generador
  ```
ollama run tinyllama ¿porqué el cielo es azul?
 ```

## Correr ollama -> chat
 ```
ollama run tinyllama
 ```

## Codigo para correr el api (Llamadas de API REST)
 ```
curl http://localhost:11434/api/generate -d '{
  "model": "tinyllama",
  "prompt":"¿Porque el cielo es azul?"
}'
 ```
 ```
curl http://localhost:11434/api/generate -d '{
  "model": "tinyllama",
  "prompt":"¿Porque el cielo es azul?",
  "system": "Responde como si fueras Gon Gokou",
  "stream": false
}'
 ```
 ```
 curl http://localhost:11434/api/generate -d '{
  "model": "tinyllama",
  "prompt":"¿Que paso con abuelito?",
  "system": "Responde como si fueras Goku",
  "stream": false
}'
 ```
  ```
 curl http://localhost:11434/api/generate -d '{
  "model": "llama2",
  "prompt":"¿Eres un gato malo?",
  "system": "Responde como si fueras Garfield",
  "stream": false
}'
 ```


falso
   ```
 curl http://localhost:11434/api/generate -d '{
  "model": "llama4",
  "prompt":"¿Eres un gato malo?",
  "system": "Responde como si fueras Garfield",
  "stream": false
}'
 ```



# Tarea
## Interfaz de una pregunta y despues su respuesta, otra pregunta (generate)
 ``` python
import json
import request
 ```

formato = JSON -> response
 url= localhost
 puerto = 11434
 uri = api/generate, api/chat, api/tags
 data = {"model": "",
        "prompt":"",
        "stream": false}



## 22/05/2024
Crear la carpeta Mdelos 
crear un archivo Modelfile
Va tener lo siguiente: FROM tinyllama
ollama create mi_modelo -f Modelfile