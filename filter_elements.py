import pandas as pd
import numpy as np
import csv
from tqdm import tqdm

#paths
prefix = "Data/dfp_cia_aberta"
# years = ["_2010","_2011","_2012","_2013","_2014","_2015","_2016","_2017","_2018","_2019","_2020"]
years = ["_2019","_2020"]
# filename = ["_BPA","_BPP","_DFC_MI","_DRE"]
filename = ["_BPP"]
type = "_con"
extention = ".csv"

#creating data
for year in years:
    for x in tqdm(filename):
        file = prefix + x + type + year + extention

        data = pd.read_csv(str(file),sep=";",engine="python",converters={"VL_CONTA":str}, quotechar='"', error_bad_lines=False)
        print(data)

        data.columns = data.columns.str.lower() #lowcase all headers
        data['dt_fim_exerc']=pd.to_datetime(data['dt_fim_exerc']) #extract year

        data["year"] = data["dt_fim_exerc"].dt.year
        data = data[data["year"]==int(year.replace("_",""))] #remove ano anterior ao de analise
        data["month"] = data["dt_fim_exerc"].dt.month
        data = data[data["month"]==12] #remove mes de novembro (11)
        data = data.drop(columns = ["cnpj_cia","dt_refer","denom_cia","grupo_dfp","moeda","escala_moeda","ordem_exerc",
                                    "versao","st_conta_fixa","ds_conta","dt_fim_exerc","month"]) #remove extra columns
        #print(data)

        #Checking data types and converting them
        # print(data.dtypes)
        data["cd_cvm"] = data['cd_cvm'].astype(str)
        data["cd_conta"] = data["cd_conta"].astype(str)
        data["vl_conta"] = data["vl_conta"].apply(lambda x: x.replace(".","")) #remove points
        data["vl_conta"] = data["vl_conta"].astype(float) #mesma coisa que dividir por 10bi?
        # print(data.dtypes)

        # final = data[data["cd_cvm"]=="1023"] #ativo total
        # print("1.08" not in final.values)
        #
        # #ativo_financeiro_2010 = data.loc[(data["cd_cvm"]==)]
        # print(final)
        #
        unique_cvm = data.cd_cvm.unique()
        unique_account = data.cd_conta.unique()

        # print(len(unique_cvm))
        # print(unique_account)

        for cvm in tqdm(unique_cvm):
            for account in unique_account:
                if account in data[(data["cd_cvm"]==str(cvm))].values:
                    #print("ja tem a conta",account,"na empresa",cvm)
                    pass
                elif account not in data[(data["cd_cvm"]==str(cvm))].values:
                    new_row = {'cd_cvm': str(cvm), 'year': int(year.replace("_","")), 'cd_conta': str(account), 'vl_conta': float(0)}
                    data = data.append(new_row,ignore_index=True)
                    #print("linha adicionada, conta:",account,"na empresa",cvm)

        # first = data[data["cd_cvm"]=="1023"]
        # second = data[data["cd_cvm"] =="14206"]
        # print(len(first))
        # print(len(second))
        savefile = "corrected_files/corrected_accounts"+str(x)+str(year)+".pkl"
        data.to_pickle(savefile) #save corrected dataframe
        data = pd.read_pickle(savefile)
        print("Ano:",year,data)
