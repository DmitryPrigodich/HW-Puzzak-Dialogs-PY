import json
import utils
import constants

class All_Pages_Backup:
    def backup_everything(self, page):
        self.page_url = constants.URL_HWM_DB
        self.page = page
        
        locator_ids = self._get_locator_ids()
        for locator_id in locator_ids:
            self.page.click(f"#{locator_id}")

            tags = self._get_tags()

            entries = {}
            entry_elements_list = self.page.query_selector_all('.entry')
            print(f"{locator_id}: {len(entry_elements_list)} entries found")

            for entry_element in entry_elements_list:
                entry_head = entry_element.query_selector(constants.LOCATOR_ENTRYHEAD).inner_text().strip()
                
                entry_items = {}
                for tag in tags:
                    entry_tag_element = entry_element.query_selector(constants.LOCATOR_ENTRYITEM_SPECIFIC.format(tag))
                    if entry_tag_element:
                        entry_tag_value = entry_tag_element.inner_text().strip()
                        entry_items[tag] = entry_tag_value
                entries[entry_head] = entry_items

            json_data = json.dumps(entries, ensure_ascii=False)
            utils.rewrite_file(json_data, f"json_bak/{locator_id}.json")

    def _get_tags(self):
        tags = []
        tag_elements_list = self.page.query_selector_all(constants.LOCATOR_TAGS)
        for tag_element in tag_elements_list:
            tag_value = tag_element.inner_text().strip()
            tags.append(tag_value)
        tags = list(set(tags))
        return tags
    
    def _get_locator_ids(self):
        locator_ids = []
        modules = self.page.query_selector_all("div.module")
        for module in modules:
            locator_id = module.get_attribute("id")
            locator_ids.append(locator_id)
        return locator_ids