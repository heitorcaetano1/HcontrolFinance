from django.db import models
import datetime

class Contas(models.Model):
    nome = models.CharField('Nome', max_length=100)
    valor = models.FloatField()
    parcelas = models.IntegerField('Numero de Parcelas')
    data = models.DateField('Data de Vencimento')

    def __str__(self):
        return f'{self.nome} {self.valor} {self.parcelas} {self.data}'



class Renda(models.Model):
    nome = models.CharField('Nome', max_length=100)
    valor = models.FloatField()
    descricao = models.CharField('Descrição', max_length=100)
    vencimento = models.DateField('Vencimento')

    def __str__(self) -> str:
        return f'{self.nome} {self.valor}'

class TipoInvest(models.Model):
    nome_tipo = models.CharField('Tipo', max_length=100)

    def __str__(self):
        return f'{self.nome_tipo}'

class Investimentos(models.Model):
    nome_invest = models.CharField('Investimento', max_length=100)
    tipo = models.ForeignKey('core.TipoInvest', verbose_name='Tipo', on_delete=models.CASCADE)
    valor = models.FloatField()
    data = models.DateField('Data do investiento')
    qtd = models.IntegerField('Quantidade')

    def __str__(self):
        return f'{self.nome_invest} {self.qtd} {self.valor}'
