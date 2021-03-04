from django import forms
from .models import DataSiswa


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
		# 'hobi': forms.Select(attrs={'class':'form-control'}),
		# 'citacita': forms.Select(attrs={'class':'form-control'}),
		# 'anakke': forms.TextInput(attrs={'class':'form-control'}),
		# 'jumlahsaudara': forms.TextInput(attrs={'class':'form-control'}),
		# 'sekolahasal' : forms.TextInput(attrs={'class':'form-control'}),
		# 'hp': forms.TextInput(attrs={'class':'form-control'}),
		# 'email': forms.TextInput(attrs={'class':'form-control'}),


		}

		labels = {
		'nama':'Nama Lengkap *', 
		'nisn':'NISN', 
		'nik':'NIK *', 
		'tempatlahir':'Tempat Lahir *', 
		}
		use_required_attribute = True



	def __init__(self, *args, **kwargs):
		super(DataSiswaForm, self).__init__(*args, **kwargs)
		self.fields['nisn'].required = False
		self.fields['nisn'].widget.attrs['placeholder'] = ' jika memiliki'
		self.fields['tanggallahir'].widget = DateInput()

	# def clean_jeniskelamin(self):
	# 	value = self.cleaned_data.get('jeniskelamin')

	# 	return dict(self.fields['jeniskelamin'].choices)[value]


