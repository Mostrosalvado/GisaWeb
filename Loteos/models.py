from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator

# Create your models here.

# Define el modelo Lote
class Lote (models.Model):
        # Opciones para el estado del lote (Vendido o Disponible)
        ESTADO_CHOICES = (
        ('Vendido', 'Vendido'),
        ('Disponible', 'Disponible'),
    )
        # Campo de ID del lote (entero con validador)
        id_lote = models.IntegerField(
        primary_key=True,
        validators=[MaxValueValidator(limit_value=102)],
        verbose_name="id_lote"
    )
        # Campo de contenido (texto enriquecido)
        content=RichTextField (verbose_name="Contenido")
        # Campo de estado del lote (elección entre las opciones definidas)
        status = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='Disponible', verbose_name="Estado")
        # Campo de precio del lote (entero)
        price=models.IntegerField(verbose_name="Precio", default=0)
        # Campo de imagen del lote (se guarda en la carpeta 'loteos' dentro de la carpeta 'media')
        image= models.ImageField(default='Null' , verbose_name="Imagen",upload_to='loteos' )
        # Campo de usuario (clave foránea hacia el modelo User de Django)
        user = models.ForeignKey(User,editable=True, verbose_name="Usuario" , on_delete=models.CASCADE)
        # Campo booleano para indicar si el lote es público
        public= models.BooleanField(verbose_name="Publicado?")
        # Campos de fecha y hora de creación y edición automáticos
        created_at = models.DateTimeField(auto_now_add=True , verbose_name="Creado el")
        updated_at = models.DateTimeField(auto_now=True , verbose_name="Editado el")
        class Meta:
            verbose_name = 'Lote'
            verbose_name_plural = 'Lotes'
            ordering = ['-created_at']

        def __str__(self):
            return str(self.id_lote)