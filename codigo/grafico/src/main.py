from graficos import (grafico_linhas, grafico_barras, grafico_boxplot, salvar_analises, inicializacao)
from time import sleep

while True:
    try:
        print('\033[1;33mGERAÇÃO DE GRÁFICOS\033[m')
        print('[1] - Gráfico de Linhas')
        print('[2] - Gráfico de Barras')
        print('[3] - Gráfico de Dispersão')
        print('[4] - Todos')

        print('\n\033[1;33mOUTRAS OPÇÕES\033[m')
        print('[5] - Salvar todos os gráficos e análises')
        print('[6] - Fechar programa')
        menu = int(input('\n\033[1;31mEscolha uma opção: \033[m'))

        salvar = False
        dados = inicializacao()

        match menu:
            case 1:
                grafico_linhas(salvar, dados)
            case 2:
                grafico_barras(salvar, dados)
            case 3:
                grafico_boxplot(salvar, dados)
            case 4:
                grafico_linhas(salvar, dados)
                grafico_barras(salvar, dados)
                grafico_boxplot(salvar, dados)
            case 5:
                salvar = True
                grafico_linhas(salvar, dados)
                grafico_barras(salvar, dados)
                grafico_boxplot(salvar, dados)
                salvar_analises(dados)
                print('Todos os Gráficos e suas análises foram salvos com sucesso\n')
                sleep(3)
            case 6:
                break
            case _:
                print('Opção inválida! Escolha entre 1 e 6')
    except ValueError:
        print('Erro: Digite um número inteiro válido.')