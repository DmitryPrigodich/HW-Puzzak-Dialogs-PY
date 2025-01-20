import utils
from .constructor_base import Constructor_Base
from .quest_constructor import Quest_Constructor
from .quest_line_constructor import Quest_Line_Constructor

class Glossary_Constructor(Constructor_Base):
    _FILE_NAME = "data/GLOSSARY.md"
    _FILE_NAME_JSON = "json/glossary.json"

    _glossary = {}

    def __init__(self):
        super().__init__()
        self._set_data()

    def _set_data(self):
        do = "nothing"

    def get_data(self):
        return self._glossary
    
    def write_json(self):
        utils.write_json(self._glossary,self._FILE_NAME_JSON)

    def write_data(self):
        body = f"# HWM Glossary:\n"

        for string_key, string_value in self._strings.items():
            if string_key.startswith("glossary"):
                # name_list = string_key.split(".")
                # UNFINISHED
                
                body += f"### {string_key}\n"
                body += f"{string_value}\n\n"
        startswith = startswith.replace(".","")

        
        
        utils.rewrite_file(body, self._FILE_NAME)



