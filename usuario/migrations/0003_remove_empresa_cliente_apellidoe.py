# Generated by Django 3.1.5 on 2021-02-03 00:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_auto_20210128_0953'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empresa_cliente',
            name='apellidoE',
        ),
    ]
