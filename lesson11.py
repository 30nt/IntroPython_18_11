#################################
# Функции сортировки
# Регулярное выражение

import re

# my_str = "190 - 196"
# ages = re.findall(r'[0-9]+', my_str)
# print(ages)


dict_list = [
    {"name": "John", "age": "1900 - 1966"},
    {"name": "Bob", "age": "1923 - 1958"},
    {"name": "Jacob", "age": "1945 - 1999"}
]


def key_sorted_by_age(obj_dict):
    ages = re.findall(r'[0-9]+', obj_dict["age"])
    d_date = ages[-1]
    return int(d_date)
#
#
# def key_sorted_by_name(obj_dict):
#     return obj_dict["name"]
#
#
# def key_sorted_by_len_name(obj_dict):
#     return len(obj_dict["name"])
#
#
new_dict_list = sorted(dict_list, key=key_sorted_by_age)
print(new_dict_list)

# test_list = ['a1sd', 'abd', 'zxc', 'q', 'we', 'ASD', "1"]
# new_list = sorted(test_list, key=len)
# print(new_list)

# numb_list = [1, 2, 3, -2, -10]
# new_numb = sorted(numb_list, key=abs)
# print(new_numb)

# for line in sorted(test_list):
#     print(line)
# test_list.sort()
# print(test_list)


# Щелчек Таноса
# 1. Создать папку ./alphabet/ или проверить, что папка существует.
# 2. В папку ./alphabet/ поместить файлы вида a.txt, b.txt, ..., z.txt в которых
# будет записана строка алфавита, но с заменой буквы из названия файла на прописную.
# Пример: для b.txt строка будет aBcde...
# 3. Сделать щелчек Таноса - удалить случайным образом половину всех файлов в этой папке.


# https://py.checkio.org/en/mission/sort-by-extension/
#
# import os
# from os.path import join as path_join
# from os.path import isfile
# from string import ascii_lowercase as alphabet
#
#
# def tanos_click(dirname):
#     files = sorted([file for file in os.listdir(dirname) if isfile(path_join(dirname, file))])
#     for file in list(set(files))[:len(files) // 2]:
#         os.remove(path_join(dirname, file))
#
#
# def create_txt_files(dirname):
#     for symbol in alphabet:
#         # file_name = f"{dirname}/{symbol}.txt" # плохо
#         file_name = os.path.join(dirname, f"{symbol}.txt")
#         new_alphabet = alphabet.replace(symbol, symbol.upper())
#         write_txt_file(file_name, new_alphabet)
#
#
# def write_txt_file(filename, data):
#     with open(filename, "w") as txt_file:
#         txt_file.write(data)
#
#
# def create_dir(dir_name):
#     try:
#         os.mkdir(dir_name)
#     except FileExistsError:
#         pass
#
#
# dir_name = 'alphabet'
# create_dir(dir_name)
# create_txt_files(dir_name)
# tanos_click(dir_name)
