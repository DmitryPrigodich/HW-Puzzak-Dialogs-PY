
import utils

from .constuctor_base import Constructor_Base

class Mission_Step_Actions_Constructor(Constructor_Base):
    MISSION_STEPS_ACTIONS_DATA_JSON = "json_bak/MissionStepActions-module.json"

    FILE_NAME = "data/MISSION_STACT.md"
    FILE_NAME_TMP = "data/MISSION_STACT_TMP.md"

    _mission_steps_actions_data = {}
    _mission_step_actions = {}

    
    # just to list them all
    _mission_step_tags = ["PCG_Meta:","StepsLinkList:","TV1:","TV2:","TV3:","TVS:","Type:"]

    def __init__(self):
        super().__init__()
        self._mission_steps_actions_data = self._read_json(self.MISSION_STEPS_ACTIONS_DATA_JSON)
        self._set_mission_step_actions()

    def _set_mission_step_actions(self):
        for msa_key, msa_tags in self._mission_steps_actions_data.items():
            msa_key_dict = {}

            for key in ["Type:"]:
                if key in msa_tags:
                    msa_key_dict[key] = msa_tags.get(key)

            for key in ["TVS:","PCG_Meta:","StepsLinkList:"]:
                if key in msa_tags:
                    msa_key_dict[key] = sorted(msa_tags.get(key).split(":"))
            
            self._mission_step_actions[msa_key] = msa_key_dict

        self._write_json(self._mission_step_actions)

    def write_data(self):
        tags = {}

        body = "\n# HWM MISSION STEP ACTIONS\n"
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
            
        utils.rewrite_file(body_tags, self.FILE_NAME)
        utils.add_to_file(body, self.FILE_NAME)

        print("Finished writing Mission Step Actions Data")

    # HWM MISSIONS STEPS ACTIONS TAGS


    def write_data_spc(self):
        body = "\n# HWM MISSION STEPS SPECIFIED\n"
        for ms_key, ms_tags in self._mission_step_actions.items():
            body += f"\n## {ms_key}\n"

            for key in ["Type:"]:
                if key in ms_tags:
                    body += f"\t* {key} {ms_tags[key]}\n"

            for key in ["TVS:","PCG_Meta:","StepsLinkList:"]:
                if key in ms_tags:
                    body += f"\t* {key}\n"
                    # for some reasons it doesn't want to unpack list in a good way
                    # at least it works, got other things to implement
                    if isinstance(ms_tags[key], list):
                        for value in ms_tags[key]:
                            body += f"\t\t* {value}\n"
                    else:
                        for value in ms_tags[key].split(":"):
                            body += f"\t\t* {value}\n"

        utils.rewrite_file(body, self.FILE_NAME_TMP)

    def get_mission_step_actions_by_id(self,mis_step_act_id):
        return self._mission_step_actions.get(mis_step_act_id)