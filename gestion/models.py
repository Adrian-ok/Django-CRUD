from django.db import models
from .choices import instrucciones
from datetime import datetime


class sector(models.Model):
    id_sector = models.AutoField(primary_key=True, unique=True)
    nom_sector = models.CharField(max_length=100, unique=True, blank=False, null=False)

    def formato(self):
        return "{}".format(self.nom_sector)

    def __str__(self):
        return self.formato()

    class Meta:
        verbose_name='sector'
        verbose_name_plural='sectores'
        db_table='sector'

class grup_sangre(models.Model):
    id_sangre = models.AutoField(primary_key=True, unique=True)
    sangre = models.CharField(unique=True, max_length=50)

    def formato(self):
        return "{}".format(self.sangre)

    def __str__(self):
        return self.formato()

    class Meta:
        verbose_name='grup_sangre'
        verbose_name_plural='grup_sangres'
        db_table='grup_sangre'

class localidad(models.Model):
    id_localidad = models.AutoField(primary_key=True, unique=True)
    localidad = models.CharField(unique=True, max_length=100)
    cp = models.CharField(max_length=50, unique=True)

    def formato(self):
        return "{}".format(self.localidad)

    def __str__(self):
        return self.formato()

    class Meta:
        verbose_name='localidad'
        verbose_name_plural='localidades'
        db_table='localidad'

class estado(models.Model):
    id_estado = models.AutoField(primary_key=True, unique=True)
    estado = models.CharField(max_length=50)

    def formato(self):
        return "{}".format(self.estado)

    def __str__(self):
        return self.formato()

    class Meta:
        verbose_name='estado_civil'
        verbose_name_plural='estados_civiles'
        db_table='estado_civil'

class persona(models.Model):
    nro_legajo = models.IntegerField( unique=True)
    apellido = models.CharField( max_length=100)
    nombre = models.CharField( max_length=100)
    dni = models.IntegerField( unique=True)
    fn = models.DateField()
    telefono = models.BigIntegerField(unique=True)
    direccion = models.CharField( max_length=100)
    localidad = models.ForeignKey('localidad', on_delete=models.CASCADE, null=True, blank=True)
    grup_sangre = models.ForeignKey('grup_sangre', on_delete=models.CASCADE, null=True, blank=True)
    estado_civil = models.ForeignKey('estado', on_delete=models.CASCADE,null=True, blank=True)
    cant_hijos = models.IntegerField(default=0)
    casa = models.BooleanField(default=False)
    instruccion = models.CharField(choices=instrucciones, default='S', max_length=100)
    titulo = models.CharField( max_length=100)
    fi = models.DateField()
    sector = models.ForeignKey('sector', on_delete=models.CASCADE, null=True, blank=True)
    renovacion = models.DateField()
    venc_libreta = models.DateField()
    recordar = models.IntegerField(default=15)
    lastupdate = models.DateTimeField(auto_now=True)
    
    
    





