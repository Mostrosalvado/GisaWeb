from django.contrib import admin
from .models import Empleado

# Register your models here.
titulo_admin="Administrador de proyectos Gisa s.a."
admin.site.site_header = titulo_admin
admin.site.site_title = titulo_admin
admin.site.index_title = ''

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'cargo','foto')  
    list_filter = ('cargo', 'fecha_de_contratacion' , )  # Filtros 
    search_fields = ('nombre', 'apellido')


admin.site.register(Empleado,EmpleadoAdmin) 