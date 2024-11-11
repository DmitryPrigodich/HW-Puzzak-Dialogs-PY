import constants
import pytest
import utils

def test_get_events_list(page):
    # page.goto(constants.URL_HWM_DB)
    assert page.title() == "HWM Database"
    assert page.is_visible("#EventData-module")
    assert page.is_visible("#entries")
    # assert page.wait_for_selector()

    page.click("#EventData-module")
    assert page.wait_for_selector("#entries > div:nth-child(1)")
    # entries > div:nth-child(157) > div.entryinfo > div:nth-child(2) > a
    selectorGroups = '//div[@class="entry"]//div[@class="entryitem"][b[@class="entryitemname" and contains(text(), "Group")]]/a[@class="entryitemvalue"]'
    event_elements_list = page.query_selector_all(selectorGroups)
    
    unsorted_event_list = []

    for event_element in event_elements_list:
        text = event_element.text_content().strip()
        unsorted_event_list.append(text)

    
    sorted_eventList = sorted(list(set(unsorted_event_list)))

    for event in sorted_eventList:
        utils.write_in_file(event)

    page.wait_for_timeout(10000)

