import pandas as pd
import numpy as np

dados_elementos = pd.read_excel("Dados/estrategia_con_1_0.xlsx", sheet_name="elementos_con")
dados_indicadores = pd.read_excel("Dados/estrategia_con_1_0.xlsx", sheet_name="indicadores_con")

dados = pd.merge(dados_elementos,dados_indicadores, on=["cd_cvm","dt_fim_exerc"])
dados = pd.DataFrame(dados)
print(dados)
print(dados.columns)
dados = dados.drop(columns=["denom_cia_x","cnpj_cia_x","denom_cia_y","cnpj_cia_y"])
dados =dados.set_index("cd_cvm")
print(dados)

dados.to_csv("dados.csv", index=True)
