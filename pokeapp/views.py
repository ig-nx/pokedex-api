import requests
from django.shortcuts import render

def index(request):
    url = "https://pokeapi.co/api/v2/pokemon/"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
    except requests.RequestException:
        data = {}

    #print(data.keys())
    n = data.get('count')
    proxima = data.get('next')
    anterior = data.get('previous')
    res = data.get('results')

    datos = []
    for item in (res or []):
        url_detail = item.get('url')
        name = item.get('name')

        pokemon_id = (url_detail or "").rstrip("/").split("/")[-1]
        url_imagen = None
        pokemon_id_int = None
        if pokemon_id.isdigit():
            pokemon_id_int = int(pokemon_id)
            url_imagen = (
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/"
                f"other/official-artwork/shiny/{pokemon_id}.png"
            )

        temporal = {
            'id': pokemon_id_int,
            'name': name.capitalize(),
            'url_imagen': url_imagen
        }
        datos.append(temporal)
    




    context = { 'datos': datos}
    return render(request, 'index.html', context)

