import constants
import utils
from .base_page import Base_Page

class Quest_Line_Data_Page(Base_Page):
    _file_name = "QUESTSLINES.md"

    quests = []
    quest_lines = []
    quests_lined = {}
    lines_quests = {}

    def __init__(self, page):
        super().__init__(page)

    def open(self):
        self.page.click(constants.LOCATOR_QUESTLINEDATA)
        assert self.page.wait_for_selector("#entries > div:nth-child(1)")

    def save_quest_lines(self):
        list_elements_entries = self.page.query_selector_all('.entry')
        print(f"Quest Lines: {len(list_elements_entries)} entries found")

        for element_entry in list_elements_entries:
            entryhead_el = element_entry.query_selector(constants.LOCATOR_ENTRYHEAD)
            quest_line = entryhead_el.inner_text().strip().lower() if entryhead_el else "Unknown"

            entryitem_el = element_entry.query_selector(constants.LOCATOR_ENTRYITEM_SPECIFIC.format("QuestIds"))
            quests = entryitem_el.inner_text().strip() if entryitem_el else "Unknown"

            self.quest_lines.append(quest_line)
            if quest_line not in self.quests_lined:
                self.quests_lined[quest_line] = []
            
            for quest in quests.split(':'):
                self.quests.append(quest.strip())
                self.lines_quests[quest] = quest_line
                self.quests_lined[quest_line].append(quest)          

        self.quests = sorted(self.quests)
        self.quest_lines = sorted(self.quest_lines)
        self.quests_lined = {key: self.quests_lined[key] for key in sorted(self.quests_lined.keys())}

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

    def output_questlines(self):
        utils.rewrite_file("# HWM QUESTLINES:\n\n", self._file_name)
        for questline in self.quest_lines:
            utils.add_to_file(f"* {questline}\n", self._file_name)

        utils.add_to_file("\n\n", self._file_name)

        utils.add_to_file("# HWM QUESTS:\n\n", self._file_name)
        for questline, quests in self.quests_lined.items():
            utils.add_to_file(f"\n## {questline}\n", self._file_name)
            for quest in sorted(quests):
                utils.add_to_file(f"* {quest}\n", self._file_name)