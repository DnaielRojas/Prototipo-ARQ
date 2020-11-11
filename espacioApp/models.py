from django.db import models

# Create your models here.
class Usuario(models.Model):
    rut = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido_pat = models.CharField(max_length=100)
    apellido_mat = models.CharField(max_length=100)
    mail = models.EmailField()

    class Meta:
        abstract = True

class TipoAdministrativo(models.Model):
    id_tipo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=25)

    class Meta:
        db_table = "tipo_administrativo"

class Administrativo(Usuario):
    tipo_administrativo = models.ForeignKey(TipoAdministrativo, on_delete=models.CASCADE)

    class Meta:
        db_table = "administrativo"

class Servicio(models.Model):
    id_servicio = models.CharField(max_length=4, primary_key=True)
    nombre = models.CharField(max_length=40)
    horario = models.DateField()
    administrativo_rut = models.ForeignKey(Administrativo, on_delete=models.CASCADE)

    class Meta:
        db_table = "servicio"

class Evento(models.Model):
    id_evento = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    fecha = models.DateField()
    descripcion = models.CharField(max_length=400)
    administrativo_rut = models.ForeignKey(Administrativo, on_delete=models.CASCADE)

    class Meta:
        db_table = "evento"

class Anuncio(models.Model):
    id_anuncio = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=40)
    fecha = models.DateField()
    descripcion = models.CharField(max_length=400)
    administrativo_rut = models.ForeignKey(Administrativo, on_delete=models.CASCADE)

    class Meta:
        db_table = "evento"

class Residente(Usuario):
    morosidad = models.BooleanField()
    habilitado = models.BooleanField()

    class Meta:
        db_table = "residente"

class Vivienda(models.Model):
    numero = models.IntegerField(primary_key=True)
    habitaciones = models.IntegerField()
    banos = models.IntegerField()
    disponible = models.BooleanField()
    residente_rut = models.ForeignKey(Residente, on_delete=models.CASCADE)

    class Meta:
        db_table = "vivienda"
