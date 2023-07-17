from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home),
    path("machine-players/", views.machine),
    path("machine-players/trade/", views.trade),
    path("machine-players/trade/submitted/", views.trade_submitted)
]
