from django import forms
from .models import Suporte
from django.forms import ModelForm

class SuporteForm(forms.ModelForm):

    class Meta:
        model = Suporte
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'mensagem': forms.TextInput(attrs={'class': 'form-control'}),

        }