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

def filter_plant(request, name=None, plant_type=None):
    plants = getPlants()
    if name:
        plants = [p for p in plants if name.lower() in p['name'].lower()]
    if plant_type:
        plants = [p for p in plants if plant_type.lower() == p['type'].lower()]
    return render(request, 'filtered_plants_template.html', {'plants': plants})