# Generated by Django 5.0.2 on 2024-02-15 14:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('estado_oc', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrdenCompra',
            fields=[
                ('id_oc', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_oc', models.DateField()),
                ('hora_oc', models.TimeField()),
                ('id_estado_oc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estado_oc.estadooc')),
            ],
            options={
                'db_table': 'orden_compra',
            },
        ),
    ]
