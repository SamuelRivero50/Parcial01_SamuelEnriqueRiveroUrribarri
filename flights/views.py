from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Avg, Count
from .models import Flight

def home(request):
    return render(request, 'flights/home.html')

def registrar_vuelo(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        tipo = request.POST.get('tipo')
        precio = request.POST.get('precio')
        
        # Validaciones correspondientes
        if not nombre or not tipo or not precio:
            messages.error(request, 'faltan campos')
            return render(request, 'flights/registrar.html')
        
        try:
            precio = float(precio)
            if precio <= 0:
                messages.error(request, 'precio debe ser positivo')
                return render(request, 'flights/registrar.html')
        except ValueError:
            messages.error(request, 'precio debe ser numero')
            return render(request, 'flights/registrar.html')
        
        # Validacion tipo a nivel de vista
        if tipo not in ['Nacional', 'Internacional']:
            messages.error(request, 'tipo debe ser nacional o internacional')
            return render(request, 'flights/registrar.html')
        
        # Registrar en base de datos
        flight = Flight.objects.create(
            nombre=nombre,
            tipo=tipo,
            precio=precio
        )
        
        messages.success(request, 'vuelo guardado')
        return redirect('flights:registrar')
    
    return render(request, 'flights/registrar.html')

def listar_vuelos(request):
    flights = Flight.objects.all()  # Ya ordenados por precio (Meta.ordering)
    return render(request, 'flights/listar.html', {'flights': flights})

def estadisticas_vuelos(request):
    # Contar vuelos nacionales e internacionales
    vuelos_nacionales = Flight.objects.filter(tipo='Nacional').count()
    vuelos_internacionales = Flight.objects.filter(tipo='Internacional').count()
    
    # Precio promedio de vuelos nacionales
    precio_promedio_nacional = Flight.objects.filter(tipo='Nacional').aggregate(
        promedio=Avg('precio')
    )['promedio']
    
    if precio_promedio_nacional is None:
        precio_promedio_nacional = 0
    
    context = {
        'vuelos_nacionales': vuelos_nacionales,
        'vuelos_internacionales': vuelos_internacionales,
        'precio_promedio_nacional': round(precio_promedio_nacional, 2)
    }
    
    return render(request, 'flights/estadisticas.html', context)
