import constants
import utils
from .base_page import Base_Page

class Event_Data_Page(Base_Page):
    _file_name = "EVENTS.md"
    events = []
    event_groups = []
    events_groupped = {}
    groups_evented = {}

    def __init__(self, page):
        super().__init__(page)

    def open(self):
        self.page.click(constants.LOCATOR_EVENTDATA)
        assert self.page.wait_for_selector("#entries > div:nth-child(1)")

    def save_events(self):
        list_elements_entries = self.page.query_selector_all('.entry')

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
        if not "No-Group":
            print(f"{group}: {event_name}")
        else:
            print("No group for this event")
        return group
    
    def output_events(self):
        utils.rewrite_file("h1. HWM EVENT GROUPS:\n\n", self._file_name)
        for group in self.event_groups:
            utils.add_to_file(f"* {group}\n", self._file_name)

        utils.add_to_file("\n\n", self._file_name)

        utils.add_to_file("h1. HWM EVENTS:\n\n", self._file_name)
        for group, events in self.events_groupped.items():
            utils.add_to_file(f"* {group}\n", self._file_name)
            for event in sorted(events):
                utils.add_to_file(f"  * {event}\n", self._file_name)