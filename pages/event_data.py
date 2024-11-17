import utils
import json
import logging
import constants
from .base_page import Base_Page

logger = logging.getLogger(__name__)

class Event_Data_Page(Base_Page):
    LOCATOR = "#EventData-module"
    FILE_NAME = "data/EVENTS.md"
    FILE_NAME_JSON = "data/EVENTS_JSON.md"

    _events = []

    def __init__(self, page):
        super().__init__(page, self.LOCATOR)

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
        json_data = json.dumps(self._events, ensure_ascii=False)
        utils.rewrite_file(json_data, self.FILE_NAME_JSON)
    
    def read_json(self):
        with open(self.FILE_NAME_JSON, 'r', encoding='utf-8') as file:
            json_data = file.read()
        logger.log(json_data)
        self._events = json.loads(json_data)
        logger.log(self._events)
        return self._events

    def get_events(self):
        return self._events

    
    def write_data(self):
        body = "# HWM EVENTS:\n"
        for event in self._events:
            body += f"* {event['header']} : {event['group']}"
        utils.rewrite_file(body, self.FILE_NAME)