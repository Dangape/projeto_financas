# Projeto de Finanças
Este projeto visa a criação de um artigo a respeito de utilização de dados financeiros de empresas para decisão de investimentos.\
Este é um projeto em andamento e ainda não está pronto para publicação ou avaliação.

# Base de dados
Caso queira ter acesso a base de dados utilizada, acesse este [link](http://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/DADOS/), onde irá encontrar dados acerca de demonstrativos financeiros de algumas empresas brasileiras.

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
resultado abrangente = 2.03.08 - 2.03.08 (ano anterior) (2010=0)\
passivo circulante = 2.01

## Resultados
ativo operacional liquido = ativo operacional - passivo operacional\
passivo financeiro liquido = passivo financeiro - ativo financeiro\
resultado financeiro liquido = resultado financeiro - proteção fiscal\
lucro abrangente = resultado abrangente + lucro liquido

## DFC_MI
Fluxo de Caixa Operacional (FCO) = 6.01\
fluxo de caixa investimentos = 6.02\
fluxo de caixa financeiro = 6.03

## DRE
Receita de vendas = 3.01\
resultado operacional liquido (ROL) = (3.11 - 3.06) + proteção fiscal\
ROL continuado = 3.09 - 3.06 + proteção fiscal\
resultado financeiro = 3.06\
proteção fiscal = resultado financeiro * 0.34 (essa aliquota muda todo ano?)\
lucro liquido = 3.11
