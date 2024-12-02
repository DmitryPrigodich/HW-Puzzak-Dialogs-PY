import utils
import logging
from .base_page import Base_Page

logger = logging.getLogger(__name__)

class Loading_Hint_Data_Page(Base_Page):
    _LOCATOR = "#LoadingHintData-module"
    _FILE_NAME = "data/HINTS.md"
    _FILE_NAME_JSON = "json/hints.json"

    _hints = []

    def __init__(self, page):
        super().__init__(page, self._LOCATOR)

    def save_data(self):
        for element_entry in self._get_list_elements_entries("Loading Hint Data"):
            hint_header = self._get_entryhead(element_entry)
            self._hints.append(hint_header)

    def write_json(self):
        self._write_json(self._hints)
    
    def read_json(self):
        return self._read_json(self._FILE_NAME_JSON)

    def write_data(self):
        body = "# HWM HINTS:\n"
        for hint in self._hints:
            body += f"* {hint}\n"
        utils.rewrite_file(body, self._FILE_NAME)

    def get_hints(self):
        return self._hints
    
    def get_hint(self, hint):
        return hint in self._hints