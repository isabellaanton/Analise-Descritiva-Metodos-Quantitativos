# 1. Carregamento de Bibliotecas e Configuração Visual
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from scipy import stats
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 120)
# Paleta de cores e estilo visual
CAT_COLORS = ['#2a78d6', '#eb6834', '#1baf7a', '#eda100',
 '#e87ba4', '#008300', '#4a3aa7', '#e34948']
SEQ_BLUE = '#2a78d6'
GRID_COLOR = '#e1e0d9'
AXIS_COLOR = '#c3c2b7'
TEXT_MUTED = '#898781'
TEXT_PRIMARY = '#0b0b0b'
plt.rcParams.update({
 'figure.facecolor': '#fcfcfb',
 'axes.facecolor': '#fcfcfb',
 'axes.edgecolor': AXIS_COLOR,
 'axes.labelcolor': TEXT_PRIMARY,
 'axes.grid': True,
 'grid.color': GRID_COLOR,
 'grid.linewidth': 0.8,
 'axes.spines.top': False,
 'axes.spines.right':False,
 'xtick.color': TEXT_MUTED,
 'ytick.color': TEXT_MUTED,
 'text.color': TEXT_PRIMARY,
 'font.size': 11,
 'figure.dpi': 100,
})
print('Bibliotecas carregadas com sucesso.')
# 2. Leitura e Preparação da Base de Dados
df = pd.read_excel('CVLI.xlsx', sheet_name='CVLI')
print(f'Dimensão da base: {df.shape[0]} linhas x {df.shape[1]} colunas\n')
# Tratamento da idade (conversão e limpeza)
df['Idade_Vitima_num'] = pd.to_numeric(df['Idade da Vítima'], errors='coerce')
n_nao_informada = df['Idade_Vitima_num'].isna().sum()
print(f'Registros com idade não informada: {n_nao_informada} ({n_nao_informada/len(df):.1%} do total)')
# Tratamento de datas e horas
df['Data'] = pd.to_datetime(df['Data'])
meses_pt = {1:'Jan', 2:'Fev', 3:'Mar', 4:'Abr', 5:'Mai', 6:'Jun',
 7:'Jul', 8:'Ago', 9:'Set', 10:'Out', 11:'Nov', 12:'Dez'}
df['Mes_num'] = df['Data'].dt.month
df['Mes'] = df['Mes_num'].map(meses_pt)
df['Ano'] = df['Data'].dt.year
df['Hora_num'] = pd.to_datetime(df['Hora'], format='%H:%M:%S').dt.hour
# Ordenação cronológica dos dias da semana
ordem_dias = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
df['Dia da Semana'] = pd.Categorical(df['Dia da Semana'], categories=ordem_dias, ordered=True)
# 3. Função Auxiliar para Tabelas de Frequência Absoluta e Relativa
def tabela_frequencia(serie, ordenar_por_valor=True):
 """Retorna um DataFrame com frequência absoluta e relativa (%) de uma variável."""
 freq_abs = serie.value_counts(sort=ordenar_por_valor, dropna=False)
 freq_rel = serie.value_counts(normalize=True, sort=ordenar_por_valor, dropna=False) * 100
 tabela = pd.DataFrame({
 'Frequência Absoluta': freq_abs,
 'Frequência Relativa (%)': freq_rel.round(2)
 })
 tabela.loc['Total'] = [tabela['Frequência Absoluta'].sum(),
 tabela['Frequência Relativa (%)'].sum().round(2)]
 return tabela
# 4. Geração das Tabelas por Variáveis Categóricas
# Natureza do Crime
print("--- NATUREZA DO CRIME ---")
print(tabela_frequencia(df['Natureza']))
# Meio Empregado
print("\n--- MEIO EMPREGADO ---")
print(tabela_frequencia(df['Meio Empregado']))
# Gênero da Vítima
print("\n--- GÊNERO DA VÍTIMA ---")
print(tabela_frequencia(df['Gênero']))
# Escolaridade Detalhada
print("\n--- ESCOLARIDADE DETALHADA ---")
print(tabela_frequencia(df['Escolaridade da Vítima']))
# Escolaridade Ordenada
ordem_escolaridade = [
 'Não Alfabetizado', 'Sem Instrução', 'Alfabetizado',
 'Ensino Fundamental Incompleto', 'Ensino Fundamental', 'Ensino Fundamental Completo',
 'Ensino Médio Incompleto', 'Ensino Médio', 'Ensino Médio Completo',
 'Superior Incompleto', 'Ensino Superior Incompleto', 'Superior Completo', 'Ensino Superior',
 'Não Informada'
]
escolaridade_ordenada = pd.Categorical(df['Escolaridade da Vítima'], categories=ordem_escolaridade,
ordered=True)
print("\n--- ESCOLARIDADE ORDENADA ---")
print(tabela_frequencia(pd.Series(escolaridade_ordenada, name='Escolaridade da Vítima'),
ordenar_por_valor=False))
# Escolaridade Agrupada
mapa_escolaridade_agrupada = {
 'Não Alfabetizado': 'Não Alfabetizado / Sem Instrução',
 'Sem Instrução': 'Não Alfabetizado / Sem Instrução',
 'Alfabetizado': 'Alfabetizado',
 'Ensino Fundamental Incompleto':'Ensino Fundamental',
 'Ensino Fundamental': 'Ensino Fundamental',
 'Ensino Fundamental Completo': 'Ensino Fundamental',
 'Ensino Médio Incompleto': 'Ensino Médio',
 'Ensino Médio': 'Ensino Médio',
 'Ensino Médio Completo': 'Ensino Médio',
 'Superior Incompleto': 'Ensino Superior',
 'Ensino Superior Incompleto': 'Ensino Superior',
 'Superior Completo': 'Ensino Superior',
 'Ensino Superior': 'Ensino Superior',
 'Não Informada': 'Não Informada'
}
ordem_escolaridade_agrupada = [
 'Não Alfabetizado / Sem Instrução', 'Alfabetizado', 'Ensino Fundamental',
 'Ensino Médio', 'Ensino Superior', 'Não Informada'
]
escolaridade_agrupada = pd.Categorical(
 df['Escolaridade da Vítima'].map(mapa_escolaridade_agrupada),
 categories=ordem_escolaridade_agrupada, ordered=True
)
print("\n--- ESCOLARIDADE AGRUPADA ---")
print(tabela_frequencia(pd.Series(escolaridade_agrupada, name='Escolaridade da Vítima'),
ordenar_por_valor=False))
# Raça da Vítima (Geral e Apenas Informadas)
print("\n--- RAÇA DA VÍTIMA (GERAL) ---")
print(tabela_frequencia(df['Raça da Vítima']))
raca_informada = df.loc[df['Raça da Vítima'] != 'Não Informada', 'Raça da Vítima']
print("\n--- RAÇA DA VÍTIMA (INFORMADAS) ---")
print(tabela_frequencia(raca_informada))
# Dia da Semana
print("\n--- DIA DA SEMANA ---")
print(tabela_frequencia(df['Dia da Semana'], ordenar_por_valor=False))
# 5. Cálculo das Estatísticas Descritivas para a Variável Idade
idade = df['Idade_Vitima_num'].dropna()
media = idade.mean()
mediana = idade.median()
moda = idade.mode()[0]
q1 = idade.quantile(0.25)
q3 = idade.quantile(0.75)
p10 = idade.quantile(0.10)
p90 = idade.quantile(0.90)
iqr = q3 - q1
variancia = idade.var()
desvio_padrao = idade.std()
cv = (desvio_padrao / media) * 100
print("\n--- MEDIDAS ESTATÍSTICAS DA IDADE DA VÍTIMA ---")
print(f"Média: {media:.2f} anos")
print(f"Mediana (Q2): {mediana:.2f} anos")
print(f"Moda: {moda:.2f} anos")
print(f"1º Quartil (Q1): {q1:.2f} anos")
print(f"3º Quartil (Q3): {q3:.2f} anos")
print(f"Percentil 10 (P10): {p10:.2f} anos")
print(f"Percentil 90 (P90): {p90:.2f} anos")
print(f"Amplitude Interquartil (IQR): {iqr:.2f} anos")
print(f"Variância: {variancia:.2f}")
print(f"Desvio-padrão: {desvio_padrao:.2f} anos")
print(f"Coeficiente de Variação (CV): {cv:.2f}%")
# 6. Construção do Diagrama de Caixa (Boxplot) para Idade
plt.figure(figsize=(8, 6))
plt.boxplot(idade, vert=True)
plt.title("Boxplot — Idade da Vítima")
plt.ylabel("Idade (anos)")
plt.show()