from django.db import models

# Create your models here.


from datetime import date


# Create your models here.


class Buku(models.Model):
	kodebuku =  models.CharField(max_length=255, unique=True)
	judulbuku =  models.CharField(max_length=255)
	pengarang =  models.CharField(max_length=255)
	def __str__(self):
		return 'Buku: {}'.format(' ' + self.judulbuku +' (' +self.kodebuku +') ')


class Pinjam(models.Model):
	buku =  models.ManyToManyField(Buku)
	nislokal =  models.CharField(max_length=255)
	nama =  models.CharField(max_length=255)
	tanggalpinjam = models.DateField()
	tanggalkembali = models.DateField()