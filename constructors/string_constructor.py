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
        startswith = startswith.replace(".","")
        utils.rewrite_file(body, f"data/STRINGS_{startswith}.md".upper())
    
    def get_cinematics_lines(self, cinematic_id):
        cinematics_map = {
            "20": ("INTRO #1", ["001_001","001_002","001_003","001_004","001_005","001_005b","001_006","001_007"]),
            "10": ("INTRO #2", ["002_001","002_002","002_003","002_004","002_005"]),
            "30": ("TANOCHET", ["003_001","003_002","003_003","003_004"]),
            "35": ("VAYGR BETRAYAL", ["004_001","004_002","004_003","004_004","004_005","004_006"]),
            "50": ("KIITHLESS", ["005_001","005_002","005_003","005_004","005_005","005_006"]),
            "40": ("LIGHTHOUSE", ["006_001","006_002","006_003","006_004","006_005","006_006","006_007"]),
            "25": ("NIMBUS", ["007_001","007_002","007_003","007_004","007_005","007_006","007_007"]),
        }

        def add_lines(title, line_numbers):
            body = f"### CINEMATIC: {title}\n"
            for number in line_numbers:
                string_text = self.get_string_by_key(f"cinematic_{number}")
                body += utils.format_quote(f"{string_text}")
            return body

        if cinematic_id in cinematics_map:
            title, line_numbers = cinematics_map[cinematic_id]
            return add_lines(title, line_numbers)
        return None