from django import forms
from recetas.models import Receta

class RecetaForm(forms.ModelForm):

	class Meta:
		model = Receta
		fields = ('nombre','ingredientes','instrucciones',)
