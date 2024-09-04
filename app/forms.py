from django import forms
from .models import SocioTorcedor

class SocioTorcedorForm(forms.ModelForm):
    class Meta:
        model = SocioTorcedor
        fields = ['nome', 'email', 'forma_pagamento']
