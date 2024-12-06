import time
import utils

from constructors.star_map_constructor import Star_Map_Constructor
from constructors.dia_seq_constructor import Dialog_Sequence_Constructor
from constructors.string_constructor import String_Data_Constructor
from constructors.quest_constructor import Quest_Constructor
from constructors.mission_constructor import Mission_Constructor
from constructors.mission_step_constructor import Mission_Step_Constructor
from constructors.mission_step_actions_constructor import Mission_Step_Actions_Constructor
from constructors.chapter_constructor import Chapter_Constructor

def test_chapter_scenario_constuction():
    start_time = time.time()

    FINAL_DESTINATION = "data/ALL_CHAPTER_SCENARIO.md"

    chapter_data = Chapter_Constructor()
    quests_data = Quest_Constructor()
    string_data = String_Data_Constructor()

    chapters_json = chapter_data.get_chapters()

    body = "# HOMEWORLD MOBILE:\n"
    body += "The Script\n\n"

    for key, chapter in chapters_json.items():
        chapter_order = chapter.get('order')
        chapter_name = chapter.get('name')
        chapter_quests = chapter.get('quest_lines')

        body += f"## {chapter_order}. {chapter_name}\n\n"
        for quest_id in chapter_quests:
            if quest_id.startswith("qm"):
                quests_data.get_quest_text(quest_id)
            else:
                quests = quests_data.get_quests_by_quest_line_id(quest_id)
                for quest_id in quests:
                    quests_data.get_quest_text(quest_id)

    utils.rewrite_file(body, FINAL_DESTINATION)

    end_time = time.time()
    print(f"Chapter-String Data Test execution time is: {(start_time-end_time):.2f} seconds")

    def get_cinematic_lines(cinematic_ids):
        cine_body = ""

        if cinematic_ids:
            # Going Manual
            match cinematic_ids:
                case "20:10:25":
                    # first video
                    cine_body += string_data.get_cinematics_lines("001") + "\n"
                    #second video
                    cine_body += string_data.get_cinematics_lines("002") + "\n"
                    #third video
                    cine_body += string_data.get_cinematics_lines("007") + "\n"

                case "30":
                    #forth video
                    cine_body += string_data.get_cinematics_lines("003") + "\n"
                    #missing video
                    cine_body += string_data.get_cinematics_lines("004") + "\n"

                case "40":
                    # fifth video
                    cine_body += string_data.get_cinematics_lines("006") + "\n"
                    #sixth video
                    cine_body += string_data.get_cinematics_lines("005") + "\n"
        return cine_body



