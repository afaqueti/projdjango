# Generated by Django 3.0.3 on 2020-03-06 04:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0008_auto_20200306_0047'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Endereco',
            new_name='Endereço',
        ),
        migrations.RenameField(
            model_name='endereço',
            old_name='caixa_postal',
            new_name='caixapostal',
        ),
    ]
