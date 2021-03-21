from django.db import models
from django.contrib import admin
# Create your models here.


class ScoreSiswa(models.Model):
	siswa_id = models.ForeignKey('home.DataKegiatan', on_delete=models.CASCADE, null=True, blank=True)
	skorpelanggaran = models.IntegerField()
	kehadiransiswa = models.IntegerField()