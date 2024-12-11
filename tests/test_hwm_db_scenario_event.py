import time
import utils

from constructors.star_map_constructor import Star_Map_Constructor
from constructors.dia_seq_constructor import Dialog_Sequence_Constructor
from constructors.string_constructor import String_Data_Constructor
from constructors.quest_constructor import Quest_Constructor
from constructors.mission_constructor import Mission_Constructor
from constructors.mission_step_constructor import Mission_Step_Constructor
from constructors.mission_step_actions_constructor import Mission_Step_Actions_Constructor
from constructors.event_constructor import Event_Constructor


def test_event_scenario_constuction():
    start_time = time.time()

    FINAL_DESTINATION = "data/ALL_EVENT_SCENARIO.md"

    events = [
        # "event_yaot_spring_2023"
        # ,"event_season_amasum_2023_t4"
        # ,"event_season_iyafal_2023_t4"
        "event_halloween_2023_t4"
        ,"event_tanochwinter_2023_t4"
        ,"event_anniversary_2023_t4"
        ,"event_yaotspring_2024_t4"
    ]
    # * banner_treasures_2024_title: Treasures of Nimbus
    # * banner_treasures_2024_desc: Special items available for Nimbus Merits in the event market.

    # * banner_yaotspring_2024_title: Yaot Stories: Tainted Conjunction
    # * banner_yaotspring_2024_desc: Complete the Yaot Stories to receive legendary Yaot gunner Chocoan Coatl.

    # * banner_monthly_mar_2024_title: Nimbus Stories: A New Home
    # * banner_monthly_mar_2024_desc: Special items available for Nimbus Merits in the event market.

    # * banner_amassarisummer_2024_title: Amassari Stories: Rise of the Kiithless
    # * banner_amassarisummer_2024_desc: Complete the Amassari Stories to receive legendary Amassari pilot Jothru Omassi.

    # event_data = Event_Constructor()
    quests_data = Quest_Constructor()
    string_data = String_Data_Constructor()

    body = "# HOMEWORLD MOBILE:\n"
    for event_id in events:
        body += f"EVENT: {event_id}\n"

        quests = quests_data.get_event_quests(event_id)
        for quest_id in quests:
            print(f"Working on {event_id}/{quest_id}")
            quest_info = quests_data.get_quest_by_id(quest_id)

            q_name = quest_info.get('Name:')
            q_description = quest_info.get('Description:')
            q_goals = quests_data._get_goal_body_formatted(quest_info.get('Goals:'))

            q_name = utils.remove_color(q_name)
            q_description = utils.remove_color(q_description)

            body += f"\n### {quest_id}\n"
            body += f"**GOALS**:\n{q_goals}\n"
            if q_name != q_description:
                body += f"**NAME**:\n{q_name}\n"
            body += f"**DESCRIPTION**:\n{q_description}\n"
            # print(f"{q_name} : {q_description}")

    utils.rewrite_file(body, FINAL_DESTINATION)

    end_time = time.time()
    print(f"Chapter-String Data Test execution time is: {(start_time-end_time):.2f} seconds")

