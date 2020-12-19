import json
import csv


def read_txt(filename):
    with open(filename, 'r') as file:
        data = []
        for line in file.readlines():
            data.append(line.strip())
    return data


def read_json(filename):
    with open(filename, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)
    return data


def read_csv(filename):
    with open(filename, "r") as csv_file:
        data = []
        reader = csv.DictReader(csv_file, delimiter=";")
        for row in reader:
            data.append(row)
    return data


def read_file(filename):
    ext = filename.split('.')[-1]
    if ext == "txt":
        result = read_txt(filename)
    elif ext == "json":
        result = read_json(filename)
    elif ext == "csv":
        result = read_csv(filename)
    else:
        print("IncorrectFileType")
        result = ''
    return result


result_txt = read_file("Homeworks/domains.txt")
print(result_txt)
result_json = read_file("test.json")
print(result_json)
result_csv = read_file('test.csv')
print(result_csv)
