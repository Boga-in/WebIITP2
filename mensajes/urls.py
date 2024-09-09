from django.urls import path
from .views import (
    ver_mensajes, index, crear_mensaje,
    ver_mensajes_enviados, ver_mensajes_recibidos, eliminar_mensaje
)

app_name = 'mensajes'

urlpatterns = [
    path('', index, name='index'),
    path('recibidos/', ver_mensajes, name='ver_mensajes'),
    path('crear/', crear_mensaje, name='crear_mensaje'),
    path('recibidos/<str:destinatario>/', ver_mensajes_recibidos, name='ver_mensajes_recibidos'),
    path('enviados/<str:remitente>/', ver_mensajes_enviados, name='ver_mensajes_enviados'),
    path('eliminar/<int:mensaje_id>/', eliminar_mensaje, name='eliminar_mensaje'),
]
