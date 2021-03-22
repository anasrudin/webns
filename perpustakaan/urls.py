from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

from . import views

app_name = 'perpustakaan'
urlpatterns = [
    path('', views.index, name='indexPerpustakaan'),
    path('transaksi/', views.transaksiPeminjaman, name='transaksiPeminjaman'),
    path('katalog/', views.katalogPeminjaman, name='katalogPeminjaman'),
    path('pinjam/', views.peminjaman, name='peminjamanBuku'),
    path('tambahbuku/', views.tambahbuku, name='tambahbuku'),
    path('denda/', views.daftarDenda, name='daftarDenda'),
]

