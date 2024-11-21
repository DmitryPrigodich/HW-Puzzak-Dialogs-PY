import json

class String_Data_Constructor():

    STRING_DATA_JSON = "json_bak/StringData-module.json"
    FILE_NAME = "data/STRINGS.md"
    _string_data = {}

    def __init__(self):
        self._string_data = self._read_json()

    def _read_json(self):
        with open(self.STRING_DATA_JSON, 'r', encoding='utf-8') as file:
            json_data = file.read()
        return json.loads(json_data)
    
    def get_string_by_key(self, key):
        return self._string_data.get(key)['en:']

