from django.urls import path
from inicio import views

app_name = 'inicio'

urlpatterns = [
    path('', views.inicio, name= 'inicio'),
    path('about/', views.about, name= 'about'),
    path('especies/', views.listar_especies, name= 'listar_especies'),

    # path('IC_Blogs/', views.listar_blogs, name= 'blogs'),
    # path('IC_Blogs/crear/', views.crear_blog, name= 'crear_blog'),
    # path('bonos/crear/', views.crear_bono, name= 'crear_bono'),
    # path('acciones/crear/', views.crear_accion, name= 'crear_accion'),
    # path('futuros/crear/', views.crear_futuro, name= 'crear_futuro'),
    # path('bonos/eliminar/<int:bono_id>', views.eliminar_bono, name= 'eliminar_bono'),
    # path('bonos/modificar/<int:bono_id>', views.modificar_bono, name= 'modificar_bono'),
    # path('acciones/modificar/<int:accion_id>', views.modificar_accion, name= 'modificar_accion'),
    # path('acciones/eliminar/<int:accion_id>', views.eliminar_accion, name= 'eliminar_accion'),
    # path('futuros/modificar/<int:futuro_id>', views.modificar_futuro, name= 'modificar_futuro'),
    # path('futuros/eliminar/<int:futuro_id>', views.eliminar_futuro, name= 'eliminar_futuro'),

    # CBV

    # path('especiesCBV/', views.ListarEspecies.as_view(), name= 'listar_especies_CBV'),

    path('IC_Blogs/crearCBV', views.CrearBlog.as_view(), name= 'crear_blog_CBV'),
    path('IC_Blogs/<int:pk>/', views.DetalleBlog.as_view(), name= 'detalle_blog'),
    path('IC_Blogs/<int:pk>/modificar/', views.ModificarBlog.as_view(), name= 'modificar_blog'),
    path('IC_Blogs/<int:pk>/eliminar/', views.EliminarBlog.as_view(), name= 'eliminar_blog'),
    path('IC_Blogs/', views.ListarBlogs.as_view(), name= 'listar_blogs_CBV'),
    path('bonos/crearCBV', views.CrearBono.as_view(), name= 'crear_bono_CBV'),
    path('bonos/<int:pk>/', views.DetalleBono.as_view(), name= 'detalle_bono'),
    path('bonos/<int:pk>/modificar/', views.ModificarBono.as_view(), name= 'modificar_bono'),
    path('bonos/<int:pk>/eliminar/', views.EliminarBono.as_view(), name= 'eliminar_bono'),
    path('acciones/crearCBV', views.CrearAccion.as_view(), name= 'crear_accion_CBV'),
    path('acciones/<int:pk>/', views.DetalleAccion.as_view(), name= 'detalle_accion'),
    path('acciones/<int:pk>/modificar/', views.ModificarAccion.as_view(), name= 'modificar_accion'),
    path('acciones/<int:pk>/eliminar/', views.EliminarAccion.as_view(), name= 'eliminar_accion'),
    path('futuros/crearCBV', views.CrearFuturo.as_view(), name= 'crear_futuro_CBV'),
    path('futuros/<int:pk>/', views.DetalleFuturo.as_view(), name= 'detalle_futuro'),
    path('futuros/<int:pk>/modificar/', views.ModificarFuturo.as_view(), name= 'modificar_futuro'),
    path('futuros/<int:pk>/eliminar/', views.EliminarFuturo.as_view(), name= 'eliminar_futuro'),

]

