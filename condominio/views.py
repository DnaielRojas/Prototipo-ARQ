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
from django.contrib.auth import authenticate, logout as auth_logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

###FUNCIONES Y CLASES###
class crearForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '12345678-9'}))
    password1 = forms.CharField(strip=False,widget=forms.PasswordInput(attrs={'placeholder': '********'}))
    password2 = forms.CharField(strip=False,widget=forms.PasswordInput(attrs={'placeholder': '********'}))
    def __init__(self, *args, **kwargs):
        super(crearForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

###VISTAS###
def index(request):
    return render(request, 'home.html', {})

def registro(request):
    if request.user.is_authenticated:
        return redirect('/')
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

def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        usuario = authenticate(request, username=request.POST['logRut'], password=request.POST['logPass'])
        if usuario is not None:
            auth_login(request, usuario)
            return redirect('/')
        else:
            messages.success(request, 'Ingreso incorrecto: Rut o contraseña incorrectos')
            return redirect('/login')
    return render(request, 'login.html', {})

@login_required(login_url='/')
def logout(request):
    auth_logout(request)
    return redirect('/login')