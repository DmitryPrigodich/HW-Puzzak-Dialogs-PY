
import utils

from .constructor_base import Constructor_Base

class Mission_Step_Actions_Constructor(Constructor_Base):
    _MISSION_STEPS_ACTIONS_DATA_JSON = "json_bak/MissionStepActions-module.json"

    _FILE_NAME = "data/MISSION_STACT.md"
    _FILE_NAME_TMP = "data/MISSION_STACT_TMP.md"
    _FILE_NAME_JSON = "json/mission_stact.json"

    _mission_steps_actions_data = {}
    _mission_step_actions = {}

    
    # just to list them all
    _mission_step_tags = ["PCG_Meta:","StepsLinkList:","TV1:","TV2:","TV3:","TVS:","Type:"]

    def __init__(self):
        super().__init__()
        self._mission_steps_actions_data = utils.read_json(self._MISSION_STEPS_ACTIONS_DATA_JSON)
        self._set_data()

    def _set_data(self):
        for msa_key, msa_tags in self._mission_steps_actions_data.items():
            msa_key_dict = {}

            for key in ["Type:"]:
                if key in msa_tags:
                    msa_key_dict[key] = msa_tags.get(key)

            for key in ["TVS:","PCG_Meta:","StepsLinkList:"]:
                if key in msa_tags:
                    msa_key_dict[key] = sorted(msa_tags.get(key).split(":"))
            
            self._mission_step_actions[msa_key] = msa_key_dict

    def write_json(self):
        utils.write_json(self._mission_step_actions, self._FILE_NAME_JSON)
    
    def write_data(self):
        body = "# HWM MISSION STEPS SPECIFIED\n"
        for msa_key, msa_tags in self._mission_step_actions.items():
            body += f"\n## {msa_key}\n"

            for key in ["Type:"]:
                if key in msa_tags:
                    body += f"\t* {key} {msa_tags[key]}\n"

            for key in ["TVS:","PCG_Meta:","StepsLinkList:"]:
                if key in msa_tags:
                    body += f"\t* **{key}** "
                    ms_tag_value = msa_tags[key]
                    if len(ms_tag_value) > 1:
                        for value in ms_tag_value:
                            body += f"\n\t\t* {value}"
                    else:
                        body += f"{ms_tag_value[0]}"
                    body += "\n"
                    
        utils.rewrite_file(body, self._FILE_NAME)

    # full set for analysis only
    def write_data_tmp(self):
        tags = {}

        body = "# HWM MISSION STEP ACTIONS\n"
        for msa_key, msa_tags in self._mission_steps_actions_data.items():
            body += f"\n## {msa_key}\n"
            for msat_key, msat_value in msa_tags.items():
                if msat_key not in tags:
                    tags[msat_key] = []
                tags[msat_key].append(msat_value)
                body += f"\t* {msat_key} {msat_value}\n"

        tags = utils.sort_dict_by_keys(tags)

        body_tags = "\n# HWM MISSIONS STEPS ACTIONS TAGS\n\n"
        for t_key, t_values in tags.items():
            t_values = sorted(list(set(t_values)))
            body_tags += f"\t* {t_key}:\n"
            body_tags += f"\t\t* {t_values}\n"
            
        utils.rewrite_file(body_tags, self._FILE_NAME_TMP)
        utils.add_to_file(body, self._FILE_NAME_TMP)

        print("Finished writing Mission Step Actions Data")

    def get_mission_step_actions_by_id(self,mis_step_act_id):
        return self._mission_step_actions.get(mis_step_act_id)