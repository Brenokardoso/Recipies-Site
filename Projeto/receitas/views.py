from django.shortcuts import render


def home(request):
    return render(request,"receitas/page/home.html",context={ 'nome' : 'BMJ'},status='202')

