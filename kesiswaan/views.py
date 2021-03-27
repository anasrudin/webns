from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

from .forms import ScoreSiswaForm
from .models import ScoreSiswa, KehadiranSiswa

from datetime import datetime, timedelta


from home.models import DataSiswa
from django.apps import apps



from django.contrib import messages

# combine query set
from itertools import chain
from django.db.models import Q
from operator import attrgetter
# from django.db.models.query import QuerySet


from django.shortcuts import get_list_or_404, get_object_or_404


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
	datapelanggar = ScoreSiswa.objects.all()
	context = {
		"page_title":"Pelanggaran Siswa",
		'nbar': 'pelanggaran',
		'datapelanggar':datapelanggar,
	}
	return render(request, 'kesiswaan/pelanggaran.html', context)












@login_required(login_url='/login/')
def kehadiran(request):
	model1 = apps.get_model('home', 'DataSiswa')
	datasiswa = model1.objects.all().filter(statussiswa="Aktif")
	# datasiswa = KehadiranSiswa.objects.all().filter(statussiswa="Aktif")
	# datasiswa = KehadiranSiswa.objects.all()

	tanggal = datetime.now()
	# num_siswa = DataSiswa.objects.count()
	# model = apps.get_model('home', 'DataSiswa')
	# num_siswa = model.objects.count()
	# tanggal = KehadiranSiswa.objects.all()
	context = {
		"page_title":"Kehadiran Siswa",
		'nbar': 'kehadiran',
		'datasiswa':datasiswa,
		'tanggal':tanggal,
	}
	return render(request, 'kesiswaan/kehadiran.html', context)


@login_required(login_url='/login/')
def daftarSiswa(request):
	model1 = apps.get_model('home', 'DataSiswa')
	# kehadiran = apps.get_model('home', 'DataSiswa')

	sis = ScoreSiswa.objects.all()
	

	datasiswa = model1.objects.all().filter(statussiswa="Aktif")
	# datakegiatan = model2.objects.all().filter(statussiswa="Aktif")
	# report = list(chain(datasiswa, datakegiatan))


	# sis_count = datasiswa.values_list('pk', flat=True)
	# sis_count = model2.objects.count()
	# sis_count = datakegiatan.values().id

	sis_count = model1.objects.all().filter(statussiswa="Aktif").count()


	# report = list(sorted(chain(datasiswa, datakegiatan)))
	# report  = datasiswa.union(datakegiatan)
	# report  = datakegiatan | datasiswa
	# report = sorted(chain(datasiswa,datakegiatan),key=attrgetter('timestamp'),)
	# report = tuple(chain.from_iterable(datasiswa,datakegiatan))

	# report = MultiQuerySet(datasiswa, datakegiatan)


	# report = datasiswa | datakegiatan.distinct()
	context = {
		"page_title":"Daftar Siswa",
		'nbar': 'daftarSiswa',
		'datasiswa':datasiswa,
		'sis':sis,
		'sis_count':sis_count,
	}
	return render(request, 'kesiswaan/daftarSiswa.html', context)


@login_required(login_url='/login/')
def tambahPelanggar(request):
	formInput = ScoreSiswaForm(request.POST or None)
	if request.method == 'POST':
		if formInput.is_valid():
			formInput.save()
			messages.success(request, 'Data Pelanggaran berhasil dibuat')
		return redirect('kesiswaan:pelanggaran')
	
	context = {
		"page_title":"Tambah Pelanggar",
		'nbar': 'tambahPelanggar',
		'formInput':formInput,
	}
	return render(request, 'kesiswaan/tambahpelanggar.html', context)

@login_required(login_url='/login/')
def deletePelanggar(request, id):
    ScoreSiswa.objects.filter(id=id).delete()
    messages.success(request, 'Data Pelanggar berhasil didelete')
    return redirect('kesiswaan:pelanggaran')


@login_required(login_url='/login/')
def updatePelanggar(request, id):
    # ScoreSiswa.objects.filter(id=id).delete()
    # messages.success(request, 'Data Pelanggar berhasil didelete')
    # return redirect('kesiswaan:pelanggaran')
    instanceModel1 = get_object_or_404(ScoreSiswa, id=id)
    formInput = ScoreSiswaForm(request.POST or None, instance=instanceModel1)
    if formInput.is_valid():
    	profile1 = formInput.save(commit=False)
    	profile1.save()
    	messages.success(request, f"Success")
    	return redirect('kesiswaan:pelanggaran')
    return render(request, 'kesiswaan/tambahpelanggar.html', {'formInput':formInput})




