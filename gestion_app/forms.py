# En forms.py
from django import forms
from .models import Activo, Report

class ActivoForm(forms.ModelForm):
    class Meta:
        model = Activo
        fields = ['titulo','fecha_inicio', 'fecha_fin']


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['nombre_responsable', 'email',
                  'estado_activo', 'descripcion', 'activo_titulo']

class LoginForm(forms.Form):
    username = forms.CharField(label='Usuario', required=True)
    password = forms.CharField(label='Contraseña', required=True, widget=forms.PasswordInput)

