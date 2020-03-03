from django.db import models
from django.contrib.auth.models import User

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Endereco(models.Model):
    bairro = models.CharField(max_length=100)
    pessoa = models.ForeignKey('Pessoa', on_delete=models.CASCADE)
    estado = models.ForeignKey('Estados', on_delete=models.CASCADE)
    municipio = models.ForeignKey('Municipios', on_delete=models.CASCADE)

    def __str__(self):
        return self.bairro


class Estados(models.Model):
    nome = models.CharField(max_length=50)
    sigla = models.CharField(max_length=2)

    def __str__(self):
        return self.nome

class Municipios(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome








