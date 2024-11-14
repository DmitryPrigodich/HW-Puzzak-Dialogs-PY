import constants
from playwright.sync_api import Page

class Base_Page:
    def __init__(self, page: Page, locator):
        self.page = page
        self.page_url = constants.URL_HWM_DB
        self.page.click(locator)
        assert self.page.wait_for_selector("#entries > div:nth-child(1)")