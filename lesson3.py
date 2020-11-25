# Функции и методы строк

my_str = "dk,vkhZSfgmb,@xvzaeymhmvsknvkhb zq"
result = len(my_str)
print(result)

if '@' not in my_str:
    print("It is not e-mail")

print(my_str[-2])  # обращение по индексу
print(my_str[3:7]) # срез строки. [От включительно: до не включая]
print(my_str[1:-1])

print(my_str[4:])
print(my_str[:-3])
print("---------------------")
# print(my_str[-100:-10])
print(my_str)
print(my_str[::-1]) # -1 шаг обратного хода
print(my_str[::2]) # шаг обхода строки
print(my_str[1::2])


count = my_str.count("mv")
up_str = my_str.upper()
print(up_str)
low_str = my_str.lower()
print(low_str)
m_pos = my_str.find("mv")
print(m_pos)
my_str = my_str.replace("ZS", "!!!!!!!")
print(my_str)

new_str = input("Введи целое число")
if new_str:
    if (new_str[0] == '-' and new_str[1:].isdigit()) or new_str.isdigit():
        new_int = int(new_str)
        print(new_int)
    else:
        print("Это не число!!!")
else:
    print("Это пустая строка!!!")


for symbol in my_str:
    # if symbol.isupper() or symbol == " ":
    if symbol not in "eyuioa" and symbol.isalpha():
        print("symbol", symbol)




# Форматирование строк

my_str = "qwerty"
my_str = f"Qwerty{my_str}"
# my_str = "Qwerty{}".format(my_str)

value = len(my_str)
print(f"Я строка: _____{my_str}_____ Моя длина: {value}")

filename = "first.py"
new_filename = f"new_{filename}"
folder = "project"

path = f"{folder}/{new_filename}"
print(path)

# Тернарный оператор

value = 123

if value < 0:
    result = -1
else:
    result = 1

result = -1 if value < 0 else 1

result = 1 if value % 2 == 1 else 0

print(result)
