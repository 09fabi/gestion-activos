# Generated by Django 4.2.7 on 2023-11-18 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_app', '0002_alter_activo_estado_activo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activo',
            name='ordenar_por',
            field=models.CharField(choices=[('fecha', 'Fecha'), ('activo', 'Activo')], max_length=50, null=True),
        ),
    ]
