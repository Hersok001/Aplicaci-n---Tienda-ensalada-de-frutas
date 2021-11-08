from django.contrib import admin
from . models import CategoriaPro,Producto #importante importar la ubicación de los models

# Register your models here.

#Registrar para que los atributos created y update sean solamente de lectura
class CategoriaProAdmin(admin.ModelAdmin):
    readonly_fields=("created","update")

class ProductoAdmin(admin.ModelAdmin):
    readonly_fields=("created","update")

#Registramos los modelos y las clases creadas arriba
admin.site.register(CategoriaPro,CategoriaProAdmin)    
admin.site.register(Producto,ProductoAdmin)

