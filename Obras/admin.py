from django.contrib import admin
from .models import Obra, Category



class CategoryAdmin (admin.ModelAdmin):
    readonly_fields=('created_at',)

class ObrasAdmin (admin.ModelAdmin):
    readonly_fields=('created_at', 'updated_at')

    def save_model(self,request,obj,form,change):
        if not obj.user_id:
            obj.user_id = request.user
        obj.save()

# Register your models here.
admin.site.register(Obra,ObrasAdmin) 
admin.site.register(Category,CategoryAdmin)
