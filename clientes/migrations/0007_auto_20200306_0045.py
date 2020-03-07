# Generated by Django 3.0.3 on 2020-03-06 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0006_auto_20200306_0036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='endereco',
            name='endereco_principal',
        ),
        migrations.AddField(
            model_name='endereco',
            name='endereço_principal',
            field=models.CharField(blank=True, choices=[('S', 'Sim'), ('N', 'Não')], max_length=1, null=True),
        ),
    ]
