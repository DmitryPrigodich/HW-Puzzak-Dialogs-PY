
import utils

from .constuctor_base import Constructor_Base

class Mission_Step_Constructor(Constructor_Base):
    MISSION_STEPS_DATA_JSON = "json_bak/MissionSteps-module.json"

    FILE_NAME = "data/MISSIONS_STEPS.md"
    FILE_NAME_TMP = "data/MISSIONS_STEPS_TMP.md"
    FILE_NAME_JSON = "json/missions_steps.json"

    _mission_steps_data = {}

    _mission_steps = {}

    # just to list them all
    _mission_step_tags = ["StepId:","Type:","IsHighlight:","TV1:","TV2:","TV3:","TVS:","TargetIdsList:","TargetType:","SuccLL","FailLL"]

    def __init__(self):
        super().__init__()
        self._mission_steps_data = self._read_json(self.MISSION_STEPS_DATA_JSON)
        self._set_mission_steps()

    def _set_mission_steps(self):
        for ms_key, ms_tags in self._mission_steps_data.items():
            ms_key_dict = {}

            for key in ["StepId:", "Type:", "TargetType:"]:
                if key in ms_tags:
                    ms_key_dict[key] = ms_tags.get(key)

            for key in ["TVS:", "SuccLL:", "FailLL:"]:
                if key in ms_tags:
                    ms_key_dict[key] = sorted(ms_tags.get(key).split(":"))
            
            self._mission_steps[ms_key] = ms_key_dict

        self._write_json(self._mission_steps)

    
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
            for t_value in sorted(t_values):
                body_tags += f"\t\t* {t_value}\n"

        utils.rewrite_file(body_tags, self.FILE_NAME)
        utils.add_to_file(body, self.FILE_NAME)

        print("Finished writing Mission Step Data")

    def write_data_spc(self):
        body = "\n# HWM MISSION STEPS SPECIFIED\n"
        for ms_key, ms_tags in self._mission_steps.items():
            body += f"\n## {ms_key}\n"

            for key in ["StepId:", "Type:", "TargetType:"]:
                if key in ms_tags:
                    body += f"\t* {key} {ms_tags[key]}\n"

            for key in ["TVS:", "SuccLL:", "FailLL:"]:
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

    def get_mission_step_by_id(self,mis_step_id):
        return self._mission_steps.get(mis_step_id)