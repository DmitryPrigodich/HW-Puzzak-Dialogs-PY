import utils
import json
import logging
import constants
from .base_page import Base_Page

logger = logging.getLogger(__name__)

class Mission_Data_Page(Base_Page):
    LOCATOR = "#MissionData-module"
    FILE_NAME = "data/MISSIONS.md"
    FILE_NAME_JSON = "json/missions.json"

    _missions = []

    def __init__(self, page):
        super().__init__(page, self.LOCATOR)

    def save_data(self):
        for element_entry in self._get_list_elements_entries("Mission Data"):
            mission_head = self._get_entryhead(element_entry)
            mode = self._get_entryitem_by_tag(element_entry, "Mode")

            mission = {
                'header': mission_head,
                'mode': mode
            }
            self._missions.append(mission)

    def write_json(self):
        json_data = json.dumps(self._missions, ensure_ascii=False)
        utils.rewrite_file(json_data, self.FILE_NAME_JSON)
    
    def read_json(self):
        with open(self.FILE_NAME_JSON, 'r', encoding='utf-8') as file:
            json_data = file.read()
        logger.log(json_data)
        self._missions = json.loads(json_data)
        logger.log(self._missions)
        return self._missions

    def get_missions(self):
        return self._missions

    def write_data(self):
        body = "# HWM MISSIONS:\n"
        for mission in self._missions:
            body += f"* {mission['header']} : {mission['mode']}\n"
        utils.rewrite_file(body, self.FILE_NAME)

