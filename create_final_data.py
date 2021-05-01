import pandas as pd
import numpy as np
import pickle

#load data
data = pd.read_pickle("corrected_accounts.pkl")

#Calculo ativo_total (conta 1)
ativo_total = data[data["cd_conta"]=="1"]
print("Ativo total:",ativo_total)

#Calculo Ativo financeiro (1.01.02 + 1.02.01.01)
first = data[data["cd_conta"]=="1.02.01.01"] #filtrat conta 1.02.01.01
first = first.sort_values(by=["cd_cvm"]) #ordenar pelo codigo cvm
first = first.reset_index(drop=True) #resetar o index do subset
print(first.duplicated(subset=['cd_cvm']).any()) #verificar se existe alguma empresa duplicada
# print(first[first["cd_cvm"].duplicated()==True])
# print(first[first["cd_cvm"]=="21199"])

second = data[data["cd_conta"]=="1.01.02"] #filtrar conta 1.01.02
second = second.sort_values(by=["cd_cvm"]) #ordenar pelo codigo cvm
second = second.reset_index(drop=True) #resetar o index do subset
print(second.duplicated(subset=['cd_cvm']).any()) #verificar se existe empresa duplicada

ativo_financeiro = second["vl_conta"].values + first["vl_conta"].values #1.02.01.01 + 1.01.02
print("Ativo financeiro:",ativo_financeiro)

#calculo ativo operacional (ativo total - ativo financeiro)
ativo_operacional  = ativo_total["vl_conta"] - ativo_financeiro #ativo total - ativo financeiro
print("Ativo operacional:",ativo_operacional)

#Data frame final
final = pd.DataFrame({"cd_cvm":ativo_total["cd_cvm"],"dt_fim_exerc":ativo_total["year"],"ativo_total":ativo_total["vl_conta"],
                      "ativo_financeiro": ativo_financeiro,"ativo_operacional":ativo_operacional}) #criar dataframe final
final = final.sort_values(by=["cd_cvm"])
final = final.reset_index(drop=True)
print(final)


