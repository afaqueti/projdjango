from django.db import models

class Pessoa(models.Model):
    primeiro_nome = models.CharField(max_length=30)
    segundo_nome = models.CharField(max_length=30)
    idade = models.IntegerField()
    salario = models.DecimalField(max_digits=5, decimal_places=2)
    apelido = models.CharField(max_length=15)
    matricula = models.CharField(max_length=20)


