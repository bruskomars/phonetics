import pandas as pd
import csv

# CONVERTING EXCEL TO DICT FILE
my_dict = pd.read_excel('__xsampa_dict.xlsx', index_col=0).to_dict()
dict2 = my_dict['sampa']

req_col = [0,0]
df_phonetics = pd.read_excel('sfpf_.xlsx', usecols=req_col)

xsampa_list = []

for i, row in df_phonetics.iterrows():
    name = str(row['phonetics'])

    for key, value in dict2.items():
        name = name.replace(str(key), str(value))

    print(name)
    xsampa_list.append(name)

df = pd.DataFrame(xsampa_list, columns=['phonetics-xSampa'])
df.to_csv('phonetics_Sampa.txt', index=False, sep='\t')