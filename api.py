import requests
from dotenv import load_dotenv

# Tu API Key de CoinMarketCap
API_KEY = "c3df0e3b-abfa-4a9f-a489-0aebe889b98f"

# URL base para la API
BASE_URL = "https://pro-api.coinmarketcap.com/v1/"

""" 
    def obtener_precios(limit=1):
    url = BASE_URL + "cryptocurrency/listings/latest"
    headers = {
        "Accepts": "application/json",
        "X-CMC_PRO_API_KEY": API_KEY,
    }
    parametros = {
        "start": "1",  # Empezar desde la primera criptomoneda
        "limit": limit,  # Cuántas criptos obtener
        "convert": "USD",  # Convertir los precios a dólares
    }

    response = requests.get(url, headers=headers, params=parametros)
    
    if response.status_code == 200:
        data = response.json()
        return data["data"]
    else:
        print("Error al obtener los datos:", response.status_code, response.text)
        return None 
"""

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


