import utils
import json
import logging
import constants
from .base_page import Base_Page

logger = logging.getLogger(__name__)

class Quest_Line_Data_Page(Base_Page):
    FILE_NAME = "data/QUESTSLINES.md"
    _locator = "#QuestLineData-module"

    quests = []
    quest_lines = []
    quests_lined = {}
    lines_quests = {}

    def __init__(self, page):
        super().__init__(page, self._locator)

    def save_data(self):
        for element_entry in self._get_list_elements_entries("Quest Line Data"):
            quest_line_header = self._get_entryhead(element_entry)
            quests = self._get_entryitem_by_tag(element_entry, "QuestIds")

            quest_line = {
                'header': quest_line_header,
                'quests': quests.split(':')
            }
        return quest_line

    def get_quests_by_quest_line(self, quest_line):
        quests = self.quests_lined.get(quest_line.lower())
        
        if quests:
            print(f"Quest Line: {quest_line}\n")
            for quest in quests:
                print(f"  * {quest}\n")

        return quests
    
    def get_quest_line_by_event(self, event):
        return "ql_" + event
    
    def get_quests_by_event(self, event):
        quest_line = self.get_quest_line_by_event(event)
        print(f"QL: {quest_line}")
        return self.get_quests_by_quest_line(quest_line)
    
    def get_quest_line_by_quest(self, quest):
        quest_line = self.lines_quests[quest]
        self.get_quests_by_quest_line(quest_line)
        return quest_line

    def record_to_file(self):
        body = "# HWM QUESTLINES:\n\n"
        for questline in self.quest_lines:
            body += f"* {questline}\n"

        body += "\n\n# HWM QUESTS:\n\n"
        for questline, quests in self.quests_lined.items():
            body += f"\n## {questline}\n"
            for quest in sorted(quests):
                body += f"* {quest}\n"
        
        utils.rewrite_file(body, self.FILE_NAME)