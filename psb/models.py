from django.db import models

# Create your models here.



# tambahan jika siswa adalah
pilihan_tahunmasuk = (("2018/2019", "2018/2019"), ("2019/2020", "2019/2020"), ("2020/2021","2020/2021"))
pilihan_statussiswa = (
	("Pendaftar", "Pendaftar"),
	("Pindahan", "Pindahan"),
	("Aktif", "Aktif"),
	("Keluar", "Keluar"),
	("Lulus", "Lulus")
	)


class DataSiswaTambahan(models.Model):
	# tambahan
	tahunmasuk = models.CharField(max_length=25, choices=pilihan_tahunmasuk)
	statussiswa = models.CharField(max_length=25, choices=pilihan_statussiswa)
	nislokal = models.CharField(max_length=255)
	# kelas =