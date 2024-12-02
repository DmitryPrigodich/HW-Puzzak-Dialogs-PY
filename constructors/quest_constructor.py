import utils
from itertools import zip_longest
from .constuctor_base import Constructor_Base

class Quest_Constructor(Constructor_Base):
    _QUEST_DATA_JSON = "json_bak/QuestData-module.json"
    _QUEST_LINE_DATA_JSON = "json_bak/QuestLineData-module.json"
   
    _quest_data = {}
    _quest_line_data = {}

    _FILE_NAME = "data/QUEST_LINE_QUESTS.md"
    _FILE_NAME_TMP = "data/QUEST_LINE_QUESTS_TMP.md"
    _FILE_NAME_JSON = "json/quest_line_quests.json"

    _quest_lines = {}
    _quest_line_quest_data = {}

    _quest_tags = ["Tier","Type:","CinematicIds:", "EventId:", "Goals:", "GoalParameters:","MailsOnCompletion:","RepetitionType:","ReplayMissionId:","FollowUps:","FollowUpLines:"]

    def __init__(self):
        super().__init__()
        self._quest_data = self._read_json(self._QUEST_DATA_JSON)
        self._quest_line_data = self._read_json(self._QUEST_LINE_DATA_JSON)
        self._set_quest_lines_w_quests()
        

    # CHAPTERS CALL FOR QUESTLINES & QUESTS
    # QUESTLINES HAVE QUESTS
    # EVENTS may be name similarly to QUEST_LINES -> QUEST etc; QUESTS have EventId
    # EVENTS should be found manually

    # Go through the _quest_data
    # Check Quest in _quest_line_data
    # COLLECT JSON: {QUEST_LINE:[{QUEST}:{ORDER}{STRING}]}
    # IF NO QUEST_LINE, SET "no_ql"
    # QUEST TYPE may show is it event or main
    # Goals / Goal Parameters may lead to
    # FollowUpLines for sure required
  
    def _set_quest_lines_w_quests(self):
        
        for quest_id, quest_tags in self._quest_data.items():
            quest = {}
            quest[quest_id] = {}
            quest_tags_collector = {}

            for key in ["Type:","CinematicIds:","EventId:","MailsOnCompletion:"]:
                if key in quest_tags:
                    quest_tags_collector[key] = quest_tags.get(key)

            # Combine FollowUps & FollowUpLines -> FollowUp:
            qt_followups_final = []
            for key in ["FollowUpLines:","FollowUps:"]:
                qt_followups = quest_tags.get(key)
                if qt_followups:
                    qt_followups_final += qt_followups.split(":")
                    quest_tags_collector["FollowUps:"] = qt_followups_final

            # Combine Goals & GoalParameters -> Goals:
            qt_goals_final = []
            qt_goals = quest_tags.get("Goals:")
            if qt_goals:
                qt_goal_params = quest_tags.get("GoalParameters:")
                if qt_goal_params:
                    qt_goals_final = self._get_goals_w_params_rearranged(qt_goals, qt_goal_params)
                else:
                    qt_goals_final = self._get_goals_rearranged(qt_goals)
                
                quest_tags_collector["Goals:"] = qt_goals_final

            quest[quest_id] = quest_tags_collector


            quest_line_id = self.get_quest_line_by_quest_id(quest_id)
            if quest_line_id not in self._quest_line_quest_data:
                self._quest_line_quest_data[quest_line_id] = []
            self._quest_line_quest_data[quest_line_id].append(quest)

        return self._quest_line_quest_data

    def write_json(self):
        self._write_json(self._quest_line_quest_data)

    def write_data(self):
        body = "# HWM QUESTLINES WITH QUESTS\n\n"

        for quest_line, quests in self._quest_line_quest_data.items():
            body += f"\n## {quest_line}".upper()

            for quest in quests:
                for quest_id, quest_tags in quest.items():
                    body += f"\n### {quest_id}\n"

                    for qt_key, qt_value in quest_tags.items():
                        match qt_key:
                            # case key if key in ["Type:","CinematicIds:","EventId:","MailsOnCompletion:"]:
                            #     body += f"\t* {qt_key}\t{qt_value}\n"
                            case "FollowUps:":
                                if len(list(qt_value)) == 1:
                                    body += f"* {qt_key} {qt_value[0]}\n"
                                else:
                                    body += f"* {qt_key}\n"
                                    for items in qt_value:
                                        body += f"\t* {items}\n"

                            case "Goals:":
                                body += f"* {qt_key}\n"
                                # this shit is complicated because I don't know why it's organised this way
                                # had to go in a evolutianary way to make it formatted like I want
                                for g_order, g_params in qt_value.items():
                                    body += f"\t* {g_order}:\n"
                                    
                                    for g_param in g_params:
                                        for gp_key, gp_value in g_param.items():

                                            if gp_key != "GoalParam:":
                                                body += f"\t\t* {gp_key} {gp_value}\n"
                                            else:
                                                for gpv_key, gpv_value in gp_value.items():

                                                    match gpv_key:
                                                        case gkey if gkey in ["Ids","ExcludedSources"]:
                                                            body += f"\t\t\t* {gpv_key}:\n"

                                                            if len(gpv_value.split("|")) > 1:
                                                                gpvi_values = gpv_value.split("|")
                                                            elif len(gpv_value.split("_")) > 1:
                                                                gpvi_values = gpv_value.split("_")

                                                            for gpvi_value in gpvi_values:
                                                                body += f"\t\t\t\t* {gpvi_value}\n"
                                                        case _:
                                                            if isinstance(gpv_value, dict):
                                                                for gpvi_key, gpvi_value in gpv_value.items():
                                                                    body += f"\t\t\t* {gpvi_key}: {gpvi_value}\n"
                                                            else:
                                                                body += f"\t\t\t* {gpv_key}: {gpv_value}\n"
                            case _:
                                body += f"* {qt_key}\t{qt_value}\n"                       

        utils.rewrite_file(body, self._FILE_NAME)

    def write_data_spc(self):
        body = "# HWM QUESTLINES WITH QUESTS\n\n"

        for quest_line, quests in self._quest_line_quest_data.items():
            body += f"\n## {quest_line}\n"

            for quest in quests:
                for quest_id, quest_tags in quest.items():

                    quest_header = self.get_quest_header(quest_id)
                    body += f"\n### {quest_id}: {quest_header}\n"

                    quest_desc = self.get_quest_desc(quest_id)
                    body += f"{quest_desc}\n"

                    for qt_key, qt_value in quest_tags.items():
                        if qt_key not in self._quest_tags_to_skip:
                            body += f"\t* {qt_key}\t"
                            if qt_key in ["FollowUps:"]:
                                body += ", ".join(qt_value) + "\n"
                            else:
                                body += f"{qt_value.replace("\n", ", ")}\n"

        utils.rewrite_file(body, self._FILE_NAME_TMP)


    def set_quest_lines(self):
        for ql_key, ql_value in self._quest_line_data.items():
            self._quest_lines.append(ql_key)
        self._quest_lines = sorted(self._quest_lines)
        return self._quest_lines

    def get_quests_by_quest_line(quest_line_id):
        quests = []
            # ql_event_yaot_spring_2023
            # qe_yaot_spring_2023_day1
        return quests
    
    def get_quest_line_by_quest_id(self, quest_id):
        for quest_line_id, quest_line_tags in self._quest_line_data.items():
            if quest_id in quest_line_tags.get("QuestIds:").split(":"):
                return quest_line_id
        return "no_ql"
        
    def get_event_quest_line(event_id):
        return f"ql_{event_id}"
    
    def get_quest_header(self, quest_id):
        quest_header = self._string_data.get(quest_id)
        if quest_header != None:
            return quest_header.get('en:')
        
        quest_header = self._string_data.get(f"desc_{quest_id[:-1]}x")
        if quest_header != None:
            return quest_header.get('en:')    
        
        return f"No header for quest {quest_id}"
        
    
    def get_quest_desc(self, quest_id):
        quest_desc = self._string_data.get(f"desc_{quest_id}")
        if quest_desc != None:
            return quest_desc.get('en:')
        
        quest_desc = self._string_data.get(f"desc_{quest_id[:-1]}x")
        if quest_desc != None:
            return quest_desc.get('en:')       
        
        return f"No description for quest {quest_id}"
    
    # dia_iyaFal_2023_day01_end_1
    # dia_iyaFal_2023_epi05_end_1


    _goal_types = [
        "ChangeName","SelectKiith","JoinClan","PlaceOrbital","CompleteQuest","CompleteMission","StartCraft","ChargeScanner"
        ,"GoTo","UpgradeOfficer","Scan","Statistic","Pay","Buy","Craft","Equip","GainItem"
        ]
    _goal_types_to_stay = ["SelectKiith","CompleteQuest","CompleteMission","GoTo"]
        
    
    def _get_goals_w_params_rearranged(self, goals_str, goal_params_str):
        goals_final = {}
        
        goals_list = goals_str.split("\n")
        goal_params_list = goal_params_str.split("\n")

        for i, (goal_line, goal_param_line) in enumerate(zip_longest(goals_list, goal_params_list, fillvalue='')):
            goal_type, task_number = goal_line.split(",")
            
            
            curr_goal_param = {}
            for goal_params in goal_param_line.split(";"):
                gp_key = goal_params.split("&")[0]
                gp_value = goal_params.split("&")[-1]
                curr_goal_param[gp_key] = gp_value

            curr_goal = {
                'GoalType:': goal_type,
                'GoalParam:': curr_goal_param
            }

            if task_number not in goals_final:
                goals_final[task_number] = []
            goals_final[task_number].append(curr_goal)

        return goals_final
    
    def _get_goals_rearranged(self, goals_str):
        goals_final = {}
        
        for goals in goals_str.split("\n"):
            goal_type, task_number = goals.split(",")
            curr_goal = {
                'Type:': goal_type
            }
            if task_number not in goals_final:
                goals_final[task_number] = []
            goals_final[task_number].append(curr_goal)

        return goals_final