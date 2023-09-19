from django.contrib import admin
from .models import Formas,Funções,Plagio,Sites, Normas

# Register your models here.

@admin.register(Formas)
class FormasAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'citacao','referencia','explicacao', 'imagem')

@admin.register(Funções)
class FunçõesAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao','citacao','referencia', 'imagem')

@admin.register(Plagio)
class PlagioAdmin(admin.ModelAdmin):
    list_display = ('nomePlagio', 'descricao', 'imagem')

@admin.register(Sites)
class SitesAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'imagem', 'link')

@admin.register(Normas)
class NormasAdmin(admin.ModelAdmin):
    list_display = ('nome', 'explicacao', 'imagem',)

# @admin.register(Autores)
# class AutoresAdmin(admin.ModelAdmin):
#     list_display = ('nome', 'descricao', 'imagem', 'link')

