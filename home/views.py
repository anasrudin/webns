from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import DataSiswaForm, DataSekolahForm, DataTinggalForm, DataOrtuForm, DataMotivasiForm


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
        form1 = DataSiswaForm()
        form2 = DataSekolahForm()
        form3 = DataTinggalForm()
        form4 = DataOrtuForm()
        form5 = DataMotivasiForm()
        context = {'page_title': 'Formpsb',}
        return render(request, 'home/formpsb.html', {'form1':form1, 'form2':form2,  'form3':form3, 'form4':form4, 'form5':form5})
    else:
        form1 = DataSiswaForm(request.POST)
        form2 = DataSekolahForm(request.POST)
        form3 = DataTinggalForm(request.POST)
        form4 = DataOrtuForm(request.POST)
        form5 = DataMotivasiForm(request.POST)
        if form1.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid() and form5.is_valid():
            profile1 = form1.save(commit=False)
            profile1.save()
            profile2 = form2.save(commit=False)
            profile2.save()
            profile3 = form3.save(commit=False)
            profile3.save()
            profile4 = form4.save(commit=False)
            profile4.save()
            profile5 = form5.save(commit=False)
            profile5.save()
            messages.success(request, f"Success")
        return redirect('sukses')

        # return render(request, 'home/formpsb.html', {'form':form})

def sukses(request):
    context = {
    'page_title': 'Registrasi Berhasil',
    }
    
    return render(request, 'home/sukses.html')