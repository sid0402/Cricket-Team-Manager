from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
    path('<str:pk>/', views.post_details)
]