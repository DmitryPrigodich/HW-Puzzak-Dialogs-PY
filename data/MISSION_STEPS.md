# HWM MISSION STEPS SPECIFIED

## debug_empty_Start
	* StepId: 0
	* Type: None
	* TargetType: MissionStart

## h_debug_AiBehavior_start
	* StepId: 0
	* Type: Trigger
	* TargetType: MissionStart
	* SuccLL: 
		* h_debug_AiBehavior_prefTarget_playerEscort
		* h_debug_AiBehavior_wave_0

## h_debug_LootDrops_Start
	* StepId: 0
	* Type: None
	* TargetType: MissionStart
	* SuccLL: 
		* h_debug_LootDrops_GAMA_0
		* h_debug_LootDrops_GAMA_2
		* h_debug_LootDrops_GAMA_4
		* h_debug_LootDrops_GAMA_6
		* h_debug_LootDrops_a_spawnWaveCommon
		* h_debug_LootDrops_a_spawnWaveEpic
		* h_debug_LootDrops_a_spawnWaveRare
		* h_debug_LootDrops_a_spawnWaveUncommon

## h_debug_LootDrops_t_KillCommon
	* StepId: 1
	* Type: TriggerRepeating
	* TargetType: AllUnitsWithTagsAreKilled
	* SuccLL: h_debug_LootDrops_GAMA_1

## h_debug_LootDrops_t_KillEpic
	* StepId: 7
	* Type: TriggerRepeating
	* TargetType: AllUnitsWithTagsAreKilled
	* SuccLL: h_debug_LootDrops_GAMA_7

## h_debug_LootDrops_t_KillRare
	* StepId: 5
	* Type: TriggerRepeating
	* TargetType: AllUnitsWithTagsAreKilled
	* SuccLL: h_debug_LootDrops_GAMA_5

## h_debug_LootDrops_t_KillUncommon
	* StepId: 3
	* Type: TriggerRepeating
	* TargetType: AllUnitsWithTagsAreKilled
	* SuccLL: h_debug_LootDrops_GAMA_3

## h_debug_LootDrops_w01
	* StepId: 2
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_debug_LootDrops_a_respawnCommon

## h_debug_LootDrops_w02
	* StepId: 4
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_debug_LootDrops_a_respawnUncommon

## h_debug_LootDrops_w03
	* StepId: 6
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_debug_LootDrops_a_respawnRare

## h_debug_LootDrops_w04
	* StepId: 8
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_debug_LootDrops_a_respawnEpic

## h_debug_rareMissionReward_reachPos
	* StepId: 1
	* Type: Goal
	* TargetType: ReachPointOfInterest
	* SuccLL: h_debug_rareMissionReward_finishMission

## h_debug_rareMissionReward_Start
	* StepId: 0
	* Type: None
	* TargetType: MissionStart
	* SuccLL: h_debug_rareMissionReward_GAMA_0

## h_debug_SimSpawnErrors_Start
	* StepId: 0
	* Type: None
	* TargetType: MissionStart
	* SuccLL: 
		* h_debug_SimSpawnErrors_GAMA_0
		* h_debug_SimSpawnErrors_GAMA_1
		* h_debug_SimSpawnErrors_GAMA_2
		* h_debug_SimSpawnErrors_GAMA_3
		* h_debug_SimSpawnErrors_a_spawnWaveCommon
		* h_debug_SimSpawnErrors_a_spawnWaveEpic
		* h_debug_SimSpawnErrors_a_spawnWaveRare
		* h_debug_SimSpawnErrors_a_spawnWaveUncommon

## h_debug_SimSpawnErrors_t_KillCommon
	* StepId: 1
	* Type: TriggerRepeating
	* TargetType: AllUnitsWithTagsAreKilled
	* SuccLL: h_debug_SimSpawnErrors_a_respawnCommon

## h_debug_SimSpawnErrors_t_KillEpic
	* StepId: 4
	* Type: TriggerRepeating
	* TargetType: AllUnitsWithTagsAreKilled
	* SuccLL: h_debug_SimSpawnErrors_a_respawnEpic

## h_debug_SimSpawnErrors_t_KillRare
	* StepId: 3
	* Type: TriggerRepeating
	* TargetType: AllUnitsWithTagsAreKilled
	* SuccLL: h_debug_SimSpawnErrors_a_respawnRare

## h_debug_SimSpawnErrors_t_KillUncommon
	* StepId: 2
	* Type: TriggerRepeating
	* TargetType: AllUnitsWithTagsAreKilled
	* SuccLL: h_debug_SimSpawnErrors_a_respawnUncommon

## h_debug_spawnSingleEnemy_Start
	* StepId: 0
	* Type: None
	* TargetType: MissionStart
	* SuccLL: 
		* h_debug_spawnSingleEnemy_GAMA_0
		* h_debug_spawnSingleEnemy_spawnWave1
		* h_debug_spawnSingleEnemy_spawnWave2
		* h_debug_spawnSingleEnemy_spawnWave3

## h_debug_spawnSingleEnemy_triggerKillDefinedWaves
	* StepId: 1
	* Type: TriggerRepeating
	* TargetType: KillDefinedWaves

## h_debug_Test_Start
	* StepId: 0
	* Type: Trigger
	* TargetType: MissionStart
	* SuccLL: h_debug_Test_GAMA_0

## h_debug_Test_w_intro
	* StepId: 1
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_debug_Test_GAMA_1
		* h_debug_Test_lookAt_intro
		* h_debug_Test_spawn_wave

## h_debug_Test_w_intro2
	* StepId: 2
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_debug_Test_position_wave

## h_event_anniversary2023_Wiracoda_9cce832fae199bd43a0a8cd2e23ed239
	* StepId: 79
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* h_event_anniversary2023_Wiracoda_td_deviceKilled
		* h_event_anniversary2023_Wiracoda_w_failForce
	* SuccLL: h_event_anniversary2023_Wiracoda_fail

## h_event_anniversary2023_Wiracoda_goal_connect
	* StepId: 10
	* Type: Goal
	* TargetType: WaitForTime

## h_event_anniversary2023_Wiracoda_goal_escort
	* StepId: 8
	* Type: Trigger
	* TargetType: ReachPointOfInterest
	* SuccLL: 
		* h_event_anniversary2023_Wiracoda_GAMA_8
		* h_event_anniversary2023_Wiracoda_d_connection
		* h_event_anniversary2023_Wiracoda_deactivate_device2

## h_event_anniversary2023_Wiracoda_goal_killMalik
	* StepId: 34
	* Type: Goal
	* TargetType: FinishGoalsString

## h_event_anniversary2023_Wiracoda_goal_killPirates
	* StepId: 22
	* Type: Goal
	* TargetType: FinishGoalsString

## h_event_anniversary2023_Wiracoda_goal_protect
	* StepId: 7
	* Type: Goal
	* TargetType: FinishGoalsString

## h_event_anniversary2023_Wiracoda_health_cateHalf
	* StepId: 23
	* Type: Trigger
	* TargetType: TaggedUnitsBelowHealthAndArmor
	* SuccLL: 
		* h_event_anniversary2023_Wiracoda_GAMA_23
		* h_event_anniversary2023_Wiracoda_GAMA_57
		* h_event_anniversary2023_Wiracoda_GAMA_58

## h_event_anniversary2023_Wiracoda_health_cateLow
	* StepId: 24
	* Type: Trigger
	* TargetType: TaggedUnitsBelowHealthAndArmor
	* SuccLL: 
		* h_event_anniversary2023_Wiracoda_GAMA_24
		* h_event_anniversary2023_Wiracoda_fow_offMalikSequence

## h_event_anniversary2023_Wiracoda_health_malik1
	* StepId: 36
	* Type: Trigger
	* TargetType: TaggedUnitsBelowHealthAndArmor
	* SuccLL: 
		* h_event_anniversary2023_Wiracoda_GAMA_36
		* h_event_anniversary2023_Wiracoda_GAMA_48

## h_event_anniversary2023_Wiracoda_healthCheck_malik2
	* StepId: 39
	* Type: Trigger
	* TargetType: TaggedUnitsBelowHealthAndArmor
	* SuccLL: 
		* h_event_anniversary2023_Wiracoda_GAMA_39
		* h_event_anniversary2023_Wiracoda_GAMA_43

## h_event_anniversary2023_Wiracoda_i_cateHealing
	* StepId: 59
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_event_anniversary2023_Wiracoda_GAMA_59
		* h_event_anniversary2023_Wiracoda_armor_cate50
		* h_event_anniversary2023_Wiracoda_health_cate50
		* h_event_anniversary2023_Wiracoda_vfx_healingCate
		* h_event_anniversary2023_Wiracoda_vfx_repairSkillCate

## h_event_anniversary2023_Wiracoda_i_intro
	* StepId: 2
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_event_anniversary2023_Wiracoda_GAMA_2
		* h_event_anniversary2023_Wiracoda_GAMA_3

## h_event_anniversary2023_Wiracoda_i_malikRegenA
	* StepId: 49
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_event_anniversary2023_Wiracoda_GAMA_49
		* h_event_anniversary2023_Wiracoda_health_malikRegenA1
		* h_event_anniversary2023_Wiracoda_vfx_malikRegenA1
		* h_event_anniversary2023_Wiracoda_vfx_malikRegenA2

## h_event_anniversary2023_Wiracoda_i_malikRegenB
	* StepId: 44
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_event_anniversary2023_Wiracoda_GAMA_44
		* h_event_anniversary2023_Wiracoda_health_malikRegenB1
		* h_event_anniversary2023_Wiracoda_vfx_malikRegen2
		* h_event_anniversary2023_Wiracoda_vfx_malikRegenB2

## h_event_anniversary2023_Wiracoda_i_setip
	* StepId: 1
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: h_event_anniversary2023_Wiracoda_ally_device

## h_event_anniversary2023_Wiracoda_kill_device
	* StepId: 77
	* Type: Trigger
	* TargetType: KillSpecificWave
	* SuccLL: 
		* h_event_anniversary2023_Wiracoda_GAMA_77
		* h_event_anniversary2023_Wiracoda_deactivate_goals

## h_event_anniversary2023_Wiracoda_multi_dControl
	* StepId: 16
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* h_event_anniversary2023_Wiracoda_td_control
		* h_event_anniversary2023_Wiracoda_w_dControl
	* SuccLL: 
		* h_event_anniversary2023_Wiracoda_GAMA_16
		* h_event_anniversary2023_Wiracoda_deactivate_killDevice
		* h_event_anniversary2023_Wiracoda_invincible_device

## h_event_anniversary2023_Wiracoda_multi_dProgRetreating
	* StepId: 15
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* h_event_anniversary2023_Wiracoda_td_progRetreating
		* h_event_anniversary2023_Wiracoda_w_dProgRetreating
	* SuccLL: 
		* h_event_anniversary2023_Wiracoda_GAMA_15
		* h_event_anniversary2023_Wiracoda_GAMA_70
		* h_event_anniversary2023_Wiracoda_GAMA_71
		* h_event_anniversary2023_Wiracoda_d_control

## h_event_anniversary2023_Wiracoda_multi_fin
	* StepId: 41
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* h_event_anniversary2023_Wiracoda_td_escape
		* h_event_anniversary2023_Wiracoda_w_fin
	* SuccLL: h_event_anniversary2023_Wiracoda_fin_jumpOut

## h_event_anniversary2023_Wiracoda_multi_malikCombat
	* StepId: 32
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* h_event_anniversary2023_Wiracoda_td_cateRetreating
		* h_event_anniversary2023_Wiracoda_w_cateRetreating2
	* SuccLL: h_event_anniversary2023_Wiracoda_GAMA_32

## h_event_anniversary2023_Wiracoda_start
	* StepId: 0
	* Type: Trigger
	* TargetType: MissionStart
	* SuccLL: 
		* h_event_anniversary2023_Wiracoda_GAMA_0
		* h_event_anniversary2023_Wiracoda_GAMA_1

## h_event_anniversary2023_Wiracoda_td_cateRetreating
	* StepId: 55
	* Type: Trigger
	* TargetType: OnDialogFinishedIndex

## h_event_anniversary2023_Wiracoda_td_control
	* StepId: 72
	* Type: Trigger
	* TargetType: OnDialogFinishedIndex

## h_event_anniversary2023_Wiracoda_td_deviceKilled
	* StepId: 81
	* Type: Trigger
	* TargetType: OnDialogFinishedIndex

## h_event_anniversary2023_Wiracoda_td_escape
	* StepId: 43
	* Type: Trigger
	* TargetType: OnDialogFinishedIndex

## h_event_anniversary2023_Wiracoda_td_intro
	* StepId: 5
	* Type: Trigger
	* TargetType: OnDialogFinishedIndex
	* SuccLL: h_event_anniversary2023_Wiracoda_GAMA_5

## h_event_anniversary2023_Wiracoda_td_progRetreating
	* StepId: 74
	* Type: Trigger
	* TargetType: OnDialogFinishedIndex

## h_event_anniversary2023_Wiracoda_w_activateDevice
	* StepId: 82
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_event_anniversary2023_Wiracoda_activate_device

## h_event_anniversary2023_Wiracoda_w_activateMalik
	* StepId: 56
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_anniversary2023_Wiracoda_activate_malik
		* h_event_anniversary2023_Wiracoda_activate_player

## h_event_anniversary2023_Wiracoda_w_attack1
	* StepId: 11
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_anniversary2023_Wiracoda_GAMA_11
		* h_event_anniversary2023_Wiracoda_GAMA_75
		* h_event_anniversary2023_Wiracoda_wave_0

## h_event_anniversary2023_Wiracoda_w_attack2
	* StepId: 12
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_anniversary2023_Wiracoda_GAMA_12
		* h_event_anniversary2023_Wiracoda_wave_1

## h_event_anniversary2023_Wiracoda_w_attack3
	* StepId: 13
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_anniversary2023_Wiracoda_GAMA_13
		* h_event_anniversary2023_Wiracoda_wave_2

## h_event_anniversary2023_Wiracoda_w_cate2
	* StepId: 18
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_anniversary2023_Wiracoda_GAMA_18
		* h_event_anniversary2023_Wiracoda_GAMA_64
		* h_event_anniversary2023_Wiracoda_d_cateIncoming
		* h_event_anniversary2023_Wiracoda_deactivate_connectionGoal

## h_event_anniversary2023_Wiracoda_w_cate3
	* StepId: 19
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_anniversary2023_Wiracoda_GAMA_19
		* h_event_anniversary2023_Wiracoda_d_deviceLost

## h_event_anniversary2023_Wiracoda_w_cate4
	* StepId: 20
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_event_anniversary2023_Wiracoda_GAMA_20

## h_event_anniversary2023_Wiracoda_w_cate5
	* StepId: 21
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_anniversary2023_Wiracoda_GAMA_21
		* h_event_anniversary2023_Wiracoda_GAMA_22
		* h_event_anniversary2023_Wiracoda_activate_everything1
		* h_event_anniversary2023_Wiracoda_d_combat
		* h_event_anniversary2023_Wiracoda_deactivate_protectGoal

## h_event_anniversary2023_Wiracoda_w_cateHealing1
	* StepId: 60
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_anniversary2023_Wiracoda_GAMA_60
		* h_event_anniversary2023_Wiracoda_armor_cate60
		* h_event_anniversary2023_Wiracoda_health_cate60

## h_event_anniversary2023_Wiracoda_w_cateHealing2
	* StepId: 61
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_anniversary2023_Wiracoda_GAMA_61
		* h_event_anniversary2023_Wiracoda_armor_cate70
		* h_event_anniversary2023_Wiracoda_health_cate70

## h_event_anniversary2023_Wiracoda_w_cateHealing3
	* StepId: 62
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_anniversary2023_Wiracoda_GAMA_62
		* h_event_anniversary2023_Wiracoda_armor_cate80
		* h_event_anniversary2023_Wiracoda_health_cate80

## h_event_anniversary2023_Wiracoda_w_cateHealing4
	* StepId: 63
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_anniversary2023_Wiracoda_GAMA_63
		* h_event_anniversary2023_Wiracoda_armor_cate90
		* h_event_anniversary2023_Wiracoda_health_cate90

## h_event_anniversary2023_Wiracoda_w_cateHealing5
	* StepId: 64
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_anniversary2023_Wiracoda_armor_cate100
		* h_event_anniversary2023_Wiracoda_health_cate100

## h_event_anniversary2023_Wiracoda_w_cateRetreating1
	* StepId: 31
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_anniversary2023_Wiracoda_GAMA_31
		* h_event_anniversary2023_Wiracoda_GAMA_53
		* h_event_anniversary2023_Wiracoda_GAMA_54
		* h_event_anniversary2023_Wiracoda_activate_everything
		* h_event_anniversary2023_Wiracoda_ai_followFlagship
		* h_event_anniversary2023_Wiracoda_d_cateRetreating
		* h_event_anniversary2023_Wiracoda_deactivate_killPiratesGoal
		* h_event_anniversary2023_Wiracoda_remove_pirates

## h_event_anniversary2023_Wiracoda_w_cateRetreating2
	* StepId: 54
	* Type: Trigger
	* TargetType: WaitForTime

## h_event_anniversary2023_Wiracoda_w_cateSequence
	* StepId: 17
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_anniversary2023_Wiracoda_GAMA_17
		* h_event_anniversary2023_Wiracoda_GAMA_66
		* h_event_anniversary2023_Wiracoda_camera_cate
		* h_event_anniversary2023_Wiracoda_close_cateSequence
		* h_event_anniversary2023_Wiracoda_deactivate_everything1

## h_event_anniversary2023_Wiracoda_w_cateSpawn
	* StepId: 67
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_anniversary2023_Wiracoda_GAMA_67
		* h_event_anniversary2023_Wiracoda_deactivate_cate
		* h_event_anniversary2023_Wiracoda_invincible_cate5
		* h_event_anniversary2023_Wiracoda_wave_cate

## h_event_anniversary2023_Wiracoda_w_cateSpawn2
	* StepId: 68
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_anniversary2023_Wiracoda_GAMA_68
		* h_event_anniversary2023_Wiracoda_deactivate_pirates1
		* h_event_anniversary2023_Wiracoda_wave_4

## h_event_anniversary2023_Wiracoda_w_cateSpawn3
	* StepId: 69
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_anniversary2023_Wiracoda_GAMA_69
		* h_event_anniversary2023_Wiracoda_deactivate_pirates2
		* h_event_anniversary2023_Wiracoda_wave_5

## h_event_anniversary2023_Wiracoda_w_cateSpawn4
	* StepId: 70
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_anniversary2023_Wiracoda_deactivate_pirates3
		* h_event_anniversary2023_Wiracoda_wave_6
		* h_event_anniversary2023_Wiracoda_wave_7

## h_event_anniversary2023_Wiracoda_w_connection
	* StepId: 9
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_anniversary2023_Wiracoda_GAMA_10
		* h_event_anniversary2023_Wiracoda_GAMA_76
		* h_event_anniversary2023_Wiracoda_GAMA_9

## h_event_anniversary2023_Wiracoda_w_dCateFiller
	* StepId: 58
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_event_anniversary2023_Wiracoda_d_cateFiller

## h_event_anniversary2023_Wiracoda_w_dControl
	* StepId: 71
	* Type: Trigger
	* TargetType: WaitForTime

## h_event_anniversary2023_Wiracoda_w_deviceKill1
	* StepId: 65
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_anniversary2023_Wiracoda_GAMA_65
		* h_event_anniversary2023_Wiracoda_activate_ally
		* h_event_anniversary2023_Wiracoda_activate_pirates
		* h_event_anniversary2023_Wiracoda_preferredTarget_decive

## h_event_anniversary2023_Wiracoda_w_deviceKill2
	* StepId: 66
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_anniversary2023_Wiracoda_deactivate_piratesLast
		* h_event_anniversary2023_Wiracoda_health_killDevice

## h_event_anniversary2023_Wiracoda_w_dProgRetreating
	* StepId: 73
	* Type: Trigger
	* TargetType: WaitForTime

## h_event_anniversary2023_Wiracoda_w_end1
	* StepId: 40
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_anniversary2023_Wiracoda_GAMA_40
		* h_event_anniversary2023_Wiracoda_GAMA_41
		* h_event_anniversary2023_Wiracoda_GAMA_42
		* h_event_anniversary2023_Wiracoda_d_escape
		* h_event_anniversary2023_Wiracoda_deactivate_killMalik
		* h_event_anniversary2023_Wiracoda_invincible_flagship

## h_event_anniversary2023_Wiracoda_w_fail
	* StepId: 78
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_anniversary2023_Wiracoda_GAMA_78
		* h_event_anniversary2023_Wiracoda_GAMA_79
		* h_event_anniversary2023_Wiracoda_GAMA_80
		* h_event_anniversary2023_Wiracoda_d_deviceKilled

## h_event_anniversary2023_Wiracoda_w_failForce
	* StepId: 80
	* Type: Trigger
	* TargetType: WaitForTime

## h_event_anniversary2023_Wiracoda_w_fin
	* StepId: 42
	* Type: Trigger
	* TargetType: WaitForTime

## h_event_anniversary2023_Wiracoda_w_intro1
	* StepId: 4
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_anniversary2023_Wiracoda_GAMA_4
		* h_event_anniversary2023_Wiracoda_d_intro

## h_event_anniversary2023_Wiracoda_w_intro2
	* StepId: 6
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_anniversary2023_Wiracoda_GAMA_6
		* h_event_anniversary2023_Wiracoda_GAMA_7
		* h_event_anniversary2023_Wiracoda_GAMA_81
		* h_event_anniversary2023_Wiracoda_d_go

## h_event_anniversary2023_Wiracoda_w_lookAt
	* StepId: 3
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_anniversary2023_Wiracoda_deactivate_device1
		* h_event_anniversary2023_Wiracoda_lookAt_gate

## h_event_anniversary2023_Wiracoda_w_malik1
	* StepId: 26
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_anniversary2023_Wiracoda_GAMA_26
		* h_event_anniversary2023_Wiracoda_d_malikA

## h_event_anniversary2023_Wiracoda_w_malik2
	* StepId: 27
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_anniversary2023_Wiracoda_GAMA_27
		* h_event_anniversary2023_Wiracoda_d_malikB

## h_event_anniversary2023_Wiracoda_w_malik3
	* StepId: 28
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_anniversary2023_Wiracoda_GAMA_28
		* h_event_anniversary2023_Wiracoda_GAMA_55
		* h_event_anniversary2023_Wiracoda_d_malikC

## h_event_anniversary2023_Wiracoda_w_malik4
	* StepId: 29
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_anniversary2023_Wiracoda_GAMA_29
		* h_event_anniversary2023_Wiracoda_d_malikComment

## h_event_anniversary2023_Wiracoda_w_malik5
	* StepId: 30
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_anniversary2023_Wiracoda_GAMA_30
		* h_event_anniversary2023_Wiracoda_wave_10

## h_event_anniversary2023_Wiracoda_w_malikCombat
	* StepId: 33
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_anniversary2023_Wiracoda_GAMA_33
		* h_event_anniversary2023_Wiracoda_GAMA_34
		* h_event_anniversary2023_Wiracoda_d_standGround

## h_event_anniversary2023_Wiracoda_w_malikRegen2
	* StepId: 37
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_anniversary2023_Wiracoda_GAMA_37
		* h_event_anniversary2023_Wiracoda_d_regeneration

## h_event_anniversary2023_Wiracoda_w_malikRegen3
	* StepId: 38
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_event_anniversary2023_Wiracoda_GAMA_38

## h_event_anniversary2023_Wiracoda_w_malikRegenA1
	* StepId: 50
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_event_anniversary2023_Wiracoda_GAMA_50
	* FailLL: h_event_anniversary2023_Wiracoda_health_malikRegenA2

## h_event_anniversary2023_Wiracoda_w_malikRegenA2
	* StepId: 51
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_event_anniversary2023_Wiracoda_GAMA_51
	* FailLL: h_event_anniversary2023_Wiracoda_health_malikRegenA3

## h_event_anniversary2023_Wiracoda_w_malikRegenA3
	* StepId: 52
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_anniversary2023_Wiracoda_GAMA_52
		* h_event_anniversary2023_Wiracoda_health_malikRegenA4

## h_event_anniversary2023_Wiracoda_w_malikRegenA4
	* StepId: 53
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_event_anniversary2023_Wiracoda_health_malikRegenA5

## h_event_anniversary2023_Wiracoda_w_malikRegenB1
	* StepId: 45
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_anniversary2023_Wiracoda_GAMA_45
		* h_event_anniversary2023_Wiracoda_health_malikRegenB2

## h_event_anniversary2023_Wiracoda_w_malikRegenB2
	* StepId: 46
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_anniversary2023_Wiracoda_GAMA_46
		* h_event_anniversary2023_Wiracoda_health_malikRegenB3

## h_event_anniversary2023_Wiracoda_w_malikRegenB3
	* StepId: 47
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_anniversary2023_Wiracoda_GAMA_47
		* h_event_anniversary2023_Wiracoda_health_malikRegenB4

## h_event_anniversary2023_Wiracoda_w_malikRegenB4
	* StepId: 48
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_event_anniversary2023_Wiracoda_health_malikRegenB5

## h_event_anniversary2023_Wiracoda_w_malikRegenCheck
	* StepId: 35
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_event_anniversary2023_Wiracoda_GAMA_35

## h_event_anniversary2023_Wiracoda_w_malikSequence
	* StepId: 25
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_anniversary2023_Wiracoda_GAMA_25
		* h_event_anniversary2023_Wiracoda_GAMA_56
		* h_event_anniversary2023_Wiracoda_camera_malik
		* h_event_anniversary2023_Wiracoda_close_malikSequence

## h_event_anniversary2023_Wiracoda_w_malikSpawn
	* StepId: 57
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_anniversary2023_Wiracoda_deactivate_everything2
		* h_event_anniversary2023_Wiracoda_invincible_Malik
		* h_event_anniversary2023_Wiracoda_wave_malik

## h_event_anniversary2023_Wiracoda_w_progIncoming1
	* StepId: 76
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_event_anniversary2023_Wiracoda_d_progIncoming

## h_event_anniversary2023_Wiracoda_w_progRetreating1
	* StepId: 14
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_anniversary2023_Wiracoda_GAMA_14
		* h_event_anniversary2023_Wiracoda_GAMA_72
		* h_event_anniversary2023_Wiracoda_GAMA_73
		* h_event_anniversary2023_Wiracoda_GAMA_74
		* h_event_anniversary2023_Wiracoda_remove_progs

## h_event_anniversary2023_Wiracoda_w_progRetreatingDialog
	* StepId: 75
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_event_anniversary2023_Wiracoda_d_progRetreating

## h_event_halloween2023_Rashidun_61d61b659b0b18c4a9556c108f15f0e8
	* StepId: 17
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* h_event_halloween2023_Rashidun_td_malikDeath
		* h_event_halloween2023_Rashidun_w_malikDeathDialog
	* SuccLL: 
		* h_event_halloween2023_Rashidun_GAMA_17
		* h_event_halloween2023_Rashidun_close_malikDeath

## h_event_halloween2023_Rashidun_goal_killDerelicts
	* StepId: 11
	* Type: Goal
	* TargetType: FinishGoalsString
	* TVS: 
		* h_event_halloween2023_Rashidun_kill_derelict1
		* h_event_halloween2023_Rashidun_kill_derelict2
	* SuccLL: 
		* h_event_halloween2023_Rashidun_GAMA_11
		* h_event_halloween2023_Rashidun_desctivate_healthCheckMalikB

## h_event_halloween2023_Rashidun_goal_killMalik
	* StepId: 13
	* Type: Goal
	* TargetType: FinishGoalsString
	* TVS: h_event_halloween2023_Rashidun_w_killMalik

## h_event_halloween2023_Rashidun_healthCheack_malikDeath
	* StepId: 16
	* Type: Trigger
	* TargetType: TaggedUnitsBelowHealthAndArmor
	* SuccLL: 
		* h_event_halloween2023_Rashidun_GAMA_16
		* h_event_halloween2023_Rashidun_GAMA_20
		* h_event_halloween2023_Rashidun_GAMA_21
		* h_event_halloween2023_Rashidun_d_malikDeath
		* h_event_halloween2023_Rashidun_invincible_everything

## h_event_halloween2023_Rashidun_healthCheck_derelictA
	* StepId: 29
	* Type: Trigger
	* TargetType: TaggedUnitsBelowHealthAndArmor
	* SuccLL: 
		* h_event_halloween2023_Rashidun_GAMA_29
		* h_event_halloween2023_Rashidun_invincible_derelictBBuffer1
		* h_event_halloween2023_Rashidun_kill_derelictA
		* h_event_halloween2023_Rashidun_vfx_derelictA

## h_event_halloween2023_Rashidun_healthCheck_derelictAWave
	* StepId: 27
	* Type: Trigger
	* TargetType: TaggedUnitsBelowHealthAndArmor
	* SuccLL: 
		* h_event_halloween2023_Rashidun_GAMA_27
		* h_event_halloween2023_Rashidun_GAMA_30
		* h_event_halloween2023_Rashidun_wave_derelictAWave

## h_event_halloween2023_Rashidun_healthCheck_derelictB
	* StepId: 34
	* Type: Trigger
	* TargetType: TaggedUnitsBelowHealthAndArmor
	* SuccLL: 
		* h_event_halloween2023_Rashidun_GAMA_34
		* h_event_halloween2023_Rashidun_invincible_derelictABuffer1
		* h_event_halloween2023_Rashidun_kill_derelictB
		* h_event_halloween2023_Rashidun_vfx_derelictB

## h_event_halloween2023_Rashidun_healthCheck_derelictBWave
	* StepId: 32
	* Type: Trigger
	* TargetType: TaggedUnitsBelowHealthAndArmor
	* SuccLL: 
		* h_event_halloween2023_Rashidun_GAMA_32
		* h_event_halloween2023_Rashidun_GAMA_35
		* h_event_halloween2023_Rashidun_wave_derelictBWave

## h_event_halloween2023_Rashidun_healthCheck_malikA
	* StepId: 38
	* Type: TriggerRepeating
	* TargetType: TaggedUnitsBelowHealthAndArmor
	* SuccLL: 
		* h_event_halloween2023_Rashidun_GAMA_38
		* h_event_halloween2023_Rashidun_GAMA_42
		* h_event_halloween2023_Rashidun_health_malikA1
		* h_event_halloween2023_Rashidun_vfx_MalikHealA2
		* h_event_halloween2023_Rashidun_vfx_malikHealA1

## h_event_halloween2023_Rashidun_healthCheck_malikB
	* StepId: 44
	* Type: TriggerRepeating
	* TargetType: TaggedUnitsBelowHealthAndArmor
	* SuccLL: 
		* h_event_halloween2023_Rashidun_GAMA_44
		* h_event_halloween2023_Rashidun_GAMA_48
		* h_event_halloween2023_Rashidun_health_malikB1
		* h_event_halloween2023_Rashidun_vfx_malikHealB1
		* h_event_halloween2023_Rashidun_vfx_malikHealB2

## h_event_halloween2023_Rashidun_healthCheck_malikLow
	* StepId: 15
	* Type: Trigger
	* TargetType: TaggedUnitsBelowHealthAndArmor
	* SuccLL: 
		* h_event_halloween2023_Rashidun_GAMA_15
		* h_event_halloween2023_Rashidun_d_malikDestroyB
		* h_event_halloween2023_Rashidun_invincible_malikLast

## h_event_halloween2023_Rashidun_i_derelictSetup
	* StepId: 10
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_event_halloween2023_Rashidun_GAMA_10
		* h_event_halloween2023_Rashidun_GAMA_22
		* h_event_halloween2023_Rashidun_GAMA_24
		* h_event_halloween2023_Rashidun_GAMA_25
		* h_event_halloween2023_Rashidun_GAMA_26
		* h_event_halloween2023_Rashidun_GAMA_31

## h_event_halloween2023_Rashidun_i_intro
	* StepId: 1
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_event_halloween2023_Rashidun_GAMA_1
		* h_event_halloween2023_Rashidun_GAMA_2

## h_event_halloween2023_Rashidun_i_malikSetup
	* StepId: 37
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_event_halloween2023_Rashidun_GAMA_37
		* h_event_halloween2023_Rashidun_GAMA_43

## h_event_halloween2023_Rashidun_i_setup
	* StepId: 52
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_event_halloween2023_Rashidun_invincible_derelictA
		* h_event_halloween2023_Rashidun_invincible_derelictB
		* h_event_halloween2023_Rashidun_wave_derelictA
		* h_event_halloween2023_Rashidun_wave_derelictB

## h_event_halloween2023_Rashidun_kill_derelict1
	* StepId: 25
	* Type: Trigger
	* TargetType: KillSpecificWave

## h_event_halloween2023_Rashidun_kill_derelict2
	* StepId: 26
	* Type: Trigger
	* TargetType: KillSpecificWave

## h_event_halloween2023_Rashidun_multi_killFirstDerelict
	* StepId: 23
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* h_event_halloween2023_Rashidun_kill_derelict1
		* h_event_halloween2023_Rashidun_kill_derelict2
	* SuccLL: 
		* h_event_halloween2023_Rashidun_GAMA_23
		* h_event_halloween2023_Rashidun_desctivate_healthCheckMalikA

## h_event_halloween2023_Rashidun_start
	* StepId: 0
	* Type: Trigger
	* TargetType: MissionStart
	* SuccLL: 
		* h_event_halloween2023_Rashidun_GAMA_0
		* h_event_halloween2023_Rashidun_GAMA_51

## h_event_halloween2023_Rashidun_td_intro
	* StepId: 4
	* Type: Trigger
	* TargetType: OnDialogFinishedIndex
	* SuccLL: h_event_halloween2023_Rashidun_GAMA_4

## h_event_halloween2023_Rashidun_td_malikDeath
	* StepId: 22
	* Type: Trigger
	* TargetType: OnDialogFinishedIndex

## h_event_halloween2023_Rashidun_td_outro
	* StepId: 20
	* Type: Trigger
	* TargetType: OnDialogFinishedIndex
	* SuccLL: h_event_halloween2023_Rashidun_fin

## h_event_halloween2023_Rashidun_w_activate
	* StepId: 50
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_event_halloween2023_Rashidun_activate_everything

## h_event_halloween2023_Rashidun_w_derelictABuffer
	* StepId: 28
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_halloween2023_Rashidun_GAMA_28
		* h_event_halloween2023_Rashidun_invincible_derelictA2

## h_event_halloween2023_Rashidun_w_derelictAInvincibleBuffer
	* StepId: 35
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_event_halloween2023_Rashidun_invincible_derelictABuffer2

## h_event_halloween2023_Rashidun_w_derelictAWave
	* StepId: 31
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_event_halloween2023_Rashidun_d_derelictAWave

## h_event_halloween2023_Rashidun_w_derelictBBuffer
	* StepId: 33
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_halloween2023_Rashidun_GAMA_33
		* h_event_halloween2023_Rashidun_invincible_derelictB2

## h_event_halloween2023_Rashidun_w_derelictBInvincibleBuffer
	* StepId: 30
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_event_halloween2023_Rashidun_invincible_derelictBBuffer2

## h_event_halloween2023_Rashidun_w_derelictBWave
	* StepId: 36
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_event_halloween2023_Rashidun_d_derelictBWave

## h_event_halloween2023_Rashidun_w_intro1
	* StepId: 2
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_halloween2023_Rashidun_deactivate_everything
		* h_event_halloween2023_Rashidun_lookAt_center

## h_event_halloween2023_Rashidun_w_intro2
	* StepId: 3
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_halloween2023_Rashidun_GAMA_3
		* h_event_halloween2023_Rashidun_d_intro
		* h_event_halloween2023_Rashidun_deactivate_everything2

## h_event_halloween2023_Rashidun_w_killDerelicts
	* StepId: 12
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_halloween2023_Rashidun_GAMA_12
		* h_event_halloween2023_Rashidun_GAMA_13
		* h_event_halloween2023_Rashidun_d_relictDownB

## h_event_halloween2023_Rashidun_w_killFirstDerelict
	* StepId: 24
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_halloween2023_Rashidun_d_derelictDownA
		* h_event_halloween2023_Rashidun_invincible_malikWeakened

## h_event_halloween2023_Rashidun_w_killMalik
	* StepId: 18
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_halloween2023_Rashidun_GAMA_18
		* h_event_halloween2023_Rashidun_kill_malik
		* h_event_halloween2023_Rashidun_remove_enemies
		* h_event_halloween2023_Rashidun_vfx_malikDeath

## h_event_halloween2023_Rashidun_w_malikDeathDialog
	* StepId: 21
	* Type: Trigger
	* TargetType: WaitForTime

## h_event_halloween2023_Rashidun_w_malikRegenA1
	* StepId: 39
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_halloween2023_Rashidun_GAMA_39
		* h_event_halloween2023_Rashidun_health_malikA2

## h_event_halloween2023_Rashidun_w_malikRegenA2
	* StepId: 40
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_halloween2023_Rashidun_GAMA_40
		* h_event_halloween2023_Rashidun_health_malikA3

## h_event_halloween2023_Rashidun_w_malikRegenA3
	* StepId: 41
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_halloween2023_Rashidun_GAMA_41
		* h_event_halloween2023_Rashidun_health_malikA4

## h_event_halloween2023_Rashidun_w_malikRegenA4
	* StepId: 42
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_event_halloween2023_Rashidun_health_malikA5

## h_event_halloween2023_Rashidun_w_malikRegenADialog
	* StepId: 43
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_event_halloween2023_Rashidun_d_malikRegenA

## h_event_halloween2023_Rashidun_w_malikRegenB1
	* StepId: 45
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_halloween2023_Rashidun_GAMA_45
		* h_event_halloween2023_Rashidun_health_malikB2

## h_event_halloween2023_Rashidun_w_malikRegenB2
	* StepId: 46
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_halloween2023_Rashidun_GAMA_46
		* h_event_halloween2023_Rashidun_health_malikB3

## h_event_halloween2023_Rashidun_w_malikRegenB3
	* StepId: 47
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_halloween2023_Rashidun_GAMA_47
		* h_event_halloween2023_Rashidun_health_malikB4

## h_event_halloween2023_Rashidun_w_malikRegenB4
	* StepId: 48
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_event_halloween2023_Rashidun_health_malikB5

## h_event_halloween2023_Rashidun_w_malikRegenBDialog
	* StepId: 49
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_event_halloween2023_Rashidun_d_

## h_event_halloween2023_Rashidun_w_malikSequence1
	* StepId: 5
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_halloween2023_Rashidun_GAMA_5
		* h_event_halloween2023_Rashidun_GAMA_50
		* h_event_halloween2023_Rashidun_camera_malik
		* h_event_halloween2023_Rashidun_close_malikSequence

## h_event_halloween2023_Rashidun_w_malikSequence2
	* StepId: 6
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_halloween2023_Rashidun_GAMA_6
		* h_event_halloween2023_Rashidun_d_malikSee

## h_event_halloween2023_Rashidun_w_malikSequence3
	* StepId: 7
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_halloween2023_Rashidun_GAMA_49
		* h_event_halloween2023_Rashidun_GAMA_7
		* h_event_halloween2023_Rashidun_d_malikDestroy2

## h_event_halloween2023_Rashidun_w_malikSequence4
	* StepId: 8
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_halloween2023_Rashidun_GAMA_8
		* h_event_halloween2023_Rashidun_wave_malikWave

## h_event_halloween2023_Rashidun_w_malikSequence5
	* StepId: 9
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_halloween2023_Rashidun_GAMA_36
		* h_event_halloween2023_Rashidun_GAMA_9
		* h_event_halloween2023_Rashidun_d_combat

## h_event_halloween2023_Rashidun_w_malikSpawn
	* StepId: 51
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_halloween2023_Rashidun_deactivate_malik
		* h_event_halloween2023_Rashidun_invincible_malik
		* h_event_halloween2023_Rashidun_wave_malik

## h_event_halloween2023_Rashidun_w_outro
	* StepId: 19
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_halloween2023_Rashidun_GAMA_19
		* h_event_halloween2023_Rashidun_d_outro

## h_event_halloween2023_Rashidun_w_relictDownBBuffer
	* StepId: 14
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_event_halloween2023_Rashidun_GAMA_14

## h_event_iyaFall2023_Escort_allyHealthLow
	* StepId: 19
	* Type: Trigger
	* TargetType: TaggedUnitsBelowStrength
	* SuccLL: h_event_iyaFall2023_Escort_d_allyLow

## h_event_iyaFall2023_Escort_goal_countdown
	* StepId: 27
	* Type: Goal
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_iyaFall2023_Escort_GAMA_27
		* h_event_iyaFall2023_Escort_remove_enemies

## h_event_iyaFall2023_Escort_goal_defend
	* StepId: 29
	* Type: Goal
	* TargetType: FinishGoalsString
	* TVS: h_event_iyaFall2023_Escort_goal_countdown

## h_event_iyaFall2023_Escort_goal_escort
	* StepId: 26
	* Type: Goal
	* TargetType: ReachPointOfInterest
	* SuccLL: 
		* h_event_iyaFall2023_Escort_GAMA_26
		* h_event_iyaFall2023_Escort_GAMA_28
		* h_event_iyaFall2023_Escort_GAMA_29
		* h_event_iyaFall2023_Escort_d_win
		* h_event_iyaFall2023_Escort_desctivate_preGoals
		* h_event_iyaFall2023_Escort_stopShip

## h_event_iyaFall2023_Escort_i_Allies
	* StepId: 12
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_event_iyaFall2023_Escort_GAMA_12
		* h_event_iyaFall2023_Escort_GAMA_13
		* h_event_iyaFall2023_Escort_GAMA_18

## h_event_iyaFall2023_Escort_i_AllySpawns
	* StepId: 13
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_event_iyaFall2023_Escort_ally0
		* h_event_iyaFall2023_Escort_ally1

## h_event_iyaFall2023_Escort_i_Intro
	* StepId: 20
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_event_iyaFall2023_Escort_GAMA_20
		* h_event_iyaFall2023_Escort_GAMA_21

## h_event_iyaFall2023_Escort_i2
	* StepId: 2
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_event_iyaFall2023_Escort_GAMA_2
		* h_event_iyaFall2023_Escort_GAMA_4
		* h_event_iyaFall2023_Escort_GAMA_6
		* h_event_iyaFall2023_Escort_GAMA_8

## h_event_iyaFall2023_Escort_killAlly0
	* StepId: 14
	* Type: Trigger
	* TargetType: KillSpecificWave
	* SuccLL: 
		* h_event_iyaFall2023_Escort_GAMA_14
		* h_event_iyaFall2023_Escort_GAMA_15
		* h_event_iyaFall2023_Escort_GAMA_16
		* h_event_iyaFall2023_Escort_deactivateGoal

## h_event_iyaFall2023_Escort_multi_fail
	* StepId: 15
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* h_event_iyaFall2023_Escort_td_fail
		* h_event_iyaFall2023_Escort_wait_fail
	* SuccLL: h_event_iyaFall2023_Escort_fail

## h_event_iyaFall2023_Escort_reachPOIPath1
	* StepId: 3
	* Type: Trigger
	* TargetType: ReachPointOfInterest
	* SuccLL: 
		* h_event_iyaFall2023_Escort_GAMA_3
		* h_event_iyaFall2023_Escort_wave0

## h_event_iyaFall2023_Escort_reachPOIPath2
	* StepId: 5
	* Type: Trigger
	* TargetType: ReachPointOfInterest
	* SuccLL: 
		* h_event_iyaFall2023_Escort_GAMA_5
		* h_event_iyaFall2023_Escort_wave1

## h_event_iyaFall2023_Escort_reachPOIPath3
	* StepId: 7
	* Type: Trigger
	* TargetType: ReachPointOfInterest
	* SuccLL: 
		* h_event_iyaFall2023_Escort_GAMA_7
		* h_event_iyaFall2023_Escort_wave2

## h_event_iyaFall2023_Escort_reachPOIPath4
	* StepId: 9
	* Type: Trigger
	* TargetType: ReachPointOfInterest
	* SuccLL: 
		* h_event_iyaFall2023_Escort_GAMA_9
		* h_event_iyaFall2023_Escort_wave3

## h_event_iyaFall2023_Escort_repeatingKillAllCheck
	* StepId: 11
	* Type: TriggerRepeating
	* TargetType: WaveFinished
	* SuccLL: h_event_iyaFall2023_Escort_d_killAll

## h_event_iyaFall2023_Escort_start
	* StepId: 0
	* Type: Trigger
	* TargetType: MissionStart
	* SuccLL: 
		* h_event_iyaFall2023_Escort_GAMA_0
		* h_event_iyaFall2023_Escort_GAMA_1
		* h_event_iyaFall2023_Escort_GAMA_10
		* h_event_iyaFall2023_Escort_GAMA_11
		* h_event_iyaFall2023_Escort_GAMA_19

## h_event_iyaFall2023_Escort_td_fail
	* StepId: 16
	* Type: Trigger
	* TargetType: OnDialogFinishedIndex

## h_event_iyaFall2023_Escort_td_intro1
	* StepId: 23
	* Type: Trigger
	* TargetType: OnDialogFinishedIndex
	* SuccLL: 
		* h_event_iyaFall2023_Escort_GAMA_23
		* h_event_iyaFall2023_Escort_GAMA_25
		* h_event_iyaFall2023_Escort_d_go

## h_event_iyaFall2023_Escort_td_win_fac
	* StepId: 1
	* Type: Trigger
	* TargetType: OnDialogFinishedIndex
	* SuccLL: h_event_iyaFall2023_Escort_win

## h_event_iyaFall2023_Escort_w_attack1
	* StepId: 30
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_iyaFall2023_Escort_GAMA_30
		* h_event_iyaFall2023_Escort_GAMA_32
		* h_event_iyaFall2023_Escort_wave4

## h_event_iyaFall2023_Escort_w_attack2
	* StepId: 31
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_iyaFall2023_Escort_GAMA_31
		* h_event_iyaFall2023_Escort_wave5

## h_event_iyaFall2023_Escort_w_attack3
	* StepId: 32
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_event_iyaFall2023_Escort_wave6

## h_event_iyaFall2023_Escort_w_attackDialog
	* StepId: 33
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_event_iyaFall2023_Escort_d_wave3

## h_event_iyaFall2023_Escort_w_go
	* StepId: 24
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_event_iyaFall2023_Escort_GAMA_24

## h_event_iyaFall2023_Escort_w_go2
	* StepId: 25
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_event_iyaFall2023_Escort_setActive

## h_event_iyaFall2023_Escort_w_wave0
	* StepId: 4
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_event_iyaFall2023_Escort_d_hostiles0

## h_event_iyaFall2023_Escort_w_wave1
	* StepId: 6
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_event_iyaFall2023_Escort_d_hostiles1

## h_event_iyaFall2023_Escort_w_wave2
	* StepId: 8
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_event_iyaFall2023_Escort_d_hostiles2

## h_event_iyaFall2023_Escort_w_wave3
	* StepId: 10
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_event_iyaFall2023_Escort_d_hostiles3

## h_event_iyaFall2023_Escort_w_win
	* StepId: 28
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_event_iyaFall2023_Escort_d_wi

## h_event_iyaFall2023_Escort_wait_fail
	* StepId: 18
	* Type: Trigger
	* TargetType: WaitForTime

## h_event_iyaFall2023_Escort_wait1
	* StepId: 22
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_iyaFall2023_Escort_GAMA_22
		* h_event_iyaFall2023_Escort_d_intro1

## h_event_iyaFall2023_Escort_wait5
	* StepId: 17
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_iyaFall2023_Escort_GAMA_17
		* h_event_iyaFall2023_Escort_d_fail

## h_event_iyaFall2023_Escort_wait7
	* StepId: 21
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_iyaFall2023_Escort_deactivate_Ally
		* h_event_iyaFall2023_Escort_lookAt_escort
		* h_event_iyaFall2023_Escort_preferredTarget

## h_event_tanWin2023_Academy_goal_defendAcademy
	* StepId: 18
	* Type: Goal
	* TargetType: FinishGoalsString

## h_event_tanWin2023_Academy_goal_defendTepin
	* StepId: 33
	* Type: Goal
	* TargetType: FinishGoalsString

## h_event_tanWin2023_Academy_goal_killVaygr
	* StepId: 15
	* Type: Goal
	* TargetType: FinishGoalsString
	* TVS: h_event_tanWin2023_Academy_i_allVaygrDead
	* SuccLL: 
		* h_event_tanWin2023_Academy_GAMA_15
		* h_event_tanWin2023_Academy_succeed_defendGoals

## h_event_tanWin2023_Academy_healthCheck_academyLow
	* StepId: 20
	* Type: Trigger
	* TargetType: TaggedUnitsBelowHealthAndArmor
	* SuccLL: h_event_tanWin2023_Academy_d_academyLow

## h_event_tanWin2023_Academy_healthCheck_JochikA
	* StepId: 25
	* Type: Trigger
	* TargetType: TaggedUnitsBelowHealthAndArmor
	* SuccLL: 
		* h_event_tanWin2023_Academy_GAMA_25
		* h_event_tanWin2023_Academy_d_jochikDownA

## h_event_tanWin2023_Academy_healthCheck_JochikB
	* StepId: 39
	* Type: Trigger
	* TargetType: TaggedUnitsBelowHealthAndArmor
	* SuccLL: 
		* h_event_tanWin2023_Academy_GAMA_39
		* h_event_tanWin2023_Academy_d_JochikDownB

## h_event_tanWin2023_Academy_i_academyChecks
	* StepId: 19
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_event_tanWin2023_Academy_GAMA_19
		* h_event_tanWin2023_Academy_GAMA_20

## h_event_tanWin2023_Academy_i_allVaygrDead
	* StepId: 42
	* Type: Trigger
	* TargetType: Immediate

## h_event_tanWin2023_Academy_i_gameplay
	* StepId: 43
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_event_tanWin2023_Academy_activate_everything2
		* h_event_tanWin2023_Academy_deactivate_outposts
		* h_event_tanWin2023_Academy_setHealth_HeyokaKill
		* h_event_tanWin2023_Academy_vincible_chicuat
		* h_event_tanWin2023_Academy_vincible_tecuban
		* h_event_tanWin2023_Academy_vincible_vaygr

## h_event_tanWin2023_Academy_i_goals
	* StepId: 11
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_event_tanWin2023_Academy_GAMA_11
		* h_event_tanWin2023_Academy_GAMA_14
		* h_event_tanWin2023_Academy_GAMA_17
		* h_event_tanWin2023_Academy_GAMA_18
		* h_event_tanWin2023_Academy_GAMA_23
		* h_event_tanWin2023_Academy_d_combat

## h_event_tanWin2023_Academy_i_jochikChecks
	* StepId: 24
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: h_event_tanWin2023_Academy_GAMA_24

## h_event_tanWin2023_Academy_i_setup
	* StepId: 1
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_event_tanWin2023_Academy_deactivate_everythingWarmUp
		* h_event_tanWin2023_Academy_invincivle_JochikA
		* h_event_tanWin2023_Academy_spawn_chicuat
		* h_event_tanWin2023_Academy_spawn_tecuban
		* h_event_tanWin2023_Academy_spawn_vaygr

## h_event_tanWin2023_Academy_killCheck_academy
	* StepId: 21
	* Type: Trigger
	* TargetType: AllUnitsWithTagsAreKilled
	* SuccLL: 
		* h_event_tanWin2023_Academy_GAMA_21
		* h_event_tanWin2023_Academy_deactivate_defendAcademy

## h_event_tanWin2023_Academy_killCheck_tepin
	* StepId: 34
	* Type: Trigger
	* TargetType: AllUnitsWithTagsAreKilled
	* SuccLL: 
		* h_event_tanWin2023_Academy_GAMA_34
		* h_event_tanWin2023_Academy_deactivate_defendTepin

## h_event_tanWin2023_Academy_multi_failAny
	* StepId: 12
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* h_event_tanWin2023_Academy_killCheck_academy
		* h_event_tanWin2023_Academy_killCheck_tepin
	* SuccLL: 
		* h_event_tanWin2023_Academy_GAMA_12
		* h_event_tanWin2023_Academy_GAMA_13

## h_event_tanWin2023_Academy_multi_failDialog
	* StepId: 13
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* h_event_tanWin2023_Academy_td_failAcademy
		* h_event_tanWin2023_Academy_td_failTepin
		* h_event_tanWin2023_Academy_w_forceFail
	* SuccLL: h_event_tanWin2023_Academy_fail

## h_event_tanWin2023_Academy_start
	* StepId: 0
	* Type: Trigger
	* TargetType: MissionStart
	* SuccLL: 
		* h_event_tanWin2023_Academy_GAMA_0
		* h_event_tanWin2023_Academy_GAMA_1
		* h_event_tanWin2023_Academy_GAMA_2

## h_event_tanWin2023_Academy_strengthCheck_reinforcementsA
	* StepId: 28
	* Type: Trigger
	* TargetType: TaggedUnitsBelowStrength
	* SuccLL: 
		* h_event_tanWin2023_Academy_GAMA_28
		* h_event_tanWin2023_Academy_camera_tepin
		* h_event_tanWin2023_Academy_invincible_chicuatB
		* h_event_tanWin2023_Academy_invincible_player1
		* h_event_tanWin2023_Academy_invincible_player2
		* h_event_tanWin2023_Academy_invincible_player3
		* h_event_tanWin2023_Academy_invincible_tecubanB
		* h_event_tanWin2023_Academy_invincible_vaygrB

## h_event_tanWin2023_Academy_strengthCheck_reinforcementsB
	* StepId: 37
	* Type: Trigger
	* TargetType: TaggedUnitsBelowStrength
	* SuccLL: 
		* h_event_tanWin2023_Academy_GAMA_37
		* h_event_tanWin2023_Academy_GAMA_38
		* h_event_tanWin2023_Academy_invincible_JochikB
		* h_event_tanWin2023_Academy_npcAI_followFlagship
		* h_event_tanWin2023_Academy_spawn_JochikB

## h_event_tanWin2023_Academy_td_failAcademy
	* StepId: 23
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: 6

## h_event_tanWin2023_Academy_td_failTepin
	* StepId: 36
	* Type: Trigger
	* TargetType: OnDialogFinishedIndex

## h_event_tanWin2023_Academy_td_fin
	* StepId: 17
	* Type: Trigger
	* TargetType: OnDialogFinishedIndex
	* SuccLL: h_event_tanWin2023_Academy_fin

## h_event_tanWin2023_Academy_td_intro
	* StepId: 5
	* Type: Trigger
	* TargetType: OnDialogFinishedIndex
	* SuccLL: h_event_tanWin2023_Academy_GAMA_5

## h_event_tanWin2023_Academy_w_activateTepin
	* StepId: 32
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_event_tanWin2023_Academy_activate_tepin

## h_event_tanWin2023_Academy_w_cameraHiigarans
	* StepId: 10
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_tanWin2023_Academy_GAMA_10
		* h_event_tanWin2023_Academy_GAMA_42

## h_event_tanWin2023_Academy_w_cameraKill
	* StepId: 8
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_tanWin2023_Academy_GAMA_8
		* h_event_tanWin2023_Academy_d_situation

## h_event_tanWin2023_Academy_w_cameraPhaseIn
	* StepId: 7
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_tanWin2023_Academy_GAMA_43
		* h_event_tanWin2023_Academy_GAMA_7
		* h_event_tanWin2023_Academy_d_heyoka

## h_event_tanWin2023_Academy_w_cameraSituation
	* StepId: 9
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_tanWin2023_Academy_GAMA_9
		* h_event_tanWin2023_Academy_d_hiigarans

## h_event_tanWin2023_Academy_w_cameraTepin1
	* StepId: 29
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_tanWin2023_Academy_GAMA_29
		* h_event_tanWin2023_Academy_GAMA_32
		* h_event_tanWin2023_Academy_GAMA_33
		* h_event_tanWin2023_Academy_deactivate_tepin
		* h_event_tanWin2023_Academy_spawn_Tepin

## h_event_tanWin2023_Academy_w_cameraTepin2
	* StepId: 30
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_tanWin2023_Academy_GAMA_30
		* h_event_tanWin2023_Academy_GAMA_31
		* h_event_tanWin2023_Academy_d_tepin

## h_event_tanWin2023_Academy_w_cameraTepin3
	* StepId: 31
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_tanWin2023_Academy_vincible_chicuatB
		* h_event_tanWin2023_Academy_vincible_player1
		* h_event_tanWin2023_Academy_vincible_player2
		* h_event_tanWin2023_Academy_vincible_player3
		* h_event_tanWin2023_Academy_vincible_tecubanB
		* h_event_tanWin2023_Academy_vincible_vaygrB

## h_event_tanWin2023_Academy_w_cinematicStart
	* StepId: 6
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_tanWin2023_Academy_GAMA_6
		* h_event_tanWin2023_Academy_camera_jochik
		* h_event_tanWin2023_Academy_close_jochik
		* h_event_tanWin2023_Academy_invincible_chicuat
		* h_event_tanWin2023_Academy_invincible_tecuban
		* h_event_tanWin2023_Academy_invincible_vaygr

## h_event_tanWin2023_Academy_w_failAcademy
	* StepId: 22
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_tanWin2023_Academy_GAMA_22
		* h_event_tanWin2023_Academy_d_failAcademy

## h_event_tanWin2023_Academy_w_failTepin
	* StepId: 35
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_tanWin2023_Academy_GAMA_35
		* h_event_tanWin2023_Academy_d_failTepin

## h_event_tanWin2023_Academy_w_forceFail
	* StepId: 14
	* Type: Trigger
	* TargetType: WaitForTime

## h_event_tanWin2023_Academy_w_heyokaKill
	* StepId: 45
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_tanWin2023_Academy_activate_Tecuban
		* h_event_tanWin2023_Academy_activate_VaygrCenter

## h_event_tanWin2023_Academy_w_heyokaShot
	* StepId: 44
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_tanWin2023_Academy_GAMA_44
		* h_event_tanWin2023_Academy_activate_HeyokaTarget
		* h_event_tanWin2023_Academy_activate_Jochik
		* h_event_tanWin2023_Academy_preferredTarget_Jochiik

## h_event_tanWin2023_Academy_w_intro1
	* StepId: 3
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_tanWin2023_Academy_GAMA_3
		* h_event_tanWin2023_Academy_deactivate_everything2
		* h_event_tanWin2023_Academy_lookAt_relic

## h_event_tanWin2023_Academy_w_intro2
	* StepId: 4
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_tanWin2023_Academy_GAMA_4
		* h_event_tanWin2023_Academy_d_intro
		* h_event_tanWin2023_Academy_deactivate_everything3

## h_event_tanWin2023_Academy_w_JochikDownA1
	* StepId: 26
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_tanWin2023_Academy_GAMA_26
		* h_event_tanWin2023_Academy_remove_JochikA

## h_event_tanWin2023_Academy_w_JochikDownA2
	* StepId: 27
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_tanWin2023_Academy_GAMA_27
		* h_event_tanWin2023_Academy_GAMA_36
		* h_event_tanWin2023_Academy_spawn_reinforcements

## h_event_tanWin2023_Academy_w_jochikDownB1
	* StepId: 40
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_tanWin2023_Academy_GAMA_40
		* h_event_tanWin2023_Academy_remove_JochikB

## h_event_tanWin2023_Academy_w_jochikDownB2
	* StepId: 41
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_tanWin2023_Academy_GAMA_41
		* h_event_tanWin2023_Academy_remove_vaygr

## h_event_tanWin2023_Academy_w_JochikReturn
	* StepId: 38
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_event_tanWin2023_Academy_d_JochikReturn

## h_event_tanWin2023_Academy_w_unitWakeUp
	* StepId: 2
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_event_tanWin2023_Academy_deactivate_everything1

## h_event_tanWin2023_Academy_w_win
	* StepId: 16
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_tanWin2023_Academy_GAMA_16
		* h_event_tanWin2023_Academy_d_win

## h_event_tanWin2023_AttackBase_check_vaygr
	* StepId: 17
	* Type: Trigger
	* TargetType: TaggedUnitsBelowStrength
	* SuccLL: h_event_tanWin2023_AttackBase_d_vaygr

## h_event_tanWin2023_AttackBase_firstAttackCheck
	* StepId: 8
	* Type: Trigger
	* TargetType: OnPlayerAttackNPC
	* SuccLL: 
		* h_event_tanWin2023_AttackBase_GAMA_8
		* h_event_tanWin2023_AttackBase_GAMA_9

## h_event_tanWin2023_AttackBase_goal_defeatBase
	* StepId: 2
	* Type: Goal
	* TargetType: FinishGoalsString
	* TVS: h_event_tanWin2023_AttackBase_multi_defeatBase
	* SuccLL: h_event_tanWin2023_AttackBase_GAMA_2

## h_event_tanWin2023_AttackBase_i_goals
	* StepId: 1
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_event_tanWin2023_AttackBase_GAMA_1
		* h_event_tanWin2023_AttackBase_GAMA_4
		* h_event_tanWin2023_AttackBase_GAMA_5
		* h_event_tanWin2023_AttackBase_GAMA_6

## h_event_tanWin2023_AttackBase_kill_all
	* StepId: 7
	* Type: Trigger
	* TargetType: WaveFinished

## h_event_tanWin2023_AttackBase_kill_vaygr
	* StepId: 6
	* Type: Trigger
	* TargetType: KillSpecificWave

## h_event_tanWin2023_AttackBase_multi_alert
	* StepId: 9
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* h_event_tanWin2023_AttackBase_strengthCheckPatrol
		* h_event_tanWin2023_AttackBase_strengthCheckWave
		* h_event_tanWin2023_AttackBase_w_alert
	* SuccLL: 
		* h_event_tanWin2023_AttackBase_behavior_alert
		* h_event_tanWin2023_AttackBase_d_alert

## h_event_tanWin2023_AttackBase_multi_defeatBase
	* StepId: 5
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* h_event_tanWin2023_AttackBase_kill_all
		* h_event_tanWin2023_AttackBase_kill_vaygr

## h_event_tanWin2023_AttackBase_start
	* StepId: 0
	* Type: Trigger
	* TargetType: MissionStart
	* SuccLL: 
		* h_event_tanWin2023_AttackBase_GAMA_0
		* h_event_tanWin2023_AttackBase_GAMA_10
		* h_event_tanWin2023_AttackBase_GAMA_18
		* h_event_tanWin2023_AttackBase_GAMA_19
		* h_event_tanWin2023_AttackBase_GAMA_7
		* h_event_tanWin2023_AttackBase_invincible_station1
		* h_event_tanWin2023_AttackBase_wave0_station

## h_event_tanWin2023_AttackBase_strengthCheck_patrols
	* StepId: 18
	* Type: Trigger
	* TargetType: TaggedUnitsBelowStrength

## h_event_tanWin2023_AttackBase_strengthCheck_station
	* StepId: 12
	* Type: Trigger
	* TargetType: TaggedUnitsBelowStrength
	* SuccLL: 
		* h_event_tanWin2023_AttackBase_GAMA_12
		* h_event_tanWin2023_AttackBase_GAMA_13
		* h_event_tanWin2023_AttackBase_invincible_station2
		* h_event_tanWin2023_AttackBase_wave0_wave

## h_event_tanWin2023_AttackBase_strengthCheck_wave
	* StepId: 14
	* Type: Trigger
	* TargetType: TaggedUnitsBelowStrength
	* SuccLL: h_event_tanWin2023_AttackBase_GAMA_14

## h_event_tanWin2023_AttackBase_td_win
	* StepId: 4
	* Type: Trigger
	* TargetType: OnDialogFinishedIndex
	* SuccLL: h_event_tanWin2023_AttackBase_fin

## h_event_tanWin2023_AttackBase_w_alert
	* StepId: 10
	* Type: Trigger
	* TargetType: WaitForTime

## h_event_tanWin2023_AttackBase_w_strengthChecks
	* StepId: 11
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_tanWin2023_AttackBase_GAMA_11
		* h_event_tanWin2023_AttackBase_GAMA_17

## h_event_tanWin2023_AttackBase_w_vaygr
	* StepId: 15
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_tanWin2023_AttackBase_GAMA_15
		* h_event_tanWin2023_AttackBase_GAMA_16
		* h_event_tanWin2023_AttackBase_wave_vaygr

## h_event_tanWin2023_AttackBase_w_vaygrDialog
	* StepId: 16
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_event_tanWin2023_AttackBase_d_boss

## h_event_tanWin2023_AttackBase_w_wave
	* StepId: 13
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_event_tanWin2023_AttackBase_d_wave

## h_event_tanWin2023_AttackBase_wait_win
	* StepId: 3
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_tanWin2023_AttackBase_GAMA_3
		* h_event_tanWin2023_AttackBase_d_win1

## h_event_tanWin2023_AttackBase_wait1
	* StepId: 20
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_event_tanWin2023_AttackBase_d_intro1

## h_event_tanWin2023_AttackBase_wait7
	* StepId: 19
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_event_tanWin2023_AttackBase_lookAt

## h_event_tanWin2023_DefendBase_goal_defendStation
	* StepId: 10
	* Type: Goal
	* TargetType: WaveFinished
	* SuccLL: h_event_tanWin2023_DefendBase_GAMA_10

## h_event_tanWin2023_DefendBase_i_goals
	* StepId: 9
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_event_tanWin2023_DefendBase_GAMA_12
		* h_event_tanWin2023_DefendBase_GAMA_13
		* h_event_tanWin2023_DefendBase_GAMA_9

## h_event_tanWin2023_DefendBase_i_intro
	* StepId: 19
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_event_tanWin2023_DefendBase_GAMA_19
		* h_event_tanWin2023_DefendBase_GAMA_20

## h_event_tanWin2023_DefendBase_i_setup
	* StepId: 8
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_event_tanWin2023_DefendBase_ally_patrolA
		* h_event_tanWin2023_DefendBase_ally_patrolB
		* h_event_tanWin2023_DefendBase_ally_patrolC
		* h_event_tanWin2023_DefendBase_ally_platformA
		* h_event_tanWin2023_DefendBase_ally_platformB
		* h_event_tanWin2023_DefendBase_ally_platformC
		* h_event_tanWin2023_DefendBase_ally_platformD
		* h_event_tanWin2023_DefendBase_ally_platformE
		* h_event_tanWin2023_DefendBase_ally_platformF
		* h_event_tanWin2023_DefendBase_ally_spawner
		* h_event_tanWin2023_DefendBase_ally_station

## h_event_tanWin2023_DefendBase_kill_station
	* StepId: 14
	* Type: Trigger
	* TargetType: KillSpecificWave
	* SuccLL: 
		* h_event_tanWin2023_DefendBase_GAMA_14
		* h_event_tanWin2023_DefendBase_deactivate_defendStation

## h_event_tanWin2023_DefendBase_multi_attack
	* StepId: 1
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: h_event_tanWin2023_DefendBase_td_intro
	* SuccLL: h_event_tanWin2023_DefendBase_GAMA_1

## h_event_tanWin2023_DefendBase_multi_fail
	* StepId: 16
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* h_event_tanWin2023_DefendBase_td_fail
		* h_event_tanWin2023_DefendBase_w_dFail
	* SuccLL: h_event_tanWin2023_DefendBase_fail

## h_event_tanWin2023_DefendBase_start
	* StepId: 0
	* Type: Trigger
	* TargetType: MissionStart
	* SuccLL: 
		* h_event_tanWin2023_DefendBase_GAMA_0
		* h_event_tanWin2023_DefendBase_GAMA_18
		* h_event_tanWin2023_DefendBase_GAMA_7
		* h_event_tanWin2023_DefendBase_GAMA_8

## h_event_tanWin2023_DefendBase_strength_station
	* StepId: 13
	* Type: Trigger
	* TargetType: TaggedUnitsBelowStrength
	* SuccLL: h_event_tanWin2023_DefendBase_d_stationLow

## h_event_tanWin2023_DefendBase_strength_wave0
	* StepId: 4
	* Type: Trigger
	* TargetType: TaggedUnitsBelowStrength
	* SuccLL: 
		* h_event_tanWin2023_DefendBase_GAMA_4
		* h_event_tanWin2023_DefendBase_GAMA_5
		* h_event_tanWin2023_DefendBase_wave_2

## h_event_tanWin2023_DefendBase_strength_wave2
	* StepId: 6
	* Type: Trigger
	* TargetType: TaggedUnitsBelowStrength
	* SuccLL: 
		* h_event_tanWin2023_DefendBase_GAMA_6
		* h_event_tanWin2023_DefendBase_wave_4

## h_event_tanWin2023_DefendBase_td_fail
	* StepId: 18
	* Type: Trigger
	* TargetType: OnDialogFinishedIndex

## h_event_tanWin2023_DefendBase_td_intro
	* StepId: 22
	* Type: Trigger
	* TargetType: OnDialogFinishedIndex

## h_event_tanWin2023_DefendBase_td_win
	* StepId: 12
	* Type: Trigger
	* TargetType: OnDialogFinishedIndex
	* SuccLL: h_event_tanWin2023_DefendBase_win

## h_event_tanWin2023_DefendBase_w_attack1
	* StepId: 2
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_tanWin2023_DefendBase_GAMA_2
		* h_event_tanWin2023_DefendBase_GAMA_3
		* h_event_tanWin2023_DefendBase_wave_0

## h_event_tanWin2023_DefendBase_w_attack2
	* StepId: 3
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_event_tanWin2023_DefendBase_d_firstWave

## h_event_tanWin2023_DefendBase_w_dFail
	* StepId: 17
	* Type: Trigger
	* TargetType: WaitForTime

## h_event_tanWin2023_DefendBase_w_fail
	* StepId: 15
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_tanWin2023_DefendBase_GAMA_15
		* h_event_tanWin2023_DefendBase_GAMA_16
		* h_event_tanWin2023_DefendBase_GAMA_17
		* h_event_tanWin2023_DefendBase_d_fail

## h_event_tanWin2023_DefendBase_w_intro
	* StepId: 21
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_tanWin2023_DefendBase_GAMA_21
		* h_event_tanWin2023_DefendBase_d_intro

## h_event_tanWin2023_DefendBase_w_lookAt
	* StepId: 20
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_event_tanWin2023_DefendBase_lookAt_intro

## h_event_tanWin2023_DefendBase_w_nextWave1
	* StepId: 5
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_event_tanWin2023_DefendBase_d_nextWave1

## h_event_tanWin2023_DefendBase_w_nextWave4
	* StepId: 7
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_event_tanWin2023_DefendBase_d_nextWave2

## h_event_tanWin2023_DefendBase_w_win
	* StepId: 11
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_tanWin2023_DefendBase_GAMA_11
		* h_event_tanWin2023_DefendBase_d_win

## h_event_tanWin2023_Relic_79205f7ad64e99942b91beafc0796af4
	* StepId: 12
	* Type: Trigger
	* TargetType: TaggedUnitsBelowStrength
	* SuccLL: h_event_tanWin2023_Relic_d_bossLow

## h_event_tanWin2023_Relic_attackNPC_intro
	* StepId: 4
	* Type: Trigger
	* TargetType: OnPlayerAttackNPC
	* SuccLL: h_event_tanWin2023_Relic_GAMA_4

## h_event_tanWin2023_Relic_goal_killVaygr
	* StepId: 1
	* Type: Goal
	* TargetType: WaveFinished
	* SuccLL: h_event_tanWin2023_Relic_GAMA_1

## h_event_tanWin2023_Relic_i_spawning
	* StepId: 6
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_event_tanWin2023_Relic_GAMA_6
		* h_event_tanWin2023_Relic_interactable_relic
		* h_event_tanWin2023_Relic_prop_ship
		* h_event_tanWin2023_Relic_spawn_patrol

## h_event_tanWin2023_Relic_start
	* StepId: 0
	* Type: Trigger
	* TargetType: MissionStart
	* SuccLL: 
		* h_event_tanWin2023_Relic_GAMA_0
		* h_event_tanWin2023_Relic_GAMA_12
		* h_event_tanWin2023_Relic_GAMA_3
		* h_event_tanWin2023_Relic_GAMA_5

## h_event_tanWin2023_Relic_strength_patrol
	* StepId: 7
	* Type: Trigger
	* TargetType: TaggedUnitsBelowStrength
	* SuccLL: 
		* h_event_tanWin2023_Relic_GAMA_7
		* h_event_tanWin2023_Relic_GAMA_8
		* h_event_tanWin2023_Relic_aiBehavior
		* h_event_tanWin2023_Relic_spawn_wave

## h_event_tanWin2023_Relic_strength_wave
	* StepId: 9
	* Type: Trigger
	* TargetType: TaggedUnitsBelowStrength
	* SuccLL: 
		* h_event_tanWin2023_Relic_GAMA_10
		* h_event_tanWin2023_Relic_GAMA_11
		* h_event_tanWin2023_Relic_GAMA_9
		* h_event_tanWin2023_Relic_spawn_boss

## h_event_tanWin2023_Relic_td_fin
	* StepId: 3
	* Type: Trigger
	* TargetType: OnDialogFinishedIndex
	* SuccLL: h_event_tanWin2023_Relic_fin

## h_event_tanWin2023_Relic_w_attackNPC
	* StepId: 5
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_event_tanWin2023_Relic_d_contact

## h_event_tanWin2023_Relic_w_boss
	* StepId: 11
	* Type: Trigger
	* TargetType: TaggedUnitsBelowStrength
	* SuccLL: h_event_tanWin2023_Relic_d_boss

## h_event_tanWin2023_Relic_w_intro1
	* StepId: 13
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_tanWin2023_Relic_GAMA_13
		* h_event_tanWin2023_Relic_lookAt_relic

## h_event_tanWin2023_Relic_w_intro2
	* StepId: 14
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_event_tanWin2023_Relic_d_intro

## h_event_tanWin2023_Relic_w_wave
	* StepId: 8
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_event_tanWin2023_Relic_d_wave

## h_event_tanWin2023_Relic_w_waveB
	* StepId: 10
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_event_tanWin2023_Relic_d_waveB

## h_event_tanWin2023_Relic_w_win
	* StepId: 2
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_tanWin2023_Relic_GAMA_2
		* h_event_tanWin2023_Relic_d_win

## h_event_yaoSpr2024_Conjunction_exist_piratesEnd
	* StepId: 54
	* Type: Trigger
	* TargetType: UnitWithTagsExists
	* SuccLL: h_event_yaoSpr2024_Conjunction_GAMA_54
	* FailLL: h_event_yaoSpr2024_Conjunction_GAMA_55

## h_event_yaoSpr2024_Conjunction_exist_piratesNotCatequil
	* StepId: 70
	* Type: Trigger
	* TargetType: UnitWithTagsExists
	* SuccLL: h_event_yaoSpr2024_Conjunction_preferredTarget_chocoanRepeating
	* FailLL: h_event_yaoSpr2024_Conjunction_move_chocoanIdle

## h_event_yaoSpr2024_Conjunction_exist_piratesNotCatequil2
	* StepId: 60
	* Type: Trigger
	* TargetType: UnitWithTagsExists
	* SuccLL: h_event_yaoSpr2024_Conjunction_preferredTarget_chocoanRepeating2
	* FailLL: h_event_yaoSpr2024_Conjunction_preferredTarget_chocoanCatequil

## h_event_yaoSpr2024_Conjunction_goal_reach
	* StepId: 6
	* Type: Goal
	* TargetType: ReachPointOfInterest

## h_event_yaoSpr2024_Conjunction_goal_survive
	* StepId: 7
	* Type: Goal
	* TargetType: FinishGoalsString

## h_event_yaoSpr2024_Conjunction_healthCheck_catequil
	* StepId: 40
	* Type: Trigger
	* TargetType: TaggedUnitsBelowHealthAndArmor
	* SuccLL: 
		* h_event_yaoSpr2024_Conjunction_GAMA_40
		* h_event_yaoSpr2024_Conjunction_GAMA_56
		* h_event_yaoSpr2024_Conjunction_d_catequilLow

## h_event_yaoSpr2024_Conjunction_i_attackA
	* StepId: 74
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_event_yaoSpr2024_Conjunction_GAMA_74
		* h_event_yaoSpr2024_Conjunction_spawn_waveAMid
		* h_event_yaoSpr2024_Conjunction_spawn_waveAPoint

## h_event_yaoSpr2024_Conjunction_i_attackB
	* StepId: 72
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_event_yaoSpr2024_Conjunction_GAMA_72
		* h_event_yaoSpr2024_Conjunction_spawn_waveBBack
		* h_event_yaoSpr2024_Conjunction_spawn_waveBMid
		* h_event_yaoSpr2024_Conjunction_spawn_waveBPoint

## h_event_yaoSpr2024_Conjunction_i_attackC
	* StepId: 66
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_event_yaoSpr2024_Conjunction_GAMA_66
		* h_event_yaoSpr2024_Conjunction_spawn_waveCBack
		* h_event_yaoSpr2024_Conjunction_spawn_waveCMid
		* h_event_yaoSpr2024_Conjunction_spawn_waveCPoint

## h_event_yaoSpr2024_Conjunction_i_catequil
	* StepId: 36
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_event_yaoSpr2024_Conjunction_GAMA_36
		* h_event_yaoSpr2024_Conjunction_GAMA_64
		* h_event_yaoSpr2024_Conjunction_c989a99cd4c195b4788daa78ccc770df
		* h_event_yaoSpr2024_Conjunction_camera_catequil
		* h_event_yaoSpr2024_Conjunction_close_catequil
		* h_event_yaoSpr2024_Conjunction_deactivate_chocoanCatequil

## h_event_yaoSpr2024_Conjunction_i_chocoanChange
	* StepId: 68
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_event_yaoSpr2024_Conjunction_GAMA_68
		* h_event_yaoSpr2024_Conjunction_GAMA_70
		* h_event_yaoSpr2024_Conjunction_activate_chocoanChange
		* h_event_yaoSpr2024_Conjunction_d_change
		* h_event_yaoSpr2024_Conjunction_preferredTarget_chocoan

## h_event_yaoSpr2024_Conjunction_i_chocoanEnd
	* StepId: 52
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_event_yaoSpr2024_Conjunction_GAMA_52
		* h_event_yaoSpr2024_Conjunction_deactivate_preferredTargetRepeating
		* h_event_yaoSpr2024_Conjunction_move_chocoan1

## h_event_yaoSpr2024_Conjunction_i_combatEnd
	* StepId: 56
	* Type: Trigger
	* TargetType: Immediate

## h_event_yaoSpr2024_Conjunction_i_end
	* StepId: 43
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_event_yaoSpr2024_Conjunction_GAMA_43
		* h_event_yaoSpr2024_Conjunction_GAMA_49
		* h_event_yaoSpr2024_Conjunction_GAMA_50
		* h_event_yaoSpr2024_Conjunction_GAMA_51
		* h_event_yaoSpr2024_Conjunction_succeed_goalSurvive

## h_event_yaoSpr2024_Conjunction_i_gameplay
	* StepId: 19
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_event_yaoSpr2024_Conjunction_GAMA_19
		* h_event_yaoSpr2024_Conjunction_activate_pilgrimPoint

## h_event_yaoSpr2024_Conjunction_i_goals
	* StepId: 5
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_event_yaoSpr2024_Conjunction_GAMA_5
		* h_event_yaoSpr2024_Conjunction_GAMA_6
		* h_event_yaoSpr2024_Conjunction_GAMA_7

## h_event_yaoSpr2024_Conjunction_i_invincibleCatequil
	* StepId: 65
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_event_yaoSpr2024_Conjunction_invincible_player1
		* h_event_yaoSpr2024_Conjunction_invincible_player2
		* h_event_yaoSpr2024_Conjunction_invincible_player3
		* h_event_yaoSpr2024_Conjunction_invincible_player4
		* h_event_yaoSpr2024_Conjunction_invincible_player5
		* h_event_yaoSpr2024_Conjunction_invincible_player6
		* h_event_yaoSpr2024_Conjunction_invincible_player7
		* h_event_yaoSpr2024_Conjunction_los_offCatequil

## h_event_yaoSpr2024_Conjunction_i_preferredTargets
	* StepId: 76
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_event_yaoSpr2024_Conjunction_preferredTarget_back
		* h_event_yaoSpr2024_Conjunction_preferredTarget_mid
		* h_event_yaoSpr2024_Conjunction_preferredTarget_point

## h_event_yaoSpr2024_Conjunction_i_reachGoals
	* StepId: 13
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_event_yaoSpr2024_Conjunction_GAMA_13
		* h_event_yaoSpr2024_Conjunction_GAMA_14
		* h_event_yaoSpr2024_Conjunction_GAMA_15
		* h_event_yaoSpr2024_Conjunction_GAMA_16
		* h_event_yaoSpr2024_Conjunction_GAMA_17

## h_event_yaoSpr2024_Conjunction_i_setup
	* StepId: 1
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_event_yaoSpr2024_Conjunction_deactivate_chocoanSpawn
		* h_event_yaoSpr2024_Conjunction_deactivate_pilgrimsSpawn
		* h_event_yaoSpr2024_Conjunction_spawn_chocoan
		* h_event_yaoSpr2024_Conjunction_spawn_pilgrimElders
		* h_event_yaoSpr2024_Conjunction_spawn_pilgrimMid
		* h_event_yaoSpr2024_Conjunction_spawn_pilgrimPoint

## h_event_yaoSpr2024_Conjunction_i_vincibleCatequil
	* StepId: 61
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_event_yaoSpr2024_Conjunction_vincible_player1
		* h_event_yaoSpr2024_Conjunction_vincible_player2
		* h_event_yaoSpr2024_Conjunction_vincible_player3
		* h_event_yaoSpr2024_Conjunction_vincible_player4
		* h_event_yaoSpr2024_Conjunction_vincible_player5
		* h_event_yaoSpr2024_Conjunction_vincible_player6
		* h_event_yaoSpr2024_Conjunction_vincible_player7

## h_event_yaoSpr2024_Conjunction_kill_remaining
	* StepId: 55
	* Type: Trigger
	* TargetType: AllUnitsWithTagsAreKilled

## h_event_yaoSpr2024_Conjunction_killUnit_pilgrim
	* StepId: 8
	* Type: Trigger
	* TargetType: OnTaggedUnitKilled
	* SuccLL: 
		* h_event_yaoSpr2024_Conjunction_GAMA_10
		* h_event_yaoSpr2024_Conjunction_GAMA_8
		* h_event_yaoSpr2024_Conjunction_GAMA_9
		* h_event_yaoSpr2024_Conjunction_deactivate_goalSurvive

## h_event_yaoSpr2024_Conjunction_multi_combatEnd
	* StepId: 42
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* h_event_yaoSpr2024_Conjunction_i_combatEnd
		* h_event_yaoSpr2024_Conjunction_kill_remaining
	* SuccLL: h_event_yaoSpr2024_Conjunction_GAMA_42

## h_event_yaoSpr2024_Conjunction_multi_end
	* StepId: 44
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* h_event_yaoSpr2024_Conjunction_reach_chocoanEnd
		* h_event_yaoSpr2024_Conjunction_td_win
	* SuccLL: h_event_yaoSpr2024_Conjunction_GAMA_44

## h_event_yaoSpr2024_Conjunction_multi_fail
	* StepId: 9
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* h_event_yaoSpr2024_Conjunction_td_fail
		* h_event_yaoSpr2024_Conjunction_wait_fail
	* SuccLL: h_event_yaoSpr2024_Conjunction_fail

## h_event_yaoSpr2024_Conjunction_reach_back
	* StepId: 16
	* Type: Trigger
	* TargetType: ReachPointOfInterest
	* SuccLL: 
		* h_event_yaoSpr2024_Conjunction_deactivate_pilgrimBack
		* h_event_yaoSpr2024_Conjunction_succeed_goalReach

## h_event_yaoSpr2024_Conjunction_reach_chocoan
	* StepId: 18
	* Type: Trigger
	* TargetType: ReachPointOfInterest
	* SuccLL: 
		* h_event_yaoSpr2024_Conjunction_deactivate_chocoan
		* h_event_yaoSpr2024_Conjunction_deactivate_chocoanStutter

## h_event_yaoSpr2024_Conjunction_reach_chocoanEnd
	* StepId: 53
	* Type: Trigger
	* TargetType: ReachPointOfInterest
	* SuccLL: h_event_yaoSpr2024_Conjunction_deactivate_chocoanEnd

## h_event_yaoSpr2024_Conjunction_reach_elders
	* StepId: 17
	* Type: Trigger
	* TargetType: ReachPointOfInterest
	* SuccLL: h_event_yaoSpr2024_Conjunction_deactivate_pilgrimElders

## h_event_yaoSpr2024_Conjunction_reach_mid
	* StepId: 15
	* Type: Trigger
	* TargetType: ReachPointOfInterest
	* SuccLL: h_event_yaoSpr2024_Conjunction_deactivate_pilgrimMid

## h_event_yaoSpr2024_Conjunction_reach_point
	* StepId: 14
	* Type: Trigger
	* TargetType: ReachPointOfInterest
	* SuccLL: h_event_yaoSpr2024_Conjunction_deactivate_pilgrimPoint

## h_event_yaoSpr2024_Conjunction_start
	* StepId: 0
	* Type: Trigger
	* TargetType: MissionStart
	* SuccLL: 
		* h_event_yaoSpr2024_Conjunction_GAMA_0
		* h_event_yaoSpr2024_Conjunction_GAMA_1
		* h_event_yaoSpr2024_Conjunction_GAMA_2

## h_event_yaoSpr2024_Conjunction_td_end
	* StepId: 49
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: e_yaoSpr2024_Conjunction_end
	* SuccLL: h_event_yaoSpr2024_Conjunction_fin

## h_event_yaoSpr2024_Conjunction_td_fail
	* StepId: 10
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: e_yaoSpr2024_Conjunction_fail

## h_event_yaoSpr2024_Conjunction_td_intro
	* StepId: 4
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: e_yaoSpr2024_Conjunction_intro
	* SuccLL: 
		* h_event_yaoSpr2024_Conjunction_GAMA_12
		* h_event_yaoSpr2024_Conjunction_GAMA_18
		* h_event_yaoSpr2024_Conjunction_GAMA_4

## h_event_yaoSpr2024_Conjunction_td_win
	* StepId: 50
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: e_yaoSpr2024_Conjunction_win

## h_event_yaoSpr2024_Conjunction_w_activateBack
	* StepId: 23
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_event_yaoSpr2024_Conjunction_activate_pilgrimBack

## h_event_yaoSpr2024_Conjunction_w_activateCatequil
	* StepId: 62
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_event_yaoSpr2024_Conjunction_activate_catequil

## h_event_yaoSpr2024_Conjunction_w_activateCatequilFleet
	* StepId: 64
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_event_yaoSpr2024_Conjunction_activate_catequilFleet

## h_event_yaoSpr2024_Conjunction_w_activateChocoan
	* StepId: 25
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_yaoSpr2024_Conjunction_GAMA_25
		* h_event_yaoSpr2024_Conjunction_GAMA_27
		* h_event_yaoSpr2024_Conjunction_GAMA_28
		* h_event_yaoSpr2024_Conjunction_activate_chocoan

## h_event_yaoSpr2024_Conjunction_w_activateChocoanRepeating
	* StepId: 26
	* Type: TriggerRepeating
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_yaoSpr2024_Conjunction_GAMA_26
		* h_event_yaoSpr2024_Conjunction_deactivate_chocoanRepeating

## h_event_yaoSpr2024_Conjunction_w_activateElders
	* StepId: 20
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_yaoSpr2024_Conjunction_GAMA_20
		* h_event_yaoSpr2024_Conjunction_GAMA_24
		* h_event_yaoSpr2024_Conjunction_activate_pilgrimElders

## h_event_yaoSpr2024_Conjunction_w_activateMid
	* StepId: 21
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_yaoSpr2024_Conjunction_GAMA_21
		* h_event_yaoSpr2024_Conjunction_activate_pilgrimMid

## h_event_yaoSpr2024_Conjunction_w_arrivalDialog
	* StepId: 24
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_event_yaoSpr2024_Conjunction_d_arrival

## h_event_yaoSpr2024_Conjunction_w_catequil1
	* StepId: 37
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_yaoSpr2024_Conjunction_GAMA_37
		* h_event_yaoSpr2024_Conjunction_GAMA_62
		* h_event_yaoSpr2024_Conjunction_deactivate_catequil
		* h_event_yaoSpr2024_Conjunction_invincible_catequil
		* h_event_yaoSpr2024_Conjunction_spawn_catequil

## h_event_yaoSpr2024_Conjunction_w_catequil2
	* StepId: 38
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_yaoSpr2024_Conjunction_GAMA_38
		* h_event_yaoSpr2024_Conjunction_GAMA_61
		* h_event_yaoSpr2024_Conjunction_d_attackC

## h_event_yaoSpr2024_Conjunction_w_catequil3
	* StepId: 39
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_yaoSpr2024_Conjunction_GAMA_39
		* h_event_yaoSpr2024_Conjunction_GAMA_57
		* h_event_yaoSpr2024_Conjunction_GAMA_60
		* h_event_yaoSpr2024_Conjunction_los_onCatequil

## h_event_yaoSpr2024_Conjunction_w_catequilFleet
	* StepId: 63
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_yaoSpr2024_Conjunction_GAMA_63
		* h_event_yaoSpr2024_Conjunction_deactivate_catequilFleet
		* h_event_yaoSpr2024_Conjunction_spawn_catequilFleet

## h_event_yaoSpr2024_Conjunction_w_catequilLow
	* StepId: 41
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_yaoSpr2024_Conjunction_GAMA_41
		* h_event_yaoSpr2024_Conjunction_GAMA_53

## h_event_yaoSpr2024_Conjunction_w_catequilLowDialog
	* StepId: 57
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_event_yaoSpr2024_Conjunction_remove_catequil

## h_event_yaoSpr2024_Conjunction_w_chocoanCatequil
	* StepId: 58
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_yaoSpr2024_Conjunction_GAMA_58
		* h_event_yaoSpr2024_Conjunction_activate_chocoanCatequil

## h_event_yaoSpr2024_Conjunction_w_chocoanChange
	* StepId: 67
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_event_yaoSpr2024_Conjunction_GAMA_67

## h_event_yaoSpr2024_Conjunction_w_combat
	* StepId: 32
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_yaoSpr2024_Conjunction_GAMA_32
		* h_event_yaoSpr2024_Conjunction_GAMA_73
		* h_event_yaoSpr2024_Conjunction_GAMA_75

## h_event_yaoSpr2024_Conjunction_w_combat2
	* StepId: 33
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_yaoSpr2024_Conjunction_GAMA_33
		* h_event_yaoSpr2024_Conjunction_GAMA_71

## h_event_yaoSpr2024_Conjunction_w_combat3
	* StepId: 34
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_yaoSpr2024_Conjunction_GAMA_34
		* h_event_yaoSpr2024_Conjunction_GAMA_65

## h_event_yaoSpr2024_Conjunction_w_combat4
	* StepId: 35
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_event_yaoSpr2024_Conjunction_GAMA_35

## h_event_yaoSpr2024_Conjunction_w_conjunction1
	* StepId: 46
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_yaoSpr2024_Conjunction_GAMA_46
		* h_event_yaoSpr2024_Conjunction_d_cunjunctionA

## h_event_yaoSpr2024_Conjunction_w_conjunction2
	* StepId: 47
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_yaoSpr2024_Conjunction_GAMA_47
		* h_event_yaoSpr2024_Conjunction_d_cunjunctionB

## h_event_yaoSpr2024_Conjunction_w_conjunction3
	* StepId: 48
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_yaoSpr2024_Conjunction_GAMA_48
		* h_event_yaoSpr2024_Conjunction_d_end

## h_event_yaoSpr2024_Conjunction_w_deactivateChocoanRepeating
	* StepId: 27
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_event_yaoSpr2024_Conjunction_activate_chocoanRepeating

## h_event_yaoSpr2024_Conjunction_w_deviationDialog
	* StepId: 29
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_yaoSpr2024_Conjunction_GAMA_29
		* h_event_yaoSpr2024_Conjunction_GAMA_31
		* h_event_yaoSpr2024_Conjunction_d_deviation

## h_event_yaoSpr2024_Conjunction_w_end
	* StepId: 45
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_yaoSpr2024_Conjunction_GAMA_45
		* h_event_yaoSpr2024_Conjunction_camera_conjuction
		* h_event_yaoSpr2024_Conjunction_close_conjunction

## h_event_yaoSpr2024_Conjunction_w_fail
	* StepId: 11
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_yaoSpr2024_Conjunction_GAMA_11
		* h_event_yaoSpr2024_Conjunction_d_fail

## h_event_yaoSpr2024_Conjunction_w_interludeDialog
	* StepId: 28
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_event_yaoSpr2024_Conjunction_d_interlude

## h_event_yaoSpr2024_Conjunction_w_intro
	* StepId: 3
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_yaoSpr2024_Conjunction_GAMA_3
		* h_event_yaoSpr2024_Conjunction_d_intro

## h_event_yaoSpr2024_Conjunction_w_lookAt
	* StepId: 2
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_event_yaoSpr2024_Conjunction_lookAt_conjunction

## h_event_yaoSpr2024_Conjunction_w_preferredTargetChocoanRepeating
	* StepId: 69
	* Type: TriggerRepeating
	* TargetType: WaitForTime
	* SuccLL: h_event_yaoSpr2024_Conjunction_GAMA_69

## h_event_yaoSpr2024_Conjunction_w_preferredTargetChocoanRepeating2
	* StepId: 59
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_event_yaoSpr2024_Conjunction_GAMA_59

## h_event_yaoSpr2024_Conjunction_w_removeElders
	* StepId: 71
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_event_yaoSpr2024_Conjunction_remove_elders

## h_event_yaoSpr2024_Conjunction_w_spawnBack
	* StepId: 22
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_yaoSpr2024_Conjunction_GAMA_22
		* h_event_yaoSpr2024_Conjunction_GAMA_23
		* h_event_yaoSpr2024_Conjunction_deactivate_pilgrimBackSpawn
		* h_event_yaoSpr2024_Conjunction_spawn_pilgrimBack

## h_event_yaoSpr2024_Conjunction_w_stutterActivate
	* StepId: 30
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_event_yaoSpr2024_Conjunction_GAMA_30
		* h_event_yaoSpr2024_Conjunction_deactivate_backStutter

## h_event_yaoSpr2024_Conjunction_w_stutterDeactivate
	* StepId: 31
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_event_yaoSpr2024_Conjunction_activate_backStutter

## h_event_yaoSpr2024_Conjunction_w_waveADialog
	* StepId: 75
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_event_yaoSpr2024_Conjunction_d_attackA

## h_event_yaoSpr2024_Conjunction_w_waveBDialog
	* StepId: 73
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_event_yaoSpr2024_Conjunction_d_attackB

## h_event_yaoSpr2024_Conjunction_w_winDialog
	* StepId: 51
	* Type: None
	* TargetType: WaitForTime
	* SuccLL: h_event_yaoSpr2024_Conjunction_d_win

## h_event_yaoSpr2024_Conjunction_wait_fail
	* StepId: 12
	* Type: Trigger
	* TargetType: WaitForTime

## h_pvp_Arena_start
	* StepId: 0
	* Type: Trigger
	* TargetType: Immediate

## h_pvp_ClanBeaconAttack_BeaconDeath
	* StepId: 2
	* Type: Goal
	* TargetType: AllUnitsWithTagsAreKilled

## h_pvp_ClanBeaconAttack_ClearAllEnemies
	* StepId: 3
	* Type: Goal
	* TargetType: AllUnitsWithTagsAreKilled

## h_pvp_ClanBeaconAttack_PostBeaconDeathEnemyCheck
	* StepId: 1
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* h_pvp_ClanBeaconAttack_BeaconDeath
		* h_pvp_ClanBeaconAttack_ClearAllEnemies
	* SuccLL: 
		* h_pvp_ClanBeaconAttack_PVP_Beacon_01_act_attackerWin
		* h_pvp_ClanBeaconAttack_finishMission

## h_pvp_ClanBeaconAttack_PVP_Beacon_01_g_defenderWin
	* StepId: 4
	* Type: Trigger
	* TargetType: OnPlayerFlagshipDestroyed
	* SuccLL: h_pvp_ClanBeaconAttack_PVP_Beacon_01_act_defenderWin

## h_pvp_ClanBeaconAttack_start
	* StepId: 0
	* Type: Trigger
	* TargetType: MissionStart
	* SuccLL: 
		* h_pvp_ClanBeaconAttack_GAMA_0
		* h_pvp_ClanBeaconAttack_GAMA_1
		* h_pvp_ClanBeaconAttack_GAMA_2
		* h_pvp_ClanBeaconAttack_GAMA_3
		* h_pvp_ClanBeaconAttack_GAMA_4
		* h_pvp_ClanBeaconAttack_spawnBeacon

## h_pvp_ClanBeaconAttack_waitTimerForDefenderRespawn
	* StepId: 5
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_pvp_ClanBeaconAttack_PVP_Beacon_01_spawnDefenderNPC

## h_side_DamageTest_Start
	* StepId: 0
	* Type: None
	* TargetType: MissionStart
	* SuccLL: 
		* h_side_DamageTest_GAMA_0
		* h_side_DamageTest_GAMA_1
		* h_side_DamageTest_GAMA_2
		* h_side_DamageTest_actn_makeUnitsInvincibleAt10

## h_side_DamageTest_t_spawnDebugUnits
	* StepId: 3
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_side_DamageTest_GAMA_11
		* h_side_DamageTest_GAMA_13
		* h_side_DamageTest_GAMA_15
		* h_side_DamageTest_GAMA_17
		* h_side_DamageTest_GAMA_19
		* h_side_DamageTest_GAMA_21
		* h_side_DamageTest_GAMA_23
		* h_side_DamageTest_GAMA_25
		* h_side_DamageTest_GAMA_3
		* h_side_DamageTest_GAMA_5
		* h_side_DamageTest_GAMA_7
		* h_side_DamageTest_GAMA_9
		* h_side_DamageTest_actn_spawnDebugAsset_01
		* h_side_DamageTest_actn_spawnDebugAsset_02
		* h_side_DamageTest_actn_spawnDebugAsset_03
		* h_side_DamageTest_actn_spawnDebugAsset_04
		* h_side_DamageTest_actn_spawnDebugAsset_05
		* h_side_DamageTest_actn_spawnDebugAsset_06
		* h_side_DamageTest_actn_spawnDebugAsset_07
		* h_side_DamageTest_actn_spawnDebugAsset_08
		* h_side_DamageTest_actn_spawnDebugAsset_09
		* h_side_DamageTest_actn_spawnDebugAsset_10
		* h_side_DamageTest_actn_spawnDebugAsset_11
		* h_side_DamageTest_actn_spawnDebugAsset_12

## h_side_DamageTest_trig_HealthCheck_DebugAsset_01
	* StepId: 2
	* Type: TriggerRepeating
	* TargetType: OnTaggedUnitIsBelowHealth
	* SuccLL: 
		* h_side_DamageTest_actn_allowDamageAgain
		* h_side_DamageTest_actn_healDebugAssetArmor_01
		* h_side_DamageTest_actn_healDebugAssetHull_01

## h_side_DamageTest_trig_RespawnDebugAsset_01
	* StepId: 4
	* Type: TriggerRepeating
	* TargetType: OnTaggedUnitKilled
	* SuccLL: h_side_DamageTest_GAMA_4

## h_side_DamageTest_trig_RespawnDebugAsset_02
	* StepId: 6
	* Type: TriggerRepeating
	* TargetType: OnTaggedUnitKilled
	* SuccLL: h_side_DamageTest_GAMA_6

## h_side_DamageTest_trig_RespawnDebugAsset_03
	* StepId: 8
	* Type: TriggerRepeating
	* TargetType: OnTaggedUnitKilled
	* SuccLL: h_side_DamageTest_GAMA_8

## h_side_DamageTest_trig_RespawnDebugAsset_04
	* StepId: 10
	* Type: TriggerRepeating
	* TargetType: OnTaggedUnitKilled
	* SuccLL: h_side_DamageTest_GAMA_10

## h_side_DamageTest_trig_RespawnDebugAsset_05
	* StepId: 12
	* Type: TriggerRepeating
	* TargetType: OnTaggedUnitKilled
	* SuccLL: h_side_DamageTest_GAMA_12

## h_side_DamageTest_trig_RespawnDebugAsset_06
	* StepId: 14
	* Type: TriggerRepeating
	* TargetType: OnTaggedUnitKilled
	* SuccLL: h_side_DamageTest_GAMA_14

## h_side_DamageTest_trig_RespawnDebugAsset_07
	* StepId: 16
	* Type: TriggerRepeating
	* TargetType: OnTaggedUnitKilled
	* SuccLL: h_side_DamageTest_GAMA_16

## h_side_DamageTest_trig_RespawnDebugAsset_08
	* StepId: 18
	* Type: TriggerRepeating
	* TargetType: OnTaggedUnitKilled
	* SuccLL: h_side_DamageTest_GAMA_18

## h_side_DamageTest_trig_RespawnDebugAsset_09
	* StepId: 20
	* Type: TriggerRepeating
	* TargetType: OnTaggedUnitKilled
	* SuccLL: h_side_DamageTest_GAMA_20

## h_side_DamageTest_trig_RespawnDebugAsset_10
	* StepId: 22
	* Type: TriggerRepeating
	* TargetType: OnTaggedUnitKilled
	* SuccLL: h_side_DamageTest_GAMA_22

## h_side_DamageTest_trig_RespawnDebugAsset_11
	* StepId: 24
	* Type: TriggerRepeating
	* TargetType: OnTaggedUnitKilled
	* SuccLL: h_side_DamageTest_GAMA_24

## h_side_DamageTest_trig_RespawnDebugAsset_12
	* StepId: 26
	* Type: TriggerRepeating
	* TargetType: OnTaggedUnitKilled
	* SuccLL: h_side_DamageTest_GAMA_26

## h_side_DamageTest_trig_WaitForTime
	* StepId: 1
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_side_DamageTest_actn_triggerDialog

## h_side_DamageTest_w_01
	* StepId: 5
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_side_DamageTest_actn_respawnDebugAsset_01

## h_side_DamageTest_w_02
	* StepId: 7
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_side_DamageTest_actn_respawnDebugAsset_02

## h_side_DamageTest_w_03
	* StepId: 9
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_side_DamageTest_actn_respawnDebugAsset_03

## h_side_DamageTest_w_04
	* StepId: 11
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_side_DamageTest_actn_respawnDebugAsset_04

## h_side_DamageTest_w_05
	* StepId: 13
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_side_DamageTest_actn_respawnDebugAsset_05

## h_side_DamageTest_w_06
	* StepId: 15
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_side_DamageTest_actn_respawnDebugAsset_06

## h_side_DamageTest_w_07
	* StepId: 17
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_side_DamageTest_actn_respawnDebugAsset_07

## h_side_DamageTest_w_08
	* StepId: 19
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_side_DamageTest_actn_respawnDebugAsset_08

## h_side_DamageTest_w_09
	* StepId: 21
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_side_DamageTest_actn_respawnDebugAsset_09

## h_side_DamageTest_w_10
	* StepId: 23
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_side_DamageTest_actn_respawnDebugAsset_10

## h_side_DamageTest_w_11
	* StepId: 25
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_side_DamageTest_actn_respawnDebugAsset_11

## h_side_DamageTest_w_12
	* StepId: 27
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_side_DamageTest_actn_respawnDebugAsset_12

## h_story_A01_DuzumiGate_Start
	* StepId: 0
	* Type: None
	* TargetType: MissionStart
	* SuccLL: 
		* h_story_A01_DuzumiGate_GAMA_0
		* h_story_A01_DuzumiGate_GAMA_9
		* h_story_A01_DuzumiGate_ally0
		* h_story_A01_DuzumiGate_seq1

## h_story_A01_DuzumiGate_t_d_1
	* StepId: 2
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: s_duzumi_intro_dialog_1
	* SuccLL: h_story_A01_DuzumiGate_GAMA_2

## h_story_A01_DuzumiGate_t_d_2
	* StepId: 4
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: s_duzumi_intro_dialog_2
	* SuccLL: h_story_A01_DuzumiGate_GAMA_4

## h_story_A01_DuzumiGate_t_d_3
	* StepId: 6
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: s_duzumi_intro_dialog_3
	* SuccLL: h_story_A01_DuzumiGate_GAMA_6

## h_story_A01_DuzumiGate_t_d_4
	* StepId: 8
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: s_duzumi_intro_dialog_4
	* SuccLL: h_story_A01_DuzumiGate_GAMA_8

## h_story_A01_DuzumiGate_t_d_6_
	* StepId: 12
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: s_duzumi_intro_dialog_6
	* SuccLL: h_story_A01_DuzumiGate_GAMA_12

## h_story_A01_DuzumiGate_t_d_7
	* StepId: 14
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: s_duzumi_intro_dialog_7
	* SuccLL: h_story_A01_DuzumiGate_GAMA_14

## h_story_A01_DuzumiGate_t_seq1
	* StepId: 10
	* Type: Trigger
	* TargetType: OnInGameSequenceFinishedForPlayer
	* SuccLL: 
		* h_story_A01_DuzumiGate_GAMA_10
		* h_story_A01_DuzumiGate_GAMA_11
		* h_story_A01_DuzumiGate_d_6_
		* h_story_A01_DuzumiGate_seq2

## h_story_A01_DuzumiGate_t_seq2
	* StepId: 11
	* Type: Trigger
	* TargetType: OnInGameSequenceFinishedForPlayer
	* SuccLL: 
		* h_story_A01_DuzumiGate_cinematic
		* h_story_A01_DuzumiGate_fin

## h_story_A01_DuzumiGate_w_0
	* StepId: 1
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A01_DuzumiGate_GAMA_1
		* h_story_A01_DuzumiGate_d_1

## h_story_A01_DuzumiGate_w_1
	* StepId: 3
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A01_DuzumiGate_GAMA_3
		* h_story_A01_DuzumiGate_d_2

## h_story_A01_DuzumiGate_w_3
	* StepId: 5
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A01_DuzumiGate_GAMA_5
		* h_story_A01_DuzumiGate_d_3

## h_story_A01_DuzumiGate_w_4
	* StepId: 9
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_A01_DuzumiGate_d_5_

## h_story_A01_DuzumiGate_w_6
	* StepId: 13
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A01_DuzumiGate_GAMA_13
		* h_story_A01_DuzumiGate_d_7_

## h_story_A01_DuzumiGate_w_7
	* StepId: 15
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_A01_DuzumiGate_d_8

## h_story_A01_DuzumiGate_w_8
	* StepId: 7
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A01_DuzumiGate_GAMA_7
		* h_story_A01_DuzumiGate_d_4_

## h_story_A01_DuzumiGateTut_dt_praise
	* StepId: 19
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: s_duzumiTut_praise
	* SuccLL: 
		* h_story_A01_DuzumiGateTut_GAMA_19
		* h_story_A01_DuzumiGateTut_addUI_enableUnitTray
		* h_story_A01_DuzumiGateTut_d_unitTray

## h_story_A01_DuzumiGateTut_goal_cameraAuto
	* StepId: 9
	* Type: Goal
	* TargetType: OnClientUIElementHasState
	* SuccLL: 
		* h_story_A01_DuzumiGateTut_GAMA_9
		* h_story_A01_DuzumiGateTut_close_cameraAutoSwipe
		* h_story_A01_DuzumiGateTut_deactivate_cameraAutoDialog
		* h_story_A01_DuzumiGateTut_stopUI_cameraAutoSwipe

## h_story_A01_DuzumiGateTut_goal_cameraSwipe
	* StepId: 5
	* Type: Goal
	* TargetType: UseCamera
	* SuccLL: 
		* h_story_A01_DuzumiGateTut_GAMA_5
		* h_story_A01_DuzumiGateTut_close_cameraSwipeDialog
		* h_story_A01_DuzumiGateTut_deactivate_cameraSwipeDialog
		* h_story_A01_DuzumiGateTut_stopUI_cameraSwipeDialog

## h_story_A01_DuzumiGateTut_goal_cameraZoom
	* StepId: 7
	* Type: Goal
	* TargetType: UseCameraZoom
	* SuccLL: 
		* h_story_A01_DuzumiGateTut_GAMA_7
		* h_story_A01_DuzumiGateTut_close_cameraZoomDialog
		* h_story_A01_DuzumiGateTut_deactivate_cameraZoomDialog
		* h_story_A01_DuzumiGateTut_stopUI_cameraZoomDialog

## h_story_A01_DuzumiGateTut_goal_killDrones
	* StepId: 17
	* Type: Goal
	* TargetType: WaveFinished
	* SuccLL: 
		* h_story_A01_DuzumiGateTut_GAMA_17
		* h_story_A01_DuzumiGateTut_close_attackTargetList
		* h_story_A01_DuzumiGateTut_deactivate_attackTargetListDialog
		* h_story_A01_DuzumiGateTut_stopUI_attackTargetList

## h_story_A01_DuzumiGateTut_goal_killFrigate
	* StepId: 25
	* Type: Goal
	* TargetType: FinishGoalsString
	* TVS: h_story_A01_DuzumiGateTut_i_explosion
	* SuccLL: 
		* h_story_A01_DuzumiGateTut_GAMA_25
		* h_story_A01_DuzumiGateTut_GAMA_40
		* h_story_A01_DuzumiGateTut_GAMA_42

## h_story_A01_DuzumiGateTut_goal_moveDrag
	* StepId: 21
	* Type: Goal
	* TargetType: ReachPointOfInterest
	* SuccLL: 
		* h_story_A01_DuzumiGateTut_GAMA_21
		* h_story_A01_DuzumiGateTut_close_moveDrag
		* h_story_A01_DuzumiGateTut_deactivate_moveDrag
		* h_story_A01_DuzumiGateTut_stopUI_moveDrag

## h_story_A01_DuzumiGateTut_goal_moveTargetList
	* StepId: 13
	* Type: Goal
	* TargetType: ReachPointOfInterest
	* SuccLL: 
		* h_story_A01_DuzumiGateTut_GAMA_13
		* h_story_A01_DuzumiGateTut_close_moveTargetList
		* h_story_A01_DuzumiGateTut_deactivate_moveTargetListDialog
		* h_story_A01_DuzumiGateTut_stopUI_moveToTargetList

## h_story_A01_DuzumiGateTut_goal_moveTaskForce
	* StepId: 27
	* Type: Goal
	* TargetType: ReachPointOfInterest
	* SuccLL: 
		* h_story_A01_DuzumiGateTut_GAMA_27
		* h_story_A01_DuzumiGateTut_GAMA_37
		* h_story_A01_DuzumiGateTut_d_outro
		* h_story_A01_DuzumiGateTut_deactivate_moveTaskForceDialog
		* h_story_A01_DuzumiGateTut_moveTo_TaskForce
		* h_story_A01_DuzumiGateTut_stopUI_moveTaskForce

## h_story_A01_DuzumiGateTut_goal_skill
	* StepId: 48
	* Type: Goal
	* TargetType: UseSkill
	* SuccLL: 
		* h_story_A01_DuzumiGateTut_GAMA_48
		* h_story_A01_DuzumiGateTut_close_skill
		* h_story_A01_DuzumiGateTut_deactivate_skill
		* h_story_A01_DuzumiGateTut_stopUI_skill

## h_story_A01_DuzumiGateTut_healthCheck_frigate
	* StepId: 46
	* Type: Trigger
	* TargetType: TaggedUnitsBelowHealthAndArmor
	* SuccLL: h_story_A01_DuzumiGateTut_GAMA_46

## h_story_A01_DuzumiGateTut_i_cameraSwipe
	* StepId: 4
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_story_A01_DuzumiGateTut_GAMA_4
		* h_story_A01_DuzumiGateTut_GAMA_66
		* h_story_A01_DuzumiGateTut_d_cameraSwipe

## h_story_A01_DuzumiGateTut_i_droneSetup
	* StepId: 61
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_story_A01_DuzumiGateTut_moveTo_drones
		* h_story_A01_DuzumiGateTut_sequence_drones
		* h_story_A01_DuzumiGateTut_wave_0_drones

## h_story_A01_DuzumiGateTut_i_explosion
	* StepId: 53
	* Type: Trigger
	* TargetType: Immediate

## h_story_A01_DuzumiGateTut_i_jumpOutSequence
	* StepId: 32
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_story_A01_DuzumiGateTut_GAMA_32
		* h_story_A01_DuzumiGateTut_d_outro6

## h_story_A01_DuzumiGateTut_i_moveTargetList
	* StepId: 12
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_story_A01_DuzumiGateTut_GAMA_12
		* h_story_A01_DuzumiGateTut_GAMA_62
		* h_story_A01_DuzumiGateTut_GAMA_63
		* h_story_A01_DuzumiGateTut_d_moveTargetList

## h_story_A01_DuzumiGateTut_i_uiSetup
	* StepId: 77
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_story_A01_DuzumiGateTut_addUI_enableBasics
		* h_story_A01_DuzumiGateTut_addUI_hideAll
		* h_story_A01_DuzumiGateTut_addUI_showLogs

## h_story_A01_DuzumiGateTut_position_KharKalaad
	* StepId: 43
	* Type: Trigger
	* TargetType: ReachPointOfInterest
	* SuccLL: h_story_A01_DuzumiGateTut_GAMA_43

## h_story_A01_DuzumiGateTut_position_moveTaskForce
	* StepId: 40
	* Type: Trigger
	* TargetType: ReachPointOfInterest
	* SuccLL: h_story_A01_DuzumiGateTut_d_preOutro

## h_story_A01_DuzumiGateTut_position_RiifSa
	* StepId: 41
	* Type: Trigger
	* TargetType: ReachPointOfInterest
	* SuccLL: h_story_A01_DuzumiGateTut_GAMA_41

## h_story_A01_DuzumiGateTut_position_targetListFill
	* StepId: 64
	* Type: Trigger
	* TargetType: ReachPointOfInterest
	* SuccLL: h_story_A01_DuzumiGateTut_d_moveTargetListFill

## h_story_A01_DuzumiGateTut_repeat_healthCheck_frigate
	* StepId: 55
	* Type: TriggerRepeating
	* TargetType: TaggedUnitsBelowHealthAndArmor
	* SuccLL: h_story_A01_DuzumiGateTut_eb5f80fed1e9bab45b7f53018d5a50ea

## h_story_A01_DuzumiGateTut_sequenceFin_drones
	* StepId: 15
	* Type: Trigger
	* TargetType: OnInGameSequenceFinishedForPlayer
	* TVS: 1
	* SuccLL: 
		* h_story_A01_DuzumiGateTut_GAMA_15
		* h_story_A01_DuzumiGateTut_close_droneSequence
		* h_story_A01_DuzumiGateTut_deactivate_dronSequenceDialog
		* h_story_A01_DuzumiGateTut_lookAt_drones
		* h_story_A01_DuzumiGateTut_teleport_drones

## h_story_A01_DuzumiGateTut_sequenceFin_frigate
	* StepId: 23
	* Type: Trigger
	* TargetType: OnInGameSequenceFinishedForPlayer
	* TVS: 1
	* SuccLL: 
		* h_story_A01_DuzumiGateTut_GAMA_23
		* h_story_A01_DuzumiGateTut_activate_frigate
		* h_story_A01_DuzumiGateTut_close_frigateSequence
		* h_story_A01_DuzumiGateTut_deactivate_frigateSequenceDialog
		* h_story_A01_DuzumiGateTut_lookAt_frigate

## h_story_A01_DuzumiGateTut_sequenceFin_Intro
	* StepId: 1
	* Type: Trigger
	* TargetType: OnInGameSequenceFinishedForPlayer
	* TVS: 1
	* SuccLL: 
		* h_story_A01_DuzumiGateTut_GAMA_1
		* h_story_A01_DuzumiGateTut_close_introSequence
		* h_story_A01_DuzumiGateTut_deactivate_introSequenceDialog
		* h_story_A01_DuzumiGateTut_lookAt_intro

## h_story_A01_DuzumiGateTut_sequenceFin_jumpOut
	* StepId: 31
	* Type: Trigger
	* TargetType: OnInGameSequenceFinishedForPlayer
	* TVS: 1
	* SuccLL: h_story_A01_DuzumiGateTut_endGraph

## h_story_A01_DuzumiGateTut_start
	* StepId: 0
	* Type: Trigger
	* TargetType: MissionStart
	* SuccLL: 
		* h_story_A01_DuzumiGateTut_GAMA_0
		* h_story_A01_DuzumiGateTut_GAMA_67
		* h_story_A01_DuzumiGateTut_GAMA_76
		* h_story_A01_DuzumiGateTut_ally_0_All
		* h_story_A01_DuzumiGateTut_disable_KK
		* h_story_A01_DuzumiGateTut_disable_RS
		* h_story_A01_DuzumiGateTut_disable_allies
		* h_story_A01_DuzumiGateTut_sequence_Intro

## h_story_A01_DuzumiGateTut_td_attackDrag
	* StepId: 45
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: s_duzumiTut_attackDrag
	* SuccLL: h_story_A01_DuzumiGateTut_ui_dragAttack

## h_story_A01_DuzumiGateTut_td_attackTargetList
	* StepId: 60
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: s_duzumiTut_attackTargetList
	* SuccLL: h_story_A01_DuzumiGateTut_ui_attackDrones

## h_story_A01_DuzumiGateTut_td_cameraAuto
	* StepId: 65
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: s_duzumiTut_cameraAuto
	* SuccLL: h_story_A01_DuzumiGateTut_ui_cameraAuto

## h_story_A01_DuzumiGateTut_td_cameraSwipe
	* StepId: 67
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: s_duzumiTut_cameraSwipe
	* SuccLL: h_story_A01_DuzumiGateTut_ui_swipe

## h_story_A01_DuzumiGateTut_td_cameraZoom
	* StepId: 66
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: s_duzumiTut_cameraZoom
	* SuccLL: h_story_A01_DuzumiGateTut_ui_zoom

## h_story_A01_DuzumiGateTut_td_intro
	* StepId: 3
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: s_duzumiTut_intro
	* SuccLL: h_story_A01_DuzumiGateTut_GAMA_3

## h_story_A01_DuzumiGateTut_td_intro1
	* StepId: 69
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: s_duzumi_intro_dialog_1
	* SuccLL: h_story_A01_DuzumiGateTut_GAMA_69

## h_story_A01_DuzumiGateTut_td_intro2
	* StepId: 71
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: s_duzumi_intro_dialog_2
	* SuccLL: h_story_A01_DuzumiGateTut_GAMA_71

## h_story_A01_DuzumiGateTut_td_intro3
	* StepId: 73
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: s_duzumi_intro_dialog_3
	* SuccLL: h_story_A01_DuzumiGateTut_GAMA_73

## h_story_A01_DuzumiGateTut_td_intro4
	* StepId: 75
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: s_duzumi_intro_dialog_4
	* SuccLL: h_story_A01_DuzumiGateTut_GAMA_75

## h_story_A01_DuzumiGateTut_td_moveDrag
	* StepId: 59
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: s_duzumiTut_moveDrag
	* SuccLL: h_story_A01_DuzumiGateTut_ui_dragMove

## h_story_A01_DuzumiGateTut_td_moveTargetList
	* StepId: 63
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: s_duzumiTut_moveTargetList
	* SuccLL: h_story_A01_DuzumiGateTut_ui_moveToTargetList

## h_story_A01_DuzumiGateTut_td_moveTaskForce
	* StepId: 39
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: s_duzumiTut_moveTaskForce
	* SuccLL: h_story_A01_DuzumiGateTut_ui_moveTaskForce

## h_story_A01_DuzumiGateTut_td_outro
	* StepId: 28
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: s_duzumiTut_outro
	* SuccLL: 
		* h_story_A01_DuzumiGateTut_GAMA_28
		* h_story_A01_DuzumiGateTut_fin_continue

## h_story_A01_DuzumiGateTut_td_outro6
	* StepId: 33
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: s_duzumi_intro_dialog_6
	* SuccLL: h_story_A01_DuzumiGateTut_GAMA_33

## h_story_A01_DuzumiGateTut_td_outro7
	* StepId: 35
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: s_duzumi_intro_dialog_7
	* SuccLL: h_story_A01_DuzumiGateTut_GAMA_35

## h_story_A01_DuzumiGateTut_td_outro8
	* StepId: 37
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: s_duzumi_intro_dialog_8

## h_story_A01_DuzumiGateTut_td_skill
	* StepId: 54
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: s_duzumiTut_skill
	* SuccLL: h_story_A01_DuzumiGateTut_ui_skill

## h_story_A01_DuzumiGateTut_td_targetList2
	* StepId: 11
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: s_duzumiTut_targetList
	* SuccLL: h_story_A01_DuzumiGateTut_GAMA_11

## h_story_A01_DuzumiGateTut_td_unitTray
	* StepId: 20
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: s_duzumiTut_unitTray
	* SuccLL: 
		* h_story_A01_DuzumiGateTut_GAMA_20
		* h_story_A01_DuzumiGateTut_GAMA_58
		* h_story_A01_DuzumiGateTut_d_moveDrag
		* h_story_A01_DuzumiGateTut_lookAt_moveDrag

## h_story_A01_DuzumiGateTut_w_attackDrones
	* StepId: 16
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A01_DuzumiGateTut_GAMA_16
		* h_story_A01_DuzumiGateTut_GAMA_59
		* h_story_A01_DuzumiGateTut_d_attackTargetList

## h_story_A01_DuzumiGateTut_w_attackFrigate
	* StepId: 24
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A01_DuzumiGateTut_GAMA_24
		* h_story_A01_DuzumiGateTut_GAMA_44
		* h_story_A01_DuzumiGateTut_GAMA_45
		* h_story_A01_DuzumiGateTut_d_attackDrag

## h_story_A01_DuzumiGateTut_w_autoCamera
	* StepId: 8
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A01_DuzumiGateTut_GAMA_64
		* h_story_A01_DuzumiGateTut_GAMA_8
		* h_story_A01_DuzumiGateTut_addUI_enableSensorManager
		* h_story_A01_DuzumiGateTut_d_cameraAuto

## h_story_A01_DuzumiGateTut_w_cameraZoom
	* StepId: 6
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A01_DuzumiGateTut_GAMA_6
		* h_story_A01_DuzumiGateTut_GAMA_65
		* h_story_A01_DuzumiGateTut_d_cameraZoom

## h_story_A01_DuzumiGateTut_w_disablePlayer
	* StepId: 38
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_A01_DuzumiGateTut_disable_Player

## h_story_A01_DuzumiGateTut_w_drones
	* StepId: 14
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A01_DuzumiGateTut_GAMA_14
		* h_story_A01_DuzumiGateTut_GAMA_60
		* h_story_A01_DuzumiGateTut_GAMA_61

## h_story_A01_DuzumiGateTut_w_droneSequence
	* StepId: 62
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_A01_DuzumiGateTut_d_targetDrones

## h_story_A01_DuzumiGateTut_w_explosion1
	* StepId: 50
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A01_DuzumiGateTut_GAMA_50
		* h_story_A01_DuzumiGateTut_activate_taskForce
		* h_story_A01_DuzumiGateTut_kill_frigate

## h_story_A01_DuzumiGateTut_w_explosion2
	* StepId: 51
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A01_DuzumiGateTut_GAMA_51
		* h_story_A01_DuzumiGateTut_d_explosion

## h_story_A01_DuzumiGateTut_w_explosion3
	* StepId: 52
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_A01_DuzumiGateTut_GAMA_52

## h_story_A01_DuzumiGateTut_w_intro
	* StepId: 2
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A01_DuzumiGateTut_GAMA_2
		* h_story_A01_DuzumiGateTut_d_intro

## h_story_A01_DuzumiGateTut_w_intro1
	* StepId: 68
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A01_DuzumiGateTut_GAMA_68
		* h_story_A01_DuzumiGateTut_d_intro1

## h_story_A01_DuzumiGateTut_w_intro2
	* StepId: 70
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A01_DuzumiGateTut_GAMA_70
		* h_story_A01_DuzumiGateTut_d_intro2

## h_story_A01_DuzumiGateTut_w_intro3
	* StepId: 72
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A01_DuzumiGateTut_GAMA_72
		* h_story_A01_DuzumiGateTut_d_intro3

## h_story_A01_DuzumiGateTut_w_intro4
	* StepId: 74
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A01_DuzumiGateTut_GAMA_74
		* h_story_A01_DuzumiGateTut_d_intro4

## h_story_A01_DuzumiGateTut_w_intro5
	* StepId: 76
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_A01_DuzumiGateTut_d_intro5

## h_story_A01_DuzumiGateTut_w_jumpOutSequence
	* StepId: 30
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A01_DuzumiGateTut_GAMA_30
		* h_story_A01_DuzumiGateTut_GAMA_31
		* h_story_A01_DuzumiGateTut_sequence_jumpOut

## h_story_A01_DuzumiGateTut_w_KharKalaad
	* StepId: 44
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_A01_DuzumiGateTut_deactivate_KharKalaad

## h_story_A01_DuzumiGateTut_w_moveTargetList
	* StepId: 10
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A01_DuzumiGateTut_GAMA_10
		* h_story_A01_DuzumiGateTut_addUI_enableTargetList
		* h_story_A01_DuzumiGateTut_d_targetList

## h_story_A01_DuzumiGateTut_w_moveTaskForce
	* StepId: 26
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A01_DuzumiGateTut_GAMA_26
		* h_story_A01_DuzumiGateTut_GAMA_38
		* h_story_A01_DuzumiGateTut_GAMA_39
		* h_story_A01_DuzumiGateTut_d_moveTaskForce
		* h_story_A01_DuzumiGateTut_lookAt_moveTaskForce

## h_story_A01_DuzumiGateTut_w_outro1
	* StepId: 34
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A01_DuzumiGateTut_GAMA_34
		* h_story_A01_DuzumiGateTut_d_outro7

## h_story_A01_DuzumiGateTut_w_outro2
	* StepId: 36
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A01_DuzumiGateTut_GAMA_36
		* h_story_A01_DuzumiGateTut_d_outro8

## h_story_A01_DuzumiGateTut_w_praise
	* StepId: 18
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A01_DuzumiGateTut_GAMA_18
		* h_story_A01_DuzumiGateTut_d_praise

## h_story_A01_DuzumiGateTut_w_RiifSa
	* StepId: 42
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_A01_DuzumiGateTut_deactivate_RiifSa

## h_story_A01_DuzumiGateTut_w_sequenceFrigate
	* StepId: 22
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A01_DuzumiGateTut_GAMA_22
		* h_story_A01_DuzumiGateTut_GAMA_55
		* h_story_A01_DuzumiGateTut_deactivate_frigate
		* h_story_A01_DuzumiGateTut_wave_2_frigate

## h_story_A01_DuzumiGateTut_w_sequenceFrigate1
	* StepId: 56
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A01_DuzumiGateTut_GAMA_56
		* h_story_A01_DuzumiGateTut_moveTo_Frigate
		* h_story_A01_DuzumiGateTut_sequence_frigate

## h_story_A01_DuzumiGateTut_w_sequenceFrigate2
	* StepId: 57
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A01_DuzumiGateTut_GAMA_57
		* h_story_A01_DuzumiGateTut_d_targetFrigate

## h_story_A01_DuzumiGateTut_w_sequenceFrigate3
	* StepId: 58
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_A01_DuzumiGateTut_d_targetFrigate2

## h_story_A01_DuzumiGateTut_w_skill1
	* StepId: 47
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A01_DuzumiGateTut_GAMA_47
		* h_story_A01_DuzumiGateTut_GAMA_53
		* h_story_A01_DuzumiGateTut_GAMA_54
		* h_story_A01_DuzumiGateTut_addUI_enableSkills
		* h_story_A01_DuzumiGateTut_d_skill
		* h_story_A01_DuzumiGateTut_deactivate_attackDragDialog
		* h_story_A01_DuzumiGateTut_stopUI_attackDragDialog

## h_story_A01_DuzumiGateTut_w_skill2
	* StepId: 49
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A01_DuzumiGateTut_GAMA_49
		* h_story_A01_DuzumiGateTut_camera_explosion

## h_story_A01_DuzumiGateTut_waitForRewards
	* StepId: 29
	* Type: Trigger
	* TargetType: WaitForPlayerReceivedRewards
	* SuccLL: h_story_A01_DuzumiGateTut_GAMA_29

## h_story_A02_WiracodaGate_endSequence_intro
	* StepId: 1
	* Type: Trigger
	* TargetType: OnInGameSequenceFinishedForPlayer
	* TVS: 1
	* SuccLL: h_story_A02_WiracodaGate_GAMA_1

## h_story_A02_WiracodaGate_goal_attackDrones
	* StepId: 11
	* Type: Goal
	* TargetType: OnPlayerAttackNPC
	* SuccLL: 
		* h_story_A02_WiracodaGate_GAMA_11
		* h_story_A02_WiracodaGate_close_goalDrones
		* h_story_A02_WiracodaGate_deactivate_goalDrones
		* h_story_A02_WiracodaGate_stopUI_attackDrones

## h_story_A02_WiracodaGate_goal_killAll
	* StepId: 45
	* Type: Goal
	* TargetType: WaveFinished

## h_story_A02_WiracodaGate_goal_killTormentor
	* StepId: 18
	* Type: Goal
	* TargetType: KillSpecificWave
	* SuccLL: 
		* h_story_A02_WiracodaGate_GAMA_18
		* h_story_A02_WiracodaGate_close_goalTormentor
		* h_story_A02_WiracodaGate_deactivate_attackTormentor
		* h_story_A02_WiracodaGate_stopUI_tormentorUIs

## h_story_A02_WiracodaGate_goal_positionForward
	* StepId: 58
	* Type: Goal
	* TargetType: ReachPointOfInterest
	* SuccLL: h_story_A02_WiracodaGate_deactivate_goalPosition

## h_story_A02_WiracodaGate_goal_useSkill
	* StepId: 13
	* Type: Goal
	* TargetType: UseSkill
	* SuccLL: 
		* h_story_A02_WiracodaGate_GAMA_13
		* h_story_A02_WiracodaGate_close_goalSkill
		* h_story_A02_WiracodaGate_deactivate_goalSkill
		* h_story_A02_WiracodaGate_deactivate_triggerRepeating
		* h_story_A02_WiracodaGate_stopUI_useSkill

## h_story_A02_WiracodaGate_goals_allShipsAtPosition
	* StepId: 4
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* h_story_A02_WiracodaGate_goal_positionForward
		* h_story_A02_WiracodaGate_reach_KharKaalad
		* h_story_A02_WiracodaGate_reach_RiffSa
	* SuccLL: 
		* h_story_A02_WiracodaGate_GAMA_4
		* h_story_A02_WiracodaGate_GAMA_7

## h_story_A02_WiracodaGate_health_tormentor
	* StepId: 52
	* Type: Trigger
	* TargetType: TaggedUnitsBelowHealthAndArmor
	* SuccLL: 
		* h_story_A02_WiracodaGate_GAMA_52
		* h_story_A02_WiracodaGate_GAMA_53
		* h_story_A02_WiracodaGate_d_skillReminder
		* h_story_A02_WiracodaGate_deactivate_preCheckAndAttack
		* h_story_A02_WiracodaGate_stopUI_attackTormentor

## h_story_A02_WiracodaGate_i_alliesMove
	* StepId: 61
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_story_A02_WiracodaGate_GAMA_61
		* h_story_A02_WiracodaGate_GAMA_62
		* h_story_A02_WiracodaGate_activate_KharKaalad
		* h_story_A02_WiracodaGate_activate_RiffSa

## h_story_A02_WiracodaGate_i_skillReminder
	* StepId: 51
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_story_A02_WiracodaGate_GAMA_51
		* h_story_A02_WiracodaGate_GAMA_54

## h_story_A02_WiracodaGate_i_spawnAllies
	* StepId: 47
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_story_A02_WiracodaGate_ally_Akalon
		* h_story_A02_WiracodaGate_ally_Haarsuk
		* h_story_A02_WiracodaGate_ally_Scout01

## h_story_A02_WiracodaGate_i_spawnEnemies
	* StepId: 48
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_story_A02_WiracodaGate_wave_Movers01
		* h_story_A02_WiracodaGate_wave_Movers02
		* h_story_A02_WiracodaGate_wave_Tormentor01
		* h_story_A02_WiracodaGate_wave_Tormentor02

## h_story_A02_WiracodaGate_i_spawningAllies
	* StepId: 65
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_story_A02_WiracodaGate_ally_KharKaalad
		* h_story_A02_WiracodaGate_ally_RiffSa
		* h_story_A02_WiracodaGate_deactivate_KharKaalad
		* h_story_A02_WiracodaGate_deactivate_RiffSa

## h_story_A02_WiracodaGate_i_uiSetup
	* StepId: 66
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_story_A02_WiracodaGate_addUI_showLogs
		* h_story_A02_WiracodaGate_addUI_tutorialHUD

## h_story_A02_WiracodaGate_playerKill
	* StepId: 64
	* Type: Trigger
	* TargetType: OnPlayerFlagshipDestroyed
	* SuccLL: h_story_A02_WiracodaGate_fail

## h_story_A02_WiracodaGate_position_Interlude
	* StepId: 59
	* Type: Trigger
	* TargetType: ReachPointOfInterest
	* SuccLL: 
		* h_story_A02_WiracodaGate_d_noSign
		* h_story_A02_WiracodaGate_deactivate_uiTrigger
		* h_story_A02_WiracodaGate_stopUI_position

## h_story_A02_WiracodaGate_reach_KharKaalad
	* StepId: 63
	* Type: Trigger
	* TargetType: ReachPointOfInterest
	* SuccLL: h_story_A02_WiracodaGate_DeactivateKharKaalad02

## h_story_A02_WiracodaGate_reach_RiffSa
	* StepId: 62
	* Type: Trigger
	* TargetType: ReachPointOfInterest
	* SuccLL: h_story_A02_WiracodaGate_DeactivateRiffSa02

## h_story_A02_WiracodaGate_sequenceEnd_end
	* StepId: 33
	* Type: Trigger
	* TargetType: OnInGameSequenceFinishedForPlayer
	* TVS: 1
	* SuccLL: 
		* h_story_A02_WiracodaGate_FinishMissionSuccess
		* h_story_A02_WiracodaGate_StartCinematic

## h_story_A02_WiracodaGate_sequenceEnd_keeper
	* StepId: 23
	* Type: Trigger
	* TargetType: OnInGameSequenceFinishedForPlayer
	* TVS: 1
	* SuccLL: 
		* h_story_A02_WiracodaGate_GAMA_23
		* h_story_A02_WiracodaGate_activate_flagship
		* h_story_A02_WiracodaGate_activate_keeper
		* h_story_A02_WiracodaGate_close_afterKeeperSequence
		* h_story_A02_WiracodaGate_deactivate_keeperSequenceDialog

## h_story_A02_WiracodaGate_start
	* StepId: 0
	* Type: Trigger
	* TargetType: MissionStart
	* SuccLL: 
		* h_story_A02_WiracodaGate_GAMA_0
		* h_story_A02_WiracodaGate_GAMA_63
		* h_story_A02_WiracodaGate_GAMA_64
		* h_story_A02_WiracodaGate_GAMA_65
		* h_story_A02_WiracodaGate_sequence_intro

## h_story_A02_WiracodaGate_td_attackDrones
	* StepId: 57
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: story_Wiracoda_dialog_attackDrones
	* SuccLL: h_story_A02_WiracodaGate_ui_attackDrones

## h_story_A02_WiracodaGate_td_attackTormentor
	* StepId: 50
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: story_Wiracoda_dialog_attackTormentor
	* SuccLL: h_story_A02_WiracodaGate_ui_attackTomentor

## h_story_A02_WiracodaGate_td_intro
	* StepId: 3
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: story_Wiracoda_dialog_intro
	* SuccLL: 
		* h_story_A02_WiracodaGate_GAMA_3
		* h_story_A02_WiracodaGate_GAMA_57
		* h_story_A02_WiracodaGate_GAMA_58
		* h_story_A02_WiracodaGate_GAMA_59
		* h_story_A02_WiracodaGate_GAMA_60
		* h_story_A02_WiracodaGate_d_moveForward

## h_story_A02_WiracodaGate_td_moveForward
	* StepId: 60
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: story_Wiracoda_dialog_moveForward
	* SuccLL: h_story_A02_WiracodaGate_ShowUIHighlightSequence01

## h_story_A02_WiracodaGate_td_skillReminder
	* StepId: 54
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: story_Wiracoda_dialog_skillReminder
	* SuccLL: h_story_A02_WiracodaGate_ui_useSkill2

## h_story_A02_WiracodaGate_td_useSkill
	* StepId: 56
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: story_Wiracoda_dialog_useSkill
	* SuccLL: h_story_A02_WiracodaGate_ui_useSkill

## h_story_A02_WiracodaGate_TriggerRepeatingSpawnDrones01
	* StepId: 6
	* Type: TriggerRepeating
	* TargetType: KillSpecificWave
	* SuccLL: h_story_A02_WiracodaGate_TriggerWaveDrones01b

## h_story_A02_WiracodaGate_useSkil_reminder
	* StepId: 53
	* Type: Trigger
	* TargetType: UseSkill
	* SuccLL: 
		* h_story_A02_WiracodaGate_close_triggerSkill
		* h_story_A02_WiracodaGate_deactivate_triggerSkill
		* h_story_A02_WiracodaGate_stopUI_useSkill2

## h_story_A02_WiracodaGate_useSkill_preCheck
	* StepId: 55
	* Type: Trigger
	* TargetType: UseSkill
	* SuccLL: h_story_A02_WiracodaGate_deactivate_healthTormentor

## h_story_A02_WiracodaGate_w_Akalon01
	* StepId: 25
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A02_WiracodaGate_GAMA_25
		* h_story_A02_WiracodaGate_GAMA_40
		* h_story_A02_WiracodaGate_armor_Akalon01
		* h_story_A02_WiracodaGate_health_Akalon01

## h_story_A02_WiracodaGate_w_Akalon02
	* StepId: 26
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A02_WiracodaGate_GAMA_26
		* h_story_A02_WiracodaGate_GAMA_39
		* h_story_A02_WiracodaGate_armor_Akalon02
		* h_story_A02_WiracodaGate_health_Akalon02

## h_story_A02_WiracodaGate_w_Akalon03
	* StepId: 27
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A02_WiracodaGate_GAMA_27
		* h_story_A02_WiracodaGate_GAMA_38
		* h_story_A02_WiracodaGate_destroy_Akalon

## h_story_A02_WiracodaGate_w_barrage
	* StepId: 14
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A02_WiracodaGate_GAMA_14
		* h_story_A02_WiracodaGate_d_dronesWin

## h_story_A02_WiracodaGate_w_closeInterlude
	* StepId: 7
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_A02_WiracodaGate_close_kkSequence

## h_story_A02_WiracodaGate_w_closeInterlude2
	* StepId: 49
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_A02_WiracodaGate_close_tormentorWin

## h_story_A02_WiracodaGate_w_diaOffset01
	* StepId: 41
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_A02_WiracodaGate_d_Akalon01

## h_story_A02_WiracodaGate_w_diaOffset02
	* StepId: 40
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_A02_WiracodaGate_d_Akalon02

## h_story_A02_WiracodaGate_w_diaOffset03
	* StepId: 39
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_A02_WiracodaGate_d_Akalon03

## h_story_A02_WiracodaGate_w_diaOffset04
	* StepId: 38
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_A02_WiracodaGate_d_Haarsuk01

## h_story_A02_WiracodaGate_w_diaOffset05
	* StepId: 37
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_A02_WiracodaGate_StartDialogHaarsuk2

## h_story_A02_WiracodaGate_w_diaOffset06
	* StepId: 36
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_A02_WiracodaGate_d_endKeeper

## h_story_A02_WiracodaGate_w_diaOffset07
	* StepId: 35
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A02_WiracodaGate_d_endOverwhelmed
		* h_story_A02_WiracodaGate_wave_sequenceDrones01
		* h_story_A02_WiracodaGate_wave_sequenceDrones02

## h_story_A02_WiracodaGate_w_droneCamera
	* StepId: 9
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A02_WiracodaGate_GAMA_9
		* h_story_A02_WiracodaGate_StartDialogFight3

## h_story_A02_WiracodaGate_w_droneCamera2
	* StepId: 10
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A02_WiracodaGate_GAMA_10
		* h_story_A02_WiracodaGate_GAMA_56
		* h_story_A02_WiracodaGate_d_attackDrones

## h_story_A02_WiracodaGate_w_drones
	* StepId: 8
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A02_WiracodaGate_GAMA_8
		* h_story_A02_WiracodaGate_RequestCameraHighlightKharKaalad

## h_story_A02_WiracodaGate_w_dronesSpawn
	* StepId: 5
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A02_WiracodaGate_GAMA_5
		* h_story_A02_WiracodaGate_GAMA_6
		* h_story_A02_WiracodaGate_TriggerWaveDrones01
		* h_story_A02_WiracodaGate_preferredTargets

## h_story_A02_WiracodaGate_w_dronesWin
	* StepId: 15
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A02_WiracodaGate_GAMA_15
		* h_story_A02_WiracodaGate_camera_tormentor
		* h_story_A02_WiracodaGate_close_tormentorSequence
		* h_story_A02_WiracodaGate_wave_tormentor

## h_story_A02_WiracodaGate_w_end
	* StepId: 31
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A02_WiracodaGate_GAMA_31
		* h_story_A02_WiracodaGate_GAMA_34

## h_story_A02_WiracodaGate_w_endKeeper
	* StepId: 30
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A02_WiracodaGate_GAMA_30
		* h_story_A02_WiracodaGate_GAMA_35
		* h_story_A02_WiracodaGate_wave_endKeeper01
		* h_story_A02_WiracodaGate_wave_endKeeper02

## h_story_A02_WiracodaGate_w_endSequence
	* StepId: 32
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A02_WiracodaGate_GAMA_32
		* h_story_A02_WiracodaGate_GAMA_33
		* h_story_A02_WiracodaGate_close_endSequence
		* h_story_A02_WiracodaGate_sequence_end

## h_story_A02_WiracodaGate_w_endSequenceDialog
	* StepId: 34
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_A02_WiracodaGate_d_endSequence

## h_story_A02_WiracodaGate_w_freeBattle
	* StepId: 22
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A02_WiracodaGate_EnablePlayerGodMode
		* h_story_A02_WiracodaGate_GAMA_22
		* h_story_A02_WiracodaGate_GAMA_41
		* h_story_A02_WiracodaGate_deactivate_keeper
		* h_story_A02_WiracodaGate_wave_keeper

## h_story_A02_WiracodaGate_w_freeBattle2
	* StepId: 44
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A02_WiracodaGate_GAMA_44
		* h_story_A02_WiracodaGate_d_freeBattle

## h_story_A02_WiracodaGate_w_Haarsuk01
	* StepId: 28
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A02_WiracodaGate_GAMA_28
		* h_story_A02_WiracodaGate_GAMA_37
		* h_story_A02_WiracodaGate_armor_Haarsuk01
		* h_story_A02_WiracodaGate_health_Haarsuk01

## h_story_A02_WiracodaGate_w_Haarsuk02
	* StepId: 29
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A02_WiracodaGate_GAMA_29
		* h_story_A02_WiracodaGate_GAMA_36
		* h_story_A02_WiracodaGate_destroy_Haarsuk

## h_story_A02_WiracodaGate_w_keeperSequence01
	* StepId: 42
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A02_WiracodaGate_GAMA_42
		* h_story_A02_WiracodaGate_close_keeperSequence
		* h_story_A02_WiracodaGate_sequence_keeper

## h_story_A02_WiracodaGate_w_keeperSequence02
	* StepId: 43
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A02_WiracodaGate_StartDialogKeeper1
		* h_story_A02_WiracodaGate_wave_moreEnemies04
		* h_story_A02_WiracodaGate_wave_moreEnemies05
		* h_story_A02_WiracodaGate_wave_moreEnemies06

## h_story_A02_WiracodaGate_w_moreEnemies
	* StepId: 46
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A02_WiracodaGate_wave_moreEnemies01
		* h_story_A02_WiracodaGate_wave_moreEnemies02
		* h_story_A02_WiracodaGate_wave_moreEnemies03

## h_story_A02_WiracodaGate_w_moveBack
	* StepId: 24
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A02_WiracodaGate_GAMA_24
		* h_story_A02_WiracodaGate_d_moveBack

## h_story_A02_WiracodaGate_w_sequenceIntro
	* StepId: 2
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A02_WiracodaGate_GAMA_2
		* h_story_A02_WiracodaGate_d_intro

## h_story_A02_WiracodaGate_w_sequenceTormentor
	* StepId: 16
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A02_WiracodaGate_GAMA_16
		* h_story_A02_WiracodaGate_d_tormentor

## h_story_A02_WiracodaGate_w_skill
	* StepId: 12
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A02_WiracodaGate_GAMA_12
		* h_story_A02_WiracodaGate_GAMA_55
		* h_story_A02_WiracodaGate_d_useSkill

## h_story_A02_WiracodaGate_w_tormentor
	* StepId: 17
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A02_WiracodaGate_GAMA_17
		* h_story_A02_WiracodaGate_GAMA_49
		* h_story_A02_WiracodaGate_GAMA_50
		* h_story_A02_WiracodaGate_active_KharKaalad
		* h_story_A02_WiracodaGate_d_attackTormentor

## h_story_A02_WiracodaGate_w_tormentorWin1
	* StepId: 19
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A02_WiracodaGate_GAMA_19
		* h_story_A02_WiracodaGate_d_tormentorWin

## h_story_A02_WiracodaGate_w_tormentorWin2
	* StepId: 20
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A02_WiracodaGate_GAMA_20
		* h_story_A02_WiracodaGate_GAMA_46
		* h_story_A02_WiracodaGate_GAMA_47
		* h_story_A02_WiracodaGate_GAMA_48

## h_story_A02_WiracodaGate_w_tormentorWin3
	* StepId: 21
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A02_WiracodaGate_ActivateRiffSa02
		* h_story_A02_WiracodaGate_GAMA_21
		* h_story_A02_WiracodaGate_GAMA_43
		* h_story_A02_WiracodaGate_GAMA_45

## h_story_A03_GulfTaln_goal_pirates2
	* StepId: 26
	* Type: Goal
	* TargetType: OnTaggedUnitIsBelowHealth
	* SuccLL: 
		* h_story_A03_GulfTaln_GAMA_26
		* h_story_A03_GulfTaln_GAMA_32
		* h_story_A03_GulfTaln_d_pirates3
		* h_story_A03_GulfTaln_deactivate_attackHighlight
		* h_story_A03_GulfTaln_stopUIHighlightAttack2

## h_story_A03_GulfTaln_goal_position
	* StepId: 18
	* Type: Goal
	* TargetType: ReachPosition
	* TVS: 
		* -2000
		* 2000
	* SuccLL: 
		* h_story_A03_GulfTaln_GAMA_18
		* h_story_A03_GulfTaln_StopHightlightMoveTo
		* h_story_A03_GulfTaln_close_position
		* h_story_A03_GulfTaln_deactivate_position

## h_story_A03_GulfTaln_goal_repair
	* StepId: 9
	* Type: Goal
	* TargetType: OnTaggedUnitsHaveAmountOfArmor
	* SuccLL: 
		* h_story_A03_GulfTaln_GAMA_47
		* h_story_A03_GulfTaln_GAMA_48
		* h_story_A03_GulfTaln_GAMA_9
		* h_story_A03_GulfTaln_d_repair2
		* h_story_A03_GulfTaln_deactivate_repairHighlight
		* h_story_A03_GulfTaln_stopUI_repair

## h_story_A03_GulfTaln_goal_undockCollector
	* StepId: 7
	* Type: Goal
	* TargetType: SquadsLaunched
	* SuccLL: 
		* h_story_A03_GulfTaln_GAMA_7
		* h_story_A03_GulfTaln_StopHighlightResColUndock
		* h_story_A03_GulfTaln_close_goalRC
		* h_story_A03_GulfTaln_deactivate_undockRCHighlight

## h_story_A03_GulfTaln_goal_undockInterceptor
	* StepId: 12
	* Type: Goal
	* TargetType: FinishGoalsString
	* TVS: h_story_A03_GulfTaln_goal_undockInterceptorSub
	* SuccLL: 
		* h_story_A03_GulfTaln_GAMA_12
		* h_story_A03_GulfTaln_close_interceptor
		* h_story_A03_GulfTaln_deactivate_interceptor
		* h_story_A03_GulfTaln_stopUIHighlight

## h_story_A03_GulfTaln_goal_undockInterceptorSub
	* StepId: 46
	* Type: Trigger
	* TargetType: SquadsLaunched

## h_story_A03_GulfTaln_i_flagshipHealth
	* StepId: 55
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_story_A03_GulfTaln_SetPlayerFlagshipArmor
		* h_story_A03_GulfTaln_SetPlayerFlagshipJull

## h_story_A03_GulfTaln_i_healFleet
	* StepId: 45
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_story_A03_GulfTaln_healEscortArmor
		* h_story_A03_GulfTaln_healEscortHealth
		* h_story_A03_GulfTaln_healFlagshipArmor
		* h_story_A03_GulfTaln_healFlagshipHealth

## h_story_A03_GulfTaln_i_skillReminder
	* StepId: 35
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_story_A03_GulfTaln_GAMA_35
		* h_story_A03_GulfTaln_GAMA_38

## h_story_A03_GulfTaln_i_uiSetup
	* StepId: 56
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_story_A03_GulfTaln_addUI_showLogs
		* h_story_A03_GulfTaln_addUI_tutorialHUD

## h_story_A03_GulfTaln_Start
	* StepId: 0
	* Type: Trigger
	* TargetType: MissionStart
	* SuccLL: 
		* h_story_A03_GulfTaln_GAMA_0
		* h_story_A03_GulfTaln_GAMA_53
		* h_story_A03_GulfTaln_GAMA_54
		* h_story_A03_GulfTaln_GAMA_55
		* h_story_A03_GulfTaln_ShowIntroSequence01

## h_story_A03_GulfTaln_t_d_pirates
	* StepId: 27
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: story_GulfTaln_escape_dialog
	* SuccLL: h_story_A03_GulfTaln_GAMA_27

## h_story_A03_GulfTaln_t_dialogOrTime
	* StepId: 10
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* h_story_A03_GulfTaln_td_repairStarted
		* h_story_A03_GulfTaln_w_3
	* SuccLL: h_story_A03_GulfTaln_GAMA_10

## h_story_A03_GulfTaln_t_health
	* StepId: 36
	* Type: Trigger
	* TargetType: OnTaggedUnitIsBelowHealth
	* SuccLL: 
		* h_story_A03_GulfTaln_GAMA_36
		* h_story_A03_GulfTaln_GAMA_37
		* h_story_A03_GulfTaln_d_useSkill
		* h_story_A03_GulfTaln_deactivate_attackHighlight2
		* h_story_A03_GulfTaln_stopUIHighlightAttack

## h_story_A03_GulfTaln_t_useSkill
	* StepId: 39
	* Type: Trigger
	* TargetType: UseSkill
	* SuccLL: h_story_A03_GulfTaln_deactivateSkillGoal

## h_story_A03_GulfTaln_t_useSkill2
	* StepId: 37
	* Type: Trigger
	* TargetType: UseSkill
	* SuccLL: 
		* h_story_A03_GulfTaln_close_skill
		* h_story_A03_GulfTaln_desctivate_skill
		* h_story_A03_GulfTaln_stopUI_skill

## h_story_A03_GulfTaln_td_conclusion
	* StepId: 31
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: story_GulfTaln_conclusion_dialog
	* SuccLL: h_story_A03_GulfTaln_GAMA_31

## h_story_A03_GulfTaln_td_help
	* StepId: 34
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: story_GulfTaln_help_dialog
	* SuccLL: h_story_A03_GulfTaln_UIHighlightAttack

## h_story_A03_GulfTaln_td_moveToPosition
	* StepId: 43
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: story_GulfTaln_move_dialog
	* SuccLL: h_story_A03_GulfTaln_HightlightMoveTo

## h_story_A03_GulfTaln_td_pirates2
	* StepId: 24
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: story_GulfTaln_pirates2_dialog
	* SuccLL: h_story_A03_GulfTaln_GAMA_24

## h_story_A03_GulfTaln_td_repair
	* StepId: 50
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: story_GulfTaln_repair_dialog
	* SuccLL: h_story_A03_GulfTaln_HighlightRepairFrigate

## h_story_A03_GulfTaln_td_repairStarted
	* StepId: 49
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: story_GulfTaln_repairStarted_dialog

## h_story_A03_GulfTaln_td_stranger2
	* StepId: 15
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: story_GulfTaln_stranger_dialog
	* SuccLL: h_story_A03_GulfTaln_GAMA_15

## h_story_A03_GulfTaln_td_undockInterceptor
	* StepId: 47
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: story_GulfTaln_undockInterceptor_dialog
	* SuccLL: h_story_A03_GulfTaln_highlight_undockInterceptor

## h_story_A03_GulfTaln_td_useSkill
	* StepId: 38
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: story_GulfTaln_skill_dialog
	* SuccLL: h_story_A03_GulfTaln_UIHighlightSkill

## h_story_A03_GulfTaln_TriggerWaitForAcropolisDialogDone
	* StepId: 51
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: story_GulfTaln_undockRC_dialog
	* SuccLL: h_story_A03_GulfTaln_HighlightResColUndock

## h_story_A03_GulfTaln_TriggerWaitForDialogIntro2
	* StepId: 3
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: story_GulfTaln_intro_dialog
	* SuccLL: h_story_A03_GulfTaln_GAMA_3

## h_story_A03_GulfTaln_TriggerWaitForIntroSequenceDone
	* StepId: 1
	* Type: Trigger
	* TargetType: OnInGameSequenceFinishedForPlayer
	* TVS: 1
	* SuccLL: 
		* h_story_A03_GulfTaln_GAMA_1
		* h_story_A03_GulfTaln_bded5f6751f543d4da8e11385dbfcdcb
		* h_story_A03_GulfTaln_deactivate_introSequenceDialog
		* h_story_A03_GulfTaln_deavtivatePlayerShips

## h_story_A03_GulfTaln_TriggerWaitForTheGift1DialogDone
	* StepId: 29
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: story_GulfTaln_farewell_dialog
	* SuccLL: 
		* h_story_A03_GulfTaln_GAMA_29
		* h_story_A03_GulfTaln_RemoveTr1Freighter01

## h_story_A03_GulfTaln_TriggerWaitTimer00
	* StepId: 2
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A03_GulfTaln_GAMA_2
		* h_story_A03_GulfTaln_StartDialogIntro2

## h_story_A03_GulfTaln_TriggerWaitTimer06
	* StepId: 21
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A03_GulfTaln_GAMA_21
		* h_story_A03_GulfTaln_GAMA_41
		* h_story_A03_GulfTaln_HighlightShowCangacianSpawns

## h_story_A03_GulfTaln_TriggerWaitTimer06b
	* StepId: 19
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A03_GulfTaln_GAMA_19
		* h_story_A03_GulfTaln_StartDialogThePirates1

## h_story_A03_GulfTaln_TriggerWaitTimer08
	* StepId: 30
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A03_GulfTaln_GAMA_30
		* h_story_A03_GulfTaln_d_conclusion

## h_story_A03_GulfTaln_w_2
	* StepId: 22
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A03_GulfTaln_GAMA_22
		* h_story_A03_GulfTaln_d_pirates

## h_story_A03_GulfTaln_w_3
	* StepId: 48
	* Type: Trigger
	* TargetType: WaitForTime

## h_story_A03_GulfTaln_w_5
	* StepId: 28
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A03_GulfTaln_GAMA_28
		* h_story_A03_GulfTaln_StartDialogTheGift1

## h_story_A03_GulfTaln_w_6
	* StepId: 4
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A03_GulfTaln_GAMA_4
		* h_story_A03_GulfTaln_GAMA_51
		* h_story_A03_GulfTaln_ShowHighlightAcropolisSpawn

## h_story_A03_GulfTaln_w_7
	* StepId: 8
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A03_GulfTaln_GAMA_49
		* h_story_A03_GulfTaln_GAMA_8
		* h_story_A03_GulfTaln_d_repair

## h_story_A03_GulfTaln_w_8
	* StepId: 25
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A03_GulfTaln_GAMA_25
		* h_story_A03_GulfTaln_GAMA_33
		* h_story_A03_GulfTaln_GAMA_34
		* h_story_A03_GulfTaln_GAMA_39
		* h_story_A03_GulfTaln_GAMA_40
		* h_story_A03_GulfTaln_d_help

## h_story_A03_GulfTaln_w_fin
	* StepId: 32
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A03_GulfTaln_fin
		* h_story_A03_GulfTaln_removeUI_showLogs
		* h_story_A03_GulfTaln_removeUI_tutorialHUD

## h_story_A03_GulfTaln_w_frigateCamera
	* StepId: 6
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A03_GulfTaln_GAMA_50
		* h_story_A03_GulfTaln_GAMA_6
		* h_story_A03_GulfTaln_GivePlayerResCol01
		* h_story_A03_GulfTaln_StartDialogSplint1
		* h_story_A03_GulfTaln_activatePlayerShips

## h_story_A03_GulfTaln_w_frigateDialog
	* StepId: 5
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A03_GulfTaln_GAMA_5
		* h_story_A03_GulfTaln_StartDialogIntro4

## h_story_A03_GulfTaln_w_frigateHealth
	* StepId: 53
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A03_GulfTaln_SetAcropolisArmor01
		* h_story_A03_GulfTaln_SetAcropolisHull01

## h_story_A03_GulfTaln_w_introDialog
	* StepId: 54
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_A03_GulfTaln_StartDialogIntro1

## h_story_A03_GulfTaln_w_pirates
	* StepId: 23
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A03_GulfTaln_GAMA_23
		* h_story_A03_GulfTaln_d_pirates2

## h_story_A03_GulfTaln_w_pirateSpawn
	* StepId: 42
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A03_GulfTaln_DeactivateCangacians
		* h_story_A03_GulfTaln_DeactivatePlayer
		* h_story_A03_GulfTaln_InvincibleCangacianCommandShip
		* h_story_A03_GulfTaln_SetCangacianTargetToPlayerFlagship
		* h_story_A03_GulfTaln_SpawnCangacianCommandShip

## h_story_A03_GulfTaln_w_removePirate
	* StepId: 33
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_A03_GulfTaln_remove_PirateCommandShip

## h_story_A03_GulfTaln_w_repair
	* StepId: 11
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A03_GulfTaln_GAMA_11
		* h_story_A03_GulfTaln_GAMA_45
		* h_story_A03_GulfTaln_GAMA_46
		* h_story_A03_GulfTaln_GivePlayerInterceptor01
		* h_story_A03_GulfTaln_d_undockInterceptor

## h_story_A03_GulfTaln_w_setPirateActive
	* StepId: 40
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_A03_GulfTaln_ActivateCangacians

## h_story_A03_GulfTaln_w_setPlayerActive
	* StepId: 41
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_A03_GulfTaln_ActivatePlayer

## h_story_A03_GulfTaln_w_spawnFrigate
	* StepId: 52
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A03_GulfTaln_GAMA_52
		* h_story_A03_GulfTaln_GiveAcropolisToPlayer

## h_story_A03_GulfTaln_w_spawnTrader
	* StepId: 44
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A03_GulfTaln_DeactivateFreighter01
		* h_story_A03_GulfTaln_GAMA_44
		* h_story_A03_GulfTaln_SpawnTr1Freighter

## h_story_A03_GulfTaln_w_traderCamera
	* StepId: 17
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A03_GulfTaln_GAMA_17
		* h_story_A03_GulfTaln_GAMA_42
		* h_story_A03_GulfTaln_d_moveToPosition

## h_story_A03_GulfTaln_w_traderCameraIntro
	* StepId: 14
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A03_GulfTaln_GAMA_14
		* h_story_A03_GulfTaln_GAMA_16
		* h_story_A03_GulfTaln_d_stranger

## h_story_A03_GulfTaln_w_traderDialog
	* StepId: 16
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_A03_GulfTaln_d_trader2

## h_story_A03_GulfTaln_w_transition
	* StepId: 13
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A03_GulfTaln_GAMA_13
		* h_story_A03_GulfTaln_GAMA_43
		* h_story_A03_GulfTaln_ShowHighlightTraderSpawn

## h_story_A03_GulfTaln_WaitForBussines
	* StepId: 20
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: story_GulfTaln_exchange_dialog
	* SuccLL: h_story_A03_GulfTaln_GAMA_20

## h_story_A04_RelicSignature_goal_deployRC
	* StepId: 16
	* Type: Goal
	* TargetType: ResourceCollectorsLaunched
	* SuccLL: 
		* h_story_A04_RelicSignature_GAMA_16
		* h_story_A04_RelicSignature_a7dd19c53a7c7cf44bdaad6ff15e2ab7

## h_story_A04_RelicSignature_goal_kill
	* StepId: 4
	* Type: Goal
	* TargetType: KillSpecificWave
	* SuccLL: 
		* h_story_A04_RelicSignature_GAMA_4
		* h_story_A04_RelicSignature_close_combat

## h_story_A04_RelicSignature_goal_relic
	* StepId: 12
	* Type: Goal
	* TargetType: OnInteractionDone
	* TVS: relic_kpr_pickup_t0
	* SuccLL: h_story_A04_RelicSignature_deactivate_relic

## h_story_A04_RelicSignature_goal_relic2
	* StepId: 18
	* Type: Goal
	* TargetType: OnInteractionDone
	* TVS: relic_kpr_pickup_t0
	* SuccLL: h_story_A04_RelicSignature_deactivate_relic2

## h_story_A04_RelicSignature_goal_signals
	* StepId: 2
	* Type: Goal
	* TargetType: OnPlayerAttackNPC
	* SuccLL: 
		* h_story_A04_RelicSignature_GAMA_2
		* h_story_A04_RelicSignature_close_intro
		* h_story_A04_RelicSignature_deactivate_intro
		* h_story_A04_RelicSignature_stopUI_intro

## h_story_A04_RelicSignature_multi_relicPickup
	* StepId: 6
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* h_story_A04_RelicSignature_goal_relic
		* h_story_A04_RelicSignature_goal_relic2
	* SuccLL: 
		* h_story_A04_RelicSignature_GAMA_6
		* h_story_A04_RelicSignature_close_collect
		* h_story_A04_RelicSignature_stopUI_collect

## h_story_A04_RelicSignature_resColCheck
	* StepId: 10
	* Type: Trigger
	* TargetType: ResourceCollectorsLaunched
	* SuccLL: 
		* h_story_A04_RelicSignature_GAMA_10
		* h_story_A04_RelicSignature_GAMA_13

## h_story_A04_RelicSignature_Start
	* StepId: 0
	* Type: Trigger
	* TargetType: MissionStart
	* SuccLL: 
		* h_story_A04_RelicSignature_GAMA_0
		* h_story_A04_RelicSignature_GAMA_20
		* h_story_A04_RelicSignature_wave_protectors

## h_story_A04_RelicSignature_td_collectorLaunched
	* StepId: 19
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: story_Relic_collectorLaunched_dialog
	* SuccLL: h_story_A04_RelicSignature_ui_collect2

## h_story_A04_RelicSignature_td_end
	* StepId: 8
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: story_Relic_end_dialog
	* SuccLL: h_story_A04_RelicSignature_fin

## h_story_A04_RelicSignature_td_intro
	* StepId: 20
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: story_Relic_intro_dialog
	* SuccLL: h_story_A04_RelicSignature_ui_dragMove

## h_story_A04_RelicSignature_td_relic
	* StepId: 13
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: story_Relic_relic_dialog
	* SuccLL: h_story_A04_RelicSignature_ui_collect

## h_story_A04_RelicSignature_w_collectorLaunched
	* StepId: 17
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A04_RelicSignature_GAMA_17
		* h_story_A04_RelicSignature_GAMA_18
		* h_story_A04_RelicSignature_d_collectorLaunched

## h_story_A04_RelicSignature_w_combat
	* StepId: 3
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A04_RelicSignature_GAMA_3
		* h_story_A04_RelicSignature_d_combat

## h_story_A04_RelicSignature_w_deactivateResColCheck
	* StepId: 14
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_A04_RelicSignature_deactivate_ResColCheck

## h_story_A04_RelicSignature_w_intro
	* StepId: 1
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A04_RelicSignature_GAMA_1
		* h_story_A04_RelicSignature_GAMA_19
		* h_story_A04_RelicSignature_d_intro

## h_story_A04_RelicSignature_w_intro2
	* StepId: 21
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_A04_RelicSignature_lookAt

## h_story_A04_RelicSignature_w_relic
	* StepId: 5
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_story_A04_RelicSignature_GAMA_14
		* h_story_A04_RelicSignature_GAMA_5
		* h_story_A04_RelicSignature_GAMA_8
		* h_story_A04_RelicSignature_GAMA_9

## h_story_A04_RelicSignature_w_relic2
	* StepId: 11
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A04_RelicSignature_GAMA_11
		* h_story_A04_RelicSignature_GAMA_12
		* h_story_A04_RelicSignature_d_relic

## h_story_A04_RelicSignature_w_relicPickup
	* StepId: 7
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A04_RelicSignature_GAMA_7
		* h_story_A04_RelicSignature_d_end

## h_story_A04_RelicSignature_w_resColCheck
	* StepId: 15
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A04_RelicSignature_GAMA_15
		* h_story_A04_RelicSignature_d_collectorMissing
		* h_story_A04_RelicSignature_deactivate_ResColCheck2

## h_story_A04_RelicSignature_w_spawnRelic
	* StepId: 9
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_A04_RelicSignature_interaction_relic

## h_story_A05_Jolja_belowStrength_waveA
	* StepId: 23
	* Type: Trigger
	* TargetType: TaggedUnitsBelowStrength
	* SuccLL: 
		* h_story_A05_Jolja_GAMA_23
		* h_story_A05_Jolja_GAMA_24
		* h_story_A05_Jolja_d_waveB
		* h_story_A05_Jolja_wave2

## h_story_A05_Jolja_belowStrength_waveAB
	* StepId: 26
	* Type: Trigger
	* TargetType: TaggedUnitsBelowStrength
	* SuccLL: 
		* h_story_A05_Jolja_GAMA_26
		* h_story_A05_Jolja_close
		* h_story_A05_Jolja_highlight_allySpawn
		* h_story_A05_Jolja_invincible_Player

## h_story_A05_Jolja_closeSensor
	* StepId: 38
	* Type: Trigger
	* TargetType: OnSensorManagerViewHasState

## h_story_A05_Jolja_closeSensorCheck
	* StepId: 35
	* Type: Trigger
	* TargetType: OnSensorManagerViewHasState
	* SuccLL: h_story_A05_Jolja_GAMA_35

## h_story_A05_Jolja_goal_kill
	* StepId: 16
	* Type: Goal
	* TargetType: FinishGoalsString
	* TVS: h_story_A05_Jolja_killBothWaves
	* SuccLL: h_story_A05_Jolja_GAMA_16

## h_story_A05_Jolja_goal_position1
	* StepId: 8
	* Type: Goal
	* TargetType: ReachPointOfInterest
	* SuccLL: h_story_A05_Jolja_GAMA_8

## h_story_A05_Jolja_goal_position2
	* StepId: 12
	* Type: Goal
	* TargetType: ReachPointOfInterest
	* SuccLL: h_story_A05_Jolja_GAMA_12

## h_story_A05_Jolja_goal_sensor
	* StepId: 3
	* Type: Goal
	* TargetType: FinishGoalsString
	* TVS: h_story_A05_Jolja_openSensor
	* SuccLL: 
		* h_story_A05_Jolja_GAMA_3
		* h_story_A05_Jolja_close_openSensor
		* h_story_A05_Jolja_deactivate_openSensor
		* h_story_A05_Jolja_stopUI_openSensor

## h_story_A05_Jolja_goal_sensor2
	* StepId: 6
	* Type: Goal
	* TargetType: FinishGoalsString
	* TVS: h_story_A05_Jolja_closeSensor
	* SuccLL: h_story_A05_Jolja_GAMA_6

## h_story_A05_Jolja_goal_terminalATimer
	* StepId: 10
	* Type: Goal
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A05_Jolja_GAMA_10
		* h_story_A05_Jolja_close_timerA

## h_story_A05_Jolja_goal_terminalBTimer
	* StepId: 14
	* Type: Goal
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A05_Jolja_GAMA_14
		* h_story_A05_Jolja_close_TimerB

## h_story_A05_Jolja_kill_wave1
	* StepId: 22
	* Type: Trigger
	* TargetType: KillSpecificWave

## h_story_A05_Jolja_kill_wave2
	* StepId: 24
	* Type: Trigger
	* TargetType: KillSpecificWave

## h_story_A05_Jolja_killBothWaves
	* StepId: 21
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* h_story_A05_Jolja_kill_wave1
		* h_story_A05_Jolja_kill_wave2

## h_story_A05_Jolja_openSensor
	* StepId: 45
	* Type: Trigger
	* TargetType: OnSensorManagerViewHasState

## h_story_A05_Jolja_openSensorCheck
	* StepId: 41
	* Type: Trigger
	* TargetType: OnSensorManagerViewHasState
	* SuccLL: h_story_A05_Jolja_GAMA_41

## h_story_A05_Jolja_sensorPreCheck
	* StepId: 43
	* Type: Trigger
	* TargetType: OnSensorManagerViewHasState
	* SuccLL: h_story_A05_Jolja_ui_sensorManager

## h_story_A05_Jolja_sensorPreCheck2
	* StepId: 34
	* Type: Trigger
	* TargetType: OnSensorManagerViewHasState
	* SuccLL: h_story_A05_Jolja_ui_SensorManager2

## h_story_A05_Jolja_st_2_1_waitIntro
	* StepId: 1
	* Type: Trigger
	* TargetType: OnInGameSequenceFinishedForPlayer
	* TVS: 1
	* SuccLL: 
		* h_story_A05_Jolja_GAMA_1
		* h_story_A05_Jolja_GAMA_46
		* h_story_A05_Jolja_close_intro
		* h_story_A05_Jolja_deactivate_introDialog

## h_story_A05_Jolja_Start
	* StepId: 0
	* Type: Trigger
	* TargetType: MissionStart
	* SuccLL: 
		* h_story_A05_Jolja_GAMA_0
		* h_story_A05_Jolja_GAMA_47
		* h_story_A05_Jolja_sequence_Intro

## h_story_A05_Jolja_td_closeSensor
	* StepId: 33
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: story_Jolja_closeSensor_dialog
	* SuccLL: 
		* h_story_A05_Jolja_GAMA_33
		* h_story_A05_Jolja_GAMA_34

## h_story_A05_Jolja_td_openSensor
	* StepId: 40
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: story_Jolja_openSensor_dialog
	* SuccLL: 
		* h_story_A05_Jolja_GAMA_40
		* h_story_A05_Jolja_GAMA_42

## h_story_A05_Jolja_td_resolution
	* StepId: 20
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: story_Jolja_resolution_dialog
	* SuccLL: h_story_A05_Jolja_st_2_1_act_fin

## h_story_A05_Jolja_td_signatures
	* StepId: 5
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: story_Jolja_signatures_dialog
	* SuccLL: 
		* h_story_A05_Jolja_GAMA_32
		* h_story_A05_Jolja_GAMA_36
		* h_story_A05_Jolja_GAMA_38
		* h_story_A05_Jolja_GAMA_5
		* h_story_A05_Jolja_d_closeSensor

## h_story_A05_Jolja_td_tepin
	* StepId: 18
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: story_Jolja_tepin_dialog
	* SuccLL: 
		* h_story_A05_Jolja_GAMA_18
		* h_story_A05_Jolja_remove_ally

## h_story_A05_Jolja_unlockTrigger_closeSensor
	* StepId: 37
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* h_story_A05_Jolja_td_closeSensor
		* h_story_A05_Jolja_w_closeSensorDelay
	* SuccLL: h_story_A05_Jolja_GAMA_37

## h_story_A05_Jolja_unlockTrigger_openSensor
	* StepId: 44
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* h_story_A05_Jolja_td_openSensor
		* h_story_A05_Jolja_w_openSensorDelay
	* SuccLL: h_story_A05_Jolja_GAMA_44

## h_story_A05_Jolja_w_3
	* StepId: 27
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A05_Jolja_GAMA_27
		* h_story_A05_Jolja_d_ally

## h_story_A05_Jolja_w_4
	* StepId: 17
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A05_Jolja_GAMA_17
		* h_story_A05_Jolja_d_tepin

## h_story_A05_Jolja_w_ally
	* StepId: 29
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A05_Jolja_GAMA_29
		* h_story_A05_Jolja_disable_Ally

## h_story_A05_Jolja_w_ally2
	* StepId: 30
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A05_Jolja_GAMA_30
		* h_story_A05_Jolja_enable_Ally

## h_story_A05_Jolja_w_allySpawn
	* StepId: 28
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A05_Jolja_GAMA_28
		* h_story_A05_Jolja_ally0

## h_story_A05_Jolja_w_attackAlly
	* StepId: 32
	* Type: Trigger
	* TargetType: WaitForTime

## h_story_A05_Jolja_w_closeSensor
	* StepId: 36
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_A05_Jolja_desctivateSensorCheck2

## h_story_A05_Jolja_w_closeSensorDelay
	* StepId: 39
	* Type: Trigger
	* TargetType: WaitForTime

## h_story_A05_Jolja_w_healthCheck2
	* StepId: 25
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_A05_Jolja_GAMA_25

## h_story_A05_Jolja_w_intro
	* StepId: 48
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_A05_Jolja_d_introSequence

## h_story_A05_Jolja_w_intro2
	* StepId: 47
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A05_Jolja_lookAt_intro
		* h_story_A05_Jolja_setActive_disablePlayerFleet
		* h_story_A05_Jolja_wave0

## h_story_A05_Jolja_w_intro3
	* StepId: 2
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A05_Jolja_GAMA_2
		* h_story_A05_Jolja_GAMA_39
		* h_story_A05_Jolja_GAMA_43
		* h_story_A05_Jolja_GAMA_45
		* h_story_A05_Jolja_d_openSensor

## h_story_A05_Jolja_w_invincivlePlayer
	* StepId: 31
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A05_Jolja_GAMA_31
		* h_story_A05_Jolja_invincivle_offPlayer

## h_story_A05_Jolja_w_openSensor
	* StepId: 42
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_A05_Jolja_deactivate_sensorPreCheck

## h_story_A05_Jolja_w_openSensorDelay
	* StepId: 46
	* Type: Trigger
	* TargetType: WaitForTime

## h_story_A05_Jolja_w_resolution
	* StepId: 19
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A05_Jolja_GAMA_19
		* h_story_A05_Jolja_d_resolution

## h_story_A05_Jolja_w_signatures
	* StepId: 4
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A05_Jolja_GAMA_4
		* h_story_A05_Jolja_d_signatures

## h_story_A05_Jolja_w_terminalA1
	* StepId: 9
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A05_Jolja_GAMA_9
		* h_story_A05_Jolja_d_terminalATimer

## h_story_A05_Jolja_w_terminalA2
	* StepId: 11
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A05_Jolja_GAMA_11
		* h_story_A05_Jolja_d_terminalB
		* h_story_A05_Jolja_lookAt_terminalB

## h_story_A05_Jolja_w_terminalA3
	* StepId: 7
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A05_Jolja_GAMA_7
		* h_story_A05_Jolja_d_terminalA
		* h_story_A05_Jolja_deactivate_fakePosition
		* h_story_A05_Jolja_lookAt_Position
		* h_story_A05_Jolja_setActive_activatePlayerFleet

## h_story_A05_Jolja_w_terminalB1
	* StepId: 13
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A05_Jolja_GAMA_13
		* h_story_A05_Jolja_d_terminalBTimer

## h_story_A05_Jolja_w_terminalB2
	* StepId: 15
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_A05_Jolja_GAMA_15
		* h_story_A05_Jolja_GAMA_20
		* h_story_A05_Jolja_GAMA_21
		* h_story_A05_Jolja_GAMA_22
		* h_story_A05_Jolja_d_waveA
		* h_story_A05_Jolja_wave1

## h_story_B01_CombatTrials_goal_destroy
	* StepId: 12
	* Type: Goal
	* TargetType: FinishGoalsString
	* TVS: h_story_B01_CombatTrials_kill0
	* SuccLL: 
		* h_story_B01_CombatTrials_8925d17f2b53d72418d7316b9b67bfe1
		* h_story_B01_CombatTrials_GAMA_12

## h_story_B01_CombatTrials_goal_position
	* StepId: 9
	* Type: Goal
	* TargetType: FinishGoalsString
	* TVS: h_story_B01_CombatTrials_t_reach
	* SuccLL: 
		* h_story_B01_CombatTrials_GAMA_9
		* h_story_B01_CombatTrials_d_tut

## h_story_B01_CombatTrials_goal_time
	* StepId: 18
	* Type: Goal
	* TargetType: Countdown
	* FailLL: h_story_B01_CombatTrials_GAMA_18

## h_story_B01_CombatTrials_goal_wave
	* StepId: 15
	* Type: Goal
	* TargetType: FinishGoalsString
	* TVS: h_story_B01_CombatTrials_kill1
	* SuccLL: h_story_B01_CombatTrials_GAMA_15

## h_story_B01_CombatTrials_i_setup
	* StepId: 4
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_story_B01_CombatTrials_deactivate_playerEscorts
		* h_story_B01_CombatTrials_deactivate_playerFlagship
		* h_story_B01_CombatTrials_deactivate_targets
		* h_story_B01_CombatTrials_spawn_outpost
		* h_story_B01_CombatTrials_spawn_targets

## h_story_B01_CombatTrials_kill0
	* StepId: 3
	* Type: Trigger
	* TargetType: KillSpecificWave

## h_story_B01_CombatTrials_kill1
	* StepId: 17
	* Type: Trigger
	* TargetType: KillSpecificWave

## h_story_B01_CombatTrials_start
	* StepId: 0
	* Type: Trigger
	* TargetType: MissionStart
	* SuccLL: 
		* h_story_B01_CombatTrials_GAMA_0
		* h_story_B01_CombatTrials_GAMA_1
		* h_story_B01_CombatTrials_GAMA_2
		* h_story_B01_CombatTrials_GAMA_20
		* h_story_B01_CombatTrials_GAMA_3
		* h_story_B01_CombatTrials_GAMA_4

## h_story_B01_CombatTrials_t_d_destroy
	* StepId: 14
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: s_shakedown_destroy_1_dialog
	* SuccLL: 
		* h_story_B01_CombatTrials_GAMA_14
		* h_story_B01_CombatTrials_GAMA_16
		* h_story_B01_CombatTrials_activateUnits
		* h_story_B01_CombatTrials_aiBehavior
		* h_story_B01_CombatTrials_d_wave
		* h_story_B01_CombatTrials_sensorView
		* h_story_B01_CombatTrials_wave1

## h_story_B01_CombatTrials_t_reach
	* StepId: 20
	* Type: Trigger
	* TargetType: ReachPosition
	* TVS: 
		* 1800
		* 1800

## h_story_B01_CombatTrials_td_fail
	* StepId: 2
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: s_shakedown_fail_1_dialog
	* SuccLL: h_story_B01_CombatTrials_fail

## h_story_B01_CombatTrials_td_fin
	* StepId: 1
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: s_shakedown_fin_1_dialog
	* SuccLL: h_story_B01_CombatTrials_fin

## h_story_B01_CombatTrials_td_intro1
	* StepId: 6
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: s_shakedown_intro_1_dialog
	* SuccLL: 
		* h_story_B01_CombatTrials_GAMA_6
		* h_story_B01_CombatTrials_d_intro2

## h_story_B01_CombatTrials_td_intro2
	* StepId: 7
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: s_shakedown_intro_2_dialog
	* SuccLL: 
		* h_story_B01_CombatTrials_GAMA_7
		* h_story_B01_CombatTrials_d_intro3

## h_story_B01_CombatTrials_td_intro3
	* StepId: 8
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: s_shakedown_intro_3_dialog
	* SuccLL: 
		* h_story_B01_CombatTrials_GAMA_19
		* h_story_B01_CombatTrials_GAMA_8
		* h_story_B01_CombatTrials_uiHighlightSwipe

## h_story_B01_CombatTrials_td_tut
	* StepId: 10
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: s_shakedown_tut_1_dialog
	* SuccLL: 
		* h_story_B01_CombatTrials_GAMA_10
		* h_story_B01_CombatTrials_d_tut2

## h_story_B01_CombatTrials_td_tut2
	* StepId: 11
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: s_shakedown_tut_2_dialog
	* SuccLL: 
		* h_story_B01_CombatTrials_GAMA_11
		* h_story_B01_CombatTrials_GAMA_17
		* h_story_B01_CombatTrials_activate_targets

## h_story_B01_CombatTrials_w_0
	* StepId: 13
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_B01_CombatTrials_GAMA_13
		* h_story_B01_CombatTrials_d_destroy
		* h_story_B01_CombatTrials_lineOfSight

## h_story_B01_CombatTrials_w_2
	* StepId: 19
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_B01_CombatTrials_d_fail

## h_story_B01_CombatTrials_w_4
	* StepId: 16
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_B01_CombatTrials_d_fin

## h_story_B01_CombatTrials_w_intro
	* StepId: 5
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_B01_CombatTrials_GAMA_5
		* h_story_B01_CombatTrials_d_intro1
		* h_story_B01_CombatTrials_deactivate_targets2

## h_story_B01_CombatTrials_w_lookAt
	* StepId: 21
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_B01_CombatTrials_lookAt_targets

## h_story_B02_MeropisDefense_allyKilled1
	* StepId: 3
	* Type: Trigger
	* TargetType: OnTaggedUnitKilled

## h_story_B02_MeropisDefense_allyKilled2
	* StepId: 4
	* Type: Trigger
	* TargetType: OnTaggedUnitKilled

## h_story_B02_MeropisDefense_fakepos1
	* StepId: 22
	* Type: Trigger
	* TargetType: ReachPosition
	* TVS: 
		* -4890
		* 6740

## h_story_B02_MeropisDefense_fakepos2
	* StepId: 23
	* Type: Trigger
	* TargetType: ReachPosition
	* TVS: 
		* -2260
		* 8710

## h_story_B02_MeropisDefense_goal_destroy
	* StepId: 15
	* Type: Goal
	* TargetType: FinishGoalsString
	* TVS: 
		* h_story_B02_MeropisDefense_kill0
		* h_story_B02_MeropisDefense_kill1
	* SuccLL: h_story_B02_MeropisDefense_GAMA_15

## h_story_B02_MeropisDefense_goal_position
	* StepId: 13
	* Type: Goal
	* TargetType: FinishGoalsString
	* TVS: h_story_B02_MeropisDefense_t_pos_2
	* SuccLL: h_story_B02_MeropisDefense_GAMA_13

## h_story_B02_MeropisDefense_i_0
	* StepId: 2
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_story_B02_MeropisDefense_GAMA_2
		* h_story_B02_MeropisDefense_GAMA_3
		* h_story_B02_MeropisDefense_GAMA_4
		* h_story_B02_MeropisDefense_sp_ally1
		* h_story_B02_MeropisDefense_sp_ally2
		* h_story_B02_MeropisDefense_sp_ally3

## h_story_B02_MeropisDefense_kill0
	* StepId: 17
	* Type: Trigger
	* TargetType: KillSpecificWave

## h_story_B02_MeropisDefense_kill1
	* StepId: 18
	* Type: Trigger
	* TargetType: KillSpecificWave

## h_story_B02_MeropisDefense_missionStart
	* StepId: 0
	* Type: Trigger
	* TargetType: MissionStart
	* SuccLL: 
		* h_story_B02_MeropisDefense_53595280a0643c7478e14f5a565444d0
		* h_story_B02_MeropisDefense_GAMA_0
		* h_story_B02_MeropisDefense_GAMA_1
		* h_story_B02_MeropisDefense_GAMA_9

## h_story_B02_MeropisDefense_multi_fail
	* StepId: 7
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* h_story_B02_MeropisDefense_t_d_dail
		* h_story_B02_MeropisDefense_w_fail
	* SuccLL: h_story_B02_MeropisDefense_fail

## h_story_B02_MeropisDefense_t_d_dail
	* StepId: 9
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: s_meropis_fail_1_dialog

## h_story_B02_MeropisDefense_t_d_fin
	* StepId: 1
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: s_meropis_finish_1_dialog
	* SuccLL: h_story_B02_MeropisDefense_fin

## h_story_B02_MeropisDefense_t_d_group1temp
	* StepId: 12
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: s_meropis_group_1_dialog
	* SuccLL: 
		* h_story_B02_MeropisDefense_GAMA_12
		* h_story_B02_MeropisDefense_GAMA_18
		* h_story_B02_MeropisDefense_GAMA_21
		* h_story_B02_MeropisDefense_GAMA_22
		* h_story_B02_MeropisDefense_d_group3

## h_story_B02_MeropisDefense_t_d_intro
	* StepId: 11
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: s_meropis_intro_1_dialog
	* SuccLL: 
		* h_story_B02_MeropisDefense_GAMA_11
		* h_story_B02_MeropisDefense_d_group1temp

## h_story_B02_MeropisDefense_t_fail
	* StepId: 5
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* h_story_B02_MeropisDefense_allyKilled1
		* h_story_B02_MeropisDefense_allyKilled2
	* SuccLL: h_story_B02_MeropisDefense_GAMA_5

## h_story_B02_MeropisDefense_t_pos_1
	* StepId: 19
	* Type: TriggerRepeating
	* TargetType: ReachPosition
	* TVS: 
		* -4890
		* 6740
	* SuccLL: 
		* h_story_B02_MeropisDefense_GAMA_19
		* h_story_B02_MeropisDefense_GAMA_20

## h_story_B02_MeropisDefense_t_pos_2
	* StepId: 21
	* Type: Trigger
	* TargetType: ReachPosition
	* TVS: 
		* -2260
		* 8710
	* SuccLL: h_story_B02_MeropisDefense_deactivate2

## h_story_B02_MeropisDefense_w_0
	* StepId: 20
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_B02_MeropisDefense_deactivate1

## h_story_B02_MeropisDefense_w_1
	* StepId: 14
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_B02_MeropisDefense_GAMA_14
		* h_story_B02_MeropisDefense_GAMA_16
		* h_story_B02_MeropisDefense_GAMA_17
		* h_story_B02_MeropisDefense_d_test
		* h_story_B02_MeropisDefense_wave0
		* h_story_B02_MeropisDefense_wave1

## h_story_B02_MeropisDefense_w_2
	* StepId: 6
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_B02_MeropisDefense_GAMA_6
		* h_story_B02_MeropisDefense_GAMA_7
		* h_story_B02_MeropisDefense_GAMA_8
		* h_story_B02_MeropisDefense_d_fail

## h_story_B02_MeropisDefense_w_3
	* StepId: 10
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_B02_MeropisDefense_GAMA_10
		* h_story_B02_MeropisDefense_d_intro

## h_story_B02_MeropisDefense_w_4
	* StepId: 16
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_B02_MeropisDefense_d_fin

## h_story_B02_MeropisDefense_w_fail
	* StepId: 8
	* Type: Trigger
	* TargetType: WaitForTime

## h_story_B03_ThePool_6723a688f4f46b64ba426786a78c409f
	* StepId: 16
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: s_pool_destroy_1_dialog
	* SuccLL: 
		* h_story_B03_ThePool_GAMA_4
		* h_story_B03_ThePool_tw6

## h_story_B03_ThePool_closeKin1
	* StepId: 8
	* Type: Trigger
	* TargetType: ReachPosition
	* TVS: 
		* -2500
		* -5700

## h_story_B03_ThePool_closeKin2
	* StepId: 9
	* Type: Trigger
	* TargetType: ReachPosition
	* TVS: 
		* -1700
		* -3600

## h_story_B03_ThePool_closeMis1
	* StepId: 10
	* Type: Trigger
	* TargetType: ReachPosition
	* TVS: 
		* 4400
		* 8000

## h_story_B03_ThePool_closeMis2
	* StepId: 11
	* Type: Trigger
	* TargetType: ReachPosition
	* TVS: 
		* 10600
		* 9200

## h_story_B03_ThePool_closeMis3
	* StepId: 12
	* Type: Trigger
	* TargetType: ReachPosition
	* TVS: 
		* 15300
		* 6800

## h_story_B03_ThePool_e139c7bc4b824ee46983dc9d271cd5e3
	* StepId: 31
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_B03_ThePool_1f39f96484f3a29428bf088b41c939e6

## h_story_B03_ThePool_g_destroy
	* StepId: 14
	* Type: Goal
	* TargetType: FinishGoalsString
	* TVS: h_story_B03_ThePool_t_killPlatforms
	* SuccLL: h_story_B03_ThePool_GAMA_2

## h_story_B03_ThePool_g_pirates
	* StepId: 18
	* Type: Goal
	* TargetType: KillSpecificWave
	* SuccLL: h_story_B03_ThePool_GAMA_6

## h_story_B03_ThePool_i_1
	* StepId: 20
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_story_B03_ThePool_tw0
		* h_story_B03_ThePool_tw1
		* h_story_B03_ThePool_tw2
		* h_story_B03_ThePool_tw3
		* h_story_B03_ThePool_tw4
		* h_story_B03_ThePool_tw5

## h_story_B03_ThePool_ksw0
	* StepId: 1
	* Type: Trigger
	* TargetType: KillSpecificWave

## h_story_B03_ThePool_ksw1
	* StepId: 2
	* Type: Trigger
	* TargetType: KillSpecificWave
	* SuccLL: h_story_B03_ThePool_9cc94ec0512799f438c0e538073867fc

## h_story_B03_ThePool_ksw2
	* StepId: 3
	* Type: Trigger
	* TargetType: KillSpecificWave
	* SuccLL: h_story_B03_ThePool_5c8f12e1ec0a3204c920aba0825ea3bb

## h_story_B03_ThePool_ksw3
	* StepId: 4
	* Type: Trigger
	* TargetType: KillSpecificWave
	* SuccLL: h_story_B03_ThePool_b1a9db98157e9b64d89d2052d21a12b3

## h_story_B03_ThePool_ksw4
	* StepId: 5
	* Type: Trigger
	* TargetType: KillSpecificWave
	* SuccLL: h_story_B03_ThePool_9e658015ab1bf8e48af8c23cb76e144d

## h_story_B03_ThePool_ksw5
	* StepId: 6
	* Type: Trigger
	* TargetType: KillSpecificWave
	* SuccLL: h_story_B03_ThePool_06dc7c2524746af4a8dae031f350df93

## h_story_B03_ThePool_missionStart
	* StepId: 0
	* Type: Trigger
	* TargetType: MissionStart
	* SuccLL: 
		* h_story_B03_ThePool_23258775cdaa2984abcfc6f3db7dd7b7
		* h_story_B03_ThePool_5d1ddc7041305d94d941e8af02f3b929
		* h_story_B03_ThePool_GAMA_0
		* h_story_B03_ThePool_GAMA_1
		* h_story_B03_ThePool_GAMA_12
		* h_story_B03_ThePool_GAMA_17
		* h_story_B03_ThePool_GAMA_3
		* h_story_B03_ThePool_GAMA_7
		* h_story_B03_ThePool_a_1
		* h_story_B03_ThePool_e0f8ca16410b78b42884b5f0ded33165
		* h_story_B03_ThePool_platformTriggers

## h_story_B03_ThePool_t_closeKin
	* StepId: 24
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* h_story_B03_ThePool_closeKin1
		* h_story_B03_ThePool_closeKin2
	* SuccLL: h_story_B03_ThePool_GAMA_11

## h_story_B03_ThePool_t_closeMis
	* StepId: 29
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* h_story_B03_ThePool_closeMis1
		* h_story_B03_ThePool_closeMis2
		* h_story_B03_ThePool_closeMis3
	* SuccLL: h_story_B03_ThePool_GAMA_16

## h_story_B03_ThePool_t_finDia
	* StepId: 13
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: s_pool_finish_1_dialog
	* SuccLL: h_story_B03_ThePool_fin

## h_story_B03_ThePool_t_killFirstKin
	* StepId: 21
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* h_story_B03_ThePool_ksw0
		* h_story_B03_ThePool_ksw1
		* h_story_B03_ThePool_ksw2
	* SuccLL: h_story_B03_ThePool_GAMA_8

## h_story_B03_ThePool_t_KillFirstMis
	* StepId: 26
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* h_story_B03_ThePool_ksw3
		* h_story_B03_ThePool_ksw4
		* h_story_B03_ThePool_ksw5
	* SuccLL: h_story_B03_ThePool_GAMA_13

## h_story_B03_ThePool_t_killPlatforms
	* StepId: 7
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* h_story_B03_ThePool_ksw0
		* h_story_B03_ThePool_ksw1
		* h_story_B03_ThePool_ksw2
		* h_story_B03_ThePool_ksw3
		* h_story_B03_ThePool_ksw4
		* h_story_B03_ThePool_ksw5

## h_story_B03_ThePool_w_1
	* StepId: 22
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_B03_ThePool_GAMA_9
		* h_story_B03_ThePool_d_tutRange
		* h_story_B03_ThePool_sensorView

## h_story_B03_ThePool_w_10
	* StepId: 19
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_B03_ThePool_d_fin

## h_story_B03_ThePool_w_2
	* StepId: 23
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_B03_ThePool_GAMA_10

## h_story_B03_ThePool_w_3
	* StepId: 25
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_B03_ThePool_d_closeKin

## h_story_B03_ThePool_w_4
	* StepId: 27
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_B03_ThePool_GAMA_14
		* h_story_B03_ThePool_d_tutFallof
		* h_story_B03_ThePool_sensorView2

## h_story_B03_ThePool_w_5
	* StepId: 28
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_B03_ThePool_GAMA_15

## h_story_B03_ThePool_w_6
	* StepId: 30
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_B03_ThePool_d_closeMis

## h_story_B03_ThePool_w_8
	* StepId: 17
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_B03_ThePool_GAMA_5
		* h_story_B03_ThePool_d_pirates

## h_story_B03_ThePool_w_9
	* StepId: 15
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_B03_ThePool_d_destroy

## h_story_C01_Tanochet_5baf0ac0919b7554890ee913ba9e5078
	* StepId: 3
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* h_story_C01_Tanochet_st_tanochet_leftStationDeath
		* h_story_C01_Tanochet_st_tanochet_mainStationDeath
		* h_story_C01_Tanochet_st_tanochet_rightStationDeath
	* SuccLL: 
		* h_story_C01_Tanochet_st_tanochet_act_dia_failure
		* h_story_C01_Tanochet_st_tanochet_act_missionFail1

## h_story_C01_Tanochet_i_failing
	* StepId: 1
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_story_C01_Tanochet_GAMA_1
		* h_story_C01_Tanochet_GAMA_2
		* h_story_C01_Tanochet_GAMA_4
		* h_story_C01_Tanochet_GAMA_5
		* h_story_C01_Tanochet_GAMA_6

## h_story_C01_Tanochet_i_sequence
	* StepId: 9
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_story_C01_Tanochet_DisablePlayer2
		* h_story_C01_Tanochet_GAMA_9
		* h_story_C01_Tanochet_disable_los_seq
		* h_story_C01_Tanochet_st_tanochet_ShowIntroSeq
		* h_story_C01_Tanochet_st_tanochet_act_dia_start

## h_story_C01_Tanochet_i_setup
	* StepId: 8
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_story_C01_Tanochet_st_tanochet_act_tanochFleet01
		* h_story_C01_Tanochet_st_tanochet_act_tanochFleet02
		* h_story_C01_Tanochet_st_tanochet_act_tanochFleet03
		* h_story_C01_Tanochet_st_tanochet_act_tanochStation
		* h_story_C01_Tanochet_st_tanochet_act_traderStation01
		* h_story_C01_Tanochet_st_tanochet_act_traderStation02

## h_story_C01_Tanochet_kill_torpedo1
	* StepId: 26
	* Type: Trigger
	* TargetType: KillSpecificWave
	* SuccLL: h_story_C01_Tanochet_GAMA_26

## h_story_C01_Tanochet_kill_torpedo2
	* StepId: 24
	* Type: Trigger
	* TargetType: KillSpecificWave
	* SuccLL: h_story_C01_Tanochet_GAMA_24

## h_story_C01_Tanochet_kill_torpedo3
	* StepId: 22
	* Type: Trigger
	* TargetType: AllUnitsWithTagsAreKilled
	* SuccLL: h_story_C01_Tanochet_GAMA_22

## h_story_C01_Tanochet_Mission_Start
	* StepId: 0
	* Type: Trigger
	* TargetType: MissionStart
	* SuccLL: 
		* h_story_C01_Tanochet_GAMA_0
		* h_story_C01_Tanochet_GAMA_10
		* h_story_C01_Tanochet_GAMA_7
		* h_story_C01_Tanochet_GAMA_8

## h_story_C01_Tanochet_multi_stationDeath
	* StepId: 3
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* h_story_C01_Tanochet_st_tanochet_leftStationDeath
		* h_story_C01_Tanochet_st_tanochet_mainStationDeath
		* h_story_C01_Tanochet_st_tanochet_rightStationDeath
	* SuccLL: 
		* h_story_C01_Tanochet_GAMA_3
		* h_story_C01_Tanochet_st_tanochet_act_dia_failure
		* h_story_C01_Tanochet_st_tanochet_act_missionFail1

## h_story_C01_Tanochet_st_tanochet_afterSequence
	* StepId: 10
	* Type: Trigger
	* TargetType: OnInGameSequenceFinishedForPlayer
	* TVS: 1
	* SuccLL: 
		* h_story_C01_Tanochet_enable_los
		* h_story_C01_Tanochet_st_tanochet_act_lookAtStation

## h_story_C01_Tanochet_st_tanochet_failMissionAfterDialog
	* StepId: 2
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: Story-03-01_dialog_failure
	* SuccLL: h_story_C01_Tanochet_st_tanochet_act_fin_fail

## h_story_C01_Tanochet_st_tanochet_gDock
	* StepId: 20
	* Type: Goal
	* TargetType: ReachPosition
	* TVS: 
		* 0
		* 5000
	* SuccLL: 
		* h_story_C01_Tanochet_st_tanochet_act_cinematic
		* h_story_C01_Tanochet_st_tanochet_act_fin

## h_story_C01_Tanochet_st_tanochet_gMove
	* StepId: 11
	* Type: Goal
	* TargetType: ReachPosition
	* TVS: 
		* 0
		* 5000
	* SuccLL: 
		* h_story_C01_Tanochet_GAMA_11
		* h_story_C01_Tanochet_enable_tanoch
		* h_story_C01_Tanochet_st_tanochet_act_dia_yaotSpawn

## h_story_C01_Tanochet_st_tanochet_gTorp1
	* StepId: 14
	* Type: Goal
	* TargetType: FinishGoalsString
	* TVS: h_story_C01_Tanochet_w_goalBufferTorpedo1
	* SuccLL: h_story_C01_Tanochet_GAMA_14

## h_story_C01_Tanochet_st_tanochet_gTorp2
	* StepId: 16
	* Type: Goal
	* TargetType: FinishGoalsString
	* TVS: h_story_C01_Tanochet_w_goalBufferTorpedo2
	* SuccLL: h_story_C01_Tanochet_GAMA_16

## h_story_C01_Tanochet_st_tanochet_gTorp3
	* StepId: 18
	* Type: Goal
	* TargetType: FinishGoalsString
	* TVS: h_story_C01_Tanochet_w_goalBufferTorpedo3
	* SuccLL: h_story_C01_Tanochet_GAMA_18

## h_story_C01_Tanochet_st_tanochet_leftStationDeath
	* StepId: 7
	* Type: Trigger
	* TargetType: OnTaggedUnitKilled

## h_story_C01_Tanochet_st_tanochet_mainStationDeath
	* StepId: 5
	* Type: Trigger
	* TargetType: OnTaggedUnitKilled

## h_story_C01_Tanochet_st_tanochet_mainYaotSpawn
	* StepId: 28
	* Type: TriggerRepeating
	* TargetType: WaitForTime
	* SuccLL: h_story_C01_Tanochet_st_tanochet_act_mainYaotFleet

## h_story_C01_Tanochet_st_tanochet_rightStationDeath
	* StepId: 6
	* Type: Trigger
	* TargetType: OnTaggedUnitKilled

## h_story_C01_Tanochet_st_tanochet_timer01
	* StepId: 13
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_C01_Tanochet_GAMA_13
		* h_story_C01_Tanochet_GAMA_25
		* h_story_C01_Tanochet_GAMA_27
		* h_story_C01_Tanochet_st_tanoch_act_spawnMainFleet
		* h_story_C01_Tanochet_st_tanochet_act_dia_torpedo1
		* h_story_C01_Tanochet_st_tanochet_act_sensorview_Torp1
		* h_story_C01_Tanochet_st_tanochet_act_yaotFleet01
		* h_story_C01_Tanochet_st_tanochet_act_yaotTorp01
		* h_story_C01_Tanochet_st_tanochet_markTorp1

## h_story_C01_Tanochet_st_tanochet_timer02
	* StepId: 15
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_C01_Tanochet_GAMA_15
		* h_story_C01_Tanochet_GAMA_23
		* h_story_C01_Tanochet_st_tanochet_act_dia_torpedo2
		* h_story_C01_Tanochet_st_tanochet_act_sensorview_Torp2
		* h_story_C01_Tanochet_st_tanochet_act_yaotFleet02
		* h_story_C01_Tanochet_st_tanochet_act_yaotTorp02
		* h_story_C01_Tanochet_st_tanochet_markTorp2

## h_story_C01_Tanochet_st_tanochet_timer03
	* StepId: 17
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_C01_Tanochet_GAMA_17
		* h_story_C01_Tanochet_GAMA_21
		* h_story_C01_Tanochet_st_tanochet_act_dia_torpedo3
		* h_story_C01_Tanochet_st_tanochet_act_sensorview_Torp3
		* h_story_C01_Tanochet_st_tanochet_act_yaotFleet03
		* h_story_C01_Tanochet_st_tanochet_act_yaotTorp03
		* h_story_C01_Tanochet_st_tanochet_markLastTorpedoFleet

## h_story_C01_Tanochet_st_tanochet_timer04
	* StepId: 19
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_C01_Tanochet_GAMA_19
		* h_story_C01_Tanochet_GAMA_20
		* h_story_C01_Tanochet_disablePlayer2
		* h_story_C01_Tanochet_st_tanochet_act_dia_attackOver
		* h_story_C01_Tanochet_st_tanochet_act_stopYaotSpawn

## h_story_C01_Tanochet_st_tanochet_trigDia_yaotSpawn
	* StepId: 12
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: Story-03-01_yaotSpawn_dialog
	* SuccLL: h_story_C01_Tanochet_GAMA_12

## h_story_C01_Tanochet_w_goalBufferTorpedo1
	* StepId: 27
	* Type: Trigger
	* TargetType: WaitForTime

## h_story_C01_Tanochet_w_goalBufferTorpedo2
	* StepId: 25
	* Type: Trigger
	* TargetType: WaitForTime

## h_story_C01_Tanochet_w_goalBufferTorpedo3
	* StepId: 23
	* Type: Trigger
	* TargetType: WaitForTime

## h_story_C01_Tanochet_w_removeYaotFail
	* StepId: 4
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_C01_Tanochet_remove_yaotFail

## h_story_C01_Tanochet_w_removeYaotWin
	* StepId: 21
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_C01_Tanochet_remove_yaotWin

## h_story_C01_Tanochet_w_yaotRetreat
	* StepId: 4
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_C01_Tanochet_remove_yaotFail

## h_story_C02_TempleTonaati_e960155643664b64aad0456a88e3157c
	* StepId: 3
	* Type: Trigger
	* TargetType: OnInGameSequenceFinishedForPlayer
	* SuccLL: 
		* h_story_C02_TempleTonaati_GAMA_18
		* h_story_C02_TempleTonaati_GAMA_3
		* h_story_C02_TempleTonaati_b43f51277456b624a90acaf186133983

## h_story_C02_TempleTonaati_s0302v2_boss_kill_goal
	* StepId: 13
	* Type: Goal
	* TargetType: KillSpecificWave
	* SuccLL: h_story_C02_TempleTonaati_s0302v2_act_finish_dia

## h_story_C02_TempleTonaati_s0302v2_cameralookat_timer
	* StepId: 23
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_C02_TempleTonaati_s0302v2_act_cameralookatStation

## h_story_C02_TempleTonaati_s0302v2_civilStation_dia_wait
	* StepId: 8
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_C02_TempleTonaati_GAMA_8
		* h_story_C02_TempleTonaati_s0302v2_act_explainStar_dia

## h_story_C02_TempleTonaati_s0302v2_fail_mission_dia_finished
	* StepId: 1
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: Story-03-02-v2_missionfail_dialog
	* SuccLL: h_story_C02_TempleTonaati_s0302v2_act_mission_failed

## h_story_C02_TempleTonaati_s0302v2_finish_dialogfinshed
	* StepId: 2
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: Story-03-02-v2_finish_dialog
	* SuccLL: h_story_C02_TempleTonaati_s0302v2_finish_mission

## h_story_C02_TempleTonaati_s0302v2_fleet_kill_goal
	* StepId: 12
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* h_story_C02_TempleTonaati_s0302v2_fleet_kill_goal_1
		* h_story_C02_TempleTonaati_s0302v2_fleet_kill_goal_2
		* h_story_C02_TempleTonaati_s0302v2_fleet_kill_goal_3
	* SuccLL: 
		* h_story_C02_TempleTonaati_GAMA_11
		* h_story_C02_TempleTonaati_s0302v2_act_boss_dia
		* h_story_C02_TempleTonaati_s0302v2_act_boss_sensorviewon
		* h_story_C02_TempleTonaati_s0302v2_act_spawn_boss0

## h_story_C02_TempleTonaati_s0302v2_fleet_kill_goal_1
	* StepId: 14
	* Type: Goal
	* TargetType: KillSpecificWave

## h_story_C02_TempleTonaati_s0302v2_fleet_kill_goal_2
	* StepId: 15
	* Type: Goal
	* TargetType: KillSpecificWave

## h_story_C02_TempleTonaati_s0302v2_fleet_kill_goal_3
	* StepId: 16
	* Type: Goal
	* TargetType: KillSpecificWave

## h_story_C02_TempleTonaati_s0302v2_goal_moveto_mark_civilStation
	* StepId: 7
	* Type: Goal
	* TargetType: ReachPosition
	* TVS: 
		* 0
		* 4000
	* SuccLL: 
		* h_story_C02_TempleTonaati_GAMA_7
		* h_story_C02_TempleTonaati_s0302v2_act_civilStation_reached_dia
		* h_story_C02_TempleTonaati_s0302v2_act_deactivate_mark_left
		* h_story_C02_TempleTonaati_s0302v2_act_deactivate_mark_right
		* h_story_C02_TempleTonaati_s0302v2_act_hilight_civilStation

## h_story_C02_TempleTonaati_s0302v2_markGoal
	* StepId: 20
	* Type: Goal
	* TargetType: FinishGoalsString
	* TVS: 
		* h_story_C02_TempleTonaati_s0302v2_showMark_path_left
		* h_story_C02_TempleTonaati_s0302v2_showMark_path_right

## h_story_C02_TempleTonaati_s0302v2_position_civilStation_timer
	* StepId: 5
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_C02_TempleTonaati_GAMA_15
		* h_story_C02_TempleTonaati_GAMA_16
		* h_story_C02_TempleTonaati_GAMA_17
		* h_story_C02_TempleTonaati_GAMA_5
		* h_story_C02_TempleTonaati_s0302v2_act_move_civilStation_dialog

## h_story_C02_TempleTonaati_s0302v2_sensorview_timer
	* StepId: 4
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_C02_TempleTonaati_GAMA_4
		* h_story_C02_TempleTonaati_s0302v2_act_sensorview_on

## h_story_C02_TempleTonaati_s0302v2_showMark_path_left
	* StepId: 21
	* Type: Trigger
	* TargetType: ReachPosition
	* TVS: 
		* -26600
		* -5300
	* SuccLL: h_story_C02_TempleTonaati_actn_deativateRightPath

## h_story_C02_TempleTonaati_s0302v2_showMark_path_right
	* StepId: 22
	* Type: Trigger
	* TargetType: ReachPosition
	* TVS: 
		* 2000
		* 24700
	* SuccLL: h_story_C02_TempleTonaati_actn_deativateLeftPath

## h_story_C02_TempleTonaati_s0302v2_Star_dia_onfinished
	* StepId: 9
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: Story-03-02-v2_explainStar_dialog
	* SuccLL: 
		* h_story_C02_TempleTonaati_GAMA_9
		* h_story_C02_TempleTonaati_s0302v2_act_yaotsuddenly_dia

## h_story_C02_TempleTonaati_s0302v2_Station_killed
	* StepId: 29
	* Type: Trigger
	* TargetType: OnTaggedUnitKilled
	* SuccLL: h_story_C02_TempleTonaati_s0302v2_act_Station_killed_dia

## h_story_C02_TempleTonaati_s0302v2_Temple_kill_wait_timer
	* StepId: 11
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_C02_TempleTonaati_GAMA_12
		* h_story_C02_TempleTonaati_s0302v2_act_Temple_killed_dia
		* h_story_C02_TempleTonaati_s0302v2_act_fleet_kill_goal
		* h_story_C02_TempleTonaati_s0302v2_act_fleet_kill_goals

## h_story_C02_TempleTonaati_s0302v2_trg_missionstart
	* StepId: 0
	* Type: Trigger
	* TargetType: MissionStart
	* SuccLL: 
		* h_story_C02_TempleTonaati_GAMA_0
		* h_story_C02_TempleTonaati_GAMA_1
		* h_story_C02_TempleTonaati_GAMA_19
		* h_story_C02_TempleTonaati_GAMA_2
		* h_story_C02_TempleTonaati_GAMA_20
		* h_story_C02_TempleTonaati_GAMA_21
		* h_story_C02_TempleTonaati_GAMA_22
		* h_story_C02_TempleTonaati_GAMA_23
		* h_story_C02_TempleTonaati_GAMA_24
		* h_story_C02_TempleTonaati_GAMA_25
		* h_story_C02_TempleTonaati_SetSensorRangeOff
		* h_story_C02_TempleTonaati_s0302v2_act_Station_killed
		* h_story_C02_TempleTonaati_s0302v2_act_dialog_intro

## h_story_C02_TempleTonaati_s0302v2_trigger_ReachedDebrisField
	* StepId: 6
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* h_story_C02_TempleTonaati_s0302v2_showMark_path_left
		* h_story_C02_TempleTonaati_s0302v2_showMark_path_right
	* SuccLL: h_story_C02_TempleTonaati_GAMA_6

## h_story_C02_TempleTonaati_s0302v2_yaotsuddenly_dia_onfinished
	* StepId: 10
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: Story-03-02-v2_yaotsuddenly_dialog
	* SuccLL: 
		* h_story_C02_TempleTonaati_GAMA_10
		* h_story_C02_TempleTonaati_s0302v2_act_spawn_fleet01
		* h_story_C02_TempleTonaati_s0302v2_act_spawn_fleet02
		* h_story_C02_TempleTonaati_s0302v2_act_spawn_fleet03
		* h_story_C02_TempleTonaati_s0302v2_act_yaotattack_dia
		* h_story_C02_TempleTonaati_s0302v2_act_yaotattack_sensorviewon
		* h_story_C02_TempleTonaati_setActive_FriendlyShipsOn
		* h_story_C02_TempleTonaati_setActive_StationOn

## h_story_C02_TempleTonaati_timer_WaitForTimeDestroyGuard01
	* StepId: 17
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_C02_TempleTonaati_GAMA_13
		* h_story_C02_TempleTonaati_actn_SetGuardHP01

## h_story_C02_TempleTonaati_timer_WaitForTimeDestroyGuard02
	* StepId: 18
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_C02_TempleTonaati_GAMA_14
		* h_story_C02_TempleTonaati_actn_SetGuardArmor02
		* h_story_C02_TempleTonaati_actn_SetGuardHP02

## h_story_C02_TempleTonaati_timer_WaitForTimeDestroyGuard03
	* StepId: 19
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_C02_TempleTonaati_actn_DestroyGuard

## h_story_C02_TempleTonaati_trigger_deactivateFriendlyShips
	* StepId: 31
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_story_C02_TempleTonaati_setActive_FriendlyShipsOff
		* h_story_C02_TempleTonaati_setActive_StationOff

## h_story_C02_TempleTonaati_trigger_SpawnAllies
	* StepId: 25
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_story_C02_TempleTonaati_s0302v2_act_spawn_civilShip1
		* h_story_C02_TempleTonaati_s0302v2_act_spawn_civilShip2
		* h_story_C02_TempleTonaati_s0302v2_act_spawn_civilShip3

## h_story_C02_TempleTonaati_trigger_SpawnGuards
	* StepId: 26
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_story_C02_TempleTonaati_s0302v2_act_spawn_guard1
		* h_story_C02_TempleTonaati_s0302v2_act_spawn_guard10
		* h_story_C02_TempleTonaati_s0302v2_act_spawn_guard11
		* h_story_C02_TempleTonaati_s0302v2_act_spawn_guard12
		* h_story_C02_TempleTonaati_s0302v2_act_spawn_guard13
		* h_story_C02_TempleTonaati_s0302v2_act_spawn_guard2
		* h_story_C02_TempleTonaati_s0302v2_act_spawn_guard3
		* h_story_C02_TempleTonaati_s0302v2_act_spawn_guard4
		* h_story_C02_TempleTonaati_s0302v2_act_spawn_guard5
		* h_story_C02_TempleTonaati_s0302v2_act_spawn_guard6
		* h_story_C02_TempleTonaati_s0302v2_act_spawn_guard7
		* h_story_C02_TempleTonaati_s0302v2_act_spawn_guard8
		* h_story_C02_TempleTonaati_s0302v2_act_spawn_guard9

## h_story_C02_TempleTonaati_trigger_SpawnMines
	* StepId: 28
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_story_C02_TempleTonaati_s0302v2_act_spawn_mine1_1
		* h_story_C02_TempleTonaati_s0302v2_act_spawn_mine1_2
		* h_story_C02_TempleTonaati_s0302v2_act_spawn_mine1_3
		* h_story_C02_TempleTonaati_s0302v2_act_spawn_mine2_1
		* h_story_C02_TempleTonaati_s0302v2_act_spawn_mine2_2
		* h_story_C02_TempleTonaati_s0302v2_act_spawn_mine2_3

## h_story_C02_TempleTonaati_trigger_SpawnPatrols
	* StepId: 27
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_story_C02_TempleTonaati_s0302v2_act_spawn_patrol1_1
		* h_story_C02_TempleTonaati_s0302v2_act_spawn_patrol1_2
		* h_story_C02_TempleTonaati_s0302v2_act_spawn_patrol2_1
		* h_story_C02_TempleTonaati_s0302v2_act_spawn_patrol2_2
		* h_story_C02_TempleTonaati_s0302v2_act_spawn_patrol3_1
		* h_story_C02_TempleTonaati_s0302v2_act_spawn_patrol3_2

## h_story_C02_TempleTonaati_trigger_SpawnStation
	* StepId: 24
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: h_story_C02_TempleTonaati_s0302v2_act_spawn_civilStation0

## h_story_C02_TempleTonaati_WaitSequenceStart
	* StepId: 30
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: h_story_C02_TempleTonaati_ShowIntroSequence

## h_story_C03_StarTotek_59082cb8d1001b8419a5d882590d61c4
	* StepId: 26
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* h_story_C03_StarTotek_dialog_finish_intro_5
		* h_story_C03_StarTotek_timer_highlight
	* SuccLL: h_story_C03_StarTotek_TriggerDialog_debri_1

## h_story_C03_StarTotek_AllEnemiesDeadDiaWait
	* StepId: 17
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_C03_StarTotek_GAMA_17
		* h_story_C03_StarTotek_TriggerDialog_salva_3

## h_story_C03_StarTotek_CheckVaygrSeqEnd
	* StepId: 35
	* Type: Trigger
	* TargetType: OnInGameSequenceFinishedForPlayer
	* TVS: 1
	* SuccLL: 
		* h_story_C03_StarTotek_DisableTimerForPlayerActiveState
		* h_story_C03_StarTotek_EnableEnemyAfterVaygrSeq
		* h_story_C03_StarTotek_EnablePlayerAfterVaygrSeq
		* h_story_C03_StarTotek_GAMA_35

## h_story_C03_StarTotek_D1_drone_warning
	* StepId: 40
	* Type: Trigger
	* TargetType: ReachPointOfInterest
	* SuccLL: h_story_C03_StarTotek_D1_drones_warning_dia

## h_story_C03_StarTotek_D3_drone_warning
	* StepId: 43
	* Type: Trigger
	* TargetType: ReachPointOfInterest
	* SuccLL: h_story_C03_StarTotek_D3_drones_warning_dia

## h_story_C03_StarTotek_dia_and_highlights_finish
	* StepId: 25
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: h_story_C03_StarTotek_wait_highlight_path_1
	* SuccLL: 
		* h_story_C03_StarTotek_GAMA_25
		* h_story_C03_StarTotek_GAMA_26
		* h_story_C03_StarTotek_GAMA_27
		* h_story_C03_StarTotek_GAMA_28

## h_story_C03_StarTotek_dialog_finish_intro_5
	* StepId: 27
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: st_startotek_intro_5_dialog

## h_story_C03_StarTotek_DialogAndWait
	* StepId: 20
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* h_story_C03_StarTotek_TempTrigger01
		* h_story_C03_StarTotek_TriggerWaitForTime04
	* SuccLL: h_story_C03_StarTotek_GAMA_20

## h_story_C03_StarTotek_GetGoalsForRouteOrShortcut
	* StepId: 9
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: h_story_C03_StarTotek_GoalUseReachPosAsSignalNode
	* SuccLL: h_story_C03_StarTotek_GAMA_9

## h_story_C03_StarTotek_GoalStopJochik
	* StepId: 10
	* Type: Goal
	* TargetType: OnTaggedUnitIsBelowHealth

## h_story_C03_StarTotek_GoalUseReachPosAsSignalNode
	* StepId: 34
	* Type: Goal
	* TargetType: ReachPointOfInterest
	* SuccLL: 
		* h_story_C03_StarTotek_DisableEnemyDuringVaygrSeq
		* h_story_C03_StarTotek_DisablePlayerDuringVaygrSeq
		* h_story_C03_StarTotek_GAMA_34
		* h_story_C03_StarTotek_RemoveProgenitors
		* h_story_C03_StarTotek_Show_Vaygr_Seq
		* h_story_C03_StarTotek_TriggerDialog_vaygr_2
		* h_story_C03_StarTotek_disableLOSFinalFight
		* h_story_C03_StarTotek_seq_make_enemy_invincible
		* h_story_C03_StarTotek_seq_make_player_invincible

## h_story_C03_StarTotek_intro_3_dia_finish
	* StepId: 24
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: st_startotek_intro_3_dialog
	* SuccLL: 
		* h_story_C03_StarTotek_GAMA_24
		* h_story_C03_StarTotek_GAMA_30

## h_story_C03_StarTotek_LastEnemyKilled
	* StepId: 16
	* Type: Goal
	* TargetType: WaveFinished
	* SuccLL: h_story_C03_StarTotek_GAMA_16

## h_story_C03_StarTotek_MissionStart
	* StepId: 0
	* Type: Trigger
	* TargetType: MissionStart
	* SuccLL: 
		* h_story_C03_StarTotek_GAMA_0
		* h_story_C03_StarTotek_intro_disableLOS
		* h_story_C03_StarTotek_intro_seq
		* h_story_C03_StarTotek_playerDisabledIntro
		* h_story_C03_StarTotek_playerIntroImortality

## h_story_C03_StarTotek_ord_node_spawn_godmode_on
	* StepId: 5
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_story_C03_StarTotek_godmode_player1
		* h_story_C03_StarTotek_godmode_player2

## h_story_C03_StarTotek_org_node_post_heal_ungodmode
	* StepId: 7
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_C03_StarTotek_ungodmode_player1
		* h_story_C03_StarTotek_ungodmode_player2
		* h_story_C03_StarTotek_ungodmode_player3

## h_story_C03_StarTotek_org_node_start_setup
	* StepId: 4
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_story_C03_StarTotek_GAMA_4
		* h_story_C03_StarTotek_TriggerWave_KeeperShips01
		* h_story_C03_StarTotek_TriggerWave_KeeperShips02
		* h_story_C03_StarTotek_TriggerWave_KeeperShips03
		* h_story_C03_StarTotek_TriggerWave_KeeperShips04
		* h_story_C03_StarTotek_TriggerWave_KeeperShips05
		* h_story_C03_StarTotek_TriggerWave_SpawnJochik
		* h_story_C03_StarTotek_TriggerWave_VaygrGuard01
		* h_story_C03_StarTotek_TriggerWave_VaygrGuard02
		* h_story_C03_StarTotek_TriggerWave_VaygrMainFleet
		* h_story_C03_StarTotek_actn_makeJochikInvincibleat

## h_story_C03_StarTotek_PostIntroBranch
	* StepId: 2
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_story_C03_StarTotek_GAMA_19
		* h_story_C03_StarTotek_GAMA_2
		* h_story_C03_StarTotek_GAMA_3
		* h_story_C03_StarTotek_GAMA_36
		* h_story_C03_StarTotek_GAMA_37
		* h_story_C03_StarTotek_GAMA_38
		* h_story_C03_StarTotek_GAMA_5
		* h_story_C03_StarTotek_GAMA_7
		* h_story_C03_StarTotek_intro_dia_1

## h_story_C03_StarTotek_repair_delay
	* StepId: 6
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_C03_StarTotek_GAMA_6
		* h_story_C03_StarTotek_repair_1_armor_post_spawn
		* h_story_C03_StarTotek_repair_1_hull_post_spawn
		* h_story_C03_StarTotek_repair_2_armor_post_spawn
		* h_story_C03_StarTotek_repair_2_hull_post_spawn

## h_story_C03_StarTotek_salva_3_dia_done
	* StepId: 18
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: st_startotek_salva_3_dialog
	* SuccLL: h_story_C03_StarTotek_GAMA_18

## h_story_C03_StarTotek_SeqMakeEnemyMortalTimer
	* StepId: 36
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_C03_StarTotek_VaygrFollowFlagship
		* h_story_C03_StarTotek_seq_make_enemy_mortal
		* h_story_C03_StarTotek_seq_make_player_mortal

## h_story_C03_StarTotek_TempTrigger01
	* StepId: 38
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: st_startotek_intro_1_dialog

## h_story_C03_StarTotek_TempTrigger02
	* StepId: 15
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_C03_StarTotek_DeactivateMakePlayer1Invincible
		* h_story_C03_StarTotek_DeactivateMakePlayer3Invincible
		* h_story_C03_StarTotek_DisableKillGoal
		* h_story_C03_StarTotek_GAMA_15
		* h_story_C03_StarTotek_RemoveJochik
		* h_story_C03_StarTotek_TriggerDialog_salva_2
		* h_story_C03_StarTotek_spawnFinalWave

## h_story_C03_StarTotek_timer_highlight
	* StepId: 28
	* Type: Trigger
	* TargetType: WaitForTime

## h_story_C03_StarTotek_Trigger50_PlaySequence
	* StepId: 13
	* Type: Trigger
	* TargetType: OnTaggedUnitIsBelowHealth
	* SuccLL: 
		* h_story_C03_StarTotek_GAMA_13
		* h_story_C03_StarTotek_MakePlayer1Invincible
		* h_story_C03_StarTotek_MakePlayer2Invincible
		* h_story_C03_StarTotek_TriggerDialog_salva_1

## h_story_C03_StarTotek_Trigger60_GiveStatMod
	* StepId: 11
	* Type: Trigger
	* TargetType: OnTaggedUnitsHaveAmountOfArmor
	* SuccLL: h_story_C03_StarTotek_boss_hp_low_boost

## h_story_C03_StarTotek_Trigger90_SpawnReinforcements
	* StepId: 12
	* Type: Trigger
	* TargetType: OnTaggedUnitIsBelowHealth
	* SuccLL: 
		* h_story_C03_StarTotek_TriggerDialog_battle_2
		* h_story_C03_StarTotek_TriggerWave_SpawnVaygrReenforcements1
		* h_story_C03_StarTotek_TriggerWave_SpawnVaygrReenforcements2

## h_story_C03_StarTotek_TriggerCheckForMissionSuccess
	* StepId: 3
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: h_story_C03_StarTotek_TriggerWaitForTimeMissionSuccess
	* SuccLL: h_story_C03_StarTotek_FinishMissionSuccess

## h_story_C03_StarTotek_TriggerForDialogeGettingClose
	* StepId: 42
	* Type: Trigger
	* TargetType: ReachPointOfInterest
	* SuccLL: 
		* h_story_C03_StarTotek_TriggerDialog_vaygr_1_ShortCut
		* h_story_C03_StarTotek_deactivate_reach_vaygr_boss_goal

## h_story_C03_StarTotek_TriggerOnDialogFinished_intro_2
	* StepId: 22
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: st_startotek_intro_2_dialog
	* SuccLL: h_story_C03_StarTotek_GAMA_22

## h_story_C03_StarTotek_TriggerOnSequenceFinished_Intro
	* StepId: 1
	* Type: Trigger
	* TargetType: OnInGameSequenceFinishedForPlayer
	* TVS: 1
	* SuccLL: 
		* h_story_C03_StarTotek_GAMA_1
		* h_story_C03_StarTotek_intro_enableLOS
		* h_story_C03_StarTotek_playerEnabledIntro

## h_story_C03_StarTotek_TriggerReachFinalPosition
	* StepId: 29
	* Type: Trigger
	* TargetType: ReachPointOfInterest
	* SuccLL: 
		* h_story_C03_StarTotek_GAMA_29
		* h_story_C03_StarTotek_TriggerDialog_vaygr_1

## h_story_C03_StarTotek_TriggerReachPos_ShortcutDialog
	* StepId: 41
	* Type: Trigger
	* TargetType: ReachPointOfInterest
	* SuccLL: 
		* h_story_C03_StarTotek_GAMA_41
		* h_story_C03_StarTotek_shortcut_D2_dia

## h_story_C03_StarTotek_TriggerSetupBossBehaviour
	* StepId: 8
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_C03_StarTotek_GAMA_10
		* h_story_C03_StarTotek_GAMA_11
		* h_story_C03_StarTotek_GAMA_12
		* h_story_C03_StarTotek_GAMA_8

## h_story_C03_StarTotek_TriggerSetupReachPosNodes
	* StepId: 39
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_story_C03_StarTotek_GAMA_39
		* h_story_C03_StarTotek_GAMA_40
		* h_story_C03_StarTotek_GAMA_42

## h_story_C03_StarTotek_TriggerWaitForDialoge_salva_1
	* StepId: 14
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: st_startotek_salva_1_dialog
	* SuccLL: h_story_C03_StarTotek_GAMA_14

## h_story_C03_StarTotek_TriggerWaitForTime01
	* StepId: 21
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_C03_StarTotek_GAMA_21
		* h_story_C03_StarTotek_TriggerDialog_intro_2

## h_story_C03_StarTotek_TriggerWaitForTime02
	* StepId: 23
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_C03_StarTotek_CloseSensorManager
		* h_story_C03_StarTotek_GAMA_23
		* h_story_C03_StarTotek_GAMA_32

## h_story_C03_StarTotek_TriggerWaitForTime03
	* StepId: 33
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_C03_StarTotek_GAMA_33
		* h_story_C03_StarTotek_TriggerDialog_intro_3
		* h_story_C03_StarTotek_highlight_destination

## h_story_C03_StarTotek_TriggerWaitForTime04
	* StepId: 37
	* Type: Trigger
	* TargetType: WaitForTime

## h_story_C03_StarTotek_TriggerWaitForTimeMissionSuccess
	* StepId: 19
	* Type: Trigger
	* TargetType: WaitForTime

## h_story_C03_StarTotek_vaygr_pos_dia_check
	* StepId: 30
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: st_startotek_vaygr_1_dialog

## h_story_C03_StarTotek_wait_highlight_path_0
	* StepId: 31
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_C03_StarTotek_GAMA_31
		* h_story_C03_StarTotek_TriggerDialog_intro_4
		* h_story_C03_StarTotek_sensormanager_path

## h_story_C03_StarTotek_wait_highlight_path_1
	* StepId: 32
	* Type: Trigger
	* TargetType: WaitForTime

## h_story_D01_SijinLighthouse_ally_seq_end
	* StepId: 5
	* Type: Trigger
	* TargetType: OnInGameSequenceFinishedForPlayer
	* TVS: 1
	* SuccLL: 
		* h_story_D01_SijinLighthouse_0057c619a510b8146ba95a1204405167
		* h_story_D01_SijinLighthouse_03617d6bdaef1704aa7832c7d268e7e7
		* h_story_D01_SijinLighthouse_40f77dd1ffd45634c87b93b7cb322c73
		* h_story_D01_SijinLighthouse_GAMA_5
		* h_story_D01_SijinLighthouse_enable_los1
		* h_story_D01_SijinLighthouse_s2_01_lighthouse_act_interactable

## h_story_D01_SijinLighthouse_checkDialogClosed
	* StepId: 18
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: st_farshore_esc_2_dialog

## h_story_D01_SijinLighthouse_checkIfEscape
	* StepId: 17
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* h_story_D01_SijinLighthouse_checkDialogClosed
		* h_story_D01_SijinLighthouse_escapeTimer
	* SuccLL: h_story_D01_SijinLighthouse_s2_01_lighthouse_act_mission_succeeded_escape

## h_story_D01_SijinLighthouse_escapeTimer
	* StepId: 19
	* Type: Trigger
	* TargetType: WaitForTime

## h_story_D01_SijinLighthouse_FightEnemiesGoal
	* StepId: 7
	* Type: Goal
	* TargetType: FinishGoalsString
	* TVS: h_story_D01_SijinLighthouse_s2_01_lighthouse_kill_wave4

## h_story_D01_SijinLighthouse_obsGateTimerBeforeCinematic
	* StepId: 15
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D01_SijinLighthouse_GAMA_15
		* h_story_D01_SijinLighthouse_disableAlly
		* h_story_D01_SijinLighthouse_disableEnemy
		* h_story_D01_SijinLighthouse_s2_01_lighthouse_act_cinematic

## h_story_D01_SijinLighthouse_repeating_spawn_final_wave
	* StepId: 20
	* Type: TriggerRepeating
	* TargetType: WaitForTime
	* SuccLL: h_story_D01_SijinLighthouse_s2_01_lighthouse_act_spawnBoss

## h_story_D01_SijinLighthouse_s2_01_lighthouse_allyDeath
	* StepId: 32
	* Type: Trigger
	* TargetType: OnTaggedUnitKilled
	* SuccLL: 
		* h_story_D01_SijinLighthouse_GAMA_32
		* h_story_D01_SijinLighthouse_s2_01_lighthouse_act_allyDeath_die

## h_story_D01_SijinLighthouse_s2_01_lighthouse_allyDeath_dia_wait
	* StepId: 33
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: Story-S2-01-Lighthouse_fail_dialog
	* SuccLL: h_story_D01_SijinLighthouse_s2_01_lighthouse_act_mission_failed

## h_story_D01_SijinLighthouse_s2_01_lighthouse_cameraLookAt_timer
	* StepId: 34
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_D01_SijinLighthouse_s2_01_lighthouse_act_cameraLookAt_target

## h_story_D01_SijinLighthouse_s2_01_lighthouse_escape1_wait3
	* StepId: 14
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D01_SijinLighthouse_GAMA_14
		* h_story_D01_SijinLighthouse_s2_01_lighthouse_act_escape1

## h_story_D01_SijinLighthouse_s2_01_lighthouse_interacted
	* StepId: 6
	* Type: Goal
	* TargetType: OnInteractionDone
	* TVS: s2_01_lighthouse_interact
	* SuccLL: 
		* h_story_D01_SijinLighthouse_GAMA_29
		* h_story_D01_SijinLighthouse_GAMA_30
		* h_story_D01_SijinLighthouse_GAMA_6
		* h_story_D01_SijinLighthouse_GAMA_7
		* h_story_D01_SijinLighthouse_d_attack
		* h_story_D01_SijinLighthouse_s2_01_lighthouse_act_spawnWave1

## h_story_D01_SijinLighthouse_s2_01_lighthouse_kill_wave1
	* StepId: 30
	* Type: Trigger
	* TargetType: KillSpecificWave

## h_story_D01_SijinLighthouse_s2_01_lighthouse_kill_wave2
	* StepId: 28
	* Type: Trigger
	* TargetType: KillSpecificWave

## h_story_D01_SijinLighthouse_s2_01_lighthouse_kill_wave3
	* StepId: 26
	* Type: Trigger
	* TargetType: KillSpecificWave

## h_story_D01_SijinLighthouse_s2_01_lighthouse_kill_wave4
	* StepId: 24
	* Type: Trigger
	* TargetType: KillSpecificWave

## h_story_D01_SijinLighthouse_s2_01_lighthouse_moveto_kalaad
	* StepId: 4
	* Type: Goal
	* TargetType: ReachPointOfInterest
	* SuccLL: 
		* h_story_D01_SijinLighthouse_148d6dcf55bfd804b826c50b8d5622f9
		* h_story_D01_SijinLighthouse_18bee1eaabd87e3499566348aab1fd59
		* h_story_D01_SijinLighthouse_87b4a24686514e443a87773a149fcb68
		* h_story_D01_SijinLighthouse_GAMA_31
		* h_story_D01_SijinLighthouse_GAMA_4
		* h_story_D01_SijinLighthouse_disable_los1
		* h_story_D01_SijinLighthouse_s2_01_lighthouse_act_ally
		* h_story_D01_SijinLighthouse_s2_01_lighthouse_act_spawnAlly
		* h_story_D01_SijinLighthouse_show_ally_seq

## h_story_D01_SijinLighthouse_s2_01_lighthouse_position_lighthouse_timer
	* StepId: 3
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_D01_SijinLighthouse_GAMA_3

## h_story_D01_SijinLighthouse_s2_01_lighthouse_sensorview_timer
	* StepId: 2
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D01_SijinLighthouse_GAMA_2
		* h_story_D01_SijinLighthouse_s2_01_lighthouse_act_sensorview_on

## h_story_D01_SijinLighthouse_s2_01_lighthouse_start_wait
	* StepId: 0
	* Type: Trigger
	* TargetType: MissionStart
	* SuccLL: h_story_D01_SijinLighthouse_GAMA_0

## h_story_D01_SijinLighthouse_s2_01_lighthouse_trig0
	* StepId: 1
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D01_SijinLighthouse_GAMA_1
		* h_story_D01_SijinLighthouse_GAMA_33
		* h_story_D01_SijinLighthouse_s2_01_lighthouse_act_intro
		* h_story_D01_SijinLighthouse_s2_01_lighthouse_act_spawnPatrol1
		* h_story_D01_SijinLighthouse_s2_01_lighthouse_act_spawnPatrol2
		* h_story_D01_SijinLighthouse_s2_01_lighthouse_act_spawnPatrol3

## h_story_D01_SijinLighthouse_t_escape1_wait1
	* StepId: 21
	* Type: Trigger
	* TargetType: WaitForTime

## h_story_D01_SijinLighthouse_t_finishObserverSequence
	* StepId: 22
	* Type: Trigger
	* TargetType: OnInGameSequenceFinishedForPlayer
	* TVS: 1

## h_story_D01_SijinLighthouse_t_finishObserverSequenceAndTimer
	* StepId: 12
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* h_story_D01_SijinLighthouse_t_escape1_wait1
		* h_story_D01_SijinLighthouse_t_finishObserverSequence
	* SuccLL: 
		* h_story_D01_SijinLighthouse_GAMA_12
		* h_story_D01_SijinLighthouse_act_enableAllyAfterSeq
		* h_story_D01_SijinLighthouse_act_enableEnemyAfterSeq
		* h_story_D01_SijinLighthouse_act_enablePlayerAfterSeq
		* h_story_D01_SijinLighthouse_s2_01_lighthouse_act_whatsthatobserver

## h_story_D01_SijinLighthouse_t_watiForSeq
	* StepId: 23
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_D01_SijinLighthouse_ObsSeq

## h_story_D01_SijinLighthouse_trigger_gate
	* StepId: 13
	* Type: Goal
	* TargetType: ReachPointOfInterest
	* SuccLL: 
		* h_story_D01_SijinLighthouse_GAMA_13
		* h_story_D01_SijinLighthouse_GAMA_19
		* h_story_D01_SijinLighthouse_remove_observer

## h_story_D01_SijinLighthouse_waitCinematicEnd
	* StepId: 16
	* Type: Trigger
	* TargetType: OnInGameSequenceFinishedForPlayer
	* TVS: 0
	* SuccLL: 
		* h_story_D01_SijinLighthouse_GAMA_16
		* h_story_D01_SijinLighthouse_GAMA_17
		* h_story_D01_SijinLighthouse_GAMA_18
		* h_story_D01_SijinLighthouse_enableEnemy
		* h_story_D01_SijinLighthouse_s2_01_lighthouse_act_escape_final

## h_story_D01_SijinLighthouse_Wave1_OrTime
	* StepId: 8
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* h_story_D01_SijinLighthouse_Wave1MaxTime
		* h_story_D01_SijinLighthouse_s2_01_lighthouse_kill_wave1
	* SuccLL: 
		* h_story_D01_SijinLighthouse_GAMA_27
		* h_story_D01_SijinLighthouse_GAMA_28
		* h_story_D01_SijinLighthouse_GAMA_8
		* h_story_D01_SijinLighthouse_s2_01_lighthouse_act_hodor2
		* h_story_D01_SijinLighthouse_s2_01_lighthouse_act_spawnWave2

## h_story_D01_SijinLighthouse_Wave1MaxTime
	* StepId: 31
	* Type: Trigger
	* TargetType: WaitForTime

## h_story_D01_SijinLighthouse_Wave2_OrTime
	* StepId: 9
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* h_story_D01_SijinLighthouse_Wave2MaxTime
		* h_story_D01_SijinLighthouse_s2_01_lighthouse_kill_wave2
	* SuccLL: 
		* h_story_D01_SijinLighthouse_GAMA_25
		* h_story_D01_SijinLighthouse_GAMA_26
		* h_story_D01_SijinLighthouse_GAMA_9
		* h_story_D01_SijinLighthouse_s2_01_lighthouse_act_hodor3
		* h_story_D01_SijinLighthouse_s2_01_lighthouse_act_spawnWave3

## h_story_D01_SijinLighthouse_Wave2MaxTime
	* StepId: 29
	* Type: Trigger
	* TargetType: WaitForTime

## h_story_D01_SijinLighthouse_Wave3_OrTime
	* StepId: 10
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* h_story_D01_SijinLighthouse_Wave3MaxTime
		* h_story_D01_SijinLighthouse_s2_01_lighthouse_kill_wave3
	* SuccLL: 
		* h_story_D01_SijinLighthouse_GAMA_10
		* h_story_D01_SijinLighthouse_GAMA_23
		* h_story_D01_SijinLighthouse_GAMA_24
		* h_story_D01_SijinLighthouse_s2_01_lighthouse_act_hodor4
		* h_story_D01_SijinLighthouse_s2_01_lighthouse_act_spawnWave4

## h_story_D01_SijinLighthouse_Wave3MaxTime
	* StepId: 27
	* Type: Trigger
	* TargetType: WaitForTime

## h_story_D01_SijinLighthouse_Wave4_OrTime
	* StepId: 11
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* h_story_D01_SijinLighthouse_Wave4MaxTime
		* h_story_D01_SijinLighthouse_s2_01_lighthouse_kill_wave4
	* SuccLL: 
		* h_story_D01_SijinLighthouse_GAMA_11
		* h_story_D01_SijinLighthouse_GAMA_20
		* h_story_D01_SijinLighthouse_GAMA_21
		* h_story_D01_SijinLighthouse_GAMA_22
		* h_story_D01_SijinLighthouse_act_disableAlly
		* h_story_D01_SijinLighthouse_act_disableEnemy
		* h_story_D01_SijinLighthouse_act_disablePlayer
		* h_story_D01_SijinLighthouse_act_obsDisableSensorManager
		* h_story_D01_SijinLighthouse_act_spawnObserver

## h_story_D01_SijinLighthouse_Wave4MaxTime
	* StepId: 25
	* Type: Trigger
	* TargetType: WaitForTime

## h_story_D02_IliyinLighthouse_2ef303072c3dbe34a98100baf725f42b
	* StepId: 39
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_D02_IliyinLighthouse_activate_player

## h_story_D02_IliyinLighthouse_90ca57b916198f649926c37254719b25
	* StepId: 42
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D02_IliyinLighthouse_GAMA_42
		* h_story_D02_IliyinLighthouse_s2_02_iliyin_act_wave2
		* h_story_D02_IliyinLighthouse_s2_02_iliyin_breakwater2_dia

## h_story_D02_IliyinLighthouse_9775f94fa14a0924faa55bbed5e10cc2
	* StepId: 20
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_story_D02_IliyinLighthouse_GAMA_20
		* h_story_D02_IliyinLighthouse_GAMA_35
		* h_story_D02_IliyinLighthouse_GAMA_36
		* h_story_D02_IliyinLighthouse_GAMA_37

## h_story_D02_IliyinLighthouse_collect_sample
	* StepId: 11
	* Type: Goal
	* TargetType: OnInteractionDone
	* TVS: iliyin_ruin_pickup
	* SuccLL: h_story_D02_IliyinLighthouse_GAMA_11

## h_story_D02_IliyinLighthouse_goal_countdown
	* StepId: 23
	* Type: Goal
	* TargetType: WaitForTime

## h_story_D02_IliyinLighthouse_goal_killWaves
	* StepId: 15
	* Type: Goal
	* TargetType: FinishGoalsString
	* TVS: h_story_D02_IliyinLighthouse_multi_killWaves
	* SuccLL: h_story_D02_IliyinLighthouse_GAMA_15

## h_story_D02_IliyinLighthouse_healthCheck
	* StepId: 35
	* Type: Trigger
	* TargetType: TaggedUnitsBelowStrength

## h_story_D02_IliyinLighthouse_i_observer
	* StepId: 25
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_story_D02_IliyinLighthouse_01db05a52c5efeb41828af9033b93b29
		* h_story_D02_IliyinLighthouse_1733a283ca3e65d4ca0ee02a7fa9c093
		* h_story_D02_IliyinLighthouse_88613b29320e93a489bb8598cc1e96e0
		* h_story_D02_IliyinLighthouse_GAMA_25
		* h_story_D02_IliyinLighthouse_GAMA_30
		* h_story_D02_IliyinLighthouse_disableLineOfSight
		* h_story_D02_IliyinLighthouse_disableSensorManager
		* h_story_D02_IliyinLighthouse_h_graph_story_s2_02_Iliyin_HighlightObserver

## h_story_D02_IliyinLighthouse_kill_KharKaalad
	* StepId: 2
	* Type: Trigger
	* TargetType: TaggedUnitsBelowHealthAndArmor
	* SuccLL: 
		* h_story_D02_IliyinLighthouse_GAMA_2
		* h_story_D02_IliyinLighthouse_GAMA_3
		* h_story_D02_IliyinLighthouse_GAMA_4
		* h_story_D02_IliyinLighthouse_d_fail

## h_story_D02_IliyinLighthouse_kill_wave1
	* StepId: 41
	* Type: Trigger
	* TargetType: KillSpecificWave
	* SuccLL: h_story_D02_IliyinLighthouse_GAMA_41

## h_story_D02_IliyinLighthouse_kill_wave2
	* StepId: 43
	* Type: Trigger
	* TargetType: KillSpecificWave

## h_story_D02_IliyinLighthouse_multi_fail
	* StepId: 3
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* h_story_D02_IliyinLighthouse_td_fail
		* h_story_D02_IliyinLighthouse_w_fail
	* SuccLL: h_story_D02_IliyinLighthouse_s2_02_iliyin_allyDeath_mission_failed

## h_story_D02_IliyinLighthouse_multi_killWaves
	* StepId: 40
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* h_story_D02_IliyinLighthouse_kill_wave1
		* h_story_D02_IliyinLighthouse_kill_wave2

## h_story_D02_IliyinLighthouse_mutli_countdown
	* StepId: 24
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* h_story_D02_IliyinLighthouse_healthCheck
		* h_story_D02_IliyinLighthouse_w_observerSpawn
	* SuccLL: h_story_D02_IliyinLighthouse_GAMA_24

## h_story_D02_IliyinLighthouse_s2_02_iliyin_breakwater3_dia_wait
	* StepId: 17
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: st_iliyin_breakwater_3_dialog
	* SuccLL: 
		* h_story_D02_IliyinLighthouse_GAMA_17
		* h_story_D02_IliyinLighthouse_ai_Passive

## h_story_D02_IliyinLighthouse_s2_02_iliyin_intro_dia_timer
	* StepId: 9
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D02_IliyinLighthouse_GAMA_9
		* h_story_D02_IliyinLighthouse_activate_KharKaalad
		* h_story_D02_IliyinLighthouse_s2_02_iliyin_intro2_dia

## h_story_D02_IliyinLighthouse_s2_02_iliyin_intro1_dia_wait
	* StepId: 8
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: st_iliyin_intro_1_dialog
	* SuccLL: h_story_D02_IliyinLighthouse_GAMA_8

## h_story_D02_IliyinLighthouse_s2_02_iliyin_intro2_dia_wait
	* StepId: 10
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: st_iliyin_intro_2_dialog
	* SuccLL: 
		* h_story_D02_IliyinLighthouse_GAMA_10
		* h_story_D02_IliyinLighthouse_interaction_sample
		* h_story_D02_IliyinLighthouse_s2_02_iliyin_investigation1_dia

## h_story_D02_IliyinLighthouse_s2_02_iliyin_kill_inhib1
	* StepId: 36
	* Type: Trigger
	* TargetType: KillSpecificWave

## h_story_D02_IliyinLighthouse_s2_02_iliyin_kill_inhib2
	* StepId: 37
	* Type: Trigger
	* TargetType: KillSpecificWave

## h_story_D02_IliyinLighthouse_s2_02_iliyin_kill_inhib3
	* StepId: 38
	* Type: Trigger
	* TargetType: KillSpecificWave

## h_story_D02_IliyinLighthouse_s2_02_iliyin_observer2_dia_wait
	* StepId: 30
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: st_iliyin_observer_2_dialog
	* SuccLL: h_story_D02_IliyinLighthouse_s2_02_iliyin_finishMission

## h_story_D02_IliyinLighthouse_s2_02_iliyin_trig_warp3_destroyed
	* StepId: 21
	* Type: Goal
	* TargetType: FinishGoalsString
	* TVS: 
		* h_story_D02_IliyinLighthouse_s2_02_iliyin_kill_inhib1
		* h_story_D02_IliyinLighthouse_s2_02_iliyin_kill_inhib2
		* h_story_D02_IliyinLighthouse_s2_02_iliyin_kill_inhib3
	* SuccLL: 
		* h_story_D02_IliyinLighthouse_GAMA_21
		* h_story_D02_IliyinLighthouse_s2_02_iliyin_act_wave3

## h_story_D02_IliyinLighthouse_s2_02_iliyin_wave2_dia_timer
	* StepId: 18
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D02_IliyinLighthouse_GAMA_18
		* h_story_D02_IliyinLighthouse_desctivate_player
		* h_story_D02_IliyinLighthouse_focus_inhib1
		* h_story_D02_IliyinLighthouse_s2_02_iliyin_spawn_warp_inhib1
		* h_story_D02_IliyinLighthouse_s2_02_iliyin_spawn_warp_inhib2
		* h_story_D02_IliyinLighthouse_s2_02_iliyin_spawn_warp_inhib3
		* h_story_D02_IliyinLighthouse_s2_02_iliyin_spawn_warp_inhib_guards

## h_story_D02_IliyinLighthouse_s2_02_iliyin_wave3_spawnMore_wait
	* StepId: 33
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D02_IliyinLighthouse_GAMA_33
		* h_story_D02_IliyinLighthouse_s2_02_iliyin_act_wave4

## h_story_D02_IliyinLighthouse_st_iliyin_investigation2_dia_wait
	* StepId: 13
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: st_iliyin_investigation_2_dialog
	* SuccLL: 
		* h_story_D02_IliyinLighthouse_GAMA_13
		* h_story_D02_IliyinLighthouse_s2_02_iliyin_amassari_1_dia

## h_story_D02_IliyinLighthouse_st_iliyin_the_amassari1_dia_wait
	* StepId: 14
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: st_iliyin_amassari_1_dialog
	* SuccLL: 
		* h_story_D02_IliyinLighthouse_GAMA_14
		* h_story_D02_IliyinLighthouse_GAMA_39
		* h_story_D02_IliyinLighthouse_GAMA_40
		* h_story_D02_IliyinLighthouse_s2_02_iliyin_act_wave1
		* h_story_D02_IliyinLighthouse_s2_02_iliyin_breakwater1_dia

## h_story_D02_IliyinLighthouse_start
	* StepId: 0
	* Type: Trigger
	* TargetType: MissionStart
	* SuccLL: 
		* h_story_D02_IliyinLighthouse_GAMA_0
		* h_story_D02_IliyinLighthouse_GAMA_5
		* h_story_D02_IliyinLighthouse_s2_02_iliyin_act_spawnAlly

## h_story_D02_IliyinLighthouse_td_fail
	* StepId: 4
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: st_iliyin_fail_1_dialog

## h_story_D02_IliyinLighthouse_w_collect
	* StepId: 12
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D02_IliyinLighthouse_GAMA_12
		* h_story_D02_IliyinLighthouse_s2_02_iliyin_investigation2_dia

## h_story_D02_IliyinLighthouse_w_countdown
	* StepId: 22
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D02_IliyinLighthouse_GAMA_22
		* h_story_D02_IliyinLighthouse_GAMA_23
		* h_story_D02_IliyinLighthouse_GAMA_31
		* h_story_D02_IliyinLighthouse_GAMA_32
		* h_story_D02_IliyinLighthouse_ai_FollowFlagship
		* h_story_D02_IliyinLighthouse_d_countdown

## h_story_D02_IliyinLighthouse_w_fail
	* StepId: 5
	* Type: Trigger
	* TargetType: WaitForTime

## h_story_D02_IliyinLighthouse_w_healthCheck
	* StepId: 34
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_D02_IliyinLighthouse_GAMA_34

## h_story_D02_IliyinLighthouse_w_inhib
	* StepId: 19
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D02_IliyinLighthouse_GAMA_19
		* h_story_D02_IliyinLighthouse_GAMA_38
		* h_story_D02_IliyinLighthouse_s2_02_iliyin_anchors1_dia

## h_story_D02_IliyinLighthouse_w_intro1
	* StepId: 6
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D02_IliyinLighthouse_GAMA_6
		* h_story_D02_IliyinLighthouse_deactivate_KharKaalad
		* h_story_D02_IliyinLighthouse_lookAt_KharKaalad2

## h_story_D02_IliyinLighthouse_w_intro2
	* StepId: 7
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D02_IliyinLighthouse_GAMA_7
		* h_story_D02_IliyinLighthouse_s2_02_iliyin_intro1_dia

## h_story_D02_IliyinLighthouse_w_killKharKaalad
	* StepId: 1
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_D02_IliyinLighthouse_GAMA_1

## h_story_D02_IliyinLighthouse_w_killWaves
	* StepId: 16
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D02_IliyinLighthouse_GAMA_16
		* h_story_D02_IliyinLighthouse_s2_02_iliyin_breakwater3_dia

## h_story_D02_IliyinLighthouse_w_observer2
	* StepId: 26
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D02_IliyinLighthouse_GAMA_26
		* h_story_D02_IliyinLighthouse_s2_02_iliyin_act_spawnObs

## h_story_D02_IliyinLighthouse_w_observer2b
	* StepId: 31
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_D02_IliyinLighthouse_s2_02_iliyin_observer1_dia

## h_story_D02_IliyinLighthouse_w_observer3
	* StepId: 27
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D02_IliyinLighthouse_GAMA_27
		* h_story_D02_IliyinLighthouse_s2_02_iliyin_act_delUnits
		* h_story_D02_IliyinLighthouse_s2_02_iliyin_act_spawnAma

## h_story_D02_IliyinLighthouse_w_observer4b
	* StepId: 28
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D02_IliyinLighthouse_GAMA_28
		* h_story_D02_IliyinLighthouse_bda0493e21acd47459ca37bb5b165aa5
		* h_story_D02_IliyinLighthouse_s2_02_iliyin_act_delObs

## h_story_D02_IliyinLighthouse_w_observer5
	* StepId: 29
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D02_IliyinLighthouse_GAMA_29
		* h_story_D02_IliyinLighthouse_cameraLookAtAma
		* h_story_D02_IliyinLighthouse_s2_02_iliyin_observer2_dia

## h_story_D02_IliyinLighthouse_w_observerSpawn
	* StepId: 32
	* Type: Trigger
	* TargetType: WaitForTime

## h_story_D03_BrightTemple_01d40ea367dc0ec4686d21fff7020aab
	* StepId: 1
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: st_bTemple_blHgn_3_dialog
	* SuccLL: h_story_D03_BrightTemple_GAMA_1

## h_story_D03_BrightTemple_escape_allyReach
	* StepId: 35
	* Type: Trigger
	* TargetType: ReachPointOfInterest
	* SuccLL: h_story_D03_BrightTemple_disableKharKaalad03

## h_story_D03_BrightTemple_finishedStartSequence
	* StepId: 11
	* Type: Trigger
	* TargetType: OnInGameSequenceFinishedForPlayer
	* TVS: 1
	* SuccLL: 
		* h_story_D03_BrightTemple_GAMA_11
		* h_story_D03_BrightTemple_close_intro
		* h_story_D03_BrightTemple_deactivate_sequenceDialog
		* h_story_D03_BrightTemple_enableLOS
		* h_story_D03_BrightTemple_lookAt_temple

## h_story_D03_BrightTemple_goal_killInhibitors
	* StepId: 20
	* Type: Goal
	* TargetType: FinishGoalsString
	* TVS: 
		* h_story_D03_BrightTemple_t_KillInhibitor01
		* h_story_D03_BrightTemple_t_KillInhibitor02
	* SuccLL: h_story_D03_BrightTemple_GAMA_20

## h_story_D03_BrightTemple_goal_KillWaves
	* StepId: 16
	* Type: Goal
	* TargetType: FinishGoalsString
	* TVS: h_story_D03_BrightTemple_multi_killWaves
	* SuccLL: h_story_D03_BrightTemple_GAMA_16

## h_story_D03_BrightTemple_goal_ReachEscapePos
	* StepId: 18
	* Type: Goal
	* TargetType: ReachPointOfInterest
	* SuccLL: h_story_D03_BrightTemple_GAMA_18

## h_story_D03_BrightTemple_goal_ReachStartPos
	* StepId: 13
	* Type: Goal
	* TargetType: ReachPointOfInterest
	* SuccLL: 
		* h_story_D03_BrightTemple_GAMA_13
		* h_story_D03_BrightTemple_d_chall1

## h_story_D03_BrightTemple_healthCheck_KharKaalad
	* StepId: 6
	* Type: Trigger
	* TargetType: TaggedUnitsBelowHealthAndArmor
	* SuccLL: 
		* h_story_D03_BrightTemple_GAMA_6
		* h_story_D03_BrightTemple_GAMA_7
		* h_story_D03_BrightTemple_GAMA_8
		* h_story_D03_BrightTemple_d_fail

## h_story_D03_BrightTemple_i_combatSetup
	* StepId: 15
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_story_D03_BrightTemple_GAMA_15
		* h_story_D03_BrightTemple_GAMA_35
		* h_story_D03_BrightTemple_GAMA_36
		* h_story_D03_BrightTemple_GAMA_37
		* h_story_D03_BrightTemple_GAMA_38
		* h_story_D03_BrightTemple_GAMA_39
		* h_story_D03_BrightTemple_removeFakeFriendly
		* h_story_D03_BrightTemple_td_chall_2_dialog

## h_story_D03_BrightTemple_i_KharKaalad
	* StepId: 34
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D03_BrightTemple_activate_KharKaalad
		* h_story_D03_BrightTemple_deactivate_reachTrigger

## h_story_D03_BrightTemple_i_setup
	* StepId: 10
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_story_D03_BrightTemple_disableLOS
		* h_story_D03_BrightTemple_spawnFakeAmassari
		* h_story_D03_BrightTemple_spawnKharKalaad

## h_story_D03_BrightTemple_multi_fail
	* StepId: 7
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* h_story_D03_BrightTemple_td_fail
		* h_story_D03_BrightTemple_w_fail
	* SuccLL: h_story_D03_BrightTemple_fail

## h_story_D03_BrightTemple_multi_killWaves
	* StepId: 36
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* h_story_D03_BrightTemple_trigger_KillWave0
		* h_story_D03_BrightTemple_trigger_KillWave1

## h_story_D03_BrightTemple_multi_preSequence
	* StepId: 22
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* h_story_D03_BrightTemple_td_caval1
		* h_story_D03_BrightTemple_w_preSequence
	* SuccLL: 
		* h_story_D03_BrightTemple_GAMA_22
		* h_story_D03_BrightTemple_GAMA_27
		* h_story_D03_BrightTemple_disablePlayer2
		* h_story_D03_BrightTemple_makePlayer3God
		* h_story_D03_BrightTemple_spawnKidara

## h_story_D03_BrightTemple_s2_03_bTemple_start_immediate
	* StepId: 0
	* Type: Trigger
	* TargetType: MissionStart
	* SuccLL: 
		* h_story_D03_BrightTemple_GAMA_0
		* h_story_D03_BrightTemple_GAMA_10
		* h_story_D03_BrightTemple_GAMA_4
		* h_story_D03_BrightTemple_GAMA_41
		* h_story_D03_BrightTemple_GAMA_9
		* h_story_D03_BrightTemple_startIntroSequence

## h_story_D03_BrightTemple_t_KillInhibitor01
	* StepId: 32
	* Type: Trigger
	* TargetType: KillSpecificWave

## h_story_D03_BrightTemple_t_KillInhibitor02
	* StepId: 33
	* Type: Trigger
	* TargetType: KillSpecificWave

## h_story_D03_BrightTemple_td_caval1
	* StepId: 31
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: st_bTemple_caval_1_dialog

## h_story_D03_BrightTemple_td_chall1
	* StepId: 14
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: st_bTemple_chall_1_dialog
	* SuccLL: h_story_D03_BrightTemple_GAMA_14

## h_story_D03_BrightTemple_td_fail
	* StepId: 8
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: st_bTemple_fail_1_dialog

## h_story_D03_BrightTemple_trig_KillAllEnemies
	* StepId: 25
	* Type: Goal
	* TargetType: WaveFinished
	* SuccLL: 
		* h_story_D03_BrightTemple_GAMA_25
		* h_story_D03_BrightTemple_deactivate_allies
		* h_story_D03_BrightTemple_deactivate_kidara

## h_story_D03_BrightTemple_trig_waitForCinematic
	* StepId: 3
	* Type: Trigger
	* TargetType: OnInGameSequenceFinishedForPlayer
	* TVS: 0
	* SuccLL: 
		* h_story_D03_BrightTemple_GAMA_3
		* h_story_D03_BrightTemple_remove_kidara1
		* h_story_D03_BrightTemple_remove_kidara2
		* h_story_D03_BrightTemple_remove_kidara3

## h_story_D03_BrightTemple_trigger_KillWave0
	* StepId: 37
	* Type: Trigger
	* TargetType: KillSpecificWave

## h_story_D03_BrightTemple_trigger_KillWave1
	* StepId: 38
	* Type: Trigger
	* TargetType: KillSpecificWave

## h_story_D03_BrightTemple_trigger_reachPosDisableKharKaalad
	* StepId: 41
	* Type: Trigger
	* TargetType: ReachPointOfInterest
	* SuccLL: 
		* h_story_D03_BrightTemple_ChangeKharKalaadAIType01
		* h_story_D03_BrightTemple_disableKharKaalad02

## h_story_D03_BrightTemple_w_blHgn_4_dialog
	* StepId: 26
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_D03_BrightTemple_td_blHgn_4_dialog

## h_story_D03_BrightTemple_w_cinematic
	* StepId: 2
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D03_BrightTemple_GAMA_2
		* h_story_D03_BrightTemple_StartCinematic

## h_story_D03_BrightTemple_w_combatAI
	* StepId: 27
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_D03_BrightTemple_ai_FollowFlagship

## h_story_D03_BrightTemple_w_EndingDialog01
	* StepId: 24
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D03_BrightTemple_GAMA_24
		* h_story_D03_BrightTemple_GAMA_26
		* h_story_D03_BrightTemple_td_blHgn_3_dialog

## h_story_D03_BrightTemple_w_fail
	* StepId: 9
	* Type: Trigger
	* TargetType: WaitForTime

## h_story_D03_BrightTemple_w_fin
	* StepId: 4
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_D03_BrightTemple_win

## h_story_D03_BrightTemple_w_firstWaves
	* StepId: 39
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D03_BrightTemple_spawnWave0
		* h_story_D03_BrightTemple_spawnWave1

## h_story_D03_BrightTemple_w_forKidaraSequence
	* StepId: 28
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D03_BrightTemple_GAMA_28
		* h_story_D03_BrightTemple_closeCurrentDialog
		* h_story_D03_BrightTemple_showKidaraSequence

## h_story_D03_BrightTemple_w_healthCheckKharKaalad
	* StepId: 5
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_D03_BrightTemple_GAMA_5

## h_story_D03_BrightTemple_w_intro1
	* StepId: 42
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D03_BrightTemple_GAMA_42
		* h_story_D03_BrightTemple_disableEnemy1
		* h_story_D03_BrightTemple_disableKharKaalad01

## h_story_D03_BrightTemple_w_intro2
	* StepId: 43
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D03_BrightTemple_GAMA_43
		* h_story_D03_BrightTemple_td_intro_1_2_dialog

## h_story_D03_BrightTemple_w_intro3
	* StepId: 44
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_D03_BrightTemple_cce798ce978c65946b91da78c96581d2

## h_story_D03_BrightTemple_w_KidaraIntro
	* StepId: 29
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_D03_BrightTemple_td_blHgn_1_dialog

## h_story_D03_BrightTemple_w_killInhibitors1
	* StepId: 21
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D03_BrightTemple_GAMA_21
		* h_story_D03_BrightTemple_GAMA_29
		* h_story_D03_BrightTemple_GAMA_30
		* h_story_D03_BrightTemple_d_caval1

## h_story_D03_BrightTemple_w_preSequence
	* StepId: 30
	* Type: Trigger
	* TargetType: WaitForTime

## h_story_D03_BrightTemple_w_reactivateKharKalaad
	* StepId: 40
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_D03_BrightTemple_enableKharKaalad03

## h_story_D03_BrightTemple_w_startSecondDialog
	* StepId: 12
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D03_BrightTemple_GAMA_12
		* h_story_D03_BrightTemple_GAMA_40
		* h_story_D03_BrightTemple_enableKharKaalad01
		* h_story_D03_BrightTemple_td_appro_1_dialog

## h_story_D03_BrightTemple_w_TimeForEscape
	* StepId: 19
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D03_BrightTemple_ChangeKharKalaadAIType03
		* h_story_D03_BrightTemple_GAMA_19
		* h_story_D03_BrightTemple_GAMA_31
		* h_story_D03_BrightTemple_GAMA_32
		* h_story_D03_BrightTemple_GAMA_33
		* h_story_D03_BrightTemple_SpawnInhibitor01
		* h_story_D03_BrightTemple_SpawnInhibitor02
		* h_story_D03_BrightTemple_spawnAmaWave02
		* h_story_D03_BrightTemple_td_escap_1_2_dialog

## h_story_D03_BrightTemple_w_TimeForRetreat
	* StepId: 17
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D03_BrightTemple_ChangeKharKalaadAIType02
		* h_story_D03_BrightTemple_GAMA_17
		* h_story_D03_BrightTemple_GAMA_34
		* h_story_D03_BrightTemple_lookAt_escapePos
		* h_story_D03_BrightTemple_td_retre_1_dialog

## h_story_D03_BrightTemple_waitForKidaraSequenceFinished
	* StepId: 23
	* Type: Trigger
	* TargetType: OnInGameSequenceFinishedForPlayer
	* TVS: 1
	* SuccLL: 
		* h_story_D03_BrightTemple_GAMA_23
		* h_story_D03_BrightTemple_MakePlayer3Vulnerable
		* h_story_D03_BrightTemple_close_endSequence
		* h_story_D03_BrightTemple_deactivate_sequenceDialog2
		* h_story_D03_BrightTemple_enablePlayer2
		* h_story_D03_BrightTemple_makePlayer2PassiveAgain
		* h_story_D03_BrightTemple_spawnAmaExtraWave
		* h_story_D03_BrightTemple_spawnAmaWave02Again

## h_story_D04_Hataldan_a84cc3294bf3aef4c9c662678d751929
	* StepId: 19
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D04_Hataldan_wave4_Drones4
		* h_story_D04_Hataldan_wave5_Drones4
		* h_story_D04_Hataldan_wave6_Drones4

## h_story_D04_Hataldan_exist_Enemies
	* StepId: 40
	* Type: Trigger
	* TargetType: UnitWithTagsExists
	* SuccLL: 
		* h_story_D04_Hataldan_GAMA_40
		* h_story_D04_Hataldan_deactivate_

## h_story_D04_Hataldan_goal_empActive1
	* StepId: 9
	* Type: Goal
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D04_Hataldan_GAMA_24
		* h_story_D04_Hataldan_GAMA_25
		* h_story_D04_Hataldan_GAMA_9

## h_story_D04_Hataldan_goal_empActive2
	* StepId: 11
	* Type: Goal
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D04_Hataldan_GAMA_11
		* h_story_D04_Hataldan_GAMA_20
		* h_story_D04_Hataldan_GAMA_21

## h_story_D04_Hataldan_goal_empActive3
	* StepId: 13
	* Type: Goal
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D04_Hataldan_GAMA_13
		* h_story_D04_Hataldan_GAMA_17

## h_story_D04_Hataldan_goal_empLoading1
	* StepId: 8
	* Type: Goal
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D04_Hataldan_GAMA_26
		* h_story_D04_Hataldan_GAMA_27
		* h_story_D04_Hataldan_GAMA_8

## h_story_D04_Hataldan_goal_empLoading2
	* StepId: 10
	* Type: Goal
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D04_Hataldan_GAMA_10
		* h_story_D04_Hataldan_GAMA_22
		* h_story_D04_Hataldan_GAMA_23

## h_story_D04_Hataldan_goal_empLoading3
	* StepId: 12
	* Type: Goal
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D04_Hataldan_GAMA_12
		* h_story_D04_Hataldan_GAMA_19

## h_story_D04_Hataldan_goal_killKeepers
	* StepId: 33
	* Type: Goal
	* TargetType: FinishGoalsString
	* TVS: 
		* h_story_D04_Hataldan_kill_keeper1
		* h_story_D04_Hataldan_kill_keeper2
	* SuccLL: 
		* h_story_D04_Hataldan_GAMA_33
		* h_story_D04_Hataldan_deactivate_empLoop

## h_story_D04_Hataldan_goal_killRemaining
	* StepId: 41
	* Type: Goal
	* TargetType: WaveFinished
	* SuccLL: h_story_D04_Hataldan_GAMA_41

## h_story_D04_Hataldan_goal_position
	* StepId: 2
	* Type: Goal
	* TargetType: ReachPointOfInterest
	* SuccLL: 
		* h_story_D04_Hataldan_GAMA_2
		* h_story_D04_Hataldan_GAMA_47
		* h_story_D04_Hataldan_close_sequenceObserver
		* h_story_D04_Hataldan_move_flagship
		* h_story_D04_Hataldan_sequence_observer

## h_story_D04_Hataldan_healthCheck_KharKalaad
	* StepId: 61
	* Type: Trigger
	* TargetType: TaggedUnitsBelowStrength
	* SuccLL: 
		* h_story_D04_Hataldan_GAMA_61
		* h_story_D04_Hataldan_GAMA_62
		* h_story_D04_Hataldan_GAMA_63
		* h_story_D04_Hataldan_d_failKharKalaad

## h_story_D04_Hataldan_i_empFired1
	* StepId: 28
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_story_D04_Hataldan_addStatMod_emp1
		* h_story_D04_Hataldan_d_empFired1
		* h_story_D04_Hataldan_effect_empPulse1
		* h_story_D04_Hataldan_effect_empStun1

## h_story_D04_Hataldan_i_empFired2
	* StepId: 24
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_story_D04_Hataldan_addStatMod_emp2
		* h_story_D04_Hataldan_d_empFired2
		* h_story_D04_Hataldan_effect_empPulse2
		* h_story_D04_Hataldan_effect_empStun2

## h_story_D04_Hataldan_i_empFired3
	* StepId: 20
	* Type: None
	* TargetType: Immediate
	* SuccLL: 
		* h_story_D04_Hataldan_addStatMod_emp3
		* h_story_D04_Hataldan_d_empFired3
		* h_story_D04_Hataldan_effect_empPulse3
		* h_story_D04_Hataldan_effect_empStun3

## h_story_D04_Hataldan_i_fightStart
	* StepId: 6
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_story_D04_Hataldan_GAMA_29
		* h_story_D04_Hataldan_GAMA_30
		* h_story_D04_Hataldan_GAMA_31
		* h_story_D04_Hataldan_GAMA_6
		* h_story_D04_Hataldan_d_fight

## h_story_D04_Hataldan_i_phase2
	* StepId: 26
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_story_D04_Hataldan_activateKeepers
		* h_story_D04_Hataldan_removeStatModd_emp
		* h_story_D04_Hataldan_wave4_Drones2
		* h_story_D04_Hataldan_wave5_Drones2
		* h_story_D04_Hataldan_wave6_Drones2

## h_story_D04_Hataldan_i_phase3
	* StepId: 22
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_story_D04_Hataldan_activateKeepers2
		* h_story_D04_Hataldan_removeStatModd_emp2
		* h_story_D04_Hataldan_wave4_Drones3
		* h_story_D04_Hataldan_wave5_Drones3
		* h_story_D04_Hataldan_wave6_Drones3

## h_story_D04_Hataldan_i_phaseEnd
	* StepId: 18
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_story_D04_Hataldan_GAMA_18
		* h_story_D04_Hataldan_activate_KeepersEnd
		* h_story_D04_Hataldan_removeStatModd_emp3
		* h_story_D04_Hataldan_wave5_failBoss

## h_story_D04_Hataldan_i_sequenceEnd
	* StepId: 4
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D04_Hataldan_GAMA_4
		* h_story_D04_Hataldan_GAMA_44
		* h_story_D04_Hataldan_GAMA_45
		* h_story_D04_Hataldan_activate_Amassari
		* h_story_D04_Hataldan_d_empTut
		* h_story_D04_Hataldan_remove_alliedKeepers

## h_story_D04_Hataldan_i_setupAllies
	* StepId: 59
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_story_D04_Hataldan_ally0_KharKalaad
		* h_story_D04_Hataldan_ally1_Kidara
		* h_story_D04_Hataldan_ally2_Observer
		* h_story_D04_Hataldan_ally3_Amassari
		* h_story_D04_Hataldan_ally4_Amassari
		* h_story_D04_Hataldan_ally5_Amassari
		* h_story_D04_Hataldan_ally6_Amassari
		* h_story_D04_Hataldan_ally7_keeper
		* h_story_D04_Hataldan_ally8_keeper
		* h_story_D04_Hataldan_deactivate_amassariStart
		* h_story_D04_Hataldan_deactivate_kidataStart
		* h_story_D04_Hataldan_deactivate_vashtiStart

## h_story_D04_Hataldan_i_setupEnemies
	* StepId: 31
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_story_D04_Hataldan_deactivate_Keepers1
		* h_story_D04_Hataldan_wave0_keeper
		* h_story_D04_Hataldan_wave1_keeper

## h_story_D04_Hataldan_i_winConditions
	* StepId: 32
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_story_D04_Hataldan_GAMA_32
		* h_story_D04_Hataldan_GAMA_42
		* h_story_D04_Hataldan_GAMA_43

## h_story_D04_Hataldan_kill_keeper1
	* StepId: 43
	* Type: Trigger
	* TargetType: KillSpecificWave

## h_story_D04_Hataldan_kill_keeper2
	* StepId: 44
	* Type: Trigger
	* TargetType: KillSpecificWave

## h_story_D04_Hataldan_multi_allEnemiesDead
	* StepId: 35
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* h_story_D04_Hataldan_w_killRemaining
		* h_story_D04_Hataldan_w_triggerWinFight
	* SuccLL: 
		* h_story_D04_Hataldan_GAMA_35
		* h_story_D04_Hataldan_d_fightWon

## h_story_D04_Hataldan_multi_dialogAndAmassari
	* StepId: 5
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* h_story_D04_Hataldan_td_empTut
		* h_story_D04_Hataldan_w_amassari
	* SuccLL: h_story_D04_Hataldan_GAMA_5

## h_story_D04_Hataldan_multi_fail
	* StepId: 15
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* h_story_D04_Hataldan_td_fail
		* h_story_D04_Hataldan_w_failTrigger
	* SuccLL: h_story_D04_Hataldan_fail

## h_story_D04_Hataldan_multi_failKharKalaad
	* StepId: 62
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* h_story_D04_Hataldan_td_failKharKalaad
		* h_story_D04_Hataldan_w_failKharKalaad
	* SuccLL: h_story_D04_Hataldan_fail_KharKalaad

## h_story_D04_Hataldan_position_playerClose
	* StepId: 54
	* Type: Trigger
	* TargetType: ReachPointOfInterest
	* SuccLL: h_story_D04_Hataldan_d_interlude

## h_story_D04_Hataldan_position_playerMoved
	* StepId: 53
	* Type: Trigger
	* TargetType: ReachPointOfInterest
	* SuccLL: 
		* h_story_D04_Hataldan_activate_KharKalaad
		* h_story_D04_Hataldan_activate_Kidara

## h_story_D04_Hataldan_sequenceEnd_intro
	* StepId: 1
	* Type: Trigger
	* TargetType: OnInGameSequenceFinishedForPlayer
	* TVS: 1
	* SuccLL: 
		* h_story_D04_Hataldan_GAMA_1
		* h_story_D04_Hataldan_GAMA_52
		* h_story_D04_Hataldan_GAMA_53
		* h_story_D04_Hataldan_GAMA_54
		* h_story_D04_Hataldan_close_sequence1
		* h_story_D04_Hataldan_deactivate_sequence1Dialog
		* h_story_D04_Hataldan_lookAt_position

## h_story_D04_Hataldan_sequenceEnd_observer
	* StepId: 3
	* Type: Trigger
	* TargetType: OnInGameSequenceFinishedForPlayer
	* TVS: 1
	* SuccLL: 
		* h_story_D04_Hataldan_GAMA_3
		* h_story_D04_Hataldan_close_sequence2
		* h_story_D04_Hataldan_deactivate_sequence2Dialog
		* h_story_D04_Hataldan_lookAt_enemies
		* h_story_D04_Hataldan_remove_Kidara2
		* h_story_D04_Hataldan_remove_Observer

## h_story_D04_Hataldan_start
	* StepId: 0
	* Type: Trigger
	* TargetType: MissionStart
	* SuccLL: 
		* h_story_D04_Hataldan_GAMA_0
		* h_story_D04_Hataldan_GAMA_55
		* h_story_D04_Hataldan_GAMA_58
		* h_story_D04_Hataldan_GAMA_59
		* h_story_D04_Hataldan_sequence_intro

## h_story_D04_Hataldan_td_conclusion
	* StepId: 38
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: s_hataldan_dialog_conclusion
	* SuccLL: h_story_D04_Hataldan_fin

## h_story_D04_Hataldan_td_empTut
	* StepId: 45
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: s_hataldan_dialog_empTut

## h_story_D04_Hataldan_td_fail
	* StepId: 16
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: st_hataldan_fail_2_dialog

## h_story_D04_Hataldan_td_failKharKalaad
	* StepId: 63
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: s_hataldan_dialog_failKharKalaad

## h_story_D04_Hataldan_td_fightWon
	* StepId: 36
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: s_hataldan_dialog_fightWon
	* SuccLL: h_story_D04_Hataldan_GAMA_36

## h_story_D04_Hataldan_w_amassari
	* StepId: 46
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_D04_Hataldan_GAMA_46

## h_story_D04_Hataldan_w_amassariKeeperBuffer
	* StepId: 47
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_D04_Hataldan_deactivate_Amassari

## h_story_D04_Hataldan_w_approachDialog
	* StepId: 55
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_D04_Hataldan_d_approach

## h_story_D04_Hataldan_w_checkKharKalaad
	* StepId: 60
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_D04_Hataldan_GAMA_60

## h_story_D04_Hataldan_w_conclusion
	* StepId: 37
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D04_Hataldan_GAMA_37
		* h_story_D04_Hataldan_d_conclusion

## h_story_D04_Hataldan_w_empLoopStart
	* StepId: 7
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D04_Hataldan_GAMA_28
		* h_story_D04_Hataldan_GAMA_7

## h_story_D04_Hataldan_w_empOff1
	* StepId: 27
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_D04_Hataldan_d_empOff1

## h_story_D04_Hataldan_w_empOff2
	* StepId: 23
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_D04_Hataldan_d_empOff2

## h_story_D04_Hataldan_w_enemyActivate
	* StepId: 30
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D04_Hataldan_activateKeepers1
		* h_story_D04_Hataldan_wave4_drones
		* h_story_D04_Hataldan_wave5_drones
		* h_story_D04_Hataldan_wave6_drones

## h_story_D04_Hataldan_w_fail
	* StepId: 14
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D04_Hataldan_GAMA_14
		* h_story_D04_Hataldan_GAMA_15
		* h_story_D04_Hataldan_GAMA_16
		* h_story_D04_Hataldan_d_fail

## h_story_D04_Hataldan_w_failKharKalaad
	* StepId: 64
	* Type: Trigger
	* TargetType: WaitForTime

## h_story_D04_Hataldan_w_failTrigger
	* StepId: 17
	* Type: Trigger
	* TargetType: WaitForTime

## h_story_D04_Hataldan_w_keeperDisable1
	* StepId: 29
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_D04_Hataldan_deactivateKeepers1

## h_story_D04_Hataldan_w_keeperDisable2
	* StepId: 25
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_D04_Hataldan_deactivateKeepers2

## h_story_D04_Hataldan_w_keeperDisable3
	* StepId: 21
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_D04_Hataldan_deactivateKeepers3

## h_story_D04_Hataldan_w_killKeepers
	* StepId: 34
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D04_Hataldan_GAMA_34
		* h_story_D04_Hataldan_GAMA_38
		* h_story_D04_Hataldan_GAMA_39

## h_story_D04_Hataldan_w_killRemaining
	* StepId: 42
	* Type: Trigger
	* TargetType: WaitForTime

## h_story_D04_Hataldan_w_seq1_1
	* StepId: 56
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D04_Hataldan_GAMA_56
		* h_story_D04_Hataldan_d_intro1

## h_story_D04_Hataldan_w_seq1_2
	* StepId: 57
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D04_Hataldan_GAMA_57
		* h_story_D04_Hataldan_d_intro2

## h_story_D04_Hataldan_w_seq1_3
	* StepId: 58
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_D04_Hataldan_d_intro3

## h_story_D04_Hataldan_w_seq2_1
	* StepId: 48
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D04_Hataldan_GAMA_48
		* h_story_D04_Hataldan_d_observer1

## h_story_D04_Hataldan_w_seq2_2
	* StepId: 49
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D04_Hataldan_GAMA_49
		* h_story_D04_Hataldan_d_observer122

## h_story_D04_Hataldan_w_seq2_3
	* StepId: 50
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D04_Hataldan_GAMA_50
		* h_story_D04_Hataldan_d_abduction1

## h_story_D04_Hataldan_w_seq2_4
	* StepId: 51
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D04_Hataldan_GAMA_51
		* h_story_D04_Hataldan_d_abduction2

## h_story_D04_Hataldan_w_seq2_5
	* StepId: 52
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_D04_Hataldan_d_abduction3

## h_story_D04_Hataldan_w_triggerWinFight
	* StepId: 39
	* Type: Trigger
	* TargetType: WaitForTime

## h_story_D05_NightmareGulf_exist_squad
	* StepId: 119
	* Type: Trigger
	* TargetType: UnitWithTagsExists
	* FailLL: h_story_D05_NightmareGulf_spawn_squad

## h_story_D05_NightmareGulf_exist_vashtiFleet
	* StepId: 128
	* Type: Trigger
	* TargetType: UnitWithTagsExists
	* FailLL: 
		* h_story_D05_NightmareGulf_deactivate_vashti2
		* h_story_D05_NightmareGulf_deactivate_vashtiFleet2
		* h_story_D05_NightmareGulf_spawn_vashtiFleet2

## h_story_D05_NightmareGulf_goal_destroyChains
	* StepId: 19
	* Type: Goal
	* TargetType: AllUnitsWithTagsAreKilled
	* SuccLL: 
		* h_story_D05_NightmareGulf_GAMA_19
		* h_story_D05_NightmareGulf_deactivate_vfxObserver

## h_story_D05_NightmareGulf_goal_destroyKidara
	* StepId: 26
	* Type: Goal
	* TargetType: AllUnitsWithTagsAreKilled
	* SuccLL: 
		* h_story_D05_NightmareGulf_GAMA_26
		* h_story_D05_NightmareGulf_GAMA_38
		* h_story_D05_NightmareGulf_GAMA_39
		* h_story_D05_NightmareGulf_deactivate_vashtiDown

## h_story_D05_NightmareGulf_goal_destroyStation
	* StepId: 17
	* Type: Goal
	* TargetType: KillSpecificWave
	* SuccLL: 
		* h_story_D05_NightmareGulf_GAMA_17
		* h_story_D05_NightmareGulf_preferredTaget_vashtiChains

## h_story_D05_NightmareGulf_healthCheck_armor1
	* StepId: 43
	* Type: Trigger
	* TargetType: TaggedUnitsBelowHealthAndArmor
	* SuccLL: h_story_D05_NightmareGulf_skill_missileBarrage1

## h_story_D05_NightmareGulf_healthCheck_armor2
	* StepId: 50
	* Type: Trigger
	* TargetType: TaggedUnitsBelowHealthAndArmor
	* SuccLL: h_story_D05_NightmareGulf_GAMA_50

## h_story_D05_NightmareGulf_healthCheck_armor3
	* StepId: 61
	* Type: Trigger
	* TargetType: TaggedUnitsBelowHealthAndArmor
	* SuccLL: 
		* h_story_D05_NightmareGulf_GAMA_61
		* h_story_D05_NightmareGulf_spawn_torpedo1

## h_story_D05_NightmareGulf_healthCheck_armor4
	* StepId: 69
	* Type: Trigger
	* TargetType: TaggedUnitsBelowHealthAndArmor
	* SuccLL: h_story_D05_NightmareGulf_spawn_squad1

## h_story_D05_NightmareGulf_healthCheck_armor5
	* StepId: 76
	* Type: Trigger
	* TargetType: TaggedUnitsBelowHealthAndArmor
	* SuccLL: h_story_D05_NightmareGulf_GAMA_76

## h_story_D05_NightmareGulf_healthCheck_armor6
	* StepId: 87
	* Type: Trigger
	* TargetType: TaggedUnitsBelowHealthAndArmor
	* SuccLL: 
		* h_story_D05_NightmareGulf_GAMA_87
		* h_story_D05_NightmareGulf_GAMA_88
		* h_story_D05_NightmareGulf_spawn_torpedo2a

## h_story_D05_NightmareGulf_healthCheck_armor7
	* StepId: 97
	* Type: Trigger
	* TargetType: TaggedUnitsBelowHealthAndArmor
	* SuccLL: h_story_D05_NightmareGulf_spawn_squad2

## h_story_D05_NightmareGulf_healthCheck_armor8
	* StepId: 104
	* Type: Trigger
	* TargetType: TaggedUnitsBelowHealthAndArmor
	* SuccLL: h_story_D05_NightmareGulf_GAMA_104

## h_story_D05_NightmareGulf_healthCheck_hull1
	* StepId: 44
	* Type: Trigger
	* TargetType: TaggedUnitsBelowHealthAndArmor
	* SuccLL: h_story_D05_NightmareGulf_GAMA_44

## h_story_D05_NightmareGulf_healthCheck_hull2
	* StepId: 55
	* Type: Trigger
	* TargetType: TaggedUnitsBelowHealthAndArmor
	* SuccLL: h_story_D05_NightmareGulf_GAMA_55

## h_story_D05_NightmareGulf_healthCheck_hull3
	* StepId: 63
	* Type: Trigger
	* TargetType: TaggedUnitsBelowHealthAndArmor
	* SuccLL: h_story_D05_NightmareGulf_GAMA_63

## h_story_D05_NightmareGulf_healthCheck_hull4
	* StepId: 70
	* Type: Trigger
	* TargetType: TaggedUnitsBelowHealthAndArmor
	* SuccLL: h_story_D05_NightmareGulf_GAMA_70

## h_story_D05_NightmareGulf_healthCheck_hull5
	* StepId: 81
	* Type: Trigger
	* TargetType: TaggedUnitsBelowHealthAndArmor
	* SuccLL: h_story_D05_NightmareGulf_GAMA_81

## h_story_D05_NightmareGulf_healthCheck_hull6
	* StepId: 91
	* Type: Trigger
	* TargetType: TaggedUnitsBelowHealthAndArmor
	* SuccLL: h_story_D05_NightmareGulf_GAMA_91

## h_story_D05_NightmareGulf_healthCheck_hull7
	* StepId: 98
	* Type: Trigger
	* TargetType: TaggedUnitsBelowHealthAndArmor
	* SuccLL: h_story_D05_NightmareGulf_GAMA_98

## h_story_D05_NightmareGulf_healthCheck_hull8
	* StepId: 112
	* Type: Trigger
	* TargetType: TaggedUnitsBelowHealthAndArmor
	* SuccLL: 
		* h_story_D05_NightmareGulf_GAMA_112
		* h_story_D05_NightmareGulf_GAMA_114
		* h_story_D05_NightmareGulf_GAMA_115
		* h_story_D05_NightmareGulf_d_destruct
		* h_story_D05_NightmareGulf_deactivate_goalDialogs
		* h_story_D05_NightmareGulf_deactivate_kidaraDestruct
		* h_story_D05_NightmareGulf_invincible_99

## h_story_D05_NightmareGulf_healthCheck_vashti
	* StepId: 13
	* Type: Trigger
	* TargetType: TaggedUnitsBelowStrength
	* SuccLL: 
		* h_story_D05_NightmareGulf_GAMA_13
		* h_story_D05_NightmareGulf_GAMA_14
		* h_story_D05_NightmareGulf_GAMA_15
		* h_story_D05_NightmareGulf_d_failVashti
		* h_story_D05_NightmareGulf_deactivate_goals
		* h_story_D05_NightmareGulf_incincible_kiithless

## h_story_D05_NightmareGulf_i_armor1
	* StepId: 42
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: h_story_D05_NightmareGulf_GAMA_42

## h_story_D05_NightmareGulf_i_armor2
	* StepId: 49
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: h_story_D05_NightmareGulf_GAMA_49

## h_story_D05_NightmareGulf_i_armor3
	* StepId: 60
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: h_story_D05_NightmareGulf_GAMA_60

## h_story_D05_NightmareGulf_i_armor4
	* StepId: 68
	* Type: None
	* TargetType: Immediate
	* SuccLL: h_story_D05_NightmareGulf_GAMA_68

## h_story_D05_NightmareGulf_i_armor5
	* StepId: 75
	* Type: None
	* TargetType: Immediate
	* SuccLL: h_story_D05_NightmareGulf_GAMA_75

## h_story_D05_NightmareGulf_i_armor6
	* StepId: 86
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: h_story_D05_NightmareGulf_GAMA_86

## h_story_D05_NightmareGulf_i_armor7
	* StepId: 96
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: h_story_D05_NightmareGulf_GAMA_96

## h_story_D05_NightmareGulf_i_armor8
	* StepId: 103
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: h_story_D05_NightmareGulf_GAMA_103

## h_story_D05_NightmareGulf_i_base
	* StepId: 4
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_story_D05_NightmareGulf_deactivate_kiithless
		* h_story_D05_NightmareGulf_spawn_base
		* h_story_D05_NightmareGulf_spawn_patrols
		* h_story_D05_NightmareGulf_spawn_platforms

## h_story_D05_NightmareGulf_i_emp1
	* StepId: 51
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_story_D05_NightmareGulf_GAMA_51
		* h_story_D05_NightmareGulf_GAMA_53
		* h_story_D05_NightmareGulf_deactivate_emp1Telegraph
		* h_story_D05_NightmareGulf_vfx_emp1Telegraph

## h_story_D05_NightmareGulf_i_emp2
	* StepId: 77
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_story_D05_NightmareGulf_GAMA_77
		* h_story_D05_NightmareGulf_deactivate_emp2Telegraph
		* h_story_D05_NightmareGulf_vfx_emp2Telegraph

## h_story_D05_NightmareGulf_i_emp3
	* StepId: 105
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_story_D05_NightmareGulf_GAMA_105
		* h_story_D05_NightmareGulf_deactivate_emp3Telegraph
		* h_story_D05_NightmareGulf_vfx_emp3Telegraph

## h_story_D05_NightmareGulf_i_gameplay
	* StepId: 21
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: h_story_D05_NightmareGulf_GAMA_21

## h_story_D05_NightmareGulf_i_goals
	* StepId: 12
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_story_D05_NightmareGulf_GAMA_12
		* h_story_D05_NightmareGulf_GAMA_16
		* h_story_D05_NightmareGulf_GAMA_18

## h_story_D05_NightmareGulf_i_kidara
	* StepId: 120
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_story_D05_NightmareGulf_addSkill_missileBarrage
		* h_story_D05_NightmareGulf_deactivate_all
		* h_story_D05_NightmareGulf_invincible_1
		* h_story_D05_NightmareGulf_spawn_kidara
		* h_story_D05_NightmareGulf_spawn_kidaraFleetA
		* h_story_D05_NightmareGulf_spawn_kidaraFleetB

## h_story_D05_NightmareGulf_i_observer
	* StepId: 5
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_story_D05_NightmareGulf_GAMA_5
		* h_story_D05_NightmareGulf_deactivate_chains
		* h_story_D05_NightmareGulf_deactivate_observer
		* h_story_D05_NightmareGulf_spawn_chains
		* h_story_D05_NightmareGulf_spawn_observer
		* h_story_D05_NightmareGulf_vfx_chains

## h_story_D05_NightmareGulf_i_postSequenceKidara
	* StepId: 117
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_story_D05_NightmareGulf_GAMA_117
		* h_story_D05_NightmareGulf_GAMA_118
		* h_story_D05_NightmareGulf_close_kidara
		* h_story_D05_NightmareGulf_deactivate_kidaraDialog
		* h_story_D05_NightmareGulf_deactivate_sequenceSquad
		* h_story_D05_NightmareGulf_los_kidaraOn

## h_story_D05_NightmareGulf_i_repair1
	* StepId: 45
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_story_D05_NightmareGulf_GAMA_45
		* h_story_D05_NightmareGulf_armor_1_1
		* h_story_D05_NightmareGulf_vfx_heal1
		* h_story_D05_NightmareGulf_vfx_repair1

## h_story_D05_NightmareGulf_i_repair2
	* StepId: 56
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_story_D05_NightmareGulf_GAMA_56
		* h_story_D05_NightmareGulf_armor_2_1
		* h_story_D05_NightmareGulf_vfx_heal2
		* h_story_D05_NightmareGulf_vfx_repair2

## h_story_D05_NightmareGulf_i_repair3
	* StepId: 64
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_story_D05_NightmareGulf_GAMA_64
		* h_story_D05_NightmareGulf_armor_3_1
		* h_story_D05_NightmareGulf_vfx_heal3
		* h_story_D05_NightmareGulf_vfx_repair3

## h_story_D05_NightmareGulf_i_repair4
	* StepId: 71
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_story_D05_NightmareGulf_GAMA_71
		* h_story_D05_NightmareGulf_armor_4_1
		* h_story_D05_NightmareGulf_vfx_heal4
		* h_story_D05_NightmareGulf_vfx_repair4

## h_story_D05_NightmareGulf_i_repair5
	* StepId: 82
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_story_D05_NightmareGulf_GAMA_82
		* h_story_D05_NightmareGulf_armor_5_1
		* h_story_D05_NightmareGulf_vfx_heal5
		* h_story_D05_NightmareGulf_vfx_repair5

## h_story_D05_NightmareGulf_i_repair6
	* StepId: 92
	* Type: None
	* TargetType: Immediate
	* SuccLL: 
		* h_story_D05_NightmareGulf_GAMA_92
		* h_story_D05_NightmareGulf_armor_6_1
		* h_story_D05_NightmareGulf_vfx_heal6
		* h_story_D05_NightmareGulf_vfx_repair6

## h_story_D05_NightmareGulf_i_repair7
	* StepId: 99
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_story_D05_NightmareGulf_GAMA_99
		* h_story_D05_NightmareGulf_armor_7_1
		* h_story_D05_NightmareGulf_vfx_heal7
		* h_story_D05_NightmareGulf_vfx_repair7

## h_story_D05_NightmareGulf_i_setup
	* StepId: 1
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_story_D05_NightmareGulf_GAMA_1
		* h_story_D05_NightmareGulf_GAMA_3
		* h_story_D05_NightmareGulf_GAMA_4

## h_story_D05_NightmareGulf_i_vashti
	* StepId: 2
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_story_D05_NightmareGulf_GAMA_2
		* h_story_D05_NightmareGulf_deactivate_vashti
		* h_story_D05_NightmareGulf_invincible_vashti
		* h_story_D05_NightmareGulf_spawn_vashti

## h_story_D05_NightmareGulf_multi_preObserverSequence
	* StepId: 28
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* h_story_D05_NightmareGulf_td_win
		* h_story_D05_NightmareGulf_w_amassariBuffer
	* SuccLL: h_story_D05_NightmareGulf_GAMA_28

## h_story_D05_NightmareGulf_multi_vashti
	* StepId: 14
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* h_story_D05_NightmareGulf_td_failVashti
		* h_story_D05_NightmareGulf_w_failVasthi
	* SuccLL: h_story_D05_NightmareGulf_fail_vasthi

## h_story_D05_NightmareGulf_sequenceEnd_intro
	* StepId: 11
	* Type: Trigger
	* TargetType: OnInGameSequenceFinishedForPlayer
	* TVS: 1
	* SuccLL: 
		* h_story_D05_NightmareGulf_GAMA_11
		* h_story_D05_NightmareGulf_GAMA_126
		* h_story_D05_NightmareGulf_GAMA_128
		* h_story_D05_NightmareGulf_GAMA_20
		* h_story_D05_NightmareGulf_activate_kiithless
		* h_story_D05_NightmareGulf_close_introSequenceDialog
		* h_story_D05_NightmareGulf_deactivate_introDialog
		* h_story_D05_NightmareGulf_lookAt_center
		* h_story_D05_NightmareGulf_los_introOn

## h_story_D05_NightmareGulf_sequenceEnd_kidara
	* StepId: 24
	* Type: Trigger
	* TargetType: OnInGameSequenceFinishedForPlayer
	* TVS: 1
	* SuccLL: 
		* h_story_D05_NightmareGulf_GAMA_116
		* h_story_D05_NightmareGulf_GAMA_24

## h_story_D05_NightmareGulf_sequenceEnd_observer
	* StepId: 30
	* Type: Trigger
	* TargetType: OnInGameSequenceFinishedForPlayer
	* TVS: 1
	* SuccLL: 
		* h_story_D05_NightmareGulf_GAMA_30
		* h_story_D05_NightmareGulf_close_observer
		* h_story_D05_NightmareGulf_deactivate_observerDialog
		* h_story_D05_NightmareGulf_lookAt_observer

## h_story_D05_NightmareGulf_start
	* StepId: 0
	* Type: Trigger
	* TargetType: MissionStart
	* SuccLL: 
		* h_story_D05_NightmareGulf_GAMA_0
		* h_story_D05_NightmareGulf_GAMA_10
		* h_story_D05_NightmareGulf_GAMA_6
		* h_story_D05_NightmareGulf_los_introOff
		* h_story_D05_NightmareGulf_sequence_intro

## h_story_D05_NightmareGulf_strength_all
	* StepId: 22
	* Type: Trigger
	* TargetType: TaggedUnitsBelowStrength
	* SuccLL: 
		* h_story_D05_NightmareGulf_GAMA_22
		* h_story_D05_NightmareGulf_ai_followFlagship

## h_story_D05_NightmareGulf_td_end
	* StepId: 32
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: s_nightmareGulf_dialog_end
	* SuccLL: h_story_D05_NightmareGulf_end

## h_story_D05_NightmareGulf_td_failVashti
	* StepId: 15
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: s_nightmareGulf_dialog_failKharKalaad

## h_story_D05_NightmareGulf_td_win
	* StepId: 36
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: s_nightmareGulf_dialog_win

## h_story_D05_NightmareGulf_w_amassari
	* StepId: 37
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D05_NightmareGulf_GAMA_37
		* h_story_D05_NightmareGulf_spawn_amassari

## h_story_D05_NightmareGulf_w_amassariBuffer
	* StepId: 38
	* Type: Trigger
	* TargetType: WaitForTime

## h_story_D05_NightmareGulf_w_clean
	* StepId: 40
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_D05_NightmareGulf_remove_progenitorHelp

## h_story_D05_NightmareGulf_w_closeDestructDialog
	* StepId: 115
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_D05_NightmareGulf_close_destruct

## h_story_D05_NightmareGulf_w_combat
	* StepId: 25
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_story_D05_NightmareGulf_GAMA_25
		* h_story_D05_NightmareGulf_GAMA_40
		* h_story_D05_NightmareGulf_activate_all
		* h_story_D05_NightmareGulf_deactivate_observer2

## h_story_D05_NightmareGulf_w_deactivateGoalDialogsRepeating
	* StepId: 116
	* Type: TriggerRepeating
	* TargetType: WaitForTime
	* SuccLL: h_story_D05_NightmareGulf_deactivate_goalDialogsRepeating

## h_story_D05_NightmareGulf_w_deactivateOpenGoals
	* StepId: 39
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_D05_NightmareGulf_deactivate_freeObserverHelp

## h_story_D05_NightmareGulf_w_dialogEmp
	* StepId: 54
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_D05_NightmareGulf_d_emp

## h_story_D05_NightmareGulf_w_dialogTorpedo
	* StepId: 62
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D05_NightmareGulf_d_torpedo
		* h_story_D05_NightmareGulf_mark_torpedo1

## h_story_D05_NightmareGulf_w_emp1
	* StepId: 52
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D05_NightmareGulf_GAMA_52
		* h_story_D05_NightmareGulf_activate_emp1Telegraph
		* h_story_D05_NightmareGulf_addStatMod_stun1
		* h_story_D05_NightmareGulf_addStatMod_stun1Ally
		* h_story_D05_NightmareGulf_invincible_2b
		* h_story_D05_NightmareGulf_vfx_emp1
		* h_story_D05_NightmareGulf_vfx_stun1
		* h_story_D05_NightmareGulf_vfx_stun1Ally

## h_story_D05_NightmareGulf_w_emp2
	* StepId: 78
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D05_NightmareGulf_GAMA_78
		* h_story_D05_NightmareGulf_GAMA_79
		* h_story_D05_NightmareGulf_activate_emp2Telegraph
		* h_story_D05_NightmareGulf_addStatMod_stun2
		* h_story_D05_NightmareGulf_addStatMod_stun2Ally
		* h_story_D05_NightmareGulf_invincible_5b
		* h_story_D05_NightmareGulf_vfx_emp2
		* h_story_D05_NightmareGulf_vfx_stun2
		* h_story_D05_NightmareGulf_vfx_stun2Ally

## h_story_D05_NightmareGulf_w_emp3
	* StepId: 106
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D05_NightmareGulf_GAMA_106
		* h_story_D05_NightmareGulf_GAMA_107
		* h_story_D05_NightmareGulf_activate_emp3Telegraph
		* h_story_D05_NightmareGulf_addStatMod_stun3
		* h_story_D05_NightmareGulf_addStatMod_stun3Ally
		* h_story_D05_NightmareGulf_invincible_8b
		* h_story_D05_NightmareGulf_vfx_emp3
		* h_story_D05_NightmareGulf_vfx_stun3
		* h_story_D05_NightmareGulf_vfx_stun3Ally

## h_story_D05_NightmareGulf_w_end
	* StepId: 31
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D05_NightmareGulf_GAMA_31
		* h_story_D05_NightmareGulf_d_end

## h_story_D05_NightmareGulf_w_engage
	* StepId: 127
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D05_NightmareGulf_GAMA_127
		* h_story_D05_NightmareGulf_d_engage

## h_story_D05_NightmareGulf_w_failVasthi
	* StepId: 16
	* Type: Trigger
	* TargetType: WaitForTime

## h_story_D05_NightmareGulf_w_freeObserver
	* StepId: 20
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D05_NightmareGulf_d_freeObserver
		* h_story_D05_NightmareGulf_preferredTaget_observerHelp
		* h_story_D05_NightmareGulf_spawn_observerHelp

## h_story_D05_NightmareGulf_w_gameplay
	* StepId: 41
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_story_D05_NightmareGulf_GAMA_111
		* h_story_D05_NightmareGulf_GAMA_41
		* h_story_D05_NightmareGulf_GAMA_43
		* h_story_D05_NightmareGulf_GAMA_54
		* h_story_D05_NightmareGulf_GAMA_62
		* h_story_D05_NightmareGulf_GAMA_69
		* h_story_D05_NightmareGulf_GAMA_80
		* h_story_D05_NightmareGulf_GAMA_90
		* h_story_D05_NightmareGulf_GAMA_97

## h_story_D05_NightmareGulf_w_introDialog1
	* StepId: 7
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D05_NightmareGulf_GAMA_7
		* h_story_D05_NightmareGulf_GAMA_9
		* h_story_D05_NightmareGulf_d_introA

## h_story_D05_NightmareGulf_w_introDialog2
	* StepId: 8
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D05_NightmareGulf_GAMA_8
		* h_story_D05_NightmareGulf_d_introB

## h_story_D05_NightmareGulf_w_introDialog3
	* StepId: 9
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_D05_NightmareGulf_d_introC

## h_story_D05_NightmareGulf_w_introMovement
	* StepId: 10
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_D05_NightmareGulf_activate_kiithlessIntro

## h_story_D05_NightmareGulf_w_kidaraSeq1
	* StepId: 122
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D05_NightmareGulf_GAMA_122
		* h_story_D05_NightmareGulf_d_kidaraSpawnA

## h_story_D05_NightmareGulf_w_kidaraSeq2
	* StepId: 123
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D05_NightmareGulf_GAMA_123
		* h_story_D05_NightmareGulf_d_kidaraSpawnB

## h_story_D05_NightmareGulf_w_kidaraSeq3
	* StepId: 124
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D05_NightmareGulf_GAMA_124
		* h_story_D05_NightmareGulf_GAMA_125
		* h_story_D05_NightmareGulf_d_kidaraSpawnC

## h_story_D05_NightmareGulf_w_kidaraSeq4
	* StepId: 125
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_D05_NightmareGulf_d_kidaraSpawnD

## h_story_D05_NightmareGulf_w_kidaraSequence
	* StepId: 121
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D05_NightmareGulf_close_kidaraSequence
		* h_story_D05_NightmareGulf_los_kidaraOff
		* h_story_D05_NightmareGulf_sequence_kidara

## h_story_D05_NightmareGulf_w_kidaraSpawn
	* StepId: 23
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D05_NightmareGulf_GAMA_119
		* h_story_D05_NightmareGulf_GAMA_120
		* h_story_D05_NightmareGulf_GAMA_121
		* h_story_D05_NightmareGulf_GAMA_23

## h_story_D05_NightmareGulf_w_kidaraSpawnEDialog
	* StepId: 118
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_D05_NightmareGulf_d_kidaraSpawnE

## h_story_D05_NightmareGulf_w_missileBarrage2
	* StepId: 80
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_D05_NightmareGulf_skill_missileBarrage2

## h_story_D05_NightmareGulf_w_observerSequence
	* StepId: 29
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D05_NightmareGulf_GAMA_29
		* h_story_D05_NightmareGulf_GAMA_32
		* h_story_D05_NightmareGulf_close_observerSequence
		* h_story_D05_NightmareGulf_los_observerOff
		* h_story_D05_NightmareGulf_move_playerFlagship
		* h_story_D05_NightmareGulf_sequence_observer
		* h_story_D05_NightmareGulf_teleport_flagship

## h_story_D05_NightmareGulf_w_observerSequence1
	* StepId: 33
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D05_NightmareGulf_GAMA_33
		* h_story_D05_NightmareGulf_d_observerA

## h_story_D05_NightmareGulf_w_observerSequence2
	* StepId: 34
	* Type: None
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D05_NightmareGulf_GAMA_34
		* h_story_D05_NightmareGulf_d_observerB

## h_story_D05_NightmareGulf_w_observerSequence3
	* StepId: 35
	* Type: None
	* TargetType: WaitForTime
	* SuccLL: h_story_D05_NightmareGulf_d_observerC

## h_story_D05_NightmareGulf_w_outro
	* StepId: 27
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D05_NightmareGulf_GAMA_27
		* h_story_D05_NightmareGulf_GAMA_35
		* h_story_D05_NightmareGulf_GAMA_36
		* h_story_D05_NightmareGulf_d_win

## h_story_D05_NightmareGulf_w_repair1_1
	* StepId: 46
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D05_NightmareGulf_GAMA_46
		* h_story_D05_NightmareGulf_armor_1_2

## h_story_D05_NightmareGulf_w_repair1_2
	* StepId: 47
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D05_NightmareGulf_GAMA_47
		* h_story_D05_NightmareGulf_armor_1_3

## h_story_D05_NightmareGulf_w_repair1_3
	* StepId: 48
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D05_NightmareGulf_GAMA_48
		* h_story_D05_NightmareGulf_armor_1_4
		* h_story_D05_NightmareGulf_invincible_2

## h_story_D05_NightmareGulf_w_repair2_1
	* StepId: 57
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D05_NightmareGulf_GAMA_57
		* h_story_D05_NightmareGulf_armor_2_2

## h_story_D05_NightmareGulf_w_repair2_2
	* StepId: 58
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D05_NightmareGulf_GAMA_58
		* h_story_D05_NightmareGulf_armor_2_3

## h_story_D05_NightmareGulf_w_repair2_3
	* StepId: 59
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D05_NightmareGulf_GAMA_59
		* h_story_D05_NightmareGulf_armor_2_4
		* h_story_D05_NightmareGulf_invincible_3

## h_story_D05_NightmareGulf_w_repair3_1
	* StepId: 65
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D05_NightmareGulf_GAMA_65
		* h_story_D05_NightmareGulf_armor_3_2

## h_story_D05_NightmareGulf_w_repair3_2
	* StepId: 66
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D05_NightmareGulf_GAMA_66
		* h_story_D05_NightmareGulf_armor_3_3

## h_story_D05_NightmareGulf_w_repair3_3
	* StepId: 67
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D05_NightmareGulf_GAMA_67
		* h_story_D05_NightmareGulf_armor_3_4
		* h_story_D05_NightmareGulf_invincible_4

## h_story_D05_NightmareGulf_w_repair4_1
	* StepId: 72
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D05_NightmareGulf_GAMA_72
		* h_story_D05_NightmareGulf_armor_4_2

## h_story_D05_NightmareGulf_w_repair4_2
	* StepId: 73
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D05_NightmareGulf_GAMA_73
		* h_story_D05_NightmareGulf_armor_4_3

## h_story_D05_NightmareGulf_w_repair4_3
	* StepId: 74
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D05_NightmareGulf_GAMA_74
		* h_story_D05_NightmareGulf_armor_4_4
		* h_story_D05_NightmareGulf_invincible_5

## h_story_D05_NightmareGulf_w_repair5_1
	* StepId: 83
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D05_NightmareGulf_GAMA_83
		* h_story_D05_NightmareGulf_armor_5_2

## h_story_D05_NightmareGulf_w_repair5_2
	* StepId: 84
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D05_NightmareGulf_GAMA_84
		* h_story_D05_NightmareGulf_armor_5_3

## h_story_D05_NightmareGulf_w_repair5_3
	* StepId: 85
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D05_NightmareGulf_GAMA_85
		* h_story_D05_NightmareGulf_armor_5_4
		* h_story_D05_NightmareGulf_invincible_6

## h_story_D05_NightmareGulf_w_repair6_1
	* StepId: 93
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D05_NightmareGulf_GAMA_93
		* h_story_D05_NightmareGulf_armor_6_2

## h_story_D05_NightmareGulf_w_repair6_2
	* StepId: 94
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D05_NightmareGulf_GAMA_94
		* h_story_D05_NightmareGulf_armor_6_3

## h_story_D05_NightmareGulf_w_repair6_3
	* StepId: 95
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D05_NightmareGulf_GAMA_95
		* h_story_D05_NightmareGulf_armor_6_4
		* h_story_D05_NightmareGulf_invincible_7

## h_story_D05_NightmareGulf_w_repair7_1
	* StepId: 100
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D05_NightmareGulf_GAMA_100
		* h_story_D05_NightmareGulf_armor_7_2

## h_story_D05_NightmareGulf_w_repair7_2
	* StepId: 101
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D05_NightmareGulf_GAMA_101
		* h_story_D05_NightmareGulf_armor_7_3

## h_story_D05_NightmareGulf_w_repair7_3
	* StepId: 102
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D05_NightmareGulf_GAMA_102
		* h_story_D05_NightmareGulf_armor_7_4
		* h_story_D05_NightmareGulf_invincible_8

## h_story_D05_NightmareGulf_w_spawnSquadSequence
	* StepId: 126
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_D05_NightmareGulf_spawn_squadSequence

## h_story_D05_NightmareGulf_w_startTelegraphDestruct
	* StepId: 113
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D05_NightmareGulf_GAMA_113
		* h_story_D05_NightmareGulf_vfx_telegraphDestruct

## h_story_D05_NightmareGulf_w_stationDialog
	* StepId: 18
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_D05_NightmareGulf_d_station

## h_story_D05_NightmareGulf_w_stun1
	* StepId: 53
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D05_NightmareGulf_removeStatMod_stun1
		* h_story_D05_NightmareGulf_removeStatMod_stun1Ally

## h_story_D05_NightmareGulf_w_stun2
	* StepId: 79
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D05_NightmareGulf_removeStatMod_stun2
		* h_story_D05_NightmareGulf_removeStatMod_stun2Ally

## h_story_D05_NightmareGulf_w_stun3
	* StepId: 107
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D05_NightmareGulf_removeStatMod_stun3
		* h_story_D05_NightmareGulf_removeStatMod_stun3Ally

## h_story_D05_NightmareGulf_w_telegraphDestruct
	* StepId: 114
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D05_NightmareGulf_destruct_kidara
		* h_story_D05_NightmareGulf_dmg_destruct
		* h_story_D05_NightmareGulf_dmg_destructAlly
		* h_story_D05_NightmareGulf_kill_kiithlessA
		* h_story_D05_NightmareGulf_kill_kiithlessB

## h_story_D05_NightmareGulf_w_torpedo2aMark
	* StepId: 88
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_D05_NightmareGulf_mark_torpedo2a

## h_story_D05_NightmareGulf_w_torpedo2b
	* StepId: 89
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D05_NightmareGulf_GAMA_89
		* h_story_D05_NightmareGulf_spawn_torpedo2b

## h_story_D05_NightmareGulf_w_torpedo2bMark
	* StepId: 90
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_D05_NightmareGulf_mark_torpedo2b

## h_story_D05_NightmareGulf_w_torpedo3a
	* StepId: 108
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D05_NightmareGulf_GAMA_108
		* h_story_D05_NightmareGulf_GAMA_109
		* h_story_D05_NightmareGulf_spawn_torpedo3a

## h_story_D05_NightmareGulf_w_torpedo3aMark
	* StepId: 109
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_D05_NightmareGulf_mark_torpedo3a

## h_story_D05_NightmareGulf_w_torpedo3b
	* StepId: 110
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D05_NightmareGulf_GAMA_110
		* h_story_D05_NightmareGulf_spawn_torpedo3b

## h_story_D05_NightmareGulf_w_torpedo3bMark
	* StepId: 111
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_D05_NightmareGulf_mark_torpedo3b

## h_story_D05_NightmareGulf_w_vashti1
	* StepId: 129
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D05_NightmareGulf_GAMA_129
		* h_story_D05_NightmareGulf_activate_Vashti
		* h_story_D05_NightmareGulf_preferredTarget_vashtiStation

## h_story_D05_NightmareGulf_w_vashti2
	* StepId: 130
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_story_D05_NightmareGulf_activate_VashtiFleet

## h_story_D05_NightmareGulf_w_vashtiFleet
	* StepId: 3
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_story_D05_NightmareGulf_deactivate_vashtiFleet
		* h_story_D05_NightmareGulf_spawn_vasthiFleet

## h_story_D05_NightmareGulf_w_vfxObserver
	* StepId: 6
	* Type: TriggerRepeating
	* TargetType: WaitForTime
	* SuccLL: h_story_D05_NightmareGulf_vfx_observer

## h_strike_01_PirateHideout_a0cb8394427daa0409f158020f456534
	* StepId: 18
	* Type: Trigger
	* TargetType: OnInGameSequenceFinishedForPlayer
	* TVS: 1
	* SuccLL: h_strike_01_PirateHideout_miss010_act_lineofsight_on

## h_strike_01_PirateHideout_check_goal_condition
	* StepId: 1
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: h_strike_01_PirateHideout_miss010_g_boss
	* SuccLL: 
		* h_strike_01_PirateHideout_miss010_act_dia_fin
		* h_strike_01_PirateHideout_miss010_act_fin
		* h_strike_01_PirateHideout_remove_units

## h_strike_01_PirateHideout_disable_repeating_spawn_farm_timer
	* StepId: 20
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_strike_01_PirateHideout_disable_spawns

## h_strike_01_PirateHideout_miss010_g_boss
	* StepId: 4
	* Type: Goal
	* TargetType: KillSpecificWave

## h_strike_01_PirateHideout_miss010_gBase0
	* StepId: 8
	* Type: Goal
	* TargetType: KillSpecificWave

## h_strike_01_PirateHideout_miss010_gGuard0
	* StepId: 9
	* Type: Goal
	* TargetType: AllUnitsWithTagsAreKilled

## h_strike_01_PirateHideout_miss010_trig1
	* StepId: 0
	* Type: Trigger
	* TargetType: MissionStart
	* SuccLL: 
		* h_strike_01_PirateHideout_GAMA_0
		* h_strike_01_PirateHideout_GAMA_1
		* h_strike_01_PirateHideout_GAMA_11
		* h_strike_01_PirateHideout_GAMA_13
		* h_strike_01_PirateHideout_GAMA_15
		* h_strike_01_PirateHideout_GAMA_16
		* h_strike_01_PirateHideout_GAMA_6
		* h_strike_01_PirateHideout_GAMA_9
		* h_strike_01_PirateHideout_TirggerWave_patrol0
		* h_strike_01_PirateHideout_TirggerWave_patrol1
		* h_strike_01_PirateHideout_TirggerWave_patrol2
		* h_strike_01_PirateHideout_miss010_ShowIntroSeq
		* h_strike_01_PirateHideout_miss010_act_dia_brief
		* h_strike_01_PirateHideout_miss010_act_lineofsight_off
		* h_strike_01_PirateHideout_miss010_act_showsensor0

## h_strike_01_PirateHideout_miss010_trigBoss
	* StepId: 2
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* h_strike_01_PirateHideout_miss010_gBase0
		* h_strike_01_PirateHideout_miss010_gGuard0
	* SuccLL: 
		* h_strike_01_PirateHideout_GAMA_2
		* h_strike_01_PirateHideout_GAMA_4
		* h_strike_01_PirateHideout_GAMA_5
		* h_strike_01_PirateHideout_MakeNPCFollowFlagship1
		* h_strike_01_PirateHideout_miss010_act_stopPatrolWave

## h_strike_01_PirateHideout_miss010_trigSensorDialog0
	* StepId: 17
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_strike_01_PirateHideout_miss010_act_dia_sensor

## h_strike_01_PirateHideout_miss010_trigSensorOn0
	* StepId: 16
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_strike_01_PirateHideout_miss010_act_showSensor0

## h_strike_01_PirateHideout_miss010_waitfor_cameralookat0
	* StepId: 19
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_strike_01_PirateHideout_miss010_act_cameralookat0

## h_strike_01_PirateHideout_setupSpawns
	* StepId: 7
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_strike_01_PirateHideout_GAMA_7
		* h_strike_01_PirateHideout_GAMA_8
		* h_strike_01_PirateHideout_miss010_act_Base0
		* h_strike_01_PirateHideout_miss010_act_Guard0
		* h_strike_01_PirateHideout_spoawnFirstWaveOfPatrols

## h_strike_01_PirateHideout_TriggerWaitForTime010
	* StepId: 5
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_strike_01_PirateHideout_miss010_act_dia_boss

## h_strike_01_PirateHideout_TriggerWaitForTime011
	* StepId: 6
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_strike_01_PirateHideout_miss010_act_sensorview_boss

## h_strike_01_PirateHideout_TriggerWaitForTime012
	* StepId: 3
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_strike_01_PirateHideout_GAMA_3
		* h_strike_01_PirateHideout_miss010_act_boss

## h_strike_01_PirateHideout_trigRepeating_respawn_patrol1
	* StepId: 10
	* Type: TriggerRepeating
	* TargetType: KillSpecificWave
	* SuccLL: h_strike_01_PirateHideout_GAMA_10

## h_strike_01_PirateHideout_trigRepeating_respawn_patrol2
	* StepId: 12
	* Type: TriggerRepeating
	* TargetType: KillSpecificWave
	* SuccLL: h_strike_01_PirateHideout_GAMA_12

## h_strike_01_PirateHideout_trigRepeating_respawn_patrol3
	* StepId: 14
	* Type: TriggerRepeating
	* TargetType: KillSpecificWave
	* SuccLL: h_strike_01_PirateHideout_GAMA_14

## h_strike_01_PirateHideout_w_respawnWaitTimer1
	* StepId: 11
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_strike_01_PirateHideout_respawn_patrol1

## h_strike_01_PirateHideout_w_respawnWaitTimer2
	* StepId: 13
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_strike_01_PirateHideout_respawn_patrol2

## h_strike_01_PirateHideout_w_respawnWaitTimer3
	* StepId: 15
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_strike_01_PirateHideout_respawn_patrol3

## h_strike_02_StationDefense_68053284737ce404dbf17c8fa3ebab27
	* StepId: 27
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: h_strike_02_StationDefense_rd_stationdef_gKillBoss
	* SuccLL: 
		* h_strike_02_StationDefense_6c93bb41b16c264499c92218a7b7db0a
		* h_strike_02_StationDefense_rd_stationdef_act_dia_fin
		* h_strike_02_StationDefense_rd_stationdef_act_fin

## h_strike_02_StationDefense_check_if_seq_end
	* StepId: 26
	* Type: Trigger
	* TargetType: OnInGameSequenceFinishedForPlayer
	* TVS: 1
	* SuccLL: h_strike_02_StationDefense_enable_los

## h_strike_02_StationDefense_disable_repeating_spawns_timer
	* StepId: 28
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_strike_02_StationDefense_disable_repeating_spawns

## h_strike_02_StationDefense_rd_stationdef_gBeaconNE
	* StepId: 14
	* Type: Trigger
	* TargetType: KillSpecificWave
	* SuccLL: h_strike_02_StationDefense_rd_stationdef_act_removeSpawnNE

## h_strike_02_StationDefense_rd_stationdef_gBeaconNW
	* StepId: 13
	* Type: Trigger
	* TargetType: KillSpecificWave
	* SuccLL: h_strike_02_StationDefense_rd_stationdef_act_removeSpawnNW

## h_strike_02_StationDefense_rd_stationdef_gBeaconSE
	* StepId: 16
	* Type: Trigger
	* TargetType: KillSpecificWave
	* SuccLL: h_strike_02_StationDefense_rd_stationdef_act_removeSpawnSE

## h_strike_02_StationDefense_rd_stationdef_gBeaconSW
	* StepId: 15
	* Type: Trigger
	* TargetType: KillSpecificWave
	* SuccLL: h_strike_02_StationDefense_rd_stationdef_act_removeSpawnSW

## h_strike_02_StationDefense_rd_stationdef_gKillBoss
	* StepId: 19
	* Type: Goal
	* TargetType: KillSpecificWave

## h_strike_02_StationDefense_rd_stationdef_gStationDefenseFail
	* StepId: 23
	* Type: Trigger
	* TargetType: OnTaggedUnitKilled
	* SuccLL: 
		* h_strike_02_StationDefense_rd_stationdef_act_dia_fail
		* h_strike_02_StationDefense_rd_stationdef_act_fail

## h_strike_02_StationDefense_rd_stationdef_tBeacons_all
	* StepId: 17
	* Type: Goal
	* TargetType: FinishGoalsString
	* TVS: 
		* h_strike_02_StationDefense_rd_stationdef_gBeaconNE
		* h_strike_02_StationDefense_rd_stationdef_gBeaconNW
		* h_strike_02_StationDefense_rd_stationdef_gBeaconSE
		* h_strike_02_StationDefense_rd_stationdef_gBeaconSW
	* SuccLL: h_strike_02_StationDefense_GAMA_7

## h_strike_02_StationDefense_rd_stationdef_trig_SpawnWaitTimer1
	* StepId: 10
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_strike_02_StationDefense_rd_stationdef_act_spawnFleet_new_NE

## h_strike_02_StationDefense_rd_stationdef_trig_SpawnWaitTimer2
	* StepId: 11
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_strike_02_StationDefense_rd_stationdef_act_spawnFleet_new_SW

## h_strike_02_StationDefense_rd_stationdef_trig_SpawnWaitTimer3
	* StepId: 12
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_strike_02_StationDefense_rd_stationdef_act_spawnFleet_new_SE

## h_strike_02_StationDefense_rd_stationdef_trigBeaconDone1
	* StepId: 20
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* h_strike_02_StationDefense_rd_stationdef_gBeaconNE
		* h_strike_02_StationDefense_rd_stationdef_gBeaconNW
		* h_strike_02_StationDefense_rd_stationdef_gBeaconSE
		* h_strike_02_StationDefense_rd_stationdef_gBeaconSW
	* SuccLL: h_strike_02_StationDefense_rd_stationdef_act_dia_beaconsdone1

## h_strike_02_StationDefense_rd_stationdef_trigBeaconDone2
	* StepId: 21
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* h_strike_02_StationDefense_rd_stationdef_gBeaconNE
		* h_strike_02_StationDefense_rd_stationdef_gBeaconNW
		* h_strike_02_StationDefense_rd_stationdef_gBeaconSE
		* h_strike_02_StationDefense_rd_stationdef_gBeaconSW
	* SuccLL: h_strike_02_StationDefense_rd_stationdef_act_dia_beaconsdone2

## h_strike_02_StationDefense_rd_stationdef_trigBeaconDone3
	* StepId: 22
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* h_strike_02_StationDefense_rd_stationdef_gBeaconNE
		* h_strike_02_StationDefense_rd_stationdef_gBeaconNW
		* h_strike_02_StationDefense_rd_stationdef_gBeaconSE
		* h_strike_02_StationDefense_rd_stationdef_gBeaconSW
	* SuccLL: h_strike_02_StationDefense_rd_stationdef_act_dia_beaconsdone3

## h_strike_02_StationDefense_rd_stationdef_trigRespawn_Timer01
	* StepId: 3
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_strike_02_StationDefense_rd_stationdef_act_RespawnFleet_new_NW

## h_strike_02_StationDefense_rd_stationdef_trigRespawn_Timer02
	* StepId: 5
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_strike_02_StationDefense_rd_stationdef_act_RespawnFleet_new_NE

## h_strike_02_StationDefense_rd_stationdef_trigRespawn_Timer03
	* StepId: 7
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_strike_02_StationDefense_rd_stationdef_act_RespawnFleet_new_SW

## h_strike_02_StationDefense_rd_stationdef_trigRespawn_Timer04
	* StepId: 9
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_strike_02_StationDefense_rd_stationdef_act_RespawnFleet_new_SE

## h_strike_02_StationDefense_rd_stationdef_trigRespawnNE
	* StepId: 4
	* Type: TriggerRepeating
	* TargetType: KillSpecificWave
	* SuccLL: h_strike_02_StationDefense_GAMA_1

## h_strike_02_StationDefense_rd_stationdef_trigRespawnNW
	* StepId: 2
	* Type: TriggerRepeating
	* TargetType: KillSpecificWave
	* SuccLL: h_strike_02_StationDefense_GAMA_0

## h_strike_02_StationDefense_rd_stationdef_trigRespawnSE
	* StepId: 8
	* Type: TriggerRepeating
	* TargetType: KillSpecificWave
	* SuccLL: h_strike_02_StationDefense_GAMA_3

## h_strike_02_StationDefense_rd_stationdef_trigRespawnSW
	* StepId: 6
	* Type: TriggerRepeating
	* TargetType: KillSpecificWave
	* SuccLL: h_strike_02_StationDefense_GAMA_2

## h_strike_02_StationDefense_rd_stationdef_trigSensorviewOn
	* StepId: 24
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_strike_02_StationDefense_rd_stationdef_act_sensorviewOn

## h_strike_02_StationDefense_rd_stationdef_trigStart
	* StepId: 0
	* Type: Trigger
	* TargetType: MissionStart
	* SuccLL: 
		* h_strike_02_StationDefense_GAMA_10
		* h_strike_02_StationDefense_GAMA_11
		* h_strike_02_StationDefense_GAMA_9
		* h_strike_02_StationDefense_disable_los
		* h_strike_02_StationDefense_rd_stationdef_ShowIntroSeq
		* h_strike_02_StationDefense_rd_stationdef_act_addcameralookat0
		* h_strike_02_StationDefense_rd_stationdef_act_dia_start
		* h_strike_02_StationDefense_rd_stationdef_act_spawnAllyBeacons
		* h_strike_02_StationDefense_rd_stationdef_act_spawnGuards
		* h_strike_02_StationDefense_rd_stationdef_act_spawnStation
		* h_strike_02_StationDefense_rd_stationdef_act_trigWaitSpawn

## h_strike_02_StationDefense_rd_stationdef_trigWaitSpawn
	* StepId: 1
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_strike_02_StationDefense_GAMA_4
		* h_strike_02_StationDefense_GAMA_5
		* h_strike_02_StationDefense_GAMA_6
		* h_strike_02_StationDefense_rd_stationdef_act_despawnAllyBeaconNW
		* h_strike_02_StationDefense_rd_stationdef_act_dia_beacons
		* h_strike_02_StationDefense_rd_stationdef_act_gBeacons
		* h_strike_02_StationDefense_rd_stationdef_act_mark_BeaconNE
		* h_strike_02_StationDefense_rd_stationdef_act_mark_BeaconNW
		* h_strike_02_StationDefense_rd_stationdef_act_mark_BeaconSE
		* h_strike_02_StationDefense_rd_stationdef_act_mark_BeaconSW
		* h_strike_02_StationDefense_rd_stationdef_act_spawnBeaconNE
		* h_strike_02_StationDefense_rd_stationdef_act_spawnBeaconNW
		* h_strike_02_StationDefense_rd_stationdef_act_spawnBeaconSE
		* h_strike_02_StationDefense_rd_stationdef_act_spawnBeaconSW
		* h_strike_02_StationDefense_rd_stationdef_act_spawnFleet_new_NW
		* h_strike_02_StationDefense_rd_stationdef_act_trigSpawns

## h_strike_02_StationDefense_rd_stationdef_waitforcameralookat0
	* StepId: 25
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_strike_02_StationDefense_rd_stationdef_act_cameralookat0

## h_strike_02_StationDefense_rd_stationdef_waitTimerAfterBeacons
	* StepId: 18
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_strike_02_StationDefense_GAMA_8
		* h_strike_02_StationDefense_rd_stationdef_act_dia_boss
		* h_strike_02_StationDefense_rd_stationdef_act_sensorview_Boss
		* h_strike_02_StationDefense_rd_stationdef_act_spawnBoss

## h_strike_03_PahrasRock_918a10d5f9d40bc4bb833b159bce009c
	* StepId: 2
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* h_strike_03_PahrasRock_kill_final_fleet
		* h_strike_03_PahrasRock_r003_goal_kill_Base
	* SuccLL: h_strike_03_PahrasRock_r003_action_finish_dialog0

## h_strike_03_PahrasRock_delay_spawn_1_1
	* StepId: 17
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_strike_03_PahrasRock_respawnPatrol1_1

## h_strike_03_PahrasRock_delay_spawn_1_2
	* StepId: 19
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_strike_03_PahrasRock_respawnPatrol1_2

## h_strike_03_PahrasRock_delay_spawn_1_3
	* StepId: 21
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_strike_03_PahrasRock_respawnPatrol1_3

## h_strike_03_PahrasRock_delay_spawn_1_4
	* StepId: 23
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_strike_03_PahrasRock_respawnPatrol1_4

## h_strike_03_PahrasRock_delay_spawn_B_1
	* StepId: 25
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_strike_03_PahrasRock_r003_spawn_patrolB_1

## h_strike_03_PahrasRock_delay_spawn_B_2
	* StepId: 27
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_strike_03_PahrasRock_r003_spawn_patrolB_2

## h_strike_03_PahrasRock_disable_repeating_spawns_timer
	* StepId: 28
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_strike_03_PahrasRock_disable_repeating_spawns

## h_strike_03_PahrasRock_i_baseHealthTrigger
	* StepId: 8
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_strike_03_PahrasRock_GAMA_10
		* h_strike_03_PahrasRock_GAMA_11
		* h_strike_03_PahrasRock_GAMA_12
		* h_strike_03_PahrasRock_GAMA_8
		* h_strike_03_PahrasRock_GAMA_9

## h_strike_03_PahrasRock_kill_final_fleet
	* StepId: 4
	* Type: Goal
	* TargetType: KillSpecificWave

## h_strike_03_PahrasRock_patrol1_1_destroyed
	* StepId: 16
	* Type: TriggerRepeating
	* TargetType: KillSpecificWave
	* SuccLL: h_strike_03_PahrasRock_GAMA_16

## h_strike_03_PahrasRock_patrol1_2_destroyed
	* StepId: 18
	* Type: TriggerRepeating
	* TargetType: KillSpecificWave
	* SuccLL: h_strike_03_PahrasRock_GAMA_18

## h_strike_03_PahrasRock_patrol1_3_destroyed
	* StepId: 20
	* Type: TriggerRepeating
	* TargetType: KillSpecificWave
	* SuccLL: h_strike_03_PahrasRock_GAMA_20

## h_strike_03_PahrasRock_patrol1_4_destroyed
	* StepId: 22
	* Type: TriggerRepeating
	* TargetType: KillSpecificWave
	* SuccLL: h_strike_03_PahrasRock_GAMA_22

## h_strike_03_PahrasRock_patrolB_1_destroyed
	* StepId: 24
	* Type: TriggerRepeating
	* TargetType: KillSpecificWave
	* SuccLL: h_strike_03_PahrasRock_GAMA_24

## h_strike_03_PahrasRock_patrolB_2_destroyed
	* StepId: 26
	* Type: TriggerRepeating
	* TargetType: KillSpecificWave
	* SuccLL: h_strike_03_PahrasRock_GAMA_26

## h_strike_03_PahrasRock_r003_BaseHP_40
	* StepId: 12
	* Type: Trigger
	* TargetType: OnTaggedUnitIsBelowHealth

## h_strike_03_PahrasRock_r003_BaseHP_60
	* StepId: 10
	* Type: Trigger
	* TargetType: OnTaggedUnitIsBelowHealth
	* SuccLL: 
		* h_strike_03_PahrasRock_r003_action_dialog_BaseHp60
		* h_strike_03_PahrasRock_r003_action_spawn_fleet2_1
		* h_strike_03_PahrasRock_r003_action_spawn_fleet2_2
		* h_strike_03_PahrasRock_r003_action_spawn_fleet2_3

## h_strike_03_PahrasRock_r003_BaseHP_80
	* StepId: 9
	* Type: Trigger
	* TargetType: OnTaggedUnitIsBelowHealth
	* SuccLL: 
		* h_strike_03_PahrasRock_MakeNPC1FollowFlagship
		* h_strike_03_PahrasRock_r003_action_dialog_BaseHp80
		* h_strike_03_PahrasRock_r003_action_spawn_fleet1_1
		* h_strike_03_PahrasRock_r003_action_spawn_fleet1_2

## h_strike_03_PahrasRock_r003_goal_kill_Base
	* StepId: 3
	* Type: Goal
	* TargetType: KillSpecificWave
	* SuccLL: h_strike_03_PahrasRock_r003_action_deactivate_patrols

## h_strike_03_PahrasRock_r003_missionstart
	* StepId: 0
	* Type: Trigger
	* TargetType: MissionStart
	* SuccLL: 
		* h_strike_03_PahrasRock_GAMA_0
		* h_strike_03_PahrasRock_GAMA_1
		* h_strike_03_PahrasRock_GAMA_13
		* h_strike_03_PahrasRock_GAMA_14
		* h_strike_03_PahrasRock_GAMA_15
		* h_strike_03_PahrasRock_GAMA_17
		* h_strike_03_PahrasRock_GAMA_19
		* h_strike_03_PahrasRock_GAMA_2
		* h_strike_03_PahrasRock_GAMA_21
		* h_strike_03_PahrasRock_GAMA_23
		* h_strike_03_PahrasRock_GAMA_25
		* h_strike_03_PahrasRock_GAMA_27
		* h_strike_03_PahrasRock_GAMA_3
		* h_strike_03_PahrasRock_GAMA_4
		* h_strike_03_PahrasRock_GAMA_7
		* h_strike_03_PahrasRock_r003_act_seq_intro
		* h_strike_03_PahrasRock_r003_action_startdialog

## h_strike_03_PahrasRock_r003_timer_cameralookat
	* StepId: 6
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_strike_03_PahrasRock_r003_action_cameralookat

## h_strike_03_PahrasRock_r003_timer_sensor
	* StepId: 7
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_strike_03_PahrasRock_r003_action_sensor_on

## h_strike_03_PahrasRock_SpawnEnemyPatrol
	* StepId: 15
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_strike_03_PahrasRock_TriggerEnemyPatrol1_1
		* h_strike_03_PahrasRock_TriggerEnemyPatrol1_2
		* h_strike_03_PahrasRock_TriggerEnemyPatrol1_3
		* h_strike_03_PahrasRock_TriggerEnemyPatrol1_4

## h_strike_03_PahrasRock_t_baseDestroyed
	* StepId: 13
	* Type: Trigger
	* TargetType: OnTaggedUnitKilled

## h_strike_03_PahrasRock_t_checkIfBaseDeador25HP
	* StepId: 11
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* h_strike_03_PahrasRock_r003_BaseHP_40
		* h_strike_03_PahrasRock_t_baseDestroyed
	* SuccLL: 
		* h_strike_03_PahrasRock_act_MakeBaseVincibleAgain
		* h_strike_03_PahrasRock_r003_BaseHp40_dialog0
		* h_strike_03_PahrasRock_r003_action_BaseHP40_sensor
		* h_strike_03_PahrasRock_r003_action_spawn_fleet3

## h_strike_03_PahrasRock_TriggerEnemyWaveSetup
	* StepId: 14
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_strike_03_PahrasRock_actn_makeBaseInvincibleAt20
		* h_strike_03_PahrasRock_r003_action_spawn_Base0
		* h_strike_03_PahrasRock_r003_action_spawn_guard0
		* h_strike_03_PahrasRock_r003_action_spawn_guard1
		* h_strike_03_PahrasRock_r003_action_spawn_guard2
		* h_strike_03_PahrasRock_r003_action_spawn_guard3
		* h_strike_03_PahrasRock_r003_action_spawn_guard4
		* h_strike_03_PahrasRock_r003_action_spawn_guard5
		* h_strike_03_PahrasRock_r003_action_spawn_guard6
		* h_strike_03_PahrasRock_r003_action_spawn_guard7
		* h_strike_03_PahrasRock_r003_action_spawn_patrolB1
		* h_strike_03_PahrasRock_r003_action_spawn_patrolB2

## h_strike_03_PahrasRock_TriggerFinishMission
	* StepId: 1
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: h_strike_03_PahrasRock_918a10d5f9d40bc4bb833b159bce009c
	* SuccLL: 
		* h_strike_03_PahrasRock_disable_platforms
		* h_strike_03_PahrasRock_r003_action_finish_mission
		* h_strike_03_PahrasRock_remove_ships

## h_strike_03_PahrasRock_TriggerOnSequenceEnd
	* StepId: 5
	* Type: Trigger
	* TargetType: OnInGameSequenceFinishedForPlayer
	* TVS: 1
	* SuccLL: 
		* h_strike_03_PahrasRock_GAMA_5
		* h_strike_03_PahrasRock_GAMA_6

## h_strike_04_Breach_c_armBomb
	* StepId: 18
	* Type: Goal
	* TargetType: WaitForTime
	* SuccLL: 
		* h_strike_04_Breach_GAMA_18
		* h_strike_04_Breach_a_deactivateBlockadeBossWave02
		* h_strike_04_Breach_a_disableLooesCondition
		* h_strike_04_Breach_a_st_breach_explosion_1_dialog

## h_strike_04_Breach_g_killTurrets1
	* StepId: 29
	* Type: Trigger
	* TargetType: AllUnitsWithTagsAreKilled
	* SuccLL: h_strike_04_Breach_a_reactivateTurret2

## h_strike_04_Breach_g_killTurrets1and2and3
	* StepId: 26
	* Type: Goal
	* TargetType: FinishGoalsString
	* TVS: 
		* h_strike_04_Breach_g_killTurrets1
		* h_strike_04_Breach_g_killTurrets2
		* h_strike_04_Breach_g_killTurrets3
	* SuccLL: 
		* h_strike_04_Breach_a_reactivateEscort3
		* h_strike_04_Breach_dialogTurret3Dead

## h_strike_04_Breach_g_killTurrets2
	* StepId: 30
	* Type: Trigger
	* TargetType: AllUnitsWithTagsAreKilled
	* SuccLL: 
		* h_strike_04_Breach_a_disableSecondFreighterStop
		* h_strike_04_Breach_a_reactivateTurret3
		* h_strike_04_Breach_a_spawnBaseProtection1
		* h_strike_04_Breach_a_spawnBlockadeWave_03_01

## h_strike_04_Breach_g_killTurrets3
	* StepId: 31
	* Type: Trigger
	* TargetType: AllUnitsWithTagsAreKilled
	* SuccLL: 
		* h_strike_04_Breach_a_disableThirdFreighterStop
		* h_strike_04_Breach_a_spawnBaseProtection2
		* h_strike_04_Breach_a_spawnPatrol4

## h_strike_04_Breach_g_protectFreighter
	* StepId: 17
	* Type: Goal
	* TargetType: ReachPointOfInterest
	* SuccLL: 
		* h_strike_04_Breach_GAMA_17
		* h_strike_04_Breach_GAMA_21
		* h_strike_04_Breach_a_armExplosives_1_dialog
		* h_strike_04_Breach_a_spawnBlockadeBossWave02
		* h_strike_04_Breach_a_spawnBoss

## h_strike_04_Breach_i_misc
	* StepId: 14
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_strike_04_Breach_GAMA_14
		* h_strike_04_Breach_a_startIntro

## h_strike_04_Breach_i_missionStart
	* StepId: 1
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_strike_04_Breach_GAMA_1
		* h_strike_04_Breach_GAMA_12
		* h_strike_04_Breach_GAMA_13
		* h_strike_04_Breach_GAMA_16
		* h_strike_04_Breach_GAMA_22
		* h_strike_04_Breach_GAMA_3
		* h_strike_04_Breach_GAMA_5
		* h_strike_04_Breach_GAMA_6
		* h_strike_04_Breach_a_spawnFreighter

## h_strike_04_Breach_i_onIntroDone
	* StepId: 15
	* Type: Trigger
	* TargetType: OnInGameSequenceFinishedForPlayer
	* TVS: 1
	* SuccLL: 
		* h_strike_04_Breach_GAMA_15
		* h_strike_04_Breach_a_cameraLookCenter
		* h_strike_04_Breach_a_useLineOfSight

## h_strike_04_Breach_i_setupEnemies
	* StepId: 6
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_strike_04_Breach_a_spawnBase
		* h_strike_04_Breach_a_spawnBlockadeWave_02_01
		* h_strike_04_Breach_a_spawnPatrol1
		* h_strike_04_Breach_a_spawnTurrets1
		* h_strike_04_Breach_a_spawnTurrets2
		* h_strike_04_Breach_a_spawnTurrets3

## h_strike_04_Breach_Start
	* StepId: 0
	* Type: Trigger
	* TargetType: MissionStart
	* SuccLL: h_strike_04_Breach_GAMA_0

## h_strike_04_Breach_t_enemyRespawns
	* StepId: 7
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: h_strike_04_Breach_g_killTurrets2
	* SuccLL: 
		* h_strike_04_Breach_GAMA_11
		* h_strike_04_Breach_GAMA_7
		* h_strike_04_Breach_GAMA_9
		* h_strike_04_Breach_a_spawnRespawnWave1
		* h_strike_04_Breach_a_spawnRespawnWave2

## h_strike_04_Breach_t_escortWait1
	* StepId: 32
	* Type: Trigger
	* TargetType: ReachPointOfInterest
	* SuccLL: h_strike_04_Breach_a_disableEscort1

## h_strike_04_Breach_t_escortWait2
	* StepId: 33
	* Type: Trigger
	* TargetType: ReachPointOfInterest
	* SuccLL: h_strike_04_Breach_a_disableEscort2

## h_strike_04_Breach_t_freighterKilled
	* StepId: 4
	* Type: Trigger
	* TargetType: OnTaggedUnitKilled
	* SuccLL: h_strike_04_Breach_GAMA_4

## h_strike_04_Breach_t_killRespawn1
	* StepId: 8
	* Type: TriggerRepeating
	* TargetType: KillSpecificWave
	* SuccLL: h_strike_04_Breach_GAMA_8

## h_strike_04_Breach_t_killRespawn2
	* StepId: 10
	* Type: TriggerRepeating
	* TargetType: KillSpecificWave
	* SuccLL: h_strike_04_Breach_GAMA_10

## h_strike_04_Breach_t_killTurrets1
	* StepId: 24
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: h_strike_04_Breach_g_killTurrets1
	* SuccLL: h_strike_04_Breach_a_reactivateEscort1

## h_strike_04_Breach_t_killTurrets1and2
	* StepId: 25
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* h_strike_04_Breach_g_killTurrets1
		* h_strike_04_Breach_g_killTurrets2
	* SuccLL: h_strike_04_Breach_a_reactivateEscort2

## h_strike_04_Breach_t_missionSuccess
	* StepId: 2
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: h_strike_04_Breach_w_waitForEndMission2
	* SuccLL: h_strike_04_Breach_GAMA_2

## h_strike_04_Breach_t_respawnBlockadeWave02
	* StepId: 22
	* Type: TriggerRepeating
	* TargetType: KillSpecificWave
	* SuccLL: h_strike_04_Breach_a_respawnBlockadeBossWave02

## h_strike_04_Breach_t_respawnDelay1
	* StepId: 9
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_strike_04_Breach_a_respawnWave1

## h_strike_04_Breach_t_respawnDelay2
	* StepId: 11
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_strike_04_Breach_a_respawnWave2

## h_strike_04_Breach_t_turrets2StrengthCheck
	* StepId: 27
	* Type: Trigger
	* TargetType: TaggedUnitsBelowStrength
	* SuccLL: h_strike_04_Breach_a_spawnAmbush1

## h_strike_04_Breach_t_turrets3StrengthCheck
	* StepId: 28
	* Type: Trigger
	* TargetType: TaggedUnitsBelowStrength
	* SuccLL: h_strike_04_Breach_a_spawnAmbush2

## h_strike_04_Breach_t_waitForTimeToDisableRespawns
	* StepId: 12
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_strike_04_Breach_a_disableRespawn

## h_strike_04_Breach_w_explodeTimer
	* StepId: 19
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_strike_04_Breach_GAMA_19
		* h_strike_04_Breach_a_baseExplosionCameraLookAt
		* h_strike_04_Breach_a_makePlayer3Invincible
		* h_strike_04_Breach_a_makePlayer4Invincible
		* h_strike_04_Breach_a_makePlayer5Invincible

## h_strike_04_Breach_w_setupInvincibility
	* StepId: 13
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_strike_04_Breach_a_Turrets2Invinc
		* h_strike_04_Breach_a_Turrets3Invinc
		* h_strike_04_Breach_a_baseInvinc
		* h_strike_04_Breach_a_disableFreighterForStart

## h_strike_04_Breach_w_startTimer
	* StepId: 23
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_strike_04_Breach_GAMA_23
		* h_strike_04_Breach_GAMA_24
		* h_strike_04_Breach_GAMA_25
		* h_strike_04_Breach_GAMA_26
		* h_strike_04_Breach_GAMA_27
		* h_strike_04_Breach_GAMA_28
		* h_strike_04_Breach_GAMA_29
		* h_strike_04_Breach_GAMA_30
		* h_strike_04_Breach_GAMA_31
		* h_strike_04_Breach_GAMA_32

## h_strike_04_Breach_w_waitForEndMission1
	* StepId: 20
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_strike_04_Breach_GAMA_20
		* h_strike_04_Breach_a_explodeAlly
		* h_strike_04_Breach_a_explodeBase

## h_strike_04_Breach_w_waitForEndMission2
	* StepId: 21
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_strike_04_Breach_a_cleanUp
		* h_strike_04_Breach_a_deactivateRespawns
		* h_strike_04_Breach_a_makePlayer3Vincible
		* h_strike_04_Breach_a_makePlayer4Vincible
		* h_strike_04_Breach_a_makePlayer5Vincible

## h_strike_04_Breach_w_waitForIntro
	* StepId: 16
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_strike_04_Breach_a_introDialog

## h_strike_04_Breach_w_waitForMissionEndFail
	* StepId: 5
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_strike_04_Breach_missionFail

## h_strike_04_Breach_w_waitForMissionEndSuccess
	* StepId: 3
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_strike_04_Breach_a_finishMissionSuccess

## h_strike_05_NightmareGulf_8ef80d3c74ed41041b017ee31cbff94a
	* StepId: 18
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_strike_05_NightmareGulf_end

## h_strike_05_NightmareGulf_goal_destroyChains
	* StepId: 10
	* Type: Goal
	* TargetType: AllUnitsWithTagsAreKilled
	* SuccLL: 
		* h_strike_05_NightmareGulf_GAMA_10
		* h_strike_05_NightmareGulf_deactivate_vfxObserver

## h_strike_05_NightmareGulf_goal_destroyKidara
	* StepId: 16
	* Type: Goal
	* TargetType: AllUnitsWithTagsAreKilled
	* SuccLL: 
		* h_strike_05_NightmareGulf_GAMA_16
		* h_strike_05_NightmareGulf_GAMA_19
		* h_strike_05_NightmareGulf_GAMA_20

## h_strike_05_NightmareGulf_goal_destroyStation
	* StepId: 8
	* Type: Goal
	* TargetType: KillSpecificWave
	* SuccLL: 
		* h_strike_05_NightmareGulf_GAMA_8
		* h_strike_05_NightmareGulf_deactivate_reinforcemenets

## h_strike_05_NightmareGulf_healthCheck_armor1
	* StepId: 24
	* Type: Trigger
	* TargetType: TaggedUnitsBelowHealthAndArmor
	* SuccLL: h_strike_05_NightmareGulf_skill_missileBarrage1

## h_strike_05_NightmareGulf_healthCheck_armor2
	* StepId: 31
	* Type: Trigger
	* TargetType: TaggedUnitsBelowHealthAndArmor
	* SuccLL: h_strike_05_NightmareGulf_GAMA_31

## h_strike_05_NightmareGulf_healthCheck_armor3
	* StepId: 42
	* Type: Trigger
	* TargetType: TaggedUnitsBelowHealthAndArmor
	* SuccLL: 
		* h_strike_05_NightmareGulf_GAMA_42
		* h_strike_05_NightmareGulf_GAMA_43
		* h_strike_05_NightmareGulf_spawn_torpedo1a

## h_strike_05_NightmareGulf_healthCheck_armor4
	* StepId: 54
	* Type: Trigger
	* TargetType: TaggedUnitsBelowHealthAndArmor
	* SuccLL: h_strike_05_NightmareGulf_spawn_squad1

## h_strike_05_NightmareGulf_healthCheck_armor5
	* StepId: 61
	* Type: Trigger
	* TargetType: TaggedUnitsBelowHealthAndArmor
	* SuccLL: h_strike_05_NightmareGulf_GAMA_61

## h_strike_05_NightmareGulf_healthCheck_armor6
	* StepId: 73
	* Type: Trigger
	* TargetType: TaggedUnitsBelowHealthAndArmor
	* SuccLL: 
		* h_strike_05_NightmareGulf_GAMA_73
		* h_strike_05_NightmareGulf_GAMA_74
		* h_strike_05_NightmareGulf_spawn_torpedo2a

## h_strike_05_NightmareGulf_healthCheck_armor7
	* StepId: 85
	* Type: Trigger
	* TargetType: TaggedUnitsBelowHealthAndArmor
	* SuccLL: h_strike_05_NightmareGulf_spawn_squad2

## h_strike_05_NightmareGulf_healthCheck_armor8
	* StepId: 92
	* Type: Trigger
	* TargetType: TaggedUnitsBelowHealthAndArmor
	* SuccLL: h_strike_05_NightmareGulf_GAMA_92

## h_strike_05_NightmareGulf_healthCheck_hull1
	* StepId: 25
	* Type: Trigger
	* TargetType: TaggedUnitsBelowHealthAndArmor
	* SuccLL: h_strike_05_NightmareGulf_GAMA_25

## h_strike_05_NightmareGulf_healthCheck_hull2
	* StepId: 36
	* Type: Trigger
	* TargetType: TaggedUnitsBelowHealthAndArmor
	* SuccLL: h_strike_05_NightmareGulf_GAMA_36

## h_strike_05_NightmareGulf_healthCheck_hull3
	* StepId: 48
	* Type: Trigger
	* TargetType: TaggedUnitsBelowHealthAndArmor
	* SuccLL: h_strike_05_NightmareGulf_GAMA_48

## h_strike_05_NightmareGulf_healthCheck_hull4
	* StepId: 55
	* Type: Trigger
	* TargetType: TaggedUnitsBelowHealthAndArmor
	* SuccLL: h_strike_05_NightmareGulf_GAMA_55

## h_strike_05_NightmareGulf_healthCheck_hull5
	* StepId: 67
	* Type: Trigger
	* TargetType: TaggedUnitsBelowHealthAndArmor
	* SuccLL: h_strike_05_NightmareGulf_GAMA_67

## h_strike_05_NightmareGulf_healthCheck_hull6
	* StepId: 79
	* Type: Trigger
	* TargetType: TaggedUnitsBelowHealthAndArmor
	* SuccLL: h_strike_05_NightmareGulf_GAMA_79

## h_strike_05_NightmareGulf_healthCheck_hull7
	* StepId: 86
	* Type: Trigger
	* TargetType: TaggedUnitsBelowHealthAndArmor
	* SuccLL: h_strike_05_NightmareGulf_GAMA_86

## h_strike_05_NightmareGulf_healthCheck_hull8
	* StepId: 103
	* Type: Trigger
	* TargetType: TaggedUnitsBelowHealthAndArmor
	* SuccLL: 
		* h_strike_05_NightmareGulf_GAMA_103
		* h_strike_05_NightmareGulf_GAMA_105
		* h_strike_05_NightmareGulf_GAMA_106
		* h_strike_05_NightmareGulf_d_destruct
		* h_strike_05_NightmareGulf_deactivate_goalDialogs
		* h_strike_05_NightmareGulf_deactivate_kidaraDestruct
		* h_strike_05_NightmareGulf_invincible_99

## h_strike_05_NightmareGulf_i_armor1
	* StepId: 23
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: h_strike_05_NightmareGulf_GAMA_23

## h_strike_05_NightmareGulf_i_armor2
	* StepId: 30
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: h_strike_05_NightmareGulf_GAMA_30

## h_strike_05_NightmareGulf_i_armor3
	* StepId: 41
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: h_strike_05_NightmareGulf_GAMA_41

## h_strike_05_NightmareGulf_i_armor4
	* StepId: 53
	* Type: None
	* TargetType: Immediate
	* SuccLL: h_strike_05_NightmareGulf_GAMA_53

## h_strike_05_NightmareGulf_i_armor5
	* StepId: 60
	* Type: None
	* TargetType: Immediate
	* SuccLL: h_strike_05_NightmareGulf_GAMA_60

## h_strike_05_NightmareGulf_i_armor6
	* StepId: 72
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: h_strike_05_NightmareGulf_GAMA_72

## h_strike_05_NightmareGulf_i_armor7
	* StepId: 84
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: h_strike_05_NightmareGulf_GAMA_84

## h_strike_05_NightmareGulf_i_armor8
	* StepId: 91
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: h_strike_05_NightmareGulf_GAMA_91

## h_strike_05_NightmareGulf_i_base
	* StepId: 2
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_strike_05_NightmareGulf_deactivate_kiithless
		* h_strike_05_NightmareGulf_spawn_base
		* h_strike_05_NightmareGulf_spawn_patrols
		* h_strike_05_NightmareGulf_spawn_platforms

## h_strike_05_NightmareGulf_i_combat
	* StepId: 15
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_strike_05_NightmareGulf_GAMA_15
		* h_strike_05_NightmareGulf_GAMA_30

## h_strike_05_NightmareGulf_i_emp1
	* StepId: 32
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_strike_05_NightmareGulf_GAMA_32
		* h_strike_05_NightmareGulf_deactivate_emp1Telegraph
		* h_strike_05_NightmareGulf_vfx_emp1Telegraph

## h_strike_05_NightmareGulf_i_emp1Stun
	* StepId: 35
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_strike_05_NightmareGulf_addStatMod_stun1A
		* h_strike_05_NightmareGulf_addStatMod_stun1B
		* h_strike_05_NightmareGulf_addStatMod_stun1C
		* h_strike_05_NightmareGulf_vfx_stun1A
		* h_strike_05_NightmareGulf_vfx_stun1B
		* h_strike_05_NightmareGulf_vfx_stun1C

## h_strike_05_NightmareGulf_i_emp2
	* StepId: 62
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_strike_05_NightmareGulf_GAMA_62
		* h_strike_05_NightmareGulf_deactivate_emp2Telegraph
		* h_strike_05_NightmareGulf_vfx_emp2Telegraph

## h_strike_05_NightmareGulf_i_emp2Stun
	* StepId: 66
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_strike_05_NightmareGulf_addStatMod_stun2A
		* h_strike_05_NightmareGulf_addStatMod_stun2B
		* h_strike_05_NightmareGulf_addStatMod_stun2C
		* h_strike_05_NightmareGulf_vfx_stun2A
		* h_strike_05_NightmareGulf_vfx_stun2AllyB
		* h_strike_05_NightmareGulf_vfx_stun2AllyC

## h_strike_05_NightmareGulf_i_emp3
	* StepId: 93
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_strike_05_NightmareGulf_GAMA_93
		* h_strike_05_NightmareGulf_deactivate_emp3Telegraph
		* h_strike_05_NightmareGulf_vfx_emp3Telegraph

## h_strike_05_NightmareGulf_i_emp3Stun
	* StepId: 96
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_strike_05_NightmareGulf_addStatMod_stun3A
		* h_strike_05_NightmareGulf_addStatMod_stun3B
		* h_strike_05_NightmareGulf_addStatMod_stun3C
		* h_strike_05_NightmareGulf_vfx_stun3A
		* h_strike_05_NightmareGulf_vfx_stun3B
		* h_strike_05_NightmareGulf_vfx_stun3C

## h_strike_05_NightmareGulf_i_gameplay
	* StepId: 12
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: h_strike_05_NightmareGulf_GAMA_12

## h_strike_05_NightmareGulf_i_goals
	* StepId: 7
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_strike_05_NightmareGulf_GAMA_7
		* h_strike_05_NightmareGulf_GAMA_9

## h_strike_05_NightmareGulf_i_kidara
	* StepId: 108
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_strike_05_NightmareGulf_addSkill_missileBarrage
		* h_strike_05_NightmareGulf_invincible_1
		* h_strike_05_NightmareGulf_spawn_kidara
		* h_strike_05_NightmareGulf_spawn_kidaraFleetA
		* h_strike_05_NightmareGulf_spawn_kidaraFleetB

## h_strike_05_NightmareGulf_i_observer
	* StepId: 3
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_strike_05_NightmareGulf_GAMA_3
		* h_strike_05_NightmareGulf_deactivate_chains
		* h_strike_05_NightmareGulf_deactivate_observer
		* h_strike_05_NightmareGulf_spawn_chains
		* h_strike_05_NightmareGulf_spawn_observer
		* h_strike_05_NightmareGulf_vfx_chains

## h_strike_05_NightmareGulf_i_reinforcements
	* StepId: 111
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_strike_05_NightmareGulf_GAMA_111
		* h_strike_05_NightmareGulf_GAMA_113
		* h_strike_05_NightmareGulf_GAMA_115

## h_strike_05_NightmareGulf_i_repair1
	* StepId: 26
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_strike_05_NightmareGulf_GAMA_26
		* h_strike_05_NightmareGulf_armor_1_1
		* h_strike_05_NightmareGulf_vfx_heal1
		* h_strike_05_NightmareGulf_vfx_repair1

## h_strike_05_NightmareGulf_i_repair2
	* StepId: 37
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_strike_05_NightmareGulf_GAMA_37
		* h_strike_05_NightmareGulf_armor_2_1
		* h_strike_05_NightmareGulf_vfx_heal2
		* h_strike_05_NightmareGulf_vfx_repair2

## h_strike_05_NightmareGulf_i_repair3
	* StepId: 49
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_strike_05_NightmareGulf_GAMA_49
		* h_strike_05_NightmareGulf_armor_3_1
		* h_strike_05_NightmareGulf_vfx_heal3
		* h_strike_05_NightmareGulf_vfx_repair3

## h_strike_05_NightmareGulf_i_repair4
	* StepId: 56
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_strike_05_NightmareGulf_GAMA_56
		* h_strike_05_NightmareGulf_armor_4_1
		* h_strike_05_NightmareGulf_vfx_heal4
		* h_strike_05_NightmareGulf_vfx_repair4

## h_strike_05_NightmareGulf_i_repair5
	* StepId: 68
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_strike_05_NightmareGulf_GAMA_68
		* h_strike_05_NightmareGulf_armor_5_1
		* h_strike_05_NightmareGulf_vfx_heal5
		* h_strike_05_NightmareGulf_vfx_repair5

## h_strike_05_NightmareGulf_i_repair6
	* StepId: 80
	* Type: None
	* TargetType: Immediate
	* SuccLL: 
		* h_strike_05_NightmareGulf_GAMA_80
		* h_strike_05_NightmareGulf_armor_6_1
		* h_strike_05_NightmareGulf_vfx_heal6
		* h_strike_05_NightmareGulf_vfx_repair6

## h_strike_05_NightmareGulf_i_repair7
	* StepId: 87
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_strike_05_NightmareGulf_GAMA_87
		* h_strike_05_NightmareGulf_armor_7_1
		* h_strike_05_NightmareGulf_vfx_heal7
		* h_strike_05_NightmareGulf_vfx_repair7

## h_strike_05_NightmareGulf_i_setup
	* StepId: 1
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_strike_05_NightmareGulf_GAMA_1
		* h_strike_05_NightmareGulf_GAMA_2

## h_strike_05_NightmareGulf_sequenceEnd_intro
	* StepId: 6
	* Type: Trigger
	* TargetType: OnInGameSequenceFinishedForPlayer
	* TVS: 1
	* SuccLL: 
		* h_strike_05_NightmareGulf_GAMA_11
		* h_strike_05_NightmareGulf_GAMA_117
		* h_strike_05_NightmareGulf_GAMA_6
		* h_strike_05_NightmareGulf_activate_kiithless
		* h_strike_05_NightmareGulf_lookAt_center
		* h_strike_05_NightmareGulf_los_introOn

## h_strike_05_NightmareGulf_start
	* StepId: 0
	* Type: Trigger
	* TargetType: MissionStart
	* SuccLL: 
		* h_strike_05_NightmareGulf_GAMA_0
		* h_strike_05_NightmareGulf_GAMA_4
		* h_strike_05_NightmareGulf_GAMA_5
		* h_strike_05_NightmareGulf_los_introOff
		* h_strike_05_NightmareGulf_sequence_intro

## h_strike_05_NightmareGulf_strength_all
	* StepId: 13
	* Type: Trigger
	* TargetType: TaggedUnitsBelowStrength
	* SuccLL: 
		* h_strike_05_NightmareGulf_GAMA_110
		* h_strike_05_NightmareGulf_GAMA_13
		* h_strike_05_NightmareGulf_ai_followFlagship

## h_strike_05_NightmareGulf_w_amassari
	* StepId: 19
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_strike_05_NightmareGulf_spawn_amassari

## h_strike_05_NightmareGulf_w_clean
	* StepId: 21
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_strike_05_NightmareGulf_remove_progenitorHelp

## h_strike_05_NightmareGulf_w_closeDestructDialog
	* StepId: 106
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_strike_05_NightmareGulf_close_destruct

## h_strike_05_NightmareGulf_w_combat
	* StepId: 15
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_strike_05_NightmareGulf_GAMA_15
		* h_strike_05_NightmareGulf_GAMA_21

## h_strike_05_NightmareGulf_w_deactivateGoalDialogsRepeating
	* StepId: 107
	* Type: TriggerRepeating
	* TargetType: WaitForTime
	* SuccLL: h_strike_05_NightmareGulf_deactivate_goalDialogsRepeating

## h_strike_05_NightmareGulf_w_deactivateOpenGoals
	* StepId: 20
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_strike_05_NightmareGulf_deactivate_freeObserverHelp

## h_strike_05_NightmareGulf_w_emp1
	* StepId: 33
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_strike_05_NightmareGulf_GAMA_33
		* h_strike_05_NightmareGulf_GAMA_34
		* h_strike_05_NightmareGulf_activate_emp1Telegraph
		* h_strike_05_NightmareGulf_invincible_2b
		* h_strike_05_NightmareGulf_vfx_emp1

## h_strike_05_NightmareGulf_w_emp2
	* StepId: 63
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_strike_05_NightmareGulf_GAMA_63
		* h_strike_05_NightmareGulf_GAMA_64
		* h_strike_05_NightmareGulf_GAMA_65
		* h_strike_05_NightmareGulf_activate_emp2Telegraph
		* h_strike_05_NightmareGulf_invincible_5b
		* h_strike_05_NightmareGulf_vfx_emp2

## h_strike_05_NightmareGulf_w_emp3
	* StepId: 94
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_strike_05_NightmareGulf_GAMA_94
		* h_strike_05_NightmareGulf_GAMA_95
		* h_strike_05_NightmareGulf_GAMA_96
		* h_strike_05_NightmareGulf_activate_emp3Telegraph
		* h_strike_05_NightmareGulf_invincible_8b
		* h_strike_05_NightmareGulf_vfx_emp3

## h_strike_05_NightmareGulf_w_engage
	* StepId: 118
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_strike_05_NightmareGulf_d_engage

## h_strike_05_NightmareGulf_w_freeObserver
	* StepId: 11
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_strike_05_NightmareGulf_d_freeObserver
		* h_strike_05_NightmareGulf_preferredTaget_observerHelp
		* h_strike_05_NightmareGulf_spawn_observerHelp

## h_strike_05_NightmareGulf_w_gameplay
	* StepId: 22
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* h_strike_05_NightmareGulf_GAMA_102
		* h_strike_05_NightmareGulf_GAMA_22
		* h_strike_05_NightmareGulf_GAMA_24
		* h_strike_05_NightmareGulf_GAMA_35
		* h_strike_05_NightmareGulf_GAMA_47
		* h_strike_05_NightmareGulf_GAMA_54
		* h_strike_05_NightmareGulf_GAMA_66
		* h_strike_05_NightmareGulf_GAMA_78
		* h_strike_05_NightmareGulf_GAMA_85

## h_strike_05_NightmareGulf_w_introDialog1
	* StepId: 5
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_strike_05_NightmareGulf_activate_kiithlessIntro

## h_strike_05_NightmareGulf_w_kidaraSpawn
	* StepId: 14
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_strike_05_NightmareGulf_GAMA_107
		* h_strike_05_NightmareGulf_GAMA_108
		* h_strike_05_NightmareGulf_GAMA_109
		* h_strike_05_NightmareGulf_GAMA_14

## h_strike_05_NightmareGulf_w_kidaraSpawnDialog
	* StepId: 109
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_strike_05_NightmareGulf_d_kidara

## h_strike_05_NightmareGulf_w_kidaraSpawnSquad
	* StepId: 110
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_strike_05_NightmareGulf_spawn_squad

## h_strike_05_NightmareGulf_w_missileBarrage2
	* StepId: 65
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_strike_05_NightmareGulf_skill_missileBarrage2

## h_strike_05_NightmareGulf_w_outro
	* StepId: 17
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_strike_05_NightmareGulf_GAMA_17
		* h_strike_05_NightmareGulf_GAMA_18
		* h_strike_05_NightmareGulf_d_win

## h_strike_05_NightmareGulf_w_reinforcementsA
	* StepId: 112
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_strike_05_NightmareGulf_GAMA_112
		* h_strike_05_NightmareGulf_spawn_reinforcementsA

## h_strike_05_NightmareGulf_w_reinforcementsB
	* StepId: 114
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_strike_05_NightmareGulf_GAMA_114
		* h_strike_05_NightmareGulf_spawn_reinforcementsB

## h_strike_05_NightmareGulf_w_reinforcementsC
	* StepId: 116
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_strike_05_NightmareGulf_GAMA_116
		* h_strike_05_NightmareGulf_spawn_reinforcementsC

## h_strike_05_NightmareGulf_w_reinforcmentsADialog
	* StepId: 113
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_strike_05_NightmareGulf_d_reinforcementsA

## h_strike_05_NightmareGulf_w_reinforcmentsBDialog
	* StepId: 115
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_strike_05_NightmareGulf_d_reinforcementsB

## h_strike_05_NightmareGulf_w_reinforcmentsCDialog
	* StepId: 117
	* Type: Trigger
	* TargetType: WaitForTime

## h_strike_05_NightmareGulf_w_repair1_1
	* StepId: 27
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_strike_05_NightmareGulf_GAMA_27
		* h_strike_05_NightmareGulf_armor_1_2

## h_strike_05_NightmareGulf_w_repair1_2
	* StepId: 28
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_strike_05_NightmareGulf_GAMA_28
		* h_strike_05_NightmareGulf_armor_1_3

## h_strike_05_NightmareGulf_w_repair1_3
	* StepId: 29
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_strike_05_NightmareGulf_GAMA_29
		* h_strike_05_NightmareGulf_armor_1_4
		* h_strike_05_NightmareGulf_invincible_2

## h_strike_05_NightmareGulf_w_repair2_1
	* StepId: 38
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_strike_05_NightmareGulf_GAMA_38
		* h_strike_05_NightmareGulf_armor_2_2

## h_strike_05_NightmareGulf_w_repair2_2
	* StepId: 39
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_strike_05_NightmareGulf_GAMA_39
		* h_strike_05_NightmareGulf_armor_2_3

## h_strike_05_NightmareGulf_w_repair2_3
	* StepId: 40
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_strike_05_NightmareGulf_GAMA_40
		* h_strike_05_NightmareGulf_armor_2_4
		* h_strike_05_NightmareGulf_invincible_3

## h_strike_05_NightmareGulf_w_repair3_1
	* StepId: 50
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_strike_05_NightmareGulf_GAMA_50
		* h_strike_05_NightmareGulf_armor_3_2

## h_strike_05_NightmareGulf_w_repair3_2
	* StepId: 51
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_strike_05_NightmareGulf_GAMA_51
		* h_strike_05_NightmareGulf_armor_3_3

## h_strike_05_NightmareGulf_w_repair3_3
	* StepId: 52
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_strike_05_NightmareGulf_GAMA_52
		* h_strike_05_NightmareGulf_armor_3_4
		* h_strike_05_NightmareGulf_invincible_4

## h_strike_05_NightmareGulf_w_repair4_1
	* StepId: 57
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_strike_05_NightmareGulf_GAMA_57
		* h_strike_05_NightmareGulf_armor_4_2

## h_strike_05_NightmareGulf_w_repair4_2
	* StepId: 58
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_strike_05_NightmareGulf_GAMA_58
		* h_strike_05_NightmareGulf_armor_4_3

## h_strike_05_NightmareGulf_w_repair4_3
	* StepId: 59
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_strike_05_NightmareGulf_GAMA_59
		* h_strike_05_NightmareGulf_armor_4_4
		* h_strike_05_NightmareGulf_invincible_5

## h_strike_05_NightmareGulf_w_repair5_1
	* StepId: 69
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_strike_05_NightmareGulf_GAMA_69
		* h_strike_05_NightmareGulf_armor_5_2

## h_strike_05_NightmareGulf_w_repair5_2
	* StepId: 70
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_strike_05_NightmareGulf_GAMA_70
		* h_strike_05_NightmareGulf_armor_5_3

## h_strike_05_NightmareGulf_w_repair5_3
	* StepId: 71
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_strike_05_NightmareGulf_GAMA_71
		* h_strike_05_NightmareGulf_armor_5_4
		* h_strike_05_NightmareGulf_invincible_6

## h_strike_05_NightmareGulf_w_repair6_1
	* StepId: 81
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_strike_05_NightmareGulf_GAMA_81
		* h_strike_05_NightmareGulf_armor_6_2

## h_strike_05_NightmareGulf_w_repair6_2
	* StepId: 82
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_strike_05_NightmareGulf_GAMA_82
		* h_strike_05_NightmareGulf_armor_6_3

## h_strike_05_NightmareGulf_w_repair6_3
	* StepId: 83
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_strike_05_NightmareGulf_GAMA_83
		* h_strike_05_NightmareGulf_armor_6_4
		* h_strike_05_NightmareGulf_invincible_7

## h_strike_05_NightmareGulf_w_repair7_1
	* StepId: 88
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_strike_05_NightmareGulf_GAMA_88
		* h_strike_05_NightmareGulf_armor_7_2

## h_strike_05_NightmareGulf_w_repair7_2
	* StepId: 89
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_strike_05_NightmareGulf_GAMA_89
		* h_strike_05_NightmareGulf_armor_7_3

## h_strike_05_NightmareGulf_w_repair7_3
	* StepId: 90
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_strike_05_NightmareGulf_GAMA_90
		* h_strike_05_NightmareGulf_armor_7_4
		* h_strike_05_NightmareGulf_invincible_8

## h_strike_05_NightmareGulf_w_startTelegraphDestruct
	* StepId: 104
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_strike_05_NightmareGulf_GAMA_104
		* h_strike_05_NightmareGulf_vfx_telegraphDestruct

## h_strike_05_NightmareGulf_w_stationDialog
	* StepId: 9
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_strike_05_NightmareGulf_d_station

## h_strike_05_NightmareGulf_w_stun1
	* StepId: 34
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_strike_05_NightmareGulf_removeStatMod_stun1A
		* h_strike_05_NightmareGulf_removeStatMod_stun1B
		* h_strike_05_NightmareGulf_removeStatMod_stun1C

## h_strike_05_NightmareGulf_w_stun2
	* StepId: 64
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_strike_05_NightmareGulf_c8c269dc61d05cb43984a12728d801c2
		* h_strike_05_NightmareGulf_removeStatMod_stun2
		* h_strike_05_NightmareGulf_removeStatMod_stun2Ally

## h_strike_05_NightmareGulf_w_stun3
	* StepId: 95
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_strike_05_NightmareGulf_removeStatMod_stun3A
		* h_strike_05_NightmareGulf_removeStatMod_stun3B
		* h_strike_05_NightmareGulf_removeStatMod_stun3C

## h_strike_05_NightmareGulf_w_telegraphDestruct
	* StepId: 105
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_strike_05_NightmareGulf_destruct_kidara
		* h_strike_05_NightmareGulf_dmg_destruct
		* h_strike_05_NightmareGulf_dmg_destructAlly
		* h_strike_05_NightmareGulf_kill_kiithlessA
		* h_strike_05_NightmareGulf_kill_kiithlessB

## h_strike_05_NightmareGulf_w_torpedo1aMark
	* StepId: 43
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_strike_05_NightmareGulf_mark_torpedo1a

## h_strike_05_NightmareGulf_w_torpedo1b
	* StepId: 44
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_strike_05_NightmareGulf_GAMA_44
		* h_strike_05_NightmareGulf_GAMA_45
		* h_strike_05_NightmareGulf_spawn_torpedo1b

## h_strike_05_NightmareGulf_w_torpedo1bMark
	* StepId: 45
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_strike_05_NightmareGulf_mark_torpedo1b

## h_strike_05_NightmareGulf_w_torpedo1c
	* StepId: 46
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_strike_05_NightmareGulf_GAMA_46
		* h_strike_05_NightmareGulf_spawn_torpedo1c

## h_strike_05_NightmareGulf_w_torpedo1cMark
	* StepId: 47
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_strike_05_NightmareGulf_mark_torpedo1c

## h_strike_05_NightmareGulf_w_torpedo2aMark
	* StepId: 74
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_strike_05_NightmareGulf_mark_torpedo2a

## h_strike_05_NightmareGulf_w_torpedo2b
	* StepId: 75
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_strike_05_NightmareGulf_GAMA_75
		* h_strike_05_NightmareGulf_GAMA_76
		* h_strike_05_NightmareGulf_spawn_torpedo2b

## h_strike_05_NightmareGulf_w_torpedo2bMark
	* StepId: 76
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_strike_05_NightmareGulf_mark_torpedo2b

## h_strike_05_NightmareGulf_w_torpedo2c
	* StepId: 77
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_strike_05_NightmareGulf_GAMA_77
		* h_strike_05_NightmareGulf_spawn_torpedo2c

## h_strike_05_NightmareGulf_w_torpedo2cMark
	* StepId: 78
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_strike_05_NightmareGulf_mark_torpedo2c

## h_strike_05_NightmareGulf_w_torpedo3a
	* StepId: 97
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_strike_05_NightmareGulf_GAMA_97
		* h_strike_05_NightmareGulf_GAMA_98
		* h_strike_05_NightmareGulf_spawn_torpedo3a

## h_strike_05_NightmareGulf_w_torpedo3aMark
	* StepId: 98
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_strike_05_NightmareGulf_mark_torpedo3a

## h_strike_05_NightmareGulf_w_torpedo3b
	* StepId: 99
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_strike_05_NightmareGulf_GAMA_100
		* h_strike_05_NightmareGulf_GAMA_99
		* h_strike_05_NightmareGulf_spawn_torpedo3b

## h_strike_05_NightmareGulf_w_torpedo3bMark
	* StepId: 100
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_strike_05_NightmareGulf_mark_torpedo3b

## h_strike_05_NightmareGulf_w_torpedo3c
	* StepId: 101
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* h_strike_05_NightmareGulf_GAMA_101
		* h_strike_05_NightmareGulf_spawn_torpedo3c

## h_strike_05_NightmareGulf_w_torpedo3cMark
	* StepId: 102
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: h_strike_05_NightmareGulf_mark_torpedo3c

## h_strike_05_NightmareGulf_w_vfxObserver
	* StepId: 4
	* Type: TriggerRepeating
	* TargetType: WaitForTime
	* SuccLL: h_strike_05_NightmareGulf_vfx_observer

## h_strike_x_DownTheWell_bossDead_victimEscaped
	* StepId: 13
	* Type: Goal
	* TargetType: FinishGoalsString
	* TVS: 
		* h_strike_x_DownTheWell_kill_boss
		* h_strike_x_DownTheWell_victim_escape
	* SuccLL: 
		* h_strike_x_DownTheWell_af92e6c61bd69294cb3376258d92bbda
		* h_strike_x_DownTheWell_wreck_dia

## h_strike_x_DownTheWell_first_tower_killed
	* StepId: 6
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* h_strike_x_DownTheWell_kill_tower1
		* h_strike_x_DownTheWell_kill_tower2
	* SuccLL: 
		* h_strike_x_DownTheWell_90a745174c73027449356ff2d90b898d
		* h_strike_x_DownTheWell_Base1_dead

## h_strike_x_DownTheWell_goto_victim
	* StepId: 9
	* Type: Trigger
	* TargetType: ReachPosition
	* TVS: 
		* 10700
		* 13600
	* SuccLL: 
		* h_strike_x_DownTheWell_ce03ce1d63f293042a8c355b74d6bd60
		* h_strike_x_DownTheWell_helping_victim

## h_strike_x_DownTheWell_intro_dia_finished
	* StepId: 2
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: Raid005_Intro_dialog
	* SuccLL: h_strike_x_DownTheWell_888f80c463b166e44ad233811628ed48

## h_strike_x_DownTheWell_kill_boss
	* StepId: 12
	* Type: Trigger
	* TargetType: KillSpecificWave

## h_strike_x_DownTheWell_kill_tower1
	* StepId: 4
	* Type: Trigger
	* TargetType: KillSpecificWave

## h_strike_x_DownTheWell_kill_tower2
	* StepId: 5
	* Type: Trigger
	* TargetType: KillSpecificWave

## h_strike_x_DownTheWell_landing_dia_finished
	* StepId: 1
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: Raid005_Landing_dialog
	* SuccLL: 
		* h_strike_x_DownTheWell_GAMA_0
		* h_strike_x_DownTheWell_intro_dia

## h_strike_x_DownTheWell_reach_tower_base
	* StepId: 3
	* Type: Goal
	* TargetType: ReachPosition
	* TVS: 
		* 0
		* 0
	* SuccLL: 
		* h_strike_x_DownTheWell_41065c926a5b2214fb170888fa6799d7
		* h_strike_x_DownTheWell_55eb828a4452b6a41b25606a26d7be99
		* h_strike_x_DownTheWell_9e8c287ede08f3d45aac7cc2d5f07aa8
		* h_strike_x_DownTheWell_c4b397861a800c045b218231d1bc55f1
		* h_strike_x_DownTheWell_challenge_dia
		* h_strike_x_DownTheWell_d2e675b1a9c4dde44b9b4e0c373ea365
		* h_strike_x_DownTheWell_dba55679414760e46a2d19376e1a6acd
		* h_strike_x_DownTheWell_enable_tower1
		* h_strike_x_DownTheWell_enable_tower2
		* h_strike_x_DownTheWell_spawn_wave1

## h_strike_x_DownTheWell_rescue_wait_time
	* StepId: 10
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: Raid005_Wreck_dialog
	* SuccLL: 
		* h_strike_x_DownTheWell_113bd747513c1c44bb16c1c975458998
		* h_strike_x_DownTheWell_270f05632898d2147ba5a1dff20c079c
		* h_strike_x_DownTheWell_boss_spawning_dia
		* h_strike_x_DownTheWell_enable_victim
		* h_strike_x_DownTheWell_f7425621e2fc06d468262a854097275a
		* h_strike_x_DownTheWell_spawn_boss

## h_strike_x_DownTheWell_second_tower_killed
	* StepId: 8
	* Type: Goal
	* TargetType: FinishGoalsString
	* TVS: 
		* h_strike_x_DownTheWell_kill_tower1
		* h_strike_x_DownTheWell_kill_tower2
	* SuccLL: 
		* h_strike_x_DownTheWell_base2_dead
		* h_strike_x_DownTheWell_c12f974e5b7d92c4d9c16187e43578ff
		* h_strike_x_DownTheWell_d0a711c1bfa452e40a6f6936197f155d

## h_strike_x_DownTheWell_Start
	* StepId: 0
	* Type: Trigger
	* TargetType: MissionStart
	* SuccLL: 
		* h_strike_x_DownTheWell_a9929bb4c8595394ab070dbf6e29f121
		* h_strike_x_DownTheWell_disable_tower1
		* h_strike_x_DownTheWell_disable_tower2
		* h_strike_x_DownTheWell_disable_victim
		* h_strike_x_DownTheWell_landing_dia
		* h_strike_x_DownTheWell_spawn_tower1
		* h_strike_x_DownTheWell_spawn_tower2
		* h_strike_x_DownTheWell_spawn_victim

## h_strike_x_DownTheWell_tower_time_limit
	* StepId: 7
	* Type: Goal
	* TargetType: WaitForTime
	* SuccLL: 
		* h_strike_x_DownTheWell_invuln_tower1
		* h_strike_x_DownTheWell_invuln_tower2
		* h_strike_x_DownTheWell_mission_fail_tower
		* h_strike_x_DownTheWell_restore_tower1
		* h_strike_x_DownTheWell_restore_tower2
		* h_strike_x_DownTheWell_tower_repaired

## h_strike_x_DownTheWell_tower1_below_33pct_hp
	* StepId: 16
	* Type: Trigger
	* TargetType: OnTaggedUnitIsBelowHealth
	* SuccLL: h_strike_x_DownTheWell_spawn_tower1_reinforcement2

## h_strike_x_DownTheWell_tower1_below_66pct_hp
	* StepId: 15
	* Type: Trigger
	* TargetType: OnTaggedUnitIsBelowHealth
	* SuccLL: 
		* h_strike_x_DownTheWell_0b05cf074edff7546afffd4a7435e51a
		* h_strike_x_DownTheWell_spawn_tower1_reinforcement1

## h_strike_x_DownTheWell_tower2_below_33pct_hp
	* StepId: 18
	* Type: Trigger
	* TargetType: OnTaggedUnitIsBelowHealth
	* SuccLL: h_strike_x_DownTheWell_spawn_tower2_reinforcement2

## h_strike_x_DownTheWell_tower2_below_66pct_hp
	* StepId: 17
	* Type: Trigger
	* TargetType: OnTaggedUnitIsBelowHealth
	* SuccLL: 
		* h_strike_x_DownTheWell_32580a1360da1ee4ba474255bf24d052
		* h_strike_x_DownTheWell_spawn_tower2_reinforcement1

## h_strike_x_DownTheWell_victim_escape
	* StepId: 11
	* Type: Trigger
	* TargetType: ReachPosition
	* TVS: 
		* 0
		* 0

## h_strike_x_DownTheWell_wreck_dia_finished
	* StepId: 14
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: Raid005_BossDead_dialog
	* SuccLL: h_strike_x_DownTheWell_mission_success

## t_belt_lobby_init
	* StepId: 0
	* Type: Trigger
	* TargetType: MissionStart
	* SuccLL: t_belt_lobby_finish

## t_belt_t0_lobby_init
	* StepId: 0
	* Type: Trigger
	* TargetType: MissionStart
	* SuccLL: 
		* t_belt_t0_lobby_finish
		* t_belt_t0_showT0UIHighlight

## t_friendlyBeacon_starbase_init
	* StepId: 0
	* Type: Trigger
	* TargetType: MissionStart
	* SuccLL: 
		* t_friendlyBeacon_starbase_act_add_PlayerHeal_Step
		* t_friendlyBeacon_starbase_trigger_npc_trigWait1
		* t_friendlyBeacon_starbase_trigger_npc_wave0
		* t_friendlyBeacon_starbase_trigger_npc_wave1

## t_friendlyBeacon_starbase_trigger_rep_wait_PlayerHeal
	* StepId: 3
	* Type: TriggerRepeating
	* TargetType: WaitForTime
	* SuccLL: 
		* t_friendlyBeacon_starbase_act_HealPlayer2
		* t_friendlyBeacon_starbase_act_HealPlayer3
		* t_friendlyBeacon_starbase_act_HealPlayer4
		* t_friendlyBeacon_starbase_act_HealPlayer5
		* t_friendlyBeacon_starbase_act_HealPlayer6

## t_friendlyBeacon_starbase_wave2
	* StepId: 1
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* t_friendlyBeacon_starbase_trigger_npc_trigWait2
		* t_friendlyBeacon_starbase_trigger_npc_wave2

## t_friendlyBeacon_starbase_wave3
	* StepId: 2
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: t_friendlyBeacon_starbase_trigger_npc_wave3

## t_jovian_Start
	* StepId: 0
	* Type: None
	* TargetType: MissionStart
	* SuccLL: t_jovian_GAMA_0

## t_jovian_w_start
	* StepId: 1
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: t_jovian_d_start

## t_liaison_BountyHunt_goal_kill
	* StepId: 3
	* Type: Goal
	* TargetType: Countdown
	* SuccLL: t_liaison_BountyHunt_GAMA_3
	* FailLL: 
		* t_liaison_BountyHunt_GAMA_4
		* t_liaison_BountyHunt_remove_target

## t_liaison_BountyHunt_health_target1
	* StepId: 16
	* Type: Trigger
	* TargetType: TaggedUnitsBelowStrength
	* SuccLL: t_liaison_BountyHunt_ai_followFlagship1

## t_liaison_BountyHunt_health_target2
	* StepId: 10
	* Type: Trigger
	* TargetType: TaggedUnitsBelowStrength
	* SuccLL: t_liaison_BountyHunt_ai_followFlagship2

## t_liaison_BountyHunt_i_loot
	* StepId: 14
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* t_liaison_BountyHunt_interaction_loot1
		* t_liaison_BountyHunt_interaction_loot2

## t_liaison_BountyHunt_kill_target
	* StepId: 12
	* Type: Trigger
	* TargetType: KillSpecificWave
	* SuccLL: t_liaison_BountyHunt_succeed_countdown

## t_liaison_BountyHunt_multi_fail
	* StepId: 6
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* t_liaison_BountyHunt_td_fail
		* t_liaison_BountyHunt_w_failTimeout
	* SuccLL: t_liaison_BountyHunt_fail

## t_liaison_BountyHunt_setup
	* StepId: 13
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* t_liaison_BountyHunt_spawn_bigDecoy1
		* t_liaison_BountyHunt_spawn_bigDecoy2
		* t_liaison_BountyHunt_spawn_bigDecoy3
		* t_liaison_BountyHunt_spawn_bigDecoy4
		* t_liaison_BountyHunt_spawn_smallDecoy1
		* t_liaison_BountyHunt_spawn_smallDecoy2
		* t_liaison_BountyHunt_spawn_smallDecoy3
		* t_liaison_BountyHunt_spawn_smallDecoy4
		* t_liaison_BountyHunt_spawn_smallDecoy5
		* t_liaison_BountyHunt_spawn_smallDecoy6
		* t_liaison_BountyHunt_spawn_target

## t_liaison_BountyHunt_start
	* StepId: 0
	* Type: Trigger
	* TargetType: MissionStart
	* SuccLL: 
		* t_liaison_BountyHunt_GAMA_0
		* t_liaison_BountyHunt_GAMA_1
		* t_liaison_BountyHunt_GAMA_11
		* t_liaison_BountyHunt_GAMA_12
		* t_liaison_BountyHunt_GAMA_13
		* t_liaison_BountyHunt_GAMA_14

## t_liaison_BountyHunt_td_fail
	* StepId: 7
	* Type: Trigger
	* TargetType: OnDialogFinishedIndex

## t_liaison_BountyHunt_td_win
	* StepId: 1
	* Type: Trigger
	* TargetType: OnDialogFinishedIndex
	* SuccLL: t_liaison_BountyHunt_fin

## t_liaison_BountyHunt_w_activate
	* StepId: 11
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: t_liaison_BountyHunt_activate_enemies

## t_liaison_BountyHunt_w_fail1
	* StepId: 5
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* t_liaison_BountyHunt_GAMA_5
		* t_liaison_BountyHunt_GAMA_6
		* t_liaison_BountyHunt_GAMA_7
		* t_liaison_BountyHunt_d_fail

## t_liaison_BountyHunt_w_failTimeout
	* StepId: 8
	* Type: Trigger
	* TargetType: WaitForTime

## t_liaison_BountyHunt_w_fin
	* StepId: 4
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: t_liaison_BountyHunt_d_win

## t_liaison_BountyHunt_w_intro
	* StepId: 2
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* t_liaison_BountyHunt_GAMA_10
		* t_liaison_BountyHunt_GAMA_2
		* t_liaison_BountyHunt_GAMA_8
		* t_liaison_BountyHunt_d_intro

## t_liaison_BountyHunt_w_lookAt
	* StepId: 15
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* t_liaison_BountyHunt_GAMA_15
		* t_liaison_BountyHunt_deactivate_enemies
		* t_liaison_BountyHunt_lookAt_start

## t_liaison_BountyHunt_w_mark
	* StepId: 9
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* t_liaison_BountyHunt_GAMA_9
		* t_liaison_BountyHunt_d_mark
		* t_liaison_BountyHunt_deactivate_health1
		* t_liaison_BountyHunt_mark_target

## t_liaison_DefendBase_exist_beacon1
	* StepId: 17
	* Type: Trigger
	* TargetType: UnitWithTagsExists
	* SuccLL: t_liaison_DefendBase_GAMA_17

## t_liaison_DefendBase_exist_beacon2
	* StepId: 10
	* Type: Trigger
	* TargetType: UnitWithTagsExists
	* SuccLL: t_liaison_DefendBase_GAMA_10

## t_liaison_DefendBase_goal_defendBeacon
	* StepId: 18
	* Type: Goal
	* TargetType: FinishGoalsString
	* TVS: 
		* t_liaison_DefendBase_goal_defendStation
		* t_liaison_DefendBase_i_reinforcements

## t_liaison_DefendBase_goal_defendStation
	* StepId: 15
	* Type: Goal
	* TargetType: WaveFinished
	* SuccLL: t_liaison_DefendBase_GAMA_15

## t_liaison_DefendBase_i_goals
	* StepId: 14
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* t_liaison_DefendBase_GAMA_14
		* t_liaison_DefendBase_GAMA_16
		* t_liaison_DefendBase_GAMA_18
		* t_liaison_DefendBase_GAMA_19
		* t_liaison_DefendBase_GAMA_24

## t_liaison_DefendBase_i_intro
	* StepId: 27
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* t_liaison_DefendBase_GAMA_27
		* t_liaison_DefendBase_GAMA_28

## t_liaison_DefendBase_i_reinforcements
	* StepId: 11
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* t_liaison_DefendBase_GAMA_11
		* t_liaison_DefendBase_ally_reinforcements
		* t_liaison_DefendBase_deactivate_killBeacon

## t_liaison_DefendBase_i_setup
	* StepId: 13
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* t_liaison_DefendBase_spawn_patrolA
		* t_liaison_DefendBase_spawn_patrolB
		* t_liaison_DefendBase_spawn_patrolC
		* t_liaison_DefendBase_spawn_platformA
		* t_liaison_DefendBase_spawn_platformB
		* t_liaison_DefendBase_spawn_platformC
		* t_liaison_DefendBase_spawn_platformD
		* t_liaison_DefendBase_spawn_platformE
		* t_liaison_DefendBase_spawn_platformF
		* t_liaison_DefendBase_spawn_spawner
		* t_liaison_DefendBase_spawn_station

## t_liaison_DefendBase_kill_beacon
	* StepId: 25
	* Type: Trigger
	* TargetType: KillSpecificWave
	* SuccLL: 
		* t_liaison_DefendBase_GAMA_25
		* t_liaison_DefendBase_deactivaet_defendBeacon

## t_liaison_DefendBase_kill_station
	* StepId: 20
	* Type: Trigger
	* TargetType: KillSpecificWave
	* SuccLL: 
		* t_liaison_DefendBase_GAMA_20
		* t_liaison_DefendBase_deactivate_defendStation

## t_liaison_DefendBase_multi_attack
	* StepId: 2
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* t_liaison_DefendBase_td_intro
		* t_liaison_DefendBase_w_dIntro
	* SuccLL: t_liaison_DefendBase_GAMA_2

## t_liaison_DefendBase_multi_fail
	* StepId: 22
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* t_liaison_DefendBase_td_fail
		* t_liaison_DefendBase_w_dFail
	* SuccLL: t_liaison_DefendBase_fail

## t_liaison_DefendBase_start
	* StepId: 0
	* Type: Trigger
	* TargetType: MissionStart
	* SuccLL: 
		* t_liaison_DefendBase_GAMA_0
		* t_liaison_DefendBase_GAMA_1
		* t_liaison_DefendBase_GAMA_12
		* t_liaison_DefendBase_GAMA_13
		* t_liaison_DefendBase_GAMA_26

## t_liaison_DefendBase_strength_station
	* StepId: 19
	* Type: Trigger
	* TargetType: TaggedUnitsBelowStrength
	* SuccLL: t_liaison_DefendBase_d_stationLow

## t_liaison_DefendBase_strength_wave0
	* StepId: 5
	* Type: Trigger
	* TargetType: TaggedUnitsBelowStrength
	* SuccLL: 
		* t_liaison_DefendBase_GAMA_5
		* t_liaison_DefendBase_GAMA_6
		* t_liaison_DefendBase_spawn_wave1
		* t_liaison_DefendBase_spawn_wave1Random

## t_liaison_DefendBase_strength_wave1
	* StepId: 7
	* Type: Trigger
	* TargetType: TaggedUnitsBelowStrength
	* SuccLL: 
		* t_liaison_DefendBase_GAMA_7
		* t_liaison_DefendBase_GAMA_8
		* t_liaison_DefendBase_wave_4
		* t_liaison_DefendBase_wavve_6Random

## t_liaison_DefendBase_td_fail
	* StepId: 24
	* Type: Trigger
	* TargetType: OnDialogFinishedIndex

## t_liaison_DefendBase_td_intro
	* StepId: 31
	* Type: Trigger
	* TargetType: OnDialogFinishedIndex

## t_liaison_DefendBase_td_win
	* StepId: 1
	* Type: Trigger
	* TargetType: OnDialogFinishedIndex
	* SuccLL: t_liaison_DefendBase_win

## t_liaison_DefendBase_w_attack1
	* StepId: 3
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* t_liaison_DefendBase_GAMA_3
		* t_liaison_DefendBase_GAMA_4
		* t_liaison_DefendBase_spawn_wave0
		* t_liaison_DefendBase_spawn_wave0Random

## t_liaison_DefendBase_w_dBeaconDown
	* StepId: 26
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: t_liaison_DefendBase_d_beaconDown

## t_liaison_DefendBase_w_dFail
	* StepId: 23
	* Type: Trigger
	* TargetType: WaitForTime

## t_liaison_DefendBase_w_dIntro
	* StepId: 30
	* Type: Trigger
	* TargetType: WaitForTime

## t_liaison_DefendBase_w_fail
	* StepId: 21
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* t_liaison_DefendBase_GAMA_21
		* t_liaison_DefendBase_GAMA_22
		* t_liaison_DefendBase_GAMA_23
		* t_liaison_DefendBase_d_fail

## t_liaison_DefendBase_w_firstWave
	* StepId: 4
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: t_liaison_DefendBase_d_firstWave

## t_liaison_DefendBase_w_intro
	* StepId: 29
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* t_liaison_DefendBase_GAMA_29
		* t_liaison_DefendBase_GAMA_30
		* t_liaison_DefendBase_d_intro

## t_liaison_DefendBase_w_lookAt
	* StepId: 28
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: t_liaison_DefendBase_lookAt_intro

## t_liaison_DefendBase_w_nextWave1
	* StepId: 6
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: t_liaison_DefendBase_d_nextWave1

## t_liaison_DefendBase_w_nextWave2
	* StepId: 8
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: t_liaison_DefendBase_d_nextWave2

## t_liaison_DefendBase_w_reinforcements
	* StepId: 12
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: t_liaison_DefendBase_d_reinforcements

## t_liaison_DefendBase_w_reinforcements1
	* StepId: 9
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: t_liaison_DefendBase_GAMA_9

## t_liaison_DefendBase_w_win
	* StepId: 16
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: t_liaison_DefendBase_d_win

## t_liaison_Escort_allyHealthLow
	* StepId: 26
	* Type: Trigger
	* TargetType: TaggedUnitsBelowStrength
	* SuccLL: t_liaison_Escort_d_allyLow

## t_liaison_Escort_checkOptionalSpawn
	* StepId: 9
	* Type: Trigger
	* TargetType: UnitWithTagsExists
	* SuccLL: t_liaison_Escort_d_hostiles2

## t_liaison_Escort_goal_defend
	* StepId: 15
	* Type: Goal
	* TargetType: FinishGoalsString
	* TVS: t_liaison_Escort_goal_remaining

## t_liaison_Escort_goal_reachPOIStation
	* StepId: 10
	* Type: Goal
	* TargetType: ReachPointOfInterest
	* SuccLL: 
		* t_liaison_Escort_GAMA_10
		* t_liaison_Escort_GAMA_11
		* t_liaison_Escort_GAMA_15
		* t_liaison_Escort_GAMA_16
		* t_liaison_Escort_stopShip

## t_liaison_Escort_goal_remaining
	* StepId: 13
	* Type: Goal
	* TargetType: WaveFinished
	* SuccLL: t_liaison_Escort_GAMA_13

## t_liaison_Escort_i_Allies
	* StepId: 19
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* t_liaison_Escort_GAMA_19
		* t_liaison_Escort_GAMA_20
		* t_liaison_Escort_GAMA_25

## t_liaison_Escort_i_AllySpawns
	* StepId: 20
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* t_liaison_Escort_spawn_escort
		* t_liaison_Escort_spawn_platform1
		* t_liaison_Escort_spawn_platform2
		* t_liaison_Escort_spawn_platform3
		* t_liaison_Escort_spawn_platform4
		* t_liaison_Escort_spawn_platform5
		* t_liaison_Escort_spawn_station

## t_liaison_Escort_i_Intro
	* StepId: 27
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* t_liaison_Escort_GAMA_27
		* t_liaison_Escort_GAMA_28

## t_liaison_Escort_i2
	* StepId: 2
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* t_liaison_Escort_GAMA_2
		* t_liaison_Escort_GAMA_4
		* t_liaison_Escort_GAMA_6
		* t_liaison_Escort_GAMA_9

## t_liaison_Escort_killAlly0
	* StepId: 21
	* Type: Trigger
	* TargetType: KillSpecificWave
	* SuccLL: 
		* t_liaison_Escort_GAMA_21
		* t_liaison_Escort_GAMA_22
		* t_liaison_Escort_GAMA_23
		* t_liaison_Escort_deactivateGoal

## t_liaison_Escort_multi_fail
	* StepId: 22
	* Type: None
	* TargetType: FinishGoalsString
	* TVS: 
		* t_liaison_Escort_td_fail
		* t_liaison_Escort_wait_fail
	* SuccLL: t_liaison_Escort_fail

## t_liaison_Escort_reachPOIPath1
	* StepId: 3
	* Type: Trigger
	* TargetType: ReachPointOfInterest
	* SuccLL: 
		* t_liaison_Escort_GAMA_3
		* t_liaison_Escort_wave0

## t_liaison_Escort_reachPOIPath2
	* StepId: 5
	* Type: Trigger
	* TargetType: ReachPointOfInterest
	* SuccLL: 
		* t_liaison_Escort_GAMA_5
		* t_liaison_Escort_wave1

## t_liaison_Escort_reachPOIPath3
	* StepId: 7
	* Type: Trigger
	* TargetType: ReachPointOfInterest
	* SuccLL: 
		* t_liaison_Escort_GAMA_7
		* t_liaison_Escort_wave2

## t_liaison_Escort_remainingCheck
	* StepId: 12
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* t_liaison_Escort_remainingCheckA
		* t_liaison_Escort_remainingCheckB
	* SuccLL: 
		* t_liaison_Escort_GAMA_12
		* t_liaison_Escort_GAMA_14
		* t_liaison_Escort_aiBehavior_FollowFlagship
		* t_liaison_Escort_d_remaining
		* t_liaison_Escort_deactivate

## t_liaison_Escort_remainingCheckA
	* StepId: 16
	* Type: Trigger
	* TargetType: UnitWithTagsExists

## t_liaison_Escort_remainingCheckB
	* StepId: 17
	* Type: Trigger
	* TargetType: UnitWithTagsExists

## t_liaison_Escort_repeatingKillAllCheck
	* StepId: 18
	* Type: TriggerRepeating
	* TargetType: WaveFinished
	* SuccLL: t_liaison_Escort_d_killAll

## t_liaison_Escort_start
	* StepId: 0
	* Type: Trigger
	* TargetType: MissionStart
	* SuccLL: 
		* t_liaison_Escort_GAMA_0
		* t_liaison_Escort_GAMA_1
		* t_liaison_Escort_GAMA_17
		* t_liaison_Escort_GAMA_18
		* t_liaison_Escort_GAMA_26
		* t_liaison_Escort_loot_0
		* t_liaison_Escort_loot_1

## t_liaison_Escort_td_fail
	* StepId: 23
	* Type: Trigger
	* TargetType: OnDialogFinishedIndex

## t_liaison_Escort_td_intro1
	* StepId: 31
	* Type: Trigger
	* TargetType: OnDialogFinishedIndex

## t_liaison_Escort_td_win_fac
	* StepId: 1
	* Type: Trigger
	* TargetType: OnDialogFinishedIndex
	* SuccLL: t_liaison_Escort_win

## t_liaison_Escort_w_quickPath
	* StepId: 11
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* t_liaison_Escort_d_win_fac
		* t_liaison_Escort_lookAt_fin2

## t_liaison_Escort_w_wave0
	* StepId: 4
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: t_liaison_Escort_d_hostiles0

## t_liaison_Escort_w_wave1
	* StepId: 6
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: t_liaison_Escort_d_hostiles1

## t_liaison_Escort_w_wave2
	* StepId: 8
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: t_liaison_Escort_GAMA_8

## t_liaison_Escort_w2
	* StepId: 14
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* t_liaison_Escort_d_win3
		* t_liaison_Escort_lookAt_fin

## t_liaison_Escort_wait_fail
	* StepId: 25
	* Type: Trigger
	* TargetType: WaitForTime

## t_liaison_Escort_wait1
	* StepId: 29
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* t_liaison_Escort_GAMA_29
		* t_liaison_Escort_GAMA_30
		* t_liaison_Escort_d_intro1

## t_liaison_Escort_wait5
	* StepId: 24
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* t_liaison_Escort_GAMA_24
		* t_liaison_Escort_d_fail

## t_liaison_Escort_wait6
	* StepId: 30
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: t_liaison_Escort_setActive

## t_liaison_Escort_wait7
	* StepId: 28
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* t_liaison_Escort_deactivate_Ally
		* t_liaison_Escort_lookAt_escort
		* t_liaison_Escort_preferredTarget

## t_liaison_LostCargo_attackNPC
	* StepId: 15
	* Type: Trigger
	* TargetType: OnPlayerAttackNPC
	* SuccLL: t_liaison_LostCargo_ai_FollowFlagship

## t_liaison_LostCargo_goal_killAll
	* StepId: 12
	* Type: Goal
	* TargetType: KillWaves

## t_liaison_LostCargo_goal_pickupAll
	* StepId: 10
	* Type: Goal
	* TargetType: FinishGoalsString
	* TVS: 
		* t_liaison_LostCargo_pickup0
		* t_liaison_LostCargo_pickup1
		* t_liaison_LostCargo_pickup2
		* t_liaison_LostCargo_pickup3

## t_liaison_LostCargo_i_pickups
	* StepId: 5
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* t_liaison_LostCargo_GAMA_10
		* t_liaison_LostCargo_GAMA_5
		* t_liaison_LostCargo_GAMA_6
		* t_liaison_LostCargo_GAMA_7
		* t_liaison_LostCargo_GAMA_8
		* t_liaison_LostCargo_GAMA_9

## t_liaison_LostCargo_i_spawning
	* StepId: 4
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* t_liaison_LostCargo_object0
		* t_liaison_LostCargo_object1
		* t_liaison_LostCargo_object3
		* t_liaison_LostCargo_object4
		* t_liaison_LostCargo_wave0

## t_liaison_LostCargo_killTrigger_PCG
	* StepId: 3
	* Type: Trigger
	* TargetType: KillSpecificWave

## t_liaison_LostCargo_multi_pickup1
	* StepId: 11
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* t_liaison_LostCargo_pickup0
		* t_liaison_LostCargo_pickup1
		* t_liaison_LostCargo_pickup2
		* t_liaison_LostCargo_pickup3
	* SuccLL: 
		* t_liaison_LostCargo_GAMA_11
		* t_liaison_LostCargo_ai_FollowFlagship2
		* t_liaison_LostCargo_d_wave1
		* t_liaison_LostCargo_wave1

## t_liaison_LostCargo_multi_pickupAllAndKillAll
	* StepId: 2
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* t_liaison_LostCargo_goal_killAll
		* t_liaison_LostCargo_goal_pickupAll
	* SuccLL: t_liaison_LostCargo_d_fin

## t_liaison_LostCargo_pickup0
	* StepId: 6
	* Type: Trigger
	* TargetType: OnInteractionDoneGeneric

## t_liaison_LostCargo_pickup1
	* StepId: 7
	* Type: Trigger
	* TargetType: OnInteractionDoneGeneric

## t_liaison_LostCargo_pickup2
	* StepId: 8
	* Type: Trigger
	* TargetType: OnInteractionDoneGeneric

## t_liaison_LostCargo_pickup3
	* StepId: 9
	* Type: Trigger
	* TargetType: OnInteractionDoneGeneric

## t_liaison_LostCargo_start
	* StepId: 0
	* Type: Trigger
	* TargetType: MissionStart
	* SuccLL: 
		* t_liaison_LostCargo_GAMA_0
		* t_liaison_LostCargo_GAMA_1
		* t_liaison_LostCargo_GAMA_12
		* t_liaison_LostCargo_GAMA_14
		* t_liaison_LostCargo_GAMA_2
		* t_liaison_LostCargo_GAMA_3
		* t_liaison_LostCargo_GAMA_4

## t_liaison_LostCargo_td_fin
	* StepId: 1
	* Type: Trigger
	* TargetType: OnDialogFinishedIndex
	* SuccLL: t_liaison_LostCargo_fin

## t_liaison_LostCargo_w_intro
	* StepId: 13
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* t_liaison_LostCargo_GAMA_13
		* t_liaison_LostCargo_lookAt_pickups

## t_liaison_LostCargo_w_intro2
	* StepId: 14
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: t_liaison_LostCargo_d_intro

## t_liaison_PlatformDefense_epic_goal_finishGoalString_killDefinedWaves
	* StepId: 2
	* Type: Goal
	* TargetType: FinishGoalsString
	* TVS: t_liaison_PlatformDefense_epic_trigg_finishGoalStrings_killAllWaves
	* SuccLL: 
		* t_liaison_PlatformDefense_epic_GAMA_2
		* t_liaison_PlatformDefense_epic_actn_spawnAlliedWave4

## t_liaison_PlatformDefense_epic_Start
	* StepId: 0
	* Type: Trigger
	* TargetType: MissionStart
	* SuccLL: 
		* t_liaison_PlatformDefense_epic_GAMA_0
		* t_liaison_PlatformDefense_epic_GAMA_1
		* t_liaison_PlatformDefense_epic_GAMA_3
		* t_liaison_PlatformDefense_epic_GAMA_4
		* t_liaison_PlatformDefense_epic_actn_addMissionSteps0
		* t_liaison_PlatformDefense_epic_actn_addMissionSteps1
		* t_liaison_PlatformDefense_epic_actn_addMissionSteps2
		* t_liaison_PlatformDefense_epic_actn_spawnAlliedWave0
		* t_liaison_PlatformDefense_epic_actn_spawnAlliedWave1
		* t_liaison_PlatformDefense_epic_actn_spawnAlliedWave2
		* t_liaison_PlatformDefense_epic_actn_startGenericInteraction0
		* t_liaison_PlatformDefense_epic_actn_startGenericInteraction1
		* t_liaison_PlatformDefense_epic_actn_startGenericInteraction2
		* t_liaison_PlatformDefense_epic_actn_triggerWave0

## t_liaison_PlatformDefense_epic_trigg_finishGoalString_allPlatformsKilled
	* StepId: 18
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* t_liaison_PlatformDefense_epic_trigg_onTaggedUnitKilled_Ally1
		* t_liaison_PlatformDefense_epic_trigg_onTaggedUnitKilled_Ally2
		* t_liaison_PlatformDefense_epic_trigg_onTaggedUnitKilled_Ally3
	* SuccLL: 
		* t_liaison_PlatformDefense_epic_GAMA_8
		* t_liaison_PlatformDefense_epic_actn_DestroyRemainingPlatforms01
		* t_liaison_PlatformDefense_epic_actn_DestroyRemainingPlatforms02
		* t_liaison_PlatformDefense_epic_actn_DestroyRemainingPlatforms03
		* t_liaison_PlatformDefense_epic_actn_triggerDialogIndex_fail

## t_liaison_PlatformDefense_epic_trigg_finishGoalStrings_killAllWaves
	* StepId: 4
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* t_liaison_PlatformDefense_epic_trigg_KillDefinedWaves0
		* t_liaison_PlatformDefense_epic_trigg_KillDefinedWaves1
		* t_liaison_PlatformDefense_epic_trigg_KillDefinedWaves2

## t_liaison_PlatformDefense_epic_trigg_KillDefinedWaves0
	* StepId: 5
	* Type: Trigger
	* TargetType: KillSpecificWave

## t_liaison_PlatformDefense_epic_trigg_KillDefinedWaves1
	* StepId: 6
	* Type: Trigger
	* TargetType: KillSpecificWave

## t_liaison_PlatformDefense_epic_trigg_KillDefinedWaves2
	* StepId: 7
	* Type: Trigger
	* TargetType: KillSpecificWave

## t_liaison_PlatformDefense_epic_trigg_onDialogFinishedIndex_fail
	* StepId: 19
	* Type: Trigger
	* TargetType: OnDialogFinishedIndex
	* SuccLL: t_liaison_PlatformDefense_epic_actn_finishMissionFailure

## t_liaison_PlatformDefense_epic_trigg_onDialogIndexFinished_victory
	* StepId: 1
	* Type: Trigger
	* TargetType: OnDialogFinishedIndex
	* SuccLL: t_liaison_PlatformDefense_epic_actn_finishMissionSuccess

## t_liaison_PlatformDefense_epic_trigg_onGroupBelowStrength01
	* StepId: 10
	* Type: Trigger
	* TargetType: TaggedUnitsBelowStrength
	* SuccLL: 
		* t_liaison_PlatformDefense_epic_GAMA_6
		* t_liaison_PlatformDefense_epic_actn_triggerWave1
		* t_liaison_PlatformDefense_epic_atcn_triggerDialogIndex_nextwave1

## t_liaison_PlatformDefense_epic_trigg_onGroupBelowStrength02
	* StepId: 11
	* Type: Trigger
	* TargetType: TaggedUnitsBelowStrength
	* SuccLL: 
		* t_liaison_PlatformDefense_epic_GAMA_7
		* t_liaison_PlatformDefense_epic_actn_triggerWave2
		* t_liaison_PlatformDefense_epic_atcn_triggerDialogIndex_nextwave2

## t_liaison_PlatformDefense_epic_trigg_onGroupBelowStrength03
	* StepId: 12
	* Type: Trigger
	* TargetType: TaggedUnitsBelowStrength
	* SuccLL: 
		* t_liaison_PlatformDefense_epic_actn_spawnAlliedWave3
		* t_liaison_PlatformDefense_epic_atcn_triggerDialogIndex_previctory

## t_liaison_PlatformDefense_epic_trigg_onTaggedUnitKilled_Ally1
	* StepId: 15
	* Type: Trigger
	* TargetType: OnTaggedUnitKilled

## t_liaison_PlatformDefense_epic_trigg_onTaggedUnitKilled_Ally2
	* StepId: 16
	* Type: Trigger
	* TargetType: OnTaggedUnitKilled

## t_liaison_PlatformDefense_epic_trigg_onTaggedUnitKilled_Ally3
	* StepId: 17
	* Type: Trigger
	* TargetType: OnTaggedUnitKilled

## t_liaison_PlatformDefense_epic_trigg_waitForTime_cameraMoveRequest
	* StepId: 13
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: t_liaison_PlatformDefense_epic_lookAt_platforms

## t_liaison_PlatformDefense_epic_trigg_WaitForTime_MissionSetup
	* StepId: 9
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: t_liaison_PlatformDefense_epic_GAMA_5

## t_liaison_PlatformDefense_epic_trigg_WaitForTime_platformSetup
	* StepId: 8
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* t_liaison_PlatformDefense_epic_actn_setTaggedUnitHealthAlly1
		* t_liaison_PlatformDefense_epic_actn_setTaggedUnitHealthAlly2
		* t_liaison_PlatformDefense_epic_actn_setTaggedUnitHealthAlly3

## t_liaison_PlatformDefense_epic_trigg_waitForTime_triggerDialog
	* StepId: 14
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: t_liaison_PlatformDefense_epic_actn_triggerDialogIndex_start

## t_liaison_PlatformDefense_epic_trigg_WaitForTime_Victory
	* StepId: 3
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: t_liaison_PlatformDefense_epic_atcn_triggerDialogIndex_victory

## t_liaison_PlatformDefense_goal_finishGoalString_killDefinedWaves
	* StepId: 2
	* Type: Goal
	* TargetType: FinishGoalsString
	* TVS: t_liaison_PlatformDefense_trigg_finishGoalStrings_killAllWaves
	* SuccLL: 
		* t_liaison_PlatformDefense_GAMA_2
		* t_liaison_PlatformDefense_actn_spawnAlliedWave4

## t_liaison_PlatformDefense_Start
	* StepId: 0
	* Type: Trigger
	* TargetType: MissionStart
	* SuccLL: 
		* t_liaison_PlatformDefense_GAMA_0
		* t_liaison_PlatformDefense_GAMA_1
		* t_liaison_PlatformDefense_GAMA_3
		* t_liaison_PlatformDefense_GAMA_4
		* t_liaison_PlatformDefense_actn_addMissionSteps0
		* t_liaison_PlatformDefense_actn_addMissionSteps1
		* t_liaison_PlatformDefense_actn_addMissionSteps2
		* t_liaison_PlatformDefense_actn_spawnAlliedWave0
		* t_liaison_PlatformDefense_actn_spawnAlliedWave1
		* t_liaison_PlatformDefense_actn_spawnAlliedWave2
		* t_liaison_PlatformDefense_actn_startGenericInteraction0
		* t_liaison_PlatformDefense_actn_startGenericInteraction1
		* t_liaison_PlatformDefense_actn_startGenericInteraction2
		* t_liaison_PlatformDefense_actn_triggerWave0

## t_liaison_PlatformDefense_trigg_finishGoalString_allPlatformsKilled
	* StepId: 18
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* t_liaison_PlatformDefense_trigg_onTaggedUnitKilled_Ally1
		* t_liaison_PlatformDefense_trigg_onTaggedUnitKilled_Ally2
		* t_liaison_PlatformDefense_trigg_onTaggedUnitKilled_Ally3
	* SuccLL: 
		* t_liaison_PlatformDefense_GAMA_8
		* t_liaison_PlatformDefense_actn_triggerDialogIndex_fail

## t_liaison_PlatformDefense_trigg_finishGoalStrings_killAllWaves
	* StepId: 4
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* t_liaison_PlatformDefense_trigg_KillDefinedWaves0
		* t_liaison_PlatformDefense_trigg_KillDefinedWaves1
		* t_liaison_PlatformDefense_trigg_KillDefinedWaves2

## t_liaison_PlatformDefense_trigg_KillDefinedWaves0
	* StepId: 5
	* Type: Trigger
	* TargetType: KillSpecificWave

## t_liaison_PlatformDefense_trigg_KillDefinedWaves1
	* StepId: 6
	* Type: Trigger
	* TargetType: KillSpecificWave

## t_liaison_PlatformDefense_trigg_KillDefinedWaves2
	* StepId: 7
	* Type: Trigger
	* TargetType: KillSpecificWave

## t_liaison_PlatformDefense_trigg_onDialogFinishedIndex_fail
	* StepId: 19
	* Type: Trigger
	* TargetType: OnDialogFinishedIndex
	* SuccLL: t_liaison_PlatformDefense_actn_finishMissionFailure

## t_liaison_PlatformDefense_trigg_onDialogIndexFinished_victory
	* StepId: 1
	* Type: Trigger
	* TargetType: OnDialogFinishedIndex
	* SuccLL: t_liaison_PlatformDefense_actn_finishMissionSuccess

## t_liaison_PlatformDefense_trigg_onGroupBelowStrength01
	* StepId: 10
	* Type: Trigger
	* TargetType: TaggedUnitsBelowStrength
	* SuccLL: 
		* t_liaison_PlatformDefense_GAMA_6
		* t_liaison_PlatformDefense_actn_triggerWave1
		* t_liaison_PlatformDefense_atcn_triggerDialogIndex_nextwave1

## t_liaison_PlatformDefense_trigg_onGroupBelowStrength02
	* StepId: 11
	* Type: Trigger
	* TargetType: TaggedUnitsBelowStrength
	* SuccLL: 
		* t_liaison_PlatformDefense_GAMA_7
		* t_liaison_PlatformDefense_actn_triggerWave2
		* t_liaison_PlatformDefense_atcn_triggerDialogIndex_nextwave2

## t_liaison_PlatformDefense_trigg_onGroupBelowStrength03
	* StepId: 12
	* Type: Trigger
	* TargetType: TaggedUnitsBelowStrength
	* SuccLL: 
		* t_liaison_PlatformDefense_actn_spawnAlliedWave3
		* t_liaison_PlatformDefense_atcn_triggerDialogIndex_previctory

## t_liaison_PlatformDefense_trigg_onTaggedUnitKilled_Ally1
	* StepId: 15
	* Type: Trigger
	* TargetType: OnTaggedUnitKilled

## t_liaison_PlatformDefense_trigg_onTaggedUnitKilled_Ally2
	* StepId: 16
	* Type: Trigger
	* TargetType: OnTaggedUnitKilled

## t_liaison_PlatformDefense_trigg_onTaggedUnitKilled_Ally3
	* StepId: 17
	* Type: Trigger
	* TargetType: OnTaggedUnitKilled

## t_liaison_PlatformDefense_trigg_waitForTime_cameraMoveRequest
	* StepId: 13
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: t_liaison_PlatformDefense_lookAt_platforms

## t_liaison_PlatformDefense_trigg_WaitForTime_MissionSetup
	* StepId: 9
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: t_liaison_PlatformDefense_GAMA_5

## t_liaison_PlatformDefense_trigg_WaitForTime_platformSetup
	* StepId: 8
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* t_liaison_PlatformDefense_actn_setTaggedUnitHealthAlly1
		* t_liaison_PlatformDefense_actn_setTaggedUnitHealthAlly2
		* t_liaison_PlatformDefense_actn_setTaggedUnitHealthAlly3

## t_liaison_PlatformDefense_trigg_waitForTime_triggerDialog
	* StepId: 14
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: t_liaison_PlatformDefense_actn_triggerDialogIndex_start

## t_liaison_PlatformDefense_trigg_WaitForTime_Victory
	* StepId: 3
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: t_liaison_PlatformDefense_atcn_triggerDialogIndex_victory

## t_liaison_Spearhead_ally_death
	* StepId: 1
	* Type: Trigger
	* TargetType: OnTaggedUnitKilled
	* SuccLL: t_liaison_Spearhead_ally_death_fail

## t_liaison_Spearhead_ally_speech_finished
	* StepId: 5
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: MAKE_SPEECH

## t_liaison_Spearhead_Defeat_enemy
	* StepId: 2
	* Type: Goal
	* TargetType: KillSpecificWave
	* SuccLL: t_liaison_Spearhead_Mission_success

## t_liaison_Spearhead_detect_player_attack
	* StepId: 3
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* t_liaison_Spearhead_ally_speech_finished
		* t_liaison_Spearhead_player_attacked
	* SuccLL: 
		* t_liaison_Spearhead_activate_friendlies
		* t_liaison_Spearhead_launch_attack_dia

## t_liaison_Spearhead_group_with_ally
	* StepId: 4
	* Type: Goal
	* TargetType: ReachPosition
	* TVS: 
		* -12500
		* 0
	* SuccLL: 
		* t_liaison_Spearhead_GAMA_4
		* t_liaison_Spearhead_attack_speech

## t_liaison_Spearhead_player_attacked
	* StepId: 6
	* Type: Trigger
	* TargetType: ReachPosition
	* TVS: 
		* 0
		* 31100

## t_liaison_Spearhead_spearhead_start
	* StepId: 0
	* Type: Trigger
	* TargetType: MissionStart
	* SuccLL: 
		* t_liaison_Spearhead_GAMA_0
		* t_liaison_Spearhead_GAMA_1
		* t_liaison_Spearhead_GAMA_2
		* t_liaison_Spearhead_GAMA_3
		* t_liaison_Spearhead_GAMA_5
		* t_liaison_Spearhead_deactivate_friendlies
		* t_liaison_Spearhead_spawn_allies
		* t_liaison_Spearhead_spawn_enemy

## t_outpost_start
	* StepId: 0
	* Type: Trigger
	* TargetType: MissionStart
	* SuccLL: 
		* t_outpost_GAMA_0
		* t_outpost_GAMA_2
		* t_outpost_act_triggerWave1
		* t_outpost_act_triggerWave2

## t_outpost_t_waitForTimeRepair1
	* StepId: 3
	* Type: TriggerRepeating
	* TargetType: WaitForTime
	* SuccLL: 
		* t_outpost_act_HealPlayer2
		* t_outpost_act_HealPlayer3
		* t_outpost_act_HealPlayer4
		* t_outpost_act_HealPlayer5
		* t_outpost_act_HealPlayer6

## t_outpost_w_waitForTime1
	* StepId: 1
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* t_outpost_GAMA_1
		* t_outpost_act_triggerWave3

## t_outpost_w_waitForTime2
	* StepId: 2
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: t_outpost_act_triggerWave4

## t_pme_RandomEventAttack_StartPME
	* StepId: 0
	* Type: None
	* TargetType: MissionStart
	* SuccLL: 
		* t_pme_RandomEventAttack_GAMA_0
		* t_pme_RandomEventAttack_GAMA_1
		* t_pme_RandomEventAttack_GAMA_2
		* t_pme_RandomEventAttack_TriggerDialoge
		* t_pme_RandomEventAttack_TriggerWave00

## t_pme_RandomEventAttack_Trigger_KillWave00
	* StepId: 3
	* Type: Trigger
	* TargetType: KillSpecificWave

## t_pme_RandomEventAttack_TriggerCheckForEndConditions
	* StepId: 1
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* t_pme_RandomEventAttack_TriggerWaitForTime
		* t_pme_RandomEventAttack_Trigger_KillWave00
	* SuccLL: t_pme_RandomEventAttack_FinishPME

## t_pme_RandomEventAttack_TriggerWaitForTime
	* StepId: 2
	* Type: Trigger
	* TargetType: WaitForTime

## t_signal_AlienProbe_exist_wave1
	* StepId: 11
	* Type: Trigger
	* TargetType: UnitWithTagsExists
	* SuccLL: 
		* t_signal_AlienProbe_GAMA_11
		* t_signal_AlienProbe_d_wave1
	* FailLL: t_signal_AlienProbe_GAMA_14

## t_signal_AlienProbe_exist_wave2
	* StepId: 14
	* Type: Trigger
	* TargetType: UnitWithTagsExists
	* SuccLL: t_signal_AlienProbe_d_wave2

## t_signal_AlienProbe_goal_collectProbe
	* StepId: 5
	* Type: Goal
	* TargetType: OnInteractionDoneGeneric
	* SuccLL: t_signal_AlienProbe_GAMA_5

## t_signal_AlienProbe_i_gameplay
	* StepId: 4
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* t_signal_AlienProbe_GAMA_4
		* t_signal_AlienProbe_GAMA_6
		* t_signal_AlienProbe_GAMA_7

## t_signal_AlienProbe_i_setup
	* StepId: 2
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* t_signal_AlienProbe_GAMA_2
		* t_signal_AlienProbe_spawn_probe
		* t_signal_AlienProbe_wave_patrol

## t_signal_AlienProbe_killTrigger
	* StepId: 3
	* Type: Trigger
	* TargetType: WaveFinished

## t_signal_AlienProbe_position_collect
	* StepId: 8
	* Type: Trigger
	* TargetType: ReachPointOfInterest
	* SuccLL: t_signal_AlienProbe_GAMA_8

## t_signal_AlienProbe_position_combat
	* StepId: 7
	* Type: Trigger
	* TargetType: ReachPointOfInterest
	* SuccLL: t_signal_AlienProbe_aiBehavior

## t_signal_AlienProbe_start
	* StepId: 0
	* Type: Trigger
	* TargetType: MissionStart
	* SuccLL: 
		* t_signal_AlienProbe_GAMA_0
		* t_signal_AlienProbe_GAMA_1
		* t_signal_AlienProbe_GAMA_16
		* t_signal_AlienProbe_GAMA_3

## t_signal_AlienProbe_td_fin
	* StepId: 1
	* Type: Trigger
	* TargetType: OnDialogFinishedIndex
	* SuccLL: t_signal_AlienProbe_fin

## t_signal_AlienProbe_w_boss
	* StepId: 15
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* t_signal_AlienProbe_GAMA_15
		* t_signal_AlienProbe_wave_boss

## t_signal_AlienProbe_w_bossDialog
	* StepId: 16
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: t_signal_AlienProbe_d_boss

## t_signal_AlienProbe_w_fin
	* StepId: 6
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: t_signal_AlienProbe_d_fin

## t_signal_AlienProbe_w_intro
	* StepId: 17
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* t_signal_AlienProbe_GAMA_17
		* t_signal_AlienProbe_look_probe

## t_signal_AlienProbe_w_intro2
	* StepId: 18
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: t_signal_AlienProbe_d_intro

## t_signal_AlienProbe_w_wave1
	* StepId: 9
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* t_signal_AlienProbe_GAMA_9
		* t_signal_AlienProbe_wave_1

## t_signal_AlienProbe_w_wave1Check
	* StepId: 10
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: t_signal_AlienProbe_GAMA_10

## t_signal_AlienProbe_w_wave2
	* StepId: 12
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* t_signal_AlienProbe_GAMA_12
		* t_signal_AlienProbe_wave_2

## t_signal_AlienProbe_w_wave2Check
	* StepId: 13
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: t_signal_AlienProbe_GAMA_13

## t_signal_AttackBase_firstAttackCheck
	* StepId: 4
	* Type: Trigger
	* TargetType: OnPlayerAttackNPC
	* SuccLL: 
		* t_signal_AttackBase_GAMA_4
		* t_signal_AttackBase_GAMA_5

## t_signal_AttackBase_goal_defeatBase
	* StepId: 2
	* Type: Goal
	* TargetType: WaveFinished
	* SuccLL: t_signal_AttackBase_GAMA_2

## t_signal_AttackBase_i_loot
	* StepId: 13
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* t_signal_AttackBase_loot0
		* t_signal_AttackBase_loot1
		* t_signal_AttackBase_loot2

## t_signal_AttackBase_i_spawn
	* StepId: 7
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* t_signal_AttackBase_key0_randomExtra
		* t_signal_AttackBase_key1_randomExtra
		* t_signal_AttackBase_key2_randomExtra
		* t_signal_AttackBase_key3_randomExtra
		* t_signal_AttackBase_key4_randomExtra
		* t_signal_AttackBase_key5_randomExtra
		* t_signal_AttackBase_wave10_platform
		* t_signal_AttackBase_wave11_platform
		* t_signal_AttackBase_wave12_platform
		* t_signal_AttackBase_wave13_platform
		* t_signal_AttackBase_wave1_station
		* t_signal_AttackBase_wave2_patrol
		* t_signal_AttackBase_wave3_patrol
		* t_signal_AttackBase_wave4_patrol
		* t_signal_AttackBase_wave5_patrol
		* t_signal_AttackBase_wave6_patrol
		* t_signal_AttackBase_wave7_platform
		* t_signal_AttackBase_wave8_platform
		* t_signal_AttackBase_wave9_platform

## t_signal_AttackBase_multi_alert
	* StepId: 5
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* t_signal_AttackBase_strengthCheckPatrol
		* t_signal_AttackBase_w_alert
	* SuccLL: 
		* t_signal_AttackBase_behavior_alert
		* t_signal_AttackBase_d_alert

## t_signal_AttackBase_start
	* StepId: 0
	* Type: Trigger
	* TargetType: MissionStart
	* SuccLL: 
		* t_signal_AttackBase_GAMA_0
		* t_signal_AttackBase_GAMA_1
		* t_signal_AttackBase_GAMA_10
		* t_signal_AttackBase_GAMA_11
		* t_signal_AttackBase_GAMA_12
		* t_signal_AttackBase_GAMA_3
		* t_signal_AttackBase_GAMA_6
		* t_signal_AttackBase_GAMA_7

## t_signal_AttackBase_strengthCheckPatrol
	* StepId: 10
	* Type: Trigger
	* TargetType: TaggedUnitsBelowStrength

## t_signal_AttackBase_strengthCheckWave
	* StepId: 9
	* Type: Trigger
	* TargetType: TaggedUnitsBelowStrength
	* SuccLL: 
		* t_signal_AttackBase_d_wave
		* t_signal_AttackBase_wave0_wave

## t_signal_AttackBase_td_win
	* StepId: 1
	* Type: Trigger
	* TargetType: OnDialogFinishedIndex
	* SuccLL: t_signal_AttackBase_fin

## t_signal_AttackBase_w_alert
	* StepId: 6
	* Type: Trigger
	* TargetType: WaitForTime

## t_signal_AttackBase_w_strengthCheckWave
	* StepId: 8
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* t_signal_AttackBase_GAMA_8
		* t_signal_AttackBase_GAMA_9

## t_signal_AttackBase_wait_win
	* StepId: 3
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: t_signal_AttackBase_d_win1

## t_signal_AttackBase_wait1
	* StepId: 12
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: t_signal_AttackBase_d_intro1

## t_signal_AttackBase_wait7
	* StepId: 11
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: t_signal_AttackBase_lookAt

## t_signal_BasicDestroy_goal_killWaves
	* StepId: 2
	* Type: Goal
	* TargetType: FinishGoalsString
	* TVS: 
		* t_signal_BasicDestroy_kill_0
		* t_signal_BasicDestroy_kill_1
	* SuccLL: t_signal_BasicDestroy_GAMA_2

## t_signal_BasicDestroy_kill_0
	* StepId: 4
	* Type: Trigger
	* TargetType: KillSpecificWave
	* SuccLL: t_signal_BasicDestroy_GAMA_4

## t_signal_BasicDestroy_kill_1
	* StepId: 7
	* Type: Trigger
	* TargetType: KillSpecificWave

## t_signal_BasicDestroy_start
	* StepId: 0
	* Type: Trigger
	* TargetType: MissionStart
	* SuccLL: 
		* t_signal_BasicDestroy_GAMA_0
		* t_signal_BasicDestroy_GAMA_1
		* t_signal_BasicDestroy_GAMA_3
		* t_signal_BasicDestroy_GAMA_6
		* t_signal_BasicDestroy_GAMA_7
		* t_signal_BasicDestroy_interaction_0
		* t_signal_BasicDestroy_interaction_1
		* t_signal_BasicDestroy_wave_0

## t_signal_BasicDestroy_t0_goal_hostiles
	* StepId: 2
	* Type: Goal
	* TargetType: WaveFinished
	* SuccLL: t_signal_BasicDestroy_t0_GAMA_2

## t_signal_BasicDestroy_t0_start
	* StepId: 0
	* Type: Trigger
	* TargetType: MissionStart
	* SuccLL: 
		* t_signal_BasicDestroy_t0_GAMA_0
		* t_signal_BasicDestroy_t0_GAMA_1
		* t_signal_BasicDestroy_t0_GAMA_3
		* t_signal_BasicDestroy_t0_GAMA_4
		* t_signal_BasicDestroy_t0_wave0

## t_signal_BasicDestroy_t0_td_win
	* StepId: 1
	* Type: Trigger
	* TargetType: OnDialogFinishedIndex
	* SuccLL: t_signal_BasicDestroy_t0_win

## t_signal_BasicDestroy_t0_w_fin
	* StepId: 3
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: t_signal_BasicDestroy_t0_d_win

## t_signal_BasicDestroy_t0_w_intro
	* StepId: 4
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: t_signal_BasicDestroy_t0_d_intro

## t_signal_BasicDestroy_t0_w_intro2
	* StepId: 5
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* t_signal_BasicDestroy_t0_GAMA_5
		* t_signal_BasicDestroy_t0_deactivate1

## t_signal_BasicDestroy_t0_w_intro3
	* StepId: 6
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: t_signal_BasicDestroy_t0_activate1

## t_signal_BasicDestroy_td_fain
	* StepId: 1
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: destroy_fin_dialog0
	* SuccLL: t_signal_BasicDestroy_fin

## t_signal_BasicDestroy_w_fin
	* StepId: 3
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: t_signal_BasicDestroy_d_fin

## t_signal_BasicDestroy_w_intro
	* StepId: 8
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: t_signal_BasicDestroy_d_intro

## t_signal_BasicDestroy_w_wave1
	* StepId: 5
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* t_signal_BasicDestroy_GAMA_5
		* t_signal_BasicDestroy_wave_1

## t_signal_BasicDestroy_w_wave1Dialog
	* StepId: 6
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: t_signal_BasicDestroy_d_wave

## t_signal_DefendBase_start
	* StepId: 0
	* Type: Trigger
	* TargetType: MissionStart

## t_signal_MiningAttack_exist_w0
	* StepId: 23
	* Type: Trigger
	* TargetType: UnitWithTagsExists
	* SuccLL: t_signal_MiningAttack_GAMA_23
	* FailLL: t_signal_MiningAttack_GAMA_24

## t_signal_MiningAttack_exist_w1
	* StepId: 27
	* Type: Trigger
	* TargetType: UnitWithTagsExists
	* SuccLL: t_signal_MiningAttack_GAMA_27
	* FailLL: t_signal_MiningAttack_GAMA_28

## t_signal_MiningAttack_exist_w2
	* StepId: 31
	* Type: Trigger
	* TargetType: UnitWithTagsExists
	* SuccLL: t_signal_MiningAttack_GAMA_31
	* FailLL: t_signal_MiningAttack_GAMA_32

## t_signal_MiningAttack_existCheck1
	* StepId: 14
	* Type: Trigger
	* TargetType: UnitWithTagsExists
	* FailLL: 
		* t_signal_MiningAttack_aiBehavior_followFlagshipRemove1
		* t_signal_MiningAttack_d_removedLastController1
		* t_signal_MiningAttack_deactivate_existCheck1

## t_signal_MiningAttack_existCheck2
	* StepId: 13
	* Type: Trigger
	* TargetType: UnitWithTagsExists
	* FailLL: 
		* t_signal_MiningAttack_aiBehavior_followFlagshipRemove2
		* t_signal_MiningAttack_d_removedLastController2
		* t_signal_MiningAttack_deactivate_flow2

## t_signal_MiningAttack_goal_clear
	* StepId: 2
	* Type: Goal
	* TargetType: WaveFinished
	* SuccLL: 
		* t_signal_MiningAttack_GAMA_2
		* t_signal_MiningAttack_GAMA_3

## t_signal_MiningAttack_i_kill
	* StepId: 21
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* t_signal_MiningAttack_GAMA_21
		* t_signal_MiningAttack_GAMA_25
		* t_signal_MiningAttack_GAMA_29

## t_signal_MiningAttack_i_killedLastController0
	* StepId: 25
	* Type: Trigger
	* TargetType: Immediate

## t_signal_MiningAttack_i_killedLastController1
	* StepId: 29
	* Type: Trigger
	* TargetType: Immediate

## t_signal_MiningAttack_i_killedLastController2
	* StepId: 33
	* Type: Trigger
	* TargetType: Immediate

## t_signal_MiningAttack_i_loot
	* StepId: 16
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* t_signal_MiningAttack_loot_0
		* t_signal_MiningAttack_loot_1

## t_signal_MiningAttack_i_spawning
	* StepId: 15
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* t_signal_MiningAttack_controller0
		* t_signal_MiningAttack_controller1
		* t_signal_MiningAttack_controller2
		* t_signal_MiningAttack_wave3
		* t_signal_MiningAttack_wave4
		* t_signal_MiningAttack_wave5

## t_signal_MiningAttack_kill_wave0
	* StepId: 22
	* Type: Trigger
	* TargetType: KillSpecificWave
	* SuccLL: t_signal_MiningAttack_GAMA_22

## t_signal_MiningAttack_kill_wave1
	* StepId: 26
	* Type: Trigger
	* TargetType: KillSpecificWave
	* SuccLL: t_signal_MiningAttack_GAMA_26

## t_signal_MiningAttack_kill_wave2
	* StepId: 30
	* Type: Trigger
	* TargetType: KillSpecificWave
	* SuccLL: t_signal_MiningAttack_GAMA_30

## t_signal_MiningAttack_multi_killedLastController
	* StepId: 5
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* t_signal_MiningAttack_i_killedLastController0
		* t_signal_MiningAttack_i_killedLastController1
		* t_signal_MiningAttack_i_killedLastController2
	* SuccLL: 
		* t_signal_MiningAttack_GAMA_5
		* t_signal_MiningAttack_aiBehavior_followFlagshipKill
		* t_signal_MiningAttack_deactivate_killDialog

## t_signal_MiningAttack_start
	* StepId: 0
	* Type: Trigger
	* TargetType: MissionStart
	* SuccLL: 
		* t_signal_MiningAttack_GAMA_0
		* t_signal_MiningAttack_GAMA_1
		* t_signal_MiningAttack_GAMA_14
		* t_signal_MiningAttack_GAMA_15
		* t_signal_MiningAttack_GAMA_16
		* t_signal_MiningAttack_GAMA_20
		* t_signal_MiningAttack_GAMA_4
		* t_signal_MiningAttack_GAMA_6

## t_signal_MiningAttack_td_fin
	* StepId: 1
	* Type: Trigger
	* TargetType: OnDialogFinishedIndex
	* SuccLL: t_signal_MiningAttack_fin

## t_signal_MiningAttack_w_controllersBuffer
	* StepId: 6
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: t_signal_MiningAttack_d_controllers

## t_signal_MiningAttack_w_deactivateControllersDialog
	* StepId: 4
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: t_signal_MiningAttack_deactivate_controllersDialog

## t_signal_MiningAttack_w_escape1
	* StepId: 7
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* t_signal_MiningAttack_GAMA_7
		* t_signal_MiningAttack_remove1

## t_signal_MiningAttack_w_escape2
	* StepId: 9
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* t_signal_MiningAttack_GAMA_9
		* t_signal_MiningAttack_remove2

## t_signal_MiningAttack_w_escape3
	* StepId: 11
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* t_signal_MiningAttack_GAMA_11
		* t_signal_MiningAttack_remove3

## t_signal_MiningAttack_w_escapeBuffer1
	* StepId: 8
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* t_signal_MiningAttack_GAMA_13
		* t_signal_MiningAttack_GAMA_8

## t_signal_MiningAttack_w_escapeBuffer2
	* StepId: 10
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* t_signal_MiningAttack_GAMA_10
		* t_signal_MiningAttack_GAMA_12

## t_signal_MiningAttack_w_escapeBuffer3
	* StepId: 12
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* t_signal_MiningAttack_aiBehavior_followFlagshipRemove3
		* t_signal_MiningAttack_d_removedLastController3

## t_signal_MiningAttack_w_intro1
	* StepId: 17
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* t_signal_MiningAttack_GAMA_17
		* t_signal_MiningAttack_deactivate_controllers
		* t_signal_MiningAttack_deactivate_enemy
		* t_signal_MiningAttack_lookAt_intro

## t_signal_MiningAttack_w_intro2
	* StepId: 18
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* t_signal_MiningAttack_GAMA_18
		* t_signal_MiningAttack_GAMA_19
		* t_signal_MiningAttack_d_intro

## t_signal_MiningAttack_w_intro3
	* StepId: 19
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: t_signal_MiningAttack_activate_controllers

## t_signal_MiningAttack_w_intro4
	* StepId: 20
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: t_signal_MiningAttack_activate_enemies

## t_signal_MiningAttack_w_killController0
	* StepId: 24
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: t_signal_MiningAttack_d_killController0

## t_signal_MiningAttack_w_killController1
	* StepId: 28
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: t_signal_MiningAttack_d_killController1

## t_signal_MiningAttack_w_killController2
	* StepId: 32
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: t_signal_MiningAttack_d_killController2

## t_signal_MiningAttack_w_win
	* StepId: 3
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: t_signal_MiningAttack_d_win

## t_signal_ProgenitorActivities_goal_FinishGoalString_FinishWaves
	* StepId: 14
	* Type: Goal
	* TargetType: FinishGoalsString
	* TVS: t_signal_ProgenitorActivities_trigg_finishedGoalString_FinishWaves

## t_signal_ProgenitorActivities_goal_killSpecificWave0_DestroyDerelict
	* StepId: 12
	* Type: Goal
	* TargetType: KillSpecificWave
	* SuccLL: 
		* t_signal_ProgenitorActivities_GAMA_12
		* t_signal_ProgenitorActivities_actn_triggerDialog_destroyed
		* t_signal_ProgenitorActivities_succeed_Countdown

## t_signal_ProgenitorActivities_goal_waitForTime_FailMission
	* StepId: 16
	* Type: Goal
	* TargetType: Countdown
	* FailLL: 
		* t_signal_ProgenitorActivities_GAMA_16
		* t_signal_ProgenitorActivities_actn_deactiveSteps_DestroyDerelict
		* t_signal_ProgenitorActivities_actn_triggerDialog_fail
		* t_signal_ProgenitorActivities_actn_triggerWave3

## t_signal_ProgenitorActivities_i_derelictChecks
	* StepId: 11
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* t_signal_ProgenitorActivities_GAMA_11
		* t_signal_ProgenitorActivities_GAMA_14
		* t_signal_ProgenitorActivities_GAMA_17

## t_signal_ProgenitorActivities_i_goals
	* StepId: 2
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* t_signal_ProgenitorActivities_GAMA_2
		* t_signal_ProgenitorActivities_GAMA_3
		* t_signal_ProgenitorActivities_GAMA_4
		* t_signal_ProgenitorActivities_GAMA_5

## t_signal_ProgenitorActivities_i_intro
	* StepId: 8
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* t_signal_ProgenitorActivities_GAMA_8
		* t_signal_ProgenitorActivities_GAMA_9

## t_signal_ProgenitorActivities_i_setup
	* StepId: 7
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* t_signal_ProgenitorActivities_actn_startGenericInteraction0
		* t_signal_ProgenitorActivities_actn_startGenericInteraction1
		* t_signal_ProgenitorActivities_invincible_derelict1
		* t_signal_ProgenitorActivities_wave0_derelict
		* t_signal_ProgenitorActivities_wave1

## t_signal_ProgenitorActivities_start
	* StepId: 0
	* Type: Trigger
	* TargetType: MissionStart
	* SuccLL: 
		* t_signal_ProgenitorActivities_GAMA_0
		* t_signal_ProgenitorActivities_GAMA_1
		* t_signal_ProgenitorActivities_GAMA_10
		* t_signal_ProgenitorActivities_GAMA_6
		* t_signal_ProgenitorActivities_GAMA_7

## t_signal_ProgenitorActivities_trig_WavesAlive
	* StepId: 13
	* Type: Trigger
	* TargetType: UnitWithTagsExists
	* SuccLL: t_signal_ProgenitorActivities_GAMA_13

## t_signal_ProgenitorActivities_trigg_finishedGoalString_FinishWaves
	* StepId: 4
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* t_signal_ProgenitorActivities_trigg_killSpecificWave1
		* t_signal_ProgenitorActivities_trigg_killSpecificWave2

## t_signal_ProgenitorActivities_trigg_killSpecificWave1
	* StepId: 5
	* Type: Trigger
	* TargetType: KillSpecificWave

## t_signal_ProgenitorActivities_trigg_killSpecificWave2
	* StepId: 6
	* Type: Trigger
	* TargetType: KillSpecificWave

## t_signal_ProgenitorActivities_trigg_onDialogFinished_victory
	* StepId: 1
	* Type: Trigger
	* TargetType: OnDialogFinished
	* TVS: progenitorActivities_victory_dialog0
	* SuccLL: t_signal_ProgenitorActivities_actn_finishMissionSuccess

## t_signal_ProgenitorActivities_trigg_OnUnitBelowHealth45
	* StepId: 18
	* Type: Trigger
	* TargetType: OnTaggedUnitIsBelowHealth
	* SuccLL: 
		* t_signal_ProgenitorActivities_actn_triggerDialog_nextwave
		* t_signal_ProgenitorActivities_actn_triggerWave2
		* t_signal_ProgenitorActivities_invincible_derelict3

## t_signal_ProgenitorActivities_trigg_OnUnitBelowHealth90
	* StepId: 15
	* Type: Trigger
	* TargetType: OnTaggedUnitIsBelowHealth
	* SuccLL: 
		* t_signal_ProgenitorActivities_GAMA_15
		* t_signal_ProgenitorActivities_actn_changeNPCAI_FollowFlagship
		* t_signal_ProgenitorActivities_actn_triggerDialog_powerUp
		* t_signal_ProgenitorActivities_invincible_derelict2

## t_signal_ProgenitorActivities_trigg_waitForTime_MissionFail
	* StepId: 17
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: t_signal_ProgenitorActivities_actn_FinishMissionFail

## t_signal_ProgenitorActivities_trigger_finishGoals_DestroyDerelictAndWaves
	* StepId: 3
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* t_signal_ProgenitorActivities_goal_killSpecificWave0_DestroyDerelict
		* t_signal_ProgenitorActivities_trigg_finishedGoalString_FinishWaves
	* SuccLL: t_signal_ProgenitorActivities_actn_triggerDialog_victory

## t_signal_ProgenitorActivities_w_introDialog
	* StepId: 10
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: t_signal_ProgenitorActivities_actn_triggerDialog_start

## t_signal_ProgenitorActivities_w_introLookAt
	* StepId: 9
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: t_signal_ProgenitorActivities_lookAt_derelict

## t_signal_Relic_goal_collectRelic
	* StepId: 3
	* Type: Goal
	* TargetType: OnInteractionDoneGeneric
	* SuccLL: t_signal_Relic_GAMA_3

## t_signal_Relic_goal_position
	* StepId: 2
	* Type: Goal
	* TargetType: ReachPointOfInterest
	* SuccLL: 
		* t_signal_Relic_GAMA_2
		* t_signal_Relic_GAMA_4
		* t_signal_Relic_aiBehavior
		* t_signal_Relic_d_position
		* t_signal_Relic_spawnRelic

## t_signal_Relic_i_spawning
	* StepId: 8
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* t_signal_Relic_GAMA_8
		* t_signal_Relic_prop_ship
		* t_signal_Relic_wave0

## t_signal_Relic_killTrigger
	* StepId: 9
	* Type: Trigger
	* TargetType: WaveFinished

## t_signal_Relic_spawnCheck
	* StepId: 7
	* Type: Trigger
	* TargetType: UnitWithTagsExists
	* SuccLL: t_signal_Relic_d_wave

## t_signal_Relic_start
	* StepId: 0
	* Type: Trigger
	* TargetType: MissionStart
	* SuccLL: 
		* t_signal_Relic_GAMA_0
		* t_signal_Relic_GAMA_1
		* t_signal_Relic_GAMA_7
		* t_signal_Relic_GAMA_9

## t_signal_Relic_td_fin
	* StepId: 1
	* Type: Trigger
	* TargetType: OnDialogFinishedIndex
	* SuccLL: t_signal_Relic_fin

## t_signal_Relic_w_fin
	* StepId: 4
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: t_signal_Relic_d_fin

## t_signal_Relic_w_intro
	* StepId: 10
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* t_signal_Relic_GAMA_10
		* t_signal_Relic_look_relic

## t_signal_Relic_w_intro2
	* StepId: 11
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: t_signal_Relic_d_start

## t_signal_Relic_w_secondWave
	* StepId: 5
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* t_signal_Relic_GAMA_5
		* t_signal_Relic_wave1

## t_signal_Relic_w_wave
	* StepId: 6
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: t_signal_Relic_GAMA_6

## t_signal_Rescue_allyHealth10
	* StepId: 14
	* Type: Trigger
	* TargetType: TaggedUnitsBelowHealthAndArmor
	* SuccLL: t_signal_Rescue_d_allyLow

## t_signal_Rescue_goal_defeatHostiles
	* StepId: 2
	* Type: Goal
	* TargetType: WaveFinished
	* SuccLL: t_signal_Rescue_GAMA_2

## t_signal_Rescue_i1
	* StepId: 15
	* Type: Trigger
	* TargetType: Immediate
	* SuccLL: 
		* t_signal_Rescue_ally0
		* t_signal_Rescue_wave0

## t_signal_Rescue_killAlly0
	* StepId: 4
	* Type: Trigger
	* TargetType: KillSpecificWave
	* SuccLL: 
		* t_signal_Rescue_GAMA_4
		* t_signal_Rescue_GAMA_5
		* t_signal_Rescue_GAMA_6
		* t_signal_Rescue_deactivateGoal

## t_signal_Rescue_start
	* StepId: 0
	* Type: Trigger
	* TargetType: MissionStart
	* SuccLL: 
		* t_signal_Rescue_GAMA_0
		* t_signal_Rescue_GAMA_1
		* t_signal_Rescue_GAMA_14
		* t_signal_Rescue_GAMA_15
		* t_signal_Rescue_GAMA_16
		* t_signal_Rescue_GAMA_3
		* t_signal_Rescue_GAMA_8
		* t_signal_Rescue_spawnContainer

## t_signal_Rescue_strengthCheck2
	* StepId: 10
	* Type: Trigger
	* TargetType: TaggedUnitsBelowStrength
	* SuccLL: 
		* t_signal_Rescue_GAMA_10
		* t_signal_Rescue_GAMA_11

## t_signal_Rescue_stringsFail
	* StepId: 5
	* Type: Trigger
	* TargetType: FinishGoalsString
	* TVS: 
		* t_signal_Rescue_td_fail
		* t_signal_Rescue_wait_fail
	* SuccLL: t_signal_Rescue_fail

## t_signal_Rescue_td_fail
	* StepId: 6
	* Type: Trigger
	* TargetType: OnDialogFinishedIndex

## t_signal_Rescue_td_win2
	* StepId: 1
	* Type: Trigger
	* TargetType: OnDialogFinishedIndex
	* SuccLL: t_signal_Rescue_fin

## t_signal_Rescue_w_goal
	* StepId: 9
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* t_signal_Rescue_GAMA_13
		* t_signal_Rescue_GAMA_9

## t_signal_Rescue_wait_fail
	* StepId: 8
	* Type: Trigger
	* TargetType: WaitForTime

## t_signal_Rescue_wait1
	* StepId: 17
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: t_signal_Rescue_d_intro1

## t_signal_Rescue_wait4
	* StepId: 12
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: t_signal_Rescue_GAMA_12

## t_signal_Rescue_wait5
	* StepId: 7
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* t_signal_Rescue_GAMA_7
		* t_signal_Rescue_d_fail

## t_signal_Rescue_wait7
	* StepId: 16
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: t_signal_Rescue_lookAt

## t_signal_Rescue_wait8
	* StepId: 3
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: t_signal_Rescue_d_win1

## t_signal_Rescue_wave0exist
	* StepId: 11
	* Type: Trigger
	* TargetType: UnitWithTagsExists
	* SuccLL: t_signal_Rescue_wave1

## t_signal_Rescue_wave1exist
	* StepId: 13
	* Type: Trigger
	* TargetType: UnitWithTagsExists
	* SuccLL: t_signal_Rescue_d_hostiles

## t_signal_TravelingTrader_goal_trade
	* StepId: 1
	* Type: Goal
	* TargetType: OnInteractionDone
	* TVS: travelingTrader_01
	* SuccLL: t_signal_TravelingTrader_GAMA_1

## t_signal_TravelingTrader_Start
	* StepId: 0
	* Type: None
	* TargetType: MissionStart
	* SuccLL: 
		* t_signal_TravelingTrader_GAMA_0
		* t_signal_TravelingTrader_GAMA_2
		* t_signal_TravelingTrader_GAMA_3
		* t_signal_TravelingTrader_actn_startInteraction

## t_signal_TravelingTrader_trigger_WaitForTime01
	* StepId: 3
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: t_signal_TravelingTrader_actn_dialogStart

## t_signal_TravelingTrader_trigger_WaitForTime02
	* StepId: 2
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: t_signal_TravelingTrader_actn_finishMission

## t_signal_TravelingTrader_trigger_WaitForTime03
	* StepId: 4
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: t_signal_TravelingTrader_actn_lookAt

## t_station_starbase_init
	* StepId: 0
	* Type: Trigger
	* TargetType: MissionStart
	* SuccLL: 
		* t_station_starbase_act_add_PlayerHeal_Step
		* t_station_starbase_trigger_npc_trigWait1
		* t_station_starbase_trigger_npc_wave0
		* t_station_starbase_trigger_npc_wave1

## t_station_starbase_trigger_rep_wait_PlayerHeal
	* StepId: 6
	* Type: TriggerRepeating
	* TargetType: WaitForTime
	* SuccLL: 
		* t_station_starbase_act_HealPlayer2
		* t_station_starbase_act_HealPlayer3
		* t_station_starbase_act_HealPlayer4
		* t_station_starbase_act_HealPlayer5
		* t_station_starbase_act_HealPlayer6

## t_station_starbase_wave2
	* StepId: 1
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* t_station_starbase_trigger_npc_trigWait2
		* t_station_starbase_trigger_npc_wave2

## t_station_starbase_wave3
	* StepId: 2
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* t_station_starbase_trigger_npc_trigWait3
		* t_station_starbase_trigger_npc_wave3

## t_station_starbase_wave4
	* StepId: 3
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* t_station_starbase_trigger_npc_trigWait4
		* t_station_starbase_trigger_npc_wave4

## t_station_starbase_wave5
	* StepId: 4
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: 
		* t_station_starbase_trigger_npc_trigWait5
		* t_station_starbase_trigger_npc_wave5

## t_station_starbase_wave6
	* StepId: 5
	* Type: Trigger
	* TargetType: WaitForTime
	* SuccLL: t_station_starbase_trigger_npc_wave6
