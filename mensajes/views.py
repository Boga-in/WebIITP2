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

def filtrar_mensajes(request):
    # Obtener listas de remitentes y destinatarios distintos
    remitentes = Mensaje.objects.values_list('remitente', flat=True).distinct()
    destinatarios = Mensaje.objects.values_list('destinatario', flat=True).distinct()

    mensajes_filtrados = None  # Inicialmente la lista de mensajes es vacía

    # Filtrar mensajes si se seleccionó un remitente o destinatario
    if request.method == 'POST':
        remitente_seleccionado = request.POST.get('remitente')
        destinatario_seleccionado = request.POST.get('destinatario')

        mensajes_filtrados = Mensaje.objects.all()

        if remitente_seleccionado:
            mensajes_filtrados = mensajes_filtrados.filter(remitente=remitente_seleccionado)
        if destinatario_seleccionado:
            mensajes_filtrados = mensajes_filtrados.filter(destinatario=destinatario_seleccionado)

    return render(request, 'filtrar.html', {
        'remitentes': remitentes,
        'destinatarios': destinatarios,
        'mensajes': mensajes_filtrados,  # Puede ser None si no hay filtro
    })



def eliminar_mensaje(request, mensaje_id):
    mensaje = get_object_or_404(Mensaje, id=mensaje_id)
    if request.method == 'POST':
        mensaje.delete()
        return redirect('mensajes:ver_mensajes')  # Redirigir a la lista de mensajes después de eliminar

    return render(request, 'eliminar_mensaje.html', {'mensaje': mensaje})
