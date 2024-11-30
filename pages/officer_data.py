import utils
import json
from .base_page import Base_Page

class Officer_Data_Page(Base_Page):
    _LOCATOR = "#OfficerData-module"
    _FILE_NAME = "data/OFFICERS.md"
    _FILE_NAME_JSON = "json/officers.json"

    _officers = []

    def __init__(self, page):
        super().__init__(page, self._LOCATOR)

    def save_data(self):
        for element_entry in self._get_list_elements_entries("Officer Data"):
            officer_head = self._get_entryhead(element_entry)
            officer_seed = self._get_entryitem_by_tag(element_entry, "Seed")

            if officer_seed != "Unknown":
                officer_faction = self._get_entryitem_by_tag(element_entry, "Faction")
                officer_jobs = self._get_entryitem_by_tag(element_entry, "Jobs")
                officer_gender = self._get_entryitem_by_tag(element_entry, "Gender")
                officer_fname = self._get_entryitem_by_tag(element_entry, "FirstName")
                officer_lname = self._get_entryitem_by_tag(element_entry, "LastName")
                officer_portrait_id = self._get_entryitem_by_tag(element_entry, "PortraitId")

                officer = {
                    'header': officer_head,
                    'seed': officer_seed,
                    'faction': officer_faction,
                    'jobs': officer_jobs,
                    'gender': officer_gender,
                    'fname': officer_fname,
                    'lname': officer_lname,
                    'portid': officer_portrait_id
                }
                self._officers.append(officer)
        return self._officers

    def write_json(self):
        json_data = json.dumps(self._officers, ensure_ascii=False)
        utils.rewrite_file(json_data, self._FILE_NAME_JSON)
    
    def read_json(self):
        with open(self._FILE_NAME_JSON, 'r', encoding='utf-8') as file:
            json_data = file.read()
        self._officers = json.loads(json_data)
        return self._officers
    
    def get_officers(self):
        return self._officers
    
    def check_officer(self, officer_seed):
        return any(item["seed"] == officer_seed for item in self._officers)


    def write_data(self):
        body = "# HWM OFFICERS:\n"
        for officer in self._officers:
            body += f"\n### {officer['seed']} {officer['header']}\n"
            body += f"* {officer['fname']} {officer['lname']}, {officer['faction']} {officer['jobs']}\n"
        utils.rewrite_file(body, self._FILE_NAME)
