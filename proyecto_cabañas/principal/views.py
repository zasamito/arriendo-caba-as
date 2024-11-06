from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Comentario  # Asegúrate de tener un modelo de Comentario definido

# Vista para la página de inicio
def index(request):
    return render(request, 'index.html')

# Vista para la página de inicio de sesión
def login(request):
    return render(request, 'login.html')

# Vista para la página de registro
def registro(request):
    return render(request, 'registro.html')

# Vista para la página de reservas
def reservar(request):
    return render(request, 'reservar.html')

# Vista para la página de comentarios
def comentarios(request):
    return render(request, 'comentarios.html')

# Vista para la página de pagos
def pagos(request):
    return render(request, 'pagos.html')

# Vista para la página de cabañas
def cabañas(request):
    return render(request, 'cabañas.html')

# Vista para guardar comentarios
def guardar_comentario(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')
        comentario = request.POST.get('comentario')

        # Aquí puedes crear un nuevo comentario en la base de datos
        nuevo_comentario = Comentario(nombre=nombre, correo=correo, comentario=comentario)
        nuevo_comentario.save()

        return redirect('index')  # Redirigir a la página de inicio después de guardar el comentario

    return HttpResponse("Método no permitido", status=405)