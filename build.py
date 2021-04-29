import pandas as pd
import numpy as np
import csv
from tqdm import tqdm

#paths
prefix = "Data/dfp_cia_aberta"
year = "_2010"
filename = "_BPA"
type = "_con"
extention = ".csv"

#loading data
file = prefix + filename + type + year + extention

data = pd.read_csv("Data/dfp_cia_aberta_BPA_con_2010.csv",sep=";",engine="python",converters={"VL_CONTA":str})

print(data.head())

data.columns = data.columns.str.lower() #lowcase all headers
data['dt_fim_exerc']=pd.to_datetime(data['dt_fim_exerc'], format='%Y-%m-%d').dt.year #extract year
data = data.drop(columns = ["cnpj_cia","dt_refer","denom_cia","grupo_dfp","moeda","escala_moeda","ordem_exerc",
                            "versao","st_conta_fixa","ds_conta"])#remove extra columns

#Checking data types and converting them
print(data.dtypes)
data["cd_cvm"] = data['cd_cvm'].astype(str)
data["cd_conta"] = data["cd_conta"].astype(str)
data["vl_conta"] = data.vl_conta.astype(float) #mesma coisa que dividir por 10bi?

print(data.dtypes)

final = data[data["cd_conta"]=="1"] #ativo total

#ativo_financeiro_2010 = data.loc[(data["cd_cvm"]==)]
print(final)

unique_cvm = data.cd_cvm.unique()
unique_account = data.cd_conta.unique()
unique_year = [2009,2010]

# print(unique_cvm)
# print(unique_account)

for year in unique_year:
    for cvm in unique_cvm:
        for account in unique_account:
            if account in data[(data["cd_cvm"]==str(cvm))&(data["dt_fim_exerc"]==year)].values:
                print("ja tem a conta",account,"na empresa",cvm)
            else:
                new_row = {'cd_cvm': str(cvm), 'dt_fim_exerc': year, 'cd_conta': str(account), 'vl_conta': float(0)}
                data = data.append(new_row,ignore_index=True)
                print("linha adicionada, conta:",account,"na empresa",cvm)

first = data[data["cd_cvm"]=="1023"]
second = data[data["cd_cvm"] =="21091"]
print(len(first))
print(len(second))

data.to_pickle("corrected_accounts.pkl")
data = pd.read_pickle("corrected_accounts.pkl")
print(data)

