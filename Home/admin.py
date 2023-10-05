from django.contrib import admin
from .models import Empleado,Maquina

# Register your models here.
titulo_admin="Administrador de proyectos Gisa s.a."
# Configuración personalizada del panel de administración
admin.site.site_header = titulo_admin # Encabezado del sitio de administración
admin.site.site_title = titulo_admin # Título de la página de administración
admin.site.index_title = '' # Título de la página de inicio del sitio de administración

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'cargo','foto')  
    list_filter = ('cargo', 'fecha_de_contratacion' , )  # Filtros 
    search_fields = ('nombre', 'apellido')

class MaquinaAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'marca', 'modelo','es_propia','patente','fecha_ultimo_mantenimiento','estado_mantenimiento','fecha_vencimiento_seguro')  
    list_filter = ('tipo', 'marca')  # Filtros 
    search_fields = ('tipo', 'marca', 'modelo')

# Registro de los modelos con sus respectivas configuraciones personalizadas
admin.site.register(Empleado,EmpleadoAdmin) 
admin.site.register(Maquina,MaquinaAdmin) 