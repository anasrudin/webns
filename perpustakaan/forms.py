from django import forms
from .models import Buku, Pinjam


class DateInput(forms.DateInput):
    input_type = "date"

    def __init__(self, **kwargs):
        kwargs["format"] = "%Y-%m-%d"
        super().__init__(**kwargs)



class BukuForm(forms.ModelForm):
	class Meta:
		model = Buku
		fields  = '__all__'
		widget = {
		'kodebuku': forms.TextInput(attrs={'class':'form-control'}),
		'judulbuku': forms.TextInput(attrs={'class':'form-control'}),
		'pengarang': forms.TextInput(attrs={'class':'form-control'}),
		}
	def __init__(self, *args, **kwargs):
		super(BukuForm, self).__init__(*args, **kwargs)
		self.fields['pengarang'].required = False






class PinjamForm(forms.ModelForm):
	class Meta:
		model = Pinjam
		fields  = '__all__'
		widget = {
		'nislokal': forms.TextInput(attrs={'class':'form-control'}),
		'nama': forms.TextInput(attrs={'class':'form-control'}),
		'buku': forms.TextInput(attrs={'class':'form-control'}),
		'statuspinjaman': forms.Select(attrs={'class':'form-control'}),
		'nominaldenda': forms.TextInput(attrs={'class':'form-control'}),
		}
	def __init__(self, *args, **kwargs):
		super(PinjamForm, self).__init__(*args, **kwargs)
		self.fields['nama'].required = False
		self.fields['tanggalpinjam'].widget = DateInput()
		self.fields['tanggalkembali'].widget = DateInput()
		self.fields['nominaldenda'].required = False





