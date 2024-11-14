import constants
import utils
from .base_page import Base_Page

class String_Data_Page(Base_Page):
    _file_name = "STRINGS.md"

    def __init__(self, page):
        super().__init__(page)

    def open(self):
        self.page.click(constants.LOCATOR_STRINGDATA)
        assert self.page.wait_for_selector("#entries > div:nth-child(1)")