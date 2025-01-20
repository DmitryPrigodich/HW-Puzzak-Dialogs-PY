import utils
from .base_page import Base_Page

class Quest_Line_Data_Page(Base_Page):
    _LOCATOR = "#QuestLineData-module"
    _FILE_NAME = "dataset/data/QUESTSLINES.md"
    _FILE_NAME_JSON = "dataset/json/questlines.json"

    _quest_lines = {}

    def __init__(self, page):
        super().__init__(page, self._LOCATOR)

    def save_data(self):
        for element_entry in self._get_list_elements_entries("Quest Line Data"):
            quest_line_header = self._get_entryhead(element_entry)
            quests = self._get_entryitem_by_tag(element_entry, "QuestIds")

            self._quest_lines[quest_line_header] = quests.split(':')
        return self._quest_lines
    
    def write_json(self):
        self._write_json(self._quest_lines)
    
    def read_json(self):
        return self._read_json(self._FILE_NAME_JSON)

    def write_data(self):
        body = "# HWM QUESTLINES:\n"
        for quest_line, quests in self._quest_lines.items():
            body += f"\n## {quest_line}\n"
            for quest in quests:
                body += f"* {quest}\n"
        utils.rewrite_file(body, self._FILE_NAME)
    
    def get_quest_lines(self):
        return self._quest_lines
    
    def get_quests_by_quest_line(self, quest_line):
        return self._quest_lines[quest_line]