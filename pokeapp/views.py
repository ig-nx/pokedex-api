import requests
from django.contrib import messages
from django.shortcuts import redirect, render

FAKE_ADMIN_USERNAME = "admin"
FAKE_ADMIN_PASSWORD = "admin"


def index(request):
    base_url = "https://pokeapi.co/api/v2/pokemon/"
    limit = 18

    try:
        page = int(request.GET.get("page", "1"))
    except ValueError:
        page = 1
    page = max(1, page)

    def fetch_data(page_number: int) -> dict:
        offset = (page_number - 1) * limit
        url = f"{base_url}?offset={offset}&limit={limit}"
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.RequestException:
            return {}

    def build_datos(results: list) -> list:
        datos = []
        for item in (results or []):
            url_detail = item.get("url")
            name = item.get("name")

            pokemon_id = (url_detail or "").rstrip("/").split("/")[-1]
            url_imagen = None
            pokemon_id_int = None
            if pokemon_id.isdigit():
                pokemon_id_int = int(pokemon_id)
                url_imagen = (
                    "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/"
                    f"other/official-artwork/shiny/{pokemon_id}.png"
                )

            datos.append(
                {
                    "id": pokemon_id_int,
                    "name": (name or "").capitalize(),
                    "url_imagen": url_imagen,
                }
            )
        return datos

    data = fetch_data(page)
    n = data.get("count")

    total_pages = None
    if isinstance(n, int) and n > 0:
        total_pages = (n + limit - 1) // limit
        if page > total_pages:
            page = total_pages
            data = fetch_data(page)
            n = data.get("count")

    proxima = data.get("next")
    anterior = data.get("previous")
    res = data.get("results")
    datos = build_datos(res)

    page_numbers = []
    show_first = False
    show_last = False
    show_left_ellipsis = False
    show_right_ellipsis = False

    if total_pages and total_pages > 1:
        window = 2
        start = max(1, page - window)
        end = min(total_pages, page + window)
        page_numbers = list(range(start, end + 1))

        show_first = 1 not in page_numbers
        show_last = total_pages not in page_numbers
        show_left_ellipsis = start > 2
        show_right_ellipsis = end < (total_pages - 1)

    context = {
        "datos": datos,
        "count": n,
        "next": proxima,
        "previous": anterior,
        "page": page,
        "limit": limit,
        "total_pages": total_pages,
        "page_numbers": page_numbers,
        "show_first": show_first,
        "show_last": show_last,
        "show_left_ellipsis": show_left_ellipsis,
        "show_right_ellipsis": show_right_ellipsis,
    }
    return render(request, "index.html", context)


def admin_login(request):
    if request.method == "POST":
        username = (request.POST.get("username") or "").strip()
        password = request.POST.get("password") or ""

        if username == FAKE_ADMIN_USERNAME and password == FAKE_ADMIN_PASSWORD:
            request.session["is_fake_admin"] = True
            messages.success(request, "Sesión de admin iniciada (modo simulado).")
            return redirect("index")

        messages.error(request, "Usuario o contraseña incorrectos.")

    return render(request, "admin_login.html")


def admin_logout(request):
    request.session.pop("is_fake_admin", None)
    messages.info(request, "Sesión cerrada.")
    return redirect("index")


def registro(request):
    if request.method == "POST":
        nombre = (request.POST.get("nombre") or "").strip()
        email = (request.POST.get("email") or "").strip()
        password = request.POST.get("password") or ""
        password2 = request.POST.get("password2") or ""

        if not nombre or not email or not password or not password2:
            messages.error(request, "Completa todos los campos.")
        elif password != password2:
            messages.error(request, "Las contraseñas no coinciden.")
        else:
            messages.success(request, "Registro simulado creado. ¡Ya puedes iniciar sesión como admin!")
            return redirect("index")

    return render(request, "registro.html")
