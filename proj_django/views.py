from django.http import HttpResponse


def hello(request):
    return HttpResponse("Ola mundo")


def articles(request, year):
    return HttpResponse('Ola mundo' + str(year))



def lerDoBanco(nome):
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


def fname(request, nome):
    res = lerDoBanco(nome)
    if res['idade'] > 0:
        return HttpResponse(str(res['nome']) + ' você tem ' + str(res['idade']))
    else:
        return HttpResponse('Pessoa não encontrada')
