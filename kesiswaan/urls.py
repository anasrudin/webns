from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

from . import views

app_name = 'kesiswaan'
urlpatterns = [
    path('', views.index, name='indexKesiswaan'),
    path('masterData/', views.masterData, name='masterData'),
    path('pelanggaran/', views.pelanggaran, name='pelanggaran'),
    path('kehadiran/', views.kehadiran, name='kehadiran'),
    path('daftarSiswa/', views.daftarSiswa, name='daftarSiswa'),
    path('tambahPelanggar/', views.tambahPelanggar, name='tambahPelanggar'),
    url(r'^deletePelanggar/(?P<id>[0-9]+)$', views.deletePelanggar, name='deletePelanggar'),
    url(r'^updatePelanggar/(?P<id>[0-9]+)$', views.updatePelanggar, name='updatePelanggar'),
]