# Объектно-ориентированное программирование

# class Point:  # Класс
#     x = 0  # атрибут класса
#     y = 0  # атрибут класса
#
# # Структуры данных
# points = {"A": {"x": 0, "y": 0},
#           "B": {"x": 2, "y": 4}}
# print(points["B"]["x"])
#
# point_A = Point()  # экземпляр класса
# B = Point()  # экземпляр класса
#
# B.x = 2
# B.y = 4
#
# print(point_A.x, point_A.y)
# print(B.x, B.y)

# атрибут экземпляра класса

class Person:
    # name = "John"
    # age = 20
    # job = "programmer"
    # address = "New York, 21 av."

    def __init__(self, name, age, job, address):
        self.name = name  # атрибут экземпляра класса
        self.age = age  # атрибут экземпляра класса
        self.job = job  # атрибут экземпляра класса
        self.address = address  # атрибут экземпляра класса

    def __str__(self):
        return f"Name: {self.name}\nAge: {self.age}"

    def __repr__(self):
        return f"{self.name}"

    def increase_age(self):  # метод класса (точнее метод экземпляра класса)
        self.age += 1

#
#
#
person_1 = Person("John", 20, "programmer", "New York, 21 av.")
person_2 = Person("Masha", 30, "programmer", "Dnipro")
persons = [person_1, person_2]
# person_1.increase_age()
print(persons)
print(person_1)


# person_1.family = "1"
# Person.family = "5"
# print(person_1.family)
# person_2 = Person("Masha", 30, "programmer", "Dnipro")
# person_3 = person_2
# print(person_1 is person_2)
# print(person_3 is person_2)
# print(person_2.family)


import os
from os.path import join as path_join
from os.path import isfile
from string import ascii_lowercase as alphabet


class TanosDemo:
    def __init__(self, dir_name):
        self.dir_name = dir_name
        self.create_dir()
        self.create_txt_files()

    def __str__(self):
        return self.dir_name

    def create_dir(self):
        try:
            os.mkdir(self.dir_name)
        except FileExistsError:
            pass

    def create_txt_files(self):
        for symbol in alphabet:
            file_name = os.path.join(self.dir_name, f"{symbol}.txt")
            new_alphabet = alphabet.replace(symbol, symbol.upper())
            self.write_txt_file(file_name, new_alphabet)


    def write_txt_file(self, filename, data):
        with open(filename, "w") as txt_file:
            txt_file.write(data)

    def tanos_click(self):
        files = sorted([file for file in os.listdir(self.dir_name) if isfile(path_join(self.dir_name, file))])
        for file in list(set(files))[:len(files) // 2]:
            os.remove(path_join(self.dir_name, file))




tanos_obj = TanosDemo("tmp")

print(tanos_obj)
# tanos_obj.tanos_click()
# tanos_obj.create_txt_files()

