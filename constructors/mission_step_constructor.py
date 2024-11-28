
import utils

from .constuctor_base import Constructor_Base

class Mission_Step_Constructor(Constructor_Base):
    MISSION_STEPS_DATA_JSON = "json_bak/MissionSteps-module.json"

    FILE_NAME = "data/MISSIONS_STEPS.md"
    FILE_NAME_TMP = "data/MISSIONS_STEPS_TMP.md"
    FILE_NAME_JSON = "json/missions_steps.json"

    _mission_steps_data = {}

    def __init__(self):
        super().__init__()
        self._mission_steps_data = self._read_json(self.MISSION_STEPS_DATA_JSON)

    def set_missions(self):
        return self._mission_steps_data

    
    def write_data(self):
        tags = {}

        body = "\n# HWM MISSION STEPS\n"
        for ms_key, ms_tags in self._mission_steps_data.items():
            body += f"\n## {ms_key}\n"
            for mst_key, mst_value in ms_tags.items():
                if mst_key not in tags:
                    tags[mst_key] = []
                tags[mst_key].append(mst_value)
                body += f"\t* {mst_key} {mst_value}\n"

        tags = utils.sort_dict_by_keys(tags)
        
        body_tags = "\n# HWM MISSIONS STEPS TAGS\n\n"
        for t_key, t_values in tags.items():
            t_values = sorted(list(set(t_values)))
            body_tags += f"\t* {t_key}:\n"
            body_tags += f"\t\t* {t_values}\n"

        utils.rewrite_file(body_tags, self.FILE_NAME_2)
        utils.add_to_file(body, self.FILE_NAME_2)

        print("Finished writing Mission Step Data")

    # HWM MISSIONS STEPS TAGS
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