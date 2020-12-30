import re

test_str = "My e-mail is vladimir12.zon1tov12@gmail.com and IP 123.23.456.1 and 1111 111.123.45.212 3"

reg_exp = r"\w+\.\w+@\w+\.\w+"

reg_exp = r"\b[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\b"

result = re.findall(reg_exp, test_str)

print(result)
url = "google.com.ua"
from urllib.request import Request

import urllib.request
with urllib.request.urlopen(url) as f:
    print(f.read(300))
res = Request(url)
print(res.headers)

# API

import requests

url = "http://api.forismatic.com/api/1.0/"

params = {"method": "getQuote",
          "format": "json",
          "key": 1,
          "lang": "ru"}
for i in range(10):
    params["key"] = i
    r = requests.get(url, params=params)
    quote = r.json()
    # print(quote)
    quote_text = quote["quoteText"]
    print(quote_text)
    quote_author = quote["quoteAuthor"]
    print(quote_author)
