# Generated by Django 5.0.2 on 2024-02-16 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_usuario_id_rol'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='no_documento_usuario',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterModelTable(
            name='usuario',
            table='usuario',
        ),
    ]
