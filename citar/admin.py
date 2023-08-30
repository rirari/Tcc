from django.contrib import admin
from .models import Formas,Funções,Plagio

# Register your models here.

@admin.register(Formas)
class FormasAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'citacao','referencia','explicacao', 'imagem')

@admin.register(Funções)
class FunçõesAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao','citacao','referencia', 'imagem')

@admin.register(Plagio)
class PlagioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'imagem')
