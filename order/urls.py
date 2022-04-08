from django.urls import path
from . import views
from order.glandsAndTerminal2 import getGlands ,getTerminals, getGlands


urlpatterns = [
    path('save/',getGlands),
    path('terminals/',  getTerminals),
    path('glands/',  getGlands),
    
]

