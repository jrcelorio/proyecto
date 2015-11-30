from django import forms
from comunioapp.models import Equipo

class ComunioForm(forms.ModelForm):

	class Meta:
		model = Equipo
		fields = ('nombre',)
