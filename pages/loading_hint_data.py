import constants
import utils
from .base_page import Base_Page

class Loading_Hint_Data_Page(Base_Page):
    _file_name = "data/HINTS.md"
    _locator = "#LoadingHintData-module"

    hints = []

    def __init__(self, page):
        super().__init__(page, self._locator)
        self._save_hints()

    def _save_hints(self):
        list_elements_entries = self.page.query_selector_all('.entry')
        print(f"Loading Hint Data: {len(list_elements_entries)} entries found")

        for element_entry in list_elements_entries:
            entryhead_el = element_entry.query_selector(constants.LOCATOR_ENTRYHEAD)
            hint = entryhead_el.inner_text().strip().lower() if entryhead_el else "Unknown"
            self.hints.append(hint)

    def record_to_file(self):
        body = "# HWM HINTS:\n\n"
        for hint in self.hints:
            body += f"{hint}\n"
        utils.rewrite_file(body, self._file_name)
