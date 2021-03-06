from django import forms
from .models import Hora,Medico
from django.contrib import messages

class HorasForm(forms.ModelForm):
    class Meta:
        model = Hora
        fields = ['fecha', 'hora', 'valor', 'paciente', 'medico']

        labels = {
            'fecha': 'Fecha',
            'hora': 'Hora',
            'valor': 'Valor',
            'paciente': 'Paciente',
            'medico': 'Médico'
        }
        widgets = {
            
            'fecha': forms.DateInput(attrs={'class': 'form-control'}),
            'hora': forms.TimeInput(attrs={'class': 'form-control'}),
            'valor': forms.TextInput(attrs={'class': 'form-control'}),
            'paciente': forms.TextInput(attrs={'class': 'form-control'}),
            'medico': forms.TextInput(attrs={'class': 'form-control'})
        }