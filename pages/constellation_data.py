import utils
import json
import constants
from .base_page import Base_Page

class Constellation_Data_Page(Base_Page):
    LOCATOR = "#ConstellationData-module"
    FILE_NAME = "data/CONSTELLATIONS.md"
    FILE_NAME_JSON = "json/constellations.json"
    
    _star_system_by_coordinates = {}
    
    def __init__(self, page):
        super().__init__(page, self.LOCATOR)
    
    def save_data(self):
        for element_entry in self._get_list_elements_entries("Constellation Data"):
            #get faction
            faction_el = element_entry.query_selector(constants.LOCATOR_ENTRYITEM_SPECIFIC.format("Name"))
            if faction_el:
                faction = faction_el.inner_text().strip()
            else:
                faction = self._get_entryhead(element_entry)
            
            faction = self._get_corrected_faction_name(faction)

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
        json_data = json.dumps(self._star_system_by_coordinates, ensure_ascii=False)
        utils.rewrite_file(json_data, self.FILE_NAME_JSON)
    
    def read_json(self):
        with open(self.FILE_NAME_JSON, 'r', encoding='utf-8') as file:
            json_data = file.read()
        self._star_system_by_coordinates = json.loads(json_data)
        return self._star_system_by_coordinates
    
    def get_star_system_by_coordinates(self, coordinates):
        system = self._star_system_by_coordinates.get(coordinates)
        if system:
            print(f"{system['faction']}: {system['name']} System")
        else:
            print("Location Unknown")
        return system
    
    def write_data(self):
        body = "# NIMBUS KNOWN STAR SYSTEMS\n"
        body += "Systems Finder is working but not all the systems are present in Constellation Data\n\n"

        for coords, system in self._star_system_by_coordinates.items():
            body += f"* {system['faction']} : {system['name']} : {system['coordinates']}\n"
        utils.rewrite_file(body, self.FILE_NAME)

    def _get_corrected_faction_name(self, faction):
        match faction:
            case "Hiigaran Territories":
                return "Medeans"
            case 'tr1_territories' | 'tr1_territories_t3' | 'tr1_territories_t4' | 'tr1_territories_special':
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
                return "Terra Incognita"