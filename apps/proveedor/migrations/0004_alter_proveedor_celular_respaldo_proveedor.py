# Generated by Django 5.0.2 on 2024-02-16 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proveedor', '0003_alter_proveedor_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='celular_respaldo_proveedor',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
