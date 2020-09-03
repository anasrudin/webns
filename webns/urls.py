"""webns URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import include, path

from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views

from .views import index, loginView, logoutView

urlpatterns = [
	path('', include('home.urls')),
    url(r'^$', RedirectView.as_view(url='/login/')),
	url(r'^login/$', loginView, name="login"),
    url(r'^logout/$', logoutView, name="logout"),
    path('kesiswaan/', include('kesiswaan.urls', namespace='kesiswaan')),    
    path('keuangan/', include('keuangan.urls', namespace='keuangan')),
    path('perpustakaan/', include('perpustakaan.urls', namespace='perpustakaan')),
    path('admin/', admin.site.urls),
]
