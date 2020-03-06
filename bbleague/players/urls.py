from django.urls import path
from . import views
app_name = 'players'

urlpatterns = [
    path('<player>', views.playerdetails, name='playerdetails'),
    path('team/selected', views.calculate, name='calculate'),
]