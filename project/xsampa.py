import pandas as pd
import csv
import openpyxl

my_dic = pd.read_excel('xsampa_dict.xlsx', index_col=0).to_dict()
dict2 = my_dic['sampa']
# # print(my_dic)

req_col = [3,3]
df_phonetics = pd.read_excel('phonetics_Feb2024.xlsx', usecols=req_col)


name_list = []
for i, row in df_phonetics.iterrows():
    name = str(row['phonetics - FIL'])

    for key, value in dict2.items():
        name = name.replace(str(key), str(value))

    print(name)
    name_list.append(name)

df = pd.DataFrame(name_list, columns=['phonetics'])
df.to_csv('phonetics-FIL_Sampa.txt', index=False, sep='\t')