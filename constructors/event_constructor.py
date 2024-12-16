import utils
from .constructor_base import Constructor_Base
from constructors.quest_line_constructor import Quest_Line_Constructor
from constructors.quest_constructor import Quest_Constructor

class Event_Constructor(Constructor_Base):
    _EVENT_DATA_JSON = "json_bak/EventData-module.json"

    _FILE_NAME = "data/EVENTS.md"
    _FILE_NAME_TMP = "data/EVENTS_TMP.md"
    _FILE_NAME_JSON = "json/events.json"

    _event_data = {}
    _events = {}

    def __init__(self):
        super().__init__()
        self._event_data = utils.read_json(self._EVENT_DATA_JSON)
        self._set_data()

    def _set_data(self):
        self._events["Unknown"] = []
        for event_id, event_params in self._event_data.items():
            if "Group:" in event_params:
                group = event_params.get("Group:")
                if group not in self._events:
                    self._events[group] = []
                self._events[group].append(event_id)
            else:
                self._events["Unknown"].append(event_id)

    def get_data(self):
        return self._events
    
    def write_json(self):
        utils.write_json(self._events, self._FILE_NAME_JSON)

    def write_data(self):
        body = "# HWM EVENTS\n"
        for group_id, events in self._events.items():
            body += f"\n## **{group_id}**\n".upper()
            for event_id in sorted(events):
                body += f"\t* {event_id}\n"

        utils.rewrite_file(body, self._FILE_NAME)

    # full set for analysis only
    def _write_data_tmp(self):
        _title = "HWM Events TMP"

        #fill it when tags are known
        _existing_tags = ["StartDate:","EndDate:","Group:","Priority:","QuestConditions:","EventParameters:","EventParameterSpecifications:","PlacementMode:","PlacementParams:","SystemSelection:","SelectionParams:","ActiveOnWeekdays:","IsEventQuestTabTimer:","IsExclusive:","Visuals:","MissionIds:"]
        _tags_single_line = ["StartDate:","EndDate:","Priority:","Group:","IsEventQuestTabTimer:","IsExclusive:","PlacementMode:","SelectionParams:"]
        _tags_multiple_lines = ["EventParameters:","EventParameterSpecifications:","QuestConditions:","PlacementParams:","MissionIds:","Visuals:","SystemSelection:"]

        def _get_single_line(param_value):
            return f"{param_value}\n"

        def _get_multiple_lines(param_value):
            body_lines = ""
            param_value_list = param_value.split(":")
            for value in param_value_list:
                body_lines += f"\n\t\t* {value}"
            body_lines += "\n"
            return body_lines

        def _get_tags(data):
            body_tags = "\n## TAGS:\n"
            tag_collector = []
            for id, params in data.items():
                for param_key, param_value in params.items():
                    tag_collector.append(param_key)
            tag_collector = sorted(list(set(tag_collector)))
            tag_list = ", ".join(map(str, tag_collector))
            body_tags += f"{tag_list}\n"
            return body_tags

        def _get_main(data):
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
        # body += _get_tags(self._event_data)
        body += _get_main(self._event_data)
        
        utils.rewrite_file(body, self._FILE_NAME_TMP)

    def get_events(self):
        return self._events
    
    def get_event_text(self,event_id):
        body_event = ""
        body_event += utils.format_br(1)
        body_event += utils.format_heading2(f"Event: {event_id}")
        body_event += utils.format_br(2)

        if event_id == "strike_missions":
            quests = ["qr_013","qr_014","qr_015","qr_019","qr_023"]
        else:
            quest_line_data = Quest_Line_Constructor()
            quest_line_id = quest_line_data.get_quest_line_by_event_id(event_id)
            quests = quest_line_data.get_quests_by_quest_line_id(quest_line_id)
        
        quest_data = Quest_Constructor()
        for quest_id in quests:
            body_event += quest_data.get_quest_text(quest_id)
        
        return body_event