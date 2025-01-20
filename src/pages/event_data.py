import utils
from .base_page import Base_Page

class Event_Data_Page(Base_Page):
    _LOCATOR = "#EventData-module"
    _FILE_NAME = "dataset/data/EVENTS.md"
    _FILE_NAME_JSON = "dataset/json/events.json"

    _events = []

    def __init__(self, page):
        super().__init__(page, self._LOCATOR)

    def save_data(self):
        for element_entry in self._get_list_elements_entries("Event Data"):
            event_header = self._get_entryhead(element_entry)
            event_group = self._get_entryitem_by_tag(element_entry, "Group")

            event = {
                'header': event_header,
                'group': event_group
            }
            self._events.append(event)
            
        return self._events
    
    def write_json(self):
        self._write_json(self._events)
    
    def read_json(self):
        return self._read_json(self._FILE_NAME_JSON)
    
    def write_data(self):
        body = "# HWM EVENTS:\n"
        for event in self._events:
            body += f"* {event['header']} : {event['group']}\n"
        utils.rewrite_file(body, self._FILE_NAME)

    def get_events(self):
        return self._events
    
    def check_event(self, event):
        return any(item["header"] == event for item in self._events)
    
    def get_tags(self):
        print(self._get_tags())
        return self._get_tags()