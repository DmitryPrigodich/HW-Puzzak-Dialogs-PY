import constants
import utils
from .base_page import Base_Page

class String_Data_Page(Base_Page):
    _file_name = "STRINGS.md"
    _locator = "#StringData-module"

    strings = {}

    def __init__(self, page):
        super().__init__(page, self._locator)
        self._save_strings()

    def _save_strings(self):
        list_elements_entries = self.page.query_selector_all('.entry')
        print(f"String Data: {len(list_elements_entries)} entries found")

        for element_entry in list_elements_entries:
            entryhead_el = element_entry.query_selector(constants.LOCATOR_ENTRYHEAD)
            string_header = entryhead_el.inner_text().strip().lower() if entryhead_el else "Unknown"

            entryitem_el = element_entry.query_selector(constants.LOCATOR_ENTRYITEM_SPECIFIC.format("en"))
            string_text = entryitem_el.inner_text().strip() if entryitem_el else "Unknown"

            self.strings[string_header] = string_text

    def get_text_by_header(self, header):
        return self.strings.get(header)
    
    def record_to_file(self):
        body = "# HWM STRINGS:\n\n"
        for str_header, str_text in self.strings.items():
            body += f"* {str_header}: {str_text}\n"
        utils.rewrite_file(body, self._file_name)