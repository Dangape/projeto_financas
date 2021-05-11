import pandas as pd
import numpy as np

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

#checar quais empresas estão em todos os dataframes
# match = [x for x in df_2010["cd_cvm"].values if x in df_2011["cd_cvm"].values if x in df_2012["cd_cvm"].values if x in df_2013["cd_cvm"].values]
frames = [df_2020,df_2019,df_2018,df_2016,df_2017,df_2015,df_2014,df_2013,df_2012,df_2011,df_2010]
final = pd.concat(frames)
final = final.reset_index(drop=True)
print(final)

#salvar arquivo
final.to_csv("Finalizados/elementos_totais.csv")
# create excel writer object
writer = pd.ExcelWriter('Finalizados/elementos_totais.xlsx')
# write dataframe to excel
final.to_excel(writer)
# save the excel
writer.save()
print('DataFrame is written successfully to Excel File.')