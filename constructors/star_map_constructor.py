import utils
from itertools import groupby
from .constuctor_base import Constructor_Base

class Star_Map_Constructor(Constructor_Base):
    _STAR_SYSTEM_DATA_JSON = "json_bak/StarSystemData-module.json"
    _CONSTELLATION_DATA_JSON = "json/constellations.json"

    FILE_NAME = "data/STARMAP.md"
    FILE_NAME_JSON = "json/starmap_final.json"

    _constellations = {}
    _star_systems = {}
    _all_systems_map = {}

    def __init__(self):
        self._star_systems = self._read_json(self._STAR_SYSTEM_DATA_JSON)
        self._constellations = self._read_json(self._CONSTELLATION_DATA_JSON)
        self._set_star_map()

    def _set_star_map(self):
        for map in [self._star_systems, self._constellations]:
            for coords, system in map.items():
                print(system)
                system_data = {
                    'name': system.get('Name:'),
                    'faction': utils.get_corrected_faction_name(system.get('Faction:'))
                }
                self._all_systems_map[coords] = system_data
    
    def write_json(self):
        self._write_json(self._all_systems_map)

    def write_data(self):
        body = "# NIMBUS KNOWN STAR SYSTEMS\n"

        sorted_systems_by_faction = sorted(self._all_systems_map.items(), key=lambda item: item[1]['faction'])
        for faction, group in groupby(sorted_systems_by_faction, key=lambda item: item[1]['faction']):
            body += f"\n## {faction}\n"
            for coords, system in group:
                body += f"* {system['name']} : {coords}\n"
        utils.rewrite_file(body, self.FILE_NAME)
            
    def get_star_system_by_coordinates(self, coordinates):
        return self._all_systems_map.get(coordinates).get('name')