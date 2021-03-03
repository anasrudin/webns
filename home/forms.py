from django import forms
from .models import DataSiswa




class DataSiswaForm(forms.ModelForm):
	class Meta:
		model = DataSiswa
		fields  = '__all__'
		widget = {
		'nama': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Search'}),
		'nisn': forms.TextInput(attrs={'class':'form-control'}),
		'nik': forms.TextInput(attrs={'class':'form-control'}),
		'tempatlahir': forms.TextInput(attrs={'class':'form-control'}),

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

	# def clean(self):
	# 	cleaned_data = super().clean()
	# 	raise forms.ValidationError("This error was added to show the non field errors styling.")
	# 	return cleaned_data