"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Marek Bábek
email: marek.babek@centrum.cz
discord: Pixoun #0920
"""

# Zadany text od autora úlohy
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.''']

#funkce pro rozdělení vět v listu (zanořené)
def split_list(sentence):
    TEXTS_separated = []
    for TEXTS in sentence:
        TEXTS_separated.append(TEXTS.split())
    return TEXTS_separated

rozdeleni = split_list(TEXTS)

# funkce pro nahrazení hvězdami namísto délky stringu
def asterisks_replace_x(str1):
    return '*' * (len(str1))

# Zadaný slovník uživatelů
users = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}

# Vyžádání přihlašovacího jména a hesla od uživatele
login_name = input("Enter your login name: ")
login_password = input("Enter your login password: ")

# Vlastní proměnné
oddelovac = "-" * 50
text_1 = rozdeleni[0]
text_2 = rozdeleni[1]
text_3 = rozdeleni[2]
symbols = (".", "-")
soucet_slov = 0
velke_pocatecni_pismeno = 0
male_pismeno = 0
cele_velke_slovo = 0
slovo_s_cislem = 0
soucet_vsech_cisel = 0
symbol = '|'

# Zjištění, jestli zadané údaje odpovídají komukoliv z registrovaných uživatelů
if users.get(login_name) == login_password:
    print(
    "", oddelovac, "\n",
    "Welcome to the analysis application, ", login_name, "\n",
    "We have 3 texts for you to analyze", "\n",
    oddelovac
    )

    # Výběr uživatele mezi texty
    vyber_cisla_uzivatele = int(input("Enter a number between 1 and 3 to select: "))
    print("", oddelovac)

    # Výpočet vybraných statistik pro 1. text
    if vyber_cisla_uzivatele == 1:
        vyber_cisla_uzivatele = text_1
        for x_1 in text_1:
            if x_1 != symbols:
                soucet_slov += 1
        print("There are ", soucet_slov, " words in the selected text")
        for x_2 in text_1:
             if x_2[0].isupper():
                velke_pocatecni_pismeno += 1
        print("There are ", velke_pocatecni_pismeno, "titlecase words")
        for x_3 in text_1:
            if x_3.isupper() and x_3.isalpha():
                cele_velke_slovo += 1
        print("There are ", cele_velke_slovo, "uppercase words")
        for x_4 in text_1:
            if x_4.islower():
                male_pismeno += 1
        print("There are ", male_pismeno, "lowercase words")
        for x_5 in text_1:
            if x_5.isnumeric():
                slovo_s_cislem += 1
        print("There are ", slovo_s_cislem, "numeric strings")
        for x_6 in text_1:
            if x_6.isnumeric():
                soucet_vsech_cisel += int(x_6)
        print("The sum of all the numbers ", soucet_vsech_cisel)

        # Odstranění přebytečných symbolů a následné doplnění všech slov z textu (1) do listu
        list_text = []
        for slovo in text_1:
            if '.' in slovo:
                list_text.append(slovo.replace('.', ''))
            elif ',' in slovo:
                list_text.append(slovo.replace(',', ''))
            else:
                list_text.append(slovo)

        # Odstranění stringů z listu, které obsahují čisla a následné uložení do listu
        my_list = [item for item in list_text if item.isalpha()]

        # Použití vlastní funkce (47. řádek) pro přepsání slov dle délky slova na hvězdice a přidání do listu
        asterisks_list = []
        for word in my_list:
            asterisks_list.append(asterisks_replace_x(word))

        #Vypsání ohraničeného záhlaví úloha č. 7
        print(
            '', '-' * 30, '\n',
            'LEN|', ' ' * 2, 'OCCURENCES', ' ' * 2, '|NR.', '\n',
                '-' * 30
            )

        # Vypsání sloupcového grafu pomocí formátu a for cyklu
        for key, value in enumerate(asterisks_list, start=1):
            print(f'{key:4}{symbol + value:19}{symbol + str(len(value))}')

    # Výpočet vybraných statistik pro 2. text
    elif vyber_cisla_uzivatele == 2:
        vyber_cisla_uzivatele = text_2
        for x_1 in text_2:
            if x_1 != symbols:
                soucet_slov += 1
        print("There are ", soucet_slov, " words in the selected text")
        for x_2 in text_2:
            if x_2[0].isupper():
                velke_pocatecni_pismeno += 1
        print("There are ", velke_pocatecni_pismeno, "titlecase words")
        for x_3 in text_2:
            if x_3.isupper() and x_3.isalpha():
                cele_velke_slovo += 1
        print("There are ", cele_velke_slovo, "uppercase words")
        for x_4 in text_2:
            if x_4.islower():
                male_pismeno += 1
        print("There are ", male_pismeno, "lowercase words")
        for x_5 in text_2:
            if x_5.isnumeric():
                slovo_s_cislem += 1
        print("There are ", slovo_s_cislem, "numeric strings")
        for x_6 in text_2:
            if x_6.isnumeric():
                soucet_vsech_cisel += int(x_6)
        print("The sum of all the numbers ", soucet_vsech_cisel)

        # Odstranění přebytečných symbolů a následné doplnění všech slov z textu (2) do listu
        list_text = []
        for slovo in text_2:
            if '.' in slovo:
                list_text.append(slovo.replace('.', ''))
            elif ',' in slovo:
                list_text.append(slovo.replace(',', ''))
            else:
                list_text.append(slovo)

        # Odstranění stringů z listu, které obsahují čisla a následné uložení do listu
        my_list = [item for item in list_text if item.isalpha()]

        # Použití vlastní funkce (47. řádek) pro přepsání slov dle délky slova na hvězdice a přidání do listu
        asterisks_list = []
        for word in my_list:
            asterisks_list.append(asterisks_replace_x(word))

        # Vypsání ohraničeného záhlaví úloha č. 7
        print(
            '', '-' * 30, '\n',
            'LEN|', ' ' * 2, 'OCCURENCES', ' ' * 2, '|NR.', '\n',
                '-' * 30
            )

        # Vypsání sloupcového grafu pomocí formátu a for cyklu
        for key, value in enumerate(asterisks_list, start=1):
            print(f'{key:4}{symbol + value:19}{symbol + str(len(value))}')

    # Výpočet vybraných statistik pro 3. text
    elif vyber_cisla_uzivatele == 3:
        vyber_cisla_uzivatele = text_3
        for x_1 in text_3:
            if x_1 != symbols:
                soucet_slov += 1
        print("There are ", soucet_slov, " words in the selected text")
        for x_2 in text_3:
            if x_2[0].isupper():
                velke_pocatecni_pismeno += 1
        print("There are ", velke_pocatecni_pismeno, "titlecase words")
        for x_3 in text_3:
            if x_3.isupper() and x_3.isalpha():
                cele_velke_slovo += 1
        print("There are ", cele_velke_slovo, "uppercase words")
        for x_4 in text_3:
            if x_4.islower():
                male_pismeno += 1
        print("There are ", male_pismeno, "lowercase words")
        for x_5 in text_3:
            if x_5.isnumeric():
                slovo_s_cislem += 1
        print("There are ", slovo_s_cislem, "numeric strings")
        for x_6 in text_3:
            if x_6.isnumeric():
                soucet_vsech_cisel += int(x_6)
        print("The sum of all the numbers ", soucet_vsech_cisel)

        # Odstranění přebytečných symbolů a následné doplnění všech slov z textu (3) do listu
        list_text = []
        for slovo in text_3:
            if '.' in slovo:
                list_text.append(slovo.replace('.', ''))
            elif ',' in slovo:
                list_text.append(slovo.replace(',', ''))
            else:
                list_text.append(slovo)

        # Odstranění stringů z listu, které obsahují čisla a následné uložení do listu
        my_list = [item for item in list_text if item.isalpha()]

        # Použití vlastní funkce (47. řádek) pro přepsání slov dle délky slova na hvězdice a přidání do listu
        asterisks_list = []
        for word in my_list:
            asterisks_list.append(asterisks_replace_x(word))

        # Vypsání ohraničeného záhlaví úloha č. 7
        print(
            '', '-' * 30, '\n',
            'LEN|', ' ' * 2, 'OCCURENCES', ' ' * 2, '|NR.', '\n',
                '-' * 30
            )

        # Vypsání sloupcového grafu pomocí formátu a for cyklu
        for key, value in enumerate(asterisks_list, start=1):
            print(f'{key:4}{symbol + value:19}{symbol + str(len(value))}')

    # Pokud uživatel zadá chybně výběr mezi texty, upozorní ho a program skončí
    else:
        print("Wrong input, try again")


# Pokud uživatel není registrovaný, ukončit program
else:
    print(
    "", "username: ", login_name, "\n",
    "password: ", login_password, "\n",
    "unregistered user, terminating the program"
    )