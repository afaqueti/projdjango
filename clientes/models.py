from django.db import models


#Clientes
class Pessoa(models.Model):
    SEXO_CHOICES = (
        ("F", "Feminino"),
        ("M", "Masculino")
    )
    nome = models.CharField(max_length=100)
    apelido = models.CharField(max_length=30, null=True, blank=True)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, blank=True, null=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    cargo = models.ForeignKey('Cargo', on_delete=models.CASCADE)
    cpf = models.CharField(max_length=11,null=True,blank=True)
    cnpj = models.CharField(max_length=11, null=True, blank=True)
    matricula = models.CharField(max_length=10, null=True, blank=True)
    empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE, null=True)

    foto = models.ImageField(upload_to='fotos_clientes', null=True, blank=True)


    def __str__(self):
        return self.nome

#Clientes
class Endereço(models.Model):
    SEXO_CHOICES = (
        ("S", "Sim"),
        ("N", "Não")
    )
    pessoa = models.ForeignKey('Pessoa', on_delete=models.CASCADE)
    caixapostal = models.CharField(max_length=10)
    bairro = models.CharField(max_length=100)
    complemento = models.CharField(max_length=100)
    endereço_principal = models.CharField(max_length=1, choices=SEXO_CHOICES, blank=True, null=True)
    logradouro = models.CharField(max_length=100)
    estado = models.ForeignKey('Estado', on_delete=models.CASCADE)
    municipio = models.ForeignKey('Municipio', on_delete=models.CASCADE)
    observacoes = models.TextField(max_length=1000)


    def __str__(self):
        return self.bairro

#Clientes
class Estado(models.Model):
    nome = models.CharField(max_length=50)
    sigla = models.CharField(max_length=2)
    pais = models.ForeignKey('Paise' , on_delete=models.CASCADE)
    gentilico = models.CharField(max_length=20)

    def __str__(self):
        return self.sigla

#Clientes
class Municipio(models.Model):
    nome = models.CharField(max_length=100)
    estado = models.ForeignKey('Estado', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

#Clientes
class Paise(models.Model):
    nome = models.CharField(max_length=20)
    gentilico = models.CharField(max_length=60)
    sigla = models.CharField(max_length=5)

    def __str__(self):
        return self.nome

#Clientes
class Cargo(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

#Clientes
class Empresa(models.Model):
    nome = models.CharField(max_length=250)
    nome_fantasia = models.CharField(max_length=100)
    logotip = models.ImageField(upload_to='fotos_clientes', null=True, blank=True)

    def __str__(self):
        return self.nome






