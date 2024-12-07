import time

from constructors.string_constructor import String_Data_Constructor
from constructors.hints_constructor import Hint_Data_Constructor

from constructors.star_map_constructor import Star_Map_Constructor
from constructors.quest_constructor import Quest_Constructor
from constructors.dia_seq_constructor import Dialog_Sequence_Constructor
from constructors.mission_constructor import Mission_Constructor
from constructors.mission_step_constructor import Mission_Step_Constructor
from constructors.mission_step_actions_constructor import Mission_Step_Actions_Constructor


def test_refill_string_data():
    start_time = time.time()

    string_data = String_Data_Constructor()
    string_data.write_json()
    string_data.write_data()

    end_time = time.time()
    print(f"Test execution time is: {(end_time - start_time):.2f} seconds")

def test_refill_hint_data():
    start_time = time.time()

    hint_data = Hint_Data_Constructor()
    hint_data.write_json()
    hint_data.write_data()

    end_time = time.time()
    print(f"Test execution time is: {(end_time - start_time):.2f} seconds")


def test_refill_starmap_data():
    start_time = time.time()

    starmap_data = Star_Map_Constructor()
    starmap_data.write_json()
    starmap_data.write_data()

    end_time = time.time()
    print(f"Test execution time is: {(end_time - start_time):.2f} seconds")


def test_refill_events_data():
    start_time = time.time()

    events_data = Star_Map_Constructor()
    events_data.write_json()
    events_data.write_data()

    end_time = time.time()
    print(f"Test execution time is: {(end_time - start_time):.2f} seconds")


def test_refill_chapter_data():
    start_time = time.time()

    chapter_data = Star_Map_Constructor()
    chapter_data.write_json()
    chapter_data.write_data()

    end_time = time.time()
    print(f"Test execution time is: {(end_time - start_time):.2f} seconds")


def test_refill_quest_data():
    start_time = time.time()

    quests_data = Quest_Constructor()
    quests_data.write_json()
    quests_data.write_data()
    quests_data.write_quest_lines()

    end_time = time.time()
    print(f"Test execution time is: {(end_time - start_time):.2f} seconds")


def test_refill_missions_data():
    start_time = time.time()

    mission_data = Star_Map_Constructor()
    mission_data.write_json()
    mission_data.write_data()

    end_time = time.time()
    print(f"Test execution time is: {(end_time - start_time):.2f} seconds")

def test_refill_officers_data():
    start_time = time.time()

    mission_data = Star_Map_Constructor()
    mission_data.write_json()
    mission_data.write_data()

    end_time = time.time()
    print(f"Test execution time is: {(end_time - start_time):.2f} seconds")

def test_refill_dialog_data():
    start_time = time.time()

    mission_data = Star_Map_Constructor()
    mission_data.write_json()
    mission_data.write_data()

    end_time = time.time()
    print(f"Test execution time is: {(end_time - start_time):.2f} seconds")