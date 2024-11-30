import utils
import json
import logging
import constants
from .base_page import Base_Page

logger = logging.getLogger(__name__)

class Quest_Data_Page(Base_Page):
    _LOCATOR = "#QuestData-module"
    _FILE_NAME = "data/QUESTS.md"
    _FILE_NAME_TMP = "data/QUEST_TMP.md"
    _FILE_NAME_JSON = "json/quests.json"

    _quests = []


    def __init__(self, page):
        super().__init__(page, self._LOCATOR)

    def save_data(self):
        for element_entry in self._get_list_elements_entries("Quest Data"):
            quest_header = self._get_entryhead(element_entry)

            quest = {
                'header': quest_header
            }
            self._quests.append(quest)

    def get_tag_values(self, tag):
        final_value_list = []
        tag_value_elements = self.page.query_selector_all(constants.LOCATOR_ENTRYITEM_SPECIFIC.format(tag))
        print(f"Found {len(tag_value_elements)} tags of '{tag}'")

        for tag_value_element in tag_value_elements:
            tag_values = tag_value_element.inner_text().strip() if tag_value_element else "Unknown"
            
            for tag_value in tag_values.split("\n"):
                tag_value = tag_value.replace("_heroic", '')
                tag_value = tag_value.replace("_mythic", '')
                match tag:
                    case "Goals":
                        tag_value = tag_value.split(',')[0]
                        final_value_list.append(tag_value)
                    case "GoalParameters":
                        tag_value = tag_value.replace("&", ':')
                        for tag_value_part in tag_value.split(';'):
                            match tag_value_part.split(':')[0]:
                                case "Amount":
                                    final_value_list.append("Amount")
                                case "Tier":
                                    final_value_list.append("Tier")
                                case "Total":
                                    final_value_list.append("Total")
                                case "MinLevel":
                                    final_value_list.append("MinLevel")
                                case "Tags":
                                    tag_value_part = tag_value_part.replace("_T1", '').replace("_T2", '').replace("_T3", '').replace("_T4", '')
                                    tag_value_part = tag_value_part.replace("_T1up", '').replace("_T2up", '').replace("_T3up", '').replace("_T4up", '')
                                    final_value_list.append(tag_value_part)
                                case "ExcludedSources":
                                    for exSour in tag_value_part.split(':')[1].split('_'):
                                        final_value_list.append(f"ExcludedSources:{exSour}")
                                case _:
                                    final_value_list.append(tag_value_part)
                    case _:
                        final_value_list.append(tag_value)

        final_value_list = sorted(list(set(final_value_list)))
        return final_value_list
    
    def write_tags(self):
        tags = []
        tag_elements = self.page.query_selector_all("//b[@class='entryitemname']")

        for tag_el in tag_elements:
            tag = tag_el.inner_text().strip() if tag_el else "Unknown"
            tags.append(tag.replace(':',''))
        
        tags = sorted(list(set(tags)))
        utils.add_to_file("\n\n# HWM QUEST TAGS:\n", self._FILE_NAME)
        for tag in tags:
            utils.add_to_file(f"{tag}\n", self._FILE_NAME_TMP)
    
    def write_tag_values(self, tag):
        tag_value_list = self.get_tag_values(tag)
        
        body = f"\n# HWM QUEST TAG '{tag}' VALUES:\n"
        for value in tag_value_list:
            body += (f"* {value}\n")
        utils.add_to_file(body, self._FILE_NAME_TMP)
    
    def write_data(self):
        body = "# HWM QUESTS:\n"
        for quest in self._quests:
            body += f"* {quest}\n"
        utils.rewrite_file(body, self._FILE_NAME)