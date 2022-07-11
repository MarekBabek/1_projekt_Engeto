"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Marek Bábek
email: marek.babek@centrum.cz
discord: Pixoun #0920

Textový analyzátor 2: (Kratší zápis než předešla verze, bez duplicity, importované User-defined funkce a text od autora
"""

import task_template as tkt
import Functions as fct

# Zanořený list
splited_texts_list = fct.split_list(tkt.autor_text)

# Zadaný slovník uživatelů
users = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}

# Vyžádání přihlašovacího jména a hesla od uživatele
login_name = input("Enter your login name: ")
login_password = input("Enter your login password: ")

# Vlastní proměnné
separator = "-" * 50
symbols = (".", "-", ":", ";")
selection = ("1", "2", "3")
vertical_line = '|'
sum_of_words = 0
first_upper_letter_in_words = 0
small_numbers = 0
whole_upper_words = 0
words_with_numbers = 0
numbers_summation = 0

# Zjištění, jestli zadané údaje odpovídají komukoliv z registrovaných uživatelů
if users.get(login_name) == login_password:
    print(
        "", separator, "\n",
        "Welcome to the analysis application, ", login_name, "\n",
        "We have 3 texts for you to analyze", "\n",
        separator
        )

    # Výběr uživatele mezi texty
    user_selection = input("Enter a number between 1 and 3 to select: ")

    # Pokud uživatel zadá číslo, tak pokračuje dále
    if user_selection in selection:
        edited_user_selection = int(user_selection)
        print("", separator)

        # For cyklus, pro jednotlivé operace dle vybraného textu uživatelem
        for number, item in enumerate(splited_texts_list, start=1):
            if edited_user_selection == number:
                for x_1 in item:
                    if x_1 != symbols:
                        sum_of_words += 1
                print("There are ", sum_of_words, "words in the selected text")
                for x_2 in item:
                    if x_2[0].isupper():
                        first_upper_letter_in_words += 1
                print("There are ", first_upper_letter_in_words, "titlecase words")
                for x_3 in item:
                    if x_3.isupper() and x_3.isalpha():
                        whole_upper_words += 1
                print("There are ", whole_upper_words, "uppercase words")
                for x_4 in item:
                    if x_4.islower():
                        small_numbers += 1
                print("There are ", small_numbers, "lowercase words")
                for x_5 in item:
                    if x_5.isnumeric():
                        words_with_numbers += 1
                print("There are ", words_with_numbers, "numeric strings")
                for x_6 in item:
                    if x_6.isnumeric():
                        numbers_summation += int(x_6)
                print("The sum of all the numbers ", numbers_summation)

                # Odstranění přebytečných symbolů a následné doplnění do listu
                without_interpunctions_list = []
                for word in item:
                    if '.' in word:
                        without_interpunctions_list.append(word.replace('.', ''))
                    elif ',' in word:
                        without_interpunctions_list.append(word.replace(',', ''))
                    else:
                        without_interpunctions_list.append(word)

                # Součet písmen každého slova + jednotlivé očíslování každého součtu a následné doplnění to listu
                len_of_every_word_list= []
                for position, word in enumerate(without_interpunctions_list):
                    len_of_every_word_list.append(len(word))

                # Proměnná s rozsahem od 1 do (součet pozic) v listu
                range_for_list = range(1, len(len_of_every_word_list))

                # Vzestupné uspořádání listu a doplnění do listu
                sorted_list = []
                for range_for_list in sorted(len_of_every_word_list):
                    sorted_list.append(range_for_list)

                # Konvertování listu (int) na list (str) s využitím list comprehensions
                from_int_to_str_list = [str(numbers) for numbers in sorted_list]

                # for smyčka pro sečtění číselných stringů a následné přidání do slovníku
                strings_with_numbers_dictionary = {}
                for x_7 in from_int_to_str_list:
                    if not x_7 in strings_with_numbers_dictionary:
                        strings_with_numbers_dictionary[x_7] = 1
                    else:
                        strings_with_numbers_dictionary[x_7] += 1

                # Převod ze slovníku na list se sečtenými string čísly
                from_dict_to_list = list(strings_with_numbers_dictionary.values())

                # User-defined funkce (importované Functions as fct)
                # pro přepsání slov dle délky slova na hvězdice a přidání do listu
                asterisks_list = []
                for word in from_dict_to_list:
                    asterisks_list.append(fct.asterisks_replace_x(word))

                # Vypsání ohraničeného záhlaví úloha č. 7
                print(
                    '', '-' * 30, '\n',
                    'LEN|', ' ' * 2, 'OCCURENCES', ' ' * 2, '|NR.', '\n',
                    '-' * 30
                    )

                # Vypsání sloupcového grafu pomocí formátu a for cyklu
                for key, value in enumerate(asterisks_list, start=1):
                    print(f'{key:4}{vertical_line + value:19}{vertical_line + str(len(value))}')

    # Pokud uživatel zadá chybně výběr mezi texty, upozorní ho a program ukončí
    else:
        print("\n", "!!! Wrong number input, please, try it again !!!")

# Pokud uživatel není registrovaný, upozorní ho a program ukončí
else:
    print(
        "", "username: ", login_name, "\n",
        "password: ", login_password, "\n",
        "unregistered user, terminating the program"
        )