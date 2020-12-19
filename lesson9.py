# csv формат
import csv

with open("test.csv", "r") as csv_file:
    data = []
    reader = csv.DictReader(csv_file, delimiter=";")
    for row in reader:
        data.append(row)
print(data)
data.append({'name': '10', 'e-mail': '20@gmail.com', 'text': '30'})

with open("test_new.csv", "w") as csv_file:
    fieldnames = data[0].keys()
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=";")
    writer.writeheader()
    writer.writerows(data)



# for row in data:
#     print("e-mail:", row["e-mail"])

# with open("test.csv", "r") as csv_file:
#     data = []
#     reader = csv.reader(csv_file, delimiter=";")
#     for row in reader:
#         data.append(row)
#
# data.append([5, "6@gmail.com", 7])
#
# with open("test_new.csv", "w") as csv_file:
#     writer = csv.writer(csv_file, delimiter=";")
#     writer.writerows(data)



# # headers = data.pop(0)
# print(data)
# # print(headers)
# for row in data[1:]:
#     print("e-mail:", row[1])






# json формат
# import json
#
# with open("test.json", "r", encoding="utf-8") as json_file:
#     data = json.load(json_file)

# print(type(data), data)

# with open("test.json", "r") as json_file:
#     data_txt = json_file.read()
# print(type(data_txt), data_txt)
# json_data = json.loads(data_txt)
# print(json_data)

# data["last_name"] = "Connor"
# data["skils"] = {"test": True}
# data_txt = json.dumps(data)
# print(data_txt, type(data_txt))

# with open("test_new.json", "w") as json_file:
#     json.dump(data, json_file, indent=2)
