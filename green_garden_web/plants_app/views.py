from django.db.models import Count, Avg
from django.shortcuts import redirect, render
from .models import Plant
from django.views.decorators.csrf import csrf_exempt


def plants(request):
    plants = Plant.objects.all()
    
    # Aggregations
    plant_count = Plant.objects.count()
    type_distribution = Plant.objects.values('type').annotate(total=Count('type'))
    average_watering_frequency = Plant.objects.annotate(num_watering=Count('watering_frequency')).order_by('-num_watering')[:5]  # Top 5 watering frequencies

    context = {
        'plants': plants,
        'plant_count': plant_count,
        'type_distribution': type_distribution,
        'average_watering_frequency': average_watering_frequency
    }
    return render(request, 'plantsmodule/plantsList.html', context)

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


@csrf_exempt
def add_plant(request):
    if request.method == 'POST':
        Plant.objects.create(
            name=request.POST['name'],
            type=request.POST['type'],
            watering_frequency=request.POST['watering_frequency'],
            sunlight_requirement=request.POST['sunlight_requirement']
        )

    return render(request, 'plantsmodule/add_plant.html')

@csrf_exempt
def edit_plant(request, pId):
    plant = Plant.objects.get(id=pId)
    if request.method == 'POST':
        plant.name = request.POST['name']
        plant.type = request.POST['type']
        plant.watering_frequency = request.POST['watering_frequency']
        plant.sunlight_requirement = request.POST['sunlight_requirement']
        plant.save()

    return render(request, 'plantsmodule/edit_plant.html', {'plant': plant})

