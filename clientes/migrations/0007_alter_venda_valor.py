# Generated by Django 3.2.5 on 2021-08-22 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0006_auto_20180210_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venda',
            name='valor',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
