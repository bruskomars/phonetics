import pandas as pd
import csv

my_dic = pd.read_excel('for_dict.xlsx', index_col=0).to_dict()
dict2 = my_dic['phonetics']
# print(my_dic)

with open('name_list_SFPF.csv', 'r') as file:

    data = csv.reader(file)
    name_list = []

    for row in data:
        name = str(row[0])
#
        name_split = name.split()
        print(name_split)
        name_split_converted = []

        for i in name_split:
            for key, value in dict2.items():
                if i == str(key):
                    name = name.replace(str(key), str(value))
                else:
                    continue

        name_list.append(name)

df = pd.DataFrame(name_list, columns=['phonetics'])
df.to_csv('phonetics_map_SFPF.txt', index=False, sep='\t')