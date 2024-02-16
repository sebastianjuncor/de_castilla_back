# Generated by Django 5.0.2 on 2024-02-16 00:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permiso', '0002_rename_description_permiso_permiso_descripcion_permiso'),
        ('rol', '0001_initial'),
        ('rol_has_permisos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rolhaspermiso',
            name='id_permiso',
        ),
        migrations.RemoveField(
            model_name='rolhaspermiso',
            name='id_rol',
        ),
        migrations.AddField(
            model_name='rolhaspermiso',
            name='id_permiso_fk',
            field=models.ForeignKey(blank=True, db_column='id_permiso_fk', null=True, on_delete=django.db.models.deletion.CASCADE, to='permiso.permiso'),
        ),
        migrations.AddField(
            model_name='rolhaspermiso',
            name='id_rol_fk',
            field=models.ForeignKey(blank=True, db_column='id_rol_fk', null=True, on_delete=django.db.models.deletion.CASCADE, to='rol.rol'),
        ),
    ]
