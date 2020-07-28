from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    context = {
    'page_title': 'Home',
    }
    
    return render(request, 'index.html', context)