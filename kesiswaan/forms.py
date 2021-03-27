from django import forms
from .models import KehadiranSiswa, ScoreSiswa


class DateInput(forms.DateInput):
    input_type = "date"

    def __init__(self, **kwargs):
        kwargs["format"] = "%Y-%m-%d"
        super().__init__(**kwargs)





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


class ScoreSiswaForm(forms.ModelForm):
	class Meta:
		model = ScoreSiswa
		fields = '__all__'
		widget = {
		'nama': forms.TextInput(attrs={'class':'form-control'}),
		'nislokal': forms.TextInput(attrs={'class':'form-control'}),
		'skorpelanggaran': forms.TextInput(attrs={'class':'form-control'}),
		'keterangan': forms.TextInput(attrs={'class':'form-control'}),
		}
	def __init__(self, *args, **kwargs):
		super(ScoreSiswaForm, self).__init__(*args, **kwargs)
		# self.fields['tanggalpelanggaran'].initial = timezone.now()
		self.fields['tanggalpelanggaran'].widget = DateInput()