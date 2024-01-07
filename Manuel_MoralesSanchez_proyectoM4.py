import requests
import matplotlib.pyplot as plt
from PIL import Image
from urllib.request import urlopen
import json
import os

def obtener_datos_pokemon(nombre_pokemon):
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre_pokemon.lower()}"
    respuesta = requests.get(url)

    if respuesta.status_code == 200:
        
        datos_pokemon = respuesta.json()
        imagen_url = datos_pokemon['sprites']['front_default']
             
        # Recolecta estadísticas del Pokémon
        peso = datos_pokemon['weight']
        tamaño = datos_pokemon['height']
        movimientos = [move['move']['name'] for move in datos_pokemon['moves']]
        habilidades = [ability['ability']['name'] for ability in datos_pokemon['abilities']]
        tipos = [tipo['type']['name'] for tipo in datos_pokemon['types']]

        # Crear diccionario con la información del Pokémon
        info_pokemon = {
            'nombre': nombre_pokemon,
            'imagen': imagen_url,
            'peso': peso,
            'tamaño': tamaño,
            'movimientos': movimientos,
            'habilidades': habilidades,
            'tipos': tipos
        }

        # Guardar la información en un archivo JSON
        carpeta = 'pokedex'
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)

        with open(f"{carpeta}/{nombre_pokemon.lower()}.json", 'w') as archivo:
            json.dump(info_pokemon, archivo, indent=4)

        return info_pokemon
    else:
        return None

# Obtener nombre del Pokémon del usuario
nombre_pokemon = input("Ingrese el nombre del Pokémon: ")
pokemon = obtener_datos_pokemon(nombre_pokemon)

if pokemon:
    print(f"Imagen del Pokémon {nombre_pokemon}: {pokemon['imagen']}")
    print(f"Peso: {pokemon['peso']}")
    print(f"Tamaño: {pokemon['tamaño']}")
    print(f"Movimientos: {', '.join(pokemon['movimientos'])}")
    print(f"Habilidades: {', '.join(pokemon['habilidades'])}")
    print(f"Tipos: {', '.join(pokemon['tipos'])}")

url = f"https://pokeapi.co/api/v2/pokemon/{nombre_pokemon.lower()}"
respuesta = requests.get(url)

datos_pokemon = respuesta.json()

try :
    imagen_url = datos_pokemon['sprites']['front_default']
    imagen = Image.open(urlopen(imagen_url))
except :
    print("Pokemon no tiene imagen")
    
plt.imshow(imagen)
plt.title(f"Imagen de {nombre_pokemon}")
plt.axis('off')
plt.show()
