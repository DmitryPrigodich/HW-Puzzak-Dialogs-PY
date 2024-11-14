import utils
import logging
import time
from pages.constellation_data import Constellation_Data_Page
from pages.event_data import Event_Data_Page
from pages.quest_line_data import Quest_Line_Data_Page
from pages.quest_data import Quest_Data_Page
from pages.string_data import String_Data_Page

logger = logging.getLogger(__name__)

# def test_benchmark(page, benchmark):
#     def run_test():
#         # test_constellation_data(page)
#         # test_event_data(page)
#         test_quest_line_data(page)
#     benchmark(run_test)

def test_constellation_data(page):
    start_time = time.time()
    constellation_data = Constellation_Data_Page(page)
    assert constellation_data.get_star_system_by_coordinates("[-831, -204]")['name'] == "DANDITA"
    # constellations_data.record_to_file()
    end_time = time.time()
    print(f"Constellation Data search time is: {(start_time-end_time):.2f} seconds")

def test_event_data(page):
    start_time = time.time()
    event_data = Event_Data_Page(page)
    assert event_data.get_group_by_event("event_7days_2023_08_21_t1") == "event_7days_2023_08"
    assert "event_7days_2023_08_21_t1" in event_data.get_events_by_group("event_7days_2023_08")
    # event_data.record_to_file()
    end_time = time.time()
    print(f"Event Data search time is: {(start_time-end_time):.2f} seconds")

def test_quest_line_data(page):
    start_time = time.time()
    quest_line_data = Quest_Line_Data_Page(page)
    assert "ql_event_YaotSpring_2024_t4".lower() == quest_line_data.get_quest_line_by_quest("qe_yaoSpr_2024_day08_t4")
    assert "qe_yaoSpr_2024_day08_t4" in quest_line_data.get_quests_by_event("event_yaotSpring_2024_t4")
    # quest_line_data.record_to_file()
    end_time = time.time()
    print(f"Quest Line Data search time is: {(start_time-end_time):.2f} seconds")
 
def _test_quest_data(page):
    start_time = time.time()
    quest_data = Quest_Data_Page(page)
    # assert 
    quest_data.record_to_file()
    end_time = time.time()
    print(f"Quest Data search time is: {(start_time-end_time):.2f} seconds")

def _test_string_data(page):
    start_time = time.time()
    string_data = String_Data_Page(page)
    assert "Donate" == string_data.get_text_by_header("send")
    string_data.record_to_file()
    end_time = time.time()
    print(f"Quest Data search time is: {(start_time-end_time):.2f} seconds")

def _test_tryout(page):
        start_time = time.time()

        # event = "event_anniversary_2023_t4"

        event_data = Event_Data_Page(page)
        event_data.open()
        event_data.save_events()

        quest_line_data = Quest_Line_Data_Page(page)
        quest_line_data.open()
        quest_line_data.save_quest_lines()

        utils.rewrite_file(f"# EVENTS and QUESTS:\n", "OUTPUT.md")
        for event_group in event_data.event_groups:
            event = event_group + "_t4"
            quests = quest_line_data.get_quests_by_event(event)
            if quests:
                utils.add_to_file(f"\n## Event: {event_group}\n", "OUTPUT.md")
                for quest in quests:
                    utils.add_to_file(f"* {quest}\n", "OUTPUT.md")
       
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


        end_time = time.time()
        print(f"Event Data search time is: {(start_time-end_time):.2f} seconds")

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
