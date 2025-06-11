# Importando bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Carrega o dataset real do CSV
def inicializacao():
    dados = pd.read_csv('dados_simulados_main.csv', delimiter=';')
    dados['Timestamp'] = pd.to_datetime(dados['Timestamp'], unit='ms', origin='unix')
    dados['Grupo'] = (dados.index // 5) + 1
    return dados

# Gráfico 1: Linha (Temperatura e Umidade ao longo do tempo)
def grafico_linhas(salvar, dados):
    plt.figure(figsize=(10, 6))
    plt.plot(dados['Timestamp'], dados['Temperatura'], marker='o', linestyle='-', color='#1f77b4', label='Temperatura (°C)')
    plt.plot(dados['Timestamp'], dados['Umidade'], marker='s', linestyle='-', color='#ff7f0e', label='Umidade (%)')
    plt.title('Variação de Temperatura e Umidade')
    plt.xlabel('Horário')
    plt.ylabel('Valores')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    if salvar == False:
        plt.show()  # Exibir gráfico
    else:
        plt.savefig('grafico_linha_temperatura_umidade.png')
    plt.close()

# Gráfico 2: Barras (Média de Temperatura e Umidade por intervalo)
def grafico_barras(salvar, dados):
    medias_grupo = dados.groupby('Grupo')[['Temperatura', 'Umidade']].mean().reset_index()
    plt.figure(figsize=(10, 6))
    bar_width = 0.35
    plt.bar(medias_grupo['Grupo'] - bar_width/2, medias_grupo['Temperatura'], bar_width, color='#1f77b4', label='Temperatura (°C)')
    plt.bar(medias_grupo['Grupo'] + bar_width/2, medias_grupo['Umidade'], bar_width, color='#ff7f0e', label='Umidade (%)')
    plt.title('Média de Temperatura e Umidade')
    plt.xlabel('Grupo (5 leituras)')
    plt.ylabel('Valores')
    plt.grid(True, axis='y')
    plt.legend()
    plt.tight_layout()
    if salvar == False:
        plt.show()  # Exibir gráfico
    else:
        plt.savefig('grafico_barras_temperatura_umidade.png')
    plt.close()

# Gráfico 3: Boxplot (Distribuição de Temperatura e Umidade)
def grafico_boxplot(salvar, dados):
    plt.figure(figsize=(10, 6))
    plt.boxplot([dados['Temperatura'], dados['Umidade']], labels=['Temperatura (°C)', 'Umidade (%)'], patch_artist=True,
                boxprops=dict(facecolor='#1f77b4'), medianprops=dict(color='black'))
    plt.title('Distribuição de Temperatura e Umidade')
    plt.ylabel('Valores')
    plt.grid(True, axis='y')
    if salvar == False:
        plt.show()  # Exibir gráfico
    else:
        plt.savefig('grafico_boxplot_temperatura_umidade.png')
    plt.close()

def salvar_analises(dados):
    # Análise estatística (foco em Temperatura e Umidade)
    media_temp = dados['Temperatura'].mean()
    max_temp = dados['Temperatura'].max()
    min_temp = dados['Temperatura'].min()
    media_umid = dados['Umidade'].mean()
    max_umid = dados['Umidade'].max()
    min_umid = dados['Umidade'].min()

    # Salvando análise em texto
    with open('dados_salvos_texto.txt', 'w') as f:
        f.write(f'Temperatura - Média: {media_temp:.2f}°C, Máxima: {max_temp:.2f}°C, Mínima: {min_temp:.2f}°C\n')
        f.write(f'Umidade - Média: {media_umid:.2f}%, Máxima: {max_umid:.2f}%, Mínima: {min_umid:.2f}%\n')
        f.write(f'Mediana Temperatura: {media_temp:.2f}°C\n')
        f.write(f'Mediana Umidade: {media_umid:.2f}%\n')

    # Salvando dados em CSV
    dados.to_csv('dados_salvos_csv.csv', index=False)