
import utils
import re

from .constructor_base import Constructor_Base
from .dia_seq_constructor import Dialog_Sequence_Constructor
from .mission_step_constructor import Mission_Step_Constructor

class Mission_Constructor(Constructor_Base):
    _MISSION_DATA_JSON = "dataset/json_bak/MissionData-module.json"
    _MISS_DIA_REA = "dataset/json/mission_dialogs_rearranged.json"

    _FILE_NAME = "dataset/data/MISSIONS.md"
    _FILE_NAME_TMP = "dataset/data/MISSIONS_TMP.md"
    _FILE_NAME_JSON = "dataset/json/missions.json"

    _mission_data = {}
    _missions = {}

    def __init__(self):
        super().__init__()
        self._mission_data = utils.read_json(self._MISSION_DATA_JSON)
        self._set_data()
   
    def _set_tags_to_skip(self):
        tags_to_skip = []
        tags_to_skip += ["BlockEscorts:","BlockSquads:","DecalTypes:","DefaultScanState:"]
        tags_to_skip += ["JoinWaitTime:","LevelSize:","Position:","ResourceSpots:", "Mode:", "InstanceId:", "LayoutId:"]
        tags_to_skip += ["HasIntroSequence:","Mode:","Tier:","SubTier:","XPRewardModifier:","TagsForQuests:", "Rewards:"]
        tags_to_skip += ["TeamAssignments:","TeamRel:","LPTeams:","UnitInitialWaitTime:","UseLineOfSight:"]
        tags_to_skip += ["T0AiTypes:","T1AiTypes:","T2AiTypes:"]
        tags_to_skip += ["T0_EMPTY:","T1_EMPTY:","T1Npc0_EMPTY:","T2_EMPTY:","T3_EMPTY:"]
        tags_to_skip += ["T0NpcIds:","T1NpcIds:","T2NpcIds:",]
        tags_to_skip += ["T0Npc0UnitSets:","T0Npc1UnitSets:","T1Npc0UnitSets:","T1Npc1UnitSets:","T1Npc2UnitSets:","T1Npc3UnitSets:","T2Npc0UnitSets:","T2Npc1UnitSets:","T2Npc2UnitSets:"]
        tags_to_skip += ["T0Npc0Behaviors:","T0Npc0Formations:","T0Npc0PoolIndices:","T0Npc0PoolPositions:","T0Npc0ShowMarkers:","T0Npc0SpawnIndices:","T0Npc0Tags:"]
        tags_to_skip += ["T0Npc1Behaviors:","T0Npc1Formations:","T0Npc1PoolIndices:","T0Npc1PoolPositions:","T0Npc1ShowMarkers:","T0Npc1SpawnIndices:","T0Npc1Tags:"]
        tags_to_skip += ["T1Npc0Behaviors:","T1Npc0Formations:","T1Npc0PoolIndices:","T1Npc0PoolPositions:","T1Npc0ShowMarkers:","T1Npc0SpawnIndices:","T1Npc0Tags:"]
        tags_to_skip += ["T1Npc1Behaviors:","T1Npc1Formations:","T1Npc1PoolIndices:","T1Npc1PoolPositions:","T1Npc1ShowMarkers:","T1Npc1SpawnIndices:","T1Npc1Tags:"]
        tags_to_skip += ["T1Npc2Behaviors:","T1Npc2Formations:","T1Npc2PoolIndices:","T1Npc2PoolPositions:","T1Npc2ShowMarkers:","T1Npc2SpawnIndices:","T1Npc2Tags:"]
        tags_to_skip += ["T1Npc3Behaviors:","T1Npc3Formations:","T1Npc3PoolIndices:","T1Npc3PoolPositions:","T1Npc3ShowMarkers:","T1Npc3SpawnIndices:","T1Npc3Tags:"]
        tags_to_skip += ["T2Npc0Behaviors:","T2Npc0Formations:","T2Npc0PoolIndices:","T2Npc0PoolPositions:","T2Npc0ShowMarkers:","T2Npc0SpawnIndices:","T2Npc0Tags:"]
        tags_to_skip += ["T2Npc1Behaviors:","T2Npc1Formations:","T2Npc1PoolIndices:","T2Npc1PoolPositions:","T2Npc1ShowMarkers:","T2Npc1SpawnIndices:","T2Npc1Tags:"]
        tags_to_skip += ["T2Npc2Behaviors:","T2Npc2Formations:","T2Npc2PoolIndices:","T2Npc2PoolPositions:","T2Npc2ShowMarkers:","T2Npc2SpawnIndices:","T2Npc2Tags:"]
        return tags_to_skip

    def _set_data(self):
        for m_key, m_tags in self._mission_data.items():
            m_tags_collector = {}

            # Strings
            for key in ["MissionMode:","InstanceId:"]:
                if key in m_tags:
                    m_tags_collector[key] = m_tags.get(key)

            if "SystemId:" in m_tags:
                coordinates = m_tags.get("SystemId:")
                star_system = self.get_starsystem_by_coords(coordinates)
                m_tags_collector["SystemId:"] = {
                    "Coordinates:": coordinates,
                    "Name:": star_system.get('Name:'),
                    "Faction:": star_system.get('Faction:')
                }

            # Lists
            for key in ["DialogSequences:", "StartingMissionSteps:"]:
                if key in m_tags:
                    m_tags_collector[key] = sorted(m_tags.get(key).split(":"))

            # Unifying factions
            factions_final = []
            for key in ["T0Factions:","T1Factions:","T2Factions:"]:
                if key in m_tags:
                    for faction in m_tags[key].split(":"):
                        if faction != "None":
                            factions_final.append(utils.get_corrected_faction_name(faction))
            if factions_final:
                factions_final = sorted(list(set(factions_final)))            
                m_tags_collector["Factions:"] = factions_final
            
            self._missions[m_key] = m_tags_collector
    
    def get_data(self):
        return self._missions
    
    def write_json(self):
        utils.write_json(self._missions, self._FILE_NAME_JSON)

    def write_data(self):
        body = "# HWM MISSIONS SELECTION\n"
        for m_key, m_tags in self._missions.items():
            body += f"\n## {m_key}\n"

            for key in ["MissionMode:", "SystemId:", "InstanceId:"]:
                if key in m_tags:
                    body += f"\t* {key} {m_tags[key]}\n"

            for key in ["Factions:","DialogSequences:", "StartingMissionSteps:"]:
                if key in m_tags:
                    body += f"\t* {key} "
                    m_tag_value = m_tags[key]
                    if len(m_tag_value) > 1:
                        for value in m_tag_value:
                            body += f"\n\t\t* {value}"
                    else:
                        body += f"{m_tag_value[0]}"
                    body += "\n"
                    
        utils.rewrite_file(body, self._FILE_NAME)


    # full set for analysis only
    def _write_data_tmp(self):
        tags = {}

        body = "# HWM MISSIONS\n"
        for m_key, m_tags in self._mission_data.items():
            body += f"\n## {m_key}\n"
            for mt_key, mt_value in m_tags.items():
                if mt_key not in tags:
                    tags[mt_key] = []
                tags[mt_key].append(mt_value)

                body += f"\t* {mt_key} {mt_value}\n"

        tags = utils.sort_dict_by_keys(tags)

        body_tags = "\n# HWM MISSIONS TAGS\n"
        for t_key, t_values in tags.items():
            t_values = sorted(list(set(t_values)))
            body_tags += f"\t* {t_key}:\n"
            body_tags += f"\t\t* {t_values}\n"
       
        utils.rewrite_file(body_tags, self._FILE_NAME_TMP)
        utils.add_to_file(body, self._FILE_NAME_TMP)
    

    def get_mission_by_id(self, mission_id):
        return self._missions.get(mission_id)
    
    def get_mission_text(self,mission_id):
        body_mission = ""

        # Mission Id
        print(f"Mission: {mission_id}")
        match = re.match(r'^event_(\d+)_StationDefense$', mission_id)
        if match:
            # m_tier = int(match.group(1))
            # mission_key = f"event_amasum2024_stationdefense_t{m_tier}"
            # mission_name = self.get_string_by_key(mission_key)
            mission_id = "strike_x_DownTheWell"
        
        mission = self.get_mission_by_id(mission_id)
        if "InstanceId:" in mission:
            mission_id = mission.get("InstanceId:")
            print(f"Replaced Mission: {mission_id}")
            mission = self.get_mission_by_id(mission_id)

        # Mission Name
        mission_name = self.get_string_by_key(mission_id)
        body_mission += utils.format_heading4(f"Mission: {mission_name}")

        # Mission Description
        mission_desc_key = f"desc_{mission_id}"
        for ending in ["_t1","_t2","_t3","_t4"]:
            if mission_id.endswith(ending):
                mission_desc_key = f"desc_{mission_id[:-1]}x"
        mission_desc_text = self.get_string_by_key(mission_desc_key)
        # print(f"Mission Desc: {mission_desc_key}")
        if mission_desc_text and mission_desc_text != "-" :
            body_mission += utils.format_br(1)
            body_mission += utils.format_bold("Description:")
            body_mission += utils.format_br(1)
            body_mission += utils.format_paragraph(mission_desc_text)
            body_mission += utils.format_br(1)
        
        # Location
        if "SystemId:" in mission:
            m_location = mission.get("SystemId:")
            m_location_name = m_location["Name:"]
            m_location_faction = m_location["Faction:"]

            body_mission += utils.format_br(1)
            body_mission += utils.format_bold("Location:")
            body_mission += utils.format_br(1)
            body_mission += utils.format_paragraph(f"{m_location_name} system, {m_location_faction} territory")
            body_mission += utils.format_br(1)
        else:
            print(f"**LOCATION:** No location for mission {mission_id}\n")

        # Factions
        if "Factions:" in mission:
            m_factions = mission.get("Factions:")
            faction_list = ", ".join(map(str, m_factions))

            body_mission += utils.format_bold("Factions Involved:")
            body_mission += utils.format_br(1)
            body_mission += utils.format_paragraph(faction_list)
            body_mission += utils.format_br(1)

        # Dialogs
        m_dialogs = mission.get("DialogSequences:")
        m_dialog_list = utils.read_json(self._MISS_DIA_REA)
        for m_dialog_key, m_dia_logs in m_dialog_list.items():
            if mission_id.startswith(m_dialog_key):
                m_dialogs = m_dia_logs

        dialog_data = Dialog_Sequence_Constructor()
        if m_dialogs:
            for dialog_id in m_dialogs:
                body_mission += dialog_data.get_dialog_text(dialog_id)
        else:
            mission_steps = Mission_Step_Constructor()
            starting_mission_steps = mission.get("StartingMissionSteps:")
            for mission_step in starting_mission_steps:
                body_mission += mission_steps.get_mission_steps_text(mission_step)

        return body_mission
