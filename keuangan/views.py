from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User


# Create your views here.
@login_required(login_url='/login/')
def index(request):
	context = {
		"page_title":"Keuangan",
		'nbar': 'keuangan',
	}
	return render(request, 'keuangan/index.html', context)


@login_required(login_url='/login/')
def indexKeuangan(request):
	getKeuangan = Keuangan.objects.all()
	context = {
		'page_title':'c',
		'getKeuangan':getKeuangan,
		'nbar': 'keuangan',
	}
	return render(request, 'keuangan/index.html', context)