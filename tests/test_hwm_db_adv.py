import utils
import logging
import time

from pages.event_data import Event_Data_Page
from pages.quest_data import Quest_Data_Page
from pages.string_data import String_Data_Page
from pages.quest_line_data import Quest_Line_Data_Page
from pages.constellation_data import Constellation_Data_Page
from pages.chapter_data import Chapter_Data_Page
from pages.loading_hint_data import Loading_Hint_Data_Page

logger = logging.getLogger(__name__)

# def test_benchmark(page, benchmark):
#     def run_test():
#         # test_constellation_data(page)
#         # test_event_data(page)
#         test_quest_line_data(page)
#     benchmark(run_test)

# @pytest.mark.asyncio
# async def _test_async(page):
#     start_time = time.time()
#     end_time = time.time()
#     print(f"Event Data search time is: {(start_time-end_time):.2f} seconds")

def test_hint_strings(page):
    start_time = time.time()

    body = "# HWM HINTS with descriptions:\n"

    hint_headers = Loading_Hint_Data_Page(page)
    string_data = String_Data_Page(page)
    
    for hint_header in hint_headers:
        hint_string = string_data.get_text_by_header(hint_header)
        body += f"* *{hint_header}:*\n"
        body += f"  * {hint_string}\n"

    utils.add_to_file(body, "data/HINTS.md")
    
    end_time = time.time()
    logger.log(f"Hint Data String search time is: {(start_time-end_time):.2f} seconds")

def _test_tryout(page):
    event = "event_anniversary_2023_t4"
    body = ""
    
    start_time = time.time()

    event_data = Event_Data_Page(page)
    quest_line_data = Quest_Line_Data_Page(page)
    quest_data = Quest_Data_Page(page)

    body += f"# EVENTS and QUESTS:\n"
    quests = quest_line_data.get_quests_by_event(event)
    if quests:
        body += f"\n## Event: {event}\n"
        for quest in quests:
            body += f"* {quest}\n"
       
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

    utils.rewrite_file(body, "OUTPUT.md")

    end_time = time.time()
    logger.log(f"General Data search time is: {(start_time-end_time):.2f} seconds")