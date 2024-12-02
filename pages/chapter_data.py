import utils
from .base_page import Base_Page

class Chapter_Data_Page(Base_Page):
    _LOCATOR = "#ChapterData-module"
    _FILE_NAME = "data/CHAPTERS.md"
    _FILE_NAME_JSON = "json/chapters.json"

    _chapters = []

    def __init__(self, page):
        super().__init__(page, self._LOCATOR)

    def save_data(self):
        for element_entry in self._get_list_elements_entries("Chapter Data"):
            chapter_head = self._get_entryhead(element_entry)
            quest_lines = self._get_entryitem_by_tag(element_entry, "Ids")
            order = self._get_entryitem_by_tag(element_entry, "Order")

            chapter = {
                'header': chapter_head,
                'order': order,
                'quest_lines': quest_lines.split("\n")
            }
            self._chapters.append(chapter)
        return self._chapters

    def write_json(self):
        self._write_json(self._chapters)
    
    def read_json(self):
        return self._read_json(self._FILE_NAME_JSON)
    
    def write_data(self):
        body = "# HWM CHAPTERS:\n"
        for chapter in self._chapters:
            body += f"### {chapter['order']}. {chapter['header']}\n"
            n = 0
            for quest_line in chapter['quest_lines']:
                n += 1
                body += f"* {chapter['order']}.{n}. {quest_line}\n"

        utils.rewrite_file(body, self._FILE_NAME)

    def get_chapters(self):
        return self._chapters
    
    def check_chapter(self, chapter):
        return any(item["header"] == chapter for item in self._chapters)
