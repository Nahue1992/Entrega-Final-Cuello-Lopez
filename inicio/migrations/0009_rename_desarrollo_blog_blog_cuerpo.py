# Generated by Django 4.2.2 on 2023-07-15 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0008_blog_desarrollo_blog_blog_fecha_publicacion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='desarrollo_blog',
            new_name='cuerpo',
        ),
    ]
