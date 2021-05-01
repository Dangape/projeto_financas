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


data.columns = data.columns.str.lower() #lowcase all headers
data['dt_fim_exerc']=pd.to_datetime(data['dt_fim_exerc'], format='%Y-%m-%d') #extract year

data["year"] = data["dt_fim_exerc"].dt.year
data = data[data["year"]==2010] #remove year 2009
data["month"] = data["dt_fim_exerc"].dt.month
data = data[data["month"]==12]
data = data.drop(columns = ["cnpj_cia","dt_refer","denom_cia","grupo_dfp","moeda","escala_moeda","ordem_exerc",
                            "versao","st_conta_fixa","ds_conta","dt_fim_exerc","month"])#remove extra columns
print(data)

#Checking data types and converting them
# print(data.dtypes)
data["cd_cvm"] = data['cd_cvm'].astype(str)
data["cd_conta"] = data["cd_conta"].astype(str)
data["vl_conta"] = data.vl_conta.astype(float) #mesma coisa que dividir por 10bi?

# print(data.dtypes)

final = data[data["cd_cvm"]=="1023"] #ativo total
print("1.08" not in final.values)

#ativo_financeiro_2010 = data.loc[(data["cd_cvm"]==)]
print(final)

unique_cvm = data.cd_cvm.unique()
unique_account = data.cd_conta.unique()

#
print(len(unique_cvm))
print(len(unique_account))



for cvm in tqdm(unique_cvm):
    for account in unique_account:
        if account in data[(data["cd_cvm"]==str(cvm))].values:
            #print("ja tem a conta",account,"na empresa",cvm)
            pass
        elif account not in data[(data["cd_cvm"]==str(cvm))].values:
            new_row = {'cd_cvm': str(cvm), 'year': int(2010), 'cd_conta': str(account), 'vl_conta': float(0)}
            data = data.append(new_row,ignore_index=True)
            #print("linha adicionada, conta:",account,"na empresa",cvm)

first = data[data["cd_cvm"]=="1023"]
second = data[data["cd_cvm"] =="14206"]
print(len(first))
print(len(second))

data.to_pickle("corrected_accounts.pkl") #save corrected dataframe
data = pd.read_pickle("corrected_accounts.pkl")
print(data)
