import utils
from itertools import groupby
from .constuctor_base import Constructor_Base

class Star_Map_Constructor(Constructor_Base):
    _STAR_SYSTEM_DATA_JSON = "json_bak/StarSystemData-module.json"
    _CONSTELLATION_DATA_JSON = "json_bak/ConstellationData-module.json"

    FILE_NAME = "data/STARMAP.md"
    FILE_NAME_JSON = "json/starmap_final.json"

    _constellation_data = {}
    _star_system_data = {}

    _constellations = {}
    _star_map = {}

    def __init__(self):
        self._star_system_data = self._read_json(self._STAR_SYSTEM_DATA_JSON)
        self._constellation_data = self._read_json(self._CONSTELLATION_DATA_JSON)
        self._set_star_map()

    def _set_star_map(self):
        for map in [self._star_system_data, self._constellation_data]:
            for coords, system in map.items():
                print(system)
                system_data = {
                    'name': system.get('Name:'),
                    'faction': utils.get_corrected_faction_name(system.get('Faction:'))
                }
                self._star_map[coords] = system_data
    
    def write_json(self):
        self._write_json(self._star_map)

    def write_data(self):
        body = "# HWM NIMBUS GALAXY KNOWN STAR SYSTEMS\n"

        sorted_systems_by_faction = sorted(self._star_map.items(), key=lambda item: item[1]['faction'])
        for faction, group in groupby(sorted_systems_by_faction, key=lambda item: item[1]['faction']):
            body += f"\n## {faction}\n"
            for coords, system in group:
                body += f"* {system['name']} : {coords}\n"
        utils.rewrite_file(body, self.FILE_NAME)
            
    def get_star_system_by_coordinates(self, coordinates):
        return self._star_map.get(coordinates).get('name')
    
    def save_constellations (self):
        for key, values in self._constellation_data.items():
            faction = values.get("FactionWeights:").split(":")[0]
            
            for map_data in values.get("CustomOverrides:").split("\n"):
                if map_data.startswith("name_"):
                    coords = map_data.replace("name_").split(":")[0]
                    name = map_data.replace("name_").split(":")[1]

                    self._constellations[coords] = {
                        'Name:': name,
                        'Faction': utils.get_corrected_faction_name(faction)
                    }

        for element_entry in self._get_list_elements_entries("Constellation Data"):

            #get system
            systems_coornames_el = element_entry.query_selector(constants.LOCATOR_ENTRYITEM_SPECIFIC.format("CustomOverrides"))
            if systems_coornames_el:
                systems_coornames = systems_coornames_el.inner_text().strip().replace("name_","")
                for coordinate_name in systems_coornames.split("\n"):
                    if coordinate_name.strip().startswith("["):
                        coordinates, name = coordinate_name.split(':')
                        star_system = {
                            'name': name,
                            'coordinates': coordinates,
                            'faction': faction
                        }
                        self._star_system_by_coordinates[coordinates] = star_system
            else:
                systems_coordinates = self._get_entryitem_by_tag(element_entry, "VoidSystems")
                for coordinates in systems_coordinates.split(":"):
                    star_system = {
                        'name': "Unknown",
                        'coordinates': coordinates,
                        'faction': faction
                    }
                    self._star_system_by_coordinates[coordinates] = star_system