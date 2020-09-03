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