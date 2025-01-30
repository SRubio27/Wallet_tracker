import requests
import os
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv(override=True)

# Obtener la API Key
API_KEY = os.getenv("COINMARKETCAP_API_KEY")

if not API_KEY:
    raise ValueError("API Key not found. Please set it in the .env file.")

print(f"API Key loaded successfully: {API_KEY[:5]}****")  # Para verificar sin exponer la clave completa

# URL base para la API
BASE_URL = "https://pro-api.coinmarketcap.com/v1/"

def obtener_precio_crypto(simbolo):
    """
    Obtiene el precio actual de una criptomoneda a partir de su símbolo.
    """
    url = BASE_URL + "cryptocurrency/quotes/latest"
    headers = {
        "Accepts": "application/json",
        "X-CMC_PRO_API_KEY": API_KEY,
    }
    parametros = {
        "symbol": simbolo,  # Símbolo de la criptomoneda
        "convert": "USD",   # Convertir el precio a USD
    }

    response = requests.get(url, headers=headers, params=parametros)
    
    if response.status_code == 200:
        data = response.json()
        try:
            precio = data["data"][simbolo]["quote"]["USD"]["price"]
            return precio
            return f"El precio de {simbolo} es ${precio: .4f} USD."
        except KeyError:
            return f"No se encontró información para el símbolo: {simbolo}."
    else:
        return f"Error al consultar la API: {response.status_code} - {response.text}"


