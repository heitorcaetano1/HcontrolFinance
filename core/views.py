from django.shortcuts import render, redirect
from .models import Contas, Investimentos, Renda
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.template import loader

from django.views.generic import TemplateView
from datetime import datetime
from django.db.models import Sum
from .forms import UsuarioForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


class Index(TemplateView):
    def get(self, request):
        return render(request, 'index.html')



class ContasView(TemplateView):
    def get(self, request):
        divida = Contas.objects.all()
        context = {
            'Contas': divida,
        }
        return render(request, 'contas.html', context)


def retorna_total_contas(request):
    total = Contas.objects.all().aggregate(Sum('valor'))['valor__sum']
    if request.method == 'GET':
        print(total)
        return JsonResponse({'total': total})


def retorna_renda(request):
    total = Renda.objects.all().aggregate(Sum('valor'))['valor__sum']
    if request.method == 'GET':
        print(total)
        return JsonResponse({'total': total})

def relatorio_dividas(request):
    x = Contas.objects.all()

    meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
    data = []
    labels = []
    cont = 0
    print(x)
    mes = datetime.now().month + 1
    ano = datetime.now().year
    for i in range(12):
        mes -= 1
        if mes == 0:
            mes = 12
            ano = 1
        y = sum([i.valor for i in x if i.data.month == mes and i.data.year == ano])
        labels.append(meses[mes-1])
        data.append(y)
        cont += 1
    data_json = {'data': data[::-1], 'labels': labels[::-1]}
    print(data_json)
    return JsonResponse(data_json)

def relatorio_renda(request):
    x = Renda.objects.all()
    meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
    data = []
    labels = []
    cont = 0
    print(x)
    mes = datetime.now().month + 1
    ano = datetime.now().year
    for i in range(12):
        mes -= 1
        if mes == 0:
            mes = 12
            ano = 1
        y = sum([i.valor for i in x if i.vencimento.month == mes and i.vencimento.year == ano])
        labels.append(meses[mes - 1])
        data.append(y)
        cont += 1
    data_json = {'data': data[::-1], 'labels': labels[::-1]}
    print(data_json)
    return JsonResponse(data_json)


def relatorio_investimentos(request):
    ativos = Investimentos.objects.all()
    valor_total = Investimentos.objects.all().aggregate(Sum('valor'))['valor__sum']
    print(valor_total)
    print(ativos)
    label = []
    data = []
    for ativo in ativos:
        label.append(ativo.nome_invest)
        data.append(ativo.valor * ativo.qtd)
        total = sum(data)
    x = list(zip(label, data))
    x.sort(key=lambda x: x[1], reverse=True)
    x = list(zip(*x))
    print(label)
    print(data)
    return JsonResponse({'label': x[0][:3], 'data': x[1][:3], 'total': total})



def investimentos(request):
    invest = Investimentos.objects.all()
    context = {
        'Invest': invest
    }
    return render(request, 'investimentos.html', context)


def cadastro_user(request):
    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':
            form = UsuarioForm(request.POST, request.FILES)
            if form.is_valid():

                form.save()

                messages.success(request, 'Usuário salvo com sucesso.')
                form = UsuarioForm()
            else:
                messages.error(request, 'Erro ao salvar usuário.')
        else:
            form = UsuarioForm()
        context = {
            'form': form
        }
        return render(request, 'cadastro.html', context)
    else:
        return redirect('index')


def error404(request, exceptions):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html: charset=utf8', status=404)


def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html: charset=utf8', status=500)
