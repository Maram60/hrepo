from django.shortcuts import render
from .models import Plant  

def plants(request):
    plants = Plant.objects.all() 
    return render(request, 'plantsmodule/plantsList.html', {'plants': plants})

def index(request):
    return render(request, 'plantsmodule/index.html')

def plant(request, pId):
    plant = Plant.objects.filter(id=pId).first()  
    return render(request, 'plantsmodule/plant.html', {'plant': plant})

def filter_plant(request):
    plants = Plant.objects.all()

    name = request.GET.get('name', '')
    plant_type = request.GET.get('type', '')
    watering_frequency = request.GET.get('watering_frequency', '')

    if name:
        plants = plants.filter(name__icontains=name)
    if plant_type:
        plants = plants.filter(type__icontains=plant_type)
    if watering_frequency:
        plants = plants.filter(watering_frequency__icontains=watering_frequency)

    return render(request, 'plantsmodule/plantsSearch.html', {'plants': plants})
