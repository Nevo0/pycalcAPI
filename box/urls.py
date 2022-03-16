from django.urls import path
from . import views


urlpatterns = [
    path('',  views.getRoutes),
    path('box/',  views.getProjekts),
    path('box/<str:pk>/',  views.getProjekt),
]

