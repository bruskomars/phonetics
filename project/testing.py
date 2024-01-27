my_str = "(zsa)-zsa zone/ brother's Dacodac"

my_dict = {
    'zsa': 'zɑː',
    'zone': 'zoʊn',
    'a': 'eɪ',
    "brother's": 'test',
    'Dacodac': 'dækədæk', 'Dacongcogon': 'dækəŋkɑːɡən', 'Dacoron': 'dækoːɹɑːn', 'Dacu': 'dɑːkuː', 'Dacudao': 'dækjuːdaʊ', 'Dacula': 'dækjʊlə'
}

aa = {'Dacodac': 'dækədæk', 'Dacongcogon': 'dækəŋkɑːɡən', 'Dacoron': 'dækoːɹɑːn', 'Dacu': 'dɑːkuː', 'Dacudao': 'dækjuːdaʊ', 'Dacula': 'dækjʊlə'}


for key, value in my_dict.items():
    my_str = my_str.replace(str(key), value)
    # print(my_str)

# 👇️ bobbyhadz.com | borislav
print(my_str)