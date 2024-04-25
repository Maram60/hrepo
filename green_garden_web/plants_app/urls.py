from django.urls import path, re_path
#import clubs views
from plants_app import views



urlpatterns = [    
    path('', views.index, name='index'),
    path('plants', views.plants),
    path('plants/<int:pId>', views.plant),
      path('plants/add', views.add_plant, name='add_plant'),
    path('plants/edit/<int:pId>', views.edit_plant, name='edit_plant'),
    path('plantsSearch', views.filter_plant, name="filter_plant")
] 