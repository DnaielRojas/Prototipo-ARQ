###IMPORT ESCENCIALES (renders y redirecciones de htmls)###
from django.shortcuts import render, redirect

###IMPORT REGISTROS###
from django.contrib import messages

###IMPORT LOGIN###
from django.contrib.auth import authenticate, logout as auth_logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

###FORMULARIOS###
from espacioApp.forms import *

###FILTROS###
from espacioApp.filters import ResidenteFiltro

###models### 
from espacioApp.models import *

###VISTAS###
def index(request):
    return render(request, 'home.html', {})

def herramientas(request):
    return render(request, 'herramientas.html', {})

def registro(request):
    if request.user.is_authenticated:
        return redirect('/')
    formulario = CrearForm()
    if request.method == 'POST':
        formulario = CrearForm(request.POST)
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

@login_required(login_url='/')
def perfil(request):
    return render(request, 'perfil.html', {})

def mod_perfil_residente(request, rut):
    usu = Residente.objects.get(rut=rut)
    usu_form = ResidenteForm(instance=usu)
    return render(request,'modificar_perfil.html',{'usu_form':usu_form,'rut':usu.rut})

def mod_perfil_administrativo(request, rut):
    adm = Administrativo.objects.get(rut=rut)
    adm_form = AdministrativoForm(instance=adm)
    return render(request,'modificar_perfil_admin.html',{'adm_form':adm_form,'rut':adm.rut})

def editar_residente(request, rut):
    usu = Residente.objects.get(rut=rut)
    if request.method == "POST":
        form = ResidenteForm(request.POST, instance=usu)
        if form.is_valid():
            try:
                form.save()
            except:
                pass
    return render(request,'perfil.html')

def editar_admin(request, rut):
    adm = Administrativo.objects.get(rut=rut)
    if request.method == "POST":
        form = ResidenteForm(request.POST, instance=adm)
        if form.is_valid():
            try:
                form.save()
            except:
                pass
    return render(request,'perfil.html')

def mod_residente_admin(request, rut):
    res = Residente.objects.get(rut=rut)
    form = ModificarResidenteForm(instance=res)
    return render(request,'modificar_perfil.html',{'form':form,'resrut':res.rut})

def editar_residente_admin(request, rut):
    usu = Residente.objects.get(rut=rut)
    if request.method == "POST":
        form = ModificarResidenteForm(request.POST, instance=usu)
        if form.is_valid():
            try:
                form.save()
            except:
                pass
    
    form = FiltroResidenteForm()
    residentes = Residente.objects.all()

    filtro = ResidenteFiltro(request.GET, queryset=residentes)
    residentes  = filtro.qs
    return render(request,'administrar_usuarios.html',{'form':form,'residentes':residentes,'filtro':filtro})

def gestion_usuarios(request):
    form = FiltroResidenteForm()
    residentes = Residente.objects.all()

    filtro = ResidenteFiltro(request.GET, queryset=residentes)
    residentes  = filtro.qs
    return render(request,'administrar_usuarios.html',{'form':form,'residentes':residentes,'filtro':filtro})

def gastos_agregar(request):
    l_gastos = GastoComun.objects.all()
    if request.method == "POST":
        form = GastosForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/gastos_agregar')
            except:
                pass
    else:
        form = GastosForm()      
    return render(request,'agregar_gastos.html',{'form': form, 'gastos': l_gastos})