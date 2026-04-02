# Pokédex (Django)

Proyecto desarrollado con **Django** como parte de un **Bootcamp Full Stack Python**.

La aplicación consume la API pública de **PokeAPI** para construir una **Pokédex** (listado de Pokémon) y mostrar sus imágenes.

## Tecnologías

- Python
- Django
- Requests (HTTP client)
- Bootstrap 5
- PokeAPI: `https://pokeapi.co/`

## Instalación y ejecución (local)

1) Crear y activar un entorno virtual.

2) Instalar dependencias:

```bash
pip install -r requirements.txt
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

## Pantallas

- `/` Home
- `/registro/` Registro (simulado)
- `/admin-login/` Login de admin (simulado)
- `/admin/` Admin de Django

## Notas

- Este proyecto es para fines educativos.
- La disponibilidad y los datos dependen de PokeAPI.

