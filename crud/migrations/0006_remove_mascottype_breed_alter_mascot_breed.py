# Generated by Django 4.2.1 on 2023-06-26 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0005_vaccine_mascot_vaccine'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mascottype',
            name='breed',
        ),
        migrations.AlterField(
            model_name='mascot',
            name='breed',
            field=models.CharField(max_length=40, verbose_name='Raza de mascota'),
        ),
    ]
