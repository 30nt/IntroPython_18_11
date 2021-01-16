# from lesson13 import TanosDemo
#
# print(dir(TanosDemo))
#
# tanos = TanosDemo()
#
# print(tanos.__create_txt_files())
# print(dir(tanos))
import os
import sys
from json_reader import JsonReader, DictWorker, ListWorker, ListDictWorker

folder = "json_data"
filename_dict = "dict.json"
filename_list = "list.json"
filename_list_dict = "list_dict.json"

dict_worker = DictWorker(os.path.join(folder, filename_dict))
list_worker = ListWorker(os.path.join(folder, filename_list), get_float=False)
list_dict_worker = ListDictWorker(os.path.join(folder, filename_list_dict))

dict_worker.read_json()
print(dict_worker.data)
dict_worker.sort()
print(dict_worker.data)

list_worker.read_json()
print(list_worker.data)
list_worker.sort()
print(list_worker.data)

# list_dict_worker.read_json()
# print(list_dict_worker.data)
# list_dict_worker.sort()
# print(list_dict_worker.data)


# reader = JsonReader(os.path.join(folder, filename))
#
# # print(dir(reader))
# reader.read_json()
#
# # print(dir(reader))
# print(reader.data)