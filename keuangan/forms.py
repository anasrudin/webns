from django import forms
from .models import Kas

class KasForm(forms.ModelForm):
	class Meta:
		model = Kas
		fields = '__all__'
		widget = {
		'kodetransaksi' : forms.TextInput(attrs={'class':'form-control'}),
		'jenistransaksi' : forms.Select(attrs={'class':'form-control'}),
		'nominal' : forms.TextInput(attrs={'class':'form-control'}),
		'keterangan' : forms.TextInput(attrs={'class':'form-control'}),
		}
		labels = {
		'kodetransaksi':'Kode Transaksi *', 
		'jenistransaksi':'Jenis Transaksi *', 
		'nominal':'Nominal', 
		'keterangan':'Keterangan ',
		}
		use_required_attribute = True

	def __init__(self, *args, **kwargs):
		super(KasForm, self).__init__(*args, **kwargs)
		self.fields['saldo'].required = False