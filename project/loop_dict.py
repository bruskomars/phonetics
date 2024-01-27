import pandas as pd
import csv

my_dic = pd.read_excel('for_dict.xlsx', index_col=0).to_dict()
dict2 = my_dic['phonetics']
# print(my_dic)

with open('name_list_test.csv', 'r') as file:

    data = csv.reader(file)
    name_list = []

    for row in data:
        name = str(row[0])
#
        name_split = name.split()
        # print(name_split)
        name_split_converted = []

        for i in name_split:
            for key, value in dict2.items():
                if i == str(key):
                    name = name.replace(str(key), value)
                    # name_split_converted.append(value)
                    # print(i, "-", value)
                    # my_str = i.replace(str(key), value)
                else:
                    continue

        #     name_join = ' '.join(name_split_converted)
        #     print(name_join)
        # name_split.append(name_join)
        print(name)
        # for key, value in dict2.items():
        #     name = name.replace(str(key), value)
        #
        # print(name)