import requests
import json

ship = json.loads(requests.get('https://swapi.dev/api/starships/10/').text)

for elem in range(0, len(ship['pilots'])):
    ship['pilots'][elem] = json.loads(requests.get(ship['pilots'][elem]).text)

with open('ship.json', 'w') as file:
    json.dump(ship, file, indent=4)
