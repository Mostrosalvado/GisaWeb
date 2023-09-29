from django.db import models

# Create your models here.
from django.db import models

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_de_nacimiento = models.DateField()
    correo_electronico = models.EmailField()
    numero_telefono = models.CharField(max_length=15)
    direccion = models.TextField()
    fecha_de_contratacion = models.DateField()
    foto = models.ImageField(upload_to='empleados/', blank=True, null=True)
    cargo = models.CharField(max_length=50, blank=True, null=True)
    salario = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    class Meta:
            verbose_name = 'Empleadx'
            verbose_name_plural = 'Empleadxs'
            ordering = ['-fecha_de_contratacion']

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    

from django.db import models

class Maquina(models.Model):
    # Información básica
    tipo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    es_propia = models.BooleanField(default=True)
    patente = models.CharField(max_length=20, blank=True, null=True)
    fecha_ultimo_mantenimiento = models.DateField(blank=True, null=True)
    estado_mantenimiento = models.CharField(max_length=50, choices=[('Operativo', 'Operativo'), ('Mantenimiento', 'Mantenimiento'), ('Fuera de Servicio', 'Fuera de Servicio')], default='Operativo')
    fecha_vencimiento_seguro = models.DateField()

    def __str__(self):
        return self.tipo




