from django.urls import path
from .views import index, admin_login, admin_logout, registro

urlpatterns = [
    path('', index, name='index'),
    path('registro/', registro, name='registro'),
    path('admin-login/', admin_login, name='admin_login'),
    path('admin-logout/', admin_logout, name='admin_logout'),
]
