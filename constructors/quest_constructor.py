import utils
from itertools import zip_longest
from .constructor_base import Constructor_Base
from .mission_constructor import Mission_Constructor
from .dia_seq_constructor import Dialog_Sequence_Constructor
from .string_constructor import String_Data_Constructor

class Quest_Constructor(Constructor_Base):
    _QUEST_DATA_JSON = "json_bak/QuestData-module.json"
    _QUEST_LINE_DATA_JSON = "json_bak/QuestLineData-module.json"
    _QUEST_LINE_JSON = "json/quest_lines.json"
   
    _quest_data = {}
    _quest_line_data = {}

    _FILE_NAME = "data/QUESTS.md"
    _FILE_NAME_TMP = "data/QUESTS_TMP.md"
    _FILE_NAME_JSON = "json/quests.json"

    _quests = {}

    # I think for my needs only "CompleteQuest","CompleteMission","GoTo" required
    _GOAL_TYPES = ["ChangeName","SelectKiith","JoinClan","PlaceOrbital","ChargeScanner","StartCraft","UpgradeOfficer","Scan","Buy","Equip","GainItem","Craft","GoTo","Pay","Statistic","CompleteMission","CompleteQuest"]


    def __init__(self):
        super().__init__()
        self._quest_data = utils.read_json(self._QUEST_DATA_JSON)
        self._set_data()
  
    def _set_data(self):

        def _get_quest_header(quest_id):
            quest_header = self.get_string_by_key(quest_id)
            if quest_header:
                return quest_header
            
            quest_id_key = f"{quest_id[:-1]}x"
            quest_header = self.get_string_by_key(quest_id_key)
            if quest_header:
                return quest_header
            
            quest_id_key = f"desc_{quest_id[:-1]}x"
            quest_header = self.get_string_by_key(quest_id_key)
            if quest_header:
                return quest_header
            
            error_msg = f"No header for quest {quest_id}"
            # print(error_msg)
            return utils.format_code(error_msg) 
        
        def _get_quest_desc(quest_id):
            quest_id_key = f"desc_{quest_id}"
            quest_desc = self.get_string_by_key(quest_id_key)
            if quest_desc:
                return quest_desc
            
            quest_id_key = f"desc_{quest_id[:-1]}x"
            quest_desc = self.get_string_by_key(quest_id_key)
            if quest_desc != None:
                return quest_desc
            
            error_msg = f"No description for quest {quest_id}"
            # print(error_msg)
            return utils.format_code(error_msg) 

        def _get_goals_w_params_rearranged(goals_str, goal_params_str):
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
        
        def _get_goals_rearranged(goals_str):
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
        

        for quest_id, quest_tags in self._quest_data.items():
            if quest_id.startswith("qe_amaSum_2023"):
                quest_id_upd = quest_id.replace("2023","2024")
                q_name = _get_quest_header(quest_id_upd)
                q_desc = _get_quest_desc(quest_id_upd)
            else:
                q_name = _get_quest_header(quest_id)
                q_desc = _get_quest_desc(quest_id)

            quest_tags_collector = {}
            quest_tags_collector['Name:'] = q_name
            quest_tags_collector['Description:'] = q_desc

            for key in ["Type:","CinematicIds:","EventId:","MailsOnCompletion:"]:
                if key in quest_tags:
                    quest_tags_collector[key] = quest_tags.get(key)

            # Combine FollowUps & FollowUpLines -> FollowUp:
            qt_followups_final = []
            for key in ["FollowUpLines:","FollowUps:"]:
                if key in quest_tags:
                    qt_followups = quest_tags.get(key)
                    qt_followups_final += qt_followups.split(":")
                    quest_tags_collector["FollowUps:"] = qt_followups_final

            # Combine Goals & GoalParameters -> Goals:
            qt_goals_final = []
            if "Goals:" in quest_tags:
                qt_goals = quest_tags.get("Goals:")
                if "GoalParameters:" in quest_tags:
                    qt_goal_params = quest_tags.get("GoalParameters:")
                    qt_goals_final = _get_goals_w_params_rearranged(qt_goals, qt_goal_params)
                else:
                    qt_goals_final = _get_goals_rearranged(qt_goals)
                
                quest_tags_collector["Goals:"] = qt_goals_final

            self._quests[quest_id] = quest_tags_collector

    def get_data(self):
        return self._quests
    
    def write_json(self):
        utils.write_json(self._quests,self._FILE_NAME_JSON)

    def write_data(self):
        body = "# HWM QUESTS\n"

        for quest_id, quest_params in self._quests.items():
            body += f"\n## {quest_id}\n".upper()

            for qt_key, qt_value in quest_params.items():
                    match qt_key:
                        case "FollowUps:":
                            if len(list(qt_value)) == 1:
                                body += f"* {qt_key} {qt_value[0]}\n"
                            else:
                                body += f"* {qt_key}\n"
                                for items in qt_value:
                                    body += f"\t* {items}\n"

                        case "Goals:":
                            body += f"* {qt_key}\n"
                            body += self._get_goal_text(qt_value)
                        case _:
                            body += f"* {qt_key} {qt_value}\n"
        
        utils.rewrite_file(body, self._FILE_NAME)

    # full set for analysis only
    def _write_data_tmp(self):
        _title = "HWM Quests"
        _tmp_data = self._quest_data
        _splitter = "\n"

        #fill it when tags are known
        _existing_tags = ["Type:", "ScheduleType:", "CinematicIds:", "EventId:", "Tier:", "XPMod:", "Rewards:", "RepetitionType:", "ReplayMissionId:", "MailsOnCompletion:", "FollowUpLines:", "FollowUps:", "GoalIconId:", "Goals:", "GoalParameters:", "StartOffset:", "EndOffset:"]
        _tags_single_line = ["Type:","ScheduleType:","CinematicIds:","EventId:","Tier:","XPMod:","RepetitionType:","MailsOnCompletion","GoalIconId:","StartOffset:","EndOffset:"]
        _tags_multiple_lines = ["ReplayMissionId:","FollowUpLines:", "FollowUps:","Goals:", "GoalParameters:","Rewards:"]

        def get_tags(data):
            body_tags = "\n## TAGS:\n"
            tag_collector = []
            for id, params in data.items():
                for param_key, param_value in params.items():
                    tag_collector.append(param_key)
            tag_collector = sorted(list(set(tag_collector)))
            tag_list = ", ".join(map(str, tag_collector))
            body_tags += f"{tag_list}\n"
            return body_tags

        def get_main(data):
            def _get_single_line(param_value):
                return f"{param_value}\n"

            def _get_multiple_lines(param_value):
                body_lines = ""
                param_value_list = param_value.split(_splitter)
                for value in param_value_list:
                    body_lines += f"\n\t\t* {value}"
                body_lines += "\n"
                return body_lines

            body_main = ""
            for id, parameters in data.items():
                body_main += f"\n## {id}\n"

                for param_key in _existing_tags:
                    if param_key in parameters:
                        body_main += f"\t* {param_key} "
                        param_value = parameters.get(param_key)
                        match param_key:                   
                            case key if key in _tags_multiple_lines:
                                body_main += _get_multiple_lines(param_value)
                            case key if key in _tags_single_line:
                                body_main += _get_single_line(param_value)
                            case _:
                                body_main += _get_single_line(param_value)
            return body_main

        body = f"# {_title}\n\n".upper()
        # body += get_tags(_tmp_data)
        body += get_main(_tmp_data)
            
        utils.rewrite_file(body, self._FILE_NAME_TMP)


    def get_quest_by_id(self, quest_id):
        return self._quests.get(quest_id)  

    
    def _get_goal_text(self, goals):
    # this shit is complicated because I don't know why it's organised this way
    # had to go in a evolutionary way to make it formatted like I want
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
                            target_system = self.get_starsystem_by_coords(goal.get('GoalParam:')['SysId'])
                            goal_text += f" in {target_system.get('Name:')} system of {target_system.get('Faction:')}'s territories"

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
                        target_system = self.get_starsystem_by_coords(goal.get('GoalParam:')['Target'])
                        goal_text += f"{goal_type} {target_system.get('Name:')} system of {target_system.get('Faction:')}'s territories\n"

                    case "Buy":
                        if "Id" in goal.get('GoalParam:'):
                            goods_id = goal.get('GoalParam:')['Id']
                            goal_text += f"{goal_type}: {goods_id}\n"

                    case "Equip":
                        equip_type = goal.get('GoalParam:')['Type']
                        goal_text += f"{goal_type} {equip_type}\n"

                    case _:
                        goal_text += f"{goal_type}\n"

        return goal_text
    
    def get_quest_text(self,quest_id):
        mission_data = Mission_Constructor()
        string_data = String_Data_Constructor()

        def _get_mission_text(mission_id):
            mission_text = ""
            match mission_id:
                case m if m in ["story_A01_DuzumiGate","story_A01_DuzumiGateTut"]:
                    mission_text += string_data.get_cinematic_text('20')
                    mission_text += mission_data.get_mission_text(mission_id)
                case "story_A02_WiracodaGate":
                    mission_text += string_data.get_cinematic_text('10')
                    mission_text += mission_data.get_mission_text(mission_id)
                case "story_A03_GulfTaln":
                    mission_text += string_data.get_cinematic_text('25')
                    mission_text += mission_data.get_mission_text(mission_id)
                case "story_C01_Tanochet":
                    mission_text += mission_data.get_mission_text(mission_id)
                    mission_text += string_data.get_cinematic_text('30')
                case "story_C03_StarTotek":
                    mission_text += mission_data.get_mission_text(mission_id)
                    mission_text += string_data.get_cinematic_text('35')
                case "story_D01_SijinLighthouse":
                    mission_text += mission_data.get_mission_text(mission_id)
                    mission_text += string_data.get_cinematic_text('40')
                case "story_D03_BrightTemple":
                    mission_text += mission_data.get_mission_text(mission_id)
                    mission_text += string_data.get_cinematic_text('50')
                case _:
                    mission_text += mission_data.get_mission_text(mission_id)
            return mission_text

        body_quest = ""

        # print(f"Quest: {quest_id}")
        quest = self.get_quest_by_id(quest_id)

        # Name
        q_name = quest.get('Name:')
        body_quest += utils.format_heading2(f"Quest: {q_name}")
        body_quest += utils.format_br(2)

        # Description
        q_description = quest.get('Description:')
        q_description_upd = utils.remove_color(q_description)

        body_quest += utils.format_bold("Description:")
        body_quest += utils.format_br(2)
        body_quest += utils.format_paragraph(q_description_upd)
        body_quest += utils.format_br(2)

        # Goals
        q_goals = quest.get('Goals:')
        q_goals_text = self._get_goal_text(q_goals)
        
        body_quest += utils.format_bold("Goals:")
        body_quest += utils.format_br(2)
        body_quest += utils.format_paragraph(q_goals_text)
        body_quest += utils.format_br(2)

        # Missions
        for q_goal_order, q_goals in q_goals.items():
            for q_goal in q_goals:
                if q_goal.get("GoalType:") == "CompleteMission":
                    if "Id" in q_goal.get("GoalParam:"):
                        mission_id = q_goal.get("GoalParam:")["Id"]
                        body_quest += _get_mission_text(mission_id)

                    if "Ids" in q_goal.get("GoalParam:"):
                        mission_ids = q_goal.get("GoalParam:")["Ids"]
                        for mission_id in mission_ids.split("|"):
                            if mission_id != "story_A01_DuzumiGate":
                                body_quest += _get_mission_text(mission_id)

        # End-Day Dialogs
        q_end_day_dialog_id = f"{quest_id}_end"
        dialog_data = Dialog_Sequence_Constructor()
        q_end_day_dialog_text = dialog_data.get_dialog_text(q_end_day_dialog_id)
        if q_end_day_dialog_text:
            # print(f"End of Day Dialog: {q_end_day_dialog_id}")
            body_quest += utils.format_bold("End-of-day-dialog:")
            body_quest += utils.format_br(2)
            body_quest += utils.format_paragraph(q_end_day_dialog_text)
            body_quest += utils.format_br(2)

        # Mails
        if "MailsOnCompletion:" in quest:
            mail = quest.get("MailsOnCompletion:")

            mail_header_key = f"{mail}_header"
            mail_body_key = f"{mail}_body"
            
            mail_header = self.get_string_by_key(mail_header_key)
            mail_body = self.get_string_by_key(mail_body_key)

            # print(f"mail_header: {mail_header}")
            # print(f"mail_body: {mail_body}")

            body_quest += utils.format_heading4(f"Mail: {mail_header}")
            body_quest += utils.format_br(1)
            body_quest += utils.format_code_block(mail_body)
            body_quest += utils.format_br(2)

        return body_quest