from django import forms
from appMTV.models import Familiar

class Buscar(forms.Form):
    nombre = forms.CharField(max_length=100)
    
class FamiliarForm(forms.ModelForm):
  class Meta:
    model = Familiar
    fields = ['nombre', 'direccion', 'numero_pasaporte']