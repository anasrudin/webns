from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User



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
	context = {
		'page_title':'Transaksi Peminjaman',
		'nbar': 'transaksiPeminjaman',
	}
	return render(request, 'perpustakaan/transaksi.html', context)


@login_required(login_url='/login/')
def katalogPeminjaman(request):
	context = {
		'page_title':'Katalog Peminjaman',
		'nbar': 'katalogPeminjaman',
	}
	return render(request, 'perpustakaan/katalog.html', context)


@login_required(login_url='/login/')
def peminjaman(request):
	context = {
		'page_title':'Peminjaman Buku',
		'nbar': 'peminjamanBuku',
	}
	return render(request, 'perpustakaan/pinjam.html', context)



@login_required(login_url='/login/')
def pengembalian(request):
	context = {
		'page_title':'Pengembalian Buku',
		'nbar': 'pengembalianBuku',
	}
	return render(request, 'perpustakaan/kembali.html', context)



@login_required(login_url='/login/')
def daftarDenda(request):
	context = {
		'page_title':'Daftar Denda',
		'nbar': 'daftarDenda',
	}
	return render(request, 'perpustakaan/denda.html', context)


