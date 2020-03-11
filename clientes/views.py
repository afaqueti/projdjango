from django.shortcuts import render, redirect, get_object_or_404
from .models import Pessoa, Endereço
from .forms import Formpessoas, Formpessoa2


def pessoa_list(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'pessoa.html', {'pessoas': pessoas})

def endereco_list(request):
    enderecos = Endereço.objects.all()
    return render(request, 'pessoa.html', {'enderecos': enderecos})




def nova_pessoa(request):
    form = Formpessoas(request.POST or None, request.FILES or None)
    form2 = Formpessoa2(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('pessoa_list')

    if form2.is_valid():
        form2.save()
        return redirect('pessoa_list')
    return render(request, 'form_pessoa.html', {'form':form, 'form2':form2})



def update_pessoa(request, id):
    pessoa = get_object_or_404(Pessoa, pk=id)
    form = Formpessoas(request.POST or None, request.FILES or None, instance=pessoa)

    if form.is_valid():
        form.save()
        return redirect('pessoa_list')
    return render(request, 'form_pessoa.html', {'form': form})

def delete_pessoa(request, id):
    pessoa = get_object_or_404(Pessoa, pk=id)
    form = Formpessoas(request.POST or None, request.FILES or None, instance=pessoa)

    if request.method == 'POST':
        pessoa.delete()
        return redirect('pessoa_list')
    return render(request, 'delete_pessoa.html', {'form': form})




