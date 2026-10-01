# Análise Estatística de Dados

## Sobre o trabalho

Este projeto acadêmico aplica técnicas de estatística descritiva e análise exploratória a bases de dados em formato Excel. O material recebido contém dois notebooks independentes:

1. **Análise de CVLI** — examina registros de Crimes Violentos Letais Intencionais (CVLI) da cidade de Fortaleza em 2026 até Setembro, com frequências por natureza do crime, meio empregado, gênero, escolaridade, raça e dia da semana. Também calcula medidas descritivas da idade das vítimas e apresenta um boxplot.
2. **Análise domiciliar de geração e destino do lixo** — explora uma base de domicílios com informações como idade, escolaridade, estado civil, salário, profissão, número de pessoas na família, quantidade de lixo gerado e destino do lixo. O notebook produz resumos estatísticos e visualizações para apoiar a interpretação dos dados.

## Objetivos

- Organizar e preparar dados para análise;
- Resumir variáveis categóricas com frequências absolutas e relativas;
- Calcular medidas descritivas de variáveis numéricas;
- Explorar padrões nos dados com tabelas e gráficos;
- Praticar o uso de Python para análise estatística.

## Tecnologias utilizadas

- Python 3
- Jupyter Notebook ou Google Colab
- pandas
- NumPy
- Matplotlib
- SciPy

## Como executar

### No Google Colab

1. Abra o notebook desejado no Google Colab.
2. Envie a planilha correspondente quando solicitado pelo notebook.
3. Confira se o nome do arquivo carregado corresponde ao nome usado na leitura dos dados.
4. Execute as células em ordem, de cima para baixo.

### Localmente

1. Instale Python 3 e Jupyter Notebook, caso ainda não estejam disponíveis.
2. Instale as bibliotecas necessárias:

   ```bash
   pip install pandas numpy matplotlib scipy openpyxl jupyter
   ```

3. Coloque a planilha esperada no local indicado pelo notebook ou ajuste o caminho do arquivo no código.
4. Inicie o Jupyter e abra o notebook:

   ```bash
   jupyter notebook
   ```

5. Execute todas as células em ordem.

## Dados necessários

- **Notebook CVLI:** espera encontrar uma planilha chamada `CVLI.xlsx`, com uma aba chamada `CVLI`. O código utiliza campos como `Natureza`, `Meio Empregado`, `Gênero`, `Escolaridade da Vítima`, `Raça da Vítima`, `Dia da Semana`, `Idade da Vítima`, `Data` e `Hora`.
- **Notebook de lixo:** espera encontrar uma planilha chamada `Base_.xlsx`. O notebook considera campos como `Idade`, `Grau de instrução`, `Estado Civil`, `Salário (S.M.)`, `Pessoas na Família`, `Lixo Gerado (Kg)` e `Destino do Lixo`.

As planilhas não foram incluídas nos arquivos recebidos junto com o código. Para reproduzir os resultados, é necessário obter os dados utilizados originalmente e manter sua origem e autorização de uso documentadas.

## Análises realizadas

### CVLI

- Limpeza e conversão da idade para formato numérico;
- Extração de mês, ano e hora a partir de data e horário;
- Tabelas de frequência para variáveis categóricas;
- Agrupamento e ordenação de categorias de escolaridade;
- Estatísticas da idade: média, mediana, moda, quartis, percentis, amplitude interquartil, variância, desvio-padrão e coeficiente de variação;
- Visualização da distribuição de idade por meio de boxplot.

### Geração e destino do lixo

- Leitura e inspeção da base de domicílios;
- Resumos estatísticos e tabelas de frequência;
- Visualizações exploratórias envolvendo características dos domicílios e geração/destino do lixo.

## Autoria acadêmica

- **Instituição:** [UNIFOR]
- **Curso/Disciplina:** [Metodos Quantitativos Computacionais]
- **Professor(a):** [Vera Lucia da Silva]
- **Integrantes:** [Isabella Anton, Anderson Herculano, Karine Duarte]
- **Período:** [4º Semestre]


Este material foi elaborado para fins acadêmicos. Registre aqui a fonte das bases de dados e a licença ou autorização de uso, se aplicável.
