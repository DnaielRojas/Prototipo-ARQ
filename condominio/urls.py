"""condominio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from condominio import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='inicio'),
    path('registro/',views.registro),
    path('login/',views.login),
    path('logout/',views.logout),
    path('perfil/',views.perfil),
    path('mod_perfil_residente/<rut>/',views.mod_perfil_residente),
    path('mod_perfil_administrativo/<rut>/',views.mod_perfil_administrativo),
    path('editar_residente/<rut>/',views.editar_residente),
    path('editar_admin/<rut>/',views.editar_admin),
    path('herramientas/',views.herramientas),
    path('gestion_usuarios/',views.gestion_usuarios),
    path('mod_residente_admin/<rut>/',views.mod_residente_admin),
    path('editar_residente_admin/<rut>/',views.editar_residente_admin),
    path('gastos_agregar/', views.gastos_agregar),
    path('gastos/<rut>/', views.ver_gastos),
    path('eliminar_gasto/<id_gasto>/', views.eliminar_gasto),
    path('reportar/', views.reportar),
    path('ver_reportes/<rut>/', views.ver_reportes)
]
