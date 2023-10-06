from django.contrib import admin
from .models import Lote


# Define una clase de administración personalizada para el modelo Lote
class LotesAdmin (admin.ModelAdmin):
    # Define los campos de solo lectura en la página de edición del administrador
    readonly_fields=('created_at', 'updated_at')

# Register your models here.
# Registra el modelo Lote con la configuración de administración personalizada
admin.site.register(Lote,LotesAdmin) 