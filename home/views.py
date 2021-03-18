from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import DataSiswaForm, DataSekolahForm, DataTinggalForm, DataOrtuForm, DataKegiatanForm
from .models import DataSiswa, DataSekolah, DataTinggal, DataOrtu, DataKegiatan

from django.contrib import messages
# Create your views here.

from django.contrib.auth.decorators import login_required


from django.shortcuts import get_list_or_404, get_object_or_404

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
        form5 = DataKegiatanForm()
        context = {'page_title': 'Formpsb',}
        return render(request, 'home/formpsb.html', {'form1':form1, 'form2':form2,  'form3':form3, 'form4':form4, 'form5':form5})
    else:
        form1 = DataSiswaForm(request.POST)
        form2 = DataSekolahForm(request.POST)
        form3 = DataTinggalForm(request.POST)
        form4 = DataOrtuForm(request.POST)
        form5 = DataKegiatanForm(request.POST)
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
        return redirect('/sukses')

        # return render(request, 'home/formpsb.html', {'form':form})

@login_required(login_url='/login/')
def deletepsb(request,id):
    DataSiswa.objects.filter(id=id).delete()
    DataSekolah.objects.filter(id=id).delete()
    DataTinggal.objects.filter(id=id).delete()
    DataOrtu.objects.filter(id=id).delete()
    DataKegiatan.objects.filter(id=id).delete()
    messages.success(request, 'Data Psb berhasil didelete')
    return redirect('home:list')

@login_required(login_url='/login/')
def updatepsb(request,id):
    instanceModel1 = get_object_or_404(DataSiswa, id=id)
    instanceModel2 = get_object_or_404(DataSekolah, id=id)
    instanceModel3 = get_object_or_404(DataTinggal, id=id)
    instanceModel4 = get_object_or_404(DataOrtu, id=id)
    instanceModel5 = get_object_or_404(DataKegiatan, id=id)
    form1 = DataSiswaForm(request.POST or None, instance=instanceModel1)
    form2 = DataSekolahForm(request.POST or None, instance=instanceModel2 )
    form3 = DataTinggalForm(request.POST or None, instance=instanceModel3)
    form4 = DataOrtuForm(request.POST or None, instance=instanceModel4)
    form5 = DataKegiatanForm(request.POST or None, instance=instanceModel5)
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
        return redirect('home:list')
    return render(request, 'home/update.html', {'form1':form1, 'form2':form2,  'form3':form3, 'form4':form4, 'form5':form5})






def sukses(request):
    context = {
    'page_title': 'Registrasi Berhasil',
    }
    
    return render(request, 'home/sukses.html')


@login_required(login_url='/login/')
def list(request):
    # Generate counts of some of the main objects
    num_siswa = DataSiswa.objects.count()
    datasiswa = DataSiswa.objects.all()


    context = {
    'page_title': 'Rlist pendaftar',
    'num_siswa':num_siswa,
    'datasiswa':datasiswa,
    }
    
    return render(request, 'home/list.html', context)


