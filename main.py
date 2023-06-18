import requests
import json


url = 'https://akabab.github.io/superhero-api/api/all.json'

response = requests.get(url)
if 200 <= response.status_code < 300:
    res_dict = response.json()
max_intelligence = None
min_intelligence = 0
for hero in res_dict:
    if hero['name'] == 'Hulk' or hero['name'] == 'Captain America' or hero['name'] == 'Thanos':
        if hero['powerstats']['intelligence'] > min_intelligence:
            min_intelligence = hero['powerstats']['intelligence']
            max_intelligence = hero['name']
print(f'Most intelligence superhero - {max_intelligence}')


