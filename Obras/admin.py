from django.contrib import admin
from .models import Obra, Category


# Define una clase de administración personalizada para el modelo Category
class CategoryAdmin (admin.ModelAdmin):
    # Hace que el campo "created_at" sea de solo lectura en el formulario de administración
    readonly_fields=('created_at',)

# Define una clase de administración personalizada para el modelo Obra
class ObrasAdmin (admin.ModelAdmin):
    # Hace que los campos "created_at" y "updated_at" sean de solo lectura en el formulario de administración
    readonly_fields=('created_at', 'updated_at')
    list_filter = ('category',)   # Agrega filtros para facilitar la búsqueda de obras por categoría en el administrador
    # Agrega la capacidad de buscar obras por título en el administrador
    search_fields = ('title', )

    # Este método se llama al guardar un objeto de obra en el administrador
    def save_model(self,request,obj):
        # Si no se ha establecido el campo "user_id" en el objeto, lo completa automáticamente con el usuario actual
        if not obj.user_id:
            obj.user_id = request.user
        # Guarda el objeto en la base de datos
        obj.save()

# Register your models here.
admin.site.register(Obra,ObrasAdmin) # Registra el modelo Obra con la clase ObrasAdmin
admin.site.register(Category,CategoryAdmin) # Registra el modelo Category con la clase CategoryAdmin
