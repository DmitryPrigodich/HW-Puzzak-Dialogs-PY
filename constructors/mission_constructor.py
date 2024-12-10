
import utils

from .constructor_base import Constructor_Base

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
            if m_key.split("_")[-1] not in ["t2","t3","t4","heroic","mythic","solo"]:
                m_tags_collector = {}

                # Strings
                if "MissionMode:" in m_tags:
                    m_tags_collector["MissionMode:"] = m_tags.get("MissionMode:")

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
                        print(f"key: {m_tags[key]}")
                        for faction in m_tags[key].split(":"):
                            if faction != "None":
                                print(f"Faction: {faction}")
                                factions_final.append(utils.get_corrected_faction_name(faction))
                if factions_final:
                    factions_final = sorted(list(set(factions_final)))            
                    m_tags_collector["Factions:"] = factions_final
                
                self._missions[m_key] = m_tags_collector
    
    def write_json(self):
        utils.write_json(self._missions, self._FILE_NAME_JSON)

    def write_data(self):
        body = "# HWM MISSIONS SELECTION\n"
        for m_key, m_tags in self._missions.items():
            body += f"\n## {m_key}\n"

            for key in ["MissionMode:", "SystemId:"]:
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
    def write_data_tmp(self):
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