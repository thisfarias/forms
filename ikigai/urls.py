from django.urls import path
from . import views

urlpatterns = [
    path('forms', views.forms),
    path('charts/<str:key>', views.charts, name='charts'),
]
