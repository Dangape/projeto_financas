import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#Carregando dados
elementos = pd.read_csv("Finalizados/elementos_totais.csv")
indicadores = pd.read_csv("Finalizados/indices.csv")

print(len(elementos.columns))
#Density plot
n_rows = 5
n_cols = 5

for column in elementos.columns:
    plt.figure()
    sns.distplot(elementos[column])
    plt.show()
