from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
    path('selector/', views.selector),
    path('team/', views.team)
]