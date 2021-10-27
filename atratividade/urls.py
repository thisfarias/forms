from django.urls import path
from . import views

urlpatterns = [
    path('forms', views.forms, name='forms'), 
    path('forms/success', views.business_rules, name='sendAnswersAtratividade'),
    path('charts/<str:key>', views.charts, name='charts'),
    path('mail', views.email, name='mail'),
]