# Generated by Django 3.0.3 on 2020-03-03 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primeiro_nome', models.CharField(max_length=30)),
                ('segundo_nome', models.CharField(max_length=30)),
                ('idade', models.IntegerField()),
                ('salario', models.DecimalField(decimal_places=2, max_digits=5)),
                ('apelido', models.CharField(max_length=30)),
                ('matricula', models.CharField(max_length=30)),
            ],
        ),
    ]