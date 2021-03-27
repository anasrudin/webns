from django.db import models
from django.utils.timezone import now


# Create your models here.
pilihan_transaksi = (
	("Infaq","Infaq"),
	("Pengeluaran","Pengeluaran"))
class Kas(models.Model):
	kodetransaksi = models.CharField(max_length=255)
	jenistransaksi = models.CharField(max_length=25, choices=pilihan_transaksi, default=None)
	nominal = models.IntegerField()
	keterangan = models.CharField(max_length=255)
	saldo = models.IntegerField(default=0)
	tanggaltransaksi = models.DateField(default=now, blank=True)

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		if self.jenistransaksi=="Infaq":
			self.saldo = self.saldo + self.nominal
		elif self.jenistransaksi=="Pengeluaran":
			self.saldo = self.saldo - self.nominal
		super().save(*args, **kwargs)
