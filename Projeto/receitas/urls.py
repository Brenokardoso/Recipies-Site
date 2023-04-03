from django.http import HttpResponse
from receitas.views import home
from django.urls import path



urlpatterns = [
    path('',home),
   
]
