
import utils

from .constructor_base import Constructor_Base

class Mission_Step_Actions_Constructor(Constructor_Base):
    _MISSION_STEPS_ACTIONS_DATA_JSON = "json_bak/MissionStepActions-module.json"

    _FILE_NAME = "data/MISSION_STACT.md"
    _FILE_NAME_TMP = "data/MISSION_STACT_TMP.md"
    _FILE_NAME_JSON = "json/mission_stact.json"

    _mission_steps_actions_data = {}
    _mission_step_actions = {}


    def __init__(self):
        super().__init__()
        self._mission_steps_actions_data = utils.read_json(self._MISSION_STEPS_ACTIONS_DATA_JSON)
        self._set_data()

    def get_data(self):
        return self._mission_step_actions
    
    def _set_data(self):
        for msa_key, msa_tags in self._mission_steps_actions_data.items():
            msa_key_dict = {}

            for key in ["Type:"]:
                if key in msa_tags:
                    msa_key_dict[key] = msa_tags.get(key)

            for key in ["TV1:", "TVS:","PCG_Meta:","StepsLinkList:"]:
                if key in msa_tags:
                    msa_key_dict[key] = sorted(msa_tags.get(key).split(":"))
            
            self._mission_step_actions[msa_key] = msa_key_dict

    def write_json(self):
        utils.write_json(self._mission_step_actions, self._FILE_NAME_JSON)
    
    def write_data(self):
        body = "# HWM MISSION STEPS SPECIFIED\n"
        for msa_key, msa_tags in self._mission_step_actions.items():
            body += f"\n## {msa_key}\n"

            for key in ["Type:", "TV1:"]:
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
    def _write_data_tmp(self):   
        _title = "HWM Mission Step Actions TMP"
        _tmp_data = self._mission_steps_actions_data
        _splitter = "\n"

        #fill it when tags are known
        _existing_tags = ["PCG_Meta:","StepsLinkList:","TV1:","TV2:","TV3:","TVS:","Type:"]
        _tags_single_line = ["Type:"]
        _tags_multiple_lines = ["PCG_Meta:","StepsLinkList:","TV1:","TV2:","TV3:","TVS:"]

        def get_tags(data):
            body_tags = "\n## TAGS:\n"
            tag_collector = []
            for id, params in data.items():
                for param_key, param_value in params.items():
                    tag_collector.append(param_key)
            tag_collector = sorted(list(set(tag_collector)))
            tag_list = ", ".join(map(str, tag_collector))
            body_tags += f"{tag_list}\n"
            return body_tags

        def get_main(data):
            def _get_single_line(param_value):
                return f"{param_value}\n"

            def _get_multiple_lines(param_value):
                body_lines = ""
                param_value_list = param_value.split(_splitter)
                for value in param_value_list:
                    body_lines += f"\n\t\t* {value}"
                body_lines += "\n"
                return body_lines

            body_main = ""
            for id, parameters in data.items():
                body_main += f"\n## {id}\n"

                for param_key in _existing_tags:
                    if param_key in parameters:
                        body_main += f"\t* {param_key} "
                        param_value = parameters.get(param_key)
                        match param_key:                   
                            case key if key in _tags_multiple_lines:
                                body_main += _get_multiple_lines(param_value)
                            case key if key in _tags_single_line:
                                body_main += _get_single_line(param_value)
                            case _:
                                body_main += _get_single_line(param_value)
            return body_main

        body = f"# {_title}\n\n".upper()
        # body += get_tags(_tmp_data)
        body += get_main(_tmp_data)
            
        utils.rewrite_file(body, self._FILE_NAME_TMP)


    def get_mission_step_actions_by_id(self,mission_step_act_id):
        return self._mission_step_actions.get(mission_step_act_id)