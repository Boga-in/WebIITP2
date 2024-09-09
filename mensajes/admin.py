from django.contrib import admin
from mensajes.models import Mensaje
class MensajeAdmin(admin.ModelAdmin):
    list_display = ("remitente","destinatario","texto","fecha_hora")
admin.site.register(Mensaje,MensajeAdmin)