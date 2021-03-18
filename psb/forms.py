from django import forms
from .models import Psb
# from home.models import DataSiswa


class postingModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s (%s)" % (obj.id, obj.nama)


# class PsbForm(forms.ModelForm):
	# posting_id = postingModelChoiceField(label="DataSiswa", queryset=DataSiswa.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))