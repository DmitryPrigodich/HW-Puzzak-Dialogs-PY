import utils

from .constructor_base import Constructor_Base

class Quest_Line_Constructor(Constructor_Base):
    _QUEST_LINE_DATA_JSON = "json_bak/QuestLineData-module.json"

    _FILE_NAME = "data/QUEST_LINES.md"
    _FILE_NAME_TMP = "data/QUEST_LINES_TMP.md"
    _FILE_NAME_JSON = "json/quest_lines.json"

    _quest_line_data = {}
    _quest_lines = {}

    # just to list them all
    

    def __init__(self):
        super().__init__()
        self._quest_line_data = utils.read_json(self._QUEST_LINE_DATA_JSON)
        self._set_data()

    def _set_data(self):
        for ql_id, ql_params in self._quest_line_data.items():
            self._quest_lines[ql_id.lower()] = ql_params.get("QuestIds:").split(":")
        
    def get_data(self):
        return self._quest_lines

    def write_json(self):
        utils.write_json(self._quest_lines, self._FILE_NAME_JSON)
  
    def write_data(self):
        body = "# HWM QUEST LINES\n"
        for ql_id, quests in self._quest_lines.items():
            body += f"\n## {ql_id}\n".upper()
            for quest_id in quests:
                body += f"\t* {quest_id}\n"
        utils.rewrite_file(body, self._FILE_NAME)

    # full set for analysis only
    def _write_data_tmp(self):
        _title = "HWM Quest Lines TMP"
        _tmp_data = self._quest_line_data
        _splitter = ":"

        #fill it when tags are known
        _existing_tags = ["Duration:", "Restarts:", "QuestIds:"]
        _tags_single_line = ["Duration:","Restarts:"]
        _tags_multiple_lines = ["QuestIds:"]

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
       
    def get_quest_line_by_event_id(self, event_id):
        match event_id:
            case "event_season_yaoSpr_2023":
                return "ql_event_yaot_spring_2023"
            case "event_season_amaSum_2023_t4":
                return "ql_event_amaSum_2023_t4"
            case "event_season_iyaFal_2023_t4":
                return "ql_event_iyaFal_2023_t4"
            case _:
                return f"ql_{event_id}"

    def get_quests_by_quest_line_id(self, quest_line_id):
        if quest_line_id in self._quest_lines:
            return self._quest_lines.get(quest_line_id)
        return None
    
    def get_quests_by_event_id(self, event_id):
        quest_line_id = self.get_quest_line_by_event_id(event_id)
        return self.get_quests_by_quest_line_id(quest_line_id)