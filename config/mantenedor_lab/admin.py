from django.contrib import admin
from .models import DirectorGeneral, Laboratorio, Producto

admin.site.site_header = 'nombre del sitio'
admin.site.index_title = 'nombre del subtitulo' 
admin.site.site_title = 'titulo pagina'



class Laboratorio_Admin(admin.ModelAdmin):
     # search_fields=['nombre'] //crea barra de busqueda     
    list_display = ('id','nombre_lab','ciudad','pais')

class D_general_Admin(admin.ModelAdmin):
     # search_fields=['nombre'] //crea barra de busqueda     
    list_display = ('id','nombre','laboratorio','especialidad')

class Productos_Admin(admin.ModelAdmin):
     # search_fields=['nombre'] //crea barra de busqueda     
    list_display = ('id','nombre_producto','laboratorio_prod','solo_annio','p_costo','p_venta')
    list_filter = ('nombre_producto','laboratorio_prod')

admin.site.register(DirectorGeneral,D_general_Admin )
admin.site.register(Laboratorio, Laboratorio_Admin)
admin.site.register(Producto, Productos_Admin)