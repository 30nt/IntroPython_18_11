import json

class JsonReader:
    def __init__(self, path_file):
        self._path_file = path_file
        self.data = None

    def __repr__(self):
        return self._path_file

    def read_json(self):
        with open(self._path_file, 'r') as file:
            self.data = json.load(file)

    def sort(self):
        raise Exception("This method should be implement into shild class")

class ListWorker(JsonReader):
    def __init__(self, path_file, get_float):
        super().__init__(path_file)
        self._get_float = get_float

    def read_json(self):
        super().read_json()
        if self._get_float:
            self.data = list(map(float, self.data))

    def sort(self):
        self.data = sorted(self.data)

class DictWorker(JsonReader):
    def sort(self):
        self.data = {key_dict: self.data[key_dict] for key_dict in sorted(self.data.keys(), key=len)}

class ListDictWorker(JsonReader):
    pass