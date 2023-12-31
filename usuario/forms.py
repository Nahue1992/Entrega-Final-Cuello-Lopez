from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from ckeditor.fields import RichTextFormField
from usuario.models import Mensaje

class FormularioCreacionUsuario(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label= 'Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label= 'Repetir Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}


class FormularioEditarDatos(UserChangeForm):
    password = None
    email = forms.EmailField()
    first_name = forms.CharField(label= 'Nombre', max_length=20)
    last_name = forms.CharField(label= 'Apellido', max_length=20)
    avatar = forms.ImageField(required=False)
    descripcion = RichTextFormField(required=False)
    pagina_web = forms.CharField(max_length=50, required=False)

    class Meta:
        model= User
        fields = ['email', 'first_name', 'last_name']


class FormularioMensaje(forms.ModelForm):
    receptor = forms.ModelChoiceField(queryset=User.objects.all(), empty_label=None)

    class Meta:
        model = Mensaje
        fields = ['mensaje', 'receptor']
        labels = {
            'mensaje': 'Mensaje',
            'receptor': 'Receptor',
        }
        widgets = {
            'mensaje': forms.Textarea(attrs={'rows': 4}),
        }