# Generated by Django 3.2.5 on 2021-08-25 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0009_auto_20210823_1522'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venda',
            name='pessoa',
        ),
        migrations.DeleteModel(
            name='ItensDoPedido',
        ),
        migrations.DeleteModel(
            name='Produto',
        ),
        migrations.DeleteModel(
            name='Venda',
        ),
    ]
