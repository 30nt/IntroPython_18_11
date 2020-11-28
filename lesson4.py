# Кортеж Tuple

my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
strings = ("qwe", "asd", "zxc")
print(my_tuple)
print(strings)
print(my_tuple[-4])  # обращение по индексу
index = 2
print(my_tuple[index])

coord_tr = ((0, 0), (1, 1), (0, 2))
print(coord_tr[-1][-1])

respose = (403, "text", "goole.com.ua", "data")
url = respose[2]
status = respose[0]
if status == 200:
    print("OK")
else:
    print("Error", status)
print(my_tuple)
print(my_tuple[2:3])  # срез ОТ(вкл) ДО(не вкл)

value = len(my_tuple)
print(value)

print(my_tuple[len(my_tuple) - 1])

print(my_tuple[2:])
print(my_tuple[:-2])
print(my_tuple[:])

print(my_tuple[::2]) # на четных местах
print(my_tuple[1::2]) # на нечетных местах
print(my_tuple[::-1]) # в обратном порядке (разворот)

print(my_tuple[-2:-5])
print(my_tuple[-5:-2])
print(my_tuple[-2:-5:-1]) # Дзен пайтон
new = my_tuple[-4:-1]
print(new[::-1])
print(my_tuple[-5:-2:-1])

a = 2
b = 5

tmp = a
a = b
b = tmp

a, b = b, a

tup = b, a
print(tup, type(tup))
a, b = tup # распаковка объекта (кортеж)
print(a, b)

_, str_2, _ = strings
print(str_2)

val1, val2, val3, *_ = my_tuple
print(_)


# Список List

my_list = [4, 9, 5, 6, 7, 8, 9]

my_strings = list(strings)
my_strings[-1] = "QWE"
my_strings = tuple(my_strings)
print(my_strings)

my_list[0] = 100
my_list.append(my_strings) # добавление в конец списка
my_list.insert(3, "00000")
my_list.remove(my_strings)
my_list.remove(9)
val = my_list.pop()
print(val)
print(my_list)

my_str = "_asd_fs_dgfhg__/fj_"
my_list = list(my_str)
split_str = my_str.split("_")
print(split_str)
res_str = "-".join(split_str[1:-1])
print(res_str)


# Циклы
my_list = [4, 9, 5, 6, 7, 8, 9]
for number in my_list:
    print(f"Number {number}")

for symbol in "saDFHfg jsjshs hmeEos23 &^(cmb":
    if (symbol.lower() in "eyuioa") and symbol.isupper():
        print(f"symbol: {symbol}")










# Обработка исключений

new_str = input("Введи целое число")

try:
    new_int = int(new_str)
    value = 1 / new_int
    print(value)
except ValueError:
    print("Введи только цифры!")
except ZeroDivisionError:
    print("На ноль делить нельзя!")
