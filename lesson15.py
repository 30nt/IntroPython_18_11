import requests
from requests_oauthlib import OAuth1
import os
import random
import time

def time_decorator(some_function): # декоратор
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = some_function(*args, **kwargs)
        print(f"Time: {time.time() - start_time}")
        return result
    return wrapper

class IconGetter:
    def __init__(self):
        key = os.environ["KEY"]
        secret = os.environ["SECRET"]
        self._auth = OAuth1(key, secret)

    @time_decorator
    def save_icon(self, key_word=''):
        if not key_word:
            key_word = str(random.randint(1, 1000))
        endpoint = f"http://api.thenounproject.com/icon/{key_word}"
        response = requests.get(endpoint, auth=self._auth)
        data = response.json()
        try:
            icon_url = data["icon"]["icon_url"]
            img = requests.get(icon_url)
            with open(f"tmp/{key_word}.svg", "wb") as file:
                file.write(img.content)
        except KeyError:
            print("Введи имя объекта")

# icon_getter = IconGetter()
# start_time = time.time()
# icon_getter.save_icon("world")
# print(f"Time: {time.time() - start_time}")

class Bbox:
    def __init__(self, x0, y0, x1, y1):
        self._x0 = x0
        self._y0 = y0
        self._x1 = x1
        self._y1 = y1

    def __repr__(self):
        return f"({self._x0}, {self._y0}, {self._x1}, {self._y1})"

    def __add__(self, other):
        x_min = min(self._x0, other._x0)
        y_min = min(self._y0, other._y0)
        x_max = max(self._x1, other._x1)
        y_max = max(self._y1, other._y1)
        return Bbox(x_min, y_min, x_max, y_max)

    @property
    def x0(self):
        return self._x0

    @property
    def y0(self):
        return self._y0

    @property
    def x1(self):
        return self._x1

    @property
    def y1(self):
        return self._y1

    @staticmethod
    def dist(point_1, point_2):
        return ((point_2[0] - point_1[0]) ** 2 - (point_2[1] - point_1[1]) ** 2) ** 0.5

bbox_1 = Bbox(3,0,5,2)
bbox_2 = Bbox(2,4,6,8)
print(dir(bbox_1))

# Полиморфизм

print(2 + 2)
print("2" + "2")
print(bbox_1 + bbox_2)