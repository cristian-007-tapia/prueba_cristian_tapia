# Generated by Django 3.1.1 on 2020-09-24 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lugar_venta_producto',
            fields=[
                ('id_lugar', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_lugar', models.CharField(max_length=60)),
                ('direccion', models.CharField(max_length=60)),
                ('departamento', models.CharField(max_length=60)),
                ('municipio', models.CharField(max_length=60)),
                ('barrio', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id_producto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=60)),
                ('marca', models.CharField(max_length=60)),
                ('lote', models.DecimalField(decimal_places=6, default=0, max_digits=18)),
                ('fecha_caducidad', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Precios_venta',
            fields=[
                ('id_precio', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad_presentacion', models.DecimalField(decimal_places=6, default=0, max_digits=18)),
                ('unidad_medida', models.CharField(max_length=60)),
                ('precio', models.DecimalField(decimal_places=6, default=0, max_digits=18)),
                ('id_Lugar_venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.lugar_venta_producto')),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.productos')),
            ],
        ),
    ]
