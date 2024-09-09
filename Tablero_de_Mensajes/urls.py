from django.contrib import admin
from django.urls import path, include
from mensajes.urls import urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
     path('',include('mensajes.urls',namespace='mensajes'))
]