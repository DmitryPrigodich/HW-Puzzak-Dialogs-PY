import utils
from itertools import zip_longest
from .constructor_base import Constructor_Base

class Quest_Constructor(Constructor_Base):
    _QUEST_DATA_JSON = "json_bak/QuestData-module.json"
    _QUEST_LINE_DATA_JSON = "json_bak/QuestLineData-module.json"
    _QUEST_LINE_JSON = "json/questlines.json"
   
    _quest_data = {}
    _quest_line_data = {}

    _FILE_NAME = "data/QUESTS.md"
    _FILE_NAME_SPC = "data/QUESTS_SPC.md"
    _FILE_NAME_JSON = "json/quests.json"

    _quests = {}
    _quest_lines = {}

    _quest_tags = ["Tier","Type:","CinematicIds:", "EventId:", "Goals:", "GoalParameters:","MailsOnCompletion:","RepetitionType:","ReplayMissionId:","FollowUps:","FollowUpLines:"]

    def __init__(self):
        super().__init__()
        self._quest_data = utils.read_json(self._QUEST_DATA_JSON)
        self._quest_line_data = utils.read_json(self._QUEST_LINE_DATA_JSON)
        self._quest_lines = utils.read_json(self._QUEST_LINE_JSON)
        self._set_quests()
        

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
  
    def _set_quests(self):

        # q = 0
        # qt = len(self._quest_data)
        for quest_id, quest_tags in self._quest_data.items():
            # q += 1
            # print(f"JSON: writing {q}/{qt} quest {quest_id}")
            quest_tags_collector = {}

            quest_tags_collector['Name:'] = self._get_quest_header(quest_id)
            quest_tags_collector['Description:'] = self._get_quest_desc(quest_id)
            quest_tags_collector['QuestLine:'] = self.get_quest_line_by_quest_id(quest_id)

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

            self._quests[quest_id] = quest_tags_collector

    def write_json(self):
        utils.write_json(self._quests,self._FILE_NAME_JSON)

    def write_data_spc(self):
        body = "# HWM QUESTLINES WITH QUESTS\n\n"

        q = 0
        ql = 0
        qt = len(self._quest_data)
        qlt = len(self._quest_lines)
        for quest_line_id, quest_line_quests in self._quest_lines.items():
            body += f"\n## {quest_line_id}".upper()
            ql += 1
            for quest_id in quest_line_quests:
                q += 1
                print(f"MD: writing {q}/{qt}. quest {quest_id} for {ql}/{qlt} questline {quest_line_id}")
                quest = self.get_quest_by_id(quest_id)
                body += f"\n### {quest_id}:\n"

                if quest:
                    for qt_key, qt_value in quest.items():
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
                                body += self.get_goal_body_formatted(qt_value)
                            case _:
                                body += f"* {qt_key} {qt_value}\n"                       

        utils.rewrite_file(body, self._FILE_NAME)
   
    def get_quest_line_by_quest_id(self, quest_id):
        for quest_line_id, quest_line_tags in self._quest_line_data.items():
            if quest_id in quest_line_tags.get("QuestIds:").split(":"):
                return quest_line_id
        return "no_ql"
        
    def get_event_quest_line(self, event_id):
        match event_id:
            case "event_season_yaoSpr_2023":
                return "ql_event_yaot_spring_2023"
            case "event_season_amaSum_2023_t4":
                return "ql_event_amaSum_2023_t4"
            case "event_season_iyaFal_2023_t4":
                return "ql_event_iyaFal_2023_t4"
            case _:
                return f"ql_{event_id}"

    def get_quests_by_quest_line_id(self, quest_line_id):
        if quest_line_id in self._quest_lines:
            return self._quest_lines.get(quest_line_id)
        return None
        
    
    def get_event_quests(self, event_id):
        quest_line_id = self.get_event_quest_line(event_id)
        return self.get_quests_by_quest_line_id(quest_line_id)
    
    def get_quest_by_id(self, quest_id):
        return self._quests.get(quest_id)

    
    def _get_quest_header(self, quest_id):
        quest_header = self._string_data.get(quest_id)
        if quest_header != None:
            return quest_header.get('en:')
        
        quest_header = self._string_data.get(f"desc_{quest_id[:-1]}x")
        if quest_header != None:
            return quest_header.get('en:')    
        
        return f"No header for quest {quest_id}"
    
    def _get_quest_desc(self, quest_id):
        quest_desc = self._string_data.get(f"desc_{quest_id}")
        if quest_desc != None:
            return quest_desc.get('en:')
        
        quest_desc = self._string_data.get(f"desc_{quest_id[:-1]}x")
        if quest_desc != None:
            return quest_desc.get('en:')       
        
        return f"No description for quest {quest_id}"

    # I think for my needs only "CompleteQuest","CompleteMission","GoTo" required
    _GOAL_TYPES = [
        "ChangeName"
        ,"SelectKiith"
        ,"JoinClan"
        ,"PlaceOrbital"
        ,"ChargeScanner"
        ,"StartCraft"
        ,"UpgradeOfficer"
        ,"Scan"
        ,"Buy"
        ,"Equip"
        ,"GainItem"
        ,"Craft"
        ,"GoTo"
        ,"Pay"
        ,"Statistic"
        ,"CompleteMission"
        ,"CompleteQuest"
        ]
    
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
                'GoalType:': goal_type
            }
            if task_number not in goals_final:
                goals_final[task_number] = []
            goals_final[task_number].append(curr_goal)

        return goals_final
    
    def get_goal_body_formatted(self, goals):
    # this shit is complicated because I don't know why it's organised this way
    # had to go in a evolutianary way to make it formatted like I want
        goal_text = ""
        for goal_order, goals_list in goals.items():
            goal_text += f"\t* Task {int(goal_order)+1}: "
            if len(goals_list) > 1: 
                goal_text += "\n"

            for goal in goals_list:
                if len(goals_list) > 1:
                    goal_text += "\t\t* "

                goal_type = goal.get('GoalType:')

                match goal_type:
                    case "CompleteMission":
                        if "Ids" in goal.get('GoalParam:'):
                            mission_ids = goal.get('GoalParam:')['Ids'].split("|")
                            if len(list(mission_ids)) == 1:
                                goal_text += f"Complete mission '{self.get_string_by_key(mission_ids)}'\n"
                            else:
                                goal_text += "Complete missions:\n"
                                for mission_id in list(mission_ids):
                                    goal_text += f"\t\t* '{self.get_string_by_key(mission_id)}'\n"

                        elif "Id" in goal.get('GoalParam:'):
                            q_id = goal.get('GoalParam:')['Id']
                            q_id_name = self.get_string_by_key(q_id)
                            if not q_id_name:
                                q_id_name = q_id
                            goal_text += f"Complete mission '{q_id_name}'\n"

                        else:
                            gp_amount = goal.get('GoalParam:')['Amount']
                            # There are also 'Tier' (used only for campaign), 'Tags' (might be missing) and 'Mode' (Generated, Strike or none)
                            # But actually these are not that important
                            if int(gp_amount) > 1:
                                goal_text += f"Complete {gp_amount} side missions\n"
                            else:
                                goal_text += f"Complete side mission\n"

                    case "CompleteQuest":
                        if "Id" in goal.get('GoalParam:'):
                            q_id = goal.get('GoalParam:')['Id']
                            q_id_name = self.get_string_by_key(q_id)
                            goal_text += f"Complete quest '{q_id_name}'\n"

                        elif "Ids" in goal.get('GoalParam:'):
                            q_ids = goal.get('GoalParam:')['Ids']
                            if 'Amount' in goal.get('GoalParam:'):
                                gp_amount = goal.get('GoalParam:')['Amount']
                                goal_text += f"Complete {gp_amount} of {q_ids}\n"
                            else:
                                q_id_name = self.get_string_by_key(q_ids)
                                goal_text += f"Complete quest '{q_id_name}'\n"

                        else:
                            gp_amount = goal.get('GoalParam:')['Amount']
                            gp_tags = goal.get('GoalParam:')['Tags']
                            goal_text += f"{gp_amount} {gp_tags}\n"

                    case "StartCraft":
                        g_category = goal.get('GoalParam:')['Category'] # Research of Crafting
                        if g_category == "Crafting":
                            g_what = goal.get('GoalParam:')['Tags']
                        else:
                            g_what = goal.get('GoalParam:')['Id']
                        goal_text += f"Start {g_category} - {g_what}\n"

                    case "Pay":
                        pay_id = goal.get('GoalParam:')['Id']
                        if pay_id.startswith("hgn_"):
                            pay_id = pay_id[:-1].replace("_t","_tX")
                        pay_id_name = self.get_string_by_key(pay_id)
                        pay_amount = goal.get('GoalParam:')['Amount']

                        goal_text += f"{goal_type} {pay_amount} {pay_id_name}"
                        if "SysId" in goal.get('GoalParam:'):
                            target_system = self.get_star_system(goal.get('GoalParam:')['SysId'])
                            goal_text += f" in {target_system.get('faction')}'s system {target_system.get('name')}"

                        goal_text += "\n"

                    case "Statistic":
                        if "Ids" in goal.get('GoalParam:'):
                            stat_id = goal.get('GoalParam:')['Ids']
                        else:
                            stat_id = goal.get('GoalParam:')['Id']

                        if "Amount" in goal.get('GoalParam:'):
                            stat_count = goal.get('GoalParam:')['Amount']
                        else:
                            stat_count = goal.get('GoalParam:')['Total']
                            # \nId&ScannedBelt;Total&4\nId&ScannedGenerated;Amount&1"
                        goal_text += f"{stat_count} {stat_id}\n"

                    case "Goto":
                        target_system_coordinates = goal.get('GoalParam:')['Target']
                        target_system = self.get_star_system(target_system_coordinates)
                        goal_text += f"{goal_type} {target_system.get('faction')}'s system {target_system.get('name')}\n"

                    case "Buy":
                        goods_id = goal.get('GoalParam:')['Id']
                        goal_text += f"{goal_type}: {goods_id}\n"

                    case "Equip":
                        equip_type = goal.get('GoalParam:')['Type']
                        goal_text += f"{goal_type} {equip_type}\n"

                    case _:
                        goal_text += f"{goal_type}\n"

        return goal_text            
                            

    def _get_goal_body_formatted_old(self, goals):
    # FOR HISTORY ONLY! REMOVE IF NOT REQUIRED
        goal_text = ""
        for goal_order, goals_list in goals.items():
            goal_text += f"\n\t* Task {int(goal_order)+1}:"
            
            for goal in goals_list:
                for goal_tag, goal_tag_value in goal.items():
                    match goal_tag:
                        case "GoalParam:":
                            for g_param_key, g_param_values in goal_tag_value.items():
                                match g_param_key:
                                    case "Ids":
                                        print("I'm here")
                                        if len(g_param_values.split("|")) > 1:
                                            g_subparam_values = g_param_values.split("|")
                                        elif len(g_param_values.split("_")) > 1:
                                            if not g_param_values.startswith("qr"):
                                                g_subparam_values = g_param_values.split("_")
                                        else:
                                            goal_text += f"\t\t* {goal_tag} {goal_tag_value}\n"
                                            return goal_text

                                        goal_text += f"\t\t\t* {g_param_key}:\n"
                                        for g_subparam_value in g_subparam_values:
                                            goal_text += f"\t\t\t\t* {g_subparam_value}\n"
                                    
                                    case "ExcludedSources":
                                        # goal_text += f"\t\t\t* {g_param_key}:\n"
                                        # g_subparam_values = g_param_values.split("_")
                                        # goal_text += "\t\t\t\t* "
                                        # for g_subparam_value in g_subparam_values:
                                        #     goal_text += f"{g_subparam_value},"
                                        # goal_text += "\n"
                                        do = "nothing" #justskipit, notrequired
                                    
                                    case _:
                                        if isinstance(g_param_values, dict):
                                            for g_subparam_key, g_subparam_value in g_param_values.items():
                                                goal_text += f"\t\t\t* {g_subparam_key}: {g_subparam_value}\n"
                                        else:
                                            goal_text += f"\t\t\t* {g_param_key}: {g_param_values}\n"
                        case _:
                            goal_text += f"\t\t* {goal_tag} {goal_tag_value}\n"
                                                    
        return goal_text
    

    def get_quest_text(self,quest_id):
        quest_info = self.get_quest_by_id(quest_id)

        q_name = quest_info.get('Name:')
        q_description = quest_info.get('Description:')
        # q_cinematics = self.get_cinematic_lines(quest_info.get('CinematicIds'))
        q_goals = self.get_goal_body_formatted(quest_info.get('Goals:'))

        quest_body = ""
        quest_body += f"\n### {quest_id}\n"
        quest_body += f"**GOALS**:\n{q_goals}\n"
        if q_name != q_description:
            quest_body += f"**NAME**:\n{q_name}\n"
        quest_body += f"**DESCRIPTION**:\n{q_description}\n"
        return quest_body