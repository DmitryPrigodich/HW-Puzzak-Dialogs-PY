import utils
from .constuctor_base import Constructor_Base

class Hint_Data_Constructor(Constructor_Base):
    _HINT_DATA_JSON = "json_bak/LoadingHintData-module.json"
    _FILE_NAME = "data/HINTS.md"
    _FILE_NAME_JSON = "json/hints.json"

    _hint_data = {}
    _hints = {}

    def __init__(self):
        super().__init__()
        self._hint_data = self._read_json(self._HINT_DATA_JSON)
        self._set_data()

    def _set_data(self):
        for hint_header, hint_tags in self._hint_data.items():
            self._hints[hint_header] = {
                "text:": self.get_string_by_key(hint_tags.get("LocalId")),
                "requirements:": hint_tags.get("Requirements:")
            }
    
    def write_json(self):
        self._write_json(self._hints)

    def write_data(self):
        body = "# HWM HINTS:\n"
        for hint_header, hint_values in self._hints.items():
            body += f"## {hint_values}\n"
            for key, value in hint_values.items():
                body += f"* {hint_values.get(key)} {hint_values.get(value)}\n"
        utils.rewrite_file(body, self._FILE_NAME)