from django.urls import path
from . import views
app_name = 'team'

urlpatterns = [
    path('<team>/', views.teamdetails, name='teamdetails'),
]