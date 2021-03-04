from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import DataSiswaForm


from django.contrib import messages
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
            profile = form.save(commit=False)
            profile.save()
            messages.success(request, f"Success")
        return redirect('sukses')

        # return render(request, 'home/formpsb.html', {'form':form})

def sukses(request):
    context = {
    'page_title': 'Registrasi Berhasil',
    }
    
    return render(request, 'home/sukses.html')