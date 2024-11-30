import utils
import json
from itertools import groupby

class Star_Map_Constructor():
    _STAR_SYSTEM_DATA_JSON = "json_bak/StarSystemData-module.json"
    _CONSTELLATION_DATA_JSON = "json/constellations.json"

    FILE_NAME = "data/STARMAP.md"
    FILE_NAME_JSON = "json/starmap_final.json"

    _constellations = {}
    _star_systems = {}
    _all_systems_map = {}

    def set_star_map(self):
        self._star_systems = self._read_json(self._STAR_SYSTEM_DATA_JSON)
        for coords, system in self._star_systems.items():
            print(system)
            system_data = {
                'name': system.get('Name:'),
                'faction': utils.get_corrected_faction_name(system.get('Faction:'))
            }
            self._all_systems_map[coords] = system_data

        self._constellations = self._read_json(self._CONSTELLATION_DATA_JSON)
        for coords, system in self._constellations.items():
            system_data = {
                'name': system.get('name'),
                'faction': utils.get_corrected_faction_name(system.get('Faction:'))
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
            
    def get_star_system_by_coordinates(self, coordinates):
        star_map = self._read_json(self.FILE_NAME_JSON)
        return star_map.get(coordinates).get('name')