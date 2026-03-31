# Pokédex (Django)

Proyecto desarrollado con **Django** como parte de un **Bootcamp Full Stack Python**, enseñado por el profesor **Carlos Garcia**.

La aplicación consume la API pública de **PokeAPI** para construir una **Pokédex** (listado de Pokémon) y mostrar sus imágenes.

## Tecnologías

- Python
- Django
- Requests (HTTP client)
- Bootstrap 5
- PokeAPI: `https://pokeapi.co/`

## Requisitos

- Python 3.11+ (recomendado)

## Instalación y ejecución (local)

1) Crear y activar un entorno virtual.

2) Instalar dependencias:

```bash
pip install django requests
```

3) Ejecutar migraciones y levantar el servidor:

```bash
python manage.py migrate
python manage.py runserver
```

4) Abrir:

```text
http://127.0.0.1:8000/
```

## Notas

- Este proyecto es para fines educativos y usa un servidor de desarrollo.
- La disponibilidad y los datos dependen de PokeAPI.
