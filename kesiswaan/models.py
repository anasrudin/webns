from django.db import models
from django.contrib import admin

from datetime import date
from datetime import datetime, timedelta

from django.utils import timezone

from home.models import DataKegiatan


from home.models import DataSiswa


from django.utils.timezone import now
# Create your models here.


class ScoreSiswa(models.Model):
	# siswa_id = models.ForeignKey(DataKegiatan, on_delete=models.CASCADE, null=True, blank=True)
	nama =  models.CharField(max_length=255)
	nislokal =  models.CharField(max_length=255)
	skorpelanggaran = models.IntegerField()
	# kehadiransiswa = models.IntegerField()
	tanggalpelanggaran = models.DateField(default=now, blank=True)
	keterangan =  models.CharField(max_length=255, null=True, blank=True)


pilihan_hadir = (
	("Hadir","Hadir)"),
	("Sakit","Sakit"),
	("Izin","Izin"),
	("Alfa","Alfa"),
	)


class KehadiranSiswa(models.Model):
	# datasiswa = models.ForeignKey(to='home.DataSiswa', related_name='hadir', null=True, blank=True)
	# datasiswa = models.ForeignKey(DataSiswa, on_delete=models.CASCADE, null=True, blank=True)
	datasiswa = models.ManyToManyField(DataSiswa)
	tanggalkbm = models.DateField(auto_now=False, auto_now_add=False)
	status = models.CharField(max_length=100, null=True, blank=True, choices=pilihan_hadir, default="Hadir")
	catatan = models.CharField(max_length=255)


# futuredate = datetime.now() + timedelta(days=10)