import time
import utils

from constructors.event_constructor import Event_Constructor


def test_event_scenario_constuction():
    event_data = Event_Constructor()
    
    start_time = time.time()

    FINAL_DESTINATION = "data_final/ALL_EVENT_SCENARIO.md"

    # There are few specific events that are required, so I won't automate this
    # event_data = Event_Constructor()
    events = [
        # ,"event_season_iyafal_2023_t4"
        # ,"event_season_amasum_2023_t4"
        # "event_yaot_spring_2023"
        "event_anniversary_2023_t4"
        ,"event_halloween_2023_t4"
        ,"event_tanochwinter_2023_t4"
        ,"event_yaotspring_2024_t4"
    ]

    # SOMEDATA
    # * banner_treasures_2024_title: Treasures of Nimbus
    # * banner_treasures_2024_desc: Special items available for Nimbus Merits in the event market.

    # dia_amasum_2024_day01_end_1-15
    # * banner_amassarisummer_2024_title: Amassari Stories: Rise of the Kiithless
    # * banner_amassarisummer_2024_desc: Complete the Amassari Stories to receive legendary Amassari pilot Jothru Omassi.
    # /SOMEDATA
    
    body = "# HOMEWORLD MOBILE:\n"

    for event_id in events:
        print(f"Event Id: {event_id}")
        body += event_data.get_event_text(event_id)
        body += "\n"

    utils.rewrite_file(body, FINAL_DESTINATION)

    end_time = time.time()
    print(f"Chapter-String Data Test execution time is: {(start_time-end_time):.2f} seconds")