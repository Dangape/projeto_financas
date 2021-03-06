import pandas as pd
import numpy as np

#Load data
pd.set_option('display.float_format', lambda x: '%.5f' % x)
data = pd.read_csv("Finalizados/elementos_totais.csv")
print(data.columns)
print(data.head(5))

lc = data.ativo_circulante/data.passivo_circulante #liquidez_corrente

molc = data.res_opera_liq_cont/data.receita_vendas #margem_operacional_liquida_continuada

mol = data.res_opera_liq/data.receita_vendas #margem_operacional_liquida

ga = data.receita_vendas/data.ativo_operacional_liq #giro do ativo

rpl = data.lucro_liquido/data.patrimonio_liquido #Retorno sobre Patrimônio Líquido

al = data.passivo_financeiro_liq/data.patrimonio_liquido #Alavancagem

raol = data.res_opera_liq_cont/data.ativo_operacional #Retorno sobre Ativo Operacional Líquido

cpfl = data.resultado_fin_liq/data.passivo_financeiro_liq #Custo do Passivo Financeiro Líquido

spread = raol + cpfl #spread

accrual = data.accrual

cnpj = data.cnpj

b3 = data.b3

indices_finais = pd.DataFrame({"cd_cvm":data.cd_cvm,"dt_fim_exerc":data.dt_fim_exerc,"liquidez_corrente":lc,"margem_operacional_liquida_continuada":molc,"margem_operacional_liquida":mol,
                               "giro_ativo":ga,"retorno_patrimonio_liquido": rpl,"alavancagem":al,"retorno_ativo_oper_liq":raol,"custo_pass_fin_liq":cpfl,
                               "spread":spread,"accrual":accrual,"cnpj":cnpj,"b3":b3})

indices_finais.replace([np.inf, -np.inf], int(0), inplace=True)
print(indices_finais)

#salvar arquivo csv
indices_finais.to_csv("Finalizados/indices.csv",index=False)

# create excel writer object
writer = pd.ExcelWriter('Finalizados/indices.xlsx')
# write dataframe to excel
indices_finais.to_excel(writer,index=False)
# save the excel
writer.save()
print('DataFrame is written successfully to Excel File.')
