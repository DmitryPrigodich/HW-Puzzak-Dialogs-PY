
import utils
import re

from .constructor_base import Constructor_Base
from .dia_seq_constructor import Dialog_Sequence_Constructor

class Mission_Constructor(Constructor_Base):
    _MISSION_DATA_JSON = "json_bak/MissionData-module.json"

    _FILE_NAME = "data/MISSIONS.md"
    _FILE_NAME_TMP = "data/MISSIONS_TMP.md"
    _FILE_NAME_JSON = "json/missions.json"

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
        print(f"Mission: {mission_id}")

        mission = self.get_mission_by_id(mission_id)
        if "InstanceId:" in mission:
            mission = self.get_mission_by_id(mission.get("InstanceId:"))
            print(f"Replaced Mission: {mission_id}")
            
        # Mission Name
        match = re.match(r'^event_(\d+)_StationDefense$', mission_id)
        if match:
            m_tier = int(match.group(1))
            mission_key = f"event_amasum2024_stationdefense_t{m_tier}"
            mission_name = self.get_string_by_key(mission_key)
        else:
            mission_name = self.get_string_by_key(mission_id)
        body_mission = f"\n### Mission [{mission_id}/{mission_name}]\n"

        # Mission Description
        mission_desc_key = f"desc_{mission_id[:-1]}x"
        mission_desc_text = self.get_string_by_key(mission_desc_key)
        print(f"Mission Desc: {mission_desc_key}")
        # * desc_event_iyafal2023_escort_tx: The missing captain has been located at an unnamed asteroid. Retrieve him at all costs.
        # desc_event_iyaFal2023_Escort_t4_tx
        if mission_desc_text:
            body_mission += f"**DESCRIPTION**: {mission_desc_text}\n"
        
        # Location
        if "SystemId:" in mission:
            m_location = mission.get("SystemId:")
            m_location_text = f"**LOCATION:** {m_location["Name:"]} system, {m_location["Faction:"]} territory\n"
            body_mission += m_location_text
        else:
            print(f"**LOCATION:** No location for mission {mission_id}\n")

        # Factions
        if "Factions:" in mission:
            m_factions = mission.get("Factions:")
            faction_list = ", ".join(map(str, m_factions))
            m_factions_text = f"**FACTIONS INVOLVED:** {faction_list}"
            body_mission += m_factions_text

        # Dialogs
        if mission_id.startswith("event_halloween2023_Rashidun"):
            m_dialogs = self.dia_event_halloween2023_Rashidun
        elif mission_id.startswith("event_tanWin2023_DefendBase"):
            m_dialogs = self.dia_event_tanWin2023_DefendBase
        elif mission_id.startswith("event_tanWin2023_AttackBase"):
            m_dialogs = self.dia_event_tanWin2023_AttackBase
        elif mission_id.startswith("event_tanWin2023_Relic"):
            m_dialogs = self.dia_event_tanWin2023_Relic
        elif mission_id.startswith("event_tanWin2023_Academy"):
            m_dialogs = self.dia_event_tanWin2023_Academy
        elif mission_id.startswith("event_anniversary2023_Wiracoda"):
            m_dialogs = self.dia_event_anniversary2023_Wiracoda
        elif mission_id.startswith("event_yaoSpr2024_Conjunction"):
            m_dialogs = self.dia_event_yaoSpr2024_Conjunction
        elif mission_id.startswith("event_iyaFal2023_Escort"):
            m_dialogs = self.dia_event_iyaFal2023_Escort
        else:
            m_dialogs = mission.get("DialogSequences:")

        dialog_data = Dialog_Sequence_Constructor()
        # print(f"Mission: {mission_id}")
        # print(f"Mission dialogs: {m_dialogs}")
        if m_dialogs:
            for dialog_id in m_dialogs:
                body_mission += dialog_data.get_dialog_text(dialog_id)

        return body_mission
    
    # Manually setting more appropriate order
    dia_event_halloween2023_Rashidun = [
		"e_halloween2023_Rashidun_intro"
		,"e_halloween2023_Rashidun_malikSee"
        ,"e_halloween2023_Rashidun_combat"
		,"e_halloween2023_Rashidun_derelictWave"
        ,"e_halloween2023_Rashidun_malikRegenA"
		,"e_halloween2023_Rashidun_derelictDownA"
        ,"e_halloween2023_Rashidun_malikDestroyA"
        ,"e_halloween2023_Rashidun_malikRegenB"
        ,"e_halloween2023_Rashidun_malikWeakened"
		,"e_halloween2023_Rashidun_malikDestroyB"
		,"e_halloween2023_Rashidun_derelictDownB"
        ,"e_halloween2023_Rashidun_malikDeath"
		,"e_halloween2023_Rashidun_outro"
    ]

    dia_event_tanWin2023_DefendBase = [
		"e_tanWin2023_DefendBase_intro"
		,"e_tanWin2023_DefendBase_firstWave"
		,"e_tanWin2023_DefendBase_nextWave"
		,"e_tanWin2023_DefendBase_stationLow"	
		,"e_tanWin2023_DefendBase_win"
        ,"e_tanWin2023_DefendBase_fail"
    ]

    dia_event_tanWin2023_AttackBase = [
		"e_tanWin2023_AttackBase_intro"
		,"e_tanWin2023_AttackBase_alert"
		,"e_tanWin2023_AttackBase_wave"
        ,"e_tanWin2023_AttackBase_boss"
		,"e_tanWin2023_AttackBase_vaygr"
		,"e_tanWin2023_AttackBase_win"
    ]

    dia_event_tanWin2023_Relic = [
		"e_tanWin2023_Relic_intro"
		,"e_tanWin2023_Relic_contact"
		,"e_tanWin2023_Relic_wave"
		,"e_tanWin2023_Relic_boss"
		,"e_tanWin2023_Relic_boss_low"
		,"e_tanWin2023_Relic_win"
    ]

    dia_event_tanWin2023_Academy = [
		"e_tanWin2023_Academy_intro"
		,"e_tanWin2023_Academy_heyoka"
		,"e_tanWin2023_Academy_situation"
		,"e_tanWin2023_Academy_hiigarans"
		,"e_tanWin2023_Academy_combat"
		,"e_tanWin2023_Academy_jochikDownA"
		,"e_tanWin2023_Academy_JochikReturn"
		,"e_tanWin2023_Academy_academyLow"
		,"e_tanWin2023_Academy_tepin"
		,"e_tanWin2023_Academy_jochikDownB"
		,"e_tanWin2023_Academy_win"
        ,"e_tanWin2023_Academy_failTepin"
		,"e_tanWin2023_Academy_failAcademy"
    ]

    dia_event_anniversary2023_Wiracoda = [
        "e_anniversary2023_Wiracoda_intro"
		,"e_anniversary2023_Wiracoda_go"
		,"e_anniversary2023_Wiracoda_cateIncoming"
		,"e_anniversary2023_Wiracoda_combat"
		,"e_anniversary2023_Wiracoda_cateFiller"
        ,"e_anniversary2023_Wiracoda_connection"
		,"e_anniversary2023_Wiracoda_progRetreating"
		,"e_anniversary2023_Wiracoda_MalikComment"
		,"e_anniversary2023_Wiracoda_MalikA"
		,"e_anniversary2023_Wiracoda_cateRetreating"
		,"e_anniversary2023_Wiracoda_standGround"
		,"e_anniversary2023_Wiracoda_MalikB"
		,"e_anniversary2023_Wiracoda_progIncoming"
		,"e_anniversary2023_Wiracoda_regeneration"
		,"e_anniversary2023_Wiracoda_control"
		,"e_anniversary2023_Wiracoda_MalikC"
        ,"e_anniversary2023_Wiracoda_deviceKilled"
        ,"e_anniversary2023_Wiracoda_deviceLost"
        ,"e_anniversary2023_Wiracoda_escape"
    ]

    dia_event_yaoSpr2024_Conjunction = [
        "e_yaoSpr2024_Conjunction_intro"
        ,"e_yaoSpr2024_Conjunction_interlude"
        ,"e_yaoSpr2024_Conjunction_arrival"
        ,"e_yaoSpr2024_Conjunction_conjunctionA"
        ,"e_yaoSpr2024_Conjunction_conjunctionB"
        ,"e_yaoSpr2024_Conjunction_deviation"
        ,"e_yaoSpr2024_Conjunction_attackA"
        ,"e_yaoSpr2024_Conjunction_attackB"
        ,"e_yaoSpr2024_Conjunction_catequil"
        ,"e_yaoSpr2024_Conjunction_change"
        ,"e_yaoSpr2024_Conjunction_catequilLow"
        ,"e_yaoSpr2024_Conjunction_win"
        ,"e_yaoSpr2024_Conjunction_end"
        ,"e_yaoSpr2024_Conjunction_fail"
    ]

    dia_event_iyaFal2023_Escort = [
	    "e_iyaFall2023_escort_dialog_intro"
		,"e_iyaFall2023_escort_dialog_go"
		,"e_iyaFall2023_escort_dialog_wave1A"
		,"e_iyaFall2023_escort_dialog_mines"
		,"e_iyaFall2023_escort_dialog_wave1B"
		,"e_iyaFall2023_escort_dialog_allyLow"
		,"e_iyaFall2023_escort_dialog_wave2"
		,"e_iyaFall2023_escort_dialog_countdown"
		,"e_iyaFall2023_escort_dialog_wave3"
		,"e_iyaFall2023_escort_dialog_killAll"
		,"e_iyaFall2023_escort_dialog_win"
		,"e_iyaFall2023_escort_dialog_fail"
    ]