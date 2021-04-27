import pandas as pd
import numpy as np
import csv

#paths
prefix = "Data/dfp_cia_aberta"
year = "_2010"
filename = "_BPA"
type = "_con"
extention = ".csv"

#loading data
file = prefix + filename + type + year + extention


with open(file) as csvfile:
    csvReader = csv.reader(csvfile, delimiter=';')
    data = pd.DataFrame(csvReader)

new_header = data.iloc[0] #grab the first row for the header
data = data[1:] #take the data less the header row
data.columns = new_header #set the header row as the df header
print(data.head())

data.columns = data.columns.str.lower() #lowcase all headers
data['dt_fim_exerc']=pd.to_datetime(data['dt_fim_exerc'], format='%Y-%m-%d').dt.year #extract year
print(data["dt_fim_exerc"].head())