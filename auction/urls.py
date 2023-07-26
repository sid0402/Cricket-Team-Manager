from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home),
    path("retain/",views.retain),
    path("simulate/", views.simulate),
    path("simulate-mini/", views.simulatemini),
    path("team/", views.team)
]
