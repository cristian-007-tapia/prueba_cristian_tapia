from rest_framework import serializers
from productos.models import Lugar_venta_producto,Precios_venta,Productos

class ProductosSerializer(serializers.ModelSerializer):
	class Meta:
		model = Productos
		fields = '__all__'

class Lugar_venta_productoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Lugar_venta_producto
		fields = '__all__'

class Precios_ventaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Precios_venta
        fields = '__all__'