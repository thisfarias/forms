from django.urls import path
from . import views

urlpatterns = [
    path('/forms', views.forms, name='forms'), 
    path('/forms/success', views.calculate_category, name='sendAnswersAtratividade'),
    path('/graphic', views.generate_graphics)
]