import utils
from itertools import groupby

class Star_Map_Constructor():
    _STAR_SYSTEM_DATA_JSON = "json_bak/StarSystemData-module.json"
    _CONSTELLATION_DATA_JSON = "json_bak/ConstellationData-module.json"

    _FILE_NAME = "data/STARMAP.md"
    _FILE_NAME_JSON = "json/starmap.json"

    _constellation_data = {}
    _star_system_data = {}
    _star_map = {}

    def __init__(self):
        self._star_system_data = utils.read_json(self._STAR_SYSTEM_DATA_JSON)
        self._constellation_data = utils.read_json(self._CONSTELLATION_DATA_JSON)
        self._set_data()

    def _set_data(self):
        for key, values in self._constellation_data.items():
            faction_weights = values.get("FactionWeights:").split(":")[0]
            faction = utils.get_corrected_faction_name(faction_weights)

            if "CustomOverrides:" in values:
                for map_data in values.get("CustomOverrides:").split("\n"):
                    if map_data.startswith("name_"):
                        system_data = map_data.replace("name_","").split(":")
                        coordinates = system_data[0]
                        name = system_data[1]

                        self._star_map[coordinates] = {
                            'Name:': name,
                            'Faction:': faction
                        }
            else:
                for coords in values.get("VoidSystems:").split(":"):
                    coordinates = coords
                    name = "Unknown"

                    self._star_map[coordinates] = {
                        'Name:': name,
                        'Faction:': faction
                    }

        for coords, system in self._star_system_data.items():
            faction_weights = system.get('Faction:')
            faction = utils.get_corrected_faction_name(faction_weights)

            coordinates = coords
            name = system.get('Name:')

            self._star_map[coordinates] = {
                'Name:': name,
                'Faction:': faction
            }
    
    def write_json(self):
        utils.write_json(self._star_map,self._FILE_NAME_JSON)

    def write_data(self):
        body = "# HWM NIMBUS GALAXY KNOWN STAR SYSTEMS\n"
        sorted_systems_by_faction = sorted(self._star_map.items(), key=lambda item: item[1]['Faction:'])
        for faction, group in groupby(sorted_systems_by_faction, key=lambda item: item[1]['Faction:']):
            body += f"\n## {faction}\n"
            for coords, system in group:
                body += f"* {system['Name:']} : {coords}\n"
        utils.rewrite_file(body, self._FILE_NAME)
            
    def get_star_system_by_coordinates(self, coordinates):
        return self._star_map.get(coordinates)
