Nome do projeto - proj_django
https://github.com/afaqueti/projdjango.git


Instalação do python
Devemos iniciar o procedimento de criar uma pasta do projeto: $ mkdir projeto

Dentro da pasta proj_django/ devemos acessar o seguinte comando para criar um arquivo venv pois essee arquivo delimitara a pasta virtual para gerar os arquivos do Django. 

$ python3 -m venv `myvenv` 

Com esse comando será criada uma pasta myvenv dentro do proj_django.
 `` Caso a venv não instale será necessário rodar o seguinte comando: 
` $ sudo apt-get install python3.6-venv
`
Para ativar a venv:

`faqueti@faqueti-Ale:~/Documentos/proj_django$ source myvenv/bin/activate
`
`(myvenv) faqueti@faqueti-Ale:~/Documentos/proj_django$
`
 Apos acessar maquina venv será necessário instalar o DJANGO

`(myvenv) faqueti@faqueti-Ale:~/Documentos$ pip install django` todos os pacotes foram instalados, caso tenha alguma duvida somente acessar o python com o seguinte comando.

`(myvenv) faqueti@faqueti-Ale:~/Documentos$ python3
`
django.version

(3, 0, 3, 'final', 0)

django-admin startproject projeto_django . O ponto no final irá criar somente uma pasta .

Configuração do time zone:

`Internationalization
 https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True`

rodando runserver

`$ python manager.py runserver`

Para acessar o admin/ é necessário rodar o seguinte comnando:

`$ python manage.py migrate
`
===========================================================================
Criando as urls
URL RESOLOTIPN - URLS.PY

Representa as devidas requições representa a porta das request. mandando para as devidas view.


para criar uma url será necessario acessar o arquivo  urls.py. vamos criar uma simples urls
dentro do arquivo informado.

`path('helo/', hello),
`

Após gerar o path dentro do arquivo urls.py devemos criar um arquivo chamdo viwes.py dentro projeto 
(proj_django) para que seja informada as devidas funções 

`def hello(request):
    pass`

Consequantemente devemos importar dentro da urls.py o arquivo wiews.py com o seguinte comando:

`from django.contrib import admin
`
`from django.urls import path
`
`from .views import hello
`
`urlpatterns = [
    path('helo/', hello),
    path('admin/', admin.site.urls),`

necessariamento tabém devemos usar a biblioteca HttpRespose

`from django.http import HttpRespose`

`def hello(request):
    num = 21
    if num > 20:
        return HttpResponse(num`)

===========================================================================
Funções

Dentro do fluxo as funções são as VIEWS:

Segue exemplo de função gerada dentro da VIEWS
Função gerada dentro de outra função:


`def lerDoBanco(nome):`

    lista_nome = [
        {'nome':'Nicolas', 'idade':10},
        {'nome':'Renata', 'idade':20},
        {'nome':'Alessandro', 'idade':30}
    ]

    for pessoa in lista_nome:
        if pessoa['nome'] == nome:
            #return HttpResponse(str(pessoa['nome']))
            return pessoa
    else:
        return {'nome': 'Nome não informado', 'idade': 0}

`def fname(request, nome):`

    res = lerDoBanco(nome)
    if res['idade'] > 0:
        return HttpResponse(str(res['nome']) + ' você tem ' + str(res['idade']))
    else:
        return HttpResponse('Pessoa não encontrada')
        

===========================================================================
Model

Model's são classe que descreve o modelo de negocio.

Para iniciar devemos gerar um APP, pois dentro do projeto podemos criar vairas
APP's para gerenciar nossos model's.

Para isso devemos criar uma APP de clientes. Lembrando que o nome cliente devido 
a aplicação ser para gestão de clientes.

`$ python manage.py startapp clientes
`

Com esse comando geramos a estrutura da nossa APP.

`from django.db import models
`

`class Person(models.Model):
    primeiro_nome = models.CharField(max_length=30)
    segundo_nome = models.CharField(max_length=30)
    idade = models.IntegerField()
    salario = models.DecimalField(max_digits=5, decimal_places=2)`
    
As classe são tratadas como as regras de negocio do cliente. Portanto esse são os campos gerados
para imputar os devidos registro dentro do banco de dados.

Para verificar as configuraçẽos de banco de dados devemos abrir o arquivo
"setings.py do proj_django".

Portanto para que uma APP seja registrada no banco de dados devemos informar na lista 
abaixo nas aplicações de definição.

`# Application definition
`

`INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'clientes',
]`

Apos executar o procedimento acima devemos rodar o seguinte comando:

`$ python manage.py makemigrations
`
Portanto o Django cria um arquivo dentro da pasta migrations:

`Migrations for 'clientes':
  clientes/migrations/0001_initial.py
    - Create model Person`

Portanto o comando para criar no banco de dados é o seguinte:

`$ python manage.py migrate`


`Operations to perform:
  Apply all migrations: admin, auth, clientes, contenttypes, sessions
Running migrations:
  Applying clientes.0001_initial... OK`
  
A partir desse momento o django criou os campos da classe na pasta 
cliente, consequentemente dentro do branco de dados SQlite3.

Para criar um novo campo conforme a classe gerada , será necessário adicionar
dentro do models o novo campo e consequentemente incluir no arquivo:
0001_initial.py.

class Pessoa(models.Model):

    primeiro_nome = models.CharField(max_length=30)
    segundo_nome = models.CharField(max_length=30)
    idade = models.IntegerField()
    salario = models.DecimalField(max_digits=5, decimal_places=2)
    apelido = models.CharField(max_length=15)
    matricula = models.CharField(max_length=20)


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




Após executar esse procedimento devemos rodar os comandos :

`python manage.py makemigrations`

Migrations for 'clientes':
  clientes/migrations/0003_auto_20200303_1257.py
    - Alter field matricula on pessoa

`$ python manage.py migrate
`
Operations to perform:
  Apply all migrations: admin, auth, clientes, contenttypes, sessions
Running migrations:
  Applying clientes.0003_auto_20200303_1257... OK

Pois o Django irá executar uma ação de incluir o campo em um arquivo e no outro
alterar.

Segue abaixo:
class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_auto_20200303_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='matricula',
            field=models.CharField(max_length=20),
        ),
    ]

