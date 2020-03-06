from django.urls import path
from . import views
app_name = 'game'

urlpatterns = [
    path('<uname>&', views.login, name='index'),
   # path('logout', views.logout, name='index')
]