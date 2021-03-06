from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from espacioApp.models import Residente, Administrativo, EspacioComun, Reserva, Reporte, TipoEspacioComun, TipoReporte, GastoComun

class CrearForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '12345678-9', 'class': 'form-control'}))
    password1 = forms.CharField(strip=False,widget=forms.PasswordInput(attrs={'placeholder': '********', 'class': 'form-control'}))
    password2 = forms.CharField(strip=False,widget=forms.PasswordInput(attrs={'placeholder': '********', 'class': 'form-control'}))
    def __init__(self, *args, **kwargs):
        super(CrearForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

class ResidenteForm(forms.ModelForm):
    class Meta:
        model = Residente
        fields = ['nombre','apellido_pat','apellido_mat','mail']
    nombre = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Cesar', 'class': 'form-control' }))
    apellido_pat = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Poblete', 'class': 'form-control'}))
    apellido_mat = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Sepúlveda', 'class': 'form-control'}))
    mail = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'mail@ejemplo.com', 'class': 'form-control'}))

class FiltroResidenteForm(forms.ModelForm):
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

class ModificarResidenteForm(forms.ModelForm):
    class Meta:
        model = Residente
        fields = ['nombre','apellido_pat','apellido_mat','mail', 'morosidad', 'habilitado']
    nombre = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Cesar', 'class': 'form-control' }))
    apellido_pat = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Poblete', 'class': 'form-control'}))
    apellido_mat = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Sepúlveda', 'class': 'form-control'}))
    mail = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'mail@ejemplo.com', 'class': 'form-control'}))
    morosidad = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}), required=False)
    habilitado = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}), required=False)

class AdministrativoForm(forms.ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    apellido_pat = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    apellido_mat = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    mail = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Administrativo
        fields = ['nombre','apellido_pat','apellido_mat','mail','tipo_administrativo']

class EspacioForm(forms.ModelForm):
    class Meta:
        model = EspacioComun
        fields = "__all__"
    tipo_espacio = forms.ModelChoiceField(queryset=TipoEspacioComun.objects.all())

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['horario','id_espacio']

class ReportarForm(forms.ModelForm):
    class Meta:
        model = Reporte
        fields = ['mensaje', 'tipo_reporte', 'residente_rut']

class GastosForm (forms.ModelForm):
    class Meta:
        model= GastoComun
        fields = ['valor', 'fecha_emision', 'fecha_vencimiento', 'estado', 'residente_rut']        
    valor= forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control' }))   
    fecha_emision = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'yyyy-mm-dd'}))
    fecha_vencimiento = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'yyyy-mm-dd'}))
