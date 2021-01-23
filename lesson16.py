# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 11:20:26 2021
@author: Александр Терещук
Lesson 14. ООП. Область видимости атрибутов и методов класса.
Наследование классов.
"""


# В компьютерной игре есть юниты (персонажи).
# Каждый юнит имеет такие характеристики:
# имя
# клан
# здоровье    (int от 1 до 100. Начальное значение 100)
# сила        (int от 1 до 10. Начальное значение 1)
# ловкость    (int от 1 до 10. Начальное значение 1)
# интелект    (int от 1 до 10. Начальное значение 1)
#
# Каждый юнит может лечиться (увеличить свое здоровье на 10 пунктов, максимум 100) - написать метод увеличения здаровья.
#
# Есть три типа юнитов - маги, лучники и рыцари.
# У магов есть дополнительная характеристика - тип магии (воздух, огонь, вода)
# У лучников есть дополнительная характеристика - тип лука (лук, арбалет)
# У рыцарей есть дополнительная характеристика - тип оружия (меч, топор, пика)

# Каждый юнит может увеличить свой базовый навык на 1 пункт, максимум 10.
# Маг увеличивает интелект.
# Лучник увеличивает ловкость.
# Рыцарь увеличивает силу.
# Написать метод увеличения базового навыка (в родительском классе).

# Предложить свою реализацию классов Unit, Mage, Archer, Knight.

class Unit:
    def __init__(self, name, clan):
        self.name = name
        self.clan = clan
        self.health = 100
        self._power = 1
        self._agility = 1
        self._intellect = 1
        self._base_skil = 1

    @property
    def power(self):
        return self._power

    @property
    def agility(self):
        return self._agility

    @property
    def intellect(self):
        return self._intellect

    def __repr__(self):
        return f"Name: {self.name}, clan: {self.clan}, intellect: {self.intellect}, power: {self.power}"

    def therapy(self):
        if self.health <= 90:
            self.health += 10
        elif self.health > 90:
            self.health = 100

    def increase_base_skill(self):
        if self._base_skil < 10:
            self._base_skil += 1


class Mage(Unit):
    def __init__(self, name, clan, type_magic):
        super().__init__(name, clan)
        self.type_magic = type_magic

    @property
    def intellect(self):
        return self._base_skil


# class Unit:
#     def __init__(self, name, clan):
#         self.name = name
#         self.clan = clan
#         self.health = 100
#         self.power = 1
#         self.agility = 1
#         self.intellect = 1
#         self.unit_type = ""
#
#     def __repr__(self):
#         return f"Name: {self.name}, clan: {self.clan}, intellect: {self.intellect}, power: {self.power}"
#
#     def therapy(self):
#         if self.health <= 90:
#             self.health += 10
#         elif self.health > 90:
#             self.health = 100
#
#     def increase_base_skill(self):
#         if self.unit_type == "mage":
#             self.intellect += 1
#         elif self.unit_type == "archer":
#             self.agility += 1
#         if self.unit_type == "knight":
#             self.power += 1
#
#
# class Mage(Unit):
#     def __init__(self, name, clan, type_magic):
#         super().__init__(name, clan)
#         self.type_magic = type_magic
#         self.unit_type = "mage"

mage_1 = Mage("Gendalf", "Humans", "Fire")
print(mage_1)
mage_1.increase_base_skill()
mage_1.increase_base_skill()
print(mage_1)


# stack

def checkio(expression):
    stack = []
    brackets_dict = {")" : "(", "}" : "{", "]" : "["}
    for symbol in expression:
        if symbol in brackets_dict.values():
            stack.append(symbol)
        elif symbol in brackets_dict:
            if not stack:
                return False
            elif brackets_dict[symbol] == stack[-1]:
                stack.pop()
            else:
                return False
    return not stack



# рекурсия
def get_recursive_list(source_list, res_list):
    if not source_list:
        return
    for index in range(len(source_list)):
        my_list = source_list.copy()
        my_list.pop(index)
        res_list.append(my_list)
        get_recursive_list(my_list, res_list)
    # res_list.append(source_list)
    res_list = list(map(tuple, res_list))
    res_list = list(set(res_list))
    res_list = list(map(list, res_list))
    return sorted(res_list, key=len, reverse=True)


my_list = [1,2,3,4,5]
res_list = []
res = get_recursive_list(my_list, res_list)
print(res)