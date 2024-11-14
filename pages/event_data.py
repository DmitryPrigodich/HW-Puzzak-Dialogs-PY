import constants
import utils
from .base_page import Base_Page

class Event_Data_Page(Base_Page):
    _file_name = "EVENTS.md"
    _locator = "#EventData-module"

    events = []
    event_groups = []
    events_groupped = {}
    groups_evented = {}

    def __init__(self, page):
        super().__init__(page, self._locator)
        self._save_events()

    def _save_events(self):
        list_elements_entries = self.page.query_selector_all('.entry')
        print(f"Event Data: {len(list_elements_entries)} entries found")

        for element_entry in list_elements_entries:
            entryhead_el = element_entry.query_selector(constants.LOCATOR_ENTRYHEAD)
            event_name = entryhead_el.inner_text().strip() if entryhead_el else "Unknown"

            entryitem_el = element_entry.query_selector(constants.LOCATOR_ENTRYITEM_SPECIFIC.format("Group"))
            event_group = entryitem_el.inner_text().strip() if entryitem_el else "No-Group"

            self.events.append(event_name)
            self.event_groups.append(event_group)
            self.groups_evented[event_name] = event_group

            if event_group not in self.events_groupped:
                self.events_groupped[event_group] = []
            self.events_groupped[event_group].append(event_name)

        self.events = sorted(self.events)
        self.event_groups = sorted(list(set(self.event_groups)))
        self.event_groups.remove("No-Group")
        self.events_groupped = {key: self.events_groupped[key] for key in sorted(self.events_groupped.keys())}

    def get_group_by_event(self, event_name):
        group = self.groups_evented[event_name]
        print 
        if group == "No-Group":
            print("No group for this event")
        else:
            print(f"{group}: {event_name}")
        return group
    
    def get_events_by_group(self, group):
        events = self.events_groupped.get(group)

        print(f"Group: {group}\n")
        for event in events:
            print(f"  * {event}\n")

        return events
    
    def record_to_file(self):
        utils.rewrite_file("h1. HWM EVENT GROUPS:\n\n", self._file_name)
        for group in self.event_groups:
            utils.add_to_file(f"* {group}\n", self._file_name)

        utils.add_to_file("\n\n", self._file_name)

        utils.add_to_file("# HWM EVENTS:\n\n", self._file_name)
        for group, events in self.events_groupped.items():
            utils.add_to_file(f"* {group}\n", self._file_name)
            for event in sorted(events):
                utils.add_to_file(f"  * {event}\n", self._file_name)