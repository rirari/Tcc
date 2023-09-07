from django.db import models

# Create your models here.

class Formas(models.Model):
    nome = models.CharField(max_length=150, verbose_name='Nome da forma de citar')
    descricao = models.TextField(verbose_name='Descrição')
    citacao = models.TextField(verbose_name='Citação')
    referencia = models.TextField(verbose_name='Referência')
    explicacao = models.TextField(verbose_name='Explicação')
    imagem = models.ImageField(upload_to = 'imagens')

    def __str__(self):
        return self.nome
    
class Funções(models.Model):
    nome = models.CharField(max_length=150, verbose_name='Nome da função de citar')
    descricao = models.TextField(verbose_name='Descrição')
    citacao = models.TextField(verbose_name='Citação')
    referencia = models.TextField(verbose_name='Referência')
    imagem = models.ImageField(upload_to = 'imagens')

    def __str__(self):
        return self.nome

class Plagio(models.Model):
    nome = models.CharField(max_length=150, verbose_name='Nome do tipo de plágio')
    descricao = models.TextField(verbose_name='Descrição')
    imagem = models.ImageField(upload_to = 'imagens')
