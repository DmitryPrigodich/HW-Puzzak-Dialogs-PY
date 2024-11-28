
import utils

from .constuctor_base import Constructor_Base

class Mission_Step_Actions_Constructor(Constructor_Base):
    MISSION_STEPS_ACTIONS_DATA_JSON = "json_bak/MissionStepActions-module.json"

    FILE_NAME = "data/MISSION_STACT.md"
    FILE_NAME_TMP = "data/MISSION_STACT_TMP.md"

    _mission_steps_actions_data = {}

    def __init__(self):
        super().__init__()
        self._mission_steps_actions_data = self._read_json(self.MISSION_STEPS_ACTIONS_DATA_JSON)


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
            
        utils.rewrite_file(body_tags, self.FILE_NAME_3)
        utils.add_to_file(body, self.FILE_NAME_3)

        print("Finished writing Mission Step Actions Data")

    # HWM MISSIONS STEPS ACTIONS TAGS
        # * FailLL:
        # * IsHighlight:
        # * StepId:
        # * SuccLL:
        # * TV1:
        # * TV2:
        # * TV3:
        # * TVS:
        # * TargetIdsList:
        # * TargetType:
        # * Type: