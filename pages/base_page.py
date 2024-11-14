import constants
from playwright.sync_api import Page

class Base_Page:
    def __init__(self, page: Page):
        self.page = page
        self.page_url = constants.URL_HWM_DB