from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


# Create your models here.

class InfoExtra(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatares', null=True, blank=True)
    descripcion = RichTextField(null=True)
    pagina_web = models.CharField(max_length=50, null=True)

class Mensaje(models.Model):
    emisor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensajes_enviados')
    mensaje = RichTextField()
    receptor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensajes_recibidos')

    def __str__(self):
        return f'Mensaje ID: {self.id} - De: {self.emisor.username} - Para: {self.receptor.username}'