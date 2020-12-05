alphabet = ''
alph = []
# ord chr

for index in range(ord("a"), ord('z') + 1):
    # alphabet += chr(index)
    alph.append(chr(index))

alphabet = "".join(alph)
print(alphabet)


result = [chr(index) for index in range(ord("a"), ord('z') + 1)]
alphabet = "".join(result)
print(alphabet)

ip_list = ["12.212.34.54", "199.0.0.1", "255.255.255.0", "199.0.1.0", "199.0.0.1"]

# [print(ip) for ip in ip_list]
last_null_ip = [ip for ip in ip_list if ip[-1] == '0']
print(last_null_ip)


# Множество set - набор уникальных представителей

my_list = [4, "2", 3, 1, 2, 3, 4, "3", 3, 3, 3, 3, 3, 3, 3, 3, 3]
my_set = set(my_list)
new_set = {1, 2, 'q', 'w'}

inter_set = my_set.intersection(new_set)
print(inter_set)
union_set = my_set.union(new_set)
print(union_set)
print(my_set)

my_set.intersection_update(new_set)
print(my_set)


print(my_set)
my_set.add("hello")
print(my_set)
my_set.add("33")
print(my_set)
my_set.discard("22")
res = my_set.pop()
print(my_set, res)


my_str="bla BLA car"
my_str = my_str.lower()

result = len(set(my_str))
print(result)

new_ip_list = list(set(ip_list))
print(new_ip_list)

rand_str = "".join(set(alphabet))[:10]
print(rand_str)

# Словари dict

person = ("Norris", "Chuck", "40", "USA", "ranger")
print(person[0], person[-1])
person = {"l_name": "Norris",
          "f_name": "Chuck",
          "age": 40,
          "country": "USA",
          "job": "ranger",
          }
dummy_dict = {-1: "Last position ))",
              0: 0,
              2: 5,
              (1, 3): "tuple",
              "skills": ["kik", "face"],
              "person": person}
print(dummy_dict)
print(person["l_name"], person["age"], person[-1], person[(1, 3)], person["skills"])

job = {"title": "python developer",
       "rate": 3,
       "time": "full time"}
address = {"city": "Dnipro",
           "street": "Polya",
           "building": "27/123"}
personal_data = {"address": address,
                 "phone": "067-123-45-67",
                 "status": "married"}
developer = {"name": "John",
             "conpany": "Wix",
             "personal_data": personal_data,
             "job": job}

developer["NEW KEY"] = "NEW VALUE"
developer["personal_data"]["address"]["city"] = "London"
# print(developer)
# print(developer["personal_data"]["address"]["city"])
