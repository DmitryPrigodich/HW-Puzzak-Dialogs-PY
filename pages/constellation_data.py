import constants
import utils
from .base_page import Base_Page

class Constellation_Data_Page(Base_Page):
    _file_name = "STARMAP.md"
    _locator = "#ConstellationData-module"
    
    star_systems_by_coordinates = {}
    star_systems_by_faction = {}
    
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
                faction = "Iyatequa"
            if faction == "P1 Territories":
                faction = "Cangacians"
            if faction in ("Tanoch Territories", "Tanoch Territories T4"): 
                faction = "Tanoch Empire"
            if faction in ("Yaot Territories", "yaot_territories_t4"):
                faction = "Yaot Federation"
            if faction in ("Hiigaran Territories"):
                faction = "Medea"
            if faction in ("Amassari Territories"):
                faction = "Amassari"
            if faction in ("Clan Territories"):
                faction = "Clans"

            if faction not in self.star_systems_by_faction:
                self.star_systems_by_faction[faction] = []

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
                        self.star_systems_by_coordinates[coordinates] = system
                        self.star_systems_by_faction[faction].append(system.get('name'))
            else:
                voidsystems_coor_el = element_entry.query_selector(constants.LOCATOR_ENTRYITEM_SPECIFIC.format("VoidSystems"))
                systems_coordinates = voidsystems_coor_el.inner_text().strip() if voidsystems_coor_el else "Unknown"

                for coordinates in systems_coordinates.split(":"):
                    system = {
                        'name': "Unknown",
                        'coordinates': coordinates,
                        'faction': faction
                    }
                    self.star_systems_by_coordinates[coordinates] = system
                    self.star_systems_by_faction[faction].append(system.get('name'))

    def get_star_system_by_coordinates(self, coordinates):
        system = self.star_systems_by_coordinates.get(coordinates)
        if system:
            print(f"{system['faction']}: {system['name']} System")
        else:
            print("Somewhere in Nimbus Galaxy")
        return system
    
    def get_star_systems_by_faction(self, faction):
        systems = self.star_systems_by_faction.get(faction)
        if systems:
            print(f"Systems of {faction}:")
            for system in systems:
                print(f"{system},")
        else:
            print(f"Faction {faction} has no systems in Nimbus Galaxy")
        return systems
    
    def record_to_file(self):
        utils.rewrite_file("# NIMBUS KNOWNN STAR SYSTEMS\n", self._file_name)
        utils.add_to_file("Systems Finder is working but not all the systems are present in ConstellationData\n\n", self._file_name)

        for coords, system in self.star_systems_by_coordinates.items():
            utils.add_to_file(f"{system['faction']} : {system['coordinates']} : {system['name']}\n", self._file_name)