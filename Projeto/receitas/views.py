from django.shortcuts import render


def home(request):
    return render(request,"receitas/page/home.html",context={ 'nome' : 'Breno Cardoso'},status='214')

