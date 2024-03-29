from django.shortcuts import render

# Function to get a fixed list of three specific plants
def getPlants():
    return [
        {'id': 1, 'name': 'Aloe Vera', 'type': 'Succulent', 'watering_frequency': 'Weekly', 'sunlight_requirement': 'Partial'},
        {'id': 2, 'name': 'Snake Plant', 'type': 'Perennial', 'watering_frequency': 'Bi-weekly', 'sunlight_requirement': 'Low to Moderate'},
        {'id': 3, 'name': 'Spider Plant', 'type': 'Perennial', 'watering_frequency': 'Weekly', 'sunlight_requirement': 'Partial to Full'}
    ]

def plants(request):
    plants = getPlants()
    return render(request, 'plantsmodule/plantsList.html', {'plants': plants})

def index(request):
    return render(request, 'plantsmodule/index.html')

def plant(request, pId):
    plants = getPlants()
    plant = next((p for p in plants if p['id'] == pId), None)
    return render(request, 'plantsmodule/plant.html', {'plant': plant})

from django.shortcuts import render

def filter_plant(request):
    plants = getPlants()

    # Get the search parameters from the GET request
    name = request.GET.get('name', '')
    plant_type = request.GET.get('type', '')
    watering_frequency = request.GET.get('watering_frequency', '')

    # Filter plants based on the search query
    if name:
        plants = [p for p in plants if name.lower() in p['name'].lower()]
    if plant_type:
        plants = [p for p in plants if plant_type.lower() in p['type'].lower()]
    if watering_frequency:
        plants = [p for p in plants if watering_frequency.lower() == p['watering_frequency'].lower()]

    return render(request, 'plantsmodule/plantsSearch.html', {'plants': plants})
