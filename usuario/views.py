from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views import View
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from usuario.forms import FormularioCreacionUsuario, FormularioEditarDatos, FormularioMensaje
from usuario.models import InfoExtra, Mensaje



# Create your views here.

def iniciar_sesion(request):

    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data['username']
            contrasenia = formulario.cleaned_data['password']

            user = authenticate(username=usuario, password=contrasenia)

            django_login(request, user)

            InfoExtra.objects.get_or_create(user=user)

            return redirect('inicio:inicio')
        else:
            return render(request, 'usuario/login.html', {'formulario': formulario})


    formulario = AuthenticationForm()
    return render(request, 'usuario/login.html', {'formulario': formulario})

def registrarse(request):

    if request.method == ('POST'):
        formulario = FormularioCreacionUsuario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('usuario:login')
        else:
            return render(request, 'usuario/signup.html', {'formulario': formulario})

    formulario = FormularioCreacionUsuario()
    return render(request, 'usuario/signup.html', {'formulario': formulario})

@login_required
def edicion_perfil(request):
    info_extra_user = request.user.infoextra
    if request.method == 'POST':
        formulario = FormularioEditarDatos(request.POST, request.FILES, instance=request.user)
        if formulario.is_valid():

            avatar = formulario.cleaned_data.get('avatar')
            descripcion = formulario.cleaned_data.get('descripcion')
            pagina_web = formulario.cleaned_data.get('pagina_web')
            if avatar:
                info_extra_user.avatar = avatar
                info_extra_user.descripcion = descripcion
                info_extra_user.pagina_web = pagina_web
                info_extra_user.save()

            formulario.save()
            return redirect('inicio:inicio')
    else:
        formulario = FormularioEditarDatos(initial= {'avatar': request.user.infoextra.avatar},
                                           instance=request.user)
    return render(request, 'usuario/edicion_perfil.html', {'formulario': formulario})


class ModificarPass(LoginRequiredMixin, PasswordChangeView):
    template_name = 'usuario/edicion_pass.html'
    success_url = reverse_lazy('usuario:editar_perfil')


def perfil_usuario(request):
    usuario = request.user
    nombre = usuario.first_name
    apellido = usuario.last_name
    email = usuario.email

    contexto = {
        'nombre': nombre,
        'apellido': apellido,
        'email': email
    }

    return render(request, 'usuario/perfil.html', contexto)


class EnviarMensajeView(LoginRequiredMixin, View):
    def get(self, request):
        form = FormularioMensaje()
        return render(request, 'usuario/enviar_mensaje.html', {'form': form})

    def post(self, request):
        form = FormularioMensaje(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.emisor = request.user
            mensaje.save()
            return redirect('usuario:leer_mensajes')
        return render(request, 'usuario/enviar_mensaje.html', {'form': form})

@ login_required
def leer_mensajes(request):
    mensajes = Mensaje.objects.filter(receptor=request.user)
    return render(request, 'usuario/leer_mensajes.html', {'mensajes': mensajes})