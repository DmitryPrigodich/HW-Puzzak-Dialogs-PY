import utils
from .base_page import Base_Page

class Mission_Data_Page(Base_Page):
    _LOCATOR = "#MissionData-module"
    _FILE_NAME = "dataset/data/MISSIONS.md"
    _FILE_NAME_JSON = "dataset/json/missions.json"

    _missions = []

    def __init__(self, page):
        super().__init__(page, self._LOCATOR)

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
        self._write_json(self._missions)
    
    def read_json(self):
        return self._read_json(self._FILE_NAME_JSON)

    def write_data(self):
        body = "# HWM MISSIONS:\n"
        for mission in self._missions:
            body += f"* {mission['header']} : {mission['mode']}\n"
        utils.rewrite_file(body, self._FILE_NAME)

    def get_missions(self):
        return self._missions

