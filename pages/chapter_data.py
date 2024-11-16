import constants
import utils
from .base_page import Base_Page

class Chapter_Data_Page(Base_Page):
    _file_name = "data/CHAPTERS.md"
    _locator = "#ChapterData-module"

    chapters = []

    def __init__(self, page):
        super().__init__(page, self._locator)
        self._save_chapters()

    def _save_chapters(self):
        list_elements_entries = self.page.query_selector_all('.entry')
        print(f"Chapter Data: {len(list_elements_entries)} entries found")

        for element_entry in list_elements_entries:
            entryhead_el = element_entry.query_selector(constants.LOCATOR_ENTRYHEAD)
            chapter_head = entryhead_el.inner_text().strip().lower() if entryhead_el else "Unknown"

            entryitem_el = element_entry.query_selector(constants.LOCATOR_ENTRYITEM_SPECIFIC.format("Ids"))
            quest_lines = entryitem_el.inner_text().strip() if entryitem_el else "Unknown"

            entryitem_el = element_entry.query_selector(constants.LOCATOR_ENTRYITEM_SPECIFIC.format("Order"))
            order = entryitem_el.inner_text().strip() if entryitem_el else "Unknown"

            chapter = {
                'name': chapter_head,
                'order': order,
                'quest_lines': quest_lines.split("\n")
            }
            self.chapters.append(chapter)

    def record_to_file(self):
        body = "# HWM CHAPTERS:\n\n"
        for chapter in self.chapters:
            body += f"### {chapter['order']}. {chapter['name']}\n"
            n = 0
            for quest_line in chapter['quest_lines']:
                n += 1
                body += f"  {chapter['order']}.{n}. {quest_line}\n"

        utils.rewrite_file(body, self._file_name)
