import pytest
import constants

@pytest.fixture(scope="function", autouse=True)
def before_each_test(page):
    page.goto(constants.URL_HWM_DB)