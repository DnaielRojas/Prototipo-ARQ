###IMPORT ESCENCIALES###
from django.shortcuts import render, redirect

###IMPORT MODELOS###
from espacioApp.models import *
from django.contrib.auth.models import User

###IMPORT REGISTROS###
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

###IMPORT LOGIN###
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

###FUNCIONES Y CLASES###
class crearForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
    username = forms.CharField(label="Rut (Obligatorio)",widget=forms.TextInput(attrs={'placeholder': '12345678-9'}))
    password1 = forms.CharField(label="Contraseña (Obligatorio)",strip=False,widget=forms.PasswordInput(attrs={'placeholder': '********'}))
    password2 = forms.CharField(label="Repetir Contraseña (Obligatorio)",strip=False,widget=forms.PasswordInput(attrs={'placeholder': '********'}))
    def __init__(self, *args, **kwargs):
        super(crearForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

###VISTAS###
def index(request):
    return render(request, 'home.html', {})

def registro(request):
    formulario = crearForm()
    if request.method == 'POST':
        formulario = crearForm(request.POST)
        filtroRut = Residente.objects.filter(rut=request.POST['username']).first()
        filtroMail = Residente.objects.filter(mail=request.POST['regMail']).first()
        if filtroRut is not None:
            messages.success(request,'Registro Incorrecto: Rut duplicado')
            return redirect('/registro')
        elif filtroMail is not None:
            messages.success(request,'Registro Incorrecto: Mail duplicado')
            return redirect('/registro')
        elif formulario.is_valid():
            formulario.save()
            nuevoResidente = Residente(
                rut=request.POST['username'],
                nombre=request.POST['regNombre'],
                apellido_pat=request.POST['regAp_pat'],
                apellido_mat=request.POST['regAp_mat'],
                mail=request.POST['regMail'],
                django_user=User.objects.latest('id'),
                morosidad=0,
                habilitado=1)
            nuevoResidente.save()
            messages.success(request,'Registro Exitoso')
            return redirect('/')
        else:
            messages.success(request,'Registro Incorrecto: Error de formulario')
            return redirect('/registro')
    return render(request, 'registro.html', {'formulario':formulario})