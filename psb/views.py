from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User


# Create your views here.
@login_required(login_url='/login/')
def index(request):
	context = {
		"page_title":"Psb",
		'nbar': 'psb',
	}
	return render(request, 'psb/index.html', context)


@login_required(login_url='/login/')
def indexPsb(request):
	getPsb = Psb.objects.all()
	context = {
		'page_title':'c',
		'getPsb':getPsb,
		'nbar': 'psb',
	}
	return render(request, 'psb/index.html', context)