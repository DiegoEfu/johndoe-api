from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length = 50)
    apellido = models.CharField(max_length = 50)
    tipo = models.CharField(max_length = 1)
    cedula = models.CharField(max_length = 9)
    genero = models.CharField(max_length = 1)

class Vehiculo(models.Model):
    dueno = models.ForeignKey(Persona, on_delete=models.CASCADE)
    placa = models.CharField(max_length=7, unique=True)
    marca = models.CharField(max_length=45)
    modelo = models.CharField(max_length=45)
    color = models.CharField(max_length=45)

class Mantenimiento(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    tipo = models.CharField(max_length = 1)
    estado = models.CharField(max_length = 1, default='P')
    resultados = models.TextField(null=True)