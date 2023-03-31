from django.shortcuts import render
from django.http import HttpResponse
import datetime



def home(request):
    return render(request,"receitas/home.html",context={ 'nome' : 'Breno cardoso'})

def contato(request):
    return render(request,"temp.html")

def sobre(request):
    return HttpResponse(f"Essa foi uma pagina feita com django usando")