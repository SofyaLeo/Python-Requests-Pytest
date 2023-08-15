import requests
token = '7e975e5dea0a872cb441fecb2ce24fb0'
responce = requests.post('https://api.pokemonbattle.me:9104/pokemons' , json = {
    "name": "Велес",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}, headers = {'Content-Type' : 'application/json' , 'trainer_token' : token})
print(responce.text)
responce_name = requests.put('https://api.pokemonbattle.me:9104/pokemons' , json = {
    "pokemon_id": "6169",
    "name": "Буба",
    "photo": "https://dolnikov.ru/pokemons/albums/030.png"
}, headers = {'Content-Type' : 'application/json' , 'trainer_token'  : token})
print(responce_name.text)
responce_ball = requests.post('https://api.pokemonbattle.me:9104 /trainers/add_pokeball' , json = {
    "pokemon_id": "6168"
}, headers = {'Content-Type' : 'application/json' , 'trainer_token' : token})
print(responce_ball.text)