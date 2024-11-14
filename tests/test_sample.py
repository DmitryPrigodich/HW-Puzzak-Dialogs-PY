import constants
import utils
import logging
from pages.constellation_data import Constellation_Data_Page
from pages.event_data import Event_Data_Page

logger = logging.getLogger(__name__)

def _test_constellation_data(page):
    constellation_data = Constellation_Data_Page(page)
    constellation_data.open()
    constellation_data.save_star_systems()
    assert constellation_data.get_star_system_by_coordinates("[-831, -204]")['name'] == "DANDITA"
    # constellations_data.output_star_systems()

def test_event_data(page):
    event_data = Event_Data_Page(page)
    event_data.open()
    event_data.save_events()
    assert event_data.get_group_by_event("event_7days_2023_08_21_t1") == "event_7days_2023_08"
    # event_data.output_events()
 
def tryout(page):
    event = "event_anniversary_2023_t4"
    # We get events from EventData - event - event_anniversary_2023
    # We get questlines from QuestLineData - ql_event
    # We get quests from QuestData - qe_event_*

    # quests = get_all_quests(event)

    #QuestData
    # head
    # MailsOnCompletion: m_anniversary_enoch_log
    # StringData: m_anniversary_enoch_log_header m_anniversary_enoch_log_body


    



    # if quest.mail 
    #     print(stringdata(quest.mail.text + header).entry)
    #     print("\n")
    #     print(stringdata(quest.mail.text + body).entry)

    # utils.rewrite_file(f"h1. {constants.LOCATOR_QUESTDATA.upper()}\n\n")
    # record_entries(dict_data)

    # utils.wait_a_bit(page)


def get_questline_list(page):
    page.click(constants.LOCATOR_QUESTLINEDATA)
    assert page.wait_for_selector("#entries > div:nth-child(1)")

    questlines = {}

    list_elements_entries = page.query_selector_all('.entry')

    for entry_element in list_elements_entries:
        entryhead_element = entry_element.query_selector(constants.LOCATOR_ENTRYHEAD)
        questline = entryhead_element.inner_text().strip() if entryhead_element else "Unknown"

        entryitem_element = entry_element.query_selector(constants.LOCATOR_ENTRYITEM_SPECIFIC.format('QuestIds'))
        quests = entryhead_element.inner_text().strip() if entryitem_element else "Unknown"

        questlines[questline] = quests.split(":")
    return questlines

def get_quest_list(event):
    questline = "ql_" + event
    quest_list = []
    #quest retrieval and parsing logic here
    return quest_list

def get_entry_items(page, module_locator):
    logger.info("get_entry_items")
    page.click(module_locator)
    assert page.wait_for_selector("#entries > div:nth-child(1)")

    logger.info("Going through all entries")
    list_entries_elements = page.query_selector_all('.entry')
    dict_entries = {}

    for n in range(len(list_entries_elements)-1):
        dict_entryitems = {}
        
        entryhead_locator = f"//div[@class='entry'][{n+1}]//div[@class='entryhead']/b"
        entryhead_element = page.query_selector(entryhead_locator)
        entryhead = entryhead_element.inner_text().strip() if entryhead_element else "Unknown"
        logger.info(f"{n+1}. Entryhead: {entryhead}")

        entryitems_locator = f"//div[@class='entry'][{n+1}]//div[@class='entryitem']"
        list_entryitem_elements = page.query_selector_all(entryitems_locator)

        for m in range(len(list_entryitem_elements)-1):
            entryitem_name_locator = f"//div[@class='entry'][{n+1}]//div[@class='entryitem'][{m+1}]//b[@class='entryitemname']"
            entryitem_name_element = page.query_selector(entryitem_name_locator)
            entryitem_name = entryitem_name_element.inner_text().strip() if entryitem_name_element else "Unknown"

            entryitem_value_locator = f"//div[@class='entry'][{n+1}]//div[@class='entryitem'][{m+1}]//a[@class='entryitemvalue']"
            entryitem_value_element = page.query_selector(entryitem_value_locator)
            entryitem_value = entryitem_value_element.inner_text().strip() if entryitem_value_element else "Unknown"

            logger.info(f"{n+1}.{m+1}. {entryitem_name} {entryitem_value}")

            dict_entryitems[entryitem_name] = entryitem_value

        dict_entries[entryhead] = dict_entryitems
    
    return dict_entries

def record_entries(dict_moduledata):
    logger.info("record_entries")
    for entryhead, entryitems in dict_moduledata.items():
        utils.add_to_file(f"* {entryhead}\n")
        for itemname, itemvalue in entryitems.items():
            utils.add_to_file(f"  * {itemname}: {itemvalue}\n")
