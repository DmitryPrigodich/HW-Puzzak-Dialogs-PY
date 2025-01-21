import utils
from .constructor_base import Constructor_Base

import os

class Glossary_Constructor(Constructor_Base):
    _FILE_NAME = "dataset/data/GLOSSARY.md"

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
        body = utils.format_heading1("HWM Glossary")

        for string_key, string_value in self._string_data.items():
            header = ""
            if string_key.startswith("glossary"):
                name_list = string_key.split(".")
                second_part = name_list[1]
                if header != second_part:
                    header = second_part
                    body += utils.format_heading1(header)
               
                body += utils.format_bold({string_key})
                body += utils.format_br(2)
                body += utils.format_paragraph({string_value})
                body += utils.format_br(2)      
        
        utils.add_to_file(body, self._FILE_NAME)
