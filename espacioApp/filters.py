from django import forms
import django_filters
from espacioApp.models import Residente

class ResidenteFiltro(django_filters.FilterSet):
    class Meta:
        model = Residente
        fields = ['rut', 'nombre','apellido_pat','apellido_mat','mail', 'morosidad', 'habilitado']
    rut = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Cesar', 'class': 'form-control' }))
    nombre = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Cesar', 'class': 'form-control' }))
    apellido_pat = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Poblete', 'class': 'form-control'}))
    apellido_mat = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Sepúlveda', 'class': 'form-control'}))
    mail = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'mail@ejemplo.com', 'class': 'form-control'}))
    morosidad = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    habilitado = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))