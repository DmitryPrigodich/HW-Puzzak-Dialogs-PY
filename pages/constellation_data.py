import utils
import constants
from .base_page import Base_Page

class Constellation_Data_Page(Base_Page):
    _LOCATOR = "#ConstellationData-module"
    _FILE_NAME = "data/CONSTELLATIONS.md"
    _FILE_NAME_JSON = "json/constellations.json"
    
    _star_system_by_coordinates = {}
    
    def __init__(self, page):
        super().__init__(page, self._LOCATOR)
    
    def save_data(self):
        for element_entry in self._get_list_elements_entries("Constellation Data"):
            #get faction
            faction_el = element_entry.query_selector(constants.LOCATOR_ENTRYITEM_SPECIFIC.format("Name"))
            if faction_el:
                faction = faction_el.inner_text().strip()
            else:
                faction = self._get_entryhead(element_entry)
            
            faction = utils.get_corrected_faction_name(faction)

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
    
    def write_json(self):
        self._write_json(self._star_system_by_coordinates)
    
    def read_json(self):
        return self._read_json(self._FILE_NAME_JSON)
        
    def write_data(self):
        body = "# NIMBUS KNOWN STAR SYSTEMS\n"
        body += "Systems Finder is working but not all the systems are present in Constellation Data\n\n"

        for coords, system in self._star_system_by_coordinates.items():
            body += f"* {system['faction']} : {system['name']} : {system['coordinates']}\n"
        utils.rewrite_file(body, self._FILE_NAME)

    def get_star_system_by_coordinates(self, coordinates):
        system = self._star_system_by_coordinates.get(coordinates)
        if system:
            print(f"{system['faction']}: {system['name']} System")
        else:
            print("Location Unknown")
        return system