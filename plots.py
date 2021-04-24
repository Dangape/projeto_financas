import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#load data (33 columns)
data = pd.read_csv("dados.csv")
data = pd.DataFrame(data)
print(data.head())

#visualize data
#correlation matrix
corr = data.corr(method='pearson')
plt.figure(figsize=(20,15))
sns.heatmap(corr, cmap="YlOrRd",vmin=-1., vmax=1., annot=False, fmt='.2f', cbar=True, linewidths=0.8)
plt.title("Pearson correlation")
plt.savefig("corr_matrix.png")
plt.show()

print(data.columns)
#dist plot
for i in data.columns:

    plt.hist(data[str(i)], density=2,alpha=0.50)
#sns.displot(data, x="lucro_liquido", bins=20)
    plt.show()

