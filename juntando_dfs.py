import pandas as pd
import numpy as np
from tqdm import tqdm

pd.set_option('display.float_format', lambda x: '%.5f' % x)
#carregando arquivos
df_2010 = pd.read_csv("Elementos/final_2010.csv")
df_2011 = pd.read_csv("Elementos/final_2011.csv")
df_2012 = pd.read_csv("Elementos/final_2012.csv")
df_2013 = pd.read_csv("Elementos/final_2013.csv")
df_2014 = pd.read_csv("Elementos/final_2014.csv")
df_2015 = pd.read_csv("Elementos/final_2015.csv")
df_2016 = pd.read_csv("Elementos/final_2016.csv")
df_2017 = pd.read_csv("Elementos/final_2017.csv")
df_2018 = pd.read_csv("Elementos/final_2018.csv")
df_2019 = pd.read_csv("Elementos/final_2019.csv")
df_2020 = pd.read_csv("Elementos/final_2020.csv")
cnpj_dict = pd.read_csv("Dicionario/cnpj_dict.csv")
b3 = pd.read_excel(r"Dicionario/dicionario_b3.xlsx",engine="openpyxl")

#checar quais empresas estão em todos os dataframes
# match = [x for x in df_2010["cd_cvm"].values if x in df_2011["cd_cvm"].values if x in df_2012["cd_cvm"].values if x in df_2013["cd_cvm"].values]
frames = [df_2020,df_2019,df_2018,df_2016,df_2017,df_2015,df_2014,df_2013,df_2012,df_2011,df_2010]
final = pd.concat(frames)
final = final.reset_index(drop=True)

for column in final.columns[2:]:
  for row in range(0,len(final)):
    if abs(final.loc[row,column]) >= 10**12:
      final.loc[row,column] = final.loc[row,column]/10**9

# final = final.round(5)

#adicionando coluna de cnpj
cnpj_dict.columns = ["cd_cvm","cnpj"]
cnpj_dict["cnpj"] = "0"+cnpj_dict.cnpj.values
# cnpj_dict.cnpj.apply(lambda x: x.rjust(1,"0"))
dicionario = dict(zip(cnpj_dict.cd_cvm,cnpj_dict.cnpj))
final["cnpj"] = final["cd_cvm"].map(dicionario)

print(b3["CNPJ"])

#verificando existencia na b3
final["b3"] = np.zeros(len(final))
print(final.loc[1,"cnpj"])

for row in range(0,len(final)):
  if final.loc[row,"cnpj"] in b3["CNPJ"].values:
    final.loc[row,"b3"] = 1
  else:
    final.loc[row,"b3"] = 0

print(final.b3)
#salvar arquivo csv
final.to_csv("Finalizados/elementos_totais.csv",index=False)

# create excel writer object
writer = pd.ExcelWriter('Finalizados/elementos_totais.xlsx',engine='xlsxwriter')
# write dataframe to excel
final.to_excel(writer,index=False)
# save the excel
writer.save()
print('DataFrame is written successfully to Excel File.')