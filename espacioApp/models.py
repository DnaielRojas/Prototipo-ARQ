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
        db_table = "anuncio"

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

class TipoReporte(models.Model):
    id_tipo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)

    class Meta:
        db_table = "tipo_reporte"

class Reporte(models.Model):
    id_reporte = models.AutoField(primary_key=True)
    mensaje = models.CharField(max_length=400)
    tipo_reporte = models.ForeignKey(TipoReporte, on_delete=models.CASCADE)
    residente_rut = models.ForeignKey(Residente, on_delete=models.CASCADE)

    class Meta:
        db_table = "reporte"

class Pago(models.Model):
    id_pago = models.AutoField(primary_key=True)
    total = models.IntegerField()
    fecha = models.DateField()

    class Meta:
        db_table = "pago"

class TipoEspacioComun(models.Model):
    id_tipo = models.CharField(max_length=5, primary_key=True)
    nombre = models.CharField(max_length=30)

    class Meta:
        db_table = "tipo_espacio_comun"

class EspacioComun(models.Model):
    id_espacio = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    id_tipo_espacio = models.ForeignKey(TipoEspacioComun, on_delete=models.CASCADE)

    class Meta:
        db_table = "espacio_comun"

class Reserva(models.Model):
    id_reserva = models.AutoField(primary_key=True)
    horario = models.DateTimeField()
    estado = models.BooleanField()
    id_espacio = models.ForeignKey(EspacioComun, on_delete=models.CASCADE)
    residente_rut = models.ForeignKey(Residente, on_delete=models.CASCADE)
    id_pago = models.ForeignKey(Pago, on_delete=models.CASCADE)

    class Meta:
        db_table = "reserva"

class Multa(models.Model):
    id_multa = models.AutoField(primary_key=True)
    valor = models.IntegerField()
    fecha_emision = models.DateField()
    estado= models.BooleanField()
    id_pago = models.ForeignKey(Pago, on_delete=models.CASCADE)
    residente_rut = models.ForeignKey(Residente, on_delete=models.CASCADE)

    class Meta:
        db_table = "multa"

class GastoComun(models.Model):
    id_gasto = models.AutoField(primary_key=True)
    valor = models.IntegerField()
    fecha_emision = models.DateField()
    fecha_vencimiento = models.DateField()
    estado = models.BooleanField()
    id_pago = models.ForeignKey(Pago, on_delete=models.CASCADE)
    residente_rut = models.ForeignKey(Residente, on_delete=models.CASCADE)

    class Meta:
        db_table = "gasto_comun"

class Observacion(models.Model):
    id_observacion = models.AutoField(primary_key=True)
    mensaje = models.CharField(max_length=400)
    id_gasto = models.ForeignKey(GastoComun, on_delete=models.CASCADE)
