from django.contrib import admin
from inicio.models import Blog, Bono, Accion, Futuro

# Register your models here.

admin.site.register(Blog)

@admin.register(Bono)
class BonoAdmin(admin.ModelAdmin):
    pass

@admin.register(Accion)
class AccionAdmin(admin.ModelAdmin):
    pass

@admin.register(Futuro)
class FuturoAdmin(admin.ModelAdmin):
    pass