# Generated by Django 4.2.7 on 2023-11-18 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_app', '0005_customuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='genero',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], default='O', max_length=1),
        ),
    ]
