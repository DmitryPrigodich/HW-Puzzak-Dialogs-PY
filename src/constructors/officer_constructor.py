import utils

from itertools import groupby

from .constructor_base import Constructor_Base

class Officer_Data_Constructor(Constructor_Base):
    _OFFICER_DATA_JSON = "dataset/json_bak/OfficerData-module.json"
    _FILE_NAME = "dataset/data/OFFICERS.md"
    _FILE_NAME_JSON = "dataset/json/officers.json"

    _officer_data = {}
    _officers = {}

    def __init__(self):
        super().__init__()
        self._officer_data = utils.read_json(self._OFFICER_DATA_JSON)
        self._set_data()

    def _set_data(self):
        for officer_key, officer_params in self._officer_data.items():
            if all(k in officer_params for k in ["Seed:", "Faction:"]):
                self._officers[officer_key] = {
                    "Seed:": officer_params.get("Seed:"),
                    "FirstName:": officer_params.get("FirstName:"),
                    "LastName:": officer_params.get("LastName:"),
                    "Gender:": officer_params.get("Gender:"),
                    "PortraitId:": officer_params.get("PortraitId:"),
                    "Jobs:": officer_params.get("Jobs:"),
                    "Faction:": officer_params.get("Faction:", "None")
                }
    
    def get_data(self):
        return self._officers
    
    def write_json(self):
        utils.write_json(self._officers, self._FILE_NAME_JSON)

    def write_data(self):
        body = "# HWM OFFICERS:\n\n"

        sorted_officers_by_faction = sorted(self._officers.items(), key=lambda item: item[1]['Faction:'])
        for faction, of_params in groupby(sorted_officers_by_faction, key=lambda item: item[1]['Faction:']):
            body += f"## {faction}\n".upper()
            
            for of_key, of_params in of_params:
                of_seed = of_params.get('Seed:')
                of_fname = of_params.get('FirstName:')
                of_lname = of_params.get('LastName:')
                of_gender = of_params.get('Gender:')
                of_portrait = of_params.get('PortraitId:')
                of_jobs = of_params.get('Jobs:')

                body += f"### {of_fname} {of_lname}\n"
                body += f"* Gender: {of_gender}\n"
                body += f"* Jobs: {of_jobs}\n"
                body += f"* Seed: {of_seed}\n"
                body += f"* Key: {of_key}\n"
                body += f"* PortraitId: {of_portrait}\n"
                body += "\n"

        utils.rewrite_file(body, self._FILE_NAME)


