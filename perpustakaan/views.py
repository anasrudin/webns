from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User


from .forms import BukuForm, PinjamForm
from .models import Buku, Pinjam



# time filter
from datetime import datetime, timedelta
from django.utils import timezone



from django.contrib import messages


from django.shortcuts import get_list_or_404, get_object_or_404

# Create your views here.
# @login_required(login_url='/login/')
# def index(request):
#     return HttpResponse("perpus page." )


@login_required(login_url='/login/')
def index(request):
	context = {
		"page_title":"Perpustakaan",
		'nbar': 'perpustakaan',
	}
	return render(request, 'perpustakaan/index.html', context)


@login_required(login_url='/login/')
def indexPerpustakaan(request):
	getPerpustakaan = Perpustakaan.objects.all()
	context = {
		'page_title':'c',
		'getPerpustakaan':getPerpustakaan,
		'nbar': 'perpustakaan',
	}
	return render(request, 'perpustakaan/index.html', context)


@login_required(login_url='/login/')
def transaksiPeminjaman(request):
	datapinjam = Pinjam.objects.all()
	context = {
		'page_title':'Transaksi Peminjaman',
		'nbar': 'transaksiPeminjaman',
		'datapinjam':datapinjam,

	}
	return render(request, 'perpustakaan/transaksi.html', context)


@login_required(login_url='/login/')
def katalogPeminjaman(request):
	databuku = Buku.objects.all()
	context = {
		'page_title':'Katalog Peminjaman',
		'nbar': 'katalogPeminjaman',
		'databuku':databuku,
	}
	return render(request, 'perpustakaan/katalog.html', context)


@login_required(login_url='/login/')
def peminjaman(request):
	formInput = PinjamForm(request.POST or None)
	if request.method == 'POST':
		if formInput.is_valid():
			formInput.save()
			messages.success(request, 'Data Buku berhasil dibuat')
		return redirect('perpustakaan:transaksiPeminjaman')

	context = {
		'page_title':'Peminjaman Buku',
		'nbar': 'peminjamanBuku',
		'formInput':formInput,
	}
	return render(request, 'perpustakaan/pinjam.html', context)



@login_required(login_url='/login/')
def tambahbuku(request):
	formInput = BukuForm(request.POST or None)
	if request.method == 'POST':
		if formInput.is_valid():
			formInput.save()
			messages.success(request, 'Data Pinjam berhasil dibuat')
		return redirect('perpustakaan:katalogPeminjaman')


	context = {
		'page_title':'tambahbuku Buku',
		'nbar': 'tambahbuku',
		'formInput':formInput,
	}
	return render(request, 'perpustakaan/kembali.html', context)





@login_required(login_url='/login/')
def daftarDenda(request):
	time_threshold = datetime.now()
	# tanggalkembali
	# datadenda = Pinjam.objects.all()
	datadenda = Pinjam.objects.filter(tanggalkembali__lt=time_threshold)

	# startdate = date.today()
 #    enddate = startdate + timedelta(days=6)
 	
 #    Sample.objects.filter(date__range=[startdate, enddate])
	context = {
		'page_title':'Daftar Denda',
		'nbar': 'daftarDenda',
		'datadenda':datadenda,
	}
	return render(request, 'perpustakaan/denda.html', context)




@login_required(login_url='/login/')
def deleteBuku(request, id):
	Buku.objects.filter(id=id).delete()
	messages.success(request, 'Data Buku berhasil didelete')
	return redirect('perpustakaan:katalogPeminjaman')


@login_required(login_url='/login/')
def deletePinjam(request, id):
	Pinjam.objects.filter(id=id).delete()
	messages.success(request, 'Data Pinjaman berhasil didelete')
	return redirect('perpustakaan:transaksiPeminjaman')





@login_required(login_url='/login/')
def updatePinjam(request, id):
	instanceModel1 = get_object_or_404(Pinjam, id=id)
	formInput = PinjamForm(request.POST or None, instance=instanceModel1)
	if formInput.is_valid():
		profile1 = formInput.save(commit=False)
		profile1.save()
		messages.success(request, f"Success")
		return redirect('perpustakaan:transaksiPeminjaman')

	return render(request, 'perpustakaan/updatepinjam.html', {'formInput':formInput})






