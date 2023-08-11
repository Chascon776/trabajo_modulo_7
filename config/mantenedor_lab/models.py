from django.db import models
from django.core.validators import MinValueValidator
from datetime import datetime
# Create your models here.
class Laboratorio(models.Model):
    nombre_lab = models.CharField(verbose_name ='NOMBRE LABORATORIO',max_length=50)
    ciudad = models.CharField(verbose_name ='CIUDAD', max_length=50)
    pais = models.CharField(verbose_name ='PAIS', max_length=50)


    class Meta:
        db_table = 'Laboratorio'  # Cambiar el nombre de la tabla a minúsculas y guiones bajos
        ordering = ['id']
    
    def __str__(self):
        datos_laboratorio ="{} {} {} {}".format(self.id, self.nombre_lab, self.ciudad, self.pais)
        return datos_laboratorio




class DirectorGeneral(models.Model):
    nombre = models.CharField(verbose_name ='NOMBRE DIRECTOR', max_length=50)
    laboratorio = models.OneToOneField(Laboratorio, verbose_name ='LABORATORIO ASOCIADO', on_delete=models.CASCADE , related_name='directores_generales')
    especialidad = models.CharField(verbose_name ='ESPECIALIDAD', max_length=50)

    class Meta:
        db_table = 'Director General'
        ordering = ['id']
    
    def __str__(self):
        datos_director="{} {}".format(self.id, self.nombre, self.laboratorio,self.especialidad)
        return datos_director



class Producto(models.Model):
    nombre_producto = models.CharField(verbose_name ='NOMBRE PRODUCTO',max_length=50)
    f_fabricacion = models.DateField(verbose_name ='AÑO FABRICACION',blank=True, null=True, validators=[MinValueValidator(limit_value=datetime(2015, 1, 1).date())],
        error_messages={
            'invalid': 'La fecha debe ser posterior a 2015.',
            'min_value': 'La fecha debe ser posterior a 2015.',
        }                      
                                    )
    p_costo = models.DecimalField(verbose_name ='PRECIO COSTO',max_digits=10, decimal_places=2, blank=True, null=True)
    p_venta = models.DecimalField(verbose_name ='PRECIO VENTA',max_digits=10, decimal_places=2, blank=True, null=True)
    laboratorio_prod = models.ForeignKey(Laboratorio,verbose_name ='LABORATORIO FABRICACION',on_delete=models.CASCADE , related_name='producto_laboratorio')
    
    class Meta:
        db_table = 'Producto'
        ordering = ['id']
        
    def datos_producto(self):
        return 

    def __str__(self):
        campos =  "{} {} {} {} {}".format(self.nombre_producto, self.f_fabricacion, self.p_costo, self.p_venta, self.laboratorio_prod)
        return campos
    
    @property
    def solo_annio(self):
        return self.f_fabricacion.strftime('%Y')




    