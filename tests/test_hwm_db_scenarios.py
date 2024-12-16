import time
import utils

from constructors.event_constructor import Event_Constructor
from constructors.chapter_constructor import Chapter_Constructor


def test_events_scenarios_construction():
    event_data = Event_Constructor()
    
    start_time = time.time()

    FINAL_DESTINATION = "data_final/ALL_EVENT_SCENARIO.md"

    # There are few specific events that are required, so I won't automate this, 
    # but you can try checking other quests
    # event_data = Event_Constructor()
    events = [
        "event_yaot_spring_2023" #has no string data anymore
        ,"event_iyafal_2023_t4"
        ,"event_iyafal_2023_epilog_t4"
        ,"event_anniversary_2023_t4"
        ,"event_halloween_2023_t4"
        ,"event_tanochwinter_2023_t4"
        ,"event_yaotspring_2024_t4"
        ,"event_amasum_2023_t4"
    ]

    body = utils.format_heading1("HOMEWORLD MOBILE EVENTS")
    body += utils.format_br(2)

    for event_id in events:
        print(f"Event Id: {event_id}")
        body += event_data.get_event_text(event_id)
        body += utils.format_br(1)

    utils.rewrite_file(body, FINAL_DESTINATION)

    end_time = time.time()
    print(f"Event Scenarios construction time is: {(start_time-end_time):.2f} seconds")


def test_chapter_scenarios_construction():
    start_time = time.time()

    chapter_data = Chapter_Constructor()

    FINAL_DESTINATION = "data_final/ALL_CHAPTER_SCENARIO.md"

    body = utils.format_heading1("HOMEWORLD MOBILE CHAPTERS SCRIPT")
    body += utils.format_br(2)

    for chapter_id in chapter_data.get_chapters():
        print(f"Chapter Id: {chapter_id}")
        body += chapter_data.get_chapter_text(chapter_id)
        body += utils.format_br(1)

    utils.rewrite_file(body, FINAL_DESTINATION)

    end_time = time.time()
    print(f"Chapter Scenarios construction time is: {(start_time-end_time):.2f} seconds")
