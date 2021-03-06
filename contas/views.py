from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
from .models import Transacao
from .form import TransacaoForm



def index(request):
    data = {}
    data['transacoes'] = ['t1', 't2', 't3']

    data['now'] = datetime.datetime.now()

    return render(request, 'index.html', data)




def listagem(request):
    data = {}
    data['transacoes'] = Transacao.objects.all()
    return render(request, 'listagem.html', data)



def nova_transacao(request):
    data = {}
    form = TransacaoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listagem')

    data['form'] = form
    return render(request, 'form.html', data)



def update(request, pk):
    data = {}
    transacao = Transacao.objects.get(pk=pk)
    form = TransacaoForm(request.POST or None, instance=transacao)

    if form.is_valid():
        form.save()
        return redirect('listagem')

    data['form'] = form
    data['transacao'] = transacao
    return render(request, 'form.html', data)



def delete(request, pk):
    transacao = Transacao.objects.get(pk=pk)
    transacao.delete()
    return redirect('listagem')

