from django.http import HttpResponse
from receitas.views import home,contato,sobre
from django.urls import path,include



urlpatterns = [
    path('',home),
    path('sobre/',sobre),
    path('contato/',contato)
]
