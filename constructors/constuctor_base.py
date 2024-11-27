import json
import utils

class Constructor_Base:
    STRING_DATA_JSON = "json_bak/StringData-module.json"
    FILE_NAME_JSON = ""
    _string_data = {}


    def __init__(self):
        self._string_data = self._read_json(self.STRING_DATA_JSON)


    def _read_json(self, json_file):
        with open(json_file, 'r', encoding='utf-8') as file:
            json_data = file.read()
        return json.loads(json_data)
    
    def _write_json(self, json_input):
        json_data = json.dumps(json_input, ensure_ascii=False)
        utils.rewrite_file(json_data, self.FILE_NAME_JSON)

    def set_string_data(self):
        self._string_data = self._read_json(self.STRING_DATA_JSON)
        self._string_data = {k.lower(): v for k, v in self._string_data.items()}