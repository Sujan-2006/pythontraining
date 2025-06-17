import requests

mainurl="https://pokeapi.co/api/v2/"

def get_poke_info(name):
    url=f"{mainurl}/pokemon/{name}"
    response=requests.get(url)
    if response.status_code==200:
        pokemon_data=response.json()
        return pokemon_data
    else:
        print(f"failed to retrieve data {response.status_code}")
name="pikachu"
pokemon_info=get_poke_info(name)

if pokemon_info:
    print(f"name: {pokemon_info["name"].capitalize()}")
    print(f"ID: {pokemon_info["id"]}")
    print(f"Weight: {pokemon_info["weight"]}")