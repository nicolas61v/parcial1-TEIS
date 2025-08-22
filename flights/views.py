from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Flight
from .forms import FlightForm

def home(request):
    return render(request, 'flights/home.html')

def registrar_vuelo(request):
    if request.method == 'POST':
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vuelo registrado exitosamente!')
            return redirect('registrar_vuelo')
    else:
        form = FlightForm()
    return render(request, 'flights/registrar_vuelo.html', {'form': form})

def listar_vuelos(request):
    vuelos = Flight.objects.all()
    return render(request, 'flights/listar_vuelos.html', {'vuelos': vuelos})

def estadisticas(request):
    total_vuelos = Flight.objects.count()
    vuelos_nacionales = Flight.objects.filter(tipo='Nacional').count()
    vuelos_internacionales = Flight.objects.filter(tipo='Internacional').count()
    
    context = {
        'total_vuelos': total_vuelos,
        'vuelos_nacionales': vuelos_nacionales,
        'vuelos_internacionales': vuelos_internacionales,
    }
    return render(request, 'flights/estadisticas.html', context)
