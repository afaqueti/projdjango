# Generated by Django 3.0.3 on 2020-03-03 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='apelido',
            field=models.CharField(max_length=15),
        ),
    ]
