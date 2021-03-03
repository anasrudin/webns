from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import DataSiswaForm

# Create your views here.


def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    context = {
    'page_title': 'Home',
    }
    
    return render(request, 'index.html', context)


def formpsb(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    if request.method == "GET":
        form = DataSiswaForm()
        context = {'page_title': 'Formpsb',}
        return render(request, 'home/formpsb.html', {'form':form})
    else:
        form = DataSiswaForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'index.html')

def siswa_form(request):
    return