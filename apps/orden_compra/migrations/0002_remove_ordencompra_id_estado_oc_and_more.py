# Generated by Django 5.0.2 on 2024-02-16 01:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estado_oc', '0001_initial'),
        ('orden_compra', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordencompra',
            name='id_estado_oc',
        ),
        migrations.AddField(
            model_name='ordencompra',
            name='id_estado_oc_fk',
            field=models.ForeignKey(blank=True, db_column='id_estado_oc_fk', null=True, on_delete=django.db.models.deletion.CASCADE, to='estado_oc.estadooc'),
        ),
    ]
