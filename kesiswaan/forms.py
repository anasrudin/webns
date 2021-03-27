from django import forms
from .models import KehadiranSiswa


class KehadiranSiswaForm(forms.ModelForm):
	class Meta:
		model = KehadiranSiswa
		fields  = '__all__'
		widget = {
		'status': forms.Select(attrs={'class':'form-control'}),
		'catatan': forms.TextInput(attrs={'class':'form-control'}),
		}
	def __init__(self, *args, **kwargs):
		super(KehadiranSiswaForm, self).__init__(*args, **kwargs)
		self.fields['tanggalkbm'].initial = timezone.now()
