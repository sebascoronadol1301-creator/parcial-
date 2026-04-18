import requests

url = "https://pokeapi.co/api/v2/pokemon?limit=20"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    for pokemon in data["results"]:
        nombre = pokemon["name"]
        
        if nombre.lower().startswith('b'):
            print(f"Nombre: {nombre} [ESPECIAL] {nombre}")
        else:
            print(f"Nombre: {nombre}")
else:
    print("Error: No se pudo obtener la información de la API")