# Generated by Django 4.2.1 on 2023-07-14 00:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0009_contact'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gender',
            options={'ordering': ['id'], 'verbose_name': 'genero', 'verbose_name_plural': 'generos'},
        ),
        migrations.AlterModelOptions(
            name='mascottype',
            options={'ordering': ['id'], 'verbose_name': 'tipo de mascota', 'verbose_name_plural': 'tipo de mascotas'},
        ),
    ]
