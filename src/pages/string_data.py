import utils
from .base_page import Base_Page

class String_Data_Page(Base_Page):
    _LOCATOR = "#StringData-module"
    _FILE_NAME = "dataset/data/STRINGS.md"
    _FILE_NAME_JSON = "dataset/json/strings.json"

    _strings = {}

    def __init__(self, page):
        super().__init__(page, self._LOCATOR)

    def save_data(self):
        for element_entry in self._get_list_elements_entries("String Data"):
            string_header = self._get_entryhead(element_entry)
            string_text = self._get_entryitem_by_tag(element_entry, "en")

            self._strings[string_header] = string_text

        return self._strings

    def write_json(self):
        self._write_json(self._strings)
    
    def read_json(self):
        return self._read_json(self._FILE_NAME_JSON)

    def write_data(self):
        body = "# HWM STRINGS:\n"
        for string_header, string_text in self._strings.items():
            body += f"* {string_header}: {string_text}\n"
        utils.rewrite_file(body, self._FILE_NAME)

    def get_text_by_header(self, string_header):
        return self._strings.get(string_header)

    # nothing to see here, just tried to sort a raw strings file
    def group_data(self):
        strings_groupped = {
            "Unsorted": []
            ,"Hints": []
            ,"Chapters": []
            ,"Main Quests": []
            ,"Intro Quests": []
            ,"Side Quests": []
            ,"Compensation Quests": []
            ,"Grind Quests": []
            ,"Time Quests": []
            ,"Event Quests": []
            ,"Names": []
            ,"Mission Suffixes": []
            ,"Clan Actions": []
            ,"Mails": []
            ,"Glossary": []
            ,"Resources": []
            ,"Resource Packs": []
            ,"Intermediates": []
            ,"Insignias": []
            ,"Internal Modules": []
            ,"Engine Modules": []
            ,"Turrets": []
            ,"Kiithid Fleet": []
            ,"Kiithless Fleet": []
            ,"Tanoch Fleet": []
            ,"Vaygr Fleet": []
            ,"Amassari Fleet": []
            ,"Keeper Fleet": []
            ,"Iyatequa Fleet": []
            ,"Yaot Fleet": []
            ,"Cangacian Fleet": []
            ,"Kiithid": []
            ,"Skins": []
            ,"Officers": []
            ,"Research": []
            ,"Replayable Quests": []
            ,"Dialogs": []
        }
        
        for string_header, string_text in self._strings.items():
            if string_header.startswith("hint_"):
                string_data = {'head': string_header, 'text': string_text}
                self._strings_groupped['Hints'].append(string_data)
            elif string_header.startswith("chaptername_"):
                string_data = {'head': string_header, 'text': string_text}
                self._strings_groupped['Chapters'].append(string_data)
            elif string_header.startswith("qm_") or string_header.startswith("desc_qm_") or string_header.startswith("chapterdesc_"):
                string_data = {'head': string_header, 'text': string_text}
                self._strings_groupped['Main Quests'].append(string_data)
            elif string_header.startswith("qi_") or string_header.startswith("desc_qi_"):
                string_data = {'head': string_header, 'text': string_text}
                self._strings_groupped['Intro Quests'].append(string_data)
            elif string_header.startswith("qs_") or string_header.startswith("desc_qs_"):
                string_data = {'head': string_header, 'text': string_text}
            elif string_header.startswith("qr_") or string_header.startswith("desc_qr_"):
                string_data = {'head': string_header, 'text': string_text}
                self._strings_groupped['Replayable Quests'].append(string_data)
            elif string_header.startswith("q_compensation_") or string_header.startswith("desc_q_compensation_"):
                string_data = {'head': string_header, 'text': string_text}
                self._strings_groupped['Compensation Quests'].append(string_data)
            elif string_header.startswith("qg_") or string_header.startswith("desc_qg_"):
                string_data = {'head': string_header, 'text': string_text}
                self._strings_groupped['Grind Quests'].append(string_data)
            elif string_header.startswith("qt_") or string_header.startswith("desc_qt_"):
                string_data = {'head': string_header, 'text': string_text}
                self._strings_groupped['Time Quests'].append(string_data)
            elif string_header.startswith("qe_") or string_header.startswith("desc_qe_"):
                string_data = {'head': string_header, 'text': string_text}
                self._strings_groupped['Event Quests'].append(string_data)
            elif string_header.startswith("name_"):
                string_data = {'head': string_header, 'text': string_text}
                self._strings_groupped['Names'].append(string_data)
            elif string_header.startswith("missionsuffix_"):
                string_data = {'head': string_header, 'text': string_text}
                self._strings_groupped['Mission Suffixes'].append(string_data)
            elif string_header.startswith("clan"):
                string_data = {'head': string_header, 'text': string_text}
                self._strings_groupped['Clan Actions'].append(string_data)
            elif string_header.startswith("m_"):
                string_data = {'head': string_header, 'text': string_text}
                self._strings_groupped['Mails'].append(string_data)
            elif string_header.startswith("glossary."):
                string_data = {'head': string_header, 'text': string_text}
                self._strings_groupped['Glossary'].append(string_data)
            elif string_header.startswith("rw_") or string_header.startswith("desc_rw"):
                string_data = {'head': string_header, 'text': string_text}
                self._strings_groupped['Resources'].append(string_data)
            elif string_header.startswith("pack_") or string_header.startswith("desc_pack_"):
                string_data = {'head': string_header, 'text': string_text}
                self._strings_groupped['Resource Packs'].append(string_data)
            elif string_header.startswith("intmed_") or string_header.startswith("desc_intmed_"):
                string_data = {'head': string_header, 'text': string_text}
                self._strings_groupped['Intermediates'].append(string_data)
            elif string_header.startswith("insig_") or string_header.startswith("desc_insig_"):
                string_data = {'head': string_header, 'text': string_text}
                self._strings_groupped['Insignias'].append(string_data)
            elif string_header.startswith("im_") or string_header.startswith("desc_im_"):
                string_data = {'head': string_header, 'text': string_text}
                self._strings_groupped['Internal Modules'].append(string_data)
            elif string_header.startswith("engine_") or string_header.startswith("desc_engine_"):
                string_data = {'head': string_header, 'text': string_text}
                self._strings_groupped['Engine Modules'].append(string_data)
            elif string_header.startswith("turret_") or string_header.startswith("desc_turret_"):
                string_data = {'head': string_header, 'text': string_text}
                self._strings_groupped['Turrets'].append(string_data)
            elif string_header.startswith("hgn_") or string_header.startswith("desc_hgn_"):
                string_data = {'head': string_header, 'text': string_text}
                self._strings_groupped['Kiithid Fleet'].append(string_data)
            elif string_header.startswith("hgd_") or string_header.startswith("desc_hgd_"):
                string_data = {'head': string_header, 'text': string_text}
                self._strings_groupped['Kiithless Fleet'].append(string_data)
            elif string_header.startswith("tan_") or string_header.startswith("desc_tan_"):
                string_data = {'head': string_header, 'text': string_text}
                self._strings_groupped['Tanoch Fleet'].append(string_data)
            elif string_header.startswith("vgr_") or string_header.startswith("desc_tan_"):
                string_data = {'head': string_header, 'text': string_text}
                self._strings_groupped['Vaygr Fleet'].append(string_data)
            elif string_header.startswith("ama_") or string_header.startswith("desc_tan_"):
                string_data = {'head': string_header, 'text': string_text}
                self._strings_groupped['Amassari Fleet'].append(string_data)
            elif string_header.startswith("kpr_") or string_header.startswith("desc_tan_"):
                string_data = {'head': string_header, 'text': string_text}
                self._strings_groupped['Keeper Fleet'].append(string_data)
            elif string_header.startswith("tr1_") or string_header.startswith("desc_tan_"):
                string_data = {'head': string_header, 'text': string_text}
                self._strings_groupped['Iyatequa Fleet'].append(string_data)
            elif string_header.startswith("yao_") or string_header.startswith("desc_yao_"):
                string_data = {'head': string_header, 'text': string_text}
                self._strings_groupped['Yaot Fleet'].append(string_data)
            elif string_header.startswith("p1_") or string_header.startswith("desc_p1_"):
                string_data = {'head': string_header, 'text': string_text}
                self._strings_groupped['Cangacian Fleet'].append(string_data)
            elif string_header.startswith("kiith") or string_header.startswith("desc_kiith"):
                string_data = {'head': string_header, 'text': string_text}
                self._strings_groupped['Kiithid'].append(string_data)
            elif string_header.startswith("c_") or string_header.startswith("desc_c_"):
                string_data = {'head': string_header, 'text': string_text}
                self._strings_groupped['Skins'].append(string_data)
            elif string_header.startswith("officer_") or string_header.startswith("desc_officer_"):
                string_data = {'head': string_header, 'text': string_text}
                self._strings_groupped['Officers'].append(string_data)
            elif string_header.startswith("rp_") or string_header.startswith("desc_rp_"):
                string_data = {'head': string_header, 'text': string_text}
                self._strings_groupped['Research'].append(string_data)
            elif string_header.startswith("dia_"):
                string_data = {'head': string_header, 'text': string_text}
                self._strings_groupped['Dialogs'].append(string_data)
            else:
                string_data = {'head': string_header, 'text': string_text}
                self._strings_groupped["Unsorted"].append(string_data)