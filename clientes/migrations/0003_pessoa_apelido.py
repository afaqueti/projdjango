# Generated by Django 3.0.3 on 2020-03-06 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_empresa_logotip'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='apelido',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
