from phonemizer import phonemize
import csv
import pandas as pd
import eng_to_ipa as ipa
from phonemizer.backend.espeak.wrapper import EspeakWrapper
_ESPEAK_LIBRARY = 'C:\Program Files\eSpeak NG\libespeak-ng.dll'
EspeakWrapper.set_library(_ESPEAK_LIBRARY)

###################################################

with open('unique_names_splitted.csv', 'r') as file:

    data = csv.reader(file)
    name = []

    for row in data:
        try:
            name.append(row[0])
            # print(row[0])

        except:
                ipa_word = [row[0], 'error occurred']
                name.append(row[0])
                break


no_dup = list(name)
no_dup.sort()

def ipa_phonetics(file):
    phonetics_ipa = []
    for n in file:
        phonetics_ipa.append(ipa.convert(n))
        print(n)

    df = pd.DataFrame(phonetics_ipa, columns=['phonemizer'])
    df.to_csv('name-IPA2.txt', index=False, sep='\t')

def phonemizer_phonetics(file):
    # language
    a = 'en-gb-x-gbclan'
    b = 'en-us'

    phonetics = phonemize(file, language=b, backend='espeak')

    df = pd.DataFrame(phonetics, columns=['phonemizer'])
    df.to_csv('PHONEMIZER_1.txt', index=False, sep='\t')

# CALL FUNC