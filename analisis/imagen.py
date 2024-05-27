import base64

def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
        return encoded_string.decode('utf-8')

# Ruta de la imagen que quieres convertir a base64
ruta_imagen = "../img/pato.jpg"

# Convertir la imagen a base64
base64_image = image_to_base64(ruta_imagen)

print("Imagen en Base64:")
print(base64_image)
