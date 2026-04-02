# Pokédex con Django

Proyecto desarrollado en **Django** como parte del **Bootcamp Full Stack Python**. Esta aplicación consume la API pública de **PokeAPI** para mostrar un listado de Pokémon con sus imágenes en una interfaz web simple.

## Demo en producción

El proyecto se encuentra publicado en:

`https://pokedex.restak.cl/`

## Funcionalidades principales

- Consumo de datos desde **PokeAPI**.
- Listado de Pokémon con imágenes.
- Paginación de resultados en la vista principal.
- Formulario de registro simulado.
- Inicio y cierre de sesión de administrador en modo simulado.
- Acceso al panel de administración de Django.

## Rutas disponibles

- `/` Inicio de la Pokédex.
- `/registro/` Registro simulado.
- `/admin-login/` Inicio de sesión de administrador simulado.
- `/admin-logout/` Cierre de sesión de administrador simulado.
- `/admin/` Panel de administración de Django.

## Tecnologías utilizadas

- **Python**
- **Django**
- **Requests**
- **Bootstrap 5**
- **SQLite**
- **Gunicorn**
- **WhiteNoise**
- **PokeAPI**: `https://pokeapi.co/`

## Ejecución en entorno local

1. Crear y activar un entorno virtual.
2. Instalar las dependencias del proyecto:

```bash
pip install -r requirements.txt
```

3. Ejecutar las migraciones:

```bash
python manage.py migrate
```

4. Levantar el servidor de desarrollo:

```bash
python manage.py runserver
```

5. Abrir en el navegador:

```text
http://127.0.0.1:8000/
```

## Despliegue en producción

El proyecto fue desplegado en un **VPS de Oracle Cloud**, utilizando el subdominio:

`https://pokedex.restak.cl/`

Para la publicación y administración del entorno de producción se consideró:

- **PM2** para la gestión del proceso en el servidor.
- **GitHub** como apoyo para versionado y despliegue.
- Configuraciones específicas de producción.
- Manejo de variables de entorno para separar la configuración del entorno de desarrollo y producción.

## Créditos

Trabajo realizado en paralelo con el profesor **Carlos García** en el contexto del **Bootcamp Full Stack Python**.

## Notas

- Proyecto realizado con fines educativos y de repositorio personal.
- La disponibilidad de datos e imágenes depende de **PokeAPI**.
