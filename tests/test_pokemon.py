import requests
import pytest

token = '7e975e5dea0a872cb441fecb2ce24fb0'

def test_status_code():
    response = requests.get('https://api.pokemonbattle.me:9104/trainers' , params= {'trainer_id' : 1861})
    assert response.status_code == 200 

def test_trainer():
    response = requests.get('https://api.pokemonbattle.me:9104/trainers' , params= {'trainer_id' : 1861})
    assert response.json()['trainer_name'] == 'Batman'