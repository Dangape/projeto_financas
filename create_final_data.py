import pandas as pd
import numpy as np
import pickle

#load data
data = pd.read_pickle("corrected_accounts.pkl")
#data = data[data["dt_fim_exerc"]==2010]
#data = data.reset_index(drop=True)


#Calculo ativo_total
ativo_total = data[data["cd_conta"]=="1"]

#Calculo Ativo financeiro
contas = ativo_total
print(contas)
first = data[data["cd_conta"]=="1.02.01.01"]
first = first.sort_values(by=["cd_cvm"])
first = first.reset_index(drop=True)
print(first.duplicated(subset=['cd_cvm']).any())
print(first[first["cd_cvm"].duplicated()==True])
print(first[first["cd_cvm"]=="21199"])
second = data[data["cd_conta"]=="1.01.02"]
second = second.sort_values(by=["cd_cvm"])
second = second.reset_index(drop=True)
print(second.duplicated(subset=['cd_cvm']).any())


contas["ativo_financeiro"] = second["vl_conta"].values + first["vl_conta"].values
print(contas)
# print(len(first.cd_cvm.unique()))
# print(len(second.cd_cvm.unique()))
# print(second)
# print(first)
# for i in first.cd_cvm.values:
#     if i in second.cd_cvm.values:
#         #print(i,"ta aqui")
#         pass
#     else:
#         print(i,"faltando!!!!!!!!!")
# final = pd.DataFrame({"cd_cvm":ativo_total["cd_cvm"],"dt_fim_exerc":ativo_total["dt_fim_exerc"],"ativo_total":ativo_total["vl_conta"],
#                       "ativo_financeiro":})
# final = final.sort_values(by=["cd_cvm"])
# final = final.reset_index(drop=True)
# print(final)


#print(data[(data["cd_cvm"]==str(22497))&(data["dt_fim_exerc"]==2010)].values)