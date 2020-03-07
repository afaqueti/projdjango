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

===========================================================================
Admin

Para acessar o admin é necessário acessar
http://127.0.0.1:8000/admin/

e consequentemente criar um usuário com o seguinte comando:

`$ python manage.py createsuperuser
`
Email adress: se necessário 
password : xxxxx
Confirma password : xxxx

Dentro do admin o Django possibilita o gerenciamento de todos os recurso de tabelas
e gestão de usuário que for necessário, inclusive a gestão de grupos de usuários

Será feito uma inclusão da tabela cliente atraves da Class no arquivo "admin.py"

Com oseguinte comando:
necessário importar o pacote da class pessoas:

`from .models import Pessoa
`

`admin.site.register(Pessoa)
`

Com esse procedimento já conseguimos visualizar os models dentro do admin.

`from django.db import models
`

`class Pessoa(models.Model):

    primeiro_nome = models.CharField(max_length=30)
    segundo_nome = models.CharField(max_length=30)
    idade = models.IntegerField()
    salario = models.DecimalField(max_digits=5, decimal_places=2)
    apelido = models.CharField(max_length=15)
    matricula = models.CharField(max_length=20)`

    def __str__(self):
        return self.primeiro_nome + ' ' + self.segundo_nome

===========================================================================
Templates

Os Templates servem para definir a forma de response na estrutura do django.
portanto devemos criar uma pasta com qualquer nome, pois para manter um padrão 
podemos gerar uma pasta chamada  "templates" dentro do nosso projeto.

Após criar uma pasta templates para geramos os arquivos .html
OBS: Criei a pasta em formato de pacote .py ( __init__.py)

executado os devidos procedimento vamos acessar os arquivos (urls.py), (views.py), (settings)

1- primeiro:

Arquivo - settings.py

    na linha DIRD:['templates'] informe a pasta que foi criada onde ficará os .html's
    
    TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]-


2 - Segundo:
    
Aquivo - views.py

from django.http import HttpResponse

from django.shortcuts import render

def indexpag(request):
    return render(request, 'index.html')

Esse metodo irá informar que existe uma função (def) que ira reinderizar o arquivo 
.hmtl que foi gerado dentro da pasta template, conforme informado anteriormente.


3 - Terceiro

Arquivo - urls.py


from django.contrib import admin

from django.urls import path

from .views import indexpag

from .views import fname,fname2


urlpatterns = {

    path('pessoa/<str:nome>', fname),
    path('admin/', admin.site.urls),
    path('index_pag/', indexpag),
    path('pessoa2/<str:nome>', fname2),

}


Dentro das urls vamos informar em qual função (def) se encontra nossa pagina .html
consequentemete, iremos acessar as devidas paginas.

OBS: devemos importar o pacote função (def) assim que gerar os devidos path.

Feito esse procedimento devemos acessar o seguinte link:

http://127.0.0.1:8000/index_pag/


4 -Quarto

Arquivo .HTML

Dentro do htmls podemos gerar algumas condições para definição de viwers na aplaicação.
Segue exemplo:


<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>

<h1>Bem vindo a pesquisa de idade!</h1>

<br>
    {{ v_nome }} você tem {{ v_idade }}

</br>

<h3>

    {% if v_idade >= 18 %}

        <b> Você pode tirar sua habilitação </b>

    {% else %}

            <b>Espere mais um pouco </b>

    {%endif%}
</h3>


</body>
</html>

Condição desenvolvida pela linguagem JINJA 



===========================================================================
Arquivos statics


O arquivo static trata dirtamente dos stilos do html, portanto a referencia será o CSS

inicialmente devemos criar uma pasta camada  "statics" pode ser o nome que quiser
dentro do projeto.

apó gerar a pasta devemos acessar o arquivo "settings.py" na linha:

Static files (CSS, JavaScript, Images)
https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    'clientes/statics',

Criar o STATICFILES conforme segue acima, consequentemente informa a pasta criada, 
pois a partir desse endereço que o django irá defenir o acesso ao stilo do css definido

apos gerar esse procedimento devomos acessar o .html para inserir o load static

{% load static %}
dentro do html

segue exemplo:

`{% load static %}
`

`link rel="stylesheet" href="{% static 'style.css' %}"
`

isso irá referenciar o caminho para o css.

OBS: esse procedimento irá funcionar conforme as definições imputadas nas views.


===========================================================================
Erros

Caso a porta do localhost informe que esta sendo usada pode rodar o seguinte comando

`sudo fuser -k 8000/tcp
`

Em caso do erro abaixo
'set' object is not reversible [duplicate]
segue a solução: Me de chaves {} para cochetes []

urlpatterns = [

    path('admin/', admin.site.urls),
    path('pessoa/<str:nome>', fname),
    path('index_pag/', indexpag),
    path('pessoa2/<str:nome>', fname2),

]


Django [Errno 13] Permission denied:

MEDIA_ROOT = os.path.join(BASE_DIR,'MEDIA')

===========================================================================
Arquivo de Media

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('pessoa/<str:nome>', fname),
    path('index_pag/', indexpag),
    path('pessoa2/<str:nome>', fname2),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

Importante dizer que esse metodo implatando não é um padrão , pois esse proceidmento 
server para o projeto em desenvolvimento.

O Django não funciona com um gerenciamento de media, portanto é necessário importar
os arquivos para um serviço melhor adptado para armazenamento de arquivos e medias

O django cuida somente de arquivos do python

===========================================================================
CRUD

C = Criar os objetos
R = Ler os objetos
U = Update os objetos
D = Deletar os objetos


Exportanto as URLS internas do projeto para a pasta padrão.

Primeiro precisamos criar uma pastas dentro do projeto raiz chamda 'urls.py'
segue exemplo:

`from django.urls import path
`

`from .views import pessoa_list
`

urlpatterns = [
    path('list/', pessoa_list ),

Executdo esse procedimento devemos acessar as urls do projeto 'proj_django'
e importar alguma pacotes

`from django.urls import path, include
`

`from clientes import urls as clientes_urls
`

criando a seguinte path:

`path('pessoa/', include(clientes_urls)),
`


abra a viwer.py do projeto raiz 'projdjango' e inclua a seguinte função:

`from django.shortcuts import render
`

def pessoa_list(request):
    return render(request, 'pessoa.html')
    
Pois esse função irá retornar a urls pessoa.html conforme as funções definidas.


