from django.urls import path
from .views import Index, ContasView, investimentos, cadastro_user, retorna_total_contas, retorna_renda
from .views import relatorio_renda, relatorio_dividas, relatorio_investimentos




urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('contas', ContasView.as_view(), name='contas'),
    path('investimentos', investimentos, name='investimentos'),
    path('cadastro', cadastro_user, name='cadastro'),

    path('retorna_renda', retorna_renda, name='retorna_renda'),
    path('retorna_total_contas', retorna_total_contas, name='retorna_total_contas'),


    path('relatorio_dividas', relatorio_dividas, name='relatorio_dividas'),
    path('relatorio_investimentos', relatorio_investimentos, name='relatorio_investimentos'),
    path('relatorio_renda', relatorio_renda, name='relatorio_renda')
]
