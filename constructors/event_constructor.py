from .constuctor_base import Constructor_Base

class Event_Constructor(Constructor_Base):
    _EVENT_DATA_JSON = "json_bak/EventData-module.json"
    _EVENT_JSON = "json/events.json"

    _FILE_NAME = "data/EVENTS.md"
    _FILE_NAME_TMP = "data/EVENTS_TMP.md"

    _event_data = {}
    _events = {}

    def __init__(self):
        super().__init__()
        self._event_data = self._read_json(self._EVENT_DATA_JSON)
        self._events = self._read_json(self._EVENT_JSON)
        # self._set_chapters()

    # # data was already recorded in pages\chapter_data.py, so I won't repeat myself for now
    # def _set_chapters(self):
    # def write_data(self):
    # def write_data_spc(self):

    def get_events(self):
        return self._events
    
    def get_event_group_by_event_id(self):
        do = "nothing"