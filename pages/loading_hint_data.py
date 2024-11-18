import utils
import json
import logging
import constants
from .base_page import Base_Page

logger = logging.getLogger(__name__)

class Loading_Hint_Data_Page(Base_Page):
    LOCATOR = "#LoadingHintData-module"
    FILE_NAME = "data/HINTS.md"
    FILE_NAME_JSON = "json/hints.json"

    _hints = []


    def __init__(self, page):
        super().__init__(page, self.LOCATOR)

    def save_data(self):
        for element_entry in self._get_list_elements_entries("Loading Hint Data"):
            hint_header = self._get_entryhead(element_entry)
            self._hints.append(hint_header)

    def write_json(self):
        json_data = json.dumps(self._hints, ensure_ascii=False)
        utils.rewrite_file(json_data, self.FILE_NAME_JSON)
    
    def read_json(self):
        with open(self.FILE_NAME_JSON, 'r', encoding='utf-8') as file:
            json_data = file.read()
        self._hints = json.loads(json_data)
        return self._hints

    def get_hints(self):
        return self._hints
    
    def get_hint(self, hint):
        return hint in self._hints

    def write_data(self):
        body = "# HWM HINTS:\n"
        for hint in self._hints:
            body += f"* {hint}\n"
        utils.rewrite_file(body, self.FILE_NAME)
