
from django.conf.urls import include, url
from productos.views import ProductosView,Precios_ventaView,\
    Lugar_venta_productoView    


urlpatterns = [
    url(r'productos', ProductosView.as_view()),
    url(r'precios_venta', Precios_ventaView.as_view()),
    url(r'lugar_venta_producto', Lugar_venta_productoView.as_view())
    ]