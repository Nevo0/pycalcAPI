from django.urls import path
from . import views
from . import glandsAndTerminal


urlpatterns = [
    path('save/',  glandsAndTerminal.getGlands),
    path('terminals/',  glandsAndTerminal.getTerminals),
    path('glands/',  glandsAndTerminal.getGlands),
    
]

