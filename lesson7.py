# Словари, методы словарей

ascii_table = {number: chr(number) for number in range(ord('a'), ord('z') + 1)}
print(ascii_table)

key = 130
if key in ascii_table: # in проверяет ключи, а не значения
    print(ascii_table[key])

print(ascii_table[key])
print(ascii_table.get(key))

for key in ascii_table: # for по ключам!
    print(key, ascii_table[key])

for key, value in ascii_table.items():
    print(key, value)


a_dict = {"age":15}
b_dict = a_dict.copy()
a_dict["name"] = "John"
print(a_dict)
print(b_dict)

print(type(ascii_table))
print(type(ascii_table.keys()), ascii_table.keys())
print(type(ascii_table.values()), ascii_table.values())
print(type(ascii_table.items()), ascii_table.items())

values = list(ascii_table.values())
print(type(values), values)

dict_1 = {"name": "John"}
dict_2 = {"age": 15, "name": "Jane"}
# dict_3 = {}
# dict_3.update(dict_1)
dict_3 = dict_1.copy()
dict_3.update(dict_2)
print(dict_3, dict_1)

# Распаковка списков и словарей

server_response = [200, "12.12.2020", "Text", {"header": "Chrome", "version": "2.0"}, "data1", "data2", 123, 0]
status, _, _, header, *_ = server_response
print(status)
print(header)
print(1,2,3)
print(*server_response)

print(header)
print(*header)

new_dict = {**dict_1, ** dict_2}
print(new_dict)
