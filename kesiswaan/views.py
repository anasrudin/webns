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

import xlwt

from django.db.models import Case, When


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
def export_datasiswa_xls(request):
	response = HttpResponse(content_type='application/ms-excel')
	response['Content-Disposition'] = 'attachment; filename="users.xls"'
	# wb = xlwt.Workbook(encoding='utf-8')
	wb = xlwt.Workbook()

	model1 = apps.get_model('home', 'DataSiswa')
	model2 = apps.get_model('home', 'DataSekolah')
	model3 = apps.get_model('home', 'DataTinggal')
	model4 = apps.get_model('home', 'DataOrtu')
	model5 = apps.get_model('home', 'DataKegiatan')
	datasiswa1 = model1.objects.filter(statussiswa="Aktif")
	ids    = datasiswa1.values_list('id', flat=True)
	datasiswa2 = model2.objects.filter(id__in=ids)
	datasiswa3 = model3.objects.filter(id__in=ids)
	datasiswa4 = model4.objects.filter(id__in=ids)
	datasiswa5 = model5.objects.filter(id__in=ids)






# -----------sheet 1 -------------
	ws = wb.add_sheet('DataSiswa')

	# Sheet header, first row
	row_num = 0
	font_style = xlwt.XFStyle()
	font_style.font.bold = True
	

	columns = [
	'nama', 
	'nisn', 
	'nik', 
	'tempatlahir',
	'tanggallahir',
	'jeniskelamin',
	'hobi',				
	'citacita',
	'anakke',
	'jumlahsaudara',
	'sekolahasal',
	'hp',
	'email',
	'tahunmasuk',
	'statussiswa',
	'nislokal',
	'kelas',
	'jurusan',
	]
	for col_num in range(len(columns)):
	    ws.write(row_num, col_num, columns[col_num], font_style)

	# Sheet body, remaining rows
	font_style = xlwt.XFStyle()
	# font_style.num_format_str = 'dd/mm/yyyy'

	rows  = datasiswa1.values_list(
		'nama', 
		'nisn', 
		'nik', 
		'tempatlahir',
		'tanggallahir',
		'jeniskelamin',
		'hobi',				
		'citacita',
		'anakke',
		'jumlahsaudara',
		'sekolahasal',
		'hp',
		'email',
		'tahunmasuk',
		'statussiswa',
		'nislokal',
		'kelas',
		'jurusan',
		) 
	baris = rows 
	for row in baris:
		row_num += 1
		for col_num in range(len(row)):
			ws.write(row_num, col_num, row[col_num], font_style)



# -----------sheet 2 -------------
	ws = wb.add_sheet('DataSekolah')
	row_num2 = 0

	columns2 = [
	'jenislembaga', 
	'statuslemaga',
	'npsn', 
	'noijazah',
	]
	for col_num2 in range(len(columns2)):
	    ws.write(row_num2, col_num2, columns2[col_num2], font_style)

	rows2  = datasiswa2.values_list(
	'jenislembaga', 
	'statuslemaga',
	'npsn', 
	'noijazah',
		)
	baris2 = rows2 
	for row2 in baris2:
		row_num2 += 1
		for col_num in range(len(row2)):
			ws.write(row_num2, col_num, row2[col_num], font_style)
 

 # -----------sheet 3 -------------
	ws = wb.add_sheet('DataTinggal')
	row_num3 = 0

	columns3 = [
	'jenistempattinggal', 
	'alamat',
	'provinsi', 
	'kabupatenkota',
	'kecamatan', 
	'desa',
	'kodepos', 
	'jaraktinggal',
	'transportasi',
	]
	for col_num3 in range(len(columns3)):
	    ws.write(row_num3, col_num3, columns3[col_num3], font_style)

	rows3  = datasiswa3.values_list(
	'jenistempattinggal', 
	'alamat',
	'provinsi', 
	'kabupatenkota',
	'kecamatan', 
	'desa',
	'kodepos', 
	'jaraktinggal',
	'transportasi',
		)
	baris3 = rows3 
	for row3 in baris3:
		row_num3 += 1
		for col_num in range(len(row3)):
			ws.write(row_num3, col_num, row3[col_num], font_style)
 


 # -----------sheet 4 -------------
	ws = wb.add_sheet('DataOrtu')
	row_num4 = 0

	columns4 = [
	'nokk' ,
	'kepalakeluarga' ,
	'ayah' ,
	'tanggallahirayah' ,
	'statusayah' ,
	'nikayah' ,
	'pendidikanayah' ,
	'pekerjaanayah' ,
	'ibu' ,
	'tanggallahiribu' ,
	'statusibu' ,
	'nikibu' ,
	'pendidikanibu' ,
	'pekerjaanibu' ,
	'wali' ,
	'tanggallahirwali' ,
	'statuswali' ,
	'nikwali' ,
	'pendidikanwali' ,
	'pekerjaanwali' ,
	'penghasilan' ,
	'kks' ,
	'pkh' ,
	'kip' ,
	'alamatortuwali' ,
	'sktm' ,
	]
	for col_num4 in range(len(columns4)):
	    ws.write(row_num4, col_num4, columns4[col_num4], font_style)

	rows4  = datasiswa4.values_list(
	'nokk' ,
	'kepalakeluarga' ,
	'ayah' ,
	'tanggallahirayah' ,
	'statusayah' ,
	'nikayah' ,
	'pendidikanayah' ,
	'pekerjaanayah' ,
	'ibu' ,
	'tanggallahiribu' ,
	'statusibu' ,
	'nikibu' ,
	'pendidikanibu' ,
	'pekerjaanibu' ,
	'wali' ,
	'tanggallahirwali' ,
	'statuswali' ,
	'nikwali' ,
	'pendidikanwali' ,
	'pekerjaanwali' ,
	'penghasilan' ,
	'kks' ,
	'pkh' ,
	'kip' ,
	'alamatortuwali' ,
	'sktm' ,

		)
	baris4 = rows4 
	for row4 in baris4:
		row_num4 += 1
		for col_num in range(len(row4)):
			ws.write(row_num4, col_num, row4[col_num], font_style)





# -----------sheet 5 -------------
	ws = wb.add_sheet('DataKegiatan')
	row_num5 = 0

	columns5 = ['motivasi', 'poinpelanggaran']
	for col_num5 in range(len(columns5)):
	    ws.write(row_num5, col_num5, columns5[col_num5], font_style)

	rows5  = datasiswa5.values_list('motivasi', 'poinpelanggaran' )
	baris5 = rows5 
	for row5 in baris5:
		row_num5 += 1
		for col_num in range(len(row5)):
			ws.write(row_num5, col_num, row5[col_num], font_style)
 



	wb.save(response)
	return response

def merge(list1, list2):
      
    merged_list = tuple(zip(list1, list2)) 
    return merged_list

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




