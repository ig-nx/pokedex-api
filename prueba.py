import requests

url = "https://pokeapi.co/api/v2/pokemon/"

response = requests.get(url)

data = response.json()

print(data.keys())

n = data.get('count')

proxima = data.get('next')
anterior = data.get('previous')

res = data.get('results')

# [{'name': 'bulbasaur', 'url': 'https://pokeapi.co/api/v2/pokemon/1/'}, {'name': 'ivysaur', 'url': 'https://pokeapi.co/api/v2/pokemon/2/'}
# 
for item in res:
    url_detail = item.get('url')
    response_detail = requests.get(url_detail)
    data_detail = response_detail.json()

    print(data_detail.keys())
    print(data_detail.get('sprites').get('other').get('official-artwork').get('front_shiny'))

    url_imagen = data_detail.get('sprites').get('other').get('official-artwork').get('front_shiny')

    break


#print(res)
