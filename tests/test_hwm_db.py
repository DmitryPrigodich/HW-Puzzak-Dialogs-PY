import utils
import logging
import time
import pytest

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

def _test_constellation_data(page):
    start_time = time.time()
    constellation_data = Constellation_Data_Page(page)
    assert constellation_data.get_star_system_by_coordinates("[-831, -204]")['name'] == "DANDITA"
    assert "DANDITA" in constellation_data.get_star_systems_by_faction("Amassari")
    constellation_data.record_to_file()
    end_time = time.time()
    print(f"Constellation Data search time is: {(start_time-end_time):.2f} seconds")

def _test_event_data(page):
    start_time = time.time()
    event_data = Event_Data_Page(page)
    assert event_data.get_group_by_event("event_7days_2023_08_21_t1") == "event_7days_2023_08"
    assert "event_7days_2023_08_21_t1" in event_data.get_events_by_group("event_7days_2023_08")
    event_data.record_to_file()
    end_time = time.time()
    print(f"Event Data search time is: {(start_time-end_time):.2f} seconds")

def _test_quest_line_data(page):
    start_time = time.time()
    quest_line_data = Quest_Line_Data_Page(page)
    assert "ql_event_YaotSpring_2024_t4".lower() == quest_line_data.get_quest_line_by_quest("qe_yaoSpr_2024_day08_t4")
    assert "qe_yaoSpr_2024_day08_t4" in quest_line_data.get_quests_by_event("event_yaotSpring_2024_t4")
    quest_line_data.record_to_file()
    end_time = time.time()
    print(f"Quest Line Data search time is: {(start_time-end_time):.2f} seconds")
 
def test_string_data(page):
    start_time = time.time()
    string_data = String_Data_Page(page)
    assert "Donate" == string_data.get_text_by_header("send")
    string_data.record_to_file()
    end_time = time.time()
    print(f"String Data search time is: {(start_time-end_time):.2f} seconds")

def _test_quest_data(page):
    start_time = time.time()
    quest_data = Quest_Data_Page(page)
    # assert 
    quest_data.record_to_file()
    quest_data.record_tags_to_file()

    quest_data.get_tag_values("Type")
    quest_data.get_tag_values("Tier")
    quest_data.get_tag_values("RepetitionType")
    quest_data.get_tag_values("ScheduleType")
    quest_data.get_tag_values("GoalIconId")
    quest_data.get_tag_values("Goals")

    quest_data.get_tag_values("EventId")
    quest_data.get_tag_values("ReplayMissionId")
    quest_data.get_tag_values("CinematicIds")
    quest_data.get_tag_values("MailsOnCompletion") 

    quest_data.get_tag_values("GoalParameters")

    end_time = time.time()
    print(f"Quest Data search time is: {(start_time-end_time):.2f} seconds")

def _test_chapter_data(page):
    start_time = time.time()
    chapter_data = Chapter_Data_Page(page)
    # assert
    chapter_data.record_to_file()
    end_time = time.time()
    print(f"Chapter Data search time is: {(start_time-end_time):.2f} seconds")

def test_hint_data(page):
    start_time = time.time()
    hint_data = Loading_Hint_Data_Page(page)
    # assert
    hint_data.record_to_file()
    end_time = time.time()
    print(f"Hint Data search time is: {(start_time-end_time):.2f} seconds")

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
    print(f"Event Data search time is: {(start_time-end_time):.2f} seconds")
