# Generated by Django 4.2.7 on 2023-11-18 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_app', '0003_alter_activo_ordenar_por'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activo',
            name='estado_activo',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='activo',
            name='ordenar_por',
            field=models.CharField(default='dafault_value', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='activo',
            name='proyecto',
            field=models.CharField(max_length=50),
        ),
    ]
