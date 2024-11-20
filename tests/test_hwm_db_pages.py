import time
import utils

from pages.event_data import Event_Data_Page
from pages.quest_data import Quest_Data_Page
from pages.string_data import String_Data_Page
from pages.chapter_data import Chapter_Data_Page
from pages.officer_data import Officer_Data_Page
from pages.quest_line_data import Quest_Line_Data_Page
from pages.loading_hint_data import Loading_Hint_Data_Page
from pages.constellation_data import Constellation_Data_Page
from pages.dialog_sequence_data import Dialog_Seq_Data_Page


def _test_constellation_data(page):
    start_time = time.time()

    constellation_data = Constellation_Data_Page(page)
    constellation_data.save_data()
    constellation_data.write_data()
    constellation_data.write_json()
    
    constellation_data.read_json()
    assert constellation_data.get_star_system_by_coordinates("[-831, -204]")['name'] == "DANDITA"
    
    end_time = time.time()
    print(f"Constellation Data Test execution time is: {(start_time-end_time):.2f} seconds")

def _test_officer_data(page):
    start_time = time.time()

    officer_data = Officer_Data_Page(page)
    officer_data.save_data()
    officer_data.write_data()
    officer_data.write_json()

    officer_data.read_json()
    assert officer_data.check_officer("RaabSjet")

    end_time = time.time()
    print(f"Officer Data Test execution time is: {(start_time-end_time):.2f} seconds")

def _test_quest_line_data(page):
    start_time = time.time()

    quest_line_data = Quest_Line_Data_Page(page)
    quest_line_data.save_data()
    quest_line_data.write_data()
    quest_line_data.write_json()

    quest_line_data.read_json()
    assert "qs_exploration_02" in quest_line_data.get_quests_by_quest_line("ql_side_exploration")

    end_time = time.time()
    print(f"Quest Line Data Test execution time is: {(start_time-end_time):.2f} seconds")

def _test_event_data(page):
    start_time = time.time()

    event_data = Event_Data_Page(page)
    event_data.save_data()
    event_data.write_data()
    event_data.write_json()

    event_data.read_json()
    assert event_data.check_event("event_we_headhunt_t1_2023_12_22")
    
    end_time = time.time()
    print(f"Event Data Test execution time is: {(start_time-end_time):.2f} seconds")

def _test_string_data(page):
    start_time = time.time()

    string_data = String_Data_Page(page)
    string_data.save_data()
    string_data.write_data()
    string_data.write_json()

    string_data.read_json()
    assert string_data.get_text_by_header("send") == "Donate"

    end_time = time.time()
    print(f"String Data Test execution time is: {(start_time-end_time):.2f} seconds")

def _test_hint_data(page):
    start_time = time.time()
    
    hint_data = Loading_Hint_Data_Page(page)
    hint_data.save_data()
    hint_data.write_data()
    hint_data.write_json()

    hint_data.read_json()
    assert hint_data.get_hint("hint_msg_35")

    end_time = time.time()
    print(f"Hint Data Test execution time is: {(start_time-end_time):.2f} seconds")

def _test_hint_string_data(page):
    start_time = time.time()
    
    hint_data = Loading_Hint_Data_Page(page)
    hint_data.read_json()
    string_data = String_Data_Page(page)
    string_data.read_json()

    hint_strings = {}
    for hint_header in hint_data._hints:
        hint_text = string_data.get_text_by_header(hint_header)
        hint_strings[hint_header] = hint_text
    assert hint_strings["hint_msg_2"] == "Beam-based weapons have a slow firing rate, but very long range."

    utils.write_json(hint_strings, "json/hint_strings.json")

    body = "# HWM HINTS with STRINGS:\n\n"
    for hint_header, hint_string in hint_strings.items():
        body += f"* {hint_header}: {hint_string}\n"
    utils.rewrite_file(body, "data/HINT_STRINGS.md")

    end_time = time.time()
    print(f"Hint Data search time is: {(start_time-end_time):.2f} seconds")

def _test_chapter_data(page):
    start_time = time.time()

    chapter_data = Chapter_Data_Page(page)
    chapter_data.save_data()
    chapter_data.write_data()
    chapter_data.write_json()

    chapter_data.read_json()
    assert chapter_data.check_chapter("chapter_main_t1_05")

    end_time = time.time()
    print(f"Chapter Data Test execution time is: {(start_time-end_time):.2f} seconds")

def _test_chapter_string_data(page):
    start_time = time.time()
    
    chapter_data = Chapter_Data_Page(page)
    chapter_data.read_json()
    string_data = String_Data_Page(page)
    string_data.read_json()

    chapter_strings = {}
    for chapter in chapter_data._chapters:
        chapter_name = string_data.get_text_by_header(f"chaptername_{chapter['header']}")
        chapter_w_name = {
                "header": chapter['header'],
                "name": chapter_name,
                "order": chapter['order'],
                "quest_lines": chapter['quest_lines']
        }
        chapter_strings[chapter['header']] = chapter_w_name
    utils.write_json(chapter_strings, "json/chapter_strings.json")

    body = "# HWM CHAPTERS with STRINGS:\n"
    for chapter_header, chapter_data in chapter_strings.items():
        body += f"\n## {chapter_data['order']}. {chapter_data['name']}\n"
        for quest_line in chapter_data['quest_lines']:
            body += f"* {quest_line}\n"
    utils.rewrite_file(body, "data/CHAPTER_STRINGS.md")

    #TODO: add quest_line & quest strings

    end_time = time.time()
    print(f"Chapter-String Data Test execution time is: {(start_time-end_time):.2f} seconds")

def _test_event_quest_line_data(page):
    start_time = time.time()

    event_data = Event_Data_Page(page)
    event_data.read_json()
    quest_line_data = Quest_Line_Data_Page(page)
    quest_line_data.read_json()

    end_time = time.time()
    print(f"Event Data Test execution time is: {(start_time-end_time):.2f} seconds")

    #TODO: add quest and quest strings

def _test_dialog_sequence_data(page):
    start_time = time.time()

    dia_seq_data = Dialog_Seq_Data_Page(page)
    dia_seq_data.save_data()
    dia_seq_data.write_data()
    dia_seq_data.write_json()

    dia_seq_data.read_json()
    assert dia_seq_data.get_dialog_seq_by_header("e_anniversary2023_Wiracoda_intro")[1]['speaker'] == "RaabSjet"

    end_time = time.time()
    print(f"Chapter Data Test execution time is: {(start_time-end_time):.2f} seconds")

    #TODO: add dialogue strings, add speakers

def _test_dialog_sequence_string_data(page):
    start_time = time.time()

    dia_seq_data = Dialog_Seq_Data_Page(page)
    dia_seq_data.read_json()
    assert dia_seq_data.get_dialog_seq_by_header("e_anniversary2023_Wiracoda_intro")[1]['speaker'] == "RaabSjet"

    end_time = time.time()
    print(f"Chapter Data Test execution time is: {(start_time-end_time):.2f} seconds")

def _test_quest_data(page):
    start_time = time.time()
    quest_data = Quest_Data_Page(page)
    # assert 
    quest_data.write_data()
    quest_data.record_tags_to_file()

    quest_data.write_tag_values("Type")
    quest_data.write_tag_values("Tier")
    quest_data.write_tag_values("RepetitionType")
    quest_data.write_tag_values("ScheduleType")
    quest_data.write_tag_values("GoalIconId")
    quest_data.write_tag_values("Goals")

    quest_data.write_tag_values("EventId")
    quest_data.write_tag_values("ReplayMissionId")
    quest_data.write_tag_values("CinematicIds")
    quest_data.write_tag_values("MailsOnCompletion") 

    quest_data.write_tag_values("GoalParameters")

    end_time = time.time()
    print(f"Quest Data Test execution time is: {(start_time-end_time):.2f} seconds")
