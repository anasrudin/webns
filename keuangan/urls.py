from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

from . import views

app_name = 'keuangan'
urlpatterns = [
    path('', views.index, name='indexKeuangan'),
    path('inputTransaksi/', views.inputTransaksi, name='inputTransaksi'),
    path('daftarTransaksi/', views.daftarTransaksi, name='daftarTransaksi'),
    path('daftarInfaq/', views.daftarInfaq, name='daftarInfaq'),
    # path('deleteTransaksi/', views.deleteTransaksi, name='deleteTransaksi'),
    url(r'^deleteTransaksi/(?P<id>[0-9]+)$', views.deleteTransaksi, name='deleteTransaksi'),
]