from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect

from django.contrib.auth import authenticate, login, logout

class IndexView(TemplateView):
	template_name = 'index.html'

def index(request):
	context = {
		'page_title': 'Home',
	}
	
	return render(request, 'login.html', context)


def loginView(request):
	context = {
		'page_title':'LOGIN',
	}
	user = None
	
	if request.method == "POST":
		
		username_login = request.POST['username']
		password_login = request.POST['password']
		
		user = authenticate(request, username=username_login, password=password_login)

		if user is not None:
			login(request, user)
			return HttpResponseRedirect('/perpustakaan')
		else:
			return HttpResponseRedirect('/login')

	return render(request, 'login.html', context)


def logoutView(request):
	logout(request)
	return HttpResponseRedirect('/login')
	# context = {
	# 	'page_title':'logout'
	# }

	#if request.method == "POST":
	#	if request.POST["logout"] == "Submit":
	#		logout(request)

	#	return redirect('index')	


	#return render(request, 'login.html', context)













