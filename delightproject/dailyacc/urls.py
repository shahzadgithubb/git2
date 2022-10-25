from django.urls import path
from . import views

urlpatterns = [
    path('master', views.master, name='master' ),
    path('condact', views.condact, name='condact')
]