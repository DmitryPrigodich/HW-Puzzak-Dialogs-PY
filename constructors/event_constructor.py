import utils
from .constructor_base import Constructor_Base

class Event_Constructor(Constructor_Base):
    _EVENT_DATA_JSON = "json_bak/EventData-module.json"

    _FILE_NAME = "data/EVENTS.md"
    _FILE_NAME_TMP = "data/EVENTS_TMP.md"
    _FILE_NAME_JSON = "json/events.json"

    _event_data = {}
    _events = {}

    # reshuffle it your way
    _event_tags = [
        "StartDate:","EndDate:","Group:","Priority:","QuestConditions:","EventParameters:","EventParameterSpecifications:","PlacementMode:","PlacementParams:","SystemSelection:","SelectionParams:","ActiveOnWeekdays:","IsEventQuestTabTimer:","IsExclusive:","Visuals:","MissionIds:"
    ]

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
    def write_data_tmp(self):
        body = "# HWM EVENTS\n"

        def _get_single_line(e_param_value):
            return f"{e_param_value}\n"

        def _get_multiple_lines(e_param_value):
            body_lines = ""
            e_param_value_list = e_param_value.split("\n")
            for value in e_param_value_list:
                body_lines += f"\n\t\t* {value}"
            body_lines += "\n"
            return body_lines
        
        def _get_tags():
            body_tags = "\n## TAGS:\n"
            tag_collector = []
            for event_id, event_params in self._event_data.items():
                for ep_key,ep_value in event_params.items():
                    tag_collector.append(ep_key)
            tag_collector = sorted(list(set(tag_collector)))
            tag_list = ", ".join(map(str, tag_collector))
            body_tags += f"{tag_list}\n"
            return body_tags
        
        # body += _get_tags()
        
        for event_id, event_params in self._event_data.items():
            body += f"\n## {event_id}\n"

            for e_param_key in self._event_tags:
                if e_param_key in event_params:
                    body += f"\t* {e_param_key} "
                    e_param_value = event_params.get(e_param_key)

                    match e_param_key:                   
                        case key if key in ["EventParameters:","EventParameterSpecifications:","QuestConditions:","PlacementParams:","MissionIds:","Visuals:","SystemSelection:"]:
                            body += _get_multiple_lines(e_param_value)
                        case key if key in ["StartDate:","EndDate:","Priority:","Group:","IsEventQuestTabTimer:","IsExclusive:","PlacementMode","SelectionParams"]:
                            body += _get_single_line(e_param_value)
                        case _:
                            body += _get_single_line(e_param_value)

        utils.rewrite_file(body, self._FILE_NAME_TMP)

    def get_events(self):
        return self._events