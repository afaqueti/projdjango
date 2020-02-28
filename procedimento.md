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


