import requests

print("Petició GET: http://localhost:5000/saludo?nombre=Charles")
url = "http://localhost:5000/saludo?nombre=Charles"
response = requests.get(url)


if response.status_code == 200:
    print("✅ Èxit!")
    print(response.text)
else:
    print(f"❌ Error {response.status_code}")

print("Petició POST: http://localhost:5000/sumar")
# URL del endpoint Flask
url = "http://localhost:5000/sumar"


# Parámetro a enviar
datos = {"numero": 7}


try:
    # Enviar petición POST con JSON
    respuesta = requests.post(url, json=datos)


    # Comprobar el código de estado
    if respuesta.status_code == 200:
        print("✅ Respuesta correcta:")
        print(respuesta.json())
    else:
        print(f"⚠️ Error {respuesta.status_code}: {respuesta.text}")


except requests.exceptions.RequestException as e:
    print(f"❌ Error en la conexión: {e}")