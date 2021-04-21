import json
import requests


print('please enter your zip code:')
zip = input()

r = requests.get('http://localhost:3000')

data = r.json()

i = 0

for widget in data:
    print(data[i]['name']+ ' is '+data[i]['color'])
    i += 1


