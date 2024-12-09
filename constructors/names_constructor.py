import utils

from .constructor_base import Constructor_Base

class Name_Data_Constructor(Constructor_Base):
    _NAME_DATA_JSON = "json_bak/OfficerNameData-module.json"
    _FILE_NAME_JSON = "json/names.json"
    _FILE_NAME = "data/NAMES.md"

    _name_data = {}
    _names = {}

    def __init__(self):
        super().__init__()
        self._name_data = utils.read_json(self._NAME_DATA_JSON)
        self._set_data()

    def _set_data(self):
        for faction_key, faction_names_params in self._name_data.items():
            faction = faction_names_params.get("Faction:")
            faction = utils.get_corrected_faction_name(faction)
            self._names[faction] = {
                "Female": faction_names_params.get("FemaleFirst:").split(":"),
                "Male": faction_names_params.get("MaleFirst:").split(":"),
                "Unisex": faction_names_params.get("BothFirst:").split(":"),
                "Family": faction_names_params.get("LastNames:").split(":"),
            }
    
    #it appeared to be more complicated than just update of dictionnaire, so I'll leave it be for now
    def _add_names(self):
        additional_names = {}

        medeans = {
            "Female": ["Kidara","Vashti","Joanna","Kamara","Bela","Esentra","Amaala","Agnes","Elise","Jassiah","Baaekh"],
            "Male": ["Gideon", "Enoch","Eshim","Micah","Ben","Reuben","Pagraan","Mehemit","Thaed","Makhaab","Adrian","Hector","Mahel","Joshua","Hyeaa","Suzaak","Thaanh"],
            "Family": ["Sasan","Matara","LiirHra"]
            }
        iyatequa = {
            "Male": ["Ekekko"]
        }
        tanoch = {
            "Male": ["Cazoma","Heyoka","Tepin"],
            "Female": ["Toci"],
            "Family": ["Tecuban","Chicuat","Citalique"," Papan"]
        }
        yaot = {
            "Male:": ["Guahai","Chaquen","Chocoan"],
            "Family:": ["Sapa","Guecha","Coatl"]
        }
        amassari = {
            "Male": ["Jothru"],
            "Family": ["Sadosar","Nacarid","Shasau","Thant","Ohau","Vareng","Omassi","Alut"]
        }
        vaygr = {
            "Male": ["Jochik"],
            "Family": ["Kaan"]
        }
        cangacians = {
            "Male": ["Supay","Catequil"],
            "Female": [""]
        }
        additional_names = {
            "Hiigaran Medea": medeans,
            "Iyatequa": iyatequa,
            "Cangacians": cangacians,
            "Tanoch": tanoch,
            "Yaot": yaot,
            "Amassari": amassari,
            "Vaygr": vaygr
        }
        return additional_names

    def write_json(self):
        utils.write_json(self._names, self._FILE_NAME_JSON)

    def write_data(self):
        body = "# HWM NAMES:"
        for faction, name_types in self._names.items():
            body += f"\n\n## {faction.upper()}"
            for name_type, names in name_types.items():
                body += f"\n\n### {name_type} Names:\n"
                body += ", ".join(map(str, names))
            body += "\n"

        utils.rewrite_file(body, self._FILE_NAME)