# Projeto de Finanças (Trabalho em andamento)
Este projeto visa a criação de um artigo a respeito de utilização de dados financeiros de empresas para decisão de investimentos.\
Este é um projeto em andamento e ainda não está pronto para publicação ou avaliação.

# Base de dados
Caso queira ter acesso a base de dados utilizada, acesse este [link](http://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/DADOS/), onde irá encontrar dados acerca de demonstrativos financeiros de algumas empresas brasileiras.

# Arquivos e Pastas
- A pasta `Artigos` possui referências bibliográficas usadas para o estudo

- O arquivo `corrigindo_contas.py` lê todos os dados baixados do site da CVM e verificar se cada empresa possui todas as contas necessárias. Caso não possua, o código cria a conta com valor zero

- O arquvivo `data_final.py` utiliza os dados corrigidos anteriormente, e o dicionário descrito para criar os elementos necessários non dataframe final.

- Para conseguir ler os arquivos de contas corrigidas é necessário usar a função `pd.read_pickle`, presente no pacote `pandas` 

- A pasta `corrected_files` possui todos os arquivos corrigidos em formato `.pkl`. Para ler os arquivos use a função `pd.read_pickle()` da biblioteca Pandas

- A pasta `Data` possui os arquivos brutos, sem nenhum tratamento, em formato `.csv`

- A pasta `Elementos`, será usada para salvar os DataFrames finais, com contas corrigidas e elementos gerados

- O arquivo `elementos_totais.csv` é o DataFrame tratado com todos os anos e empresas, este é o dataframe que deverá ser usado para calculo de índices e testes.

# Dicionário de Variáveis
Nessa seção está descrito como foram filtrados os elementos de cada balanço baixado do site da CVM. Os balanços usados foram: `BPP`,`BPA`,`DFC_MI` e `DRE`. Abaixo estão demonstrados as formas de cálculos de cada elemento.

## BPA
ativo total = 1 \
ativo financeiro = 1.01.02 + 1.02.01.01\
ativo operacional = ativo total-ativo financeiro\
ativo circulante = 1.01

## BPP
passivo = 2 - 2.03 \
passivo financeiro = 2.01.04 + 2.02.01\
passivo operacional = passivo - passivo financeiro\
patrimonio liquido = 2.03\
passivo circulante = 2.01

## Resultados
ativo operacional liquido = ativo operacional - passivo operacional\
passivo financeiro liquido = passivo financeiro - ativo financeiro\
resultado financeiro liquido = resultado financeiro - proteção fiscal

## DFC_MI
Fluxo de Caixa Operacional (FCO) = 6.01\
fluxo de caixa investimentos = 6.02\
fluxo de caixa financeiro = 6.03

## DRE
Receita de vendas = 3.01\
resultado operacional liquido (ROL) = (3.11 - 3.06) + proteção fiscal\
ROL continuado = 3.09 - 3.06 + proteção fiscal\
resultado financeiro = 3.06\
proteção fiscal = resultado financeiro * 0.34\
lucro liquido = 3.11

# Dicionário de Indicadores

- Liquidez corrente = ativo circulante/passivo circulante

- Margem Operacional Líquida Continuada = resultado operacional líquido continuado/receita vendas

- Margem Operacional Líquida = resultado operacional líquido/receita vendas

- Giro do Ativo = receita vendas/ativo operacional líquido

- Retorno sobre Patrimônio Líquido Ajustado = lucro abrangente/patrimônio líquido

- Retorno sobre Patrimônio Líquido = lucro líquido/patrimônio líquido

- Alavancagem = passivo financeiro líquido/patrimônio líquido

- Retorno sobre Ativo Operacional Líquido (RAOL) = resultado operacional líquido continuado/ativo operacional líquido

- Custo do Passivo Financeiro Líquido (CPFL) = resultado financeiro líquido/passivo financeiro líquido

- Spread = RAOL + CPFL

