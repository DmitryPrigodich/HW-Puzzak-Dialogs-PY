import constants
from playwright.sync_api import Page

class Base_Page:
    def __init__(self, page: Page, locator):
        self.page = page
        self.page_url = constants.URL_HWM_DB
        self.page.click(locator)
        assert self.page.wait_for_selector("#entries > div:nth-child(1)")
        

    def _get_list_elements_entries(self, data_text):
        list_elements_entries = self.page.query_selector_all('.entry')
        print(f"{data_text}: {len(list_elements_entries)} entries found")
        return list_elements_entries
    
    def _get_entryhead(self, element_entry):
        entryhead_el = element_entry.query_selector(constants.LOCATOR_ENTRYHEAD)
        entryhead = entryhead_el.inner_text().strip() if entryhead_el else "Unknown"
        return entryhead
    
    def _get_entryitem(self, element_entry):
        entryitem_el = element_entry.query_selector(constants.LOCATOR_ENTRYITEM)
        entryitems = entryitem_el.inner_text().strip() if entryitem_el else "Unknown"
        return entryitems
    
    def _get_tags(self):
        tags = []
        list_elements_entries = self.page.query_selector_all(constants.LOCATOR_TAGS)
        for entry in list_elements_entries:
            tags.append(entry.inner_text().strip())
        return list(set(tags))
        

    def _get_entryitem_by_tag(self, element_entry, tag):
        entryitem_el = element_entry.query_selector(constants.LOCATOR_ENTRYITEM_SPECIFIC.format(tag))
        entryitem = entryitem_el.inner_text().strip() if entryitem_el else "Unknown"
        return entryitem