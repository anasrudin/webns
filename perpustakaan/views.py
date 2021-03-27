from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User


from .forms import BukuForm, PinjamForm
from .models import Buku, Pinjam




from django.contrib import messages

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
		return redirect('keuangan:inputTransaksi')

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
		return redirect('keuangan:inputTransaksi')


	context = {
		'page_title':'tambahbuku Buku',
		'nbar': 'tambahbuku',
		'formInput':formInput,
	}
	return render(request, 'perpustakaan/kembali.html', context)














@login_required(login_url='/login/')
def daftarDenda(request):
	datadenda = Pinjam.objects.all()

	# startdate = date.today()
 #    enddate = startdate + timedelta(days=6)
 	
 #    Sample.objects.filter(date__range=[startdate, enddate])
	context = {
		'page_title':'Daftar Denda',
		'nbar': 'daftarDenda',
		'datadenda':datadenda,
	}
	return render(request, 'perpustakaan/denda.html', context)


