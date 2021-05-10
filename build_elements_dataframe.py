import pandas as pd
import numpy as np
import pickle

#Carregando BPA
data_BPA = pd.read_pickle("corrected_files/corrected_accounts_BPA_2010.pkl")
#Carregando BPP
data_BPP = pd.read_pickle("corrected_files/corrected_accounts_BPP_2010.pkl")
#Carregando DRE
#Carregando DFC_MI

#Calculo ativo_total (conta 1)
ativo_total = data_BPA[data_BPA["cd_conta"]=="1"]
# print("Ativo total:",ativo_total)

#Calculo Ativo financeiro (1.01.02 + 1.02.01.01)
first = data_BPA[data_BPA["cd_conta"]=="1.02.01.01"] #filtrar conta 1.02.01.01
first = first.sort_values(by=["cd_cvm"]) #ordenar pelo codigo cvm
first = first.reset_index(drop=True) #resetar o index do subset
# print(first.duplicated(subset=['cd_cvm']).any()) #verificar se existe alguma empresa duplicada
# print(first[first["cd_cvm"].duplicated()==True])
# print(first[first["cd_cvm"]=="21199"])

second = data_BPA[data_BPA["cd_conta"]=="1.01.02"] #filtrar conta 1.01.02
second = second.sort_values(by=["cd_cvm"]) #ordenar pelo codigo cvm
second = second.reset_index(drop=True) #resetar o index do subset
# print(second.duplicated(subset=['cd_cvm']).any()) #verificar se existe empresa duplicada

ativo_financeiro = second["vl_conta"].values + first["vl_conta"].values #1.02.01.01 + 1.01.02
# print("Ativo financeiro:",ativo_financeiro)

#calculo ativo operacional (ativo total - ativo financeiro)
ativo_operacional  = ativo_total["vl_conta"] - ativo_financeiro #ativo total - ativo financeiro
# print("Ativo operacional:",ativo_operacional)

#calculo ativo circulante
ativo_circulante = data_BPA[data_BPA["cd_conta"] == "1.01"]["vl_conta"]
# print("ativo circulante:",ativo_circulante)

#calculo do passivo
passivo = data_BPP[data_BPP["cd_conta"]=="2"]["vl_conta"].values - data_BPP[data_BPP["cd_conta"]=="2.03"]["vl_conta"].values
# print("Passivo:",passivo)

#passivo financeiro
passivo_financeiro = data_BPP[data_BPP["cd_conta"]=="2.01.04"]["vl_conta"].values - data_BPP[data_BPP["cd_conta"]=="2.02.01"]["vl_conta"].values

#passivo operacional
passivo_operacional = passivo - passivo_financeiro #arrumar valores negativos

#patrimonio liquido
patrimonio_liquido = data_BPP[data_BPP["cd_conta"]=="2.03"]["vl_conta"].values

#Data frame final
final = pd.DataFrame({"cd_cvm":ativo_total["cd_cvm"],"dt_fim_exerc":ativo_total["year"],"ativo_total":ativo_total["vl_conta"],
                      "ativo_financeiro": ativo_financeiro,"ativo_operacional":ativo_operacional,"ativo_circulante":ativo_circulante.values,
                      "passivo":passivo,"passivo_financeiro":passivo_financeiro,"passivo_operacional":passivo_operacional,
                      "patrimonio_liquido":patrimonio_liquido}) #criar dataframe final

final = final.sort_values(by=["cd_cvm"])
final = final.reset_index(drop=True)
print(final)

#salva em arquivo csv
final.to_csv("Elementos/final_2010.csv", index=False)
# def returnNotMatches(a, b):
#     return [[x for x in a if x not in b], [x for x in b if x not in a]]

