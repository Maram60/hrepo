from django.db import models

class Plant(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)  # For example, 'Succulent', 'Perennial'
    watering_frequency = models.CharField(max_length=50)  # For example, 'Weekly', 'Bi-weekly'
    sunlight_requirement = models.CharField(max_length=100)  # For example, 'Partial', 'Full Sun'

    def __str__(self):
        return self.name
