from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name= models.CharField(max_length=100 , verbose_name="Nombre")
    description = models.CharField(max_length=255 , verbose_name="Descripción")
    created_at = models.DateTimeField(auto_now_add=True , verbose_name="Creado el")

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self): 
        return self.name
    
class Obra (models.Model):
        title=models.CharField(max_length=150 , verbose_name="Titulo")
        content=RichTextField (verbose_name="Contenido")
        image_1= models.ImageField(default='Null' , verbose_name="Imagen1",upload_to='obras' )
        image_2= models.ImageField(default='Null' , verbose_name="Imagen2",upload_to='obras' )
        image_3= models.ImageField(default='Null' , verbose_name="Imagen3",upload_to='obras' )
        user = models.ForeignKey(User,editable=True, verbose_name="Usuario" , on_delete=models.CASCADE)
        category = models.ManyToManyField(Category,verbose_name="Categorias",blank=True)
        public= models.BooleanField(verbose_name="Publicado?")
        created_at = models.DateTimeField(auto_now_add=True , verbose_name="Creado el")
        updated_at = models.DateTimeField(auto_now=True , verbose_name="Editado el")
        class Meta:
            verbose_name = 'Obra'
            verbose_name_plural = 'Obras'
            ordering = ['-created_at']

        def __str__(self):
            return self.title