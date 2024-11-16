import constants
import utils
from .base_page import Base_Page

class String_Data_Page(Base_Page):
    _file_name = "data/STRINGS.md"
    _locator = "#StringData-module"

    strings = {}
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

    def __init__(self, page):
        super().__init__(page, self._locator)
        self._save_strings()

    def _save_strings(self):
        list_elements_entries = self.page.query_selector_all('.entry')
        print(f"String Data: {len(list_elements_entries)} entries found")

        for element_entry in list_elements_entries:
            entryhead_el = element_entry.query_selector(constants.LOCATOR_ENTRYHEAD)
            string_header = entryhead_el.inner_text().strip().lower() if entryhead_el else "Unknown"

            entryitem_el = element_entry.query_selector(constants.LOCATOR_ENTRYITEM_SPECIFIC.format("en"))
            string_text = entryitem_el.inner_text().strip() if entryitem_el else "Unknown"

            self.strings[string_header] = string_text

            if string_header.startswith("hint_"):
                string_data = {'head': string_header, 'text': string_text}
                self.strings_groupped['Hints'].append(string_data)
            elif string_header.startswith("chaptername_"):
                string_data = {'head': string_header, 'text': string_text}
                self.strings_groupped['Chapters'].append(string_data)
            elif string_header.startswith("qm_") or string_header.startswith("desc_qm_") or string_header.startswith("chapterdesc_"):
                string_data = {'head': string_header, 'text': string_text}
                self.strings_groupped['Main Quests'].append(string_data)
            elif string_header.startswith("qi_") or string_header.startswith("desc_qi_"):
                string_data = {'head': string_header, 'text': string_text}
                self.strings_groupped['Intro Quests'].append(string_data)
            elif string_header.startswith("qs_") or string_header.startswith("desc_qs_"):
                string_data = {'head': string_header, 'text': string_text}
            elif string_header.startswith("qr_") or string_header.startswith("desc_qr_"):
                string_data = {'head': string_header, 'text': string_text}
                self.strings_groupped['Replayable Quests'].append(string_data)
            elif string_header.startswith("q_compensation_") or string_header.startswith("desc_q_compensation_"):
                string_data = {'head': string_header, 'text': string_text}
                self.strings_groupped['Compensation Quests'].append(string_data)
            elif string_header.startswith("qg_") or string_header.startswith("desc_qg_"):
                string_data = {'head': string_header, 'text': string_text}
                self.strings_groupped['Grind Quests'].append(string_data)
            elif string_header.startswith("qt_") or string_header.startswith("desc_qt_"):
                string_data = {'head': string_header, 'text': string_text}
                self.strings_groupped['Time Quests'].append(string_data)
            elif string_header.startswith("qe_") or string_header.startswith("desc_qe_"):
                string_data = {'head': string_header, 'text': string_text}
                self.strings_groupped['Event Quests'].append(string_data)
            elif string_header.startswith("name_"):
                string_data = {'head': string_header, 'text': string_text}
                self.strings_groupped['Names'].append(string_data)
            elif string_header.startswith("missionsuffix_"):
                string_data = {'head': string_header, 'text': string_text}
                self.strings_groupped['Mission Suffixes'].append(string_data)
            elif string_header.startswith("clan"):
                string_data = {'head': string_header, 'text': string_text}
                self.strings_groupped['Clan Actions'].append(string_data)
            elif string_header.startswith("m_"):
                string_data = {'head': string_header, 'text': string_text}
                self.strings_groupped['Mails'].append(string_data)
            elif string_header.startswith("glossary."):
                string_data = {'head': string_header, 'text': string_text}
                self.strings_groupped['Glossary'].append(string_data)
            elif string_header.startswith("rw_") or string_header.startswith("desc_rw"):
                string_data = {'head': string_header, 'text': string_text}
                self.strings_groupped['Resources'].append(string_data)
            elif string_header.startswith("pack_") or string_header.startswith("desc_pack_"):
                string_data = {'head': string_header, 'text': string_text}
                self.strings_groupped['Resource Packs'].append(string_data)
            elif string_header.startswith("intmed_") or string_header.startswith("desc_intmed_"):
                string_data = {'head': string_header, 'text': string_text}
                self.strings_groupped['Intermediates'].append(string_data)
            elif string_header.startswith("insig_") or string_header.startswith("desc_insig_"):
                string_data = {'head': string_header, 'text': string_text}
                self.strings_groupped['Insignias'].append(string_data)
            elif string_header.startswith("im_") or string_header.startswith("desc_im_"):
                string_data = {'head': string_header, 'text': string_text}
                self.strings_groupped['Internal Modules'].append(string_data)
            elif string_header.startswith("engine_") or string_header.startswith("desc_engine_"):
                string_data = {'head': string_header, 'text': string_text}
                self.strings_groupped['Engine Modules'].append(string_data)
            elif string_header.startswith("turret_") or string_header.startswith("desc_turret_"):
                string_data = {'head': string_header, 'text': string_text}
                self.strings_groupped['Turrets'].append(string_data)
            elif string_header.startswith("hgn_") or string_header.startswith("desc_hgn_"):
                string_data = {'head': string_header, 'text': string_text}
                self.strings_groupped['Kiithid Fleet'].append(string_data)
            elif string_header.startswith("hgd_") or string_header.startswith("desc_hgd_"):
                string_data = {'head': string_header, 'text': string_text}
                self.strings_groupped['Kiithless Fleet'].append(string_data)
            elif string_header.startswith("tan_") or string_header.startswith("desc_tan_"):
                string_data = {'head': string_header, 'text': string_text}
                self.strings_groupped['Tanoch Fleet'].append(string_data)
            elif string_header.startswith("vgr_") or string_header.startswith("desc_tan_"):
                string_data = {'head': string_header, 'text': string_text}
                self.strings_groupped['Vaygr Fleet'].append(string_data)
            elif string_header.startswith("ama_") or string_header.startswith("desc_tan_"):
                string_data = {'head': string_header, 'text': string_text}
                self.strings_groupped['Amassari Fleet'].append(string_data)
            elif string_header.startswith("kpr_") or string_header.startswith("desc_tan_"):
                string_data = {'head': string_header, 'text': string_text}
                self.strings_groupped['Keeper Fleet'].append(string_data)
            elif string_header.startswith("tr1_") or string_header.startswith("desc_tan_"):
                string_data = {'head': string_header, 'text': string_text}
                self.strings_groupped['Iyatequa Fleet'].append(string_data)
            elif string_header.startswith("yao_") or string_header.startswith("desc_yao_"):
                string_data = {'head': string_header, 'text': string_text}
                self.strings_groupped['Yaot Fleet'].append(string_data)
            elif string_header.startswith("p1_") or string_header.startswith("desc_p1_"):
                string_data = {'head': string_header, 'text': string_text}
                self.strings_groupped['Cangacian Fleet'].append(string_data)
            elif string_header.startswith("kiith") or string_header.startswith("desc_kiith"):
                string_data = {'head': string_header, 'text': string_text}
                self.strings_groupped['Kiithid'].append(string_data)
            elif string_header.startswith("c_") or string_header.startswith("desc_c_"):
                string_data = {'head': string_header, 'text': string_text}
                self.strings_groupped['Skins'].append(string_data)
            elif string_header.startswith("officer_") or string_header.startswith("desc_officer_"):
                string_data = {'head': string_header, 'text': string_text}
                self.strings_groupped['Officers'].append(string_data)
            elif string_header.startswith("rp_") or string_header.startswith("desc_rp_"):
                string_data = {'head': string_header, 'text': string_text}
                self.strings_groupped['Research'].append(string_data)
            elif string_header.startswith("dia_"):
                string_data = {'head': string_header, 'text': string_text}
                self.strings_groupped['Dialogs'].append(string_data)
            else:
                string_data = {'head': string_header, 'text': string_text}
                self.strings_groupped['Unsorted'].append(string_data)

    def get_text_by_header(self, header):
        return self.strings.get(header)
    
    def record_to_file(self):
        body = "# HWM STRINGS:\n"
        for group, string_datas in self.strings_groupped.items():
            body += f"\n## {group}:\n"
            for string_data in string_datas:
                body += f"{string_data.get('head')}: {string_data.get('text')}\n"
        utils.rewrite_file(body, self._file_name)