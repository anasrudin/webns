from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User


# Create your views here.
@login_required(login_url='/login/')
def index(request):
	context = {
		"page_title":"Kesiswaan",
		'nbar': 'kesiswaan',
	}
	return render(request, 'kesiswaan/index.html', context)


@login_required(login_url='/login/')
def indexKesiswaan(request):
	getKesiswaan = Kesiswaan.objects.all()
	context = {
		'page_title':'c',
		'getKesiswaan':getKesiswaan,
		'nbar': 'kesiswaan',
	}
	return render(request, 'kesiswaan/index.html', context)

@login_required(login_url='/login/')
def masterData(request):
	context = {
		"page_title":"Master Data",
		'nbar': 'masterData',
	}
	return render(request, 'kesiswaan/master.html', context)

@login_required(login_url='/login/')
def pelanggaran(request):
	context = {
		"page_title":"Pelanggaran Siswa",
		'nbar': 'pelanggaran',
	}
	return render(request, 'kesiswaan/pelanggaran.html', context)

@login_required(login_url='/login/')
def kehadiran(request):
	context = {
		"page_title":"Kehadiran Siswa",
		'nbar': 'kehadiran',
	}
	return render(request, 'kesiswaan/kehadiran.html', context)


@login_required(login_url='/login/')
def daftarSiswa(request):
	context = {
		"page_title":"Daftar Siswa",
		'nbar': 'daftarSiswa',
	}
	return render(request, 'kesiswaan/daftarSiswa.html', context)
