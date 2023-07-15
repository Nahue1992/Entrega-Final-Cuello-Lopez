# Generated by Django 4.2.2 on 2023-07-15 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0013_remove_blog_imagen_infoextrablog'),
    ]

    operations = [
        migrations.RenameField(
            model_name='infoextrablog',
            old_name='user',
            new_name='blog',
        ),
        migrations.AlterField(
            model_name='infoextrablog',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='imagen_blog'),
        ),
    ]
