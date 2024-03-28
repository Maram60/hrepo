from django.shortcuts import render, redirect

def index(request):
    # This view returns the index page for Green Garden Web App
    return render(request, 'plantsmodule/index.html')

def plants(request):
    # This view returns the plants list page for Green Garden Web App
    return render(request, 'plantsmodule/plantsList.html')

def plant(request, pId):
    # This view returns the details of a specific plant for Green Garden Web App

    # Example plant data
    plant1 = {'id': 1, 'name': 'Aloe Vera', 'type': 'Succulent', 'watering_frequency': 'Weekly', 'sunlight_requirement': 'Partial'}
    plant2 = {'id': 2, 'name': 'Snake Plant', 'type': 'Perennial', 'watering_frequency': 'Bi-weekly', 'sunlight_requirement': 'Low to Moderate'}

    targetPlant = None
    if plant1['id'] == pId: targetPlant = plant1
    if plant2['id'] == pId: targetPlant = plant2

    if targetPlant == None: return redirect('/plants')

    context = {'plant': targetPlant}  # 'plant' is the variable name accessible by the template
    return render(request, 'plantsmodule/plant.html', context)
