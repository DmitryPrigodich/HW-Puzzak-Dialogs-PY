import constants
import pytest
import utils

def test_get_events_list(page):
    check_page_loaded(page)
    get_events(page)
    wait_a_bit(page)


def check_page_loaded(page):
    # page.goto(constants.URL_HWM_DB)
    assert page.title() == "HWM Database"
    assert page.is_visible(constants.LOCATOR_EVENTDATA)
    assert page.is_visible("#entries")

def get_events(page):
    page.click(constants.LOCATOR_EVENTDATA)
    assert page.wait_for_selector("#entries > div:nth-child(1)")

    locator_entryhead = constants.LOCATOR_ENTRYHEAD
    locator_entryitem_group = constants.LOCATOR_ENTRYITEM.format("Group")

    # list_entryhead = page.query_selector_all(locator_entryhead)

    list_entries = page.query_selector_all('.entry')

    list_entries_grouped = {}

    for entry in list_entries:
        entryhead = entry.query_selector(locator_entryhead)
        event_name = entryhead.inner_text().strip() if entryhead else "Unknown"

        entryitem = entry.query_selector(locator_entryitem_group)
        group_name = entryitem.inner_text().strip() if entryitem else "No-Group"
   
        if group_name not in list_entries_grouped:
            list_entries_grouped[group_name] = []

        list_entries_grouped[group_name].append(event_name)

    for group, names in list_entries_grouped.items():
        utils.write_to_file("h1. EVENTS:\n\n")
        utils.write_to_file("* {}".format(group))
        for name in names:
            print(f"  - {name}")
            utils.write_to_file("  * {}".format(name))

    
    # # entries > div:nth-child(157) > div.entryinfo > div.entryhead > b
    # # entries > div:nth-child(157) > div.entryinfo > div:nth-child(2) > b
    # # entries > div:nth-child(157) > div.entryinfo > div:nth-child(2) > a

    # list_eventdata = page.query_selector_all(locator_entryitem_group)
    
    # list_events_unsorted = []

    # for eventdata in list_eventdata:
    #     text = eventdata.text_content().strip()
    #     list_events_unsorted.append(text)

    # return sorted(list(set(list_events_unsorted)))

def get_quests(page):
    page.click('#QuestLineData-module')
    assert page.wait_for_selector("#entries > div:nth-child(1)")

    locator_entryhead = constants.LOCATOR_ENTRYHEAD
    locator_entryitem_group = constants.LOCATOR_ENTRYITEM.format("QuestIds")

    # event_elements_list = page.query_selector_all(selector_event_group)
    
    # unsorted_event_list = []

    # for event_element in event_elements_list:
    #     text = event_element.text_content().strip()
    #     unsorted_event_list.append(text)

    # sorted_eventList = sorted(list(set(unsorted_event_list)))

    # return sorted_eventList


def wait_a_bit(page):
    page.wait_for_timeout(2000)

def record(header, list):
    # write to the file
    utils.write_to_file("h1. {}:\n\n".format(header.upper()))
    for event in list:
        utils.write_to_file('* ')
        utils.write_to_file(event)
        utils.write_to_file('\n')