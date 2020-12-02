# REVERSE = True

my_str = 'blablacar'
my_symbol = "bla"
"""
1) У вас есть переменная my_str, тип - str. И переменная my_symbol, тип - str. 
Напечатать ЧИСЛО сколько раз my_symbol встречается в my_str. 
Пример:  my_str="blablacar", my_symbol="bla". 
Вывод на экран:
2
"""

# count = my_str.count(my_symbol)
# print(count)


"""
2) У вас есть переменная my_str, тип - str. И переменная my_symbol, тип - str. 
Напечатать столько раз my_symbol, сколько он встречается в my_str. 
Пример:  my_str="blablacar", my_symbol="bla". 
Вывод на экран:
bla
bla
"""
# print("\n".join([my_symbol] * count))
# res = f"{my_symbol}\n" * count
# print(res.strip())
# print('---------')

# for _ in range(count):
#     print(my_symbol)

# [print(my_symbol) for _ in range(count)]

"""
3) У вас есть переменная my_str, тип - str. Напечатать ЧИСЛО сколько 
РАЗНЫХ символов встречается в my_str. 
Большая и маленькая буква считается как один символ. 
Пробелы, запятые и т.д. считаем тоже как символы.
Пример:  my_str="bla BLA car". 
Вывод на экран:
6
"""
# my_str="bla BLA car"
# my_str = my_str.lower()
#
# res_str = ''
# for symbol in my_str:
#     if symbol not in res_str:
#         res_str += symbol
# print(len(res_str), res_str)

"""
4)
Дана строка my_str и пустой список my_list.
Заполнить my_list символами из my_str, 
которые стоят на четных местах в строке (считаем с 0)
"""
# my_list = list(my_str[::2])  # создание нового объекта
#
# my_list = []
# my_list.extend(list(my_str[::2]))  # добавление в существующий!!!

# ИНДЕКСЫ ))
# for index in range(len(my_str)):
#     if not index % 2:
#         my_list.append(my_str[index])
# print(my_str)
# print(my_list)
"""
5)
Дана строка my_str, список str_index целых чисел в диапазоне от 
0 до длинны строки минус 1, пустой список my_list.
Заполнить my_list символами из my_str, которые стоят на местах с 
индексами из str_index
"""
# my_str = "qwerty"
# str_index = [5, 5, 4, 0, 3, 1, 2, 5, 2, 0]
# my_list = []
#
# for index in str_index:
#     my_list.append(my_str[index])
#
# print(my_list)

"""
6)
Даны списки my_list_1 и my_list_2.
Создать список my_result в который поместить элементы из my_list_1 и 
my_list_2 через один, начиная с my_list_1.
a) кол-во эл-тов одинаковое
б) кол-во эл-тов разное. Оставшиеся дописать в конец.
"""
my_list_1 = [10, 20, ]
my_list_2 = [1, 2, 3, 4, 5, 6]
my_result = []
# if len(my_list_1) == len(my_list_2):
#     # for index in range(len(my_list_1)):
#     #     my_result.append(my_list_1[index])
#     for index, value in enumerate(my_list_1):
#         my_result.append(value)
#         my_result.append(my_list_2[index])
# else:
#     if len(my_list_1) < len(my_list_2):
#         my_list_1, my_list_2 = my_list_2, my_list_1
#     for index in range(len(my_list_2)):
#         my_result.append(my_list_1[index])
#         my_result.append(my_list_2[index])
#     my_result.extend(my_list_1[len(my_list_2):])
#
# print(my_result)




"""
7)
Даны списки my_list_1 и my_list_2.
Создать список my_result в который вначале поместить 
элементы на четных местах из my_list_1, 
а потом все элементы на нечетных местах из my_list_2.
"""

# ДЗ




"""
8)
Дано целое число (int). Определить сколько цифр в этом числе.
"""

value = 172635138486283571265300000000
#
# count = len(str(value))
# print(count)






"""
9)
Дано целое число. Определить наибольшую цифру в этом числе.
"""
# value = "123qweA}"
res = max(str(value))
# print(res)

# print(ord("1"), ord("z"))
# print(chr(123))




"""
10)
Дано целое число. Составить число с цифрами в обратном порядке.
"""

# res = int(str(value)[::-1])
# print(res)
# print(len(str(res)))



"""
11)
Дано целое число. Составить число с цифрами в порядке возрастания(убывания).
"""

# value_list = list(str(value))
# value_list.sort()  # сортировка списка
# res = int("".join(value_list))
# print(res)

# value_list = list(str(value))
# new_list = sorted(value_list)  # сортировка копии списка
# res = int("".join(new_list))
# print(res)




"""
Цикл с условием(while)
Игра с угадыванием числа.

"""
VALUE = 12

user_value = int(input("Угадай число!"))

while user_value != VALUE:
    if user_value > VALUE:
        user_value = int(input("Попробуй меньше число"))
    else:
        user_value = int(input("Попробуй больше число"))

# you_are_right = False
# while not you_are_right:
#     if user_value > VALUE:
#         user_value = int(input("Попробуй меньше число"))
#     elif user_value < VALUE:
#         user_value = int(input("Попробуй больше число"))
#     else:
#         you_are_right = True

print("Ура, Красавчик!")

