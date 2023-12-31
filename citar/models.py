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
    nomePlagio = models.CharField(max_length=150, verbose_name='Nome do tipo de plágio')
    descricao = models.TextField(verbose_name='Descrição')
    imagem = models.ImageField(upload_to = 'imagens')

    def __str__(self):
        return self.nomePlagio

class Sites(models.Model):
    nome = models.CharField(max_length=150, verbose_name='Nome do site recomendado')
    descricao = models.TextField(verbose_name='Descrição')
    imagem = models.ImageField(upload_to = 'imagens')
    link = models.TextField(verbose_name='Link para acessar o site')

    def __str__(self):
        return
    
class Normas(models.Model):
    nome = models.CharField(max_length=150, verbose_name='Nome do sistema de chamada')
    explicacao = models.TextField(verbose_name='Explicação')
    explicacao2 = models.TextField(verbose_name='Explicação 2')
    explicacao3 = models.TextField(verbose_name='Explicação 3')
    imagem = models.ImageField(upload_to = 'imagens')

    def __str__(self):
        return self.nome
    
class Suporte(models.Model):
    nome = models.CharField(max_length=300, verbose_name='Nome completo')
    email = models.EmailField()
    mensagem = models.TextField(verbose_name='Mensagem')

    def __str__(self):
        return self.nome
    
# class Autores(models.Model):
#     nome = models.CharField(max_length=150, verbose_name='Nome do(a) autor(a) recomendado(a)')
#     descricao = models.TextField(verbose_name='Descrição')
#     imagem = models.ImageField(upload_to = 'imagens')
#     link = models.TextField(verbose_name='Link para acessar o material')

#     def __str__(self):
#         return self.nome

