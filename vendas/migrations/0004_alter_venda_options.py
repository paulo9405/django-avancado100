# Generated by Django 3.2.5 on 2021-09-16 02:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0003_auto_20210827_1258'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='venda',
            options={'permissions': (('setar_nfe', 'Usuário pode alterar parametro NF-e'), ('permissão2', 'Permissão2'), ('permissão3', 'Permissão3'))},
        ),
    ]
