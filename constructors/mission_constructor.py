
import utils

from .constuctor_base import Constructor_Base

class Mission_Constructor(Constructor_Base):
    MISSION_DATA_JSON = "json_bak/MissionData-module.json"
    STAR_MAP_JSON = "json/starmap.json"

    FILE_NAME = "data/MISSIONS.md"
    FILE_NAME_TMP = "data/MISSIONS_TMP.md"
    FILE_NAME_JSON = "json/missions.json"

    _mission_data = {}
    _star_system_data = {}

    _mission_tags_to_skip = []

    _missions = {}

    def __init__(self):
        super().__init__()
        self._mission_data = self._read_json(self.MISSION_DATA_JSON)
        self._star_system_data = self._read_json(self.STAR_MAP_JSON)
        self._mission_tags_to_skip = self._set_tags_to_skip()
   
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

    def set_missions(self):
        return self._missions
    
    def write_data(self):
        tags = {}

        body = "\n# HWM MISSIONS\n"
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
       
        utils.rewrite_file(body_tags, self.FILE_NAME)
        utils.add_to_file(body, self.FILE_NAME)
        print("Finished writing Mission Data")

    def write_data_spc(self):
        tags = {}

        body = "\n# HWM MISSIONS SELECTION\n"
        for m_key, m_tags in self._mission_data.items():
            # no rec for mission version by difficulty (heroic, mythic)
            if 'InstanceId:' in m_tags:
                continue
            # no rec for mission version by tier
            elif m_key.split("_")[-1] in ["t2","t3","t4","solo"]:
                continue
            else:
                body += f"\n## {m_key}\n"

                for mt_key, mt_value in m_tags.items():
                    # no point in empty value
                    if mt_value != "None":
                        # some tags are useless for me
                        if mt_key not in self._mission_tags_to_skip:
                            # recoding all value in one key for analysis
                            if mt_key not in tags:
                                tags[mt_key] = []
                            tags[mt_key].append(mt_value)

                            match mt_key:
                                case "DialogSequences:":
                                    body += f"\t* {mt_key}\n"
                                    for dia_seq in mt_value.split(":"):
                                        body += f"\t\t\t* {dia_seq}\n"
                                case "SystemId:":
                                    system_name = self._star_system_data.get(mt_value)['name']
                                    system_faction = self._star_system_data.get(mt_value)['faction']
                                    body += f"\t* {mt_key} {mt_value} - {system_faction}'s {system_name}\n"
                                case _:
                                    body += f"\t* {mt_key} {mt_value}\n"

        tags = utils.sort_dict_by_keys(tags)
        body_tags = "\n# HWM MISSIONS TAGS\n"
        for t_key, t_values in tags.items():
            body_tags += f"\t* {t_key}:\n"
            t_values = sorted(list(set(t_values)))

            if t_key in ["DialogSequences:", "InstanceId:", "LayoutId:", "Rewards:", "StartingMissionSteps:"]:
                for t_value in t_values:
                    body_tags += f"\t\t* "
                    if t_key in ["DialogSequences:"]:
                        for dia_seq in t_value.split(":"):
                            body_tags += f"\n\t\t\t* {dia_seq}"
                    else:
                        body_tags += f"{t_value}".replace("\n","\t\t")
                    body_tags += "\n"
            else:
                body_tags += f"\t\t* {t_values}\n"
       
        utils.rewrite_file(body_tags, self.FILE_NAME_TMP)
        utils.add_to_file(body, self.FILE_NAME_TMP)
        print("Finished writing Mission Data")