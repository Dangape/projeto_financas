import pandas as pd
import numpy as np
import datetime as dt


#Load data
dados_elementos = pd.read_excel("Dados/estrategia_con_1_0.xlsx", sheet_name="elementos_con")
dados_indicadores = pd.read_excel("Dados/estrategia_con_1_0.xlsx", sheet_name="indicadores_con")

dados = pd.merge(dados_elementos,dados_indicadores, on=["cd_cvm","dt_fim_exerc"]) #merge data
dados = pd.DataFrame(dados)
print(dados)
print(dados.columns)
dados = dados.drop(columns=["denom_cia_x","cnpj_cia_x","denom_cia_y","cnpj_cia_y"]) #drop company name and cnpj column
#dados =dados.set_index("cd_cvm") #set CVM code as index
dados['dt_fim_exerc']=pd.to_datetime(dados['dt_fim_exerc'], format='%m/%d/%Y').dt.year
print(dados)

#save new data do csv
dados.to_csv("dados.csv", index=True)
