from django.db import models

# Create your models here.
class Productos(models.Model):
    id_producto= models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=60, blank=False, null=False)
    marca = models.CharField(max_length=60, blank=False, null=False)
    lote = models.DecimalField(max_digits=18,decimal_places=6, default=0)
    fecha_caducidad = models.DateField(blank=True, null=True)
	
class Lugar_venta_producto(models.Model):
    id_lugar= models.AutoField(primary_key=True)
    nombre_lugar= models.CharField(max_length=60, blank=False, null=False)
    direccion = models.CharField(max_length=60, blank=False, null=False)
    departamento = models.CharField(max_length=60, blank=False, null=False)
    municipio = models.CharField(max_length=60, blank=False, null=False)
    barrio = models.CharField(max_length=60, blank=False, null=False)

class Precios_venta(models.Model):
    id_precio= models.AutoField(primary_key=True)
    id_lugar = models.ForeignKey(Lugar_venta_producto, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    cantidad_presentacion = models.DecimalField(max_digits=18,decimal_places=6,default=0)
    unidad_medida = models.CharField(max_length=60, blank=False, null=False)
    precio = models.DecimalField(max_digits=18,decimal_places=6, default=0)