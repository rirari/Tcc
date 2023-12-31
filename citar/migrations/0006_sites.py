# Generated by Django 3.2.20 on 2023-09-08 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citar', '0005_delete_integralidade'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, verbose_name='Nome do tipo de plágio')),
                ('descricao', models.TextField(verbose_name='Descrição')),
                ('imagem', models.ImageField(upload_to='imagens')),
                ('link', models.TextField()),
            ],
        ),
    ]
