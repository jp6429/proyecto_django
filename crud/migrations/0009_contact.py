# Generated by Django 4.2.1 on 2023-06-28 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0008_gender_alter_mascottype_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=12)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('comentario', models.TextField(max_length=120)),
            ],
            options={
                'verbose_name': 'contacto',
                'verbose_name_plural': 'contactos',
                'ordering': ['nombre', 'apellido'],
            },
        ),
    ]