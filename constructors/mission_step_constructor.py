import utils

from .constructor_base import Constructor_Base
from .mission_step_actions_constructor import Mission_Step_Actions_Constructor
from .dia_seq_constructor import Dialog_Sequence_Constructor

class Mission_Step_Constructor(Constructor_Base):
    _MISSION_STEPS_DATA_JSON = "json_bak/MissionSteps-module.json"

    _FILE_NAME = "data/MISSION_STEPS.md"
    _FILE_NAME_TMP = "data/MISSION_STEPS_TMP.md"
    _FILE_NAME_JSON = "json/mission_steps.json"

    _mission_steps_data = {}
    _mission_steps = {}


    def __init__(self):
        super().__init__()
        self._mission_steps_data = utils.read_json(self._MISSION_STEPS_DATA_JSON)
        self._set_data()

    def _set_data(self):
        for ms_key, ms_tags in self._mission_steps_data.items():
            ms_key_dict = {}

            for key in ["StepId:", "Type:", "TargetType:"]:
                if key in ms_tags:
                    ms_key_dict[key] = ms_tags.get(key)

            for key in ["TVS:", "SuccLL:", "FailLL:"]:
                if key in ms_tags:
                    ms_key_dict[key] = sorted(ms_tags.get(key).split(":"))
            
            self._mission_steps[ms_key] = ms_key_dict
        
    def get_data(self):
        return self._mission_steps
    
    def write_json(self):
        utils.write_json(self._mission_steps,self._FILE_NAME_JSON)
  
    def write_data(self):
        body = "# HWM MISSION STEPS SPECIFIED\n"
        for ms_key, ms_tags in self._mission_steps.items():
            body += f"\n## {ms_key}\n"

            for key in ["StepId:", "Type:", "TargetType:"]:
                if key in ms_tags:
                    body += f"\t* {key} {ms_tags[key]}\n"

            for key in ["TVS:", "SuccLL:", "FailLL:"]:
                if key in ms_tags:
                    body += f"\t* {key} "
                    ms_tag_value = ms_tags[key]
                    if len(ms_tag_value) > 1:
                        for value in ms_tag_value:
                            body += f"\n\t\t* {value}"
                    else:
                        body += f"{ms_tag_value[0]}"
                    body += "\n"

        utils.rewrite_file(body, self._FILE_NAME)

    # full set for analysis only
    def _write_data_tmp(self):
        _title = "HWM Mission Steps TMP"
        _tmp_data = self._mission_steps_data
        _splitter = "\n"

        #fill it when tags are known
        _existing_tags = ["StepId:","Type:","IsHighlight:","TV1:","TV2:","TV3:","TVS:","TargetIdsList:","TargetType:","SuccLL","FailLL"]
        _tags_single_line = ["StepId:", "Type:", "TargetType:"]
        _tags_multiple_lines = ["TVS:", "SuccLL:", "FailLL:"]

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

    def get_mission_step_by_id(self,mission_step_id):
        return self._mission_steps.get(mission_step_id)
    
    def get_mission_steps_text(self, mission_step_id):
        body_mission_step = ""

        dialog_data = Dialog_Sequence_Constructor()
        ms_action_data = Mission_Step_Actions_Constructor()
        
        # print(f"Mission step {mission_step_id}")
        mission_step = self.get_mission_step_by_id(mission_step_id)

        ms_target_type = mission_step.get("TargetType:")
        if ms_target_type == "OnDialogFinished":
            ms_dialogs = mission_step.get("TVS:")
            for ms_dialog_id in ms_dialogs:
                ms_dialog_text = dialog_data.get_dialog_text(ms_dialog_id)
                if ms_dialog_text:
                    body_mission_step += ms_dialog_text
                else:
                    error_text = f"Dialog_id not found: {ms_dialog_id}"
                    print(error_text)
                    body_mission_step += f"{error_text}\n"

        if "SuccLL:" in mission_step:
            ms_actions = mission_step.get("SuccLL:")
            for ms_action_id in ms_actions:
                ms_action = ms_action_data.get_mission_step_actions_by_id(ms_action_id)
                
                ms_action_type = ms_action.get("Type:")
                match ms_action_type:
                    case "TriggerDialog":
                        msa_dialogs = ms_action.get("TVS:")
                        for msa_dialog_id in msa_dialogs:
                            msa_dialog_text = dialog_data.get_dialog_text(msa_dialog_id)
                            if msa_dialog_text:
                                body_mission_step += msa_dialog_text
                            else:
                                error_text = f"Dialog_id not found: {msa_dialog_id}"
                                print(error_text)
                                body_mission_step += f"{error_text}\n"
                            
                    case "AddMissionSteps":
                        link_mission_steps = ms_action.get("StepsLinkList:")
                        for link_mission_step_id in link_mission_steps:
                            body_mission_step += self.get_mission_steps_text(link_mission_step_id)

        return body_mission_step