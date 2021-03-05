from django import forms
from .models import DataSiswa, DataSekolah, DataTinggal, DataOrtu, DataMotivasi


class DateInput(forms.DateInput):
    input_type = "date"

    def __init__(self, **kwargs):
        kwargs["format"] = "%Y-%m-%d"
        super().__init__(**kwargs)


class DataSiswaForm(forms.ModelForm):
	class Meta:
		model = DataSiswa
		fields  = '__all__'
		widget = {
		'nama': forms.TextInput(attrs={'class':'form-control'}),
		'nisn': forms.TextInput(attrs={'class':'form-control'}),
		'nik': forms.TextInput(attrs={'class':'form-control'}),
		'tempatlahir': forms.TextInput(attrs={'class':'form-control'}),
		'jeniskelamin' : forms.Select(attrs={'class':'form-control'}),
		'hobi': forms.Select(attrs={'class':'form-control'}),
		'citacita': forms.Select(attrs={'class':'form-control'}),
		'anakke': forms.TextInput(attrs={'class':'form-control'}),
		'jumlahsaudara': forms.TextInput(attrs={'class':'form-control'}),
		'sekolahasal' : forms.TextInput(attrs={'class':'form-control'}),
		'hp': forms.TextInput(attrs={'class':'form-control'}),
		'email': forms.TextInput(attrs={'class':'form-control'}),


		}

		labels = {
		'nama':'Nama Lengkap *', 
		'nisn':'NISN', 
		'nik':'NIK *', 
		'tempatlahir':'Tempat Lahir *',
		'tanggallahir':'Tanggal Lahir *',
		'jeniskelamin':'Jenis Kelamin *',
		'hobi': 'Hobi *',
		'citacita': 'Cita-Cita *',
		'anakke': 'Anak Ke- *',
		'jumlahsaudara': 'Jumlah Saudara *',
		'sekolahasal' : 'Madrasah / Sekolah Asal *',
		'hp': 'No HP / WA *',
		'email': 'Email',
		}
		use_required_attribute = True



	def __init__(self, *args, **kwargs):
		super(DataSiswaForm, self).__init__(*args, **kwargs)
		self.fields['nisn'].required = False
		self.fields['nisn'].widget.attrs['placeholder'] = 'Nomor Induk Siswa Nasional Terdapat Pada Raport / Ijazah'
		self.fields['tanggallahir'].widget = DateInput()
		self.fields['email'].required = False
		self.fields['nik'].widget.attrs['placeholder'] = 'Nomor Induk Kependudukan terdapat pada Kartu Keluarga'
		self.fields['anakke'].widget.attrs['placeholder'] = 'Hanya boleh diisi dengan angka. Misal : 2'
		self.fields['jumlahsaudara'].widget.attrs['placeholder'] = 'Hanya boleh diisi dengan angka. Misal : 3'
		self.fields['sekolahasal'].widget.attrs['placeholder'] = 'Madrasah/Sekolah asal. Misal : MTsN Kota Bandung'
		self.fields['hp'].widget.attrs['placeholder'] = 'No HP / WA Aktif'
		self.fields['email'].widget.attrs['placeholder'] = 'Kosongkan jika tidak memiliki Email'



	# def clean_jeniskelamin(self):
	# 	value = self.cleaned_data.get('jeniskelamin')

	# 	return dict(self.fields['jeniskelamin'].choices)[value]

class DataSekolahForm(forms.ModelForm):
	class Meta:
		model = DataSekolah
		fields = '__all__'
		widget = {
		'jenislembaga' : forms.TextInput(attrs={'class':'form-control'}),
		'statuslemaga' : forms.TextInput(attrs={'class':'form-control'}),
		'npsn' : forms.TextInput(attrs={'class':'form-control'}),
		'noijazah' : forms.TextInput(attrs={'class':'form-control'}),
		}
		labels = {
		'jenislembaga':'Jenis Lembaga *', 
		'statuslemaga':'Status Lembaga *', 
		'npsn':'NPSN', 
		'noijazah':'Nomor Seri Ijazah',
		}
		use_required_attribute = True

	def __init__(self, *args, **kwargs):
		super(DataSekolahForm, self).__init__(*args, **kwargs)
		self.fields['npsn'].required = False
		self.fields['noijazah'].required = False
		self.fields['npsn'].widget.attrs['placeholder'] = 'NPSN terdapat pada ijazah. Kosongkan jika tidak tahu'
		self.fields['noijazah'].widget.attrs['placeholder'] = 'Terdapat pada paling bawah ijazah. Kosongkan jika belum mempunyai Ijazah'

class DataTinggalForm(forms.ModelForm):
	class Meta:
		model  = DataTinggal 
		fields = '__all__'
		widget = {
		'jenistempattinggal' : forms.Select(attrs={'class':'form-control'}),
		'alamat ' : forms.TextInput(attrs={'class':'form-control'}),
		'provinsi' : forms.TextInput(attrs={'class':'form-control'}),
		'kabupatenkota' : forms.TextInput(attrs={'class':'form-control'}),
		'kecamatan' : forms.TextInput(attrs={'class':'form-control'}),
		'desa' : forms.TextInput(attrs={'class':'form-control'}),
		'kodepos' : forms.TextInput(attrs={'class':'form-control'}),
		'jaraktinggal' : forms.Select(attrs={'class':'form-control'}),
		'transportasi' : forms.Select(attrs={'class':'form-control'}),
		}
		labels = {
		'jenistempattinggal' : 'Jenis tempat tinggal *',
		'alamat ' : 'Alamat *',
		'provinsi' : 'Provinsi *',
		'kabupatenkota' : 'Kabupaten / Kota *',
		'kecamatan' : 'Kecamatan *',
		'desa' : 'Desa *',
		'kodepos' : 'Kode Pos',
		'jaraktinggal' : 'Jarak tempat tinggal *',
		'transportasi' : 'Transportasi Yang Dipakai *',
		}

		use_required_attribute = True

	def __init__(self, *args, **kwargs):
		super(DataTinggalForm, self).__init__(*args, **kwargs)
		self.fields['kodepos'].required = False
		self.fields['alamat'].widget.attrs['placeholder'] = 'Nama jalan / Kp / RT ? RW. Misal . Jl. Raya Cipatik no 16'

class DataOrtuForm(forms.ModelForm):
	class Meta:
		model = DataOrtu
		fields = '__all__'
		widget = {
		'nokk' : forms.TextInput(attrs={'class':'form-control'}),
		'kepalakeluarga' : forms.TextInput(attrs={'class':'form-control'}),
		# ayah
		'ayah' : forms.TextInput(attrs={'class':'form-control'}),
		'statusayah': forms.Select(attrs={'class':'form-control'}),
		'nikayah' : forms.TextInput(attrs={'class':'form-control'}),
		'pendidikanayah' : forms.Select(attrs={'class':'form-control'}),
		'pekerjaanayah' : forms.Select(attrs={'class':'form-control'}),
		# ibu
		'ibu' : forms.TextInput(attrs={'class':'form-control'}),

		'statusibu' : forms.Select(attrs={'class':'form-control'}),
		'nikibu' : forms.TextInput(attrs={'class':'form-control'}),
		'pendidikanibu' : forms.Select(attrs={'class':'form-control'}),
		'pekerjaanibu' : forms.Select(attrs={'class':'form-control'}),
		# wali
		'wali' : forms.TextInput(attrs={'class':'form-control'}),

		'statuswali' : forms.Select(attrs={'class':'form-control'}),
		'nikwali' : forms.TextInput(attrs={'class':'form-control'}),
		'pendidikanwali' : forms.Select(attrs={'class':'form-control'}),
		'pekerjaanwali' : forms.Select(attrs={'class':'form-control'}),
		# penghasilan
		'penghasilan' : forms.Select(attrs={'class':'form-control'}),
		'kks' : forms.TextInput(attrs={'class':'form-control'}),
		'pkh' : forms.TextInput(attrs={'class':'form-control'}),
		'kip' : forms.TextInput(attrs={'class':'form-control'}),
		'alamatortuwali' : forms.TextInput(attrs={'class':'form-control'}),
		'sktm' : forms.Select(attrs={'class':'form-control'}),

		}
		labels = {
		'nokk' : 'Nomor Kartu Keluarga *',
		'kepalakeluarga' : 'Nama Kepala Keluarga *',
		# ayah
		'ayah' : 'Nama Lengkap Ayah Kandung *',
		'statusayah': 'Status Ayah Kandung *',
		'nikayah' : 'NIK / Nomor KTP Ayah Kandung',
		'pendidikanayah' : 'Pendidikan Ayah',
		'pekerjaanayah' : 'Pekerjaan Ayah',
		# ibu
		'ibu' : 'Nama Lengkap Ibu Kandung *',

		'statusibu' : 'Status Ibu Kandung *',
		'nikibu' : 'NIK / Nomor KTP Ibu Kandung',
		'pendidikanibu' : 'Pendidikan Ibu',
		'pekerjaanibu' : 'Pekerjaan Ibu',
		# wali
		'wali' : 'Nama Lengkap Wali',

		'statuswali' : 'Status Wali',
		'nikwali' : 'NIK / Nomor KTP Wali',
		'pendidikanwali' : 'Pendidikan Wali',
		'pekerjaanwali' : 'Pekerjaan Wali',
		# penghasilan
		'penghasilan' : 'Rata-Rata Penghasilan Orang Tua/Wali: Per Bulan *',
		'kks' : 'KKS',
		'pkh' : 'PKH',
		'kip' : 'KIP',
		'alamatortuwali' : 'Alamat Tempat Tinggal Orang Tua/Wali *',
		'sktm' : 'Memiliki Surat Keterangan Tidak Mampu',
		'tanggallahirayah' : 'Tanggal Lahir Ayah *',
		'tanggallahiribu' : 'Tanggal Lahir Ibu *',
		'tanggallahirwali' : 'Tanggal Lahir Wali',

		}

	def __init__(self, *args, **kwargs):
		super(DataOrtuForm, self).__init__(*args, **kwargs)
		self.fields['nikayah'].required = False
		self.fields['pendidikanayah'].required = False
		self.fields['pekerjaanayah'].required = False
		self.fields['nikibu'].required = False
		self.fields['pendidikanibu'].required = False
		self.fields['pekerjaanibu'].required = False
		self.fields['tanggallahirayah'].widget = DateInput()
		self.fields['tanggallahiribu'].widget = DateInput()
		self.fields['tanggallahirwali'].widget = DateInput()
		self.fields['wali'].required = False
		self.fields['tanggallahirwali'].required = False
		self.fields['statuswali'].required = False
		self.fields['nikwali'].required = False
		self.fields['pendidikanwali'].required = False
		self.fields['pekerjaanwali'].required = False
		self.fields['kks'].required = False
		self.fields['pkh'].required = False
		self.fields['kip'].required = False
		self.fields['kks'].widget.attrs['placeholder'] = 'Nomor Kartu Keluarga Sejahtera (KKS)'
		self.fields['pkh'].widget.attrs['placeholder'] = 'Nomor Kartu Program Keluarga Harapan (PKH)'
		self.fields['kip'].widget.attrs['placeholder'] = 'Nomor Kartu Indonesia Pintar (KIP)'


class DataMotivasiForm(forms.ModelForm):
	class Meta:
		model = DataMotivasi
		fields = ['motivasi']
		widget = { 
		'motivasi' : forms.TextInput(attrs={'class':'form-control'}),
		}
		labels = {
		'motivasi' : 'Motivasi*'
		}
	def __init__(self, *args, **kwargs):
		super(DataMotivasiForm, self).__init__(*args, **kwargs)
		self.fields['motivasi'].widget.attrs['placeholder'] = 'Tulis alasan/motivasi anda ingin bersekolah di MA Nuurus Salaam'