import utils
import json
import logging
from .base_page import Base_Page

logger = logging.getLogger(__name__)

class Quest_Line_Data_Page(Base_Page):
    LOCATOR = "#QuestLineData-module"
    FILE_NAME = "data/QUESTSLINES.md"
    FILE_NAME_JSON = "json/questlines.json"

    _quest_lines = {}

    def __init__(self, page):
        super().__init__(page, self.LOCATOR)

    def save_data(self):
        for element_entry in self._get_list_elements_entries("Quest Line Data"):
            quest_line_header = self._get_entryhead(element_entry)
            quests = self._get_entryitem_by_tag(element_entry, "QuestIds")

            self._quest_lines[quest_line_header] = quests.split(':')
        return self._quest_lines
    
    def write_json(self):
        json_data = json.dumps(self._quest_lines, ensure_ascii=False)
        utils.rewrite_file(json_data, self.FILE_NAME_JSON)
    
    def read_json(self):
        with open(self.FILE_NAME_JSON, 'r', encoding='utf-8') as file:
            json_data = file.read()
        self._quest_lines = json.loads(json_data)
        return self._quest_lines

    def get_quest_lines(self):
        return self._quest_lines
    
    def get_quests_by_quest_line(self, quest_line):
        return self._quest_lines[quest_line]

    def write_data(self):
        body = "# HWM QUESTLINES:\n"
        for quest_line, quests in self._quest_lines.items():
            body += f"\n## {quest_line}\n"
            for quest in quests:
                body += f"* {quest}\n"
        utils.rewrite_file(body, self.FILE_NAME)