# Generated by Django 5.0.2 on 2024-02-15 14:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('insumo', '0001_initial'),
        ('producto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id_inventario', models.AutoField(primary_key=True, serialize=False)),
                ('stock_inventario', models.IntegerField()),
                ('tipo_inventario', models.CharField(max_length=255)),
                ('estado', models.BooleanField(default=True)),
                ('id_insumo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='insumo.insumo')),
                ('id_producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='producto.producto')),
            ],
            options={
                'db_table': 'inventario',
            },
        ),
    ]
