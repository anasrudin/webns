from django.db import models


pilihan_kelamin = (("Laki-Laki", "Laki-Laki"), ("Perempuan", "Perempuan"))
pilihan_hobi = (("Olahraga", "Olahraga"), ("Kesenian", "Kesenian"), ("Membaca", "Membaca"), ("Menulis", "Menulis"),("Jalan-Jalan", "Jalan-Jalan"), ("Lainnya", "Lainnya"))
pilihan_citacita = (("PNS", "PNS"), ("TNI/Porli", "TNI/Porli"), ("Guru/Dosen", "Guru/Dosen"), ("Dokter", "Dokter"),("Politikus", "Politikus"), ("Wiraswasta", "Wiraswasta"), ("Seniman/Artis", "Seniman/Artis"), ("Ilmuan", "Ilmuan"), ("Agamawan", "Agamawan"), ("Lainnya", "Lainnya"))




# Create your models here.
class DataSiswa(models.Model):
	nama =  models.CharField(max_length=255)
	nisn =  models.CharField(max_length=255)
	nik =  models.CharField(max_length=255)
	tempatlahir =  models.CharField(max_length=255)
	tanggallahir = models.DateField()
	jeniskelamin = models.CharField(max_length=25, choices=pilihan_kelamin, default=None)
	hobi = models.CharField(max_length=25, choices=pilihan_hobi, default=None)
	citacita = models.CharField(max_length=25, choices=pilihan_citacita, default=None)
	anakke =  models.IntegerField()
	jumlahsaudara =  models.IntegerField()
	sekolahasal =  models.CharField(max_length=255)
	hp =  models.IntegerField()
	email = models.CharField(max_length=255)





pilihan_lembaga = (("SMP", "SMP"), ("MTs", "MTs"), ("Paket C", "Paket C"), ("Lainnya", "Lainnya"))
pilihan_status_lembaga = (("Negeri", "Negeri"), ("Swasta", "Swasta"))
class DataSekolah(models.Model):
	jenislembaga = models.CharField(max_length=25, choices=pilihan_lembaga, default=None)
	statuslemaga = models.CharField(max_length=25, choices=pilihan_status_lembaga, default=None)
	npsn = models.CharField(max_length=255)
	noijazah = models.CharField(max_length=255)




pilihan_tinggal = (("Tinggal Dengan Orang Tua/Wali", "Tinggal Dengan Orang Tua/Wali"), ("Ikut Saudara/Kerabat", "Ikut Saudara/Kerabat"), ("Asrama Madrasah", "Asrama Madrasah"), ("Kontrak/Kost", "Kontrak/Kost"), ("Asrama Pesantren", "Asrama Pesantren"), ("Panti Asuhan", "Panti Asuhan"), ("Rumah Singgah", "Rumah Singgah"), ("Lainnya", "Lainnya"))
pilihan_jarak = (("Kurang dari 5 KM","Kurang dari 5 KM"),("Antara 5 - 10 KM","Antara 5 - 10 KM"),("Antara 11 - 20 KM","Antara 11 - 20 KM"),("Antara 21 - 30 KM","Antara 21 - 30 KM"),("Lebih dari 30 KM","Lebih dari 30 KM"))
pilihan_transportasi = (("Jalan Kaki","Jalan Kaki"),("Sepeda","Sepeda"),("Sepeda Motor","Sepeda Motor"),("Mobil Pribadi","Mobil Pribadi"),("Antar Jemput Sekolah","Antar Jemput Sekolah"),("Angkutan Umum","Angkutan Umum"),("Perahu/Sampan","Perahu/Sampan"),("Lainnya","Lainnya"))

# pilihan_transportasi = (("",""),("",""),("",""),("",""),("",""),("",""),("",""),("",""))

class DataTinggal(models.Model):
	jenistempattinggal = models.CharField(max_length=100, choices=pilihan_tinggal, default=None)
	alamat = models.CharField(max_length=255)
	provinsi = models.CharField(max_length=255)
	kabupatenkota = models.CharField(max_length=255)
	kecamatan = models.CharField(max_length=255)
	desa = models.CharField(max_length=255)
	kodepos = models.CharField(max_length=255) #optional
	jaraktinggal = models.CharField(max_length=100, choices=pilihan_jarak, default=None)
	transportasi = models.CharField(max_length=100, choices=pilihan_transportasi, default=None)





pilihan_status = (("", "Silahkan Pilih"),("Masih Hidup","Masih Hidup"),("Sudah Meninggal","Sudah Meninggal"),("Tidak Diketahui","Tidak Diketahui"))
pilihan_pendidikan = (("", "Silahkan Pilih"),("MI / SD / Sederajat","MI / SD / Sederajat"),("MTs / SMP","MTs / SMP"),("SMK / SMA / MA","SMK / SMA / MA"),("D1","D1"),("D2","D2"),("D3","D3"),("D4 / S1","D4 / S1"),("S2","S2"),("S3","S3"))
pilihan_pekerjaan = (
	("", "Silahkan Pilih"),
	("Tidak Bekerja","Tidak Bekerja"),
	("Pensiunan","Pensiunan"),
	("PNS","PNS"),
	("TNI/Polisi","TNI/Polisi"),
	("Guru/Dosen","Guru/Dosen"),
	("Pegawai Swasta","Pegawai Swasta"),
	("Wiraswasta/Wirausaha","Wiraswasta/Wirausaha"),
	("Pengacara/Hakim/Jaksa/Notaris","Pengacara/Hakim/Jaksa/Notaris"),
	("Seniman/Artis","Seniman/Artis"),
	("Dokter/Perawat","Dokter/Perawat"),
	("Pilot / Pramugara/i","Pilot / Pramugara/i"),
	("Pedagang","Pedagang"),
	("Petani/Peternak","Petani/Peternak"),
	("Nelayan","Nelayan"),
	("Buruh (Tani/Pabrik/Bangunan)","Buruh (Tani/Pabrik/Bangunan)"),
	("Sopir/Masinis/Kondektur","Sopir/Masinis/Kondektur"),
	("Politikus","Politikus"),
	("Lainnya","Lainnya")
	)
pilihan_penghasilan = (("Kurang Dari Rp 500.000,-","Kurang Dari Rp 500.000,-"), ("Rp 500.000 - 1.000.000", "Rp 500.000 - 1.000.000"), ("Rp 1.000.000 - 2.000.000", "Rp 1.000.000 - 2.000.000"), ("Rp 2.000.000 - 3.000.000","Rp 2.000.000 - 3.000.000"), ("Rp 3.000.000 - 5.000.000","Rp 3.000.000 - 5.000.000"),("Lebih Dari Rp 5.000.000","Lebih Dari Rp 5.000.000"))
pilihan_sktm = (
	("Ya","Ya (Harap Lampirkan SKTM kepada pihak Madrasah)"),
	("Tidak","Tidak"))


class DataOrtu(models.Model):
	nokk = models.CharField(max_length=255)
	kepalakeluarga = models.CharField(max_length=255)
	# ayah
	ayah = models.CharField(max_length=255)
	tanggallahirayah = models.DateField()
	statusayah = models.CharField(max_length=100, choices=pilihan_status, default=None)
	nikayah = models.CharField(max_length=255) #optional
	pendidikanayah = models.CharField(max_length=100, choices=pilihan_pendidikan, default=None) #optional
	pekerjaanayah = models.CharField(max_length=100, choices=pilihan_pekerjaan, default=None) #optional
	# ibu
	ibu = models.CharField(max_length=255)
	tanggallahiribu = models.DateField()
	statusibu = models.CharField(max_length=100, choices=pilihan_status, default=None)
	nikibu = models.CharField(max_length=255) #optional
	pendidikanibu = models.CharField(max_length=100, choices=pilihan_pendidikan, default=None) #optional
	pekerjaanibu = models.CharField(max_length=100, choices=pilihan_pekerjaan, default=None) #optional
	# wali
	wali = models.CharField(max_length=255) #optional
	tanggallahirwali = models.DateField(null=True) #optional
	statuswali = models.CharField(max_length=100, choices=pilihan_status, default=None) #optional
	nikwali = models.CharField(max_length=255) #optional
	pendidikanwali = models.CharField(max_length=100, choices=pilihan_pendidikan, default=None) #optional
	pekerjaanwali = models.CharField(max_length=100, choices=pilihan_pekerjaan, default=None) #optional
	# penghasilan
	penghasilan = models.CharField(max_length=100, choices=pilihan_penghasilan, default=None)
	kks = models.CharField(max_length=255) #optional
	pkh = models.CharField(max_length=255) #optional
	kip =models.CharField(max_length=255) #optional
	alamatortuwali = models.CharField(max_length=255) 
	sktm = models.CharField(max_length=100, choices=pilihan_sktm, default=None)



class DataMotivasi(models.Model):
	motivasi = models.CharField(max_length=255)

