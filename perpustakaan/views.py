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