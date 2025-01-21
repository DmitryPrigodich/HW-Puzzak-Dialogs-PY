import utils
from .constructor_base import Constructor_Base

class Glossary_Constructor(Constructor_Base):
    _FILE_NAME = "dataset/data/GLOSSARY.md"
    _FILE_NAME_JSON = "dataset/json/glossary.json"

    _glossary = {}

    def __init__(self):
        super().__init__()
        self._set_data()

    def _set_data(self):
        for string_key, string_value in self._string_data.items():
            if string_key.startswith("glossary."):
                if string_value != "None":
                    self._glossary[string_key.replace("glossary.","")] = string_value.get('en:')

    def get_data(self):
        return self._glossary
    
    def write_json(self):
        utils.write_json(self._glossary,self._FILE_NAME_JSON)

    def write_data(self):
        body = utils.format_heading1("HWM Glossary")

        header = ""
        for gl_key, gl_value in self._glossary.items():
            name_first_part = gl_key.split(".")[0]

            if header != name_first_part:
                header = name_first_part
                print(name_first_part)
                body += utils.format_heading2(header.upper())
               
            body += utils.format_bold(gl_key.replace(f"{header}.", ""))
            body += utils.format_br(1)
            body += utils.format_paragraph(gl_value)
            body += utils.format_br(1)      
        
        utils.rewrite_file(body, self._FILE_NAME)
