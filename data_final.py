import pandas as pd
import numpy as np
import pickle
from tqdm import tqdm

years = ["2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020"]

for year in tqdm(years):
    #Carregando BPA
    data_BPA = pd.read_pickle("corrected_files/corrected_accounts_BPA_"+year+".pkl")
    #Carregando BPP
    data_BPP = pd.read_pickle("corrected_files/corrected_accounts_BPP_"+year+".pkl")
    #Carregando DRE
    data_DRE = pd.read_pickle("corrected_files/corrected_accounts_DRE_"+year+".pkl")
    #Carregando DFC_MI
    data_DFCMI = pd.read_pickle("corrected_files/corrected_accounts_DFC_MI_"+year+".pkl")

    # def returnNotMatches(a, b):
    #     return [[x for x in a if x not in b], [x for x in b if x not in a]]
    ################################BPA####################################################
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

    ################################BPP####################################################
    #calculo do passivo
    passivo = data_BPP[data_BPP["cd_conta"]=="2"]["vl_conta"].values - data_BPP[data_BPP["cd_conta"]=="2.03"]["vl_conta"].values
    # print("Passivo:",passivo)

    #passivo financeiro
    passivo_financeiro = data_BPP[data_BPP["cd_conta"]=="2.01.04"]["vl_conta"].values + data_BPP[data_BPP["cd_conta"]=="2.02.01"]["vl_conta"].values

    #passivo operacional
    passivo_operacional = passivo - abs(passivo_financeiro) #arrumar valores negativos

    #patrimonio liquido
    patrimonio_liquido = data_BPP[data_BPP["cd_conta"]=="2.03"]["vl_conta"].values

    #passivo circulante
    passivo_circulante = data_BPP[data_BPP["cd_conta"]=="2.01"]["vl_conta"].values

    ################################DRE####################################################
    #lucro liquido
    lucro_liquido = data_DRE[data_DRE["cd_conta"]=="3.11"]["vl_conta"].values

    #receita de vendas
    receita_vendas = data_DRE[data_DRE["cd_conta"]=="3.01"]["vl_conta"].values

    #resultado financeiro
    resultado_financeiro = data_DRE[data_DRE["cd_conta"]=="3.06"]["vl_conta"].values

    #resultado operacional liquido (ROL)
    protecao_fiscal = resultado_financeiro * 0.34
    rol = lucro_liquido - resultado_financeiro + protecao_fiscal

    #ROL continuado
    rol_cont = data_DRE[data_DRE["cd_conta"]=="3.09"]["vl_conta"].values - resultado_financeiro + protecao_fiscal

    ################################DFC_MI####################################################
    #fluxo de caixa operacional(FCO)
    fco = data_DFCMI[data_DFCMI["cd_conta"]=="6.01"]["vl_conta"].values
    unique_DFCMI = data_DFCMI.cd_cvm.unique()
    unique_BPA = data_BPA.cd_cvm.unique()
    mismatch = [x for x in unique_BPA if x not in unique_DFCMI] #tem no BPA e nao tem no DFCMI

    #fluxo de caixa investimentos
    fco_invest = data_DFCMI[data_DFCMI["cd_conta"]=="6.02"]["vl_conta"].values

    #fluxo de caixa financeiro
    fco_financeiro = data_DFCMI[data_DFCMI["cd_conta"]=="6.03"]["vl_conta"].values

    ################################FINAL####################################################

    #Data frame final
    final = pd.DataFrame({"cd_cvm":ativo_total["cd_cvm"],"dt_fim_exerc":ativo_total["year"],"ativo_total":ativo_total["vl_conta"],
                          "ativo_financeiro": ativo_financeiro,"ativo_operacional":ativo_operacional,"ativo_circulante":ativo_circulante.values,
                          "passivo":passivo,"passivo_financeiro":passivo_financeiro,"passivo_operacional":passivo_operacional,
                          "patrimonio_liquido":patrimonio_liquido,"passivo_circulante":passivo_circulante,
                          "lucro_liquido":lucro_liquido,"receita_vendas":receita_vendas,"protecao_fiscal":protecao_fiscal,
                          "res_opera_liq":rol,"res_opera_liq_cont":rol_cont,"resultado_financeiro":resultado_financeiro}) #criar dataframe final

    final = final.sort_values(by=["cd_cvm"])
    final = final.reset_index(drop=True)

    final = final[~final["cd_cvm"].isin(mismatch)] #remove mismatch
    final["fco"] = fco
    final["fco_investimento"] = fco_invest
    final["fco_financeiro"] = fco_financeiro

    #colunas de resultados
    final["ativo_operacional_liq"] = final["ativo_operacional"] - final["passivo_operacional"]
    final["passivo_financeiro_liq"] = final["passivo_financeiro"] - final["ativo_financeiro"]
    final["resultado_fin_liq"] = final["resultado_financeiro"] - final["protecao_fiscal"]
    final["accrual"] = final["res_opera_liq"] - final["fco"]

    #salva em arquivo csv
    final.to_csv("Elementos/final_"+year+".csv", index=False)



