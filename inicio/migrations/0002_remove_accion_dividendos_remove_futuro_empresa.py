# Generated by Django 4.2.2 on 2023-06-27 00:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accion',
            name='dividendos',
        ),
        migrations.RemoveField(
            model_name='futuro',
            name='Empresa',
        ),
    ]