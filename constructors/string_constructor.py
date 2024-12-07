from .constuctor_base import Constructor_Base

class String_Data_Constructor(Constructor_Base):
    FILE_NAME = "data/STRINGS.md"
    _FILE_NAME_JSON = "json/strings.json"

    def __init__(self):
        super().__init__()

    def write_json():
        do = "nothing"

    def write_data():
        do = "nothing"
    
    def get_cinematics_lines(self, cinematic_id):
        cine_body = ""

        # cinematics = [key for key in my_dict if key.startswith("cinematic_001")]
        match cinematic_id:
            case "001":
                # first video
                cine_body += "### CINEMATIC: INTRO #1"
                cine_body += f"{self.get_string_by_key("cinematic_001_001")}\n"
                cine_body += f"{self.get_string_by_key("cinematic_001_002")}\n"
                cine_body += f"{self.get_string_by_key("cinematic_001_003")}\n"
                cine_body += f"{self.get_string_by_key("cinematic_001_004")}\n"
                cine_body += f"{self.get_string_by_key("cinematic_001_005")}\n"
                cine_body += f"{self.get_string_by_key("cinematic_001_005b")}\n"
                cine_body += f"{self.get_string_by_key("cinematic_001_006")}\n"
                cine_body += f"{self.get_string_by_key("cinematic_001_007")}\n"

            case "002":
                #second video
                cine_body += "### CINEMATIC: INTRO #2"
                cine_body += f"{self.get_string_by_key("cinematic_002_001")}\n"
                cine_body += f"{self.get_string_by_key("cinematic_002_002")}\n"
                cine_body += f"{self.get_string_by_key("cinematic_002_003")}\n"
                cine_body += f"{self.get_string_by_key("cinematic_002_004")}\n"
                cine_body += f"{self.get_string_by_key("cinematic_002_005")}\n"

            case "007":
                #third video
                cine_body += "### CINEMATIC: NIMBUS"
                cine_body += f"{self.get_string_by_key("cinematic_007_001")}\n"
                cine_body += f"{self.get_string_by_key("cinematic_007_002")}\n"
                cine_body += f"{self.get_string_by_key("cinematic_007_003")}\n"
                cine_body += f"{self.get_string_by_key("cinematic_007_004")}\n"
                cine_body += f"{self.get_string_by_key("cinematic_007_005")}\n"
                cine_body += f"{self.get_string_by_key("cinematic_007_006")}\n"
                cine_body += f"{self.get_string_by_key("cinematic_007_007")}\n"

            case "003":
                #forth video
                cine_body += "### CINEMATIC: TANOCHETLAN"
                cine_body += f"{self.get_string_by_key("cinematic_003_001")}\n"
                cine_body += f"{self.get_string_by_key("cinematic_003_002")}\n"
                cine_body += f"{self.get_string_by_key("cinematic_003_003")}\n"
                cine_body += f"{self.get_string_by_key("cinematic_003_004")}\n"

            case "004":
                #missing video
                cine_body += "### CINEMATIC: VAYGR BETRAYAL"
                cine_body += f"{self.get_string_by_key("cinematic_004_001")}\n"
                cine_body += f"{self.get_string_by_key("cinematic_004_002")}\n"
                cine_body += f"{self.get_string_by_key("cinematic_004_003")}\n"
                cine_body += f"{self.get_string_by_key("cinematic_004_004")}\n"
                cine_body += f"{self.get_string_by_key("cinematic_004_005")}\n"
                cine_body += f"{self.get_string_by_key("cinematic_004_006")}\n"

            case "006":
                # fifth video
                cine_body += "### CINEMATIC: LIGHTHOUSE"
                cine_body += f"{self.get_string_by_key("cinematic_006_001")}\n"
                cine_body += f"{self.get_string_by_key("cinematic_006_002")}\n"
                cine_body += f"{self.get_string_by_key("cinematic_006_003")}\n"
                cine_body += f"{self.get_string_by_key("cinematic_006_004")}\n"
                cine_body += f"{self.get_string_by_key("cinematic_006_005")}\n"
                cine_body += f"{self.get_string_by_key("cinematic_006_006")}\n"
                cine_body += f"{self.get_string_by_key("cinematic_006_007")}\n"

            case "005":
                #sixth video
                cine_body += "### CINEMATIC: VAYGR BETRAYAL"
                cine_body += f"{self.get_string_by_key("cinematic_005_001")}\n"
                cine_body += f"{self.get_string_by_key("cinematic_005_002")}\n"
                cine_body += f"{self.get_string_by_key("cinematic_005_003")}\n"
                cine_body += f"{self.get_string_by_key("cinematic_005_004")}\n"
                cine_body += f"{self.get_string_by_key("cinematic_005_005")}\n"
                cine_body += f"{self.get_string_by_key("cinematic_005_006")}\n"

        return cine_body