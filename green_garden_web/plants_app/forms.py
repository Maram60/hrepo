from django import forms
from .models import Plant

class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = ['name', 'type', 'watering_frequency', 'sunlight_requirement']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter plant name', 'id': 'name'}),
            'type': forms.TextInput(attrs={'placeholder': 'Enter plant type', 'id': 'type'}),
            'watering_frequency': forms.TextInput(attrs={'placeholder': 'Enter watering frequency', 'id': 'watering_frequency'}),
            'sunlight_requirement': forms.TextInput(attrs={'placeholder': 'Enter sunlight requirement', 'id': 'sunlight_requirement'}),
        }
