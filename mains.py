import pandas as pd
import numpy as np

dados_elementos = pd.read_excel("Dados/estrategia_con_1_0.xlsx", sheet_name="elementos_con")
dados_indicadores = pd.read_excel("Dados/estrategia_con_1_0.xlsx", sheet_name="indicadores_con")
print(dados_elementos.head())
print(dados_indicadores.head())

