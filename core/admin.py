from django.contrib import admin
from .models import Contas, TipoInvest, Investimentos, Renda

class ContasAdmin(admin.ModelAdmin):
    list_display = ('nome', 'valor', 'parcelas')

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email')

class RendaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'valor', 'descricao', 'vencimento')

class TipoInvestAdmin(admin.ModelAdmin):
    list_display = ['nome_tipo']

class InvestimentosAdmin(admin.ModelAdmin):
    list_display = ('nome_invest', 'tipo', 'valor', 'data', 'qtd')


admin.site.register(Contas, ContasAdmin)
admin.site.register(Renda, RendaAdmin)
admin.site.register(TipoInvest, TipoInvestAdmin)
admin.site.register(Investimentos, InvestimentosAdmin)
