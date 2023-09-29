from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator

# Create your models here.

    
class Lote (models.Model):
        ESTADO_CHOICES = (
        ('Vendido', 'Vendido'),
        ('Disponible', 'Disponible'),
    )
        id_lote = models.IntegerField(
        primary_key=True,
        validators=[MaxValueValidator(limit_value=102)],
        verbose_name="id_lote"
    )
        content=RichTextField (verbose_name="Contenido")
        status = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='Disponible', verbose_name="Estado")
        price=models.IntegerField(verbose_name="Precio", default=0)
        image= models.ImageField(default='Null' , verbose_name="Imagen",upload_to='loteos' )
        user = models.ForeignKey(User,editable=True, verbose_name="Usuario" , on_delete=models.CASCADE)
        public= models.BooleanField(verbose_name="Publicado?")
        created_at = models.DateTimeField(auto_now_add=True , verbose_name="Creado el")
        updated_at = models.DateTimeField(auto_now=True , verbose_name="Editado el")
        class Meta:
            verbose_name = 'Lote'
            verbose_name_plural = 'Lotes'
            ordering = ['-created_at']

        def __str__(self):
            return str(self.id_lote)