from django.forms import ModelForm
from .models import Pessoa

class Formpessoas(ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome','apelido','cargo','cpf','sexo','email']


class Formpessoa2(ModelForm):
    class Meta:
        model = Pessoa
        fields = ['cnpj','matricula','empresa','foto']