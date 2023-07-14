from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator, MaxLengthValidator, MinLengthValidator
from inicio.models import Blog, Bono, Futuro, Accion

class BonoFormularioBase(forms.Form):
    ticker = forms.CharField(max_length=5, validators=[MaxLengthValidator(5), MinLengthValidator(5)])
    descripcion = forms.CharField(max_length=30, required=False)
    cupon = forms.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(100)])
    emisor = forms.CharField(max_length=30)
    fecha_emision = forms.DateField()
    fecha_vencimiento = forms.DateField()


class CrearBonoFormulario(BonoFormularioBase):
    ...

class ModificarBonoFormulario(BonoFormularioBase):
    ...

class AccionFormularioBase(forms.Form):
    ticker = forms.CharField(max_length=4)
    descripcion = forms.CharField(max_length=30, required=False)
    empresa = forms.CharField(max_length=20)

class CrearAccionFormulario(AccionFormularioBase):
    ...

class ModificarAccionFormulario(AccionFormularioBase):
    ...

class FuturoFormularioBase(forms.Form):
    ticker = forms.CharField(max_length=9, validators=[MaxLengthValidator(9), MinLengthValidator(9)])
    descripcion = forms.CharField(max_length=30)
    fecha_vencimiento = forms.DateField()

class CrearFuturoFormulario(FuturoFormularioBase):
    ...

class ModificarFuturoFormulario(FuturoFormularioBase):
    ...

class BuscarEspeciesFormulario(forms.Form):
    ticker = forms.CharField(required=False)


class BuscarBlogFormulario(forms.Form):
    titulo = forms.CharField(max_length=30, required=False)
    subtitulo = forms.CharField(max_length=40, required=False)
    autor = forms.CharField(max_length=20, required=False)

class CrearBlogFormulario(forms.Form):
    titulo = forms.CharField(max_length=30)
    subtitulo = forms.CharField(max_length=40)
    # cuerpo = forms.CharField()
    autor = forms.CharField(max_length=20)
    # fecha_publicacion = forms.DateField()
    # imagen = forms.CharField()


class CrearBlogFormularioCBV(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'

class CrearBonoFormularioCBV(forms.ModelForm):
    class Meta:
        model = Bono
        fields = '__all__'

class CrearAccionFormularioCBV(forms.ModelForm):
    class Meta:
        model = Accion
        fields = '__all__'

class CrearFuturoFormularioCBV(forms.ModelForm):
    class Meta:
        model = Futuro
        fields = '__all__'