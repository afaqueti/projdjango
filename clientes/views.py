from django.shortcuts import render

# Create your views here.
def pessoa_list(request):
    return render(request, 'pessoa.html')
