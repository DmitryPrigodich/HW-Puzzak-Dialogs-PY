import time
import utils

from constructors.event_constructor import Event_Constructor
from constructors.chapter_constructor import Chapter_Constructor


def test_events_scenarios_construction():
    event_data = Event_Constructor()
    
    start_time = time.time()

    FINAL_DESTINATION = "data_final/ALL_EVENT_SCENARIO.md"

    # There are few specific events that are required, so I won't automate this
    # event_data = Event_Constructor()
    events = [
        "event_yaot_spring_2023" #has no string data anymore
        ,"event_anniversary_2023_t4"
        ,"event_halloween_2023_t4"
        ,"event_tanochwinter_2023_t4"
        ,"event_yaotspring_2024_t4"
        ,"event_amasum_2023_t4"
        ,"event_iyafal_2023_t4"
        ,"event_iyafal_2023_epilog_t4"
    ]

        # dia_iyafal_2023_day01
        # event_iyafal2023_escort_t1

        # * event_iyafal2023_escort_t1: Trader's Bargain T1
        # * event_iyafal2023_escort_t2: Trader's Bargain T2
        # * event_iyafal2023_escort_t3: Trader's Bargain T3
        # * event_iyafal2023_escort_t4: Trader's Bargain T4
        # * desc_event_iyafal2023_escort_tx: The missing captain has been located at an unnamed asteroid. Retrieve him at all costs.
        # * e_iyafall2023_escort_intro_1: Hiigaran vessel, this is Captain Mahel. Praise Sajuuk you arrived, I couldn't break cover without an escort.
        # * e_iyafall2023_escort_intro_2: We're here to assist and extract you, Captain.
        # * e_iyafall2023_escort_intro_3: I must transmit crucial data using this base's equipment, but the Iyatequa are on to me. I can't go without escort.
        # * e_iyafall2023_escort_go_1: We'll cover you. Begin your run.
        # * e_iyafall2023_escort_wave1a_1: Cangacians incoming! They are coming for the bounty on my head. The Iyatequa don't want the information I have getting out.
        # * e_iyafall2023_escort_wave1b_1: Attention, a new wave has come out of hyperspace behind us.
        # * e_iyafall2023_escort_mines_1: Commander, we've detected a mine field ahead. We must clear the path to give Captain Mahel a straight shot to the station.
        # * e_iyafall2023_escort_wave2_1: Commander, another wave has appeared. The bounty must be huge to send a fleet this big just for me.
        # * e_iyafall2023_escort_countdown_1: I've docked. My crew has hooked up the transmitter... sending now.
        # * e_iyafall2023_escort_wave3_1: More ships have emerged from Hyperspace. The Iyatequa really want this information burried.
        # * e_iyafall2023_escort_killall_1: Looks like the Cangaicans ran out of ships. All hostiles destroyed, proceed on mission.
        # * e_iyafall2023_escort_win_1: Transmission to Lazarus base completed. It's done, the word is out.
        # * e_iyafall2023_escort_win_2: The Cangacians are retreating. What information did you have?
        # * e_iyafall2023_escort_win_3: The Iyatequa have been selling our Progenitor control codes.
        # * e_iyafall2023_escort_win_4: If the powers here can command Progenitor units like we used to, it's going to be disasterous for the balance of power in this area.
        # * e_iyafall2023_escort_allylow_1: Commander, our ship is in danger! Please assist!
        # * e_iyafall2023_escort_fail_1: Mahel's ship is destroyed! Abort mission!
        # * goaltxt_h_event_iyafall2023_escort_goal_escort: Escort Mahel to the station.
        # * goaltxt_h_event_iyafall2023_escort_goal_countdown: Data transfer...
        # * goaltxt_h_event_iyafall2023_escort_goal_defend: Defend Mahel.


        # * m_iyafal_day4_log_header: Captain’s Log, Mahel Manaan
        # * m_iyafal_day4_log_body: Day 547
        # When I was a boy, my father would tell me stories of the Trader’s Bargain. Long gone now, I can picture that lone standing stone at the edge of the Shiiaro Mountains. The Manaan remember it as a promise of the joy to come. Now, I think of how solitary it was standing above the sands alone.
        # * m_iyafal_day8_log_header: Captain’s Log, Mahel Manaan
        # * m_iyafal_day8_log_body: Day 562
        # Today I’m reminded of an old saying among us Manaani. Fourteen days, fourteen turns, and fourteen hundred lost to that day on the dancing sands. Such a joyous day that changed our people so dramatically and without warning.
        # * m_iyafal_day12_log_header: Captain’s Log, Mahel Manaan
        # * m_iyafal_day12_log_body: Day 577
        # It is said the Kaalel have no true friends, but every one is a true friend to the Manaan. I can’t think of a better way to describe my time among these Iyatequa: The lone Manaan against these secret-keepers. But the old Manaan adage is still true: the slight of hand is more powerful than anything any coin could ever buy. Now is a war between magicians.


    body = "# HOMEWORLD MOBILE EVENTS"

    for event_id in events:
        print(f"Event Id: {event_id}")
        body += event_data.get_event_text(event_id)
        body += "\n"

    utils.rewrite_file(body, FINAL_DESTINATION)

    end_time = time.time()
    print(f"Event Scenarios construction time is: {(start_time-end_time):.2f} seconds")


def test_chapter_scenarios_construction():
    start_time = time.time()

    FINAL_DESTINATION = "data_final/ALL_CHAPTER_SCENARIO.md"

    body = "# HOMEWORLD MOBILE CHAPTERS SCRIPT"

    chapter_data = Chapter_Constructor()
    for chapter_id in chapter_data.get_chapters():
        print(f"Chapter Id: {chapter_id}")
        body += chapter_data.get_chapter_text(chapter_id)
        body += "\n"

    utils.rewrite_file(body, FINAL_DESTINATION)

    end_time = time.time()
    print(f"Chapter Scenarios construction time is: {(start_time-end_time):.2f} seconds")    