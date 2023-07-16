from django.urls import path
from usuario import views
from django.contrib.auth.views import LogoutView

app_name = 'usuario'

urlpatterns = [
    path('login/', views.login, name= 'login'),
    path('logout/', LogoutView.as_view(template_name= 'usuario/logout.html'), name= 'logout'),
    path('signup/', views.signup, name ='signup'),
    path('perfil/', views.perfil_usuario, name= 'perfil'),
    path('perfil/editar/', views.edicion_perfil, name ='editar_perfil'),
    path('perfil/editar/password/', views.ModificarPass.as_view(), name ='cambiar_pass'),


]
