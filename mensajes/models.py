from django.db import models
from django.utils import timezone

class Mensaje(models.Model):
    remitente = models.CharField(max_length=100)
    destinatario = models.CharField(max_length=100)
    texto = models.TextField()
    fecha_hora = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.remitente} a {self.destinatario}: {self.texto}"

    @staticmethod
    def filtrar_por_destinatario(destinatario):
        return Mensaje.objects.filter(destinatario=destinatario).order_by('fecha_hora')
