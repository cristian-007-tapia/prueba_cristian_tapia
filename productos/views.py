from django.shortcuts import render
from rest_framework.views import APIView
from productos.models import Productos,Lugar_venta_producto,\
    Precios_venta
from productos.serializers import ProductosSerializer,\
    Lugar_venta_productoSerializer,Precios_ventaSerializers
from rest_framework import status
from rest_framework.response import Response
# Create your views here.

class ProductosView(APIView):

    def post(self, request):
        serializer = ProductosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        producto = Productos.objects.all()
        serializer = ProductosSerializer(producto, many=True)
        return Response(serializer.data)

    def delete(self, request):
        try:
            productos = Productos.objects.get(pk=request.query_params['id'])
        except Productos.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        productos.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request):
        try:
            productos = Productos.objects.get(pk=request.query_params['id'])
        except Productos.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND) 
        serializer = ProductosSerializer(productos, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

class Precios_ventaView(APIView):

    def post(self, request):
        serializer = Precios_ventaSerializers(data=request.data)
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save()
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        precios_venta = Precios_venta.objects.all()
        serializer = Precios_ventaSerializers(precios_venta, many=True)
        return Response(serializer.data)

    def delete(self, request):
        try:
            precios_venta = Precios_venta.objects.get(pk=request.query_params['id'])
        except Precios_venta.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        precios_venta.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request):
        try:
            precios_venta = Precios_venta.objects.get(pk=request.query_params['id'])
        except Precios_venta.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND) 
        serializer = Precios_ventaSerializers(precios_venta, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Lugar_venta_productoView(APIView):

    def post(self, request):
        serializer = Lugar_venta_productoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

   
    