import constants
import utils

def test_get_data(page):
    check_page_loaded(page)

    dict_stringdata = get_entry_items(page, constants.LOCATOR_STRINGDATA)

    for entryhead, entryitems in dict_stringdata.items():
        utils.write_to_file(f"* {entryhead}\n")
        for name, value in entryitems.items():
            utils.write_to_file(f"  * {name}: {value}\n")

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

    utils.write_to_file("h1. EVENTS:\n")
    for group, names in list_entries_grouped.items():
        utils.write_to_file("\n* {}\n".format(group))
        for name in sorted(names):
            utils.write_to_file("  * {}\n".format(name))

def get_entry_items(page, module_locator):
    page.click(module_locator)
    assert page.wait_for_selector("#entries > div:nth-child(1)")

    list_entries_elements = page.query_selector_all('.entry')
    dict_entries = {}

    for n in range(len(list_entries_elements)-1):
        dict_entryitems = {}
        
        # entryhead_locator = f'.entry[{n+1}] .entryhead b'
        entryhead_locator = f"//div[@class='entry'][{n+1}]//div[@class='entryhead']/b"
        entryhead_element = page.query_selector(entryhead_locator)
        entryhead = entryhead_element.inner_text().strip() if entryhead_element else "Unknown"

        # entryitems_locator = f'.entry[{n+1}] .entryitem'
        entryitems_locator = f"//div[@class='entry'][{n+1}]//div[@class='entryitem']"
        list_entryitem_elements = page.query_selector_all(entryitems_locator)

        for m in range(len(list_entryitem_elements)-1):
            # entryitem_name_locator = f'.entry[{n+1}] .entryitem[{m+1}] b.entryitemname'
            entryitem_name_locator = f"//div[@class='entry'][{n+1}]//div[@class='entryitem'][{m+1}]//b[@class='entryitemname']"
            entryitem_name_element = page.query_selector(entryitem_name_locator)
            entryitem_name = entryitem_name_element.inner_text().strip() if entryitem_name_element else "Unknown"

            # entryitem_value_locator = f'.entry[{n+1}] .entryitem[{m+1}] a.entryitemvalue'
            entryitem_value_locator = f"//div[@class='entry'][{n+1}]//div[@class='entryitem'][{m+1}]//a[@class='entryitemvalue']"
            entryitem_value_element = page.query_selector(entryitem_value_locator)
            entryitem_value = entryitem_value_element.inner_text().strip() if entryitem_value_element else "Unknown"

            dict_entryitems[entryitem_name] = entryitem_value

        dict_entries[entryhead] = dict_entryitems
    
    return dict_entries


def wait_a_bit(page):
    page.wait_for_timeout(2000)

def record(header, list):
    # write to the file
    utils.write_to_file("h1. {}:\n\n".format(header.upper()))
    for event in list:
        utils.write_to_file('* ')
        utils.write_to_file(event)
        utils.write_to_file('\n')