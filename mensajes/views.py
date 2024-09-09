from django.shortcuts import render, redirect 
from django.shortcuts import get_object_or_404 
from .models import Mensaje 
from .forms import MensajeForm   

def index(request):
    return render(request, 'index.html')

def ver_mensajes(request):
    mensajes_recibidos = Mensaje.objects.all().order_by('fecha_hora')
    return render(request, 'recibidos.html', {'mensajes': mensajes_recibidos})

def crear_mensaje(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            form.save()  # Guardar el mensaje en la base de datos
            return redirect('mensajes:ver_mensajes')  # Redirigir a la lista de mensajes después de crear
    else:
        form = MensajeForm()

    return render(request, 'crear_mensaje.html', {'form': form})

def ver_mensajes_recibidos(request, destinatario):
    mensajes_recibidos = Mensaje.objects.filter(destinatario=destinatario).order_by('fecha_hora')
    return render(request, 'recibidos.html', {'mensajes': mensajes_recibidos})


def ver_mensajes_enviados(request, remitente):
    mensajes_enviados = Mensaje.objects.filter(remitente=remitente).order_by('fecha_hora')
    return render(request, 'enviados.html', {'mensajes': mensajes_enviados})


def eliminar_mensaje(request, mensaje_id):
    mensaje = get_object_or_404(Mensaje, id=mensaje_id)
    if request.method == 'POST':
        mensaje.delete()
        return redirect('mensajes:ver_mensajes')  # Redirigir a la lista de mensajes después de eliminar

    return render(request, 'eliminar_mensaje.html', {'mensaje': mensaje})
