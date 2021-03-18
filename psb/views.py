from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User


#data
from home.models import *
# from .models import Psb
# from .forms import PsbForm

# Create your views here.
@login_required(login_url='/login/')
def index(request):
	context = {
		"page_title":"Psb",
		'nbar': 'psb',
	}
	return render(request, 'psb/index.html', context)


# @login_required(login_url='/login/')
# def indexPsb(request):
# 	getPsb = Psb.objects.all()
# 	context = {
# 		'page_title':'c',
# 		'getPsb':getPsb,
# 		'nbar': 'psb',
# 	}
# 	return render(request, 'psb/index.html', context)

@login_required(login_url='/login/')
def indexPsb(request):
	# jumlah_siswa = HomeDataSiswa.objects.count()
	print('jumlah_siswa')
	print(jumlah_siswa)

	context = {
		'page_title':'c',
		'jumlah_siswa':jumlah_siswa,
		'nbar': 'psb',
	}
	return render(request, 'psb/index.html', context)







# @login_required(login_url='/login/')
# def indexDataSiswa(request):
# 	getDataSiswa = Psb.objects.all()
# 	print(getDataSiswa)
# 	context = {
#     "getDataSiswa": getDataSiswa
# }
# 	# context = {
# 	# 	'page_title':'c',
# 	# 	'getDataSiswa':getDataSiswa,
# 	# 	'nbar': 'getDataSiswa',
# 	# }
# 	return render_to_response('psb/index.html', context)