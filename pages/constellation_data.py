import constants
import utils
from .base_page import Base_Page

class Constellation_Data_Page(Base_Page):
    _file_name = "STARMAP.md"
    _locator = "#ConstellationData-module"
    
    star_systems = {}
    
    def __init__(self, page):
        super().__init__(page, self._locator)
        self._save_star_systems()
    
    def _save_star_systems(self):
        list_elements_entries = self.page.query_selector_all('.entry')
        print(f"Constellation Data: {len(list_elements_entries)} entries found")

        for element_entry in list_elements_entries:
            faction_el = element_entry.query_selector(constants.LOCATOR_ENTRYITEM_SPECIFIC.format("Name"))
            if faction_el:
                faction = faction_el.inner_text().strip()
            else: 
                entryhead_element = element_entry.query_selector(constants.LOCATOR_ENTRYHEAD)
                faction = entryhead_element.inner_text().strip() if entryhead_element else "Unknown"
            
            if faction in ('tr1_territories', 'tr1_territories_t3', 'tr1_territories_t4', 'tr1_territories_special'):
                faction = "Iyatequa Territories"
            if faction == "P1 Territories":
                faction = "Cangacian Territories"
            if faction == "Tanoch Territories T4":
                faction = "Tanoch Territories"
            if faction == "yaot_territories_t4":
                faction = "Yaot Territories"

            systems_coornames_el = element_entry.query_selector(constants.LOCATOR_ENTRYITEM_SPECIFIC.format("CustomOverrides"))
            if systems_coornames_el:
                systems_coornames = systems_coornames_el.inner_text().strip().replace("name_","")

                for coordinate_name in systems_coornames.split("\n"):
                    if coordinate_name.strip().startswith("["):
                        coordinates, name = coordinate_name.split(':')
                        system = {
                            'name': name,
                            'coordinates': coordinates,
                            'faction': faction
                        }
                        self.star_systems[coordinates] = system
            else:
                voidsystems_coor_el = element_entry.query_selector(constants.LOCATOR_ENTRYITEM_SPECIFIC.format("VoidSystems"))
                systems_coordinates = voidsystems_coor_el.inner_text().strip() if voidsystems_coor_el else "Unknown"

                for coordinates in systems_coordinates.split(":"):
                    system = {
                        'name': "Unknown",
                        'coordinates': coordinates,
                        'faction': faction
                    }
                    self.star_systems[coordinates] = system

    def get_star_system_by_coordinates(self, coordinates):
        system = self.star_systems.get(coordinates)
        if system:
            print(f"{system['faction']}: {system['name']} System")
        else:
            print("Somewhere in Nimbus Galaxy")
        return system
    
    def record_to_file(self):
        utils.rewrite_file("# NIMBUS KNOWNN STAR SYSTEMS\n", self._file_name)
        utils.add_to_file("Systems Finder is working but not all the systems are present in ConstellationData\n\n", self._file_name)

        for coords, system in self.star_systems.items():
            utils.add_to_file(f"{system['faction']} : {system['coordinates']} : {system['name']}\n", self._file_name)