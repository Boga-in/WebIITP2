from django.urls import path
from .views import (
    ver_mensajes, index, crear_mensaje,
    filtrar_mensajes, eliminar_mensaje
)

app_name = 'mensajes'

urlpatterns = [
    path('', index, name='index'),
    path('recibidos/', ver_mensajes, name='ver_mensajes'),
    path('crear/', crear_mensaje, name='crear_mensaje'),
    path('filtrar/', filtrar_mensajes, name='filtrar_mensajes'),
    path('eliminar/<int:mensaje_id>/', eliminar_mensaje, name='eliminar_mensaje'),
]
