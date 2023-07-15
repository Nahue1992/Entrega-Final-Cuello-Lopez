from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, MaxLengthValidator, MinLengthValidator
from ckeditor.fields import RichTextField

# Create your models here.

class Bono(models.Model):
    ticker = models.CharField(max_length=5, validators=[MaxLengthValidator(5), MinLengthValidator(5)])
    descripcion = models.CharField(max_length=30)
    cupon = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(100)])
    emisor = models.CharField(max_length=30)
    fecha_emision = models.DateField()
    fecha_vencimiento = models.DateField()

    def __str__(self):
        return f'BONO - Ticker: {self.ticker} - Descripción {self.descripcion}'

class Accion(models.Model):
    ticker = models.CharField(max_length=4)
    descripcion = models.CharField(max_length=30)
    empresa = models.CharField(max_length=20)

    def __str__(self):
        return f'ACCION - Ticker: {self.ticker} - Descripción {self.descripcion}'


class Futuro(models.Model):
    ticker = models.CharField(max_length=10, validators=[MaxLengthValidator(9), MinLengthValidator(9)])
    descripcion = models.CharField(max_length=30)
    fecha_vencimiento = models.DateField()

    def __str__(self):
        return f'FUTURO - Ticker: {self.ticker} - Descripción {self.descripcion}'

class Blog(models.Model):
    titulo = models.CharField(max_length=30)
    subtitulo = models.CharField(max_length=40)
    autor = models.CharField(max_length=20)
    fecha_publicacion = models.DateField()
    cuerpo = RichTextField(null=True)
    imagen = models.ImageField(upload_to='imagenes/', null=True, blank=True)

    def __str__(self):
        return f'Titulo: {self.titulo} - Autor: {self.autor}'

# class ImagenBlog(models.Model):
#     blog = models.OneToOneField(Blog, on_delete=models.CASCADE)
#     imagen = models.ImageField(upload_to='imagenes', null=True, blank=True)