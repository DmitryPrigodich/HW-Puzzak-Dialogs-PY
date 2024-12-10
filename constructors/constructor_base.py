import utils

class Constructor_Base:
    _FILE_NAME = ""
    _FILE_NAME_TMP = ""
    _FILE_NAME_JSON = ""

    _STRING_DATA_JSON = "json_bak/StringData-module.json"
    _STAR_MAP_JSON = "json/starmap.json"

    _string_data = {}
    _star_map = {}

    def __init__(self):
        self._star_map = utils.read_json(self._STAR_MAP_JSON)
        self._set_string_data()

    def _set_string_data(self):
        self._string_data = utils.read_json(self._STRING_DATA_JSON)
        self._string_data = {k.lower(): v for k, v in self._string_data.items()}

    def get_string_by_key(self, key):
        key = key.lower()
        if key in self._string_data:
            return self._string_data.get(key)["en:"]
        return None
    
    def get_starsystem_by_coords(self,coords):
        if coords in self._star_map:
            return self._star_map.get(coords)
        return None