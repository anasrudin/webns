from django.db import models
from django.apps import apps


from home.models import DataSiswa

# Create your models here.

# class Psb(models.Model):
# 	siswa_id = models.ForeignKey('home.DataSiswa', on_delete=models.CASCADE, null=True, blank=True)


# # tambahan jika siswa adalah
# pilihan_tahunmasuk = (("2018/2019", "2018/2019"), ("2019/2020", "2019/2020"), ("2020/2021","2020/2021"))
# pilihan_statussiswa = (
# 	("Pendaftar", "Pendaftar"),
# 	("Pindahan", "Pindahan"),
# 	("Aktif", "Aktif"),
# 	("Keluar", "Keluar"),
# 	("Lulus", "Lulus")
# 	)


# class DataSiswaTambahan(models.Model):
# 	# tambahan
# 	tahunmasuk = models.CharField(max_length=25, choices=pilihan_tahunmasuk)
# 	statussiswa = models.CharField(max_length=25, choices=pilihan_statussiswa)
# 	nislokal = models.CharField(max_length=255)
# 	# kelas =


# # HomeDataSiswa = get_model('home', 'DataSiswa')

# class HomeDataSiswa(models.Model):
#    psbmodel = models.ForeignKey('home.DataSiswa', on_delete=models.CASCADE, null=True, blank=True)

# class HomeDataSiswa(models.Model):
# 	psbmodel = models.ManyToManyField(DataSiswa)