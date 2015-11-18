from django import forms
from comunioapp.models import Jugadores
from comunioapp.models import Equipo

class ComunioForm(forms.ModelForm):

	class Meta:
		model = Jugadores
		fields = ('nombre','equipo',)
