from django.db import models

# Create your models here.
class DataSiswa(models.Model):
	nama =  models.CharField(max_length=255)
	nisn =  models.CharField(max_length=255)
	nik =  models.CharField(max_length=255)
	tempatlahir =  models.CharField(max_length=255)