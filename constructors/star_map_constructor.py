import utils
import json
from itertools import groupby

class Star_Map_Constructor():

    STAR_SYSTEM_DATA_JSON = "json_bak/StarSystemData-module.json"
    CONSTELLATION_DATA_JSON = "json/constellations.json"

    FILE_NAME = "data/STARMAP.md"
    FILE_NAME_JSON = "json/starmap_final.json"

    _constellations = {}
    _star_systems = {}
    _all_systems_map = {}

    def get_systems_from_star_system_data(self):
        self._star_systems = self._read_json(self.STAR_SYSTEM_DATA_JSON)
        for coords, system in self._star_systems.items():
            print(system)
            system_data = {
                'name': system.get('Name:'),
                'faction': self._get_corrected_faction_name(system.get('Faction:'))
            }
            self._all_systems_map[coords] = system_data
    
    def get_systems_from_constellation_data(self):
        self._constellations = self._read_json(self.CONSTELLATION_DATA_JSON)
        for coords, system in self._constellations.items():
            system_data = {
                'name': system.get('name'),
                'faction': self._get_corrected_faction_name(system.get('faction'))
            }
            self._all_systems_map[coords] = system_data


    def _read_json(self, json_file):
        with open(json_file, 'r', encoding='utf-8') as file:
            json_data = file.read()
        json_input = json.loads(json_data)
        return json_input
    
    def write_json(self):
        json_data = json.dumps(self._all_systems_map, ensure_ascii=False)
        utils.rewrite_file(json_data, self.FILE_NAME_JSON)

    def write_data(self):
        body = "# NIMBUS KNOWN STAR SYSTEMS\n"
        # for coords, system in self._all_systems_map.items():
        #     body += f"* {system['faction']} : {system['name']} : {coords}\n"
        # utils.rewrite_file(body, self.FILE_NAME)

        sorted_systems_by_faction = sorted(self._all_systems_map.items(), key=lambda item: item[1]['faction'])
        for faction, group in groupby(sorted_systems_by_faction, key=lambda item: item[1]['faction']):
            body += f"\n## {faction}\n"
            for coords, system in group:
                body += f"* {system['name']} : {coords}\n"
        utils.rewrite_file(body, self.FILE_NAME)


    def _get_corrected_faction_name(self, faction):
        match faction:
            case "Hiigaran Territories" | "Hiigaran":
                return "Medeans"
            case 'Tr1' | 'tr1_territories' | 'tr1_territories_t3' | 'tr1_territories_t4' | 'tr1_territories_special':
                return "Iyatequa"
            case "P1 Territories":
                return "Cangacians"
            case "Tanoch Territories" | "Tanoch Territories T4":
                return "Tanoch"
            case "Yaot Territories" | "yaot_territories_t4":
                return "Yaot"
            case "Amassari Territories":
                return "Amassari"
            case "Clan Territories":
                return "Clans"
            case _:
                return faction
            
    def get_star_system_by_coordinates(self, coordinates):
        star_map = self._read_json(self.FILE_NAME_JSON)
        return star_map.get(coordinates).get('name')