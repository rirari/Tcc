# Generated by Django 4.2.4 on 2023-09-25 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citar', '0010_normas'),
    ]

    operations = [
        migrations.AddField(
            model_name='normas',
            name='explicacao2',
            field=models.TextField(default='', verbose_name='Explicação 2'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='normas',
            name='explicacao3',
            field=models.TextField(default=' ', verbose_name='Explicação'),
            preserve_default=False,
        ),
    ]