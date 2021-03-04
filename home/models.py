from django.db import models


pilihan_kelamin = (("1", "Laki-Laki"), ("2", "Perempuan"))
pilihan_hobi = (("1", "Olahraga"), ("2", "Kesenian"), ("3", "Membaca"), ("4", "Menulis"),("5", "Jalan-Jalan"), ("6", "Lainnya"))
pilihan_citacita = (("1", "PNS"), ("2", "TNI/Porli"), ("3", "Guru/Dosen"), ("4", "Dokter"),("5", "Politikus"), ("6", "Wiraswasta"), ("7", "Seniman/Artis"), ("8", "Ilmuan"), ("9", "Agamawan"), ("10", "Lainnya"))





# Create your models here.
class DataSiswa(models.Model):
	nama =  models.CharField(max_length=255)
	nisn =  models.CharField(max_length=255)
	nik =  models.CharField(max_length=255)
	tempatlahir =  models.CharField(max_length=255)
	tanggallahir = models.DateField()
	jeniskelamin = models.CharField(max_length=1, choices=pilihan_kelamin, default=None)
	# hobi = models.CharField(max_length=1, choices=pilihan_hobi, default=None)
	# citacita = models.CharField(max_length=2, choices=pilihan_citacita, default=None)
	# anakke =  models.IntegerField()
	# jumlahsaudara =  models.IntegerField()
	# sekolahasal =  models.CharField(max_length=255)
	# hp =  models.IntegerField()
	# email = models.CharField(max_length=255)


	# def __str__(self):
	# 	return self.tanggallahir