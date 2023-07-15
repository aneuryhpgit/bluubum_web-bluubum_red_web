from django import forms
from .models import Confirmacion

class ConfirmacionForm(forms.Form):
    codigo = forms.CharField(max_length=6, required=True, widget=forms.TextInput(attrs={'placeholder': 'Código de confirmación'}))

    def clean_codigo(self):
        codigo = self.cleaned_data['codigo']

        try:
            confirmacion = Confirmacion.objects.get(codigo=codigo)
        except Confirmacion.DoesNotExist:
            raise forms.ValidationError('El código de confirmación es inválido.')

        if confirmacion.caducado():
            confirmacion.delete()
            raise forms.ValidationError('El código de confirmación ha caducado. Por favor, solicite un nuevo código de confirmación.')

        return codigo
    

