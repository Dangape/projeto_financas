import pandas as pd
import numpy as np
import csv
from tqdm import tqdm

#paths
prefix = "Data/dfp_cia_aberta"
years = ["_2010","_2011","_2012","_2013","_2014","_2015","_2016","_2017","_2018","_2019","_2020"]
filename = "_BPA"
type = "_con"
extention = ".csv"

unique_cvm = []
unique_cnpj = []
for year in years:
    file = prefix + filename + type + year + extention
    col_list = ['cnpj_cia','cd_cvm','dt_fim_exerc']

    data = pd.read_csv(str(file),sep=";",engine="python", quotechar='"', error_bad_lines=False)

    data.columns = data.columns.str.lower() #lowcase all headers
    data = data[col_list]
    data['dt_fim_exerc']=pd.to_datetime(data['dt_fim_exerc']) #extract year

    data["year"] = data["dt_fim_exerc"].dt.year
    data = data[data["year"]==int(year.replace("_",""))] #remove ano anterior ao de analise
    data["month"] = data["dt_fim_exerc"].dt.month
    data = data[data["month"]==12] #remove mes de novembro (11)

    unique_cvm.extend(data.cd_cvm.unique())
    unique_cnpj.extend(data.cnpj_cia.unique())
    print(len(unique_cnpj))
    print(len(unique_cvm))


cnpj_dict = pd.DataFrame({"cvm":unique_cvm,"cnpj":unique_cnpj})
cnpj_dict.drop_duplicates(subset="cvm",inplace=True)
cnpj_dict.reset_index(drop=True,inplace=True)
print(cnpj_dict)

cnpj_dict.to_csv("Dicionario/cnpj_dict.csv",index=False)