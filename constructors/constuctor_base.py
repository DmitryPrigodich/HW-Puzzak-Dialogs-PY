import json
import utils

class Constructor_Base:
    _FILE_NAME_JSON = ""

    _STRING_DATA_JSON = "json_bak/StringData-module.json"
    _STAR_MAP_DATA_JSON = "json/starmap.json"

    _string_data = {}
    _star_map = {}

    def __init__(self):
        self._string_data = self._read_json(self._STRING_DATA_JSON)
        self._star_map = self._read_json(self._STAR_MAP_DATA_JSON)

    def clean_file(self, file_name):
        utils.rewrite_file("", file_name)

    def _read_json(self, json_file):
        with open(json_file, 'r', encoding='utf-8') as file:
            json_data = file.read()
        return json.loads(json_data)
    
    def _write_json(self, json_input):
        json_data = json.dumps(json_input, ensure_ascii=False)
        utils.rewrite_file(json_data, self._FILE_NAME_JSON)

    def set_string_data(self):
        self._string_data = self._read_json(self._STRING_DATA_JSON)
        self._string_data = {k.lower(): v for k, v in self._string_data.items()}

    def get_string_by_key(self, key):
        if key in self._string_data:
            return self._string_data.get(key)["en:"]
        return None
    
    def get_star_system(self, coords):
        return self._star_map.get(coords)