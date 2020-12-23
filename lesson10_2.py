from lesson11 import number
# from lesson10 import create_text_line
#
# result = create_text_line(10, 100)
# print(__name__)
# print(">>>>>", result)

import random

def generate_number(limit=100):
    return random.randint(1, limit)

result = generate_number(number)
print(result)
assert result <= 100
