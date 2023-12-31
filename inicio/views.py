from typing import Any, Dict
from django.shortcuts import render, redirect
from inicio.forms import CrearAccionFormulario, CrearBonoFormulario, CrearFuturoFormulario, ModificarAccionFormulario, ModificarBonoFormulario, ModificarFuturoFormulario, BuscarEspeciesFormulario, CrearBlogFormulario, CrearBlogFormularioCBV, BuscarBlogFormulario, CrearBlogFormularioCBV, CrearBonoFormularioCBV, CrearAccionFormularioCBV, CrearFuturoFormularioCBV, ModificarBlogFormulario
from inicio.models import Bono, Accion, Futuro, Blog
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def inicio(request):
    return render(request, 'inicio/inicio.html')

def about(request):
    return render(request, 'inicio/about.html')



def listar_especies(request):

    formulario = BuscarEspeciesFormulario(request.GET)
    ticker_a_buscar = None
    if formulario.is_valid():
        ticker_a_buscar = formulario.cleaned_data['ticker']
        listado_de_bonos = Bono.objects.filter(ticker__icontains=ticker_a_buscar)
        listado_de_acciones = Accion.objects.filter(ticker__icontains=ticker_a_buscar)
        listado_de_futuros = Futuro.objects.filter(ticker__icontains=ticker_a_buscar)
    formulario = BuscarEspeciesFormulario()
    return render(request, 'inicio/listar_especies.html', {'formulario': formulario, 'Bonos': listado_de_bonos,
                                                           'Acciones': listado_de_acciones,'Futuros': listado_de_futuros})

###################

class ListarBlogs(LoginRequiredMixin, ListView):
    model = Blog
    template_name = "inicio/CBV/listar_blog_CBV.html"
    context_object_name = 'blogs'

    def get_queryset(self):
        formulario = BuscarBlogFormulario(self.request.GET)
        lista_blogs = []
        if formulario.is_valid():
            titulo_a_buscar = formulario.cleaned_data.get('titulo', '')
            subtitulo_a_buscar = formulario.cleaned_data.get('subtitulo', '')
            autor_a_buscar = formulario.cleaned_data.get('autor', '')

            if titulo_a_buscar:
                lista_blogs = Blog.objects.filter(titulo__icontains=titulo_a_buscar)
            if subtitulo_a_buscar:
                lista_blogs = Blog.objects.filter(subtitulo__icontains=subtitulo_a_buscar)
            if autor_a_buscar:
                lista_blogs = Blog.objects.filter(autor__icontains=autor_a_buscar)

            formulario = BuscarBlogFormulario()
            return lista_blogs

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['formulario'] = BuscarBlogFormulario()
        return contexto

##################

class CrearBlog(LoginRequiredMixin, CreateView):
    model = Blog
    form_class = CrearBlogFormularioCBV
    template_name = "inicio/CBV/crear_blog_CBV.html"
    success_url = reverse_lazy('inicio:listar_blogs_CBV')

    def form_valid(self, form):
        form.instance.imagen = self.request.FILES.get('imagen')
        return super().form_valid(form)

class CrearBono(LoginRequiredMixin, CreateView):
    model = Bono
    form_class = CrearBonoFormularioCBV
    template_name = "inicio/CBV/crear_bono_CBV.html"
    success_url = reverse_lazy('inicio:listar_especies')

class CrearAccion(LoginRequiredMixin, CreateView):
    model = Accion
    form_class = CrearAccionFormularioCBV
    template_name = "inicio/CBV/crear_accion_CBV.html"
    success_url = reverse_lazy('inicio:listar_especies')

class CrearFuturo(LoginRequiredMixin, CreateView):
    model = Futuro
    form_class = CrearFuturoFormularioCBV
    template_name = "inicio/CBV/crear_futuro_CBV.html"
    success_url = reverse_lazy('inicio:listar_especies')

###################

class DetalleBono(DetailView):
    model = Bono
    template_name = "inicio/CBV/detalle_Bono_CBV.html"

class DetalleAccion(DetailView):
    model = Accion
    template_name = "inicio/CBV/detalle_accion_CBV.html"

class DetalleFuturo(DetailView):
    model = Futuro
    template_name = "inicio/CBV/detalle_futuro_CBV.html"

class DetalleBlog(LoginRequiredMixin, DetailView):
    model = Blog
    template_name = "inicio/CBV/detalle_blog_CBV.html"

###################

class ModificarBono(LoginRequiredMixin, UpdateView):
    model = Bono
    fields = ['ticker', 'descripcion', 'cupon', 'emisor', 'fecha_emision', 'fecha_vencimiento']
    template_name = "inicio/CBV/modificar_Bono_CBV.html"
    success_url = reverse_lazy('inicio:listar_especies')

class ModificarAccion(LoginRequiredMixin, UpdateView):
    model = Accion
    fields = ['ticker', 'descripcion', 'empresa']
    template_name = "inicio/CBV/modificar_accion_CBV.html"
    success_url = reverse_lazy('inicio:listar_especies')

class ModificarFuturo(LoginRequiredMixin, UpdateView):
    model = Futuro
    fields = ['ticker', 'descripcion', 'fecha_vencimiento']
    template_name = "inicio/CBV/modificar_futuro_CBV.html"
    success_url = reverse_lazy('inicio:listar_especies')

class ModificarBlog(LoginRequiredMixin, UpdateView):
    model = Blog
    form_class = ModificarBlogFormulario
    template_name = "inicio/CBV/modificar_blog_CBV.html"
    success_url = reverse_lazy('inicio:listar_blogs_CBV')

###################

class EliminarAccion(LoginRequiredMixin, DeleteView):
    model = Accion
    template_name = "inicio/CBV/eliminar_accion_CBV.html"
    success_url = reverse_lazy('inicio:listar_especies')

class EliminarBono(LoginRequiredMixin, DeleteView):
    model = Bono
    template_name = "inicio/CBV/eliminar_Bono_CBV.html"
    success_url = reverse_lazy('inicio:listar_especies')

class EliminarFuturo(LoginRequiredMixin, DeleteView):
    model = Futuro
    template_name = "inicio/CBV/eliminar_futuro_CBV.html"
    success_url = reverse_lazy('inicio:listar_especies')

class EliminarBlog(LoginRequiredMixin, DeleteView):
    model = Blog
    template_name = "inicio/CBV/eliminar_blog_CBV.html"
    success_url = reverse_lazy('inicio:listar_blogs_CBV')


# ##################
# def crear_blog(request):
#     imagenblog = request.blog.imagenblog
#     mensaje = ''
#     if request.method == 'POST':
#         formulario = CrearBlogFormulario(request.POST, instance=request.blog)
#         if formulario.is_valid():
#             info = formulario.cleaned_data
#             blog = blog(titulo=info['titulo'], subtitulo=info['subtitulo'],
#                         autor=info['autor'], fecha_publicacion=info['fecha_publicacion'],
#                         cuerpo=info['cuerpo'])
#             blog.save()
#             imagen_blog = formulario.cleaned_data.get('imagen')
#             imagenblog.blog = imagen_blog
#             imagenblog.save()
#             formulario.save()
#             return redirect('inicio:listar_blogs_CBV')
#         else:
#             return render(request, 'inicio/crear_blog.html', {'formulario': formulario})

#     formulario = CrearBlogFormulario()
#     return render(request, 'inicio/crear_blog.html', {'formulario': formulario, 'mensaje': mensaje})


##################

# def listar_blogs(request):

#     formulario = BuscarBlogFormulario(request.GET)
#     lista_blogs = Blog.objects.all()

#     if formulario.is_valid():
#         titulo_a_buscar = formulario.cleaned_data.get('titulo', '')
#         subtitulo_a_buscar = formulario.cleaned_data.get('subtitulo', '')
#         autor_a_buscar = formulario.cleaned_data.get('autor', '')

#         if titulo_a_buscar:
#             lista_blogs = Blog.objects.filter(titulo__icontains=titulo_a_buscar)
#         if subtitulo_a_buscar:
#             lista_blogs = Blog.objects.filter(subtitulo__icontains=subtitulo_a_buscar)
#         if autor_a_buscar:
#             lista_blogs = Blog.objects.filter(autor__icontains=autor_a_buscar)

#     formulario = BuscarBlogFormulario()
#     return render(request, 'inicio/blogs.html', {'formulario': formulario, 'lista_blogs': lista_blogs})

# class ListarEspecies(ListView):
#     queryset = Bono.objects.all()
#     queryset = queryset.union(Accion.objects.all())
#     queryset = queryset.union(Futuro.objects.all())
#     template_name = "inicio/CBV/listar_especies_CBV.html"
#     context_object_name = 'especies'

# def crear_bono(request):
#     mensaje = ''
#     if request.method == 'POST':
#         formulario = CrearBonoFormulario(request.POST)
#         if formulario.is_valid():
#             info = formulario.cleaned_data
#             bono = Bono(ticker=info['ticker'], descripcion=info['descripcion'], cupon=info['cupon'],
#                         emisor=info['emisor'], fecha_emision=info['fecha_emision'],
#                         fecha_vencimiento=info['fecha_vencimiento'])
#             bono.save()
#             return redirect('inicio:listar_especies')
#         else:
#             return render(request, 'inicio/crear_bono.html', {'formulario': formulario})

#     formulario = CrearBonoFormulario()
#     return render(request, 'inicio/crear_bono.html', {'formulario': formulario, 'mensaje': mensaje})

# def crear_accion(request):

#     mensaje = ''
#     if request.method == 'POST':
#         formulario = CrearAccionFormulario(request.POST)
#         if formulario.is_valid():
#             info = formulario.cleaned_data
#             accion = Accion(ticker=info['ticker'], descripcion=info['descripcion'], empresa=info['empresa'])
#             accion.save()
#             return redirect('inicio:listar_especies')
#         else:
#             return render(request, 'inicio/crear_accion.html', {'formulario': formulario})

#     formulario = CrearAccionFormulario()
#     return render(request, 'inicio/crear_accion.html', {'formulario': formulario, 'mensaje': mensaje})


# def crear_futuro(request):

#     mensaje = ''
#     if request.method == 'POST':
#         formulario = CrearFuturoFormulario(request.POST)
#         if formulario.is_valid():
#             info = formulario.cleaned_data
#             futuro = Futuro(ticker=info['ticker'], descripcion=info['descripcion'], fecha_vencimiento=info['fecha_vencimiento'])
#             futuro.save()
#             return redirect('inicio:listar_especies')
#         else:
#             return render(request, 'inicio/crear_futuro.html', {'formulario': formulario})

#     formulario = CrearFuturoFormulario()
#     return render(request, 'inicio/crear_futuro.html', {'formulario': formulario, 'mensaje': mensaje})



# def eliminar_accion(request, accion_id):

#     accion = Accion.objects.get(id=accion_id)
#     accion.delete()

#     return redirect('inicio:listar_especies')


# def eliminar_bono(request, bono_id):

#     bono = Bono.objects.get(id=bono_id)
#     bono.delete()

#     return redirect('inicio:listar_especies')


# def eliminar_futuro(request, futuro_id):

#     futuro = Futuro.objects.get(id=futuro_id)
#     futuro.delete()

#     return redirect('inicio:listar_especies')

# def modificar_accion(request, accion_id):
#     accion_a_modificar = Accion.objects.get(id=accion_id)

#     if request.method == 'POST':
#         formulario = ModificarAccionFormulario(request.POST)
#         if formulario.is_valid():
#             info = formulario.cleaned_data
#             accion_a_modificar.ticker = info['ticker']
#             accion_a_modificar.descripcion = info['descripcion']
#             accion_a_modificar.empresa = info['empresa']
#             accion_a_modificar.save()
#             return redirect('inicio:listar_especies')
#         else:
#             return render(request, 'inicio/modificar_accion.html', {'formulario': formulario})

#     formulario = ModificarAccionFormulario(initial={'ticker': accion_a_modificar.ticker,
#                                                    'descripcion': accion_a_modificar.descripcion,
#                                                    'empresa': accion_a_modificar.empresa, })
#     return render(request, 'inicio/modificar_accion.html', {'formulario': formulario})

# def modificar_bono(request, bono_id):
#     bono_a_modificar = Bono.objects.get(id=bono_id)

#     if request.method == 'POST':
#         formulario = ModificarBonoFormulario(request.POST)
#         if formulario.is_valid():
#             info = formulario.cleaned_data
#             bono_a_modificar.ticker = info['ticker']
#             bono_a_modificar.descripcion = info['descripcion']
#             bono_a_modificar.cupon = info['cupon']
#             bono_a_modificar.emisor = info['emisor']
#             bono_a_modificar.fecha_emision = info['fecha_emision']
#             bono_a_modificar.fecha_vencimiento = ['fecha_vencimiento']

#             bono_a_modificar.save()
#             return redirect('inicio:listar_especies')
#         else:
#             return render(request, 'inicio/modificar_bono.html', {'formulario': formulario})

#     formulario = ModificarBonoFormulario(initial={'ticker': bono_a_modificar.ticker,
#                                                     'descripcion': bono_a_modificar.descripcion,
#                                                     'cupon': bono_a_modificar.cupon,
#                                                     'emisor': bono_a_modificar.emisor,
#                                                     'fecha_emision': bono_a_modificar.fecha_emision,
#                                                     'fecha_vencimiento': bono_a_modificar.fecha_vencimiento})
#     return render(request, 'inicio/modificar_bono.html', {'formulario': formulario})

# def modificar_futuro(request, futuro_id):
#     futuro_a_modificar = Futuro.objects.get(id=futuro_id)

#     if request.method == 'POST':
#         formulario = ModificarFuturoFormulario(request.POST)
#         if formulario.is_valid():
#             info = formulario.cleaned_data
#             futuro_a_modificar.ticker = info['ticker']
#             futuro_a_modificar.descripcion = info['descripcion']
#             futuro_a_modificar.fecha_vencimiento = info['fecha_vencimiento']
#             futuro_a_modificar.save()
#             return redirect('inicio:listar_especies')
#         else:
#             return render(request, 'inicio/modificar_futuro.html', {'formulario': formulario})

#     formulario = ModificarFuturoFormulario(initial={'ticker': futuro_a_modificar.ticker,
#                                                    'descripcion': futuro_a_modificar.descripcion,
#                                                    'fecha_vencimiento': futuro_a_modificar.fecha_vencimiento, })
#     return render(request, 'inicio/modificar_futuro.html', {'formulario': formulario})
