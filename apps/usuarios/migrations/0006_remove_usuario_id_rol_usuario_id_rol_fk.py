# Generated by Django 5.0.2 on 2024-02-16 01:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rol', '0001_initial'),
        ('usuarios', '0005_alter_usuario_no_documento_usuario_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='id_rol',
        ),
        migrations.AddField(
            model_name='usuario',
            name='id_rol_fk',
            field=models.ForeignKey(db_column='id_rol_fk', null=True, on_delete=django.db.models.deletion.SET_NULL, to='rol.rol'),
        ),
    ]
