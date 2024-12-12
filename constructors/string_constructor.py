import utils
from .constructor_base import Constructor_Base

class String_Data_Constructor(Constructor_Base):
    _FILE_NAME = "data/STRINGS.md"
    _FILE_NAME_JSON = "json/strings.json"

    _strings = {}

    def __init__(self):
        super().__init__()
        self._set_data()

    def _set_data(self):
        for string_header, string_tags in self._string_data.items():
            self._strings[string_header] = string_tags.get('en:')
    
    def get_data(self):
        return self._strings

    def write_json(self):
        utils.write_json(self._strings, self._FILE_NAME_JSON)

    def write_data(self):
        body = "# HWM STRINGS:\n"
        for string_header, string_text in self._strings.items():
            body += f"* {string_header}: {string_text}\n"
        utils.rewrite_file(body, "self._FILE_NAME")

    def write_startswith(self, startswith):
        body = f"# HWM Glossary: Starts with {startswith}:\n"
        for string_key, string_value in self._strings.items():
            if string_key.startswith(startswith):
                body += f"### {string_key}\n"
                body += f"{string_value}\n\n"
        utils.rewrite_file(body, f"data/STRINGS_{startswith.replace(".","")}.md".upper())
    
    def get_cinematics_lines(self, cinematic_id):
        cinematics_map = {
            "001": ("INTRO #1", ["001","002","003","004","005","005b","006","007"]),
            "002": ("INTRO #2", ["001","002","003","004","005"]),
            "003": ("TANOCHETLAN", ["001","002","003","004"]),
            "004": ("VAYGR BETRAYAL", ["001","002","003","004","005","006"]),
            "005": ("KIITHLESS", ["001","002","003","004","005","006"]),
            "006": ("LIGHTHOUSE", ["001","002","003","004","005","006","007"]),
            "007": ("NIMBUS", ["001","002","003","004","005","006","007"]),
        }

        def add_lines(title, line_numbers):
            body = f"### CINEMATIC: {title}\n"
            for number in line_numbers:
                string_text = self.get_string_by_key(f"cinematic_{cinematic_id}_{number}")
                body += f"{string_text}\n"
            return body

        if cinematic_id in cinematics_map:
            title, line_numbers = cinematics_map[cinematic_id]
            return add_lines(title, line_numbers)
        return None