from django.db import models

# Create your models here.

class Especialidad(models.Model):
        descripcion = models.CharField(max_length=100)
 
        def __str__(self):
            return self.descripcion

class Medico(models.Model):
        rut = models.IntegerField()
        dVerificador = models.CharField(max_length=1)
        primerNombre = models.CharField(max_length=20)
        segundoNombre = models.CharField(max_length=20)
        primerApellido = models.CharField(max_length=20)
        segundoApellido = models.CharField(max_length=20)
        edad = models.IntegerField()
        direccion = models.CharField(max_length=100)
        sexo = models.CharField(max_length=10)
        telefono = models.IntegerField()
        fechaNacimiento = models.DateField()
        correo = models.CharField(max_length=70)
        tipoContrato = models.CharField(max_length=20)
        sueldo = models.IntegerField()
        sucursal = models.CharField(max_length=60)
        especialidad = models.ForeignKey(Especialidad, on_delete=models.PROTECT)

        def __str__(self):
            return self.primerNombre +" "+ self.primerApellido

class Paciente(models.Model):
        rut = models.IntegerField()
        dVerificador = models.CharField(max_length=1)
        primerNombre = models.CharField(max_length=20)
        segundoNombre = models.CharField(max_length=20)
        primerApellido = models.CharField(max_length=20)
        segundoApellido = models.CharField(max_length=20)
        edad = models.IntegerField()
        direccion = models.CharField(max_length=100)
        sexo = models.CharField(max_length=10)
        telefono = models.IntegerField()
        fechaNacimiento = models.DateField()
        correo = models.CharField(max_length=70)

        def __str__(self):
            return self.primerNombre +" "+ self.primerApellido

class Hora(models.Model):
        fecha = models.DateField()
        hora = models.DateTimeField()
        valor = models.IntegerField()
        paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT)
        medico = models.ForeignKey(Medico, on_delete=models.PROTECT)