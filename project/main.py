from phonemizer import phonemize
import csv
import pandas as pd
import eng_to_ipa as ipa
from phonemizer.backend.espeak.wrapper import EspeakWrapper
_ESPEAK_LIBRARY = 'C:\Program Files\eSpeak NG\libespeak-ng.dll'
EspeakWrapper.set_library(_ESPEAK_LIBRARY)

###################################################

# with open('unique_names_splitted.csv', 'r') as file:
#
#     data = csv.reader(file)
#     name = []
#
#     for row in data:
#         try:
#             # mname = phonemize(row[0], language='en-us', backend='espeak')
#
#
#             #FOR SF PF
#             # ext = phonemize(row[0], language='en-us', backend='espeak')
#             # ipa_word = [row[0], ext]
#
#             # ipa_word = [line_count, row[0], mname]
#             name.append(row[0])
#             # print(row[0])
#
#         except:
#                 ipa_word = [row[0], 'error occurred']
#                 name.append(row[0])
#                 break
#
# ## Language
# a = 'en-gb-x-gbclan'
# b = 'en-us'
#
#
# no_dup = list(set(name))
# no_dup.sort()
#
# ##FOR IPA
# phonetics_ipa = []
# for name in no_dup:
#     phonetics_ipa.append(ipa.convert(name))
#     print(name)
#
# df = pd.DataFrame(phonetics_ipa, columns=['phonemizer'])
# df.to_csv('name-IPA.txt', index=False, sep='\t')
#
# ##FOR phonemizer
# # phonetics = phonemize(no_dup, language=b, backend='espeak')
# #
# # df = pd.DataFrame(phonetics, columns=['phonemizer'])
# # df.to_csv('name-phonemizer-en-us.txt', index=False, sep='\t')
#
# ##NAME FILE
# # df = pd.DataFrame(no_dup, columns=['name'])
# # df.to_csv('name.txt', index=False, sep='\t')

print(phonemize("street", language='en-us', backend='espeak'))