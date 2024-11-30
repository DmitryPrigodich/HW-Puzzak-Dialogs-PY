# HWM QUESTLINES WITH QUESTS


## ql_main_t0_tutorial

### qm_t0_tutMissions
	* Rewards:	CR:500
	* XPMod:	5
	* Tier:	0
	* Goals:	CompleteMission,0	CompleteMission,1	CompleteMission,2
	* Type:	Main
	* CinematicIds:	20:10:25
	* GoalParameters:	Ids&story_A01_DuzumiGate|story_A01_DuzumiGateTut	Id&story_A02_WiracodaGate	Id&story_A03_GulfTaln
	* FollowUpLines:	ql_main_t0_station

## ql_main_t0_station

### qm_t0_introStation
	* Rewards:	0A:700
	* XPMod:	5
	* Tier:	0
	* Goals:	Goto,0
	* Type:	Main
	* GoalParameters:	Target&[-1822, -636];TargetMode&Station

### qm_t0_introMarket
	* Rewards:	bp_hgn_sf_intc_01_t0:1	unlockToken_fabricator:1
	* XPMod:	5
	* Tier:	0
	* Goals:	Buy,0
	* Type:	Main
	* GoalParameters:	Id&pack_market_freeHC_insta
	* FollowUpLines:	ql_main_t0_strikeCraft

## ql_main_t0_strikeCraft

### qm_t0_introFabricator
	* Rewards:	bp_hgn_su_rcol_01_t0:1	CR:200
	* XPMod:	5
	* Tier:	0
	* Goals:	Craft,0
	* Type:	Main
	* GoalParameters:	Category&Crafting;Tags&Interceptor;Amount&1

### qm_t0_introEquipStrikecraft
	* Rewards:	bp_hgn_sf_plbo_01_t0:1
	* XPMod:	5
	* Tier:	0
	* Goals:	Equip,0
	* Type:	Main
	* GoalParameters:	Type&Squad
	* FollowUpLines:	ql_main_t0_v2_signals

## ql_main_t0_v2_signals

### qm_t0_v2_introScanning
	* Rewards:	CR:500
	* XPMod:	5
	* Tier:	0
	* Goals:	Scan,0	Scan,1
	* Type:	Main
	* GoalParameters:	Tags&InSystem_Generated;Amount&1	Tags&InSystem_Generated;Amount&1;Analyzed&True

### qm_t0_v2_introSignals
	* Rewards:	hgn_su_rcol_01_t0:1
	* XPMod:	5
	* Tier:	0
	* Goals:	CompleteMission,0	Goto,1
	* Type:	Main
	* GoalParameters:	Mode&Generated;Amount&1	Target&[-1822, -636];TargetMode&Station
	* FollowUpLines:	ql_main_t0_mining

## ql_main_t0_mining

### qm_t0_introScanBelts
	* Rewards:	CR:500
	* XPMod:	5
	* Tier:	0
	* Goals:	Goto,0	Statistic,1
	* Type:	Main
	* GoalParameters:	Target&[-1747, -653]	Id&ScannedBelt;Total&1

### qm_t0_introMining
	* Rewards:	0A:600
	* XPMod:	5
	* Tier:	0
	* Goals:	Statistic,0
	* Type:	Main
	* GoalParameters:	Id&Mined0A;Amount&50
	* FollowUpLines:	ql_main_t0_support

## ql_main_t0_support

### qm_t0_support
	* Rewards:	officer_riffsaOfficer:1
	* XPMod:	5
	* Tier:	0
	* Goals:	Pay,0
	* Type:	Main
	* GoalParameters:	Id&0A;Amount&25;SysId&[-1822, -636];Mode&Station
	* FollowUpLines:	ql_main_t0_officer

## ql_main_t0_officer

### qm_t0_introBridge
	* Rewards:	bp_hgn_cf_assa_01_t0:1	0A:700	unlockToken_shipyard:1
	* XPMod:	5
	* Tier:	0
	* Goals:	Equip,0
	* Type:	Main
	* GoalParameters:	Type&Officer;Location&Bridge
	* FollowUpLines:	ql_main_t0_escorts

## ql_main_t0_escorts

### qm_t0_introShipyard
	* Rewards:	CR:500
	* XPMod:	5
	* Tier:	0
	* Goals:	Craft,0
	* Type:	Main
	* GoalParameters:	Category&Crafting;Tags&AssaultFrigate;Amount&1

### qm_t0_introEquipEscorts
	* Rewards:	bp_hgn_cf_scou_01_t0:1	0A:200
	* XPMod:	5
	* Tier:	0
	* Goals:	Equip,0
	* Type:	Main
	* GoalParameters:	Type&Escort
	* FollowUpLines:	ql_main_t0_sideProg

## ql_main_t0_sideProg

### qm_t0_scientist_Baaekh_A
	* Rewards:	CR:500
	* XPMod:	5
	* Tier:	0
	* Goals:	Goto,0	Goto,1	Statistic,2	Statistic,2
	* Type:	Main
	* GoalParameters:	Target&[-1785, -690]	Target&[-1844, -690]	Id&ScannedBelt;Total&4	Id&ScannedGenerated;Amount&1

### qm_t0_scientist_Baaekh_B
	* Rewards:	0A:700
	* XPMod:	5
	* Tier:	0
	* Goals:	CompleteMission,0	Goto,1
	* Type:	Main
	* GoalParameters:	Mode&Generated;Amount&1	Target&[-1785, -690]
	* FollowUpLines:	ql_main_t0_relic

## ql_main_t0_relic

### qm_t0_relic
	* Rewards:	CR:700	0A:300
	* XPMod:	5
	* Tier:	0
	* Goals:	Goto,0	Scan,1	CompleteMission, 2
	* Type:	Main
	* GoalParameters:	Target&[-1832, -619]	Tags&InSystem;Amount&1	Id&story_A04_RelicSignature
	* FollowUpLines:	ql_main_t0_moreMining

## ql_main_t0_moreMining

### qm_t0_scientist_Hyeaa_A
	* Rewards:	CR:600	0A:400
	* XPMod:	5
	* Tier:	0
	* Goals:	Goto,0	Craft,1	Equip,2	Statistic,3
	* Type:	Main
	* GoalParameters:	Target&[-1800, -623]	Category&Crafting;Tags&RCol;Amount&1	Type&Squad;Tags&RCol	Id&Mined0A;Amount&225
	* FollowUpLines:	ql_main_t0_jolja

## no_ql

### qm_t0_scientist_Hyeaa_B
	* Rewards:	0A:700
	* XPMod:	5
	* Tier:	0
	* Goals:	Craft,0	Craft,0	Craft,0	Craft,1
	* Type:	Main
	* GoalParameters:	Category&Crafting;Tags&RCol;Amount&1	Category&Crafting;Tags&PlasmaBomber;Amount&1	Category&Crafting;Tags&Interceptor;Amount&1	Category&Crafting;Tags&Frigate;Amount&1

### qm_t1_facHiigaran_A
	* Rewards:	1C:1500
	* XPMod:	15
	* Tier:	1
	* Goals:	Goto,0	Statistic,1	CompleteMission,1	Pay,2
	* Type:	Side
	* GoalParameters:	Target&[-1558, -672]	Id&ScannedGenerated;Amount&3	Mode&Generated;Amount&3	Id&1A;Amount&500

### qm_t1_facHiigaran_B
	* Rewards:	CR:3500
	* XPMod:	15
	* Tier:	1
	* Goals:	Goto,0	Statistic,1	Statistic,2	Statistic,2	Goto,3
	* Type:	Side
	* GoalParameters:	Target&[-1429, -553]	Id&ScannedBelt;Total&10	Ids&Mined1A_Mined1B_Mined1C;Amount&500	Id&ShipsDestroyed;Amount&15	Target&[-1429, -553]

### qm_t1_facHiigaran_C
	* Rewards:	1B:1500
	* XPMod:	15
	* Tier:	1
	* Goals:	Goto,0	Statistic,1	Pay,2	Pay,3	Pay,4
	* Type:	Side
	* GoalParameters:	Target&[-1552, -610]	Id&Mined1A;Amount&500	Id&1A;Amount&150	Id&hgn_su_rcol_01_t0;Amount&3	Id&hgn_sf_intc_01_t0;Amount&1

### qm_t1_facHiigaran_D
	* Rewards:	1A:1500
	* XPMod:	15
	* Tier:	1
	* Goals:	Goto,0	Scan,1	Statistic,2	CompleteMission,2	Goto,3
	* Type:	Side
	* GoalParameters:	Target&[-1525, -731]	Tags&InSystem;Amount&3;Analyzed&True	Id&ShipsDestroyed;Amount&15	Mode&Generated;Amount&3	Target&[-1525, -731]

### qm_t1_facCangacian_A
	* Rewards:	insig_r1:15
	* XPMod:	15
	* Tier:	1
	* Goals:	Goto,0	Statistic,1	Statistic,2	Statistic,2	Goto,3
	* Type:	Side
	* GoalParameters:	Target&[-1376, -709]	Id&ShipsDestroyedP1;Amount&15	Ids&Mined1A_Mined1B_Mined1C;Amount&1000	Ids&Refining1N_Refining1O_Refining1P;Amount&500	Target&[-1376, -709]

### qm_t1_facCangacian_B
	* Rewards:	1A:1500
	* XPMod:	15
	* Tier:	1
	* Goals:	Goto,0	Statistic,1	CompleteMission,1	Statistic,1	Goto,2
	* Type:	Side
	* GoalParameters:	Target&[-1497, -628]	Id&ScannedGenerated;Amount&4	Mode&Generated;Amount&4	Id&ShipsDestroyedP1;Amount&15	Target&[-1497, -628]

### qm_t1_facCangacian_C
	* Rewards:	1C:1500
	* XPMod:	15
	* Tier:	1
	* Goals:	Goto,0	Statistic,1	Statistic,2	Statistic,2	Pay,3
	* Type:	Side
	* GoalParameters:	Target&[-1793, -424]	Id&ScannedBelt;Total&15	Id&Mined1A;Amount&1000	Id&Refining1N;Amount&500	Id&1N;Amount&300

### qm_t1_facCangacian_D
	* Rewards:	CR:3500	0A: 750
	* XPMod:	15
	* Tier:	1
	* Goals:	Goto,0	Scan,1	Pay,2	CompleteMission,3	Goto,4
	* Type:	Side
	* GoalParameters:	Target&[-1752, -861]	Tags&InSystem;Amount&2;Analyzed&True	Id&hgn_sf_intc_01_t1;Amount&1	Mode&Generated;Amount&4	Target&[-1752, -861]

### qm_t1_facProgenitors_A
	* Rewards:	CR:3500	0A: 750
	* XPMod:	15
	* Tier:	1
	* Goals:	Goto,0	Statistic,1	Statistic,1	Statistic,1	Goto,2
	* Type:	Side
	* GoalParameters:	Target&[-1497, -628]	Id&ShipsDestroyedProgenitor;Amount&10	Ids&Mined1A_Mined1B_Mined1C;Amount&3000	Ids&Refining1N_Refining1O_Refining1P;Amount&1500	Target&[-1497, -628]

### qm_t1_facProgenitors_B
	* Rewards:	1A:1500
	* XPMod:	15
	* Tier:	1
	* Goals:	Goto,0	Statistic,1	Craft,1	CompleteMission,1	Goto,2
	* Type:	Side
	* GoalParameters:	Target&[-1376, -709]	Id&ScannedGenerated;Amount&5	Category&Upgrade;Tags&Weapon_Module;Amount&1	Mode&Generated;Amount&5;Tier&1	Target&[-1376, -709]

### qm_t1_facProgenitors_C
	* Rewards:	1C:1500
	* XPMod:	15
	* Tier:	1
	* Goals:	Goto,0	GainItem,1	Craft,2	CompleteMission,3	Goto,4
	* Type:	Side
	* GoalParameters:	Target&[-1543, -626]	Id&AA;Amount&30;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash	Category&Upgrade;Tags&Weapon_Module;Amount&2	Mode&Generated;Amount&5;Tier&1	Target&[-1543, -626]

### qm_t1_facProgenitors_D
	* Rewards:	1B:1500
	* XPMod:	15
	* Tier:	1
	* Goals:	Goto,0	Statistic,1	GainItem,2	Statistic,2	Goto,3
	* Type:	Side
	* GoalParameters:	Target&[-1793, -424]	Id&ScannedBelt;Total&20	Id&AB;Amount&10;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash	Id&ShipsDestroyedProgenitor;Amount&10	Target&[-1793, -424]

### qm_t1_facIyatequa_A
	* Rewards:	1B:1500
	* XPMod:	15
	* Tier:	1
	* Goals:	Goto,0	Statistic,1	GainItem,1	Craft,1	Goto,2
	* Type:	Side
	* GoalParameters:	Target&[-1825, -480]	Ids&Mined1A_Mined1B_Mined1C;Amount&3000	Tags&RareEarth;Amount&60;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash	Category&Upgrade;Tags&Weapon_Module;Amount&2	Target&[-1825, -480]

### qm_t1_facIyatequa_B
	* Rewards:	1A:1500
	* XPMod:	15
	* Tier:	1
	* Goals:	Goto,0	Statistic,1	Craft,1	Statistic,2	Goto,3
	* Type:	Side
	* GoalParameters:	Target&[-1525, -731]	Ids&Refining1N_Refining1O_Refining1P;Amount&1500	Category&Upgrade;Tags&Weapon_Module;Amount&1	Id&ShipsDestroyed;Amount&25	Target&[-1525, -731]

### qm_t1_facIyatequa_C
	* Rewards:	CR:3500	0A: 750
	* XPMod:	15
	* Tier:	1
	* Goals:	Goto,0	Scan,1	CompleteMission,1	Statistic,1	Goto,2
	* Type:	Side
	* GoalParameters:	Target&[-1429, -553]	Tags&InSystem;Amount&5;Analyzed&True	Mode&Generated;Amount&5;Tier&1	Id&ShipsDestroyed;Amount&25	Target&[-1429, -553]

### qm_t1_facIyatequa_D
	* Rewards:	1C:1500
	* XPMod:	15
	* Tier:	1
	* Goals:	Goto,0	Goto,1	Scan,2	CompleteMission,2	Pay,3	Goto,4
	* Type:	Side
	* GoalParameters:	Target&[-1552, -610]	Target&[-1558, -672]	Tags&InSystem;Amount&5;Analyzed&True	Mode&Generated;Amount&5;Tier&1	Id&1O;Amount&1000	Target&[-1552, -610]

### qm_t2_facCangacian_A
	* Rewards:	2C:2000
	* XPMod:	45
	* Tier:	2
	* Goals:	Goto,0	Statistic,1	GainItem,2	Craft,3	Goto,4
	* Type:	Side
	* GoalParameters:	Target&[-1491, -596]	Id&ShipsDestroyed;Amount&35	Id&RP;Amount&45;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash	Tags&Research;Amount&1	Target&[-1491, -596]

### qm_t2_facCangacian_B
	* Rewards:	2B:2000
	* XPMod:	45
	* Tier:	2
	* Goals:	Goto,0	CompleteMission,1	Pay,2	Pay,2	Pay,2	GainItem,3	Goto,4
	* Type:	Side
	* GoalParameters:	Target&[-1643, -552]	Mode&Generated;Amount&10;Tier&1	Id&2A;Amount&650	Id&2B;Amount&650	Id&2C;Amount&650	Id&RP;Amount&45;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash	Target&[-1643, -552]

### qm_t2_facCangacian_C
	* Rewards:	2A:2000
	* XPMod:	45
	* Tier:	2
	* Goals:	Goto,0	GainItem,1	Statistic,2	Statistic,2	Goto,3
	* Type:	Side
	* GoalParameters:	Target&[-1784, -564]	Id&RP;Amount&45;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash	Id&ScannedBelt;Total&30	Id&ShipsDestroyed;Amount&35	Target&[-1784, -564]

### qm_t2_facCangacian_D
	* Rewards:	insig_r2:10
	* XPMod:	45
	* Tier:	2
	* Goals:	Goto,0	Pay,1	Statistic,2	CompleteMission,2	Goto,3
	* Type:	Side
	* GoalParameters:	Target&[-1559, -788]	Id&2O;Amount&1000	Id&ScannedGenerated;Amount&10	Mode&Generated;Amount&10;Tier&1	Target&[-1559, -788]

### qm_t2_facHiigaran_A
	* Rewards:	2B:2000
	* XPMod:	45
	* Tier:	2
	* Goals:	Goto,0	Scan,1	Craft,2	Pay,3
	* Type:	Side
	* GoalParameters:	Target&[-1784, -564]	Tags&InSystem_T2up;Amount&5;Analyzed&True	Category&Crafting;Tags&Part;Amount&450	Id&2P;Amount&1000

### qm_t2_facHiigaran_B
	* Rewards:	2C:2000
	* XPMod:	45
	* Tier:	2
	* Goals:	Goto,0	CompleteMission,1	Craft,2	Pay,3
	* Type:	Side
	* GoalParameters:	Target&[-1659, -561]	Mode&Generated;Amount&10;Tier&1	Category&Crafting;Tags&Part;Amount&180	Id&intmed_ship_small_t2;Amount&60

### qm_t2_facHiigaran_C
	* Rewards:	2A:2000
	* XPMod:	45
	* Tier:	2
	* Goals:	Goto,0	CompleteMission,1	Statistic,1	Pay,2
	* Type:	Side
	* GoalParameters:	Target&[-1491, -596]	Mode&Strike;Amount&1	Id&ShipsDestroyed;Amount&35	Id&intmed_weapon_small_t2;Amount&60

### qm_t2_facHiigaran_D
	* Rewards:	CR:5000	insig_r1:15
	* XPMod:	45
	* Tier:	2
	* Goals:	Goto,0	Statistic,1	Statistic,1	Pay,2	Pay,2	Pay,2
	* Type:	Side
	* GoalParameters:	Target&[-1780, -457]	Id&ScannedBelt;Total&35	Id&ShipsDestroyed;Amount&35	Id&2A;Amount&650	Id&2B;Amount&650	Id&2C;Amount&650

### qm_t2_facIyatequa_A
	* Rewards:	insig_r1:15	CR:5000
	* XPMod:	45
	* Tier:	2
	* Goals:	Goto,0	Pay,1	Pay,1	Pay,1	CompleteQuest,2	Goto,3
	* Type:	Side
	* GoalParameters:	Target&[-1643, -552]	Id&2O;Amount&1000	Id&2P;Amount&1000	Id&intmed_ship_large_t2;Amount&20	Amount&7;Tags&Faction_Tr1_T2up	Target&[-1643, -552]

### qm_t2_facIyatequa_B
	* Rewards:	2C:2000
	* XPMod:	45
	* Tier:	2
	* Goals:	Goto,0	Statistic,1	CompleteQuest,2	Goto,3
	* Type:	Side
	* GoalParameters:	Target&[-1659, -561]	Id&ShipsDestroyedProgenitor;Amount&15	Amount&15;Tags&Faction_Tr1_T2up	Target&[-1659, -561]

### qm_t2_facIyatequa_C
	* Rewards:	2B:2000
	* XPMod:	45
	* Tier:	2
	* Goals:	Goto,0	Statistic,1	Statistic,2	CompleteQuest,2	Goto,3
	* Type:	Side
	* GoalParameters:	Target&[-1780, -457]	Id&ShipsDestroyedP1;Amount&30	Id&ShipsDestroyed;Amount&30	Amount&7;Tags&Faction_Tr1_T2up	Target&[-1780, -457]

### qm_t2_facIyatequa_D
	* Rewards:	2A:2000
	* XPMod:	45
	* Tier:	2
	* Goals:	Goto,0	Scan,1	GainItem,2	Pay,3	Pay,3	Goto,4
	* Type:	Side
	* GoalParameters:	Target&[-1559, -788]	Tags&InSystem_T2up;Amount&10;Analyzed&True	Id&RP;Amount&45;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash	Id&hgn_su_rcol_01_t2;Amount&1	Id&2D;Amount&500	Target&[-1559, -788]

### qm_t2_internalRefinery
	* Rewards:	1A:500	1C:500
	* XPMod:	45
	* Tier:	2
	* Goals:	Craft,0	Equip,1
	* Type:	Main
	* GoalParameters:	Tags&Refining_Factory	Type&Internal;Tags&Refining_Factory

### qm_t2_facTanoch_A
	* Rewards:	CR:5000	1C:1000
	* XPMod:	45
	* Tier:	2
	* Goals:	Statistic,0	Pay,1	Pay,1	Pay,1
	* Type:	Side
	* GoalParameters:	Id&ScannedBelt;Total&40	Id&2N;Amount&350	Id&2O;Amount&350	Id&2P;Amount&350

### qm_t2_facTanoch_B
	* Rewards:	2B:750	1A:1000
	* XPMod:	45
	* Tier:	2
	* Goals:	Statistic,0	Statistic,0
	* Type:	Side
	* GoalParameters:	Id&RepTanoch;Amount&350	Id&ShipsDestroyedP1;Amount&15

### qm_t2_facTanoch_C
	* Rewards:	2A:750	0A:1250
	* XPMod:	45
	* Tier:	2
	* Goals:	Craft,0	Craft,0	Pay,1	Pay,1	Pay,1
	* Type:	Side
	* GoalParameters:	Category&Refining;Amount&2000;Tags&T2	Category&Crafting;Tags&Part;Amount&150	Id&2O;Amount&350	Id&intmed_module_small_t2;Amount&50	Id&hgn_su_rcol_01_t2;Amount&1

### qm_t2_facTanoch_D
	* Rewards:	2C:750	1B:1000
	* XPMod:	45
	* Tier:	2
	* Goals:	Scan,0	Statistic,0
	* Type:	Side
	* GoalParameters:	Tags&InSystem_Generated_T2up;Amount&10;Analyzed&True	Id&ShipsDestroyedYaot;Amount&15

### qm_t2_facYaot_A
	* Rewards:	2A:1000	1B:1250
	* XPMod:	45
	* Tier:	2
	* Goals:	Statistic,0
	* Type:	Side
	* GoalParameters:	Id&ShipsDestroyedYaot;Amount&30

### qm_t2_facYaot_B
	* Rewards:	CR:6000	1C:1250
	* XPMod:	45
	* Tier:	2
	* Goals:	Statistic,0	Statistic,0
	* Type:	Side
	* GoalParameters:	Id&ScannedBelt;Total&45	Ids&Mined2A_Mined2B_Mined2C_Mined2D;Amount&1800

### qm_t2_facYaot_C
	* Rewards:	2C:1000	1A:1250
	* XPMod:	45
	* Tier:	2
	* Goals:	Scan,0	CompleteMission,0	Scan,0
	* Type:	Side
	* GoalParameters:	Tags&InSystem_Generated_T2up;Amount&10;Analyzed&True	Mode&Generated;Tags&T2up;Amount&10	Tags&InGalaxy_T2up;Amount&7

### qm_t2_facYaot_D
	* Rewards:	2B:1000	0A:1500
	* XPMod:	45
	* Tier:	2
	* Goals:	GainItem,0	UpgradeOfficer,0
	* Type:	Side
	* GoalParameters:	Tags&Insignia;Amount&80;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash	Amount&15

### qs_unlockStrikes_t1
	* Rewards:	rw_rbox_qr_large:1
	* XPMod:	2
	* Tier:	1
	* Goals:	Goto,0	Scan,1
	* Type:	Side
	* GoalParameters:	Target&[-1535, -436];MoveType&InSystem

### qt_daily_buy
	* Rewards:	LP:3	battery_c:1
	* XPMod:	10
	* Tier:	-1
	* Goals:	Buy,0
	* Type:	Daily
	* GoalIconId:	GoalBuy
	* RepetitionType:	Daily
	* GoalParameters:	Amount&1

### qt_daily_mine
	* Rewards:	LP:3	battery_c:1
	* XPMod:	10
	* Tier:	-1
	* Goals:	Statistic,0
	* Type:	Daily
	* GoalIconId:	GoalMine
	* RepetitionType:	Daily
	* GoalParameters:	Id&Mined;Amount&1500

### qt_daily_refine
	* Rewards:	OF:1
	* XPMod:	10
	* Tier:	-1
	* Goals:	Craft,0
	* Type:	Daily
	* GoalIconId:	GoalRefinery
	* RepetitionType:	Daily
	* GoalParameters:	Category&Refining;Amount&500

### qt_daily_craft
	* Rewards:	LP:3	battery_c:1
	* XPMod:	10
	* Tier:	-1
	* Goals:	Craft,0
	* Type:	Daily
	* GoalIconId:	GoalCraft
	* RepetitionType:	Daily
	* GoalParameters:	Category&Crafting;Amount&10

### qt_daily_gainRP
	* Rewards:	LP:3	battery_c:1
	* XPMod:	10
	* Tier:	-1
	* Goals:	GainItem,0
	* Type:	Daily
	* GoalIconId:	GoalRP
	* RepetitionType:	Daily
	* GoalParameters:	Id&RP;Amount&400;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qt_daily_insignias
	* Rewards:	OF:1
	* XPMod:	10
	* Tier:	-1
	* Goals:	GainItem,0
	* Type:	Daily
	* GoalIconId:	GoalInsignias
	* RepetitionType:	Daily
	* GoalParameters:	Tags&Insignia;Amount&5;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qt_daily_liaison
	* Rewards:	LP:3	battery_c:1
	* XPMod:	10
	* Tier:	-1
	* Goals:	CompleteMission,0
	* Type:	Daily
	* GoalIconId:	GoalMissions
	* RepetitionType:	Daily
	* GoalParameters:	Amount&3

### qt_daily_destroy
	* Rewards:	LP:3	battery_c:1
	* XPMod:	10
	* Tier:	-1
	* Goals:	Statistic,0
	* Type:	Daily
	* GoalIconId:	GoalDestroyEnemy
	* RepetitionType:	Daily
	* GoalParameters:	Id&ShipsDestroyed;Amount&15

### qt_daily_signals
	* Rewards:	LP:3	battery_c:1
	* XPMod:	10
	* Tier:	-1
	* Goals:	Scan,0
	* Type:	Daily
	* GoalIconId:	GoalScan
	* RepetitionType:	Daily
	* GoalParameters:	Tags&InSystem;Amount&5;Analyzed&True

### qt_daily_dailyMission
	* Rewards:	OF:1
	* XPMod:	10
	* Tier:	-1
	* Goals:	CompleteMission,0
	* Type:	Daily
	* GoalIconId:	GoalStrike
	* RepetitionType:	Daily
	* GoalParameters:	Amount&1;Mode&Strike

### qt_daily_dailies
	* Rewards:	HC:25
	* XPMod:	10
	* Tier:	-1
	* Goals:	CompleteQuest,0
	* Type:	Daily
	* GoalIconId:	GoalDaily
	* RepetitionType:	Daily
	* GoalParameters:	Amount&8;Tags&Daily

### qt_weekly_dailies
	* Rewards:	LP:6	OF:3
	* XPMod:	60
	* Tier:	-1
	* Goals:	CompleteQuest,0
	* Type:	Weekly
	* GoalIconId:	GoalDaily
	* RepetitionType:	Weekly
	* GoalParameters:	Amount&40;Tags&Daily

### qt_weekly_reputation
	* Rewards:	LP:12	battery_r:1
	* XPMod:	60
	* Tier:	-1
	* Goals:	CompleteQuest,0
	* Type:	Weekly
	* GoalIconId:	GoalLiason
	* RepetitionType:	Weekly
	* GoalParameters:	Amount&9;Tags&Faction

### qt_weekly_clanQuests
	* Rewards:	LP:12	battery_r:1
	* XPMod:	60
	* Tier:	-1
	* Goals:	CompleteQuest,0
	* Type:	Weekly
	* GoalIconId:	GoalClan
	* RepetitionType:	Weekly
	* GoalParameters:	Amount&10;Tags&Clan

### qt_weekly_levelOfficers
	* Rewards:	LP:6	OF:3
	* XPMod:	60
	* Tier:	-1
	* Goals:	UpgradeOfficer,0
	* Type:	Weekly
	* GoalIconId:	GoalOfficerUpgrade
	* RepetitionType:	Weekly
	* GoalParameters:	Amount&7

### qt_weekly_upgrades
	* Rewards:	LP:12	battery_r:1
	* XPMod:	60
	* Tier:	-1
	* Goals:	Craft,0
	* Type:	Weekly
	* GoalIconId:	GoalModuleUpgrade
	* RepetitionType:	Weekly
	* GoalParameters:	Category&Upgrade;Amount&10

### qt_weekly_missions
	* Rewards:	LP:6	OF:3
	* XPMod:	60
	* Tier:	-1
	* Goals:	CompleteMission,0
	* Type:	Weekly
	* GoalIconId:	GoalSignals
	* RepetitionType:	Weekly
	* GoalParameters:	Amount&9;Mode&Generated

### qt_weekly_research
	* Rewards:	LP:12	battery_r:1
	* XPMod:	60
	* Tier:	-1
	* Goals:	Craft,0
	* Type:	Weekly
	* GoalIconId:	GoalRP
	* GoalParameters:	Tags&Research;Amount&5

### qe_amaSum_2023_daily_A_t1
	* Rewards:	Z4:10
	* ScheduleType:	Hidden
	* XPMod:	10
	* EndOffset:	0:0:0
	* EventId:	event_season_amaSum_2023_t1
	* Tier:	1
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Tags&Asteroid_Crud_T1up;Amount&350;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

### qe_amaSum_2023_daily_B_t1
	* Rewards:	Z4:10
	* ScheduleType:	Hidden
	* XPMod:	10
	* EndOffset:	0:0:0
	* EventId:	event_season_amaSum_2023_t1
	* Tier:	1
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Category&Crafting;Tags&T1up;Amount&1

### qe_amaSum_2023_daily_C_t1
	* Rewards:	Z4:10
	* ScheduleType:	Hidden
	* XPMod:	10
	* EndOffset:	0:0:0
	* EventId:	event_season_amaSum_2023_t1
	* Tier:	1
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Ids&ShipsDestroyedDarkHiigaranT1_ShipsDestroyedDarkHiigaranT2_ShipsDestroyedDarkHiigaranT3_ShipsDestroyedDarkHiigaranT4;Amount&10

### qe_amaSum_2023_daily_D_t1
	* Rewards:	Z4:10
	* ScheduleType:	Hidden
	* XPMod:	10
	* EndOffset:	0:0:0
	* EventId:	event_season_amaSum_2023_t1
	* Tier:	1
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Tags&ProgenitorRelic_T1up;Amount&1;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_amaSum_2023_daily_A_t2
	* Rewards:	Z4:10
	* ScheduleType:	Hidden
	* XPMod:	30
	* EndOffset:	0:0:0
	* EventId:	event_season_amaSum_2023_t2
	* Tier:	2
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Tags&Asteroid_Crud_T2up;Amount&400;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

### qe_amaSum_2023_daily_B_t2
	* Rewards:	Z4:10
	* ScheduleType:	Hidden
	* XPMod:	30
	* EndOffset:	0:0:0
	* EventId:	event_season_amaSum_2023_t2
	* Tier:	2
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Category&Crafting;Tags&Part_T2up;Amount&25

### qe_amaSum_2023_daily_C_t2
	* Rewards:	Z4:10
	* ScheduleType:	Hidden
	* XPMod:	30
	* EndOffset:	0:0:0
	* EventId:	event_season_amaSum_2023_t2
	* Tier:	2
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Ids&ShipsDestroyedDarkHiigaranT2_ShipsDestroyedDarkHiigaranT3_ShipsDestroyedDarkHiigaranT4;Amount&10

### qe_amaSum_2023_daily_D_t2
	* Rewards:	Z4:10
	* ScheduleType:	Hidden
	* XPMod:	30
	* EndOffset:	0:0:0
	* EventId:	event_season_amaSum_2023_t2
	* Tier:	2
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Tags&ProgenitorRelic_T2up;Amount&1;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_amaSum_2023_daily_A_t3
	* Rewards:	Z4:10
	* ScheduleType:	Hidden
	* XPMod:	90
	* EndOffset:	0:0:0
	* EventId:	event_season_amaSum_2023_t3
	* Tier:	3
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Tags&Asteroid_Crud_T3up;Amount&450;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

### qe_amaSum_2023_daily_B_t3
	* Rewards:	Z4:10
	* ScheduleType:	Hidden
	* XPMod:	90
	* EndOffset:	0:0:0
	* EventId:	event_season_amaSum_2023_t3
	* Tier:	3
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Category&Crafting;Tags&Part_T3up;Amount&25

### qe_amaSum_2023_daily_C_t3
	* Rewards:	Z4:10
	* ScheduleType:	Hidden
	* XPMod:	90
	* EndOffset:	0:0:0
	* EventId:	event_season_amaSum_2023_t3
	* Tier:	3
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Ids&ShipsDestroyedDarkHiigaranT3_ShipsDestroyedDarkHiigaranT4;Amount&10

### qe_amaSum_2023_daily_D_t3
	* Rewards:	Z4:10
	* ScheduleType:	Hidden
	* XPMod:	90
	* EndOffset:	0:0:0
	* EventId:	event_season_amaSum_2023_t3
	* Tier:	3
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Tags&ProgenitorRelic_T3up;Amount&1;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_amaSum_2023_daily_A_t4
	* Rewards:	Z4:10
	* ScheduleType:	Hidden
	* XPMod:	270
	* EndOffset:	0:0:0
	* EventId:	event_season_amaSum_2023_t4
	* Tier:	4
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Tags&Asteroid_Crud_T4up;Amount&500;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

### qe_amaSum_2023_daily_B_t4
	* Rewards:	Z4:10
	* ScheduleType:	Hidden
	* XPMod:	270
	* EndOffset:	0:0:0
	* EventId:	event_season_amaSum_2023_t4
	* Tier:	4
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Category&Crafting;Tags&Part_T4up;Amount&25

### qe_amaSum_2023_daily_C_t4
	* Rewards:	Z4:10
	* ScheduleType:	Hidden
	* XPMod:	270
	* EndOffset:	0:0:0
	* EventId:	event_season_amaSum_2023_t4
	* Tier:	4
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Ids&ShipsDestroyedDarkHiigaranT4;Amount&10

### qe_amaSum_2023_daily_D_t4
	* Rewards:	Z4:10
	* ScheduleType:	Hidden
	* XPMod:	270
	* EndOffset:	0:0:0
	* EventId:	event_season_amaSum_2023_t4
	* Tier:	4
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Tags&ProgenitorRelic_T4up;Amount&1;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_mar_2024_daily_A_t1
	* Rewards:	Z0:10
	* ScheduleType:	Hidden
	* XPMod:	10
	* EndOffset:	0:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t1
	* Tier:	1
	* Goals:	Scan,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Tags&InSystem_Container_T1up;Amount&1;Analyzed&True

### qe_7days_mar_2024_daily_A_t2
	* Rewards:	Z0:10
	* ScheduleType:	Hidden
	* XPMod:	30
	* EndOffset:	0:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t2
	* Tier:	2
	* Goals:	Scan,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Tags&InSystem_Container_T2up;Amount&1;Analyzed&True

### qe_7days_mar_2024_daily_A_t3
	* Rewards:	Z0:10
	* ScheduleType:	Hidden
	* XPMod:	90
	* EndOffset:	0:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t3
	* Tier:	3
	* Goals:	Scan,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Tags&InSystem_Container_T3up;Amount&1;Analyzed&True

### qe_7days_mar_2024_daily_A_t4
	* Rewards:	Z0:10
	* ScheduleType:	Hidden
	* XPMod:	270
	* EndOffset:	0:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t4
	* Tier:	4
	* Goals:	Scan,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Tags&InSystem_Container_T4up;Amount&1;Analyzed&True

### qe_7days_mar_2024_daily_B_t1
	* Rewards:	Z0:10
	* ScheduleType:	Hidden
	* XPMod:	10
	* EndOffset:	0:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t1
	* Tier:	1
	* Goals:	Pay,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Id&questItem_progenitorRelic_t1;Amount&1

### qe_7days_mar_2024_daily_B_t2
	* Rewards:	Z0:10
	* ScheduleType:	Hidden
	* XPMod:	30
	* EndOffset:	0:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t2
	* Tier:	2
	* Goals:	Pay,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Id&questItem_progenitorRelic_t2;Amount&1

### qe_7days_mar_2024_daily_B_t3
	* Rewards:	Z0:10
	* ScheduleType:	Hidden
	* XPMod:	90
	* EndOffset:	0:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t3
	* Tier:	3
	* Goals:	Pay,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Id&questItem_progenitorRelic_t3;Amount&1

### qe_7days_mar_2024_daily_B_t4
	* Rewards:	Z0:10
	* ScheduleType:	Hidden
	* XPMod:	270
	* EndOffset:	0:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t4
	* Tier:	4
	* Goals:	Pay,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Id&questItem_progenitorRelic_t4;Amount&1

### qe_7days_mar_2024_daily_C_t1
	* Rewards:	Z0:10
	* ScheduleType:	Hidden
	* XPMod:	10
	* EndOffset:	0:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t1
	* Tier:	1
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Amount&1;Tags&Rare_T1up;Mode&Generated

### qe_7days_mar_2024_daily_C_t2
	* Rewards:	Z0:10
	* ScheduleType:	Hidden
	* XPMod:	30
	* EndOffset:	0:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t2
	* Tier:	2
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Amount&1;Tags&Epic_T2up;Mode&Generated

### qe_7days_mar_2024_daily_C_t3
	* Rewards:	Z0:10
	* ScheduleType:	Hidden
	* XPMod:	90
	* EndOffset:	0:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t3
	* Tier:	3
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Amount&1;Tags&Epic_T3up;Mode&Generated

### qe_7days_mar_2024_daily_C_t4
	* Rewards:	Z0:10
	* ScheduleType:	Hidden
	* XPMod:	270
	* EndOffset:	0:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t4
	* Tier:	4
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Amount&1;Tags&Epic_T4up;Mode&Generated

### qe_7days_mar_2024_daily_D_t1
	* Rewards:	Z0:10
	* ScheduleType:	Hidden
	* XPMod:	10
	* EndOffset:	0:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t1
	* Tier:	1
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Id&LP;Amount&10;ExcludedSources&BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem

### qe_7days_mar_2024_daily_D_t2
	* Rewards:	Z0:10
	* ScheduleType:	Hidden
	* XPMod:	30
	* EndOffset:	0:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t2
	* Tier:	2
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Id&LP;Amount&10;ExcludedSources&BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem

### qe_7days_mar_2024_daily_D_t3
	* Rewards:	Z0:10
	* ScheduleType:	Hidden
	* XPMod:	90
	* EndOffset:	0:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t3
	* Tier:	3
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Id&LP;Amount&10;ExcludedSources&BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem

### qe_7days_mar_2024_daily_D_t4
	* Rewards:	Z0:10
	* ScheduleType:	Hidden
	* XPMod:	270
	* EndOffset:	0:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t4
	* Tier:	4
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Id&LP;Amount&10;ExcludedSources&BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem

### qe_iyaFal_2023_daily_A_t1
	* Rewards:	Z3:10
	* ScheduleType:	Locked
	* XPMod:	10
	* EndOffset:	-7:0:0
	* EventId:	event_season_iyaFal_2023_t1
	* Tier:	1
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Ids&ShipsDestroyedP1T1_ShipsDestroyedP1T2_ShipsDestroyedP1T3_ShipsDestroyedP1T4;Amount&10

### qe_iyaFal_2023_daily_B_t1
	* Rewards:	Z3:10
	* ScheduleType:	Locked
	* XPMod:	10
	* EndOffset:	-7:0:0
	* EventId:	event_season_iyaFal_2023_t1
	* Tier:	1
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Id&CR;Amount&1250;ExcludedSources&BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

### qe_iyaFal_2023_daily_C_t1
	* Rewards:	Z3:10
	* ScheduleType:	Locked
	* XPMod:	10
	* EndOffset:	-7:0:0
	* EventId:	event_season_iyaFal_2023_t1
	* Tier:	1
	* Goals:	Scan,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Tags&InSystem_T1up;Amount&10;Analyzed&True

### qe_iyaFal_2023_daily_D_t1
	* Rewards:	Z3:10
	* ScheduleType:	Locked
	* XPMod:	10
	* EndOffset:	-7:0:0
	* EventId:	event_season_iyaFal_2023_t1
	* Tier:	1
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Tags&RareEarth_T1up;Amount&20;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_iyaFal_2023_daily_A_t2
	* Rewards:	Z3:10
	* ScheduleType:	Locked
	* XPMod:	30
	* EndOffset:	-7:0:0
	* EventId:	event_season_iyaFal_2023_t2
	* Tier:	2
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Ids&ShipsDestroyedP1T2_ShipsDestroyedP1T3_ShipsDestroyedP1T4;Amount&10

### qe_iyaFal_2023_daily_B_t2
	* Rewards:	Z3:10
	* ScheduleType:	Locked
	* XPMod:	30
	* EndOffset:	-7:0:0
	* EventId:	event_season_iyaFal_2023_t2
	* Tier:	2
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Id&CR;Amount&2500;ExcludedSources&BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

### qe_iyaFal_2023_daily_C_t2
	* Rewards:	Z3:10
	* ScheduleType:	Locked
	* XPMod:	30
	* EndOffset:	-7:0:0
	* EventId:	event_season_iyaFal_2023_t2
	* Tier:	2
	* Goals:	Scan,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Tags&InSystem_T2up;Amount&10;Analyzed&True

### qe_iyaFal_2023_daily_D_t2
	* Rewards:	Z3:10
	* ScheduleType:	Locked
	* XPMod:	30
	* EndOffset:	-7:0:0
	* EventId:	event_season_iyaFal_2023_t2
	* Tier:	2
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Tags&RareEarth_T2up;Amount&20;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_iyaFal_2023_daily_A_t3
	* Rewards:	Z3:10
	* ScheduleType:	Locked
	* XPMod:	90
	* EndOffset:	-7:0:0
	* EventId:	event_season_iyaFal_2023_t3
	* Tier:	3
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Ids&ShipsDestroyedP1T3_ShipsDestroyedP1T4;Amount&10

### qe_iyaFal_2023_daily_B_t3
	* Rewards:	Z3:10
	* ScheduleType:	Locked
	* XPMod:	90
	* EndOffset:	-7:0:0
	* EventId:	event_season_iyaFal_2023_t3
	* Tier:	3
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Id&CR;Amount&5000;ExcludedSources&BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

### qe_iyaFal_2023_daily_C_t3
	* Rewards:	Z3:10
	* ScheduleType:	Locked
	* XPMod:	90
	* EndOffset:	-7:0:0
	* EventId:	event_season_iyaFal_2023_t3
	* Tier:	3
	* Goals:	Scan,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Tags&InSystem_T3up;Amount&10;Analyzed&True

### qe_iyaFal_2023_daily_D_t3
	* Rewards:	Z3:10
	* ScheduleType:	Locked
	* XPMod:	90
	* EndOffset:	-7:0:0
	* EventId:	event_season_iyaFal_2023_t3
	* Tier:	3
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Tags&RareEarth_T3up;Amount&20;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_iyaFal_2023_daily_A_t4
	* Rewards:	Z3:10
	* ScheduleType:	Locked
	* XPMod:	270
	* EndOffset:	-7:0:0
	* EventId:	event_season_iyaFal_2023_t4
	* Tier:	4
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Ids&ShipsDestroyedP1T4;Amount&10

### qe_iyaFal_2023_daily_B_t4
	* Rewards:	Z3:10
	* ScheduleType:	Locked
	* XPMod:	270
	* EndOffset:	-7:0:0
	* EventId:	event_season_iyaFal_2023_t4
	* Tier:	4
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Id&CR;Amount&10000;ExcludedSources&BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

### qe_iyaFal_2023_daily_C_t4
	* Rewards:	Z3:10
	* ScheduleType:	Locked
	* XPMod:	270
	* EndOffset:	-7:0:0
	* EventId:	event_season_iyaFal_2023_t4
	* Tier:	4
	* Goals:	Scan,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Tags&InSystem_T4up;Amount&10;Analyzed&True

### qe_iyaFal_2023_daily_D_t4
	* Rewards:	Z3:10
	* ScheduleType:	Locked
	* XPMod:	270
	* EndOffset:	-7:0:0
	* EventId:	event_season_iyaFal_2023_t4
	* Tier:	4
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Tags&RareEarth_T4up;Amount&20;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_anniversary_2023_daily_A_t1
	* Rewards:	Z0:15
	* ScheduleType:	Locked
	* XPMod:	10
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t1
	* Tier:	1
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Amount&5;Tags&T1up;Mode&Generated

### qe_anniversary_2023_daily_B_t1
	* Rewards:	Z0:15
	* ScheduleType:	Locked
	* XPMod:	10
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t1
	* Tier:	1
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Tags&RareEarth_T1up;Amount&50;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_anniversary_2023_daily_A_t2
	* Rewards:	Z0:15
	* ScheduleType:	Locked
	* XPMod:	30
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t2
	* Tier:	2
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Amount&5;Tags&T2up;Mode&Generated

### qe_anniversary_2023_daily_B_t2
	* Rewards:	Z0:15
	* ScheduleType:	Locked
	* XPMod:	30
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t2
	* Tier:	2
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Tags&RareEarth_T2up;Amount&50;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_anniversary_2023_daily_A_t3
	* Rewards:	Z0:15
	* ScheduleType:	Locked
	* XPMod:	90
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t3
	* Tier:	3
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Amount&5;Tags&T3up;Mode&Generated

### qe_anniversary_2023_daily_B_t3
	* Rewards:	Z0:15
	* ScheduleType:	Locked
	* XPMod:	90
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t3
	* Tier:	3
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Tags&RareEarth_T3up;Amount&50;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_anniversary_2023_daily_A_t4
	* Rewards:	Z0:15
	* ScheduleType:	Locked
	* XPMod:	270
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t4
	* Tier:	4
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Amount&5;Tags&T4up;Mode&Generated

### qe_anniversary_2023_daily_B_t4
	* Rewards:	Z0:15
	* ScheduleType:	Locked
	* XPMod:	270
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t4
	* Tier:	4
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Tags&RareEarth_T4up;Amount&50;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_halloween_2023_daily_A_t1
	* Rewards:	Z0:5
	* ScheduleType:	Locked
	* XPMod:	5
	* EndOffset:	0:0:0
	* EventId:	event_halloween_2023_t1
	* Tier:	1
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Amount&1;Tags&ProgenitorInvasion_T1up;Mode&Generated

### qe_halloween_2023_daily_B_t1
	* Rewards:	Z0:5
	* ScheduleType:	Locked
	* XPMod:	10
	* EndOffset:	0:0:0
	* EventId:	event_halloween_2023_t1
	* Tier:	1
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Amount&2;Tags&ProgenitorInvasion_T1up;Mode&Generated

### qe_halloween_2023_daily_C_t1
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	15
	* EndOffset:	0:0:0
	* EventId:	event_halloween_2023_t1
	* Tier:	1
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Amount&5;Tags&ProgenitorInvasion_T1up;Mode&Generated

### qe_halloween_2023_daily_D_t1
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	20
	* EndOffset:	0:0:0
	* EventId:	event_halloween_2023_t1
	* Tier:	1
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Amount&10;Tags&ProgenitorInvasion_T1up;Mode&Generated

### qe_halloween_2023_daily_A_t2
	* Rewards:	Z0:5
	* ScheduleType:	Locked
	* XPMod:	15
	* EndOffset:	0:0:0
	* EventId:	event_halloween_2023_t2
	* Tier:	2
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Amount&1;Tags&ProgenitorInvasion_T2up;Mode&Generated

### qe_halloween_2023_daily_B_t2
	* Rewards:	Z0:5
	* ScheduleType:	Locked
	* XPMod:	30
	* EndOffset:	0:0:0
	* EventId:	event_halloween_2023_t2
	* Tier:	2
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Amount&2;Tags&ProgenitorInvasion_T2up;Mode&Generated

### qe_halloween_2023_daily_C_t2
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	45
	* EndOffset:	0:0:0
	* EventId:	event_halloween_2023_t2
	* Tier:	2
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Amount&5;Tags&ProgenitorInvasion_T2up;Mode&Generated

### qe_halloween_2023_daily_D_t2
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	60
	* EndOffset:	0:0:0
	* EventId:	event_halloween_2023_t2
	* Tier:	2
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Amount&10;Tags&ProgenitorInvasion_T2up;Mode&Generated

### qe_halloween_2023_daily_A_t3
	* Rewards:	Z0:5
	* ScheduleType:	Locked
	* XPMod:	45
	* EndOffset:	0:0:0
	* EventId:	event_halloween_2023_t3
	* Tier:	3
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Amount&1;Tags&ProgenitorInvasion_T3up;Mode&Generated

### qe_halloween_2023_daily_B_t3
	* Rewards:	Z0:5
	* ScheduleType:	Locked
	* XPMod:	90
	* EndOffset:	0:0:0
	* EventId:	event_halloween_2023_t3
	* Tier:	3
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Amount&2;Tags&ProgenitorInvasion_T3up;Mode&Generated

### qe_halloween_2023_daily_C_t3
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	135
	* EndOffset:	0:0:0
	* EventId:	event_halloween_2023_t3
	* Tier:	3
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Amount&5;Tags&ProgenitorInvasion_T3up;Mode&Generated

### qe_halloween_2023_daily_D_t3
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	180
	* EndOffset:	0:0:0
	* EventId:	event_halloween_2023_t3
	* Tier:	3
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Amount&10;Tags&ProgenitorInvasion_T3up;Mode&Generated

### qe_halloween_2023_daily_A_t4
	* Rewards:	Z0:5
	* ScheduleType:	Locked
	* XPMod:	135
	* EndOffset:	0:0:0
	* EventId:	event_halloween_2023_t4
	* Tier:	4
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Amount&1;Tags&ProgenitorInvasion_T4up;Mode&Generated

### qe_halloween_2023_daily_B_t4
	* Rewards:	Z0:5
	* ScheduleType:	Locked
	* XPMod:	270
	* EndOffset:	0:0:0
	* EventId:	event_halloween_2023_t4
	* Tier:	4
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Amount&2;Tags&ProgenitorInvasion_T4up;Mode&Generated

### qe_halloween_2023_daily_C_t4
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	405
	* EndOffset:	0:0:0
	* EventId:	event_halloween_2023_t4
	* Tier:	4
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Amount&5;Tags&ProgenitorInvasion_T4up;Mode&Generated

### qe_halloween_2023_daily_D_t4
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	540
	* EndOffset:	0:0:0
	* EventId:	event_halloween_2023_t4
	* Tier:	4
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Amount&10;Tags&ProgenitorInvasion_T4up;Mode&Generated

### qe_tanWin_2023_daily_A_t1
	* Rewards:	Z2:10
	* ScheduleType:	Hidden
	* XPMod:	10
	* EndOffset:	-2:0:0
	* EventId:	event_tanochWinter_2023_t1
	* Tier:	1
	* Goals:	Pay,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Id&questItem_progenitorRelic_t1;Amount&1

### qe_tanWin_2023_daily_B_t1
	* Rewards:	Z2:10
	* ScheduleType:	Hidden
	* XPMod:	10
	* EndOffset:	-2:0:0
	* EventId:	event_tanochWinter_2023_t1
	* Tier:	1
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Amount&5;Tags&T1up;Mode&Generated

### qe_tanWin_2023_daily_C_t1
	* Rewards:	Z2:10
	* ScheduleType:	Hidden
	* XPMod:	10
	* EndOffset:	-2:0:0
	* EventId:	event_tanochWinter_2023_t1
	* Tier:	1
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Category&Crafting;Tags&T1up;Amount&1

### qe_tanWin_2023_daily_D_t1
	* Rewards:	Z2:10
	* ScheduleType:	Hidden
	* XPMod:	10
	* EndOffset:	-2:0:0
	* EventId:	event_tanochWinter_2023_t1
	* Tier:	1
	* Goals:	UpgradeOfficer,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Amount&1

### qe_tanWin_2023_daily_A_t2
	* Rewards:	Z2:10
	* ScheduleType:	Hidden
	* XPMod:	30
	* EndOffset:	-2:0:0
	* EventId:	event_tanochWinter_2023_t2
	* Tier:	2
	* Goals:	Pay,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Id&questItem_progenitorRelic_t2;Amount&1

### qe_tanWin_2023_daily_B_t2
	* Rewards:	Z2:10
	* ScheduleType:	Hidden
	* XPMod:	30
	* EndOffset:	-2:0:0
	* EventId:	event_tanochWinter_2023_t2
	* Tier:	2
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Amount&5;Mode&Faction;Tags&T2up_Tanoch

### qe_tanWin_2023_daily_C_t2
	* Rewards:	Z2:10
	* ScheduleType:	Hidden
	* XPMod:	30
	* EndOffset:	-2:0:0
	* EventId:	event_tanochWinter_2023_t2
	* Tier:	2
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Category&Crafting;Tags&Part_T2up;Amount&100

### qe_tanWin_2023_daily_D_t2
	* Rewards:	Z2:10
	* ScheduleType:	Hidden
	* XPMod:	30
	* EndOffset:	-2:0:0
	* EventId:	event_tanochWinter_2023_t2
	* Tier:	2
	* Goals:	UpgradeOfficer,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Amount&2

### qe_tanWin_2023_daily_A_t3
	* Rewards:	Z2:10
	* ScheduleType:	Hidden
	* XPMod:	90
	* EndOffset:	-2:0:0
	* EventId:	event_tanochWinter_2023_t3
	* Tier:	3
	* Goals:	Pay,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Id&questItem_progenitorRelic_t3;Amount&1

### qe_tanWin_2023_daily_B_t3
	* Rewards:	Z2:10
	* ScheduleType:	Hidden
	* XPMod:	90
	* EndOffset:	-2:0:0
	* EventId:	event_tanochWinter_2023_t3
	* Tier:	3
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Amount&5;Mode&Faction;Tags&T3up_Tanoch

### qe_tanWin_2023_daily_C_t3
	* Rewards:	Z2:10
	* ScheduleType:	Hidden
	* XPMod:	90
	* EndOffset:	-2:0:0
	* EventId:	event_tanochWinter_2023_t3
	* Tier:	3
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Category&Crafting;Tags&Part_T3up;Amount&100

### qe_tanWin_2023_daily_D_t3
	* Rewards:	Z2:10
	* ScheduleType:	Hidden
	* XPMod:	90
	* EndOffset:	-2:0:0
	* EventId:	event_tanochWinter_2023_t3
	* Tier:	3
	* Goals:	UpgradeOfficer,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Amount&3

### qe_tanWin_2023_daily_A_t4
	* Rewards:	Z2:10
	* ScheduleType:	Hidden
	* XPMod:	270
	* EndOffset:	-2:0:0
	* EventId:	event_tanochWinter_2023_t4
	* Tier:	4
	* Goals:	Pay,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Id&questItem_progenitorRelic_t4;Amount&1

### qe_tanWin_2023_daily_B_t4
	* Rewards:	Z2:10
	* ScheduleType:	Hidden
	* XPMod:	270
	* EndOffset:	-2:0:0
	* EventId:	event_tanochWinter_2023_t4
	* Tier:	4
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Amount&5;Mode&Faction;Tags&T4up_Tanoch

### qe_tanWin_2023_daily_C_t4
	* Rewards:	Z2:10
	* ScheduleType:	Hidden
	* XPMod:	270
	* EndOffset:	-2:0:0
	* EventId:	event_tanochWinter_2023_t4
	* Tier:	4
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Category&Crafting;Tags&Part_T4up;Amount&100

### qe_tanWin_2023_daily_D_t4
	* Rewards:	Z2:10
	* ScheduleType:	Hidden
	* XPMod:	270
	* EndOffset:	-2:0:0
	* EventId:	event_tanochWinter_2023_t4
	* Tier:	4
	* Goals:	UpgradeOfficer,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Amount&5

### qe_nimbusTreasures_2024_daily_A_t1
	* Rewards:	Z0:10
	* ScheduleType:	Hidden
	* XPMod:	10
	* EndOffset:	0:0:0
	* EventId:	event_nimbusTreasures_2024_t1
	* Tier:	1
	* Goals:	ChargeScanner,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	NewCharge&1.5

### qe_nimbusTreasures_2024_daily_B_t1
	* Rewards:	Z0:10
	* ScheduleType:	Hidden
	* XPMod:	10
	* EndOffset:	0:0:0
	* EventId:	event_nimbusTreasures_2024_t1
	* Tier:	1
	* Goals:	Scan,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Tags&InSystem_Container_T1up;Amount&3;Analyzed&True

### qe_nimbusTreasures_2024_daily_C1_t1
	* Rewards:	Z0:4
	* ScheduleType:	Hidden
	* XPMod:	5
	* EndOffset:	0:0:0
	* EventId:	event_nimbusTreasures_2024_t1
	* Tier:	1
	* Goals:	Pay,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Id&questItem_alienProbe_t1;Amount&1

### qe_nimbusTreasures_2024_daily_C2_t1
	* Rewards:	Z0:8
	* ScheduleType:	Hidden
	* XPMod:	10
	* EndOffset:	0:0:0
	* EventId:	event_nimbusTreasures_2024_t1
	* Tier:	1
	* Goals:	Pay,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Id&questItem_alienProbe_t1;Amount&2

### qe_nimbusTreasures_2024_daily_C3_t1
	* Rewards:	Z0:12
	* ScheduleType:	Hidden
	* XPMod:	15
	* EndOffset:	0:0:0
	* EventId:	event_nimbusTreasures_2024_t1
	* Tier:	1
	* Goals:	Pay,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Id&questItem_alienProbe_t1;Amount&3

### qe_nimbusTreasures_2024_daily_C4_t1
	* Rewards:	Z0:16	battery_r:1
	* ScheduleType:	Hidden
	* XPMod:	20
	* EndOffset:	0:0:0
	* EventId:	event_nimbusTreasures_2024_t1
	* Tier:	1
	* Goals:	Pay,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Id&questItem_alienProbe_t1;Amount&4

### qe_nimbusTreasures_2024_daily_A_t2
	* Rewards:	Z0:10
	* ScheduleType:	Hidden
	* XPMod:	30
	* EndOffset:	0:0:0
	* EventId:	event_nimbusTreasures_2024_t2
	* Tier:	2
	* Goals:	ChargeScanner,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	NewCharge&1.5

### qe_nimbusTreasures_2024_daily_B_t2
	* Rewards:	Z0:10
	* ScheduleType:	Hidden
	* XPMod:	30
	* EndOffset:	0:0:0
	* EventId:	event_nimbusTreasures_2024_t2
	* Tier:	2
	* Goals:	Scan,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Tags&InSystem_Container_T2up;Amount&3;Analyzed&True

### qe_nimbusTreasures_2024_daily_C1_t2
	* Rewards:	Z0:4
	* ScheduleType:	Hidden
	* XPMod:	15
	* EndOffset:	0:0:0
	* EventId:	event_nimbusTreasures_2024_t2
	* Tier:	2
	* Goals:	Pay,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Id&questItem_alienProbe_t2;Amount&1

### qe_nimbusTreasures_2024_daily_C2_t2
	* Rewards:	Z0:8
	* ScheduleType:	Hidden
	* XPMod:	30
	* EndOffset:	0:0:0
	* EventId:	event_nimbusTreasures_2024_t2
	* Tier:	2
	* Goals:	Pay,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Id&questItem_alienProbe_t2;Amount&2

### qe_nimbusTreasures_2024_daily_C3_t2
	* Rewards:	Z0:12
	* ScheduleType:	Hidden
	* XPMod:	45
	* EndOffset:	0:0:0
	* EventId:	event_nimbusTreasures_2024_t2
	* Tier:	2
	* Goals:	Pay,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Id&questItem_alienProbe_t2;Amount&3

### qe_nimbusTreasures_2024_daily_C4_t2
	* Rewards:	Z0:16	battery_r:1
	* ScheduleType:	Hidden
	* XPMod:	60
	* EndOffset:	0:0:0
	* EventId:	event_nimbusTreasures_2024_t2
	* Tier:	2
	* Goals:	Pay,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Id&questItem_alienProbe_t2;Amount&4

### qe_nimbusTreasures_2024_daily_A_t3
	* Rewards:	Z0:10
	* ScheduleType:	Hidden
	* XPMod:	90
	* EndOffset:	0:0:0
	* EventId:	event_nimbusTreasures_2024_t3
	* Tier:	3
	* Goals:	ChargeScanner,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	NewCharge&1.5

### qe_nimbusTreasures_2024_daily_B_t3
	* Rewards:	Z0:10
	* ScheduleType:	Hidden
	* XPMod:	90
	* EndOffset:	0:0:0
	* EventId:	event_nimbusTreasures_2024_t3
	* Tier:	3
	* Goals:	Scan,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Tags&InSystem_Container_T3up;Amount&3;Analyzed&True

### qe_nimbusTreasures_2024_daily_C1_t3
	* Rewards:	Z0:4
	* ScheduleType:	Hidden
	* XPMod:	45
	* EndOffset:	0:0:0
	* EventId:	event_nimbusTreasures_2024_t3
	* Tier:	3
	* Goals:	Pay,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Id&questItem_alienProbe_t3;Amount&1

### qe_nimbusTreasures_2024_daily_C2_t3
	* Rewards:	Z0:8
	* ScheduleType:	Hidden
	* XPMod:	90
	* EndOffset:	0:0:0
	* EventId:	event_nimbusTreasures_2024_t3
	* Tier:	3
	* Goals:	Pay,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Id&questItem_alienProbe_t3;Amount&2

### qe_nimbusTreasures_2024_daily_C3_t3
	* Rewards:	Z0:12
	* ScheduleType:	Hidden
	* XPMod:	135
	* EndOffset:	0:0:0
	* EventId:	event_nimbusTreasures_2024_t3
	* Tier:	3
	* Goals:	Pay,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Id&questItem_alienProbe_t3;Amount&3

### qe_nimbusTreasures_2024_daily_C4_t3
	* Rewards:	Z0:16	battery_r:1
	* ScheduleType:	Hidden
	* XPMod:	180
	* EndOffset:	0:0:0
	* EventId:	event_nimbusTreasures_2024_t3
	* Tier:	3
	* Goals:	Pay,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Id&questItem_alienProbe_t3;Amount&4

### qe_nimbusTreasures_2024_daily_A_t4
	* Rewards:	Z0:10
	* ScheduleType:	Hidden
	* XPMod:	270
	* EndOffset:	0:0:0
	* EventId:	event_nimbusTreasures_2024_t4
	* Tier:	4
	* Goals:	ChargeScanner,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	NewCharge&1.5

### qe_nimbusTreasures_2024_daily_B_t4
	* Rewards:	Z0:10
	* ScheduleType:	Hidden
	* XPMod:	270
	* EndOffset:	0:0:0
	* EventId:	event_nimbusTreasures_2024_t4
	* Tier:	4
	* Goals:	Scan,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Tags&InSystem_Container_T4up;Amount&3;Analyzed&True

### qe_nimbusTreasures_2024_daily_C1_t4
	* Rewards:	Z0:4
	* ScheduleType:	Hidden
	* XPMod:	135
	* EndOffset:	0:0:0
	* EventId:	event_nimbusTreasures_2024_t4
	* Tier:	4
	* Goals:	Pay,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Id&questItem_alienProbe_t4;Amount&1

### qe_nimbusTreasures_2024_daily_C2_t4
	* Rewards:	Z0:8
	* ScheduleType:	Hidden
	* XPMod:	270
	* EndOffset:	0:0:0
	* EventId:	event_nimbusTreasures_2024_t4
	* Tier:	4
	* Goals:	Pay,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Id&questItem_alienProbe_t4;Amount&2

### qe_nimbusTreasures_2024_daily_C3_t4
	* Rewards:	Z0:12
	* ScheduleType:	Hidden
	* XPMod:	405
	* EndOffset:	0:0:0
	* EventId:	event_nimbusTreasures_2024_t4
	* Tier:	4
	* Goals:	Pay,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Id&questItem_alienProbe_t4;Amount&3

### qe_nimbusTreasures_2024_daily_C4_t4
	* Rewards:	Z0:16	battery_r:1
	* ScheduleType:	Hidden
	* XPMod:	540
	* EndOffset:	0:0:0
	* EventId:	event_nimbusTreasures_2024_t4
	* Tier:	4
	* Goals:	Pay,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Id&questItem_alienProbe_t4;Amount&4

### qe_yaoSpr_2024_daily_A_t1
	* Rewards:	Z1:10
	* ScheduleType:	Hidden
	* XPMod:	10
	* EndOffset:	-3:0:0
	* EventId:	event_yaotSpring_2024_t1
	* Tier:	1
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Ids&ShipsDestroyedP1T1_ShipsDestroyedP1T2_ShipsDestroyedP1T3_ShipsDestroyedP1T4;Amount&10

### qe_yaoSpr_2024_daily_A_t2
	* Rewards:	Z1:10
	* ScheduleType:	Hidden
	* XPMod:	30
	* EndOffset:	-3:0:0
	* EventId:	event_yaotSpring_2024_t2
	* Tier:	2
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Ids&ShipsDestroyedP1T2_ShipsDestroyedP1T3_ShipsDestroyedP1T4;Amount&10

### qe_yaoSpr_2024_daily_A_t3
	* Rewards:	Z1:10
	* ScheduleType:	Hidden
	* XPMod:	90
	* EndOffset:	-3:0:0
	* EventId:	event_yaotSpring_2024_t3
	* Tier:	3
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Ids&ShipsDestroyedP1T3_ShipsDestroyedP1T4;Amount&10

### qe_yaoSpr_2024_daily_A_t4
	* Rewards:	Z1:10
	* ScheduleType:	Hidden
	* XPMod:	270
	* EndOffset:	-3:0:0
	* EventId:	event_yaotSpring_2024_t4
	* Tier:	4
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Ids&ShipsDestroyedP1T4;Amount&10

### qe_yaoSpr_2024_daily_B_t1
	* Rewards:	Z1:10
	* ScheduleType:	Hidden
	* XPMod:	10
	* EndOffset:	-3:0:0
	* EventId:	event_yaotSpring_2024_t1
	* Tier:	1
	* Goals:	Scan,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Tags&InSystem_Container_T1up;Amount&1;Analyzed&True

### qe_yaoSpr_2024_daily_B_t2
	* Rewards:	Z1:10
	* ScheduleType:	Hidden
	* XPMod:	30
	* EndOffset:	-3:0:0
	* EventId:	event_yaotSpring_2024_t2
	* Tier:	2
	* Goals:	Scan,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Tags&InSystem_Container_T2up;Amount&1;Analyzed&True

### qe_yaoSpr_2024_daily_B_t3
	* Rewards:	Z1:10
	* ScheduleType:	Hidden
	* XPMod:	90
	* EndOffset:	-3:0:0
	* EventId:	event_yaotSpring_2024_t3
	* Tier:	3
	* Goals:	Scan,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Tags&InSystem_Container_T3up;Amount&1;Analyzed&True

### qe_yaoSpr_2024_daily_B_t4
	* Rewards:	Z1:10
	* ScheduleType:	Hidden
	* XPMod:	270
	* EndOffset:	-3:0:0
	* EventId:	event_yaotSpring_2024_t4
	* Tier:	4
	* Goals:	Scan,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Tags&InSystem_Container_T4up;Amount&1;Analyzed&True

### qe_yaoSpr_2024_daily_C_t1
	* Rewards:	Z1:10
	* ScheduleType:	Hidden
	* XPMod:	10
	* EndOffset:	-3:0:0
	* EventId:	event_yaotSpring_2024_t1
	* Tier:	1
	* Goals:	Pay,0	Pay,0	Pay,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Id&1N;Amount&100	Id&1O;Amount&100	Id&1P;Amount&100

### qe_yaoSpr_2024_daily_C_t2
	* Rewards:	Z1:10
	* ScheduleType:	Hidden
	* XPMod:	30
	* EndOffset:	-3:0:0
	* EventId:	event_yaotSpring_2024_t2
	* Tier:	2
	* Goals:	Pay,0	Pay,0	Pay,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Id&2N;Amount&100	Id&2O;Amount&100	Id&2P;Amount&100

### qe_yaoSpr_2024_daily_C_t3
	* Rewards:	Z1:10
	* ScheduleType:	Hidden
	* XPMod:	90
	* EndOffset:	-3:0:0
	* EventId:	event_yaotSpring_2024_t3
	* Tier:	3
	* Goals:	Pay,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Id&yao_collectable_u_01;Amount&1

### qe_yaoSpr_2024_daily_C_t4
	* Rewards:	Z1:10
	* ScheduleType:	Hidden
	* XPMod:	270
	* EndOffset:	-3:0:0
	* EventId:	event_yaotSpring_2024_t4
	* Tier:	4
	* Goals:	Pay,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Id&yao_collectable_u_01;Amount&3

### qe_yaoSpr_2024_daily_D_t1
	* Rewards:	Z1:10
	* ScheduleType:	Hidden
	* XPMod:	10
	* EndOffset:	-3:0:0
	* EventId:	event_yaotSpring_2024_t1
	* Tier:	1
	* Goals:	Scan,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Tags&InSystem_Generated_T1up;Amount&5;Analyzed&True

### qe_yaoSpr_2024_daily_D_t2
	* Rewards:	Z1:10
	* ScheduleType:	Hidden
	* XPMod:	30
	* EndOffset:	-3:0:0
	* EventId:	event_yaotSpring_2024_t2
	* Tier:	2
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Id&RP;Amount&400;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_yaoSpr_2024_daily_D_t3
	* Rewards:	Z1:10
	* ScheduleType:	Hidden
	* XPMod:	90
	* EndOffset:	-3:0:0
	* EventId:	event_yaotSpring_2024_t3
	* Tier:	3
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Id&RP;Amount&400;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_yaoSpr_2024_daily_D_t4
	* Rewards:	Z1:10
	* ScheduleType:	Hidden
	* XPMod:	270
	* EndOffset:	-3:0:0
	* EventId:	event_yaotSpring_2024_t4
	* Tier:	4
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Id&RP;Amount&400;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

## ql_main_t0_jolja

### qm_t0_Jolja
	* Rewards:	0A:400	unlockToken_changeKiith:1
	* XPMod:	5
	* Tier:	0
	* Goals:	Goto,0	Scan,1	CompleteMission,2	Goto,3
	* Type:	Main
	* ReplayMissionId:	story_A05_Jolja	story_A05_Jolja_heroic
	* GoalParameters:	Target&[-1764, -703]	Tags&InSystem;Amount&1	Id&story_A05_Jolja	Target&[-1822, -636];TargetMode&Station
	* FollowUpLines:	ql_main_t0_setupPlayer

## ql_main_t0_setupPlayer

### qm_t0_pickKiith
	* Rewards:	rw_recruitToken_hiig_random:1	premium_token_manual_weeks_1:1	unlockToken_changeName:1
	* XPMod:	5
	* Tier:	0
	* Goals:	SelectKiith,0
	* Type:	Main

### qm_t0_pickName
	* Rewards:	rp_catExpl_hyperCap_t1_c:1	HC:20	unlockToken_chat:1
	* XPMod:	5
	* Tier:	0
	* Goals:	ChangeName,0
	* Type:	Main
	* FollowUpLines:	ql_main_t1_newOres:ql_main_t0_joinClan

## ql_main_t0_joinClan

### qm_t0_joinClan
	* Rewards:	HC:20
	* XPMod:	5
	* Tier:	0
	* Goals:	JoinClan,0
	* Type:	Main

## ql_main_t1_newOres

### qm_t1_newOres
	* Rewards:	1A:500	unlockToken_refinery:1
	* XPMod:	15
	* Tier:	1
	* Goals:	Goto,0	Statistic,1	Statistic,2
	* Type:	Main
	* GoalParameters:	Target&[-1793, -424]	Id&ScannedBelt;Total&6	Ids&Mined1A_Mined1B_Mined1C;Amount&200
	* FollowUpLines:	ql_esca_mineT1

### qm_t1_introRefining
	* Rewards:	1B:500
	* XPMod:	15
	* Tier:	1
	* Goals:	Statistic,0	Goto,1
	* Type:	Main
	* FollowUps:	qm_t1_facHiigaran_A:qm_t1_facHiigaran_B:qm_t1_facHiigaran_C:qm_t1_facHiigaran_D
	* GoalParameters:	Ids&Refining1N_Refining1O_Refining1P;Amount&100	Target&[-1822, -636];TargetMode&Station
	* FollowUpLines:	ql_main_t1_sideHiig

## ql_main_t1_sideHiig

### qm_t1_facHiigaran
	* Rewards:	bp_hgn_sf_intc_01_t1:1	bp_hgn_sf_plbo_01_t1:1
	* XPMod:	15
	* Tier:	1
	* Goals:	CompleteQuest,0	Goto,1
	* Type:	Main
	* GoalParameters:	Amount&3;Ids&qm_t1_facHiigaran_A|qm_t1_facHiigaran_B|qm_t1_facHiigaran_C|qm_t1_facHiigaran_D	Target&[-1822, -636];TargetMode&Station
	* FollowUpLines:	ql_main_t1_strikeCraft

## ql_main_t1_strikeCraft

### qm_t1_strikeCraft
	* Rewards:	bp_hgn_su_rcol_01_t1:1
	* XPMod:	15
	* Tier:	1
	* Goals:	Craft,0	Craft,0	Equip,1	Equip,1
	* Type:	Main
	* GoalParameters:	Category&Crafting;Tags&Interceptor_T1;Amount&1	Category&Crafting;Tags&PlasmaBomber_T1;Amount&1	Type&Squad;Tags&Interceptor_T1up	Type&Squad;Tags&PlasmaBomber_T1up
	* FollowUpLines:	ql_main_t1_advCombat_01:ql_main_t1_RCol

## ql_main_t1_RCol

### qm_t1_RColEquip
	* Rewards:	CR:1000	0A:500
	* XPMod:	15
	* Tier:	1
	* Goals:	Craft,0	Equip,1
	* Type:	Main
	* GoalParameters:	Category&Crafting;Tags&RCol_T1;Amount&1	Type&Squad;Tags&RCol_T1up

### qm_t1_RColMine
	* Rewards:	1C:500
	* XPMod:	15
	* Tier:	1
	* Goals:	Statistic,0
	* Type:	Main
	* GoalParameters:	Ids&Mined1A_Mined1B_Mined1C;Amount&4500

## ql_main_t1_advCombat_01

### qm_t1_advCombat_01
	* Rewards:	1A:500
	* XPMod:	15
	* Tier:	1
	* Goals:	CompleteMission,0
	* Type:	Main
	* ReplayMissionId:	story_B01_CombatTrials	story_B01_CombatTrials_heroic
	* GoalParameters:	Id&story_B01_CombatTrials

### qm_t1_killEnemyShips
	* Rewards:	CR:2000	insig_r1:10
	* XPMod:	15
	* Tier:	1
	* Goals:	Statistic,0
	* Type:	Main
	* GoalParameters:	Id&ShipsDestroyed;Amount&25
	* FollowUpLines:	ql_main_t1_promoteOfficer

## ql_main_t1_promoteOfficer

### qm_t1_introPromoteOfficer
	* Rewards:	bp_hgn_cf_assa_01_t1:1	insig_r1:5
	* XPMod:	15
	* Tier:	1
	* Goals:	UpgradeOfficer,0
	* Type:	Main
	* GoalParameters:	Amount&1
	* FollowUpLines:	ql_main_t1_escorts

### qm_t1_rankUpOfficer
	* Rewards:	rw_recruitToken_hiig_minUncommon:1
	* XPMod:	15
	* Tier:	1
	* Goals:	UpgradeOfficer,0
	* Type:	Side
	* GoalParameters:	Amount&1;MinLevel&10

## ql_main_t1_escorts

### qm_t1_escort
	* Rewards:	bp_hgn_cf_scou_01_t1:1	1B: 500
	* XPMod:	15
	* Tier:	1
	* Goals:	Craft,0	Equip,1
	* Type:	Main
	* GoalParameters:	Category&Crafting;Tags&AssaultFrigate_T1;Amount&1	Type&Escort;Tags&AssaultFrigate_T1up
	* FollowUpLines:	ql_main_t1_advCombat_02

## ql_main_t1_advCombat_02

### qm_t1_advCombat_02
	* Rewards:	bp_hgn_sc_assa_01_t1:1
	* XPMod:	15
	* Tier:	1
	* Goals:	CompleteMission,0
	* Type:	Main
	* ReplayMissionId:	story_B02_MeropisDefense	story_B02_MeropisDefense_heroic
	* GoalParameters:	Id&story_B02_MeropisDefense

### qm_t1_doSignals
	* Rewards:	CR:1500
	* XPMod:	15
	* Tier:	1
	* Goals:	CompleteMission,0
	* Type:	Main
	* FollowUps:	qm_t1_facCangacian_A:qm_t1_facCangacian_B:qm_t1_facCangacian_C:qm_t1_facCangacian_D
	* GoalParameters:	Mode&Generated;Amount&1;Tier&1
	* FollowUpLines:	ql_main_t1_sideCang:ql_esca_killPirate1

## ql_main_t1_sideCang

### qm_t1_facCangacian
	* Rewards:	bp_hgn_fs_expl_01_t1:1
	* XPMod:	15
	* Tier:	1
	* Goals:	CompleteQuest,0	Goto,1
	* Type:	Main
	* GoalParameters:	Amount&3;Ids&qm_t1_facCangacian_A|qm_t1_facCangacian_B|qm_t1_facCangacian_C|qm_t1_facCangacian_D	Target&[-1822, -636];TargetMode&Station
	* FollowUpLines:	ql_main_t1_flagship

## ql_main_t1_flagship

### qm_t1_introCraftFlagship
	* Rewards:	insig_r1:10
	* XPMod:	15
	* Tier:	1
	* Goals:	StartCraft,0
	* Type:	Main
	* GoalParameters:	Category&Crafting;Tags&Flagship_Ship;Amount&1
	* FollowUpLines:	ql_main_t1_killCangacians

### qm_t1_introEquipFlagship
	* Rewards:	1C:500
	* XPMod:	15
	* Tier:	1
	* Goals:	Craft,0	Equip,1	Equip,2	Equip,2	Equip,2
	* Type:	Main
	* GoalParameters:	Category&Crafting;Tags&Flagship_Ship;Amount&1	Type&Flagship	Type&Squad	Type&Escort	Type&Officer;Location&Bridge
	* FollowUpLines:	ql_main_t1_advCombat_03

## ql_main_t1_killCangacians

### qm_t1_killCangacians
	* Rewards:	CR:1000
	* XPMod:	15
	* Tier:	1
	* Goals:	Statistic,0
	* Type:	Side
	* GoalParameters:	Id&ShipsDestroyedP1;Amount&20

## ql_main_t1_advCombat_03

### qm_t1_advCombat_03
	* Rewards:	rw_recruitToken_hiig_random:1
	* XPMod:	15
	* Tier:	1
	* Goals:	CompleteMission,0
	* Type:	Main
	* ReplayMissionId:	story_B03_ThePool	story_B03_ThePool_heroic
	* GoalParameters:	Id&story_B03_ThePool

### qm_t1_killProgenitors
	* Rewards:	bp_turret_hgn_kinetic_fs_s_01_t1:1	insig_r1:10	unlockToken_externalModules:1
	* XPMod:	15
	* Tier:	1
	* Goals:	Statistic,0
	* Type:	Main
	* GoalParameters:	Id&ShipsDestroyedProgenitor;Amount&10
	* FollowUpLines:	ql_main_t1_turrets

## ql_main_t1_turrets

### qm_t1_craftTurret
	* Rewards:	1B:500
	* XPMod:	15
	* Tier:	1
	* Goals:	Craft,0
	* Type:	Main
	* GoalParameters:	Category&Crafting;Tags&Weapon_Module_T1;Amount&1

### qm_t1_mountTurret
	* Rewards:	bp_turret_hgn_missile_fs_s_02_t1:1	1A:500
	* XPMod:	15
	* Tier:	1
	* Goals:	Equip,0
	* Type:	Main
	* GoalParameters:	Type&Weapon
	* FollowUpLines:	ql_main_t1_upgrades

## ql_main_t1_upgrades

### qm_t1_rareEarths
	* Rewards:	AA:10	AB:5
	* XPMod:	15
	* Tier:	1
	* Goals:	GainItem,0
	* Type:	Main
	* GoalParameters:	Tags&RareEarth;Amount&5;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qm_t1_upgradeTurret
	* Rewards:	bp_turret_hgn_kinetic_fs_m_02_t1:1	CR:1000
	* XPMod:	15
	* Tier:	1
	* Goals:	Craft,0
	* Type:	Main
	* FollowUps:	qm_t1_facProgenitors_A:qm_t1_facProgenitors_B:qm_t1_facProgenitors_C:qm_t1_facProgenitors_D
	* GoalParameters:	Category&Upgrade;Tags&Weapon_Module;Amount&1
	* FollowUpLines:	ql_main_t1_sideProg

### qm_t1_upgradeTurret_3
	* Rewards:	1A:1500
	* XPMod:	15
	* Tier:	1
	* Goals:	Craft,0
	* Type:	Side
	* GoalParameters:	Category&Upgrade;Tags&Weapon_Module;Amount&1;MinLevel&3

### qm_t1_upgradeTurret_4
	* Rewards:	1A:1500	1B:1500
	* XPMod:	15
	* Tier:	1
	* Goals:	Craft,0
	* Type:	Side
	* GoalParameters:	Category&Upgrade;Tags&Weapon_Module;Amount&1;MinLevel&4

### qm_t1_upgradeTurret_5
	* Rewards:	1A:2000	1B:2000	1C:2000
	* XPMod:	15
	* Tier:	1
	* Goals:	Craft,0
	* Type:	Side
	* GoalParameters:	Category&Upgrade;Tags&Weapon_Module;Amount&1;MinLevel&5

### qm_t1_upgradeTurret_6
	* Rewards:	insig_r1:100
	* XPMod:	15
	* Tier:	1
	* Goals:	Craft,0
	* Type:	Side
	* GoalParameters:	Category&Upgrade;Tags&Weapon_Module;Amount&1;MinLevel&6

### qm_t1_upgradeTurret_7
	* Rewards:	rw_recruitToken_hiig_random:1
	* XPMod:	15
	* Tier:	1
	* Goals:	Craft,0
	* Type:	Side
	* GoalParameters:	Category&Upgrade;Tags&Weapon_Module;Amount&1;MinLevel&7

### qm_t1_upgradeTurret_8
	* Rewards:	rw_recruitToken_hiig_minUncommon:1
	* XPMod:	15
	* Tier:	1
	* Goals:	Craft,0
	* Type:	Side
	* GoalParameters:	Category&Upgrade;Tags&Weapon_Module;Amount&1;MinLevel&8

### qm_t1_upgradeTurretMax
	* Rewards:	rw_recruitToken_hiig_minRare:1
	* XPMod:	15
	* Tier:	1
	* Goals:	Craft,0
	* Type:	Side
	* GoalParameters:	Category&Upgrade;Tags&Weapon_Module;Amount&1;MinLevel&9

## ql_main_t1_sideProg

### qm_t1_facProgenitors
	* Rewards:	bp_sensor_hgn_s_01_t1:1	0A: 500
	* XPMod:	15
	* Tier:	1
	* Goals:	CompleteQuest,0	Goto,1
	* Type:	Main
	* GoalParameters:	Amount&3;Ids&qm_t1_facProgenitors_A|qm_t1_facProgenitors_B|qm_t1_facProgenitors_C|qm_t1_facProgenitors_D	Target&[-1822, -636];TargetMode&Station
	* FollowUpLines:	ql_main_t1_scanner

## ql_main_t1_scanner

### qm_t1_scannerModule
	* Rewards:	bp_hgn_sf_plbo_01_u_t1:1	CR:1000	battery_e:1
	* XPMod:	15
	* Tier:	1
	* Goals:	Craft,0	Equip,1
	* Type:	Main
	* GoalParameters:	Category&Crafting;Tags&Sensor_Module_T1;Amount&1	Type&Sensor;Tags&T1up
	* FollowUpLines:	ql_main_t2_strike:ql_esca_scan:ql_main_t1_scannerCharge

## ql_main_t1_scannerCharge

### qm_t1_scannerOvercharge
	* Rewards:	battery_c:3
	* XPMod:	15
	* Tier:	1
	* Goals:	ChargeScanner,0	Scan,1
	* Type:	Side
	* GoalParameters:	NewCharge&1.25	Tags&InSystem_Rare;Amount&1

## ql_main_t2_strike

### qm_t2_findPirateHideout
	* Rewards:	bp_turret_hgn_missile_fs_s_02_u_t1:1	1C:500	unlockToken_liaisonOffice:1
	* XPMod:	15
	* Tier:	1
	* Goals:	Scan,0	Goto,0
	* Type:	Main
	* GoalParameters:	Tags&InGalaxy_T1up;Amount&1;Analyzed&True	Target&[-1793, -424]
	* FollowUpLines:	ql_raid_013:ql_main_t1_upgradeExternals:ql_main_t1_introLiaison

### qm_t2_strikePirateHideout
	* Rewards:	rw_recruitToken_hiig_random:1
	* XPMod:	15
	* Tier:	1
	* Goals:	CompleteQuest,0
	* Type:	Main
	* GoalParameters:	Ids&qr_013;Amount&1

## ql_main_t1_upgradeExternals

### qm_t1_upgradeModules
	* Rewards:	bp_im_factory_01_t1:1	insig_r1:10	unlockToken_internalModules:1
	* XPMod:	15
	* Tier:	1
	* Goals:	Craft,0	Craft,0
	* Type:	Main
	* GoalParameters:	Category&Upgrade;Tags&Sensor;Amount&1;MinLevel&5	Category&Upgrade;Tags&Engine;Amount&1;MinLevel&5
	* FollowUpLines:	ql_main_t1_introInternals

## ql_main_t1_introLiaison

### qm_t1_introLiaison
	* Rewards:	1B:250	1A:250
	* XPMod:	15
	* Tier:	1
	* Goals:	CompleteQuest,0
	* Type:	Side
	* GoalParameters:	Amount&3;Tags&Faction

## ql_main_t1_introInternals

### qm_t1_introInternals
	* Rewards:	bp_im_refinery_01_t1:1	0A:2000	1B:1000
	* XPMod:	15
	* Tier:	1
	* Goals:	Craft,0	Equip,1
	* Type:	Main
	* GoalParameters:	Tags&Crafting_Factory	Type&Internal;Tags&Crafting_Factory

### qm_t1_upgradeInternals
	* Rewards:	bp_hgn_cf_assa_01_u_t1:1	1A:1000	1C:1000
	* XPMod:	15
	* Tier:	1
	* Goals:	Craft,0
	* Type:	Main
	* FollowUps:	qm_t1_facIyatequa_A:qm_t1_facIyatequa_B:qm_t1_facIyatequa_C:qm_t1_facIyatequa_D
	* GoalParameters:	Category&Upgrade;Tags&Factory;MinLevel&2
	* FollowUpLines:	ql_main_t1_sideIyat

## ql_main_t1_sideIyat

### qm_t1_facIyatequa
	* Rewards:	bp_turret_hgn_kinetic_fs_m_02_u_t1:1	AA:25	unlockToken_research:1
	* XPMod:	15
	* Tier:	1
	* Goals:	CompleteQuest,0	Goto,1
	* Type:	Main
	* GoalParameters:	Amount&3;Ids&qm_t1_facIyatequa_A|qm_t1_facIyatequa_B|qm_t1_facIyatequa_C|qm_t1_facIyatequa_D	Target&[-1822, -636];TargetMode&Station
	* FollowUpLines:	ql_main_t2_research

## ql_main_t2_research

### qm_t2_introRP
	* Rewards:	rp_catExpl_hyperCap_t2:1	RP:15	AB:5
	* XPMod:	45
	* Tier:	2
	* Goals:	GainItem,0
	* Type:	Main
	* GoalParameters:	Id&RP;Amount&15;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qm_t2_introResearch
	* Rewards:	CR:5000
	* XPMod:	45
	* Tier:	2
	* Goals:	Craft,0
	* Type:	Main
	* GoalParameters:	Category&Research;Id&rp_catExpl_hyperCap_t2_c;Tags&T2
	* FollowUpLines:	ql_main_t2_newResources

## ql_main_t2_newResources

### qm_t2_newResources
	* Rewards:	2A:750
	* XPMod:	45
	* Tier:	2
	* Goals:	Goto,0	Statistic,1	Statistic,2	Craft,3	Goto,4
	* Type:	Main
	* FollowUps:	qm_t2_facCangacian_A:qm_t2_facCangacian_B:qm_t2_facCangacian_C:qm_t2_facCangacian_D
	* GoalParameters:	Target&[-1491, -596]	Id&ScannedBelt;Total&25	Ids&Mined2A_Mined2B_Mined2C_Mined2D;Amount&3000	Category&Refining;Amount&1500;Tags&T2	Target&[-1822, -636];TargetMode&Station
	* FollowUpLines:	ql_main_t2_sideCang

## ql_main_t2_sideCang

### qm_t2_facCangacian
	* Rewards:	rp_catStrCraft_bp_sf_intc_t2:1	BA:20	BB:5
	* XPMod:	45
	* Tier:	2
	* Goals:	CompleteQuest,0	Goto,1
	* Type:	Main
	* GoalParameters:	Amount&3;Ids&qm_t2_facCangacian_A|qm_t2_facCangacian_B|qm_t2_facCangacian_C|qm_t2_facCangacian_D	Target&[-1822, -636];TargetMode&Station
	* FollowUpLines:	ql_main_t2_strikeCraftResearch

## ql_main_t2_strikeCraftResearch

### qm_t2_startResearchT2Intc
	* Rewards:	0A:500	1A:500
	* XPMod:	45
	* Tier:	2
	* Goals:	StartCraft,0
	* Type:	Main
	* GoalParameters:	Category&Research;Id&rp_catStrCraft_bp_sf_intc_t2_c
	* FollowUpLines:	ql_main_t2_strikeCraftCraft

### qm_t2_finResearchT2Intc
	* Rewards:	2C: 750
	* XPMod:	45
	* Tier:	2
	* Goals:	Craft,0
	* Type:	Main
	* GoalParameters:	Category&Research;Id&rp_catStrCraft_bp_sf_intc_t2_c

## ql_main_t2_strikeCraftCraft

### qm_t2_introParts
	* Rewards:	2A:750
	* XPMod:	45
	* Tier:	2
	* Goals:	Buy,0	Craft,1
	* Type:	Main
	* GoalParameters:	Id&bp_intmed_ship_small_t2	Tags&Part_Ship_S_T2;Amount&400;Category&Crafting

### qm_t2_strikeCraft
	* Rewards:	1B:500	1C:500
	* XPMod:	45
	* Tier:	2
	* Goals:	CompleteQuest,0	Craft,1
	* Type:	Main
	* FollowUps:	qm_t2_facHiigaran_A:qm_t2_facHiigaran_B:qm_t2_facHiigaran_C:qm_t2_facHiigaran_D
	* GoalParameters:	Ids&qm_t2_finResearchT2Intc;Amount&1	Category&Crafting;Tags&Interceptor_T2;Amount&1
	* FollowUpLines:	ql_main_t2_sideHiig:ql_main_t2_RCol:ql_raid_016

## ql_main_t2_sideHiig

### qm_t2_facHiigaran
	* Rewards:	rp_catEscorts_bp_cf_assa_t2:1	insig_r2:15
	* XPMod:	45
	* Tier:	2
	* Goals:	CompleteQuest,0
	* Type:	Main
	* GoalParameters:	Amount&3;Ids&qm_t2_facHiigaran_A|qm_t2_facHiigaran_B|qm_t2_facHiigaran_C|qm_t2_facHiigaran_D
	* FollowUpLines:	ql_main_t2_researchEscort

## ql_main_t2_RCol

### qm_t2_craftRCol
	* Rewards:	0A:500	1B:500
	* XPMod:	45
	* Tier:	2
	* Goals:	Craft,0
	* Type:	Side
	* GoalParameters:	Category&Crafting;Tags&RCol_T2;Amount&1

### qm_t2_RColMining
	* Rewards:	bp_hgn_cu_rcon_01_t1:1	2B:750
	* XPMod:	45
	* Tier:	2
	* Goals:	Statistic,0
	* Type:	Side
	* GoalParameters:	Ids&Mined2A_Mined2B_Mined2C_Mined2D;Amount&9000
	* FollowUpLines:	ql_main_t2_RCon

## ql_main_t2_RCon

### qm_t2_craftRCon
	* Rewards:	1C:500	1A:500
	* XPMod:	45
	* Tier:	2
	* Goals:	Craft,0
	* Type:	Side
	* GoalParameters:	Category&Crafting;Tags&RCon;Amount&1

### qm_t2_introIdleMine
	* Rewards:	insig_r2:10	rw_recruitToken_hiig_random:1
	* XPMod:	45
	* Tier:	2
	* Goals:	Statistic,0
	* Type:	Side
	* GoalParameters:	Ids&IdleMined;Amount&5000

## ql_main_t2_researchEscort

### qm_t2_startResearchT2Frig
	* Rewards:	insig_r1:10	CR:3000
	* XPMod:	45
	* Tier:	2
	* Goals:	StartCraft,0
	* Type:	Main
	* GoalParameters:	Category&Research;Id&rp_catEscorts_bp_cf_assa_t2_c
	* FollowUpLines:	ql_main_t2_oreD

### qm_t2_finResearchT2Frig
	* Rewards:	2C:750
	* XPMod:	45
	* Tier:	2
	* Goals:	Craft,0
	* Type:	Main
	* GoalParameters:	Category&Research;Id&rp_catEscorts_bp_cf_assa_t2_c
	* FollowUpLines:	ql_main_t2_craftEscort:ql_main_t2_researchPulsarCorvette

## ql_main_t2_oreD

### qm_t2_introOreD
	* Rewards:	bp_hgn_sf_intc_01_u_t2:1	2D:300
	* XPMod:	45
	* Tier:	2
	* Goals:	Statistic,0	Craft,1
	* Type:	Side
	* GoalParameters:	Id&Mined2D;Amount&3500	Category&Refining;Amount&1500;Id&2Q

### qm_t2_craftUncShip
	* Rewards:	2A:750
	* XPMod:	45
	* Tier:	2
	* Goals:	Craft,0
	* Type:	Side
	* GoalParameters:	Id&hgn_sf_intc_01_u_t2

## ql_main_t2_researchPulsarCorvette

### qm_t2_researchPulsarCorvette
	* Rewards:	insig_r1:10
	* XPMod:	45
	* Tier:	2
	* Goals:	Craft,0
	* Type:	Side
	* GoalParameters:	Category&Research;Id&rp_catStrCraft_bp_sc_puls_t2_c;MinLevel&1
	* FollowUpLines:	ql_main_t2_pulsarCorvette

## ql_main_t2_pulsarCorvette

### qm_t2_pulsarCorvette
	* Rewards:	insig_r2:10
	* XPMod:	45
	* Tier:	2
	* Goals:	Craft,0
	* Type:	Side
	* GoalParameters:	Category&Crafting;Tags&PulsarCorvette_T2;Amount&1

## ql_main_t2_craftEscort

### qm_t2_largeHullParts
	* Rewards:	0A:500	1C:500
	* XPMod:	45
	* Tier:	2
	* Goals:	Buy,0	Craft,1
	* Type:	Main
	* GoalParameters:	Id&bp_intmed_ship_large_t2	Tags&Part_Ship_L_T2;Amount&400;Category&Crafting

### qm_t2_escort
	* Rewards:	CR:5000	unlockToken_liaisonOffice:1
	* XPMod:	45
	* Tier:	2
	* Goals:	Craft,0
	* Type:	Main
	* GoalParameters:	Category&Crafting;Tags&AssaultFrigate_T2;Amount&1
	* FollowUpLines:	ql_main_t2_introLiaison:ql_main_t2_strikeStationDefense:ql_raid_014

## ql_main_t2_introLiaison

### qm_t2_introLiaison
	* Rewards:	1B:500	1A:500
	* XPMod:	45
	* Tier:	2
	* Goals:	CompleteQuest,0
	* Type:	Main
	* FollowUps:	qm_t2_facIyatequa_A:qm_t2_facIyatequa_B:qm_t2_facIyatequa_C:qm_t2_facIyatequa_D
	* GoalParameters:	Amount&3;Tags&Faction
	* FollowUpLines:	ql_main_t2_sideIyat

## ql_main_t2_sideIyat

### qm_t2_facIyatequa
	* Rewards:	BA:20	BB:5
	* XPMod:	45
	* Tier:	2
	* Goals:	CompleteQuest,0	Goto,1
	* Type:	Main
	* GoalParameters:	Amount&3;Ids&qm_t2_facIyatequa_A|qm_t2_facIyatequa_B|qm_t2_facIyatequa_C|qm_t2_facIyatequa_D	Target&[-1822, -636];TargetMode&Station
	* FollowUpLines:	ql_main_t2_largeWpnParts:ql_main_t2_largeMchParts

## ql_main_t2_strikeStationDefense

### qm_t2_strikeStationDefense
	* Rewards:	rw_recruitToken_hiig_random:1
	* XPMod:	45
	* Tier:	2
	* Goals:	CompleteQuest,0
	* Type:	Side
	* GoalParameters:	Ids&qr_014;Amount&1

## ql_main_t2_largeWpnParts

### qm_t2_liaisonTanoch
	* Rewards:	0A:500	CR:3000
	* XPMod:	45
	* Tier:	2
	* Goals:	CompleteQuest,0
	* Type:	Main
	* GoalParameters:	Amount&10;Tags&Faction_Tanoch_T2up

### qm_t2_largeWeaponParts
	* Rewards:	2C:750
	* XPMod:	45
	* Tier:	2
	* Goals:	Craft,0
	* Type:	Main
	* GoalParameters:	Tags&Part_Weapon_L_T2;Amount&100;Category&Crafting
	* FollowUpLines:	ql_main_t2_flagship

## ql_main_t2_largeMchParts

### qm_t2_liaisonIyatequa
	* Rewards:	1A:500	1B:500
	* XPMod:	45
	* Tier:	2
	* Goals:	CompleteQuest,0
	* Type:	Main
	* GoalParameters:	Amount&10;Tags&Faction_Tr1_T2up

### qm_t2_largeMachineParts
	* Rewards:	2A:750
	* XPMod:	45
	* Tier:	2
	* Goals:	Craft,0
	* Type:	Main
	* GoalParameters:	Tags&Part_Module_L_T2;Amount&100;Category&Crafting
	* FollowUpLines:	ql_main_t2_flagship

## ql_main_t2_flagship

### qm_t2_startCraftFlagship
	* Rewards:	1C:500	CR:3000
	* XPMod:	45
	* Tier:	2
	* Goals:	CompleteQuest,0	StartCraft,1
	* Type:	Main
	* GoalParameters:	Amount&2;Ids&qm_t2_largeWeaponParts|qm_t2_largeMachineParts	Category&Crafting;Tags&Flagship_Ship_T2
	* FollowUpLines:	ql_Keid:ql_main_t2_strikePahrasRock:ql_raid_015

### qm_t2_finCraftFlagship
	* Rewards:	rp_catTurrets1_bp_kinetic_t2:1	2B:750
	* XPMod:	45
	* Tier:	2
	* Goals:	Craft,0
	* Type:	Main
	* GoalParameters:	Category&Crafting;Tags&Flagship_Ship_T2
	* FollowUpLines:	ql_main_t2_tanochet:ql_main_t2_turrets

## ql_main_t2_strikePahrasRock

### qm_t2_strikePahrasRock
	* Rewards:	rw_recruitToken_hiig_random:1
	* XPMod:	45
	* Tier:	2
	* Goals:	CompleteQuest,0
	* Type:	Side
	* GoalParameters:	Ids&qr_015;Amount&1

## ql_main_t2_turrets

### qm_t2_turrets
	* Rewards:	2C:750
	* XPMod:	45
	* Tier:	2
	* Goals:	Craft,0	Craft,1	Equip,2
	* Type:	Side
	* GoalParameters:	Category&Research;Id&rp_catTurrets1_bp_kinetic_t2_c	Category&Crafting;Tags&Weapon_Module_T2;Amount&1	Type&Weapon;Tags&T2up

## ql_main_t2_tanochet

### qm_t2_tanochet
	* Rewards:	bp_tan_sc_miss_01_fu_t2:1	insig_r1:15	insig_r2:15
	* XPMod:	45
	* Tier:	2
	* Goals:	CompleteMission,0
	* Type:	Main
	* FollowUps:	qm_t2_facTanoch_A:qm_t2_facTanoch_B:qm_t2_facTanoch_C:qm_t2_facTanoch_D
	* ReplayMissionId:	story_C01_Tanochet	story_C01_Tanochet_heroic
	* CinematicIds:	30
	* GoalParameters:	Id&story_C01_Tanochet
	* FollowUpLines:	ql_main_t2_sideTano:ql_main_t2_epicSignals

## ql_main_t2_internals

### qm_t2_internalFabricator
	* Rewards:	bp_im_refinery_01_t1:1	0A:500	1B:500
	* XPMod:	45
	* Tier:	2
	* Goals:	Craft,0	Equip,1
	* Type:	Main
	* GoalParameters:	Tags&Crafting_Factory	Type&Internal;Tags&Crafting_Factory

## ql_main_t2_epicSignals

### qm_t2_epicSignals
	* Rewards:	OF:3
	* XPMod:	45
	* Tier:	2
	* Goals:	Scan,0	CompleteMission,0
	* Type:	Side
	* GoalParameters:	Tags&InGalaxy_T2up;Amount&1;Analyzed&True	Mode&Generated;Tags&Epic_T2up;Amount&1

## ql_main_t2_sideTano

### qm_t2_facTanoch
	* Rewards:	bp_turret_hgn_missile_fs_s_02_u_t2:1	insig_r1:20	insig_r2:20
	* XPMod:	45
	* Tier:	2
	* Goals:	CompleteQuest,0	Goto,1
	* Type:	Main
	* FollowUps:	qm_t2_facYaot_A:qm_t2_facYaot_B:qm_t2_facYaot_C:qm_t2_facYaot_D
	* GoalParameters:	Amount&3;Ids&qm_t2_facTanoch_A|qm_t2_facTanoch_B|qm_t2_facTanoch_C|qm_t2_facTanoch_D	Target&[-1240, -410]
	* FollowUpLines:	ql_main_t2_sideYaot:ql_main_t2_compartments

## ql_main_t2_upgradeInternals

### qm_t2_upgradeInternals
	* Rewards:	BA:30	BC:10
	* XPMod:	45
	* Tier:	2
	* Goals:	Craft,0
	* Type:	Main
	* GoalParameters:	Category&Upgrade;Tags&Factory;Amount&2;MinLevel&5

### qm_t2_otherInternals
	* Rewards:	MF:9
	* XPMod:	45
	* Tier:	2
	* Goals:	Equip,0	Equip,0
	* Type:	Side
	* GoalParameters:	Type&Internal;Tags&Front	Type&Internal;Tags&Back

## ql_main_t2_compartments

### qm_t2_compartments
	* Rewards:	MF:9
	* XPMod:	45
	* Tier:	2
	* Goals:	Equip,0	Equip,0
	* Type:	Side
	* GoalParameters:	Type&Internal;Tags&Front	Type&Internal;Tags&Back

## ql_main_t2_sideYaot

### qm_t2_facYaot
	* Rewards:	bp_hgn_cf_torp_01_u_t2:1	BA:25	BB:10
	* XPMod:	45
	* Tier:	2
	* Goals:	CompleteQuest,0	Goto,1
	* Type:	Main
	* GoalParameters:	Amount&3;Ids&qm_t2_facYaot_A|qm_t2_facYaot_B|qm_t2_facYaot_C|qm_t2_facYaot_D	Target&[-1240, -410]
	* FollowUpLines:	ql_main_t2_templeTonaati

## ql_main_t2_templeTonaati

### qm_t2_templeTonaati
	* Rewards:	bp_turret_hgn_ion_fs_m_01_u_t2:1	rp_catExpl_hyperCap_t3:1	BB:10
	* XPMod:	45
	* Tier:	2
	* Goals:	CompleteMission,0
	* Type:	Main
	* ReplayMissionId:	story_C02_TempleTonaati	story_C02_TempleTonaati_heroic
	* GoalParameters:	Id&story_C02_TempleTonaati
	* FollowUpLines:	ql_Exile:ql_side_exploration:ql_main_t3_jumpCap

## ql_main_t3_jumpCap

### qm_t3_researchJumpCap
	* Rewards:	RP:20
	* XPMod:	135
	* Tier:	3
	* Goals:	Craft,0
	* Type:	Main
	* GoalParameters:	Category&Research;Id&rp_catExpl_hyperCap_t3_c;MinLevel&1
	* FollowUpLines:	ql_main_t3_intro

## ql_main_t3_intro

### qm_t3_scouting
	* Rewards:	insig_r3:10	0A:2180
	* XPMod:	135
	* Tier:	3
	* Goals:	Craft,0	Craft,0
	* Type:	Main
	* GoalParameters:	Category&Upgrade;Tags&Engine;Amount&1;MinLevel&6	Category&Upgrade;Tags&Sensor;Amount&1;MinLevel&6

### qm_t3_scouting_scanBelts
	* Rewards:	AA:30	AB:10
	* XPMod:	135
	* Tier:	3
	* Goals:	Statistic,0
	* Type:	Main
	* GoalParameters:	Id&ScannedBelt;Total&55

### qm_t3_scouting_scanJovian
	* Rewards:	CR:7000
	* XPMod:	135
	* Tier:	3
	* Goals:	Statistic,0
	* Type:	Main
	* GoalParameters:	Id&ScannedJovian;Total&1
	* FollowUpLines:	ql_main_t3_gasMining:ql_main_t3_yaotLiaison

## ql_main_t3_gasMining

### qm_t3_gasMining
	* Rewards:	3E:120	3A:1200
	* XPMod:	135
	* Tier:	3
	* Goals:	Craft,0	Statistic,1
	* Type:	Main
	* GoalParameters:	Category&Crafting;Tags&GCol;Amount&1	Ids&Mined3E_Mined3F_Mined3G_Mined3H;Amount&1000
	* FollowUpLines:	ql_main_t3_sideYaot:ql_main_t3_sideYaot_A:ql_main_t3_sideYaot_B:ql_main_t3_sideYaot_C

## ql_main_t3_yaotLiaison

### qm_t3_yaotLiaison
	* Rewards:	CC:5	BB:5
	* XPMod:	135
	* Tier:	3
	* Goals:	Statistic,0
	* Type:	Side
	* GoalParameters:	Id&RepYaot;Total&1000

## ql_main_t3_sideYaot

### qm_t3_facYaot
	* Rewards:	bp_hgn_sf_intc_01_u_t3:1	CR:7000
	* XPMod:	135
	* Tier:	3
	* Goals:	CompleteQuest,0	Goto,1
	* Type:	Main
	* GoalParameters:	Amount&2;Ids&qm_t3_sideYaot_A_3|qm_t3_sideYaot_B_3|qm_t3_sideYaot_C_3	Target&[-942, -820]
	* FollowUpLines:	ql_raid_017:ql_main_t3_sideTanoch:ql_main_t3_sideTanoch_A:ql_main_t3_sideTanoch_B:ql_main_t3_sideTanoch_C:ql_orb_t3_intro

## ql_main_t3_sideYaot_A

### qm_t3_sideYaot_A_1
	* Rewards:	3C:900	2C:1100
	* XPMod:	135
	* Tier:	3
	* Goals:	Statistic,0	Pay,0
	* Type:	Side
	* GoalParameters:	Id&ScannedBelt;Total&65	Id&3O;Amount&50

### qm_t3_sideYaot_A_2
	* Rewards:	3A:1350	0A:2250
	* XPMod:	135
	* Tier:	3
	* Goals:	Statistic,0	Statistic,0
	* Type:	Side
	* GoalParameters:	Id&Mined3C;Amount&2500	Id&ShipsDestroyed;Amount&30

### qm_t3_sideYaot_A_3
	* Rewards:	3H:75	insig_r1:35
	* XPMod:	135
	* Tier:	3
	* Goals:	Statistic,0	Pay,0
	* Type:	Side
	* GoalParameters:	Id&Refining3N;Amount&300	Id&3N;Amount&100

## ql_main_t3_sideYaot_B

### qm_t3_sideYaot_B_1
	* Rewards:	3A:900	1C:1300
	* XPMod:	135
	* Tier:	3
	* Goals:	Scan,0	CompleteMission,0
	* Type:	Side
	* GoalParameters:	Tags&InSystem_Generated_T3up;Amount&5;Analyzed&True	Amount&6;Tags&T2up;Mode&Generated

### qm_t3_sideYaot_B_2
	* Rewards:	3G:135	2A:1650
	* XPMod:	135
	* Tier:	3
	* Goals:	Statistic,0	GainItem,0
	* Type:	Side
	* GoalParameters:	Id&ShipsDestroyed;Amount&30	Tags&Insignia;Amount&50;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qm_t3_sideYaot_B_3
	* Rewards:	3D:720	AA:30
	* XPMod:	135
	* Tier:	3
	* Goals:	CompleteMission,0
	* Type:	Side
	* GoalParameters:	Amount&3;Tags&T2up;Mode&Strike

## ql_main_t3_sideYaot_C

### qm_t3_sideYaot_C_1
	* Rewards:	3E:90	1A:1300
	* XPMod:	135
	* Tier:	3
	* Goals:	CompleteQuest,0
	* Type:	Side
	* GoalParameters:	Amount&5;Tags&Faction_Yaot_T3up

### qm_t3_sideYaot_C_2
	* Rewards:	3B:1350	1B:1950
	* XPMod:	135
	* Tier:	3
	* Goals:	Statistic,0	Statistic,0
	* Type:	Side
	* GoalParameters:	Id&RepYaot;Amount&250	Id&ShipsDestroyed;Amount&30

### qm_t3_sideYaot_C_3
	* Rewards:	3F:180	2B:2200
	* XPMod:	135
	* Tier:	3
	* Goals:	GainItem,0	Statistic,0
	* Type:	Side
	* GoalParameters:	Tags&Insignia;Amount&65;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash	Id&RepYaot;Total&4050

## ql_main_t3_sideTanoch

### qm_t3_facTanoch
	* Rewards:	bp_hgn_sf_plbo_01_u_t3:1	CR:8000
	* XPMod:	135
	* Tier:	3
	* Goals:	CompleteQuest,0	Goto,1
	* Type:	Main
	* GoalParameters:	Amount&2;Ids&qm_t3_sideTanoch_A_3|qm_t3_sideTanoch_B_3|qm_t3_sideTanoch_C_3	Target&[-1240, -410]
	* FollowUpLines:	ql_raid_018:ql_main_t3_starTotek

## ql_main_t3_sideTanoch_A

### qm_t3_sideTanoch_A_1
	* Rewards:	3F:100	2C:1200
	* XPMod:	135
	* Tier:	3
	* Goals:	Pay,0	Pay,0	Pay,0
	* Type:	Side
	* GoalParameters:	Id&3A;Amount&400	Id&3B;Amount&200	Id&3C;Amount&1400

### qm_t3_sideTanoch_A_2
	* Rewards:	3C:1500	0A:2500
	* XPMod:	135
	* Tier:	3
	* Goals:	Pay,0
	* Type:	Side
	* GoalParameters:	Id&intmed_module_large_t2;Amount&15

### qm_t3_sideTanoch_A_3
	* Rewards:	CC:5	AB:8
	* XPMod:	135
	* Tier:	3
	* Goals:	Pay,0	Pay,0	CompleteMission,1
	* Type:	Side
	* GoalParameters:	Id&intmed_ship_small_t3;Amount&50	Id&intmed_weapon_small_t3;Amount&50	Amount&5

## ql_main_t3_sideTanoch_B

### qm_t3_sideTanoch_B_1
	* Rewards:	3B:975	2B:1200
	* XPMod:	135
	* Tier:	3
	* Goals:	Scan,0	Statistic,0
	* Type:	Side
	* GoalParameters:	Tags&InSystem_T3up;Amount&6;Analyzed&True	Id&ShipsDestroyed;Amount&35

### qm_t3_sideTanoch_B_2
	* Rewards:	3C:1500	1B:2170
	* XPMod:	135
	* Tier:	3
	* Goals:	CompleteMission,0	Statistic,0
	* Type:	Side
	* GoalParameters:	Amount&7	Id&ShipsDestroyedP1;Amount&25

### qm_t3_sideTanoch_B_3
	* Rewards:	insig_r3:18	2D:990
	* XPMod:	135
	* Tier:	3
	* Goals:	CompleteMission,0	GainItem,0
	* Type:	Side
	* GoalParameters:	Amount&3;Tags&T2up;Mode&Strike	Tags&StrikeToken;Amount&6;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

## ql_main_t3_sideTanoch_C

### qm_t3_sideTanoch_C_1
	* Rewards:	3A:975	insig_r1:17
	* XPMod:	135
	* Tier:	3
	* Goals:	Statistic,0
	* Type:	Side
	* GoalParameters:	Id&RepTanoch;Amount&500

### qm_t3_sideTanoch_C_2
	* Rewards:	3B:1500	1A:2170
	* XPMod:	135
	* Tier:	3
	* Goals:	UpgradeOfficer,0	CompleteQuest,0
	* Type:	Side
	* GoalParameters:	Amount&15	Amount&7;Tags&Faction_Tanoch_T2up

### qm_t3_sideTanoch_C_3
	* Rewards:	3G:205	insig_r2:27
	* XPMod:	135
	* Tier:	3
	* Goals:	Statistic,0	Statistic,0
	* Type:	Side
	* GoalParameters:	Id&RepTanoch;Total&8500	Ids&Refining3N_Refining3O_Refining3P_Refining3Q;Amount&600

## ql_main_t3_starTotek

### qm_t3_starTotek
	* Rewards:	bp_turret_tan_kinetic_fs_s_02_u_t3:2
	* XPMod:	135
	* Tier:	3
	* Goals:	CompleteMission,0
	* Type:	Main
	* ReplayMissionId:	story_C03_StarTotek	story_C03_StarTotek_heroic
	* GoalParameters:	Id&story_C03_StarTotek
	* FollowUpLines:	ql_main_t3_sideHiig:ql_main_t3_sideHiig_A:ql_main_t3_sideHiig_B:ql_main_t3_sideHiig_C:ql_main_t3_strikeBreach:ql_raid_019

## ql_main_t3_strikeBreach

### qm_t3_strikeBreach
	* Rewards:	rw_recruitToken_hiig_minUncommon:1
	* XPMod:	135
	* Tier:	3
	* Goals:	CompleteQuest,0
	* Type:	Side
	* GoalParameters:	Ids&qr_019;Amount&1

## ql_main_t3_sideHiig

### qm_t3_facHiigaran
	* Rewards:	bp_yao_sc_assa_01_fu_t3:1	CR:9000	RF:27
	* XPMod:	135
	* Tier:	3
	* Goals:	CompleteQuest,0	Goto,1
	* Type:	Main
	* GoalParameters:	Amount&2;Ids&qm_t3_sideHiigaran_A_3|qm_t3_sideHiigaran_B_3|qm_t3_sideHiigaran_C_3	Target&[-1822, -636]
	* FollowUpLines:	ql_main_t3_sideIyat:ql_main_t3_sideIyat_A:ql_main_t3_sideIyat_B:ql_main_t3_sideIyat_C

## ql_main_t3_sideHiig_A

### qm_t3_sideHiigaran_A_1
	* Rewards:	3B:1125	1C:1625
	* XPMod:	135
	* Tier:	3
	* Goals:	Statistic,0	Statistic,0
	* Type:	Side
	* GoalParameters:	Id&ScannedJovian;Total&20	Ids&Mined3E_Mined3F_Mined3G_Mined3H;Amount&600

### qm_t3_sideHiigaran_A_2
	* Rewards:	3G:175	2A:2110
	* XPMod:	135
	* Tier:	3
	* Goals:	Statistic,0	GainItem,0
	* Type:	Side
	* GoalParameters:	Ids&Mined3A_Mined3B_Mined3C_Mined3D;Amount&5000	Id&RP;Amount&35;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qm_t3_sideHiigaran_A_3
	* Rewards:	CB:9	AA:37
	* XPMod:	135
	* Tier:	3
	* Goals:	Pay,0	Pay,0	Pay,0
	* Type:	Side
	* GoalParameters:	Id&3G;Amount&100	Id&3O;Amount&200	Id&intmed_ship_small_t3;Amount&40

## ql_main_t3_sideHiig_B

### qm_t3_sideHiigaran_B_1
	* Rewards:	3A:1125	2B:1375
	* XPMod:	135
	* Tier:	3
	* Goals:	Statistic,0	GainItem,0
	* Type:	Side
	* GoalParameters:	Id&ShipsDestroyedP1;Amount&30	Tags&Insignia;Amount&40;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qm_t3_sideHiigaran_B_2
	* Rewards:	3E:175	1A:2500
	* XPMod:	135
	* Tier:	3
	* Goals:	Scan,0	CompleteMission,0
	* Type:	Side
	* GoalParameters:	Tags&InSystem_Generated_T3up;Amount&7;Analyzed&True	Amount&5;Tags&T3up;Mode&Generated

### qm_t3_sideHiigaran_B_3
	* Rewards:	insig_r3:20	insig_r2:30
	* XPMod:	135
	* Tier:	3
	* Goals:	Statistic,0	GainItem,0
	* Type:	Side
	* GoalParameters:	Id&ShipsDestroyedProgenitor;Amount&15	Id&RP;Amount&45;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

## ql_main_t3_sideHiig_C

### qm_t3_sideHiigaran_C_1
	* Rewards:	3B:1125	2C:1375
	* XPMod:	135
	* Tier:	3
	* Goals:	GainItem,0	Statistic,0
	* Type:	Side
	* GoalParameters:	Id&LP;Amount&12;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash	Id&PlayerXP;Amount&2000

### qm_t3_sideHiigaran_C_2
	* Rewards:	3C:1725	0A:2875
	* XPMod:	135
	* Tier:	3
	* Goals:	Craft,0	UpgradeOfficer,0
	* Type:	Side
	* GoalParameters:	Category&Crafting;Tags&Ship_Unit_T3up;Amount&5	Amount&20

### qm_t3_sideHiigaran_C_3
	* Rewards:	CD:5	BA:33
	* XPMod:	135
	* Tier:	3
	* Goals:	CompleteMission,0	UpgradeOfficer,1
	* Type:	Side
	* GoalParameters:	Amount&10	Amount&5;MinLevel&20

## ql_main_t3_sideIyat

### qm_t3_facIyatequa
	* Rewards:	bp_turret_hgn_pulsar_fs_s_01_u_t3:1	CR:10000	MF:27
	* XPMod:	135
	* Tier:	3
	* Goals:	CompleteQuest,0	Goto,1
	* Type:	Main
	* GoalParameters:	Amount&2;Ids&qm_t3_sideIyatequa_A_3|qm_t3_sideIyatequa_B_3|qm_t3_sideIyatequa_C_3	Target&[-1543, -626]
	* FollowUpLines:	ql_main_t3_Cang:ql_main_t3_Cang_A:ql_main_t3_Cang_B:ql_main_t3_Cang_C

## ql_main_t3_sideIyat_A

### qm_t3_sideIyatequa_A_1
	* Rewards:	3C:1200	2C:1470
	* XPMod:	135
	* Tier:	3
	* Goals:	CompleteQuest,0	Statistic,0
	* Type:	Side
	* GoalParameters:	Amount&7;Tags&Faction_Tr1_T3up	Id&PlayerXP;Amount&2250

### qm_t3_sideIyatequa_A_2
	* Rewards:	3E:200	1B:2700
	* XPMod:	135
	* Tier:	3
	* Goals:	Statistic,0	Statistic,0
	* Type:	Side
	* GoalParameters:	Id&RepTr1;Amount&500	Ids&Refining3N_Refining3O_Refining3P_Refining3Q;Amount&1000

### qm_t3_sideIyatequa_A_3
	* Rewards:	CA:35	BA:35
	* XPMod:	135
	* Tier:	3
	* Goals:	Statistic,0	Scan,0
	* Type:	Side
	* GoalParameters:	Id&RepTr1;Total&8500	Tags&InGalaxy_T3up;Amount&5;Analyzed&True

## ql_main_t3_sideIyat_B

### qm_t3_sideIyatequa_B_1
	* Rewards:	3B:1200	1A:1735
	* XPMod:	135
	* Tier:	3
	* Goals:	Scan,0	Statistic,0
	* Type:	Side
	* GoalParameters:	Tags&InSystem_Generated_T3up;Amount&8;Analyzed&True	Id&ShipsDestroyedP1;Amount&35

### qm_t3_sideIyatequa_B_2
	* Rewards:	3C:1875	2A:2300
	* XPMod:	135
	* Tier:	3
	* Goals:	CompleteMission,0	GainItem,0
	* Type:	Side
	* GoalParameters:	Amount&8;Tags&T3up;Mode&Generated	Tags&Insignia;Amount&60;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qm_t3_sideIyatequa_B_3
	* Rewards:	CB:10	insig_r1:45
	* XPMod:	135
	* Tier:	3
	* Goals:	CompleteMission,0	CompleteMission,0
	* Type:	Side
	* GoalParameters:	Amount&5;Tags&T2up;Mode&Strike	Amount&2;Tags&T3up;Mode&Strike

## ql_main_t3_sideIyat_C

### qm_t3_sideIyatequa_C_1
	* Rewards:	3F:120	1C:1735
	* XPMod:	135
	* Tier:	3
	* Goals:	Statistic,0	Statistic,0
	* Type:	Side
	* GoalParameters:	Ids&Mined3A_Mined3B_Mined3C_Mined3D;Amount&6000	Id&ShipsDestroyed;Amount&55

### qm_t3_sideIyatequa_C_2
	* Rewards:	3A:1875	0A:3125
	* XPMod:	135
	* Tier:	3
	* Goals:	Statistic,0	Statistic,0
	* Type:	Side
	* GoalParameters:	Ids&Mined3E_Mined3F_Mined3G_Mined3H;Amount&600	Id&Mined3H;Amount&100

### qm_t3_sideIyatequa_C_3
	* Rewards:	insig_r3:23	BB:10
	* XPMod:	135
	* Tier:	3
	* Goals:	Pay,0	Pay,0	Pay,0
	* Type:	Side
	* GoalParameters:	Id&3G;Amount&150	Id&3O;Amount&300	Id&intmed_ship_small_t3;Amount&50

## ql_main_t3_Cang

### qm_t3_facCangacian
	* Rewards:	bp_hgn_cf_ionc_01_u_t3:1	CR:11000	EF:27
	* XPMod:	135
	* Tier:	3
	* Goals:	CompleteQuest,0
	* Type:	Main
	* GoalParameters:	Amount&2;Ids&qm_t3_sideCangacian_A_3|qm_t3_sideCangacian_B_3|qm_t3_sideCangacian_C_3
	* FollowUpLines:	ql_main_t3_sijinLighthouse

## ql_main_t3_Cang_A

### qm_t3_sideCangacian_A_1
	* Rewards:	3B:1350	1B:1950
	* XPMod:	135
	* Tier:	3
	* Goals:	Statistic,0	GainItem,0
	* Type:	Side
	* GoalParameters:	Id&ShipsDestroyedP1;Amount&40	Id&LP;Amount&12;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qm_t3_sideCangacian_A_2
	* Rewards:	3A:2100	2A:2570
	* XPMod:	135
	* Tier:	3
	* Goals:	Scan,0	CompleteMission,0
	* Type:	Side
	* GoalParameters:	Tags&InSystem_Generated_T3up;Amount&9;Analyzed&True	Amount&9;Tags&T3up;Mode&Generated

### qm_t3_sideCangacian_A_3
	* Rewards:	CA:40	BC:6
	* XPMod:	135
	* Tier:	3
	* Goals:	CompleteMission,0	Scan,0
	* Type:	Side
	* GoalParameters:	Amount&4;Tags&T3up;Mode&Strike	Tags&InGalaxy_T3up;Amount&10;Analyzed&True

## ql_main_t3_Cang_B

### qm_t3_sideCangacian_B_1
	* Rewards:	3C:1350	1A:1950
	* XPMod:	135
	* Tier:	3
	* Goals:	GainItem,0	UpgradeOfficer,0
	* Type:	Side
	* GoalParameters:	Tags&Insignia;Amount&80;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash	Amount&25

### qm_t3_sideCangacian_B_2
	* Rewards:	3F:210	0A:3500
	* XPMod:	135
	* Tier:	3
	* Goals:	GainItem,0	Statistic,0
	* Type:	Side
	* GoalParameters:	Id&RP;Amount&50;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash	Id&PlayerXP;Amount&2500

### qm_t3_sideCangacian_B_3
	* Rewards:	3E:285	2D:1400
	* XPMod:	135
	* Tier:	3
	* Goals:	CompleteMission,0	UpgradeOfficer,1
	* Type:	Side
	* GoalParameters:	Amount&10	Amount&5;MinLevel&25

## ql_main_t3_Cang_C

### qm_t3_sideCangacian_C_1
	* Rewards:	3G:135	2B:1650
	* XPMod:	135
	* Tier:	3
	* Goals:	Statistic,0	Statistic,0
	* Type:	Side
	* GoalParameters:	Id&ScannedBelt;Total&80	Ids&Refining3N_Refining3O_Refining3P_Refining3Q;Amount&1500

### qm_t3_sideCangacian_C_2
	* Rewards:	3A:2100	1C:3035
	* XPMod:	135
	* Tier:	3
	* Goals:	Statistic,0	Statistic,0
	* Type:	Side
	* GoalParameters:	Id&ScannedJovian;Total&40	Ids&Mined3E_Mined3F_Mined3G_Mined3H;Amount&750

### qm_t3_sideCangacian_C_3
	* Rewards:	insig_r3:25	insig_r2:38
	* XPMod:	135
	* Tier:	3
	* Goals:	Pay,0	Pay,0	Pay,0
	* Type:	Side
	* GoalParameters:	Id&intmed_ship_small_t3;Amount&20	Id&intmed_weapon_small_t3;Amount&20	Id&intmed_module_small_t3;Amount&20

## ql_main_t3_sijinLighthouse

### qm_t3_sijinLighthouse
	* Rewards:	bp_turret_hgn_kinetic_fs_m_02_u_t3:1	rp_catExpl_hyperCap_t4:1	insig_r3:25
	* XPMod:	135
	* Tier:	3
	* Goals:	CompleteMission,0
	* Type:	Main
	* ReplayMissionId:	story_D01_SijinLighthouse	story_D01_SijinLighthouse_heroic
	* CinematicIds:	40
	* GoalParameters:	Id&story_D01_SijinLighthouse
	* FollowUpLines:	ql_main_t4_intro

## ql_main_t4_intro

### qm_t4_researchJumpCap
	* Rewards:	RP:25
	* XPMod:	405
	* Tier:	4
	* Goals:	Craft,0
	* Type:	Main
	* GoalParameters:	Category&Research;Id&rp_catExpl_hyperCap_t4_c;MinLevel&1
	* FollowUpLines:	ql_main_t4_iliyinLighthouse

## ql_main_t4_iliyinLighthouse

### qm_t4_iliyinLighthouse
	* Rewards:	rw_recruitToken_hiig_random:1
	* XPMod:	405
	* Tier:	4
	* Goals:	CompleteMission,0
	* Type:	Main
	* ReplayMissionId:	story_D02_IliyinLighthouse	story_D02_IliyinLighthouse_heroic
	* GoalParameters:	Id&story_D02_IliyinLighthouse
	* FollowUpLines:	ql_raid_020:ql_raid_021:ql_raid_022:ql_main_t4_amassariLiaison:ql_main_t4_moonResources

## ql_main_t4_amassariLiaison

### qm_t4_amassariLiaison
	* Rewards:	insig_r4:50
	* XPMod:	405
	* Tier:	4
	* Goals:	Statistic,0
	* Type:	Side
	* GoalParameters:	Id&RepAmassari;Total&1000

## ql_main_t4_moonResources

### qm_t4_moonResources
	* Rewards:	4R:100
	* XPMod:	405
	* Tier:	4
	* Goals:	GainItem,0	Statistic,1
	* Type:	Main
	* GoalParameters:	Tags&Moon_Crud;Amount&200;ExcludedSources&PayGoal_BuyItem_SellItem_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash	Ids&Refining4V_Refining4W_Refining4X_Refining4Y;Amount&100
	* FollowUpLines:	ql_main_t4_brightTemple

## ql_main_t4_brightTemple

### qm_t4_brightTemple
	* Rewards:	bp_hgn_sc_puls_01_r_t4:1	4S:100
	* XPMod:	405
	* Tier:	4
	* Goals:	CompleteMission,0
	* Type:	Main
	* ReplayMissionId:	story_D03_BrightTemple	story_D03_BrightTemple_heroic
	* GoalParameters:	Id&story_D03_BrightTemple
	* FollowUpLines:	ql_main_t4_postBrightTemple

## ql_main_t4_postBrightTemple

### qm_t4_postBrightTemple_1
	* Rewards:	4A:2000	4E:500
	* XPMod:	405
	* Tier:	4
	* Goals:	Statistic,0
	* Type:	Main
	* GoalParameters:	Id&RepAmassari;Amount&1000

### qm_t4_postBrightTemple_2
	* Rewards:	4B:2000	4F:500
	* XPMod:	405
	* Tier:	4
	* Goals:	GainItem,0
	* Type:	Main
	* GoalParameters:	Tags&RareEarth_T4up;Amount&300;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qm_t4_postBrightTemple_3
	* Rewards:	CR:80000	battery_u:3
	* XPMod:	405
	* Tier:	4
	* Goals:	GainItem,0
	* Type:	Main
	* GoalParameters:	Tags&Insignia;Amount&600;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash
	* FollowUpLines:	ql_main_t4_hataldan

## ql_main_t4_hataldan

### qm_t4_hataldan
	* Rewards:	bp_hgn_cf_assa_01_r_t4:1	4T:100
	* XPMod:	405
	* Tier:	4
	* Goals:	CompleteMission,0
	* Type:	Main
	* ReplayMissionId:	story_D04_Hataldan	story_D04_Hataldan_heroic
	* GoalParameters:	Id&story_D04_Hataldan
	* FollowUpLines:	ql_main_t4_postHataldan

## ql_main_t4_postHataldan

### qm_t4_postHataldan_1
	* Rewards:	4C:2000	4G:500
	* XPMod:	405
	* Tier:	4
	* Goals:	Scan,0
	* Type:	Main
	* GoalParameters:	Tags&InSystem_Container_T4up;Amount&10;Analyzed&True

### qm_t4_postHataldan_2
	* Rewards:	battery_u:3	battery_r:3	battery_e:3
	* XPMod:	405
	* Tier:	4
	* Goals:	Statistic,0
	* Type:	Main
	* GoalParameters:	Ids&ShipsDestroyedDarkHiigaranT4;Amount&50

### qm_t4_postHataldan_3
	* Rewards:	insig_r4:75	battery_u:3
	* XPMod:	405
	* Tier:	4
	* Goals:	GainItem,0
	* Type:	Main
	* GoalParameters:	Id&ama_collectable_u_01;Amount&15;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash
	* FollowUpLines:	ql_main_t4_nightmareGulf

## ql_main_t4_nightmareGulf

### qm_t4_nightmareGulf
	* Rewards:	bp_ama_sc_assa_01_fu_t4:1	4U:50
	* XPMod:	405
	* Tier:	4
	* Goals:	CompleteMission,0
	* Type:	Main
	* ReplayMissionId:	story_D05_NightmareGulf	story_D05_NightmareGulf_heroic
	* GoalParameters:	Id&story_D05_NightmareGulf
	* FollowUpLines:	ql_raid_023:ql_main_t4_strikeNightmareGulf:ql_main_t4_tanWin

## ql_main_t4_strikeNightmareGulf

### qm_t4_strikeNightmareGulf
	* Rewards:	CR:80000	rw_recruitToken_hiig_minRare:1
	* XPMod:	405
	* Tier:	4
	* Goals:	CompleteQuest,0
	* Type:	Side
	* GoalParameters:	Ids&qr_023;Amount&1

## ql_main_t4_tanWin

### qm_t4_tanWin_DefendBase
	* Rewards:	battery_u:3	battery_r:3	battery_e:3
	* XPMod:	405
	* Tier:	4
	* Goals:	CompleteMission,0
	* Type:	Main
	* ReplayMissionId:	event_tanWin2023_DefendBase_t4
	* GoalParameters:	Id&event_tanWin2023_DefendBase_t4

### qm_t4_tanWin_AttackBase
	* Rewards:	4R:100	4S:100	4T:100
	* XPMod:	405
	* Tier:	4
	* Goals:	CompleteMission,0
	* Type:	Main
	* ReplayMissionId:	event_tanWin2023_AttackBase_t4
	* GoalParameters:	Id&event_tanWin2023_AttackBase_t4

### qm_t4_tanWin_Relic
	* Rewards:	CR:120000
	* XPMod:	405
	* Tier:	4
	* Goals:	CompleteMission,0
	* Type:	Main
	* ReplayMissionId:	event_tanWin2023_Relic_t4
	* GoalParameters:	Id&event_tanWin2023_Relic_t4

### qm_t4_tanWin_Academy
	* Rewards:	bp_tan_cf_assa_01_fr_t4:1
	* XPMod:	405
	* Tier:	4
	* Goals:	CompleteMission,0
	* Type:	Main
	* ReplayMissionId:	event_tanWin2023_Academy_t4
	* GoalParameters:	Id&event_tanWin2023_Academy_t4
	* FollowUpLines:	ql_main_t4_yaoSpr

## ql_main_t4_yaoSpr

### qm_t4_yaoSpr_Conjunction
	* Rewards:	rw_recruitToken_hiig_minEpic:1
	* XPMod:	405
	* Tier:	4
	* Goals:	CompleteMission,0
	* Type:	Main
	* ReplayMissionId:	event_yaoSpr2024_Conjunction_t4
	* GoalParameters:	Id&event_yaoSpr2024_Conjunction_t4

## ql_orb_t3_intro

### qm_orb_t3_components
	* Rewards:	CA:125	CB:35
	* XPMod:	135
	* Tier:	3
	* Goals:	Craft,0	Craft,0	Craft,0
	* Type:	Side
	* GoalParameters:	Id&playerOrb_comp_stabilizer_t3	Id&playerOrb_comp_frame_t3	Id&playerOrb_comp_lifeSupport_t3

### qm_orb_t3_orbital
	* Rewards:	insig_r1:45	insig_r3:25
	* XPMod:	135
	* Tier:	3
	* Goals:	Craft,0
	* Type:	Side
	* GoalParameters:	Id&hgn_co_orbi_01_t1

### qm_orb_t3_placeOrbital
	* Rewards:	CR:50000	ticket_moveOrbital:1
	* XPMod:	135
	* Tier:	3
	* Goals:	PlaceOrbital,0
	* Type:	Side
	* GoalParameters:	NoParameter&None

### qm_orb_t3_modules
	* Rewards:	insig_r2:35	rw_recruitToken_hiig_minRare:1
	* XPMod:	135
	* Tier:	3
	* Goals:	Equip,0
	* Type:	Side
	* GoalParameters:	Type&Internal;Tags&Orbital;Target&hgn_co_orbi_01_t1

## ql_side_exploration

### qs_exploration_01
	* Rewards:	rw_rbox_qr_small:1
	* XPMod:	15
	* Tier:	2
	* Goals:	Scan,0	CompleteMission,0
	* Type:	Side
	* GoalParameters:	Tags&InSystem;Amount&15;Analyzed&True	Amount&10;Tier&2;Mode&Generated
	* FollowUpLines:	ql_side_001

### qs_exploration_02
	* Rewards:	rw_rbox_qr_medium:1
	* XPMod:	60
	* Tier:	2
	* Goals:	GainItem,0
	* Type:	Side
	* GoalParameters:	Id&RP;Amount&900;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash
	* FollowUpLines:	ql_side_002

### qs_exploration_03
	* Rewards:	rw_rbox_qr_large:1
	* XPMod:	60
	* Tier:	2
	* Goals:	Scan,0	Pay,1
	* Type:	Side
	* GoalParameters:	Tags&InSystem;Amount&25;Analyzed&True	Id&2P;Amount&5000
	* FollowUpLines:	ql_Ytep

## ql_side_001

### qs_economy_01
	* Rewards:	rw_rbox_qr_small:1
	* XPMod:	15
	* Tier:	2
	* Goals:	Craft,0	CompleteMission,0
	* Type:	Side
	* GoalParameters:	Category&Refining;Amount&2000	Amount&5;Tier&2;Mode&Generated

### qs_economy_02
	* Rewards:	rw_rbox_qr_medium:1
	* XPMod:	60
	* Tier:	2
	* Goals:	Craft,0
	* Type:	Side
	* GoalParameters:	Category&Crafting;Amount&50

### qs_economy_03
	* Rewards:	rw_rbox_qr_large:1
	* XPMod:	60
	* Tier:	2
	* Goals:	Craft,0	Pay,1
	* Type:	Side
	* GoalParameters:	Category&Refining;Amount&4500	Id&2N;Amount&5000

## ql_side_002

### qs_battle_01
	* Rewards:	rw_rbox_qr_small:1
	* XPMod:	15
	* Tier:	2
	* Goals:	Craft,0	CompleteMission,0
	* Type:	Side
	* GoalParameters:	Category&Upgrade;Amount&10	Amount&15;Tier&2;Mode&Generated

### qs_battle_02
	* Rewards:	rw_rbox_qr_medium:1
	* XPMod:	60
	* Tier:	2
	* Goals:	CompleteQuest,0
	* Type:	Side
	* GoalParameters:	Amount&25;Tags&Faction_T2up

### qs_battle_03
	* Rewards:	rw_rbox_qr_large:1
	* XPMod:	60
	* Tier:	2
	* Goals:	CompleteMission,0	Pay,1
	* Type:	Side
	* GoalParameters:	Amount&1;Tier&2;Mode&Strike	Id&2O;Amount&5000

## ql_side_unlockStrikes_t2

### qs_unlockStrikes_t2
	* Rewards:	rw_rbox_qr_large:1
	* XPMod:	2
	* Tier:	1
	* Goals:	Equip,0
	* Type:	Side
	* GoalParameters:	Type&Flagship;Tags&T1
	* FollowUpLines:	ql_raid_014:ql_raid_015:ql_raid_016

## ql_side_unlockStrikes_t3

### qs_unlockStrikes_t3
	* Rewards:	rw_rbox_qr_large:1
	* XPMod:	2
	* Tier:	2
	* Goals:	Equip,0
	* Type:	Side
	* GoalParameters:	Type&Flagship;Tags&T2
	* FollowUpLines:	ql_raid_017:ql_raid_018

## ql_Keid

### qs_Keid_01
	* Rewards:	BC:50	insig_r1:45
	* XPMod:	6
	* Tier:	2
	* Goals:	Goto,0	Scan,1	CompleteMission,1	Statistic,1
	* Type:	Side
	* GoalParameters:	Target&[-1784, -564];TargetMode&Station	Tags&InSystem_T2up;Amount&10;Analyzed&True	Mode&Generated;Tier&2;Amount&10	Id&ShipsDestroyedT2;Amount&50

### qs_Keid_02
	* Rewards:	insig_r1:45	insig_r2:45
	* XPMod:	8
	* Tier:	2
	* Goals:	Statistic,0	Statistic,0	Statistic,0	Statistic,0	Statistic,1	Statistic,1	Statistic,1	Statistic,1
	* Type:	Side
	* GoalParameters:	Id&Mined2A;Amount&2000	Id&Mined2B;Amount&2000	Id&Mined2C;Amount&2000	Id&Mined2D;Amount&1500	Id&Refining2N;Amount&1000	Id&Refining2O;Amount&1000	Id&Refining2P;Amount&1000	Id&Refining2Q;Amount&700

### qs_Keid_03
	* Rewards:	BA:125	insig_r2:45	rw_cryo_hiig_minRare:1
	* XPMod:	10
	* Tier:	2
	* Goals:	Pay,0	Pay,0	Pay,0	Pay,1	Pay,1
	* Type:	Side
	* GoalParameters:	Id&2N;Amount&1000;SysId&[-1784, -564]	Id&2O;Amount&1000;SysId&[-1784, -564]	Id&2P;Amount&1000;SysId&[-1784, -564]	Id&2Q;Amount&700;SysId&[-1784, -564]	Id&CR;Amount&10000;SysId&[-1784, -564]

## ql_Exile

### qs_Exile_01
	* Rewards:	CR:20000	BB:35
	* XPMod:	8
	* Tier:	2
	* Goals:	CompleteMission,0	Statistic,0
	* Type:	Side
	* GoalParameters:	Amount&10;Tier&2;Mode&Strike	Id&ShipsDestroyedP1;Amount&150

### qs_Exile_02
	* Rewards:	CR:20000	intmed_weapon_small_t2:450
	* XPMod:	10
	* Tier:	2
	* Goals:	Statistic,0	Statistic,0	Statistic,0	Craft,1
	* Type:	Side
	* GoalParameters:	Id&Mined2A;Amount&15000	Id&Mined2B;Amount&15000	Id&Mined2C;Amount&15000	Category&Crafting;Amount&10;Tags&Squad_T2up

### qs_Exile_03
	* Rewards:	bp_turret_hgn_kinetic_fs_m_02_r_t2:1	CR:20000	intmed_weapon_large_t2:50
	* XPMod:	12
	* Tier:	2
	* Goals:	Goto,0	Goto,0	Goto,0	Scan,1
	* Type:	Side
	* GoalParameters:	Target&[-1752, -861];TargetMode&Station	Target&[-1020, -650];TargetMode&Station	Target&[-1665, 176];TargetMode&Station	Tags&InSystem_T2up;Amount&50;Analyzed&True

## ql_Ytep

### qs_Ytep_01
	* Rewards:	CR:20000	3A:9000
	* XPMod:	10
	* Tier:	3
	* Goals:	Goto,0	Scan,1	CompleteMission,1	Statistic,1
	* Type:	Side
	* GoalParameters:	Target&[-946, -690];TargetMode&Station	Tags&InSystem_T3up;Amount&10;Analyzed&True	Mode&Generated;Tier&3;Amount&10	Id&ShipsDestroyedT3;Amount&75

### qs_Ytep_02
	* Rewards:	bp_hgn_sc_puls_01_r_t3:1	CR:20000
	* XPMod:	12
	* Tier:	3
	* Goals:	Craft,0	Craft,0	Craft,0	Craft,1	Craft,1
	* Type:	Side
	* GoalParameters:	Tags&Part_Ship_S_T2;Amount&2000;Category&Crafting	Tags&Part_Weapon_S_T2;Amount&2000;Category&Crafting	Tags&Part_Module_S_T2;Amount&2000;Category&Crafting	Type&Squad;Tags&Interceptor_T2;Amount&1;Category&Crafting	Type&Squad;Tags&AssaultCorvette_T2;Amount&1;Category&Crafting

### qs_Ytep_03
	* Rewards:	bp_hgn_cf_torp_01_e_t3:1	CR:20000	CC:10
	* XPMod:	14
	* Tier:	3
	* Goals:	Pay,0	Pay,0	Pay,0	Pay,1	Pay,1
	* Type:	Side
	* GoalParameters:	Id&intmed_ship_small_t2;Amount&20;SysId&[-946, -690]	Id&intmed_weapon_small_t2;Amount&800;SysId&[-946, -690]	Id&intmed_module_small_t2;Amount&800;SysId&[-946, -690]	Id&hgn_sf_intc_01_t2;Amount&1;SysId&[-946, -690]	Id&hgn_sc_assa_01_t2;Amount&1;SysId&[-946, -690]

## ql_esca_killPirate1

### qs_killPirate1_pre01
	* Rewards:	CR:3000
	* XPMod:	0.5
	* Tier:	1
	* Goals:	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&ShipsDestroyedP1;Total&10

### qs_killPirate1_00
	* Rewards:	1A:1000	1B:1000	1C:1000
	* XPMod:	1
	* Tier:	1
	* Goals:	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&ShipsDestroyedP1;Total&25

### qs_killPirate1_01
	* Rewards:	CR:6500	insig_r1:10
	* XPMod:	2
	* Tier:	1
	* Goals:	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&ShipsDestroyedP1;Total&50

### qs_killPirate1_02
	* Rewards:	CR:10000	insig_r1:10
	* XPMod:	4
	* Tier:	1
	* Goals:	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&ShipsDestroyedP1;Total&100

### qs_killPirate1_03
	* Rewards:	CR:25000	insig_r1:10
	* XPMod:	8
	* Tier:	1
	* Goals:	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&ShipsDestroyedP1;Total&200
	* FollowUpLines:	ql_esca_killYaot

### qs_killPirate1_04
	* Rewards:	insig_r1:30	insig_r2:30
	* XPMod:	16
	* Tier:	1
	* Goals:	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&ShipsDestroyedP1;Total&400

### qs_killPirate1_05
	* Rewards:	rw_1h_cr_t2:1	insig_r2:30
	* XPMod:	32
	* Tier:	1
	* Goals:	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&ShipsDestroyedP1;Total&800

### qs_killPirate1_06
	* Rewards:	rw_cryo_hiig_random:1	bp_hgn_sf_intc_01_u_t2:1	insig_r2:30
	* XPMod:	64
	* Tier:	1
	* Goals:	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&ShipsDestroyedP1;Total&1600

### qs_killPirate1_07
	* Rewards:	rw_cryo_hiig_minUncommon:1	rw_1h_ree_t3:1	insig_r3:30
	* XPMod:	128
	* Tier:	1
	* Goals:	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&ShipsDestroyedP1;Total&3200

### qs_killPirate1_08
	* Rewards:	rw_cryo_hiig_minRare:1	rw_1h_cr_t3:1	insig_r3:30
	* XPMod:	256
	* Tier:	1
	* Goals:	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&ShipsDestroyedP1;Total&6400

## ql_esca_killTanoch

### qs_killTanoch_pre01
	* Rewards:	CR:3000
	* XPMod:	0.5
	* Tier:	2
	* Goals:	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&ShipsDestroyedTanoch;Total&10

### qs_killTanoch_00
	* Rewards:	intmed_ship_small_t3:60	intmed_weapon_small_t3:60	intmed_module_small_t3:60
	* XPMod:	1
	* Tier:	2
	* Goals:	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&ShipsDestroyedTanoch;Total&25

### qs_killTanoch_01
	* Rewards:	CR:6500	insig_r2:10
	* XPMod:	2
	* Tier:	2
	* Goals:	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&ShipsDestroyedTanoch;Total&50

### qs_killTanoch_02
	* Rewards:	bp_hgn_sf_intc_01_u_t2:1	insig_r2:10
	* XPMod:	4
	* Tier:	2
	* Goals:	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&ShipsDestroyedTanoch;Total&100

### qs_killTanoch_03
	* Rewards:	BA:50	insig_r2:10
	* XPMod:	8
	* Tier:	2
	* Goals:	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&ShipsDestroyedTanoch;Total&200

### qs_killTanoch_04
	* Rewards:	hc_bun_100:1	insig_r2:30
	* XPMod:	16
	* Tier:	2
	* Goals:	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&ShipsDestroyedTanoch;Total&400

### qs_killTanoch_05
	* Rewards:	bp_hgn_sf_intc_01_u_t2:1	insig_r2:30
	* XPMod:	32
	* Tier:	2
	* Goals:	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&ShipsDestroyedTanoch;Total&800

### qs_killTanoch_06
	* Rewards:	rw_cryo_hiig_random:1	rw_1h_ree_t2:1	insig_r2:30
	* XPMod:	64
	* Tier:	2
	* Goals:	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&ShipsDestroyedTanoch;Total&1600

### qs_killTanoch_07
	* Rewards:	rw_cryo_hiig_minUncommon:1	hc_bun_100:1	insig_r3:30
	* XPMod:	128
	* Tier:	2
	* Goals:	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&ShipsDestroyedTanoch;Total&3200

### qs_killTanoch_08
	* Rewards:	rw_cryo_hiig_minRare:1	bp_hgn_sf_intc_01_u_t3:1	insig_r3:30
	* XPMod:	256
	* Tier:	2
	* Goals:	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&ShipsDestroyedTanoch;Total&6400

## ql_esca_killYaot

### qs_killYaot_pre01
	* Rewards:	CR:3000
	* XPMod:	0.5
	* Tier:	2
	* Goals:	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&ShipsDestroyedYaot;Total&10

### qs_killYaot_00
	* Rewards:	2N:70	2O:70	2P:70
	* XPMod:	1
	* Tier:	2
	* Goals:	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&ShipsDestroyedYaot;Total&25

### qs_killYaot_01
	* Rewards:	CR:6500	insig_r2:10
	* XPMod:	2
	* Tier:	2
	* Goals:	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&ShipsDestroyedYaot;Total&50

### qs_killYaot_02
	* Rewards:	bp_hgn_sf_plbo_01_u_t2:1	insig_r2:10
	* XPMod:	4
	* Tier:	2
	* Goals:	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&ShipsDestroyedYaot;Total&100

### qs_killYaot_03
	* Rewards:	BA:50	insig_r2:10
	* XPMod:	8
	* Tier:	2
	* Goals:	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&ShipsDestroyedYaot;Total&200
	* FollowUpLines:	ql_esca_killTanoch

### qs_killYaot_04
	* Rewards:	hc_bun_100:1	insig_r2:30
	* XPMod:	16
	* Tier:	2
	* Goals:	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&ShipsDestroyedYaot;Total&400

### qs_killYaot_05
	* Rewards:	bp_hgn_sf_plbo_01_u_t2:1	insig_r2:30
	* XPMod:	32
	* Tier:	2
	* Goals:	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&ShipsDestroyedYaot;Total&800

### qs_killYaot_06
	* Rewards:	rw_cryo_hiig_random:1	rw_1h_ree_t2:1	insig_r2:30
	* XPMod:	64
	* Tier:	2
	* Goals:	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&ShipsDestroyedYaot;Total&1600

### qs_killYaot_07
	* Rewards:	rw_cryo_hiig_minUncommon:1	hc_bun_100:1	insig_r3:30
	* XPMod:	128
	* Tier:	2
	* Goals:	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&ShipsDestroyedYaot;Total&3200

### qs_killYaot_08
	* Rewards:	rw_cryo_hiig_minRare:1	bp_hgn_sf_plbo_01_u_t3:1	insig_r3:30
	* XPMod:	256
	* Tier:	2
	* Goals:	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&ShipsDestroyedYaot;Total&6400

## ql_esca_mineT1

### qs_mineT1ABC_pre01
	* Rewards:	CR:3000
	* XPMod:	0.5
	* Tier:	1
	* Goals:	Statistic,0	Statistic,0	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&Mined1A;Total&1000	Id&Mined1B;Total&1000	Id&Mined1C;Total&1000

### qs_mineT1ABC_00
	* Rewards:	1A:1000	1B:1000	1C:1000
	* XPMod:	1
	* Tier:	1
	* Goals:	Statistic,0	Statistic,0	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&Mined1A;Total&3000	Id&Mined1B;Total&3000	Id&Mined1C;Total&3000

### qs_mineT1ABC_01
	* Rewards:	CR:6500	1P:500
	* XPMod:	2
	* Tier:	1
	* Goals:	Statistic,0	Statistic,0	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&Mined1A;Total&6000	Id&Mined1B;Total&6000	Id&Mined1C;Total&6000

### qs_mineT1ABC_02
	* Rewards:	AA:50	1O:500
	* XPMod:	4
	* Tier:	1
	* Goals:	Statistic,0	Statistic,0	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&Mined1A;Total&12000	Id&Mined1B;Total&12000	Id&Mined1C;Total&12000

### qs_mineT1ABC_03
	* Rewards:	HC:50	1N:500
	* XPMod:	8
	* Tier:	1
	* Goals:	Statistic,0	Statistic,0	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&Mined1A;Total&24000	Id&Mined1B;Total&24000	Id&Mined1C;Total&24000
	* FollowUpLines:	ql_esca_mineT2

### qs_mineT1ABC_04
	* Rewards:	rw_1h_cr_t2:1	rw_1h_refined_t2:1
	* XPMod:	16
	* Tier:	1
	* Goals:	Statistic,0	Statistic,0	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&Mined1A;Total&48000	Id&Mined1B;Total&48000	Id&Mined1C;Total&48000

### qs_mineT1ABC_05
	* Rewards:	rw_1h_ree_t2:1	intmed_ship_small_t2:375	intmed_module_small_t2:375
	* XPMod:	32
	* Tier:	1
	* Goals:	Statistic,0	Statistic,0	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&Mined1A;Total&96000	Id&Mined1B;Total&96000	Id&Mined1C;Total&96000

### qs_mineT1ABC_06
	* Rewards:	rw_cryo_hiig_random:1	hc_bun_100:1	intmed_ship_large_t2:105
	* XPMod:	64
	* Tier:	1
	* Goals:	Statistic,0	Statistic,0	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&Mined1A;Total&192000	Id&Mined1B;Total&192000	Id&Mined1C;Total&192000

### qs_mineT1ABC_07
	* Rewards:	rw_cryo_hiig_minUncommon:1	rw_1h_cr_t3:1	intmed_ship_small_t3:195
	* XPMod:	128
	* Tier:	1
	* Goals:	Statistic,0	Statistic,0	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&Mined1A;Total&384000	Id&Mined1B;Total&384000	Id&Mined1C;Total&384000

### qs_mineT1ABC_08
	* Rewards:	rw_cryo_hiig_minRare:1	rw_1h_ree_t3:1	intmed_ship_large_t3:30
	* XPMod:	256
	* Tier:	1
	* Goals:	Statistic,0	Statistic,0	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&Mined1A;Total&768000	Id&Mined1B;Total&768000	Id&Mined1C;Total&768000

## ql_esca_mineT2

### qs_mineT2ABC_pre01
	* Rewards:	CR:3000
	* XPMod:	0.5
	* Tier:	2
	* Goals:	Statistic,0	Statistic,0	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&Mined2A;Total&1000	Id&Mined2B;Total&1000	Id&Mined2C;Total&1000

### qs_mineT2ABC_00
	* Rewards:	2N:70	2O:70	2P:70
	* XPMod:	1
	* Tier:	2
	* Goals:	Statistic,0	Statistic,0	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&Mined2A;Total&3000	Id&Mined2B;Total&3000	Id&Mined2C;Total&3000

### qs_mineT2ABC_01
	* Rewards:	CR:6500	2N:100	2P:100
	* XPMod:	2
	* Tier:	2
	* Goals:	Statistic,0	Statistic,0	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&Mined2A;Total&6000	Id&Mined2B;Total&6000	Id&Mined2C;Total&6000

### qs_mineT2ABC_02
	* Rewards:	HC:50	intmed_ship_small_t2:70
	* XPMod:	4
	* Tier:	2
	* Goals:	Statistic,0	Statistic,0	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&Mined2A;Total&12000	Id&Mined2B;Total&12000	Id&Mined2C;Total&12000

### qs_mineT2ABC_03
	* Rewards:	CR:25000	intmed_weapon_small_t2:35	intmed_module_small_t2:35
	* XPMod:	8
	* Tier:	2
	* Goals:	Statistic,0	Statistic,0	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&Mined2A;Total&24000	Id&Mined2B;Total&24000	Id&Mined2C;Total&24000
	* FollowUpLines:	ql_esca_mineT3

### qs_mineT2ABC_04
	* Rewards:	bp_hgn_sf_plbo_01_u_t2:1	rw_1h_refined_t2:1
	* XPMod:	16
	* Tier:	2
	* Goals:	Statistic,0	Statistic,0	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&Mined2A;Total&48000	Id&Mined2B;Total&48000	Id&Mined2C;Total&48000

### qs_mineT2ABC_05
	* Rewards:	hc_bun_100:1	intmed_weapon_small_t2:375	intmed_module_small_t2:375
	* XPMod:	32
	* Tier:	2
	* Goals:	Statistic,0	Statistic,0	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&Mined2A;Total&96000	Id&Mined2B;Total&96000	Id&Mined2C;Total&96000

### qs_mineT2ABC_06
	* Rewards:	rw_cryo_hiig_random:1	rw_1h_cr_t2:1	intmed_module_large_t2:105
	* XPMod:	64
	* Tier:	2
	* Goals:	Statistic,0	Statistic,0	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&Mined2A;Total&192000	Id&Mined2B;Total&192000	Id&Mined2C;Total&192000

### qs_mineT2ABC_07
	* Rewards:	rw_cryo_hiig_minUncommon:1	bp_hgn_sf_plbo_01_u_t3:1	intmed_weapon_small_t3:195
	* XPMod:	128
	* Tier:	2
	* Goals:	Statistic,0	Statistic,0	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&Mined2A;Total&384000	Id&Mined2B;Total&384000	Id&Mined2C;Total&384000

### qs_mineT2ABC_08
	* Rewards:	rw_cryo_hiig_minRare:1	hc_bun_100:1	intmed_weapon_large_t3:30
	* XPMod:	256
	* Tier:	2
	* Goals:	Statistic,0	Statistic,0	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&Mined2A;Total&768000	Id&Mined2B;Total&768000	Id&Mined2C;Total&768000

## ql_esca_mineT3

### qs_mineT3ABC_pre01
	* Rewards:	CR:3000
	* XPMod:	0.5
	* Tier:	3
	* Goals:	Statistic,0	Statistic,0	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&Mined3A;Total&1000	Id&Mined3B;Total&1000	Id&Mined3C;Total&1000

### qs_mineT3ABC_00
	* Rewards:	intmed_ship_small_t3:60	intmed_weapon_small_t3:60	intmed_module_small_t3:60
	* XPMod:	1
	* Tier:	3
	* Goals:	Statistic,0	Statistic,0	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&Mined3A;Total&3000	Id&Mined3B;Total&3000	Id&Mined3C;Total&3000

### qs_mineT3ABC_01
	* Rewards:	CR:6500	intmed_ship_small_t3:30
	* XPMod:	2
	* Tier:	3
	* Goals:	Statistic,0	Statistic,0	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&Mined3A;Total&6000	Id&Mined3B;Total&6000	Id&Mined3C;Total&6000

### qs_mineT3ABC_02
	* Rewards:	CA:50	intmed_module_small_t3:15	intmed_weapon_small_t3:15
	* XPMod:	4
	* Tier:	3
	* Goals:	Statistic,0	Statistic,0	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&Mined3A;Total&12000	Id&Mined3B;Total&12000	Id&Mined3C;Total&12000

### qs_mineT3ABC_03
	* Rewards:	HC:50	3O:130
	* XPMod:	8
	* Tier:	3
	* Goals:	Statistic,0	Statistic,0	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&Mined3A;Total&24000	Id&Mined3B;Total&24000	Id&Mined3C;Total&24000

### qs_mineT3ABC_04
	* Rewards:	rw_1h_cr_t3:1	intmed_module_small_t3:65	intmed_ship_small_t3:130
	* XPMod:	16
	* Tier:	3
	* Goals:	Statistic,0	Statistic,0	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&Mined3A;Total&48000	Id&Mined3B;Total&48000	Id&Mined3C;Total&48000

### qs_mineT3ABC_05
	* Rewards:	rw_1h_ree_t3:1	intmed_module_large_t3:20	intmed_ship_large_t3:10
	* XPMod:	32
	* Tier:	3
	* Goals:	Statistic,0	Statistic,0	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&Mined3A;Total&96000	Id&Mined3B;Total&96000	Id&Mined3C;Total&96000

### qs_mineT3ABC_06
	* Rewards:	rw_cryo_hiig_random:1	hc_bun_100:1	rw_1h_refined_t3:1
	* XPMod:	64
	* Tier:	3
	* Goals:	Statistic,0	Statistic,0	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&Mined3A;Total&192000	Id&Mined3B;Total&192000	Id&Mined3C;Total&192000

### qs_mineT3ABC_07
	* Rewards:	rw_cryo_hiig_minUncommon:1	rw_1h_cr_t3:1	intmed_module_small_t3:195
	* XPMod:	128
	* Tier:	3
	* Goals:	Statistic,0	Statistic,0	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&Mined3A;Total&384000	Id&Mined3B;Total&384000	Id&Mined3C;Total&384000

### qs_mineT3ABC_08
	* Rewards:	rw_cryo_hiig_minRare:1	rw_1h_ree_t3:1	intmed_module_large_t3:30
	* XPMod:	256
	* Tier:	3
	* Goals:	Statistic,0	Statistic,0	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&Mined3A;Total&768000	Id&Mined3B;Total&768000	Id&Mined3C;Total&768000

## ql_esca_scan

### qs_scan_pre01
	* Rewards:	CR:3000
	* XPMod:	0.5
	* Tier:	1
	* Goals:	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&Scanned;Total&50

### qs_scan_00
	* Rewards:	insig_r1:10
	* XPMod:	1
	* Tier:	1
	* Goals:	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&Scanned;Total&150

### qs_scan_01
	* Rewards:	CR:6500	1A:3000
	* XPMod:	4
	* Tier:	1
	* Goals:	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&Scanned;Total&300
	* FollowUpLines:	ql_esca_generated

### qs_scan_02
	* Rewards:	HC:50	1O:500
	* XPMod:	8
	* Tier:	1
	* Goals:	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&Scanned;Total&600

### qs_scan_03
	* Rewards:	CR:25000	1C:3000
	* XPMod:	16
	* Tier:	1
	* Goals:	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&Scanned;Total&1200

### qs_scan_04
	* Rewards:	bp_hgn_sf_intc_01_u_t2:1	rw_1h_ore_T2:1
	* XPMod:	32
	* Tier:	1
	* Goals:	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&Scanned;Total&2500

### qs_scan_05
	* Rewards:	hc_bun_100:1	rw_1h_refined_t2:1
	* XPMod:	64
	* Tier:	1
	* Goals:	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&Scanned;Total&5000

### qs_scan_06
	* Rewards:	rw_cryo_hiig_random:1	rw_1h_cr_t2:1	rw_1h_ore_T2:1
	* XPMod:	128
	* Tier:	1
	* Goals:	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&Scanned;Total&10000

### qs_scan_07
	* Rewards:	rw_cryo_hiig_minUncommon:1	bp_hgn_sf_intc_01_u_t3:1	rw_1h_ore_T3:1
	* XPMod:	256
	* Tier:	1
	* Goals:	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&Scanned;Total&20000

### qs_scan_08
	* Rewards:	rw_cryo_hiig_minRare:1	hc_bun_100:1	rw_1h_refined_t3:1
	* XPMod:	512
	* Tier:	1
	* Goals:	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&Scanned;Total&40000

## ql_esca_generated

### qs_finishGenerated_pre01
	* Rewards:	CR:3000
	* XPMod:	0.5
	* Tier:	1
	* Goals:	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&MissionsDoneGenerated;Total&2

### qs_finishGenerated_00
	* Rewards:	insig_r1:10
	* XPMod:	1
	* Tier:	1
	* Goals:	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&MissionsDoneGenerated;Total&5

### qs_finishGenerated_01
	* Rewards:	CR:6500	1B:3000
	* XPMod:	6
	* Tier:	1
	* Goals:	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&MissionsDoneGenerated;Total&10

### qs_finishGenerated_02
	* Rewards:	CR:13000	1P:500
	* XPMod:	12
	* Tier:	1
	* Goals:	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&MissionsDoneGenerated;Total&20

### qs_finishGenerated_03
	* Rewards:	bp_hgn_sf_plbo_01_u_t1:1	1A:3000
	* XPMod:	24
	* Tier:	1
	* Goals:	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&MissionsDoneGenerated;Total&40

### qs_finishGenerated_04
	* Rewards:	rw_1h_ree_t2:1	rw_1h_ore_T2:1
	* XPMod:	48
	* Tier:	1
	* Goals:	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&MissionsDoneGenerated;Total&80

### qs_finishGenerated_05
	* Rewards:	rw_1h_cr_t2:1	rw_1h_refined_t2:1
	* XPMod:	72
	* Tier:	1
	* Goals:	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&MissionsDoneGenerated;Total&160

### qs_finishGenerated_06
	* Rewards:	rw_cryo_hiig_random:1	bp_hgn_sf_plbo_01_u_t2:1	rw_1h_ore_T2:1
	* XPMod:	108
	* Tier:	1
	* Goals:	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&MissionsDoneGenerated;Total&320

### qs_finishGenerated_07
	* Rewards:	rw_cryo_hiig_minUncommon:1	rw_1h_ree_t3:1	rw_1h_ore_T3:1
	* XPMod:	162
	* Tier:	1
	* Goals:	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&MissionsDoneGenerated;Total&640

### qs_finishGenerated_08
	* Rewards:	rw_cryo_hiig_minRare:1	rw_1h_cr_t3:1	rw_1h_refined_t3:1
	* XPMod:	243
	* Tier:	1
	* Goals:	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&MissionsDoneGenerated;Total&1300

## ql_raid_013

### qr_013
	* Rewards:	rw_i_strike_quest_pirateHideout_N:1
	* XPMod:	0
	* Tier:	1
	* Goals:	CompleteMission,0
	* Type:	Strike
	* GoalParameters:	Id&strike_01_PirateHideout

## ql_raid_016

### qr_016
	* Rewards:	rw_i_strike_quest_pirateHideout_H:1
	* XPMod:	0
	* Tier:	2
	* Goals:	CompleteMission,0
	* Type:	Strike
	* GoalParameters:	Id&strike_01_PirateHideout_heroic

## ql_raid_014

### qr_014
	* Rewards:	rw_i_strike_quest_stationDefense_N:1
	* XPMod:	0
	* Tier:	2
	* Goals:	CompleteMission,0
	* Type:	Strike
	* GoalParameters:	Id&strike_02_StationDefense

## ql_raid_017

### qr_017
	* Rewards:	rw_i_strike_quest_stationDefense_H:1
	* XPMod:	0
	* Tier:	3
	* Goals:	CompleteMission,0
	* Type:	Strike
	* GoalParameters:	Id&strike_02_StationDefense_heroic

## ql_raid_021

### qr_021
	* Rewards:	rw_i_strike_quest_stationDefense_M:1
	* XPMod:	0
	* Tier:	4
	* Goals:	CompleteMission,0
	* Type:	Strike
	* GoalParameters:	Id&strike_02_StationDefense_mythic

## ql_raid_015

### qr_015
	* Rewards:	rw_i_strike_quest_pahrasRock_N:1
	* XPMod:	0
	* Tier:	2
	* Goals:	CompleteMission,0
	* Type:	Strike
	* GoalParameters:	Id&strike_03_PahrasRock

## ql_raid_018

### qr_018
	* Rewards:	rw_i_strike_quest_pahrasRock_H:1
	* XPMod:	0
	* Tier:	3
	* Goals:	CompleteMission,0
	* Type:	Strike
	* GoalParameters:	Id&strike_03_PahrasRock_heroic

## ql_raid_022

### qr_022
	* Rewards:	rw_i_strike_quest_pahrasRock_M:1
	* XPMod:	0
	* Tier:	4
	* Goals:	CompleteMission,0
	* Type:	Strike
	* GoalParameters:	Id&strike_03_PahrasRock_mythic

## ql_raid_019

### qr_019
	* Rewards:	rw_i_strike_quest_breach_N:1
	* XPMod:	0
	* Tier:	3
	* Goals:	CompleteMission,0
	* Type:	Strike
	* GoalParameters:	Id&strike_04_Breach

## ql_raid_020

### qr_020
	* Rewards:	rw_i_strike_quest_breach_H:1
	* XPMod:	0
	* Tier:	4
	* Goals:	CompleteMission,0
	* Type:	Strike
	* GoalParameters:	Id&strike_04_Breach_heroic

## ql_raid_023

### qr_023
	* Rewards:	rw_i_strike_quest_nightmareGulf_N:1
	* XPMod:	0
	* Tier:	4
	* Goals:	CompleteMission,0
	* Type:	Strike
	* GoalParameters:	Id&strike_05_NightmareGulf

## ql_event_test_1

### qe_test_eventtestquest_1
	* Rewards:	LP:6	OF:3	rw_recruitToken_hiig_random:1
	* ScheduleType:	Hidden
	* XPMod:	10
	* EndOffset:	0:0:0
	* Tier:	1
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Category&Crafting;Amount&10

## ql_event_test_2

### qe_test_eventtestquest_2
	* Rewards:	insig_r3:23	BB:10	rw_cryo_hiig_random:1
	* ScheduleType:	Hidden
	* XPMod:	10
	* EndOffset:	0:0:0
	* Tier:	1
	* Goals:	Pay,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Id&CR;Amount&10

## ql_event_test_3

### qe_test_eventtestquest_3
	* Rewards:	intmed_ship_small_t3:60	intmed_weapon_small_t3:60	intmed_module_small_t3:60
	* ScheduleType:	Locked
	* XPMod:	10
	* EndOffset:	0:0:0
	* Tier:	1
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Amount&1

## ql_yaot_spring_2023_daily_A_t2

### qe_yaot_spring_2023_daily_A_t2
	* Rewards:	Z1:10
	* ScheduleType:	Hidden
	* XPMod:	45
	* EndOffset:	0:0:0
	* EventId:	event_season_yaoSpr_2023
	* Tier:	2
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Id&RP;Amount&200;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

## ql_yaot_spring_2023_daily_B_t2

### qe_yaot_spring_2023_daily_B_t2
	* Rewards:	Z1:10
	* ScheduleType:	Hidden
	* XPMod:	45
	* EndOffset:	0:0:0
	* EventId:	event_season_yaoSpr_2023
	* Tier:	2
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Id&ShipsDestroyedTanoch;Amount&10

## ql_yaot_spring_2023_daily_C_t3

### qe_yaot_spring_2023_daily_C_t3
	* Rewards:	Z1:10
	* ScheduleType:	Hidden
	* XPMod:	135
	* EndOffset:	0:0:0
	* EventId:	event_season_yaoSpr_2023
	* Tier:	3
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Ids&Mined3E_Mined3F_Mined3G_Mined3H_Mined4E_Mined4F_Mined4G_Mined4H;Amount&100

## ql_yaot_spring_2023_daily_D_t3

### qe_yaot_spring_2023_daily_D_t3
	* Rewards:	Z1:10
	* ScheduleType:	Hidden
	* XPMod:	135
	* EndOffset:	0:0:0
	* EventId:	event_season_yaoSpr_2023
	* Tier:	3
	* Goals:	CompleteQuest,0
	* Type:	Event
	* StartOffset:	0:0:0
	* RepetitionType:	Daily
	* GoalParameters:	Amount&5;Tags&Faction_Yaot

## ql_event_yaot_spring_2023

### qe_yaot_spring_2023_day1
	* Rewards:	Z1:20
	* ScheduleType:	Hidden
	* XPMod:	15
	* EndOffset:	0:0:0
	* EventId:	event_season_yaoSpr_2023
	* Tier:	1
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Id&Mined;Amount&750

### qe_yaot_spring_2023_day2
	* Rewards:	Z1:20
	* ScheduleType:	Locked
	* XPMod:	16
	* EndOffset:	0:0:0
	* EventId:	event_season_yaoSpr_2023
	* Tier:	1
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	1:0:0
	* GoalParameters:	Amount&3;Mode&Generated

### qe_yaot_spring_2023_day3
	* Rewards:	Z1:20
	* ScheduleType:	Locked
	* XPMod:	17
	* EndOffset:	0:0:0
	* EventId:	event_season_yaoSpr_2023
	* Tier:	1
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	2:0:0
	* GoalParameters:	Category&Refining;Amount&500

### qe_yaot_spring_2023_day4
	* Rewards:	Z1:20
	* ScheduleType:	Locked
	* XPMod:	18
	* EndOffset:	0:0:0
	* EventId:	event_season_yaoSpr_2023
	* Tier:	1
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	3:0:0
	* GoalParameters:	Tags&Insignia;Amount&15;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_yaot_spring_2023_day5
	* Rewards:	Z1:20
	* ScheduleType:	Locked
	* XPMod:	19
	* EndOffset:	0:0:0
	* EventId:	event_season_yaoSpr_2023
	* Tier:	1
	* Goals:	UpgradeOfficer,0
	* Type:	Event
	* StartOffset:	4:0:0
	* GoalParameters:	Amount&3

### qe_yaot_spring_2023_day6
	* Rewards:	Z1:20
	* ScheduleType:	Locked
	* XPMod:	20
	* EndOffset:	0:0:0
	* EventId:	event_season_yaoSpr_2023
	* Tier:	1
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	5:0:0
	* GoalParameters:	Amount&3;Mode&Generated

### qe_yaot_spring_2023_day7
	* Rewards:	Z1:20
	* ScheduleType:	Locked
	* XPMod:	21
	* EndOffset:	0:0:0
	* EventId:	event_season_yaoSpr_2023
	* Tier:	1
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	6:0:0
	* GoalParameters:	Id&Mined;Amount&750

### qe_yaot_spring_2023_day8
	* Rewards:	Z1:20
	* ScheduleType:	Locked
	* XPMod:	22
	* EndOffset:	0:0:0
	* EventId:	event_season_yaoSpr_2023
	* Tier:	1
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	7:0:0
	* GoalParameters:	Tags&ProgenitorRelic;Amount&1;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_yaot_spring_2023_day9
	* Rewards:	Z1:20
	* ScheduleType:	Locked
	* XPMod:	23
	* EndOffset:	0:0:0
	* EventId:	event_season_yaoSpr_2023
	* Tier:	1
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	8:0:0
	* GoalParameters:	Category&Refining;Amount&500

### qe_yaot_spring_2023_day10
	* Rewards:	Z1:20
	* ScheduleType:	Locked
	* XPMod:	24
	* EndOffset:	0:0:0
	* EventId:	event_season_yaoSpr_2023
	* Tier:	1
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	9:0:0
	* GoalParameters:	Amount&3;Mode&Generated

### qe_yaot_spring_2023_day11
	* Rewards:	Z1:20
	* ScheduleType:	Locked
	* XPMod:	25
	* EndOffset:	0:0:0
	* EventId:	event_season_yaoSpr_2023
	* Tier:	1
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	10:0:0
	* GoalParameters:	Id&Mined;Amount&750

### qe_yaot_spring_2023_day12
	* Rewards:	Z1:20
	* ScheduleType:	Locked
	* XPMod:	26
	* EndOffset:	0:0:0
	* EventId:	event_season_yaoSpr_2023
	* Tier:	1
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	11:0:0
	* GoalParameters:	Tags&Insignia;Amount&15;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_yaot_spring_2023_day13
	* Rewards:	Z1:20
	* ScheduleType:	Locked
	* XPMod:	27
	* EndOffset:	0:0:0
	* EventId:	event_season_yaoSpr_2023
	* Tier:	1
	* Goals:	UpgradeOfficer,0
	* Type:	Event
	* StartOffset:	12:0:0
	* GoalParameters:	Amount&3

### qe_yaot_spring_2023_day14
	* Rewards:	Z1:20	rw_recruitToken_hiig_minEpic:1
	* ScheduleType:	Locked
	* XPMod:	28
	* EndOffset:	0:0:0
	* EventId:	event_season_yaoSpr_2023
	* Tier:	3
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	13:0:0
	* GoalParameters:	Id&story_C01_Tanochet_event_heroic

## ql_event_amaSum_2023_t1

### qe_amaSum_2023_day1_t1
	* Rewards:	Z4:20
	* ScheduleType:	Hidden
	* XPMod:	15
	* EndOffset:	2:0:0
	* EventId:	event_season_amaSum_2023_t1
	* Tier:	1
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Category&Refining;Tags&Asteroid_Refined_T1up;Amount&350

### qe_amaSum_2023_day2_t1
	* Rewards:	Z4:20
	* ScheduleType:	Locked
	* XPMod:	16
	* EndOffset:	2:0:0
	* EventId:	event_season_amaSum_2023_t1
	* Tier:	1
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	1:0:0
	* GoalParameters:	Amount&3;Tags&T1up;Mode&Generated

### qe_amaSum_2023_day3_t1
	* Rewards:	Z4:20
	* ScheduleType:	Locked
	* XPMod:	17
	* EndOffset:	2:0:0
	* EventId:	event_season_amaSum_2023_t1
	* Tier:	1
	* Goals:	UpgradeOfficer,0
	* Type:	Event
	* StartOffset:	2:0:0
	* GoalParameters:	Amount&3

### qe_amaSum_2023_day4_t1
	* Rewards:	Z4:20
	* ScheduleType:	Locked
	* XPMod:	18
	* EndOffset:	2:0:0
	* EventId:	event_season_amaSum_2023_t1
	* Tier:	1
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	3:0:0
	* GoalParameters:	Amount&3;Tags&T1up;Mode&Generated

### qe_amaSum_2023_day5_t1
	* Rewards:	Z4:20
	* ScheduleType:	Locked
	* XPMod:	19
	* EndOffset:	2:0:0
	* EventId:	event_season_amaSum_2023_t1
	* Tier:	1
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	4:0:0
	* GoalParameters:	Category&Refining;Tags&Asteroid_Refined_T1up;Amount&350

### qe_amaSum_2023_day6_t1
	* Rewards:	Z4:20
	* ScheduleType:	Locked
	* XPMod:	20
	* EndOffset:	2:0:0
	* EventId:	event_season_amaSum_2023_t1
	* Tier:	1
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	5:0:0
	* GoalParameters:	Amount&3;Tags&T1up;Mode&Generated

### qe_amaSum_2023_day7_t1
	* Rewards:	Z4:20
	* ScheduleType:	Locked
	* XPMod:	21
	* EndOffset:	2:0:0
	* EventId:	event_season_amaSum_2023_t1
	* Tier:	1
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	6:0:0
	* GoalParameters:	Tags&Insignia_T1up;Amount&15;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_amaSum_2023_day8_t1
	* Rewards:	Z4:20
	* ScheduleType:	Locked
	* XPMod:	22
	* EndOffset:	2:0:0
	* EventId:	event_season_amaSum_2023_t1
	* Tier:	1
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	7:0:0
	* GoalParameters:	Amount&3;Tags&T1up;Mode&Generated

### qe_amaSum_2023_day9_t1
	* Rewards:	Z4:20
	* ScheduleType:	Locked
	* XPMod:	23
	* EndOffset:	2:0:0
	* EventId:	event_season_amaSum_2023_t1
	* Tier:	1
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	8:0:0
	* GoalParameters:	Category&Refining;Tags&Asteroid_Refined_T1up;Amount&350

### qe_amaSum_2023_day10_t1
	* Rewards:	Z4:20
	* ScheduleType:	Locked
	* XPMod:	24
	* EndOffset:	2:0:0
	* EventId:	event_season_amaSum_2023_t1
	* Tier:	1
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	9:0:0
	* GoalParameters:	Amount&3;Tags&T1up;Mode&Generated

### qe_amaSum_2023_day11_t1
	* Rewards:	Z4:20
	* ScheduleType:	Locked
	* XPMod:	25
	* EndOffset:	2:0:0
	* EventId:	event_season_amaSum_2023_t1
	* Tier:	1
	* Goals:	UpgradeOfficer,0
	* Type:	Event
	* StartOffset:	10:0:0
	* GoalParameters:	Amount&3

### qe_amaSum_2023_day12_t1
	* Rewards:	Z4:20
	* ScheduleType:	Locked
	* XPMod:	26
	* EndOffset:	2:0:0
	* EventId:	event_season_amaSum_2023_t1
	* Tier:	1
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	11:0:0
	* GoalParameters:	Amount&3;Tags&T1up;Mode&Generated

### qe_amaSum_2023_day13_t1
	* Rewards:	Z4:20
	* ScheduleType:	Locked
	* XPMod:	27
	* EndOffset:	2:0:0
	* EventId:	event_season_amaSum_2023_t1
	* Tier:	1
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	12:0:0
	* GoalParameters:	Category&Refining;Tags&Asteroid_Refined_T1up;Amount&350

### qe_amaSum_2023_day14_t1
	* Rewards:	Z4:20
	* ScheduleType:	Locked
	* XPMod:	28
	* EndOffset:	2:0:0
	* EventId:	event_season_amaSum_2023_t1
	* Tier:	1
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	13:0:0
	* GoalParameters:	Tags&Insignia_T1up;Amount&15;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_amaSum_2023_day15_t1
	* Rewards:	Z4:20	HC:100	ama_sc_assa_01_fu_t2:1
	* ScheduleType:	Locked
	* XPMod:	35
	* EndOffset:	2:0:0
	* EventId:	event_season_amaSum_2023_t1
	* Tier:	1
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	14:0:0
	* GoalParameters:	Id&event_01_StationDefense

## ql_event_amaSum_2023_t2

### qe_amaSum_2023_day1_t2
	* Rewards:	Z4:20
	* ScheduleType:	Hidden
	* XPMod:	45
	* EndOffset:	2:0:0
	* EventId:	event_season_amaSum_2023_t2
	* Tier:	2
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Category&Refining;Tags&Asteroid_Refined_T2up;Amount&400

### qe_amaSum_2023_day2_t2
	* Rewards:	Z4:20
	* ScheduleType:	Locked
	* XPMod:	48
	* EndOffset:	2:0:0
	* EventId:	event_season_amaSum_2023_t2
	* Tier:	2
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	1:0:0
	* GoalParameters:	Amount&3;Tags&T2up;Mode&Generated

### qe_amaSum_2023_day3_t2
	* Rewards:	Z4:20
	* ScheduleType:	Locked
	* XPMod:	51
	* EndOffset:	2:0:0
	* EventId:	event_season_amaSum_2023_t2
	* Tier:	2
	* Goals:	UpgradeOfficer,0
	* Type:	Event
	* StartOffset:	2:0:0
	* GoalParameters:	Amount&3

### qe_amaSum_2023_day4_t2
	* Rewards:	Z4:20
	* ScheduleType:	Locked
	* XPMod:	54
	* EndOffset:	2:0:0
	* EventId:	event_season_amaSum_2023_t2
	* Tier:	2
	* Goals:	CompleteQuest,0
	* Type:	Event
	* StartOffset:	3:0:0
	* GoalParameters:	Amount&5;Tags&Faction_T2up

### qe_amaSum_2023_day5_t2
	* Rewards:	Z4:20
	* ScheduleType:	Locked
	* XPMod:	57
	* EndOffset:	2:0:0
	* EventId:	event_season_amaSum_2023_t2
	* Tier:	2
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	4:0:0
	* GoalParameters:	Category&Refining;Tags&Asteroid_Refined_T2up;Amount&400

### qe_amaSum_2023_day6_t2
	* Rewards:	Z4:20
	* ScheduleType:	Locked
	* XPMod:	60
	* EndOffset:	2:0:0
	* EventId:	event_season_amaSum_2023_t2
	* Tier:	2
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	5:0:0
	* GoalParameters:	Amount&3;Tags&T2up;Mode&Generated

### qe_amaSum_2023_day7_t2
	* Rewards:	Z4:20
	* ScheduleType:	Locked
	* XPMod:	63
	* EndOffset:	2:0:0
	* EventId:	event_season_amaSum_2023_t2
	* Tier:	2
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	6:0:0
	* GoalParameters:	Tags&Insignia_T2up;Amount&15;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_amaSum_2023_day8_t2
	* Rewards:	Z4:20
	* ScheduleType:	Locked
	* XPMod:	66
	* EndOffset:	2:0:0
	* EventId:	event_season_amaSum_2023_t2
	* Tier:	2
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	7:0:0
	* GoalParameters:	Amount&1;Mode&Strike;Tags&T1up

### qe_amaSum_2023_day9_t2
	* Rewards:	Z4:20
	* ScheduleType:	Locked
	* XPMod:	69
	* EndOffset:	2:0:0
	* EventId:	event_season_amaSum_2023_t2
	* Tier:	2
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	8:0:0
	* GoalParameters:	Category&Refining;Tags&Asteroid_Refined_T2up;Amount&400

### qe_amaSum_2023_day10_t2
	* Rewards:	Z4:20
	* ScheduleType:	Locked
	* XPMod:	72
	* EndOffset:	2:0:0
	* EventId:	event_season_amaSum_2023_t2
	* Tier:	2
	* Goals:	CompleteQuest,0
	* Type:	Event
	* StartOffset:	9:0:0
	* GoalParameters:	Amount&5;Tags&Faction_T2up

### qe_amaSum_2023_day11_t2
	* Rewards:	Z4:20
	* ScheduleType:	Locked
	* XPMod:	75
	* EndOffset:	2:0:0
	* EventId:	event_season_amaSum_2023_t2
	* Tier:	2
	* Goals:	UpgradeOfficer,0
	* Type:	Event
	* StartOffset:	10:0:0
	* GoalParameters:	Amount&3

### qe_amaSum_2023_day12_t2
	* Rewards:	Z4:20
	* ScheduleType:	Locked
	* XPMod:	78
	* EndOffset:	2:0:0
	* EventId:	event_season_amaSum_2023_t2
	* Tier:	2
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	11:0:0
	* GoalParameters:	Amount&1;Mode&Strike;Tags&T1up

### qe_amaSum_2023_day13_t2
	* Rewards:	Z4:20
	* ScheduleType:	Locked
	* XPMod:	81
	* EndOffset:	2:0:0
	* EventId:	event_season_amaSum_2023_t2
	* Tier:	2
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	12:0:0
	* GoalParameters:	Category&Refining;Tags&Asteroid_Refined_T2up;Amount&400

### qe_amaSum_2023_day14_t2
	* Rewards:	Z4:20
	* ScheduleType:	Locked
	* XPMod:	84
	* EndOffset:	2:0:0
	* EventId:	event_season_amaSum_2023_t2
	* Tier:	2
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	13:0:0
	* GoalParameters:	Tags&Insignia_T2up;Amount&15;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_amaSum_2023_day15_t2
	* Rewards:	Z4:20	HC:100	ama_sc_assa_01_fu_t3:1
	* ScheduleType:	Locked
	* XPMod:	105
	* EndOffset:	2:0:0
	* EventId:	event_season_amaSum_2023_t2
	* Tier:	2
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	14:0:0
	* GoalParameters:	Id&event_02_StationDefense

## ql_event_amaSum_2023_t3

### qe_amaSum_2023_day1_t3
	* Rewards:	Z4:20
	* ScheduleType:	Hidden
	* XPMod:	135
	* EndOffset:	2:0:0
	* EventId:	event_season_amaSum_2023_t3
	* Tier:	3
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Category&Refining;Tags&Asteroid_Refined_T3up;Amount&450

### qe_amaSum_2023_day2_t3
	* Rewards:	Z4:20
	* ScheduleType:	Locked
	* XPMod:	144
	* EndOffset:	2:0:0
	* EventId:	event_season_amaSum_2023_t3
	* Tier:	3
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	1:0:0
	* GoalParameters:	Amount&3;Tags&T3up;Mode&Generated

### qe_amaSum_2023_day3_t3
	* Rewards:	Z4:20
	* ScheduleType:	Locked
	* XPMod:	153
	* EndOffset:	2:0:0
	* EventId:	event_season_amaSum_2023_t3
	* Tier:	3
	* Goals:	UpgradeOfficer,0
	* Type:	Event
	* StartOffset:	2:0:0
	* GoalParameters:	Amount&3

### qe_amaSum_2023_day4_t3
	* Rewards:	Z4:20
	* ScheduleType:	Locked
	* XPMod:	162
	* EndOffset:	2:0:0
	* EventId:	event_season_amaSum_2023_t3
	* Tier:	3
	* Goals:	CompleteQuest,0
	* Type:	Event
	* StartOffset:	3:0:0
	* GoalParameters:	Amount&5;Tags&Faction_T3up

### qe_amaSum_2023_day5_t3
	* Rewards:	Z4:20
	* ScheduleType:	Locked
	* XPMod:	171
	* EndOffset:	2:0:0
	* EventId:	event_season_amaSum_2023_t3
	* Tier:	3
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	4:0:0
	* GoalParameters:	Tags&Gas_T3up;Amount&800;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

### qe_amaSum_2023_day6_t3
	* Rewards:	Z4:20
	* ScheduleType:	Locked
	* XPMod:	180
	* EndOffset:	2:0:0
	* EventId:	event_season_amaSum_2023_t3
	* Tier:	3
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	5:0:0
	* GoalParameters:	Amount&3;Tags&T3up;Mode&Generated

### qe_amaSum_2023_day7_t3
	* Rewards:	Z4:20
	* ScheduleType:	Locked
	* XPMod:	189
	* EndOffset:	2:0:0
	* EventId:	event_season_amaSum_2023_t3
	* Tier:	3
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	6:0:0
	* GoalParameters:	Tags&Insignia_T3up;Amount&15;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_amaSum_2023_day8_t3
	* Rewards:	Z4:20
	* ScheduleType:	Locked
	* XPMod:	198
	* EndOffset:	2:0:0
	* EventId:	event_season_amaSum_2023_t3
	* Tier:	3
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	7:0:0
	* GoalParameters:	Amount&3;Mode&Strike;Tags&T2up

### qe_amaSum_2023_day9_t3
	* Rewards:	Z4:20
	* ScheduleType:	Locked
	* XPMod:	207
	* EndOffset:	2:0:0
	* EventId:	event_season_amaSum_2023_t3
	* Tier:	3
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	8:0:0
	* GoalParameters:	Category&Refining;Tags&Asteroid_Refined_T3up;Amount&450

### qe_amaSum_2023_day10_t3
	* Rewards:	Z4:20
	* ScheduleType:	Locked
	* XPMod:	216
	* EndOffset:	2:0:0
	* EventId:	event_season_amaSum_2023_t3
	* Tier:	3
	* Goals:	CompleteQuest,0
	* Type:	Event
	* StartOffset:	9:0:0
	* GoalParameters:	Amount&5;Tags&Faction_T3up

### qe_amaSum_2023_day11_t3
	* Rewards:	Z4:20
	* ScheduleType:	Locked
	* XPMod:	225
	* EndOffset:	2:0:0
	* EventId:	event_season_amaSum_2023_t3
	* Tier:	3
	* Goals:	UpgradeOfficer,0
	* Type:	Event
	* StartOffset:	10:0:0
	* GoalParameters:	Amount&3

### qe_amaSum_2023_day12_t3
	* Rewards:	Z4:20
	* ScheduleType:	Locked
	* XPMod:	234
	* EndOffset:	2:0:0
	* EventId:	event_season_amaSum_2023_t3
	* Tier:	3
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	11:0:0
	* GoalParameters:	Amount&3;Mode&Strike;Tags&T2up

### qe_amaSum_2023_day13_t3
	* Rewards:	Z4:20
	* ScheduleType:	Locked
	* XPMod:	243
	* EndOffset:	2:0:0
	* EventId:	event_season_amaSum_2023_t3
	* Tier:	3
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	12:0:0
	* GoalParameters:	Tags&Gas_T3up;Amount&800;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

### qe_amaSum_2023_day14_t3
	* Rewards:	Z4:20
	* ScheduleType:	Locked
	* XPMod:	252
	* EndOffset:	2:0:0
	* EventId:	event_season_amaSum_2023_t3
	* Tier:	3
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	13:0:0
	* GoalParameters:	Tags&Insignia_T3up;Amount&15;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_amaSum_2023_day15_t3
	* Rewards:	Z4:20	HC:100	ama_sc_assa_01_fu_t4:1
	* ScheduleType:	Locked
	* XPMod:	315
	* EndOffset:	2:0:0
	* EventId:	event_season_amaSum_2023_t3
	* Tier:	3
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	14:0:0
	* GoalParameters:	Id&event_03_StationDefense

## ql_event_amaSum_2023_t4

### qe_amaSum_2023_day1_t4
	* Rewards:	Z4:20
	* ScheduleType:	Hidden
	* XPMod:	405
	* EndOffset:	2:0:0
	* EventId:	event_season_amaSum_2023_t4
	* Tier:	4
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Category&Refining;Tags&Asteroid_Refined_T4up;Amount&500

### qe_amaSum_2023_day2_t4
	* Rewards:	Z4:20
	* ScheduleType:	Locked
	* XPMod:	432
	* EndOffset:	2:0:0
	* EventId:	event_season_amaSum_2023_t4
	* Tier:	4
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	1:0:0
	* GoalParameters:	Amount&3;Tags&T4up;Mode&Generated

### qe_amaSum_2023_day3_t4
	* Rewards:	Z4:20
	* ScheduleType:	Locked
	* XPMod:	459
	* EndOffset:	2:0:0
	* EventId:	event_season_amaSum_2023_t4
	* Tier:	4
	* Goals:	UpgradeOfficer,0
	* Type:	Event
	* StartOffset:	2:0:0
	* GoalParameters:	Amount&3

### qe_amaSum_2023_day4_t4
	* Rewards:	Z4:20
	* ScheduleType:	Locked
	* XPMod:	486
	* EndOffset:	2:0:0
	* EventId:	event_season_amaSum_2023_t4
	* Tier:	4
	* Goals:	CompleteQuest,0
	* Type:	Event
	* StartOffset:	3:0:0
	* GoalParameters:	Amount&5;Tags&Faction_Amassari_T4up

### qe_amaSum_2023_day5_t4
	* Rewards:	Z4:20
	* ScheduleType:	Locked
	* XPMod:	513
	* EndOffset:	2:0:0
	* EventId:	event_season_amaSum_2023_t4
	* Tier:	4
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	4:0:0
	* GoalParameters:	Tags&Gas_T4up;Amount&1000;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

### qe_amaSum_2023_day6_t4
	* Rewards:	Z4:20
	* ScheduleType:	Locked
	* XPMod:	540
	* EndOffset:	2:0:0
	* EventId:	event_season_amaSum_2023_t4
	* Tier:	4
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	5:0:0
	* GoalParameters:	Amount&3;Tags&T4up;Mode&Generated

### qe_amaSum_2023_day7_t4
	* Rewards:	Z4:20
	* ScheduleType:	Locked
	* XPMod:	567
	* EndOffset:	2:0:0
	* EventId:	event_season_amaSum_2023_t4
	* Tier:	4
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	6:0:0
	* GoalParameters:	Tags&Insignia_T4up;Amount&15;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_amaSum_2023_day8_t4
	* Rewards:	Z4:20
	* ScheduleType:	Locked
	* XPMod:	594
	* EndOffset:	2:0:0
	* EventId:	event_season_amaSum_2023_t4
	* Tier:	4
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	7:0:0
	* GoalParameters:	Amount&5;Mode&Strike;Tags&T3up

### qe_amaSum_2023_day9_t4
	* Rewards:	Z4:20
	* ScheduleType:	Locked
	* XPMod:	621
	* EndOffset:	2:0:0
	* EventId:	event_season_amaSum_2023_t4
	* Tier:	4
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	8:0:0
	* GoalParameters:	Category&Refining;Tags&Asteroid_Refined_T4up;Amount&500

### qe_amaSum_2023_day10_t4
	* Rewards:	Z4:20
	* ScheduleType:	Locked
	* XPMod:	648
	* EndOffset:	2:0:0
	* EventId:	event_season_amaSum_2023_t4
	* Tier:	4
	* Goals:	CompleteQuest,0
	* Type:	Event
	* StartOffset:	9:0:0
	* GoalParameters:	Amount&5;Tags&Faction_Amassari_T4up

### qe_amaSum_2023_day11_t4
	* Rewards:	Z4:20
	* ScheduleType:	Locked
	* XPMod:	675
	* EndOffset:	2:0:0
	* EventId:	event_season_amaSum_2023_t4
	* Tier:	4
	* Goals:	UpgradeOfficer,0
	* Type:	Event
	* StartOffset:	10:0:0
	* GoalParameters:	Amount&3

### qe_amaSum_2023_day12_t4
	* Rewards:	Z4:20
	* ScheduleType:	Locked
	* XPMod:	702
	* EndOffset:	2:0:0
	* EventId:	event_season_amaSum_2023_t4
	* Tier:	4
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	11:0:0
	* GoalParameters:	Amount&5;Mode&Strike;Tags&T3up

### qe_amaSum_2023_day13_t4
	* Rewards:	Z4:20
	* ScheduleType:	Locked
	* XPMod:	729
	* EndOffset:	2:0:0
	* EventId:	event_season_amaSum_2023_t4
	* Tier:	4
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	12:0:0
	* GoalParameters:	Tags&Gas_T4up;Amount&1000;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

### qe_amaSum_2023_day14_t4
	* Rewards:	Z4:20
	* ScheduleType:	Locked
	* XPMod:	756
	* EndOffset:	2:0:0
	* EventId:	event_season_amaSum_2023_t4
	* Tier:	4
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	13:0:0
	* GoalParameters:	Tags&Insignia_T4up;Amount&15;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_amaSum_2023_day15_t4
	* Rewards:	Z4:20	HC:100	ama_sc_assa_01_fu_t4:2
	* ScheduleType:	Locked
	* XPMod:	945
	* EndOffset:	2:0:0
	* EventId:	event_season_amaSum_2023_t4
	* Tier:	4
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	14:0:0
	* GoalParameters:	Id&event_04_StationDefense

## ql_7days_mar_2024_day1_t1

### qe_7days_mar_2024_day1_a_t1
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	255
	* EndOffset:	-9:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t1
	* Tier:	1
	* Goals:	Scan,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Tags&InSystem_T1up;Amount&10;Analyzed&True

### qe_7days_mar_2024_day1_b_t1
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	270
	* EndOffset:	-9:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t1
	* Tier:	1
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Ids&ShipsDestroyedT1_ShipsDestroyedT2_ShipsDestroyedT3_ShipsDestroyedT4;Amount&15

### qe_7days_mar_2024_day1_c_t1
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	285
	* EndOffset:	-9:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t1
	* Tier:	1
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Tags&Asteroid_Crud_T1up;Amount&800;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_mar_2024_day1_d_t1
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	300
	* EndOffset:	-9:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t1
	* Tier:	1
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Tags&RareEarth_T1up;Amount&15;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

## ql_7days_mar_2024_day1_t2

### qe_7days_mar_2024_day1_a_t2
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	255
	* EndOffset:	-9:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t2
	* Tier:	2
	* Goals:	Scan,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Tags&InSystem_T2up;Amount&10;Analyzed&True

### qe_7days_mar_2024_day1_b_t2
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	270
	* EndOffset:	-9:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t2
	* Tier:	2
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Ids&ShipsDestroyedT2_ShipsDestroyedT3_ShipsDestroyedT4;Amount&15

### qe_7days_mar_2024_day1_c_t2
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	285
	* EndOffset:	-9:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t2
	* Tier:	2
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Tags&Asteroid_Crud_T2up;Amount&1000;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_mar_2024_day1_d_t2
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	300
	* EndOffset:	-9:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t2
	* Tier:	2
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Tags&RareEarth_T2up;Amount&15;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

## ql_7days_mar_2024_day1_t3

### qe_7days_mar_2024_day1_a_t3
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	255
	* EndOffset:	-9:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t3
	* Tier:	3
	* Goals:	Scan,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Tags&InSystem_T3up;Amount&10;Analyzed&True

### qe_7days_mar_2024_day1_b_t3
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	270
	* EndOffset:	-9:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t3
	* Tier:	3
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Ids&ShipsDestroyedT3_ShipsDestroyedT4;Amount&15

### qe_7days_mar_2024_day1_c_t3
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	285
	* EndOffset:	-9:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t3
	* Tier:	3
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Tags&Gas_T3up;Amount&800;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_mar_2024_day1_d_t3
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	300
	* EndOffset:	-9:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t3
	* Tier:	3
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Tags&RareEarth_T3up;Amount&15;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

## ql_7days_mar_2024_day1_t4

### qe_7days_mar_2024_day1_a_t4
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	255
	* EndOffset:	-9:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t4
	* Tier:	4
	* Goals:	Scan,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Tags&InSystem_T4up;Amount&10;Analyzed&True

### qe_7days_mar_2024_day1_b_t4
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	270
	* EndOffset:	-9:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t4
	* Tier:	4
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Id&ShipsDestroyedT4;Amount&15

### qe_7days_mar_2024_day1_c_t4
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	285
	* EndOffset:	-9:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t4
	* Tier:	4
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Tags&Gas_T4up;Amount&1000;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_mar_2024_day1_d_t4
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	300
	* EndOffset:	-9:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t4
	* Tier:	4
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Tags&RareEarth_T4up;Amount&15;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

## ql_7days_mar_2024_day2_t1

### qe_7days_mar_2024_day2_a_t1
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	255
	* EndOffset:	-8:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t1
	* Tier:	1
	* Goals:	CompleteQuest,0
	* Type:	Event
	* StartOffset:	1:0:0
	* GoalParameters:	Amount&5;Tags&T1up

### qe_7days_mar_2024_day2_b_t1
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	270
	* EndOffset:	-8:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t1
	* Tier:	1
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	1:0:0
	* GoalParameters:	Amount&3;Tags&T1up

### qe_7days_mar_2024_day2_c_t1
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	285
	* EndOffset:	-8:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t1
	* Tier:	1
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	1:0:0
	* GoalParameters:	Tags&Insignia_T1up;Amount&50;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_mar_2024_day2_d_t1
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	300
	* EndOffset:	-8:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t1
	* Tier:	1
	* Goals:	UpgradeOfficer,0
	* Type:	Event
	* StartOffset:	1:0:0
	* GoalParameters:	Amount&1

## ql_7days_mar_2024_day2_t2

### qe_7days_mar_2024_day2_a_t2
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	255
	* EndOffset:	-8:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t2
	* Tier:	2
	* Goals:	CompleteQuest,0
	* Type:	Event
	* StartOffset:	1:0:0
	* GoalParameters:	Amount&5;Tags&Faction_T2up

### qe_7days_mar_2024_day2_b_t2
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	270
	* EndOffset:	-8:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t2
	* Tier:	2
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	1:0:0
	* GoalParameters:	Amount&3;Mode&Faction;Tags&T2up

### qe_7days_mar_2024_day2_c_t2
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	285
	* EndOffset:	-8:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t2
	* Tier:	2
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	1:0:0
	* GoalParameters:	Ids&RepTr1_RepTanoch_RepYaot_RepAmassari;Amount&135

### qe_7days_mar_2024_day2_d_t2
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	300
	* EndOffset:	-8:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t2
	* Tier:	2
	* Goals:	UpgradeOfficer,0
	* Type:	Event
	* StartOffset:	1:0:0
	* GoalParameters:	Amount&2

## ql_7days_mar_2024_day2_t3

### qe_7days_mar_2024_day2_a_t3
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	255
	* EndOffset:	-8:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t3
	* Tier:	3
	* Goals:	CompleteQuest,0
	* Type:	Event
	* StartOffset:	1:0:0
	* GoalParameters:	Amount&5;Tags&Faction_T3up

### qe_7days_mar_2024_day2_b_t3
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	270
	* EndOffset:	-8:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t3
	* Tier:	3
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	1:0:0
	* GoalParameters:	Amount&3;Mode&Faction;Tags&T3up

### qe_7days_mar_2024_day2_c_t3
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	285
	* EndOffset:	-8:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t3
	* Tier:	3
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	1:0:0
	* GoalParameters:	Ids&RepTr1_RepTanoch_RepYaot_RepAmassari;Amount&180

### qe_7days_mar_2024_day2_d_t3
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	300
	* EndOffset:	-8:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t3
	* Tier:	3
	* Goals:	UpgradeOfficer,0
	* Type:	Event
	* StartOffset:	1:0:0
	* GoalParameters:	Amount&3

## ql_7days_mar_2024_day2_t4

### qe_7days_mar_2024_day2_a_t4
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	255
	* EndOffset:	-8:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t4
	* Tier:	4
	* Goals:	CompleteQuest,0
	* Type:	Event
	* StartOffset:	1:0:0
	* GoalParameters:	Amount&5;Tags&Faction_T4up

### qe_7days_mar_2024_day2_b_t4
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	270
	* EndOffset:	-8:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t4
	* Tier:	4
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	1:0:0
	* GoalParameters:	Amount&3;Mode&Faction;Tags&T4up

### qe_7days_mar_2024_day2_c_t4
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	285
	* EndOffset:	-8:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t4
	* Tier:	4
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	1:0:0
	* GoalParameters:	Ids&RepTr1_RepTanoch_RepYaot_RepAmassari;Amount&225

### qe_7days_mar_2024_day2_d_t4
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	300
	* EndOffset:	-8:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t4
	* Tier:	4
	* Goals:	UpgradeOfficer,0
	* Type:	Event
	* StartOffset:	1:0:0
	* GoalParameters:	Amount&5

## ql_7days_mar_2024_day3_t1

### qe_7days_mar_2024_day3_a_t1
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	255
	* EndOffset:	-7:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t1
	* Tier:	1
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	2:0:0
	* GoalParameters:	Tags&Asteroid_Crud_T1up;Amount&800;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_mar_2024_day3_b_t1
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	270
	* EndOffset:	-7:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t1
	* Tier:	1
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	2:0:0
	* GoalParameters:	Category&Refining;Tags&Asteroid_Refined_T1up;Amount&500

### qe_7days_mar_2024_day3_c_t1
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	285
	* EndOffset:	-7:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t1
	* Tier:	1
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	2:0:0
	* GoalParameters:	Category&Crafting;Tags&T1up;Amount&1

### qe_7days_mar_2024_day3_d_t1
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	300
	* EndOffset:	-7:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t1
	* Tier:	1
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	2:0:0
	* GoalParameters:	Id&CR;Amount&150;ExcludedSources&BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

## ql_7days_mar_2024_day3_t2

### qe_7days_mar_2024_day3_a_t2
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	255
	* EndOffset:	-7:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t2
	* Tier:	2
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	2:0:0
	* GoalParameters:	Tags&Asteroid_Crud_T2up;Amount&1000;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_mar_2024_day3_b_t2
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	270
	* EndOffset:	-7:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t2
	* Tier:	2
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	2:0:0
	* GoalParameters:	Category&Refining;Tags&Asteroid_Refined_T2up;Amount&500

### qe_7days_mar_2024_day3_c_t2
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	285
	* EndOffset:	-7:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t2
	* Tier:	2
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	2:0:0
	* GoalParameters:	Category&Crafting;Tags&Part_T2up;Amount&25

### qe_7days_mar_2024_day3_d_t2
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	300
	* EndOffset:	-7:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t2
	* Tier:	2
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	2:0:0
	* GoalParameters:	Id&CR;Amount&300;ExcludedSources&BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

## ql_7days_mar_2024_day3_t3

### qe_7days_mar_2024_day3_a_t3
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	255
	* EndOffset:	-7:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t3
	* Tier:	3
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	2:0:0
	* GoalParameters:	Tags&Asteroid_Crud_T3up;Amount&1200;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_mar_2024_day3_b_t3
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	270
	* EndOffset:	-7:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t3
	* Tier:	3
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	2:0:0
	* GoalParameters:	Category&Refining;Tags&Asteroid_Refined_T3up;Amount&500

### qe_7days_mar_2024_day3_c_t3
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	285
	* EndOffset:	-7:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t3
	* Tier:	3
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	2:0:0
	* GoalParameters:	Category&Crafting;Tags&Part_T3up;Amount&25

### qe_7days_mar_2024_day3_d_t3
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	300
	* EndOffset:	-7:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t3
	* Tier:	3
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	2:0:0
	* GoalParameters:	Id&CR;Amount&600;ExcludedSources&BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

## ql_7days_mar_2024_day3_t4

### qe_7days_mar_2024_day3_a_t4
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	255
	* EndOffset:	-7:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t4
	* Tier:	4
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	2:0:0
	* GoalParameters:	Tags&Asteroid_Crud_T4up;Amount&1400;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_mar_2024_day3_b_t4
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	270
	* EndOffset:	-7:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t4
	* Tier:	4
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	2:0:0
	* GoalParameters:	Category&Refining;Tags&Asteroid_Refined_T4up;Amount&500

### qe_7days_mar_2024_day3_c_t4
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	285
	* EndOffset:	-7:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t4
	* Tier:	4
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	2:0:0
	* GoalParameters:	Category&Crafting;Tags&Part_T4up;Amount&25

### qe_7days_mar_2024_day3_d_t4
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	300
	* EndOffset:	-7:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t4
	* Tier:	4
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	2:0:0
	* GoalParameters:	Id&CR;Amount&1200;ExcludedSources&BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

## ql_7days_mar_2024_day4_t1

### qe_7days_mar_2024_day4_a_t1
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	255
	* EndOffset:	-6:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t1
	* Tier:	1
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	3:0:0
	* GoalParameters:	Amount&3;Tags&T1up;Mode&Generated

### qe_7days_mar_2024_day4_b_t1
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	270
	* EndOffset:	-6:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t1
	* Tier:	1
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	3:0:0
	* GoalParameters:	Tags&ProgenitorRelic_T1up;Amount&1;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_mar_2024_day4_c_t1
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	285
	* EndOffset:	-6:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t1
	* Tier:	1
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	3:0:0
	* GoalParameters:	Ids&ShipsDestroyedProgenitorT1_ShipsDestroyedProgenitorT2_ShipsDestroyedProgenitorT3_ShipsDestroyedProgenitorT4;Amount&7

### qe_7days_mar_2024_day4_d_t1
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	300
	* EndOffset:	-6:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t1
	* Tier:	1
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	3:0:0
	* GoalParameters:	Amount&1;Tags&Rare_T1up;Mode&Generated

## ql_7days_mar_2024_day4_t2

### qe_7days_mar_2024_day4_a_t2
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	255
	* EndOffset:	-6:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t2
	* Tier:	2
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	3:0:0
	* GoalParameters:	Id&RP;Amount&200;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_mar_2024_day4_b_t2
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	270
	* EndOffset:	-6:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t2
	* Tier:	2
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	3:0:0
	* GoalParameters:	Tags&ProgenitorRelic_T2up;Amount&1;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_mar_2024_day4_c_t2
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	285
	* EndOffset:	-6:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t2
	* Tier:	2
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	3:0:0
	* GoalParameters:	Ids&ShipsDestroyedProgenitorT2_ShipsDestroyedProgenitorT3_ShipsDestroyedProgenitorT4;Amount&7

### qe_7days_mar_2024_day4_d_t2
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	300
	* EndOffset:	-6:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t2
	* Tier:	2
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	3:0:0
	* GoalParameters:	Amount&1;Tags&Epic_T2up;Mode&Generated

## ql_7days_mar_2024_day4_t3

### qe_7days_mar_2024_day4_a_t3
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	255
	* EndOffset:	-6:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t3
	* Tier:	3
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	3:0:0
	* GoalParameters:	Id&RP;Amount&200;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_mar_2024_day4_b_t3
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	270
	* EndOffset:	-6:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t3
	* Tier:	3
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	3:0:0
	* GoalParameters:	Tags&ProgenitorRelic_T3up;Amount&1;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_mar_2024_day4_c_t3
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	285
	* EndOffset:	-6:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t3
	* Tier:	3
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	3:0:0
	* GoalParameters:	Ids&ShipsDestroyedProgenitorT3_ShipsDestroyedProgenitorT4;Amount&7

### qe_7days_mar_2024_day4_d_t3
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	300
	* EndOffset:	-6:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t3
	* Tier:	3
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	3:0:0
	* GoalParameters:	Amount&1;Tags&Epic_T3up;Mode&Generated

## ql_7days_mar_2024_day4_t4

### qe_7days_mar_2024_day4_a_t4
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	255
	* EndOffset:	-6:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t4
	* Tier:	4
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	3:0:0
	* GoalParameters:	Id&RP;Amount&200;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_mar_2024_day4_b_t4
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	270
	* EndOffset:	-6:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t4
	* Tier:	4
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	3:0:0
	* GoalParameters:	Tags&ProgenitorRelic_T4up;Amount&1;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_mar_2024_day4_c_t4
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	285
	* EndOffset:	-6:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t4
	* Tier:	4
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	3:0:0
	* GoalParameters:	Ids&ShipsDestroyedProgenitorT4;Amount&7

### qe_7days_mar_2024_day4_d_t4
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	300
	* EndOffset:	-6:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t4
	* Tier:	4
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	3:0:0
	* GoalParameters:	Amount&1;Tags&Epic_T4up;Mode&Generated

## ql_7days_mar_2024_day5_t1

### qe_7days_mar_2024_day5_a_t1
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	255
	* EndOffset:	-5:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t1
	* Tier:	1
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	4:0:0
	* GoalParameters:	Amount&3;Tags&T1up;Mode&Generated

### qe_7days_mar_2024_day5_b_t1
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	270
	* EndOffset:	-5:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t1
	* Tier:	1
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	4:0:0
	* GoalParameters:	Tags&Insignia_T1up;Amount&50;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_mar_2024_day5_c_t1
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	285
	* EndOffset:	-5:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t1
	* Tier:	1
	* Goals:	UpgradeOfficer,0
	* Type:	Event
	* StartOffset:	4:0:0
	* GoalParameters:	Amount&1

### qe_7days_mar_2024_day5_d_t1
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	300
	* EndOffset:	-5:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t1
	* Tier:	1
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	4:0:0
	* GoalParameters:	Tags&Insignia;Amount&2;ExcludedSources&OpenContainer_QuestReward_MissionReward_ClaimMail_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_BuyItem_SellItem

## ql_7days_mar_2024_day5_t2

### qe_7days_mar_2024_day5_a_t2
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	255
	* EndOffset:	-5:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t2
	* Tier:	2
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	4:0:0
	* GoalParameters:	Amount&3;Tags&T2up;Mode&Generated

### qe_7days_mar_2024_day5_b_t2
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	270
	* EndOffset:	-5:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t2
	* Tier:	2
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	4:0:0
	* GoalParameters:	Tags&Insignia_T2up;Amount&50;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_mar_2024_day5_c_t2
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	285
	* EndOffset:	-5:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t2
	* Tier:	2
	* Goals:	UpgradeOfficer,0
	* Type:	Event
	* StartOffset:	4:0:0
	* GoalParameters:	Amount&2

### qe_7days_mar_2024_day5_d_t2
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	300
	* EndOffset:	-5:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t2
	* Tier:	2
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	4:0:0
	* GoalParameters:	Tags&Insignia;Amount&4;ExcludedSources&OpenContainer_QuestReward_MissionReward_ClaimMail_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_BuyItem_SellItem

## ql_7days_mar_2024_day5_t3

### qe_7days_mar_2024_day5_a_t3
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	255
	* EndOffset:	-5:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t3
	* Tier:	3
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	4:0:0
	* GoalParameters:	Amount&3;Tags&T3up;Mode&Generated

### qe_7days_mar_2024_day5_b_t3
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	270
	* EndOffset:	-5:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t3
	* Tier:	3
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	4:0:0
	* GoalParameters:	Tags&Insignia_T3up;Amount&50;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_mar_2024_day5_c_t3
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	285
	* EndOffset:	-5:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t3
	* Tier:	3
	* Goals:	UpgradeOfficer,0
	* Type:	Event
	* StartOffset:	4:0:0
	* GoalParameters:	Amount&3

### qe_7days_mar_2024_day5_d_t3
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	300
	* EndOffset:	-5:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t3
	* Tier:	3
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	4:0:0
	* GoalParameters:	Tags&Insignia;Amount&6;ExcludedSources&OpenContainer_QuestReward_MissionReward_ClaimMail_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_BuyItem_SellItem

## ql_7days_mar_2024_day5_t4

### qe_7days_mar_2024_day5_a_t4
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	255
	* EndOffset:	-5:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t4
	* Tier:	4
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	4:0:0
	* GoalParameters:	Amount&3;Tags&T4up;Mode&Generated

### qe_7days_mar_2024_day5_b_t4
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	270
	* EndOffset:	-5:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t4
	* Tier:	4
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	4:0:0
	* GoalParameters:	Tags&Insignia_T4up;Amount&50;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_mar_2024_day5_c_t4
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	285
	* EndOffset:	-5:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t4
	* Tier:	4
	* Goals:	UpgradeOfficer,0
	* Type:	Event
	* StartOffset:	4:0:0
	* GoalParameters:	Amount&5

### qe_7days_mar_2024_day5_d_t4
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	300
	* EndOffset:	-5:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t4
	* Tier:	4
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	4:0:0
	* GoalParameters:	Tags&Insignia;Amount&10;ExcludedSources&OpenContainer_QuestReward_MissionReward_ClaimMail_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_BuyItem_SellItem

## ql_7days_mar_2024_day6_t1

### qe_7days_mar_2024_day6_a_t1
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	255
	* EndOffset:	-4:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t1
	* Tier:	1
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	5:0:0
	* GoalParameters:	Tags&RareEarth_T1up;Amount&15;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_mar_2024_day6_b_t1
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	270
	* EndOffset:	-4:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t1
	* Tier:	1
	* Goals:	UpgradeOfficer,0
	* Type:	Event
	* StartOffset:	5:0:0
	* GoalParameters:	Amount&1

### qe_7days_mar_2024_day6_c_t1
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	285
	* EndOffset:	-4:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t1
	* Tier:	1
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	5:0:0
	* GoalParameters:	Category&Crafting;Tags&T1up;Amount&1

### qe_7days_mar_2024_day6_d_t1
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	300
	* EndOffset:	-4:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t1
	* Tier:	1
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	5:0:0
	* GoalParameters:	Ids&ShipsDestroyedT1_ShipsDestroyedT2_ShipsDestroyedT3_ShipsDestroyedT4;Amount&15

## ql_7days_mar_2024_day6_t2

### qe_7days_mar_2024_day6_a_t2
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	255
	* EndOffset:	-4:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t2
	* Tier:	2
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	5:0:0
	* GoalParameters:	Tags&RareEarth_T2up;Amount&15;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_mar_2024_day6_b_t2
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	270
	* EndOffset:	-4:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t2
	* Tier:	2
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	5:0:0
	* GoalParameters:	Category&Upgrade;Tags&External_Module_T1up;Amount&1

### qe_7days_mar_2024_day6_c_t2
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	285
	* EndOffset:	-4:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t2
	* Tier:	2
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	5:0:0
	* GoalParameters:	Category&Crafting;Tags&Part_T2up;Amount&25

### qe_7days_mar_2024_day6_d_t2
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	300
	* EndOffset:	-4:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t2
	* Tier:	2
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	5:0:0
	* GoalParameters:	Ids&ShipsDestroyedT2_ShipsDestroyedT3_ShipsDestroyedT4;Amount&15

## ql_7days_mar_2024_day6_t3

### qe_7days_mar_2024_day6_a_t3
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	255
	* EndOffset:	-4:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t3
	* Tier:	3
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	5:0:0
	* GoalParameters:	Tags&RareEarth_T3up;Amount&15;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_mar_2024_day6_b_t3
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	270
	* EndOffset:	-4:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t3
	* Tier:	3
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	5:0:0
	* GoalParameters:	Category&Upgrade;Tags&External_Module_T2up;Amount&1

### qe_7days_mar_2024_day6_c_t3
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	285
	* EndOffset:	-4:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t3
	* Tier:	3
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	5:0:0
	* GoalParameters:	Category&Upgrade;Tags&Internal_Module_T2up;Amount&1

### qe_7days_mar_2024_day6_d_t3
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	300
	* EndOffset:	-4:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t3
	* Tier:	3
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	5:0:0
	* GoalParameters:	Ids&ShipsDestroyedT3_ShipsDestroyedT4;Amount&15

## ql_7days_mar_2024_day6_t4

### qe_7days_mar_2024_day6_a_t4
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	255
	* EndOffset:	-4:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t4
	* Tier:	4
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	5:0:0
	* GoalParameters:	Tags&RareEarth_T4up;Amount&15;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_mar_2024_day6_b_t4
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	270
	* EndOffset:	-4:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t4
	* Tier:	4
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	5:0:0
	* GoalParameters:	Category&Upgrade;Tags&External_Module_T3up;Amount&1

### qe_7days_mar_2024_day6_c_t4
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	285
	* EndOffset:	-4:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t4
	* Tier:	4
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	5:0:0
	* GoalParameters:	Category&Upgrade;Tags&Internal_Module_T3up;Amount&1

### qe_7days_mar_2024_day6_d_t4
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	300
	* EndOffset:	-4:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t4
	* Tier:	4
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	5:0:0
	* GoalParameters:	Id&ShipsDestroyedT4;Amount&15

## ql_7days_mar_2024_day7_t1

### qe_7days_mar_2024_day7_a_t1
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	255
	* EndOffset:	-3:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t1
	* Tier:	1
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	6:0:0
	* GoalParameters:	Amount&3;Tags&T1up;Mode&Generated

### qe_7days_mar_2024_day7_b_t1
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	270
	* EndOffset:	-3:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t1
	* Tier:	1
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	6:0:0
	* GoalParameters:	Ids&ShipsDestroyedT1_ShipsDestroyedT2_ShipsDestroyedT3_ShipsDestroyedT4;Amount&15

### qe_7days_mar_2024_day7_c_t1
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	285
	* EndOffset:	-3:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t1
	* Tier:	1
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	6:0:0
	* GoalParameters:	Tags&Salvage_T1up;Amount&3;ExcludedSources&MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_mar_2024_day7_d_t1
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	300
	* EndOffset:	-3:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t1
	* Tier:	1
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	6:0:0
	* GoalParameters:	Amount&3;Tags&T1up;Mode&Generated

## ql_7days_mar_2024_day7_t2

### qe_7days_mar_2024_day7_a_t2
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	255
	* EndOffset:	-3:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t2
	* Tier:	2
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	6:0:0
	* GoalParameters:	Amount&3;Tags&T2up;Mode&Generated

### qe_7days_mar_2024_day7_b_t2
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	270
	* EndOffset:	-3:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t2
	* Tier:	2
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	6:0:0
	* GoalParameters:	Ids&ShipsDestroyedT2_ShipsDestroyedT3_ShipsDestroyedT4;Amount&15

### qe_7days_mar_2024_day7_c_t2
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	285
	* EndOffset:	-3:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t2
	* Tier:	2
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	6:0:0
	* GoalParameters:	Tags&Salvage_T2up;Amount&3;ExcludedSources&MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_mar_2024_day7_d_t2
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	300
	* EndOffset:	-3:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t2
	* Tier:	2
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	6:0:0
	* GoalParameters:	Amount&1;Mode&Strike;Tags&T1up

## ql_7days_mar_2024_day7_t3

### qe_7days_mar_2024_day7_a_t3
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	255
	* EndOffset:	-3:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t3
	* Tier:	3
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	6:0:0
	* GoalParameters:	Amount&3;Tags&T3up;Mode&Generated

### qe_7days_mar_2024_day7_b_t3
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	270
	* EndOffset:	-3:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t3
	* Tier:	3
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	6:0:0
	* GoalParameters:	Ids&ShipsDestroyedT3_ShipsDestroyedT4;Amount&15

### qe_7days_mar_2024_day7_c_t3
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	285
	* EndOffset:	-3:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t3
	* Tier:	3
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	6:0:0
	* GoalParameters:	Tags&Salvage_T3up;Amount&3;ExcludedSources&MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_mar_2024_day7_d_t3
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	300
	* EndOffset:	-3:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t3
	* Tier:	3
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	6:0:0
	* GoalParameters:	Amount&1;Mode&Strike;Tags&T2up

## ql_7days_mar_2024_day7_t4

### qe_7days_mar_2024_day7_a_t4
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	255
	* EndOffset:	-3:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t4
	* Tier:	4
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	6:0:0
	* GoalParameters:	Amount&3;Tags&T4up;Mode&Generated

### qe_7days_mar_2024_day7_b_t4
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	270
	* EndOffset:	-3:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t4
	* Tier:	4
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	6:0:0
	* GoalParameters:	Id&ShipsDestroyedT4;Amount&15

### qe_7days_mar_2024_day7_c_t4
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	285
	* EndOffset:	-3:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t4
	* Tier:	4
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	6:0:0
	* GoalParameters:	Tags&Salvage_T4up;Amount&3;ExcludedSources&MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_mar_2024_day7_d_t4
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	300
	* EndOffset:	-3:0:0
	* EventId:	event_monthlyEvent_2024_03_01_t4
	* Tier:	4
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	6:0:0
	* GoalParameters:	Amount&1;Mode&Strike;Tags&T3up

## ql_7days_2023_08_day1_t1

### qe_7days_2023_08_day1_a_t1
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	255
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t1
	* Tier:	1
	* Goals:	Scan,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Tags&InSystem_T1up;Amount&10;Analyzed&True

### qe_7days_2023_08_day1_b_t1
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	270
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t1
	* Tier:	1
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Ids&ShipsDestroyedT1_ShipsDestroyedT2_ShipsDestroyedT3_ShipsDestroyedT4;Amount&15

### qe_7days_2023_08_day1_c_t1
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	285
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t1
	* Tier:	1
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Tags&Asteroid_Crud_T1up;Amount&800;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_2023_08_day1_d_t1
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	300
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t1
	* Tier:	1
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Tags&RareEarth_T1up;Amount&15;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

## ql_7days_2023_08_day1_t2

### qe_7days_2023_08_day1_a_t2
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	255
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t2
	* Tier:	2
	* Goals:	Scan,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Tags&InSystem_T2up;Amount&10;Analyzed&True

### qe_7days_2023_08_day1_b_t2
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	270
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t2
	* Tier:	2
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Ids&ShipsDestroyedT2_ShipsDestroyedT3_ShipsDestroyedT4;Amount&15

### qe_7days_2023_08_day1_c_t2
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	285
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t2
	* Tier:	2
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Tags&Asteroid_Crud_T2up;Amount&1000;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_2023_08_day1_d_t2
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	300
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t2
	* Tier:	2
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Tags&RareEarth_T2up;Amount&15;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

## ql_7days_2023_08_day1_t3

### qe_7days_2023_08_day1_a_t3
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	255
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t3
	* Tier:	3
	* Goals:	Scan,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Tags&InSystem_T3up;Amount&10;Analyzed&True

### qe_7days_2023_08_day1_b_t3
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	270
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t3
	* Tier:	3
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Ids&ShipsDestroyedT3_ShipsDestroyedT4;Amount&15

### qe_7days_2023_08_day1_c_t3
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	285
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t3
	* Tier:	3
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Tags&Gas_T3up;Amount&800;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_2023_08_day1_d_t3
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	300
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t3
	* Tier:	3
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Tags&RareEarth_T3up;Amount&15;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

## ql_7days_2023_08_day1_t4

### qe_7days_2023_08_day1_a_t4
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	255
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t4
	* Tier:	4
	* Goals:	Scan,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Tags&InSystem_T4up;Amount&10;Analyzed&True

### qe_7days_2023_08_day1_b_t4
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	270
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t4
	* Tier:	4
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Id&ShipsDestroyedT4;Amount&15

### qe_7days_2023_08_day1_c_t4
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	285
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t4
	* Tier:	4
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Tags&Gas_T4up;Amount&1000;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_2023_08_day1_d_t4
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	300
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t4
	* Tier:	4
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Tags&RareEarth_T4up;Amount&15;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

## ql_7days_2023_08_day2_t1

### qe_7days_2023_08_day2_a_t1
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	255
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t1
	* Tier:	1
	* Goals:	CompleteQuest,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Amount&5;Tags&T1up

### qe_7days_2023_08_day2_b_t1
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	270
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t1
	* Tier:	1
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Amount&3;Tags&T1up

### qe_7days_2023_08_day2_c_t1
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	285
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t1
	* Tier:	1
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Tags&Insignia_T1up;Amount&50;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_2023_08_day2_d_t1
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	300
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t1
	* Tier:	1
	* Goals:	UpgradeOfficer,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Amount&1

## ql_7days_2023_08_day2_t2

### qe_7days_2023_08_day2_a_t2
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	255
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t2
	* Tier:	2
	* Goals:	CompleteQuest,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Amount&5;Tags&Faction_T2up

### qe_7days_2023_08_day2_b_t2
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	270
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t2
	* Tier:	2
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Amount&3;Mode&Faction;Tags&T2up

### qe_7days_2023_08_day2_c_t2
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	285
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t2
	* Tier:	2
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Ids&RepTr1_RepTanoch_RepYaot_RepAmassari;Amount&135

### qe_7days_2023_08_day2_d_t2
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	300
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t2
	* Tier:	2
	* Goals:	UpgradeOfficer,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Amount&2

## ql_7days_2023_08_day2_t3

### qe_7days_2023_08_day2_a_t3
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	255
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t3
	* Tier:	3
	* Goals:	CompleteQuest,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Amount&5;Tags&Faction_T3up

### qe_7days_2023_08_day2_b_t3
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	270
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t3
	* Tier:	3
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Amount&3;Mode&Faction;Tags&T3up

### qe_7days_2023_08_day2_c_t3
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	285
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t3
	* Tier:	3
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Ids&RepTr1_RepTanoch_RepYaot_RepAmassari;Amount&180

### qe_7days_2023_08_day2_d_t3
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	300
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t3
	* Tier:	3
	* Goals:	UpgradeOfficer,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Amount&3

## ql_7days_2023_08_day2_t4

### qe_7days_2023_08_day2_a_t4
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	255
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t4
	* Tier:	4
	* Goals:	CompleteQuest,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Amount&5;Tags&Faction_T4up

### qe_7days_2023_08_day2_b_t4
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	270
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t4
	* Tier:	4
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Amount&3;Mode&Faction;Tags&T4up

### qe_7days_2023_08_day2_c_t4
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	285
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t4
	* Tier:	4
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Ids&RepTr1_RepTanoch_RepYaot_RepAmassari;Amount&225

### qe_7days_2023_08_day2_d_t4
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	300
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t4
	* Tier:	4
	* Goals:	UpgradeOfficer,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Amount&5

## ql_7days_2023_08_day3_t1

### qe_7days_2023_08_day3_a_t1
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	255
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t1
	* Tier:	1
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Tags&Asteroid_Crud_T1up;Amount&800;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_2023_08_day3_b_t1
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	270
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t1
	* Tier:	1
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Category&Refining;Tags&Asteroid_Refined_T1up;Amount&500

### qe_7days_2023_08_day3_c_t1
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	285
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t1
	* Tier:	1
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Category&Crafting;Tags&T1up;Amount&1

### qe_7days_2023_08_day3_d_t1
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	300
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t1
	* Tier:	1
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Id&CR;Amount&150;ExcludedSources&BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

## ql_7days_2023_08_day3_t2

### qe_7days_2023_08_day3_a_t2
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	255
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t2
	* Tier:	2
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Tags&Asteroid_Crud_T2up;Amount&1000;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_2023_08_day3_b_t2
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	270
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t2
	* Tier:	2
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Category&Refining;Tags&Asteroid_Refined_T2up;Amount&500

### qe_7days_2023_08_day3_c_t2
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	285
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t2
	* Tier:	2
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Category&Crafting;Tags&Part_T2up;Amount&25

### qe_7days_2023_08_day3_d_t2
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	300
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t2
	* Tier:	2
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Id&CR;Amount&300;ExcludedSources&BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

## ql_7days_2023_08_day3_t3

### qe_7days_2023_08_day3_a_t3
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	255
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t3
	* Tier:	3
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Tags&Asteroid_Crud_T3up;Amount&1200;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_2023_08_day3_b_t3
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	270
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t3
	* Tier:	3
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Category&Refining;Tags&Asteroid_Refined_T3up;Amount&500

### qe_7days_2023_08_day3_c_t3
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	285
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t3
	* Tier:	3
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Category&Crafting;Tags&Part_T3up;Amount&25

### qe_7days_2023_08_day3_d_t3
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	300
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t3
	* Tier:	3
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Id&CR;Amount&600;ExcludedSources&BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

## ql_7days_2023_08_day3_t4

### qe_7days_2023_08_day3_a_t4
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	255
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t4
	* Tier:	4
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Tags&Asteroid_Crud_T4up;Amount&1400;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_2023_08_day3_b_t4
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	270
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t4
	* Tier:	4
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Category&Refining;Tags&Asteroid_Refined_T4up;Amount&500

### qe_7days_2023_08_day3_c_t4
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	285
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t4
	* Tier:	4
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Category&Crafting;Tags&Part_T4up;Amount&25

### qe_7days_2023_08_day3_d_t4
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	300
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t4
	* Tier:	4
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Id&CR;Amount&1200;ExcludedSources&BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

## ql_7days_2023_08_day4_t1

### qe_7days_2023_08_day4_a_t1
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	255
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t1
	* Tier:	1
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Amount&3;Tags&T1up;Mode&Generated

### qe_7days_2023_08_day4_b_t1
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	270
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t1
	* Tier:	1
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Tags&ProgenitorRelic_T1up;Amount&1;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_2023_08_day4_c_t1
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	285
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t1
	* Tier:	1
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Ids&ShipsDestroyedProgenitorT1_ShipsDestroyedProgenitorT2_ShipsDestroyedProgenitorT3_ShipsDestroyedProgenitorT4;Amount&7

### qe_7days_2023_08_day4_d_t1
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	300
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t1
	* Tier:	1
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Amount&1;Tags&Rare_T1up;Mode&Generated

## ql_7days_2023_08_day4_t2

### qe_7days_2023_08_day4_a_t2
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	255
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t2
	* Tier:	2
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Id&RP;Amount&200;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_2023_08_day4_b_t2
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	270
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t2
	* Tier:	2
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Tags&ProgenitorRelic_T2up;Amount&1;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_2023_08_day4_c_t2
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	285
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t2
	* Tier:	2
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Ids&ShipsDestroyedProgenitorT2_ShipsDestroyedProgenitorT3_ShipsDestroyedProgenitorT4;Amount&7

### qe_7days_2023_08_day4_d_t2
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	300
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t2
	* Tier:	2
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Amount&1;Tags&Epic_T2up;Mode&Generated

## ql_7days_2023_08_day4_t3

### qe_7days_2023_08_day4_a_t3
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	255
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t3
	* Tier:	3
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Id&RP;Amount&200;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_2023_08_day4_b_t3
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	270
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t3
	* Tier:	3
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Tags&ProgenitorRelic_T3up;Amount&1;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_2023_08_day4_c_t3
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	285
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t3
	* Tier:	3
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Ids&ShipsDestroyedProgenitorT3_ShipsDestroyedProgenitorT4;Amount&7

### qe_7days_2023_08_day4_d_t3
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	300
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t3
	* Tier:	3
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Amount&1;Tags&Epic_T3up;Mode&Generated

## ql_7days_2023_08_day4_t4

### qe_7days_2023_08_day4_a_t4
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	255
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t4
	* Tier:	4
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Id&RP;Amount&200;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_2023_08_day4_b_t4
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	270
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t4
	* Tier:	4
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Tags&ProgenitorRelic_T4up;Amount&1;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_2023_08_day4_c_t4
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	285
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t4
	* Tier:	4
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Ids&ShipsDestroyedProgenitorT4;Amount&7

### qe_7days_2023_08_day4_d_t4
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	300
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t4
	* Tier:	4
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Amount&1;Tags&Epic_T4up;Mode&Generated

## ql_7days_2023_08_day5_t1

### qe_7days_2023_08_day5_a_t1
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	255
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t1
	* Tier:	1
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Amount&3;Tags&T1up;Mode&Generated

### qe_7days_2023_08_day5_b_t1
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	270
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t1
	* Tier:	1
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Tags&Insignia_T1up;Amount&50;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_2023_08_day5_c_t1
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	285
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t1
	* Tier:	1
	* Goals:	UpgradeOfficer,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Amount&1

### qe_7days_2023_08_day5_d_t1
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	300
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t1
	* Tier:	1
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Tags&Insignia;Amount&2;ExcludedSources&OpenContainer_QuestReward_MissionReward_ClaimMail_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_BuyItem_SellItem

## ql_7days_2023_08_day5_t2

### qe_7days_2023_08_day5_a_t2
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	255
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t2
	* Tier:	2
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Amount&3;Tags&T2up;Mode&Generated

### qe_7days_2023_08_day5_b_t2
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	270
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t2
	* Tier:	2
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Tags&Insignia_T2up;Amount&50;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_2023_08_day5_c_t2
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	285
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t2
	* Tier:	2
	* Goals:	UpgradeOfficer,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Amount&2

### qe_7days_2023_08_day5_d_t2
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	300
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t2
	* Tier:	2
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Tags&Insignia;Amount&4;ExcludedSources&OpenContainer_QuestReward_MissionReward_ClaimMail_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_BuyItem_SellItem

## ql_7days_2023_08_day5_t3

### qe_7days_2023_08_day5_a_t3
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	255
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t3
	* Tier:	3
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Amount&3;Tags&T3up;Mode&Generated

### qe_7days_2023_08_day5_b_t3
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	270
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t3
	* Tier:	3
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Tags&Insignia_T3up;Amount&50;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_2023_08_day5_c_t3
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	285
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t3
	* Tier:	3
	* Goals:	UpgradeOfficer,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Amount&3

### qe_7days_2023_08_day5_d_t3
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	300
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t3
	* Tier:	3
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Tags&Insignia;Amount&6;ExcludedSources&OpenContainer_QuestReward_MissionReward_ClaimMail_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_BuyItem_SellItem

## ql_7days_2023_08_day5_t4

### qe_7days_2023_08_day5_a_t4
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	255
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t4
	* Tier:	4
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Amount&3;Tags&T4up;Mode&Generated

### qe_7days_2023_08_day5_b_t4
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	270
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t4
	* Tier:	4
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Tags&Insignia_T4up;Amount&50;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_2023_08_day5_c_t4
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	285
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t4
	* Tier:	4
	* Goals:	UpgradeOfficer,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Amount&5

### qe_7days_2023_08_day5_d_t4
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	300
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t4
	* Tier:	4
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Tags&Insignia;Amount&10;ExcludedSources&OpenContainer_QuestReward_MissionReward_ClaimMail_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_BuyItem_SellItem

## ql_7days_2023_08_day6_t1

### qe_7days_2023_08_day6_a_t1
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	255
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t1
	* Tier:	1
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Tags&RareEarth_T1up;Amount&15;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_2023_08_day6_b_t1
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	270
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t1
	* Tier:	1
	* Goals:	UpgradeOfficer,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Amount&1

### qe_7days_2023_08_day6_c_t1
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	285
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t1
	* Tier:	1
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Category&Crafting;Tags&T1up;Amount&1

### qe_7days_2023_08_day6_d_t1
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	300
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t1
	* Tier:	1
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Ids&ShipsDestroyedT1_ShipsDestroyedT2_ShipsDestroyedT3_ShipsDestroyedT4;Amount&15

## ql_7days_2023_08_day6_t2

### qe_7days_2023_08_day6_a_t2
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	255
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t2
	* Tier:	2
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Tags&RareEarth_T2up;Amount&15;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_2023_08_day6_b_t2
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	270
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t2
	* Tier:	2
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Category&Upgrade;Tags&External_Module_T1up;Amount&1

### qe_7days_2023_08_day6_c_t2
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	285
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t2
	* Tier:	2
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Category&Crafting;Tags&Part_T2up;Amount&25

### qe_7days_2023_08_day6_d_t2
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	300
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t2
	* Tier:	2
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Ids&ShipsDestroyedT2_ShipsDestroyedT3_ShipsDestroyedT4;Amount&15

## ql_7days_2023_08_day6_t3

### qe_7days_2023_08_day6_a_t3
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	255
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t3
	* Tier:	3
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Tags&RareEarth_T3up;Amount&15;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_2023_08_day6_b_t3
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	270
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t3
	* Tier:	3
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Category&Upgrade;Tags&External_Module_T2up;Amount&1

### qe_7days_2023_08_day6_c_t3
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	285
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t3
	* Tier:	3
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Category&Upgrade;Tags&Internal_Module_T2up;Amount&1

### qe_7days_2023_08_day6_d_t3
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	300
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t3
	* Tier:	3
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Ids&ShipsDestroyedT3_ShipsDestroyedT4;Amount&15

## ql_7days_2023_08_day6_t4

### qe_7days_2023_08_day6_a_t4
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	255
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t4
	* Tier:	4
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Tags&RareEarth_T4up;Amount&15;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_2023_08_day6_b_t4
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	270
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t4
	* Tier:	4
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Category&Upgrade;Tags&External_Module_T3up;Amount&1

### qe_7days_2023_08_day6_c_t4
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	285
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t4
	* Tier:	4
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Category&Upgrade;Tags&Internal_Module_T3up;Amount&1

### qe_7days_2023_08_day6_d_t4
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	300
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t4
	* Tier:	4
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Id&ShipsDestroyedT4;Amount&15

## ql_7days_2023_08_day7_t1

### qe_7days_2023_08_day7_a_t1
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	255
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t1
	* Tier:	1
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Amount&3;Tags&T1up;Mode&Generated

### qe_7days_2023_08_day7_b_t1
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	270
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t1
	* Tier:	1
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Ids&ShipsDestroyedT1_ShipsDestroyedT2_ShipsDestroyedT3_ShipsDestroyedT4;Amount&15

### qe_7days_2023_08_day7_c_t1
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	285
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t1
	* Tier:	1
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Tags&Salvage_T1up;Amount&3;ExcludedSources&MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_2023_08_day7_d_t1
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	300
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t1
	* Tier:	1
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Amount&3;Tags&T1up;Mode&Generated

## ql_7days_2023_08_day7_t2

### qe_7days_2023_08_day7_a_t2
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	255
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t2
	* Tier:	2
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Amount&3;Tags&T2up;Mode&Generated

### qe_7days_2023_08_day7_b_t2
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	270
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t2
	* Tier:	2
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Ids&ShipsDestroyedT2_ShipsDestroyedT3_ShipsDestroyedT4;Amount&15

### qe_7days_2023_08_day7_c_t2
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	285
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t2
	* Tier:	2
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Tags&Salvage_T2up;Amount&3;ExcludedSources&MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_2023_08_day7_d_t2
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	300
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t2
	* Tier:	2
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Amount&1;Mode&Strike;Tags&T1up

## ql_7days_2023_08_day7_t3

### qe_7days_2023_08_day7_a_t3
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	255
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t3
	* Tier:	3
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Amount&3;Tags&T3up;Mode&Generated

### qe_7days_2023_08_day7_b_t3
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	270
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t3
	* Tier:	3
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Ids&ShipsDestroyedT3_ShipsDestroyedT4;Amount&15

### qe_7days_2023_08_day7_c_t3
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	285
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t3
	* Tier:	3
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Tags&Salvage_T3up;Amount&3;ExcludedSources&MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_2023_08_day7_d_t3
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	300
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t3
	* Tier:	3
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Amount&1;Mode&Strike;Tags&T2up

## ql_7days_2023_08_day7_t4

### qe_7days_2023_08_day7_a_t4
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	255
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t4
	* Tier:	4
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Amount&3;Tags&T4up;Mode&Generated

### qe_7days_2023_08_day7_b_t4
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	270
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t4
	* Tier:	4
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Id&ShipsDestroyedT4;Amount&15

### qe_7days_2023_08_day7_c_t4
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	285
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t4
	* Tier:	4
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Tags&Salvage_T4up;Amount&3;ExcludedSources&MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_2023_08_day7_d_t4
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	300
	* EndOffset:	0:0:0
	* EventId:	event_7days_2023_08_21_t4
	* Tier:	4
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Amount&1;Mode&Strike;Tags&T3up

## ql_event_iyaFal_2023_t1

### qe_iyaFal_2023_day01_t1
	* Rewards:	Z3:20
	* ScheduleType:	Locked
	* XPMod:	15
	* EndOffset:	-5:0:0
	* EventId:	event_season_iyaFal_2023_t1
	* Tier:	1
	* Goals:	CompleteQuest,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Amount&5;Tags&T1up

### qe_iyaFal_2023_day02_t1
	* Rewards:	Z3:20
	* ScheduleType:	Locked
	* XPMod:	16
	* EndOffset:	-5:0:0
	* EventId:	event_season_iyaFal_2023_t1
	* Tier:	1
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	1:0:0
	* GoalParameters:	Tags&Salvage_T1up;Amount&5;ExcludedSources&MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_iyaFal_2023_day03_t1
	* Rewards:	Z3:20
	* ScheduleType:	Locked
	* XPMod:	17
	* EndOffset:	-5:0:0
	* EventId:	event_season_iyaFal_2023_t1
	* Tier:	1
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	2:0:0
	* GoalParameters:	Category&Crafting;Tags&T1up;Amount&5

### qe_iyaFal_2023_day04_t1
	* Rewards:	Z3:20
	* ScheduleType:	Locked
	* XPMod:	18
	* EndOffset:	-5:0:0
	* EventId:	event_season_iyaFal_2023_t1
	* MailsOnCompletion:	m_iyaFal_day4_log
	* Tier:	1
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	3:0:0
	* GoalParameters:	Amount&3;Tags&T1up;Mode&Generated

### qe_iyaFal_2023_day05_t1
	* Rewards:	Z3:20
	* ScheduleType:	Locked
	* XPMod:	19
	* EndOffset:	-5:0:0
	* EventId:	event_season_iyaFal_2023_t1
	* Tier:	1
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	4:0:0
	* GoalParameters:	Amount&3;Tags&T1up

### qe_iyaFal_2023_day06_t1
	* Rewards:	Z3:20
	* ScheduleType:	Locked
	* XPMod:	20
	* EndOffset:	-5:0:0
	* EventId:	event_season_iyaFal_2023_t1
	* Tier:	1
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	5:0:0
	* GoalParameters:	Tags&Insignia_T1up;Amount&50;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_iyaFal_2023_day07_t1
	* Rewards:	Z3:20
	* ScheduleType:	Locked
	* XPMod:	21
	* EndOffset:	-5:0:0
	* EventId:	event_season_iyaFal_2023_t1
	* Tier:	1
	* Goals:	UpgradeOfficer,0
	* Type:	Event
	* StartOffset:	6:0:0
	* GoalParameters:	Amount&1

### qe_iyaFal_2023_day08_t1
	* Rewards:	Z3:20
	* ScheduleType:	Locked
	* XPMod:	22
	* EndOffset:	-5:0:0
	* EventId:	event_season_iyaFal_2023_t1
	* MailsOnCompletion:	m_iyaFal_day8_log
	* Tier:	1
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	7:0:0
	* GoalParameters:	Tags&ProgenitorRelic_T1up;Amount&1;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_iyaFal_2023_day09_t1
	* Rewards:	Z3:20
	* ScheduleType:	Locked
	* XPMod:	23
	* EndOffset:	-5:0:0
	* EventId:	event_season_iyaFal_2023_t1
	* Tier:	1
	* Goals:	CompleteQuest,0
	* Type:	Event
	* StartOffset:	8:0:0
	* GoalParameters:	Amount&5;Tags&T1up

### qe_iyaFal_2023_day10_t1
	* Rewards:	Z3:20
	* ScheduleType:	Locked
	* XPMod:	24
	* EndOffset:	-5:0:0
	* EventId:	event_season_iyaFal_2023_t1
	* Tier:	1
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	9:0:0
	* GoalParameters:	Tags&Salvage_T1up;Amount&5;ExcludedSources&MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_iyaFal_2023_day11_t1
	* Rewards:	Z3:20
	* ScheduleType:	Locked
	* XPMod:	25
	* EndOffset:	-5:0:0
	* EventId:	event_season_iyaFal_2023_t1
	* Tier:	1
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	10:0:0
	* GoalParameters:	Category&Crafting;Tags&T1up;Amount&5

### qe_iyaFal_2023_day12_t1
	* Rewards:	Z3:20
	* ScheduleType:	Locked
	* XPMod:	26
	* EndOffset:	-5:0:0
	* EventId:	event_season_iyaFal_2023_t1
	* MailsOnCompletion:	m_iyaFal_day12_log
	* Tier:	1
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	11:0:0
	* GoalParameters:	Amount&1;Tags&Rare_T1up;Mode&Generated

### qe_iyaFal_2023_day13_t1
	* Rewards:	Z3:20
	* ScheduleType:	Locked
	* XPMod:	27
	* EndOffset:	-5:0:0
	* EventId:	event_season_iyaFal_2023_t1
	* Tier:	1
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	12:0:0
	* GoalParameters:	Tags&Insignia_T1up;Amount&50;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_iyaFal_2023_day14_t1
	* Rewards:	Z3:20
	* ScheduleType:	Locked
	* XPMod:	28
	* EndOffset:	-5:0:0
	* EventId:	event_season_iyaFal_2023_t1
	* Tier:	1
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	13:0:0
	* GoalParameters:	Tags&ProgenitorRelic_T1up;Amount&1;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_iyaFal_2023_day15_t1
	* Rewards:	Z3:20	HC:100	officer_iyatequaFall_2023:1
	* ScheduleType:	Locked
	* XPMod:	35
	* EndOffset:	-5:0:0
	* EventId:	event_season_iyaFal_2023_t1
	* Tier:	1
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	14:0:0
	* GoalParameters:	Id&event_iyaFal2023_Escort_t1

## ql_event_iyaFal_2023_epilog_t1

### qe_iyaFal_2023_epi01_t1
	* Rewards:	insig_r1:50
	* ScheduleType:	Locked
	* XPMod:	21
	* EndOffset:	0:0:0
	* EventId:	event_season_iyaFal_2023_t1
	* Tier:	1
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	15:0:0
	* GoalParameters:	Tags&Asteroid_Crud_T1up;Amount&1000;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_iyaFal_2023_epi02_t1
	* Rewards:	1N:300	1O:300	1P:300
	* ScheduleType:	Locked
	* XPMod:	23
	* EndOffset:	0:0:0
	* EventId:	event_season_iyaFal_2023_t1
	* Tier:	1
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	16:0:0
	* GoalParameters:	Ids&ShipsDestroyedProgenitorT1_ShipsDestroyedProgenitorT2_ShipsDestroyedProgenitorT3_ShipsDestroyedProgenitorT4;Amount&10

### qe_iyaFal_2023_epi03_t1
	* Rewards:	1N:300	1O:300	1P:300
	* ScheduleType:	Locked
	* XPMod:	25
	* EndOffset:	0:0:0
	* EventId:	event_season_iyaFal_2023_t1
	* Tier:	1
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	17:0:0
	* GoalParameters:	Tags&Insignia_T1up;Amount&50;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_iyaFal_2023_epi04_t1
	* Rewards:	1N:300	1O:300	1P:300
	* ScheduleType:	Locked
	* XPMod:	27
	* EndOffset:	0:0:0
	* EventId:	event_season_iyaFal_2023_t1
	* Tier:	1
	* Goals:	UpgradeOfficer,0
	* Type:	Event
	* StartOffset:	18:0:0
	* GoalParameters:	Amount&1

### qe_iyaFal_2023_epi05_t1
	* Rewards:	rw_recruitToken_hiig_minEpic:1
	* ScheduleType:	Locked
	* XPMod:	35
	* EndOffset:	0:0:0
	* EventId:	event_season_iyaFal_2023_t1
	* Tier:	1
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	19:0:0
	* GoalParameters:	Amount&1;Tags&Rare_T1up;Mode&Generated

## ql_event_iyaFal_2023_t2

### qe_iyaFal_2023_day01_t2
	* Rewards:	Z3:20
	* ScheduleType:	Locked
	* XPMod:	45
	* EndOffset:	-5:0:0
	* EventId:	event_season_iyaFal_2023_t2
	* Tier:	2
	* Goals:	CompleteQuest,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Amount&5;Tags&Faction_Tr1_T2up

### qe_iyaFal_2023_day02_t2
	* Rewards:	Z3:20
	* ScheduleType:	Locked
	* XPMod:	48
	* EndOffset:	-5:0:0
	* EventId:	event_season_iyaFal_2023_t2
	* Tier:	2
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	1:0:0
	* GoalParameters:	Tags&Salvage_T2up;Amount&5;ExcludedSources&MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_iyaFal_2023_day03_t2
	* Rewards:	Z3:20
	* ScheduleType:	Locked
	* XPMod:	51
	* EndOffset:	-5:0:0
	* EventId:	event_season_iyaFal_2023_t2
	* Tier:	2
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	2:0:0
	* GoalParameters:	Category&Crafting;Tags&Part_T2up;Amount&100

### qe_iyaFal_2023_day04_t2
	* Rewards:	Z3:20
	* ScheduleType:	Locked
	* XPMod:	54
	* EndOffset:	-5:0:0
	* EventId:	event_season_iyaFal_2023_t2
	* MailsOnCompletion:	m_iyaFal_day4_log
	* Tier:	2
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	3:0:0
	* GoalParameters:	Amount&3;Tags&T2up;Mode&Generated

### qe_iyaFal_2023_day05_t2
	* Rewards:	Z3:20
	* ScheduleType:	Locked
	* XPMod:	57
	* EndOffset:	-5:0:0
	* EventId:	event_season_iyaFal_2023_t2
	* Tier:	2
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	4:0:0
	* GoalParameters:	Amount&3;Mode&Faction;Tags&T2up

### qe_iyaFal_2023_day06_t2
	* Rewards:	Z3:20
	* ScheduleType:	Locked
	* XPMod:	60
	* EndOffset:	-5:0:0
	* EventId:	event_season_iyaFal_2023_t2
	* Tier:	2
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	5:0:0
	* GoalParameters:	Tags&Insignia_T2up;Amount&50;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_iyaFal_2023_day07_t2
	* Rewards:	Z3:20
	* ScheduleType:	Locked
	* XPMod:	63
	* EndOffset:	-5:0:0
	* EventId:	event_season_iyaFal_2023_t2
	* Tier:	2
	* Goals:	UpgradeOfficer,0
	* Type:	Event
	* StartOffset:	6:0:0
	* GoalParameters:	Amount&2

### qe_iyaFal_2023_day08_t2
	* Rewards:	Z3:20
	* ScheduleType:	Locked
	* XPMod:	66
	* EndOffset:	-5:0:0
	* EventId:	event_season_iyaFal_2023_t2
	* MailsOnCompletion:	m_iyaFal_day8_log
	* Tier:	2
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	7:0:0
	* GoalParameters:	Tags&ProgenitorRelic_T2up;Amount&1;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_iyaFal_2023_day09_t2
	* Rewards:	Z3:20
	* ScheduleType:	Locked
	* XPMod:	69
	* EndOffset:	-5:0:0
	* EventId:	event_season_iyaFal_2023_t2
	* Tier:	2
	* Goals:	CompleteQuest,0
	* Type:	Event
	* StartOffset:	8:0:0
	* GoalParameters:	Amount&5;Tags&Faction_Tr1_T2up

### qe_iyaFal_2023_day10_t2
	* Rewards:	Z3:20
	* ScheduleType:	Locked
	* XPMod:	72
	* EndOffset:	-5:0:0
	* EventId:	event_season_iyaFal_2023_t2
	* Tier:	2
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	9:0:0
	* GoalParameters:	Tags&Salvage_T2up;Amount&5;ExcludedSources&MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_iyaFal_2023_day11_t2
	* Rewards:	Z3:20
	* ScheduleType:	Locked
	* XPMod:	75
	* EndOffset:	-5:0:0
	* EventId:	event_season_iyaFal_2023_t2
	* Tier:	2
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	10:0:0
	* GoalParameters:	Id&RP;Amount&400;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_iyaFal_2023_day12_t2
	* Rewards:	Z3:20
	* ScheduleType:	Locked
	* XPMod:	78
	* EndOffset:	-5:0:0
	* EventId:	event_season_iyaFal_2023_t2
	* MailsOnCompletion:	m_iyaFal_day12_log
	* Tier:	2
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	11:0:0
	* GoalParameters:	Amount&1;Tags&Epic_T2up;Mode&Generated

### qe_iyaFal_2023_day13_t2
	* Rewards:	Z3:20
	* ScheduleType:	Locked
	* XPMod:	81
	* EndOffset:	-5:0:0
	* EventId:	event_season_iyaFal_2023_t2
	* Tier:	2
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	12:0:0
	* GoalParameters:	Ids&RepTr1;Amount&135

### qe_iyaFal_2023_day14_t2
	* Rewards:	Z3:20
	* ScheduleType:	Locked
	* XPMod:	84
	* EndOffset:	-5:0:0
	* EventId:	event_season_iyaFal_2023_t2
	* Tier:	2
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	13:0:0
	* GoalParameters:	Tags&ProgenitorRelic_T2up;Amount&1;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_iyaFal_2023_day15_t2
	* Rewards:	Z3:20	HC:100	officer_iyatequaFall_2023:1
	* ScheduleType:	Locked
	* XPMod:	105
	* EndOffset:	-5:0:0
	* EventId:	event_season_iyaFal_2023_t2
	* Tier:	2
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	14:0:0
	* GoalParameters:	Id&event_iyaFal2023_Escort_t2

## ql_event_iyaFal_2023_epilog_t2

### qe_iyaFal_2023_epi01_t2
	* Rewards:	insig_r2:50
	* ScheduleType:	Locked
	* XPMod:	63
	* EndOffset:	0:0:0
	* EventId:	event_season_iyaFal_2023_t2
	* Tier:	2
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	15:0:0
	* GoalParameters:	Tags&Asteroid_Crud_T2up;Amount&1200;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_iyaFal_2023_epi02_t2
	* Rewards:	2Q:500
	* ScheduleType:	Locked
	* XPMod:	69
	* EndOffset:	0:0:0
	* EventId:	event_season_iyaFal_2023_t2
	* Tier:	2
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	16:0:0
	* GoalParameters:	Ids&ShipsDestroyedProgenitorT2_ShipsDestroyedProgenitorT3_ShipsDestroyedProgenitorT4;Amount&10

### qe_iyaFal_2023_epi03_t2
	* Rewards:	2N:300	2O:300	2P:300
	* ScheduleType:	Locked
	* XPMod:	75
	* EndOffset:	0:0:0
	* EventId:	event_season_iyaFal_2023_t2
	* Tier:	2
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	17:0:0
	* GoalParameters:	Tags&Insignia_T2up;Amount&50;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_iyaFal_2023_epi04_t2
	* Rewards:	2N:300	2O:300	2P:300
	* ScheduleType:	Locked
	* XPMod:	81
	* EndOffset:	0:0:0
	* EventId:	event_season_iyaFal_2023_t2
	* Tier:	2
	* Goals:	UpgradeOfficer,0
	* Type:	Event
	* StartOffset:	18:0:0
	* GoalParameters:	Amount&2

### qe_iyaFal_2023_epi05_t2
	* Rewards:	rw_recruitToken_hiig_minEpic:1
	* ScheduleType:	Locked
	* XPMod:	105
	* EndOffset:	0:0:0
	* EventId:	event_season_iyaFal_2023_t2
	* Tier:	2
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	19:0:0
	* GoalParameters:	Amount&1;Mode&Strike;Tags&T1up

## ql_event_iyaFal_2023_t3

### qe_iyaFal_2023_day01_t3
	* Rewards:	Z3:20
	* ScheduleType:	Locked
	* XPMod:	135
	* EndOffset:	-5:0:0
	* EventId:	event_season_iyaFal_2023_t3
	* Tier:	3
	* Goals:	CompleteQuest,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Amount&5;Tags&Faction_Tr1_T3up

### qe_iyaFal_2023_day02_t3
	* Rewards:	Z3:20
	* ScheduleType:	Locked
	* XPMod:	144
	* EndOffset:	-5:0:0
	* EventId:	event_season_iyaFal_2023_t3
	* Tier:	3
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	1:0:0
	* GoalParameters:	Tags&Salvage_T3up;Amount&5;ExcludedSources&MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_iyaFal_2023_day03_t3
	* Rewards:	Z3:20
	* ScheduleType:	Locked
	* XPMod:	153
	* EndOffset:	-5:0:0
	* EventId:	event_season_iyaFal_2023_t3
	* Tier:	3
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	2:0:0
	* GoalParameters:	Category&Crafting;Tags&Part_T3up;Amount&100

### qe_iyaFal_2023_day04_t3
	* Rewards:	Z3:20
	* ScheduleType:	Locked
	* XPMod:	162
	* EndOffset:	-5:0:0
	* EventId:	event_season_iyaFal_2023_t3
	* MailsOnCompletion:	m_iyaFal_day4_log
	* Tier:	3
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	3:0:0
	* GoalParameters:	Amount&3;Tags&T3up;Mode&Generated

### qe_iyaFal_2023_day05_t3
	* Rewards:	Z3:20
	* ScheduleType:	Locked
	* XPMod:	171
	* EndOffset:	-5:0:0
	* EventId:	event_season_iyaFal_2023_t3
	* Tier:	3
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	4:0:0
	* GoalParameters:	Amount&3;Mode&Faction;Tags&T3up

### qe_iyaFal_2023_day06_t3
	* Rewards:	Z3:20
	* ScheduleType:	Locked
	* XPMod:	180
	* EndOffset:	-5:0:0
	* EventId:	event_season_iyaFal_2023_t3
	* Tier:	3
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	5:0:0
	* GoalParameters:	Tags&Insignia_T3up;Amount&50;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_iyaFal_2023_day07_t3
	* Rewards:	Z3:20
	* ScheduleType:	Locked
	* XPMod:	189
	* EndOffset:	-5:0:0
	* EventId:	event_season_iyaFal_2023_t3
	* Tier:	3
	* Goals:	UpgradeOfficer,0
	* Type:	Event
	* StartOffset:	6:0:0
	* GoalParameters:	Amount&3

### qe_iyaFal_2023_day08_t3
	* Rewards:	Z3:20
	* ScheduleType:	Locked
	* XPMod:	198
	* EndOffset:	-5:0:0
	* EventId:	event_season_iyaFal_2023_t3
	* MailsOnCompletion:	m_iyaFal_day8_log
	* Tier:	3
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	7:0:0
	* GoalParameters:	Tags&ProgenitorRelic_T3up;Amount&1;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_iyaFal_2023_day09_t3
	* Rewards:	Z3:20
	* ScheduleType:	Locked
	* XPMod:	207
	* EndOffset:	-5:0:0
	* EventId:	event_season_iyaFal_2023_t3
	* Tier:	3
	* Goals:	CompleteQuest,0
	* Type:	Event
	* StartOffset:	8:0:0
	* GoalParameters:	Amount&5;Tags&Faction_Tr1_T3up

### qe_iyaFal_2023_day10_t3
	* Rewards:	Z3:20
	* ScheduleType:	Locked
	* XPMod:	216
	* EndOffset:	-5:0:0
	* EventId:	event_season_iyaFal_2023_t3
	* Tier:	3
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	9:0:0
	* GoalParameters:	Tags&Salvage_T3up;Amount&5;ExcludedSources&MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_iyaFal_2023_day11_t3
	* Rewards:	Z3:20
	* ScheduleType:	Locked
	* XPMod:	225
	* EndOffset:	-5:0:0
	* EventId:	event_season_iyaFal_2023_t3
	* Tier:	3
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	10:0:0
	* GoalParameters:	Id&RP;Amount&400;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_iyaFal_2023_day12_t3
	* Rewards:	Z3:20
	* ScheduleType:	Locked
	* XPMod:	234
	* EndOffset:	-5:0:0
	* EventId:	event_season_iyaFal_2023_t3
	* MailsOnCompletion:	m_iyaFal_day12_log
	* Tier:	3
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	11:0:0
	* GoalParameters:	Amount&1;Tags&Epic_T3up;Mode&Generated

### qe_iyaFal_2023_day13_t3
	* Rewards:	Z3:20
	* ScheduleType:	Locked
	* XPMod:	243
	* EndOffset:	-5:0:0
	* EventId:	event_season_iyaFal_2023_t3
	* Tier:	3
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	12:0:0
	* GoalParameters:	Ids&RepTr1;Amount&180

### qe_iyaFal_2023_day14_t3
	* Rewards:	Z3:20
	* ScheduleType:	Locked
	* XPMod:	252
	* EndOffset:	-5:0:0
	* EventId:	event_season_iyaFal_2023_t3
	* Tier:	3
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	13:0:0
	* GoalParameters:	Tags&ProgenitorRelic_T3up;Amount&1;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_iyaFal_2023_day15_t3
	* Rewards:	Z3:20	HC:100	officer_iyatequaFall_2023:1
	* ScheduleType:	Locked
	* XPMod:	315
	* EndOffset:	-5:0:0
	* EventId:	event_season_iyaFal_2023_t3
	* Tier:	3
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	14:0:0
	* GoalParameters:	Id&event_iyaFal2023_Escort_t3

## ql_event_iyaFal_2023_epilog_t3

### qe_iyaFal_2023_epi01_t3
	* Rewards:	insig_r3:50
	* ScheduleType:	Locked
	* XPMod:	189
	* EndOffset:	0:0:0
	* EventId:	event_season_iyaFal_2023_t3
	* Tier:	3
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	15:0:0
	* GoalParameters:	Tags&Gas_T3up;Amount&1000;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_iyaFal_2023_epi02_t3
	* Rewards:	3Q:500
	* ScheduleType:	Locked
	* XPMod:	207
	* EndOffset:	0:0:0
	* EventId:	event_season_iyaFal_2023_t3
	* Tier:	3
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	16:0:0
	* GoalParameters:	Ids&ShipsDestroyedProgenitorT3_ShipsDestroyedProgenitorT4;Amount&10

### qe_iyaFal_2023_epi03_t3
	* Rewards:	3H:500
	* ScheduleType:	Locked
	* XPMod:	225
	* EndOffset:	0:0:0
	* EventId:	event_season_iyaFal_2023_t3
	* Tier:	3
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	17:0:0
	* GoalParameters:	Tags&Insignia_T3up;Amount&50;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_iyaFal_2023_epi04_t3
	* Rewards:	3N:300	3O:300	3P:300
	* ScheduleType:	Locked
	* XPMod:	243
	* EndOffset:	0:0:0
	* EventId:	event_season_iyaFal_2023_t3
	* Tier:	3
	* Goals:	UpgradeOfficer,0
	* Type:	Event
	* StartOffset:	18:0:0
	* GoalParameters:	Amount&3

### qe_iyaFal_2023_epi05_t3
	* Rewards:	rw_recruitToken_hiig_minEpic:1
	* ScheduleType:	Locked
	* XPMod:	315
	* EndOffset:	0:0:0
	* EventId:	event_season_iyaFal_2023_t3
	* Tier:	3
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	19:0:0
	* GoalParameters:	Amount&3;Mode&Strike;Tags&T2up

## ql_event_iyaFal_2023_t4

### qe_iyaFal_2023_day01_t4
	* Rewards:	Z3:20
	* ScheduleType:	Locked
	* XPMod:	405
	* EndOffset:	-5:0:0
	* EventId:	event_season_iyaFal_2023_t4
	* Tier:	4
	* Goals:	CompleteQuest,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Amount&5;Tags&Faction_T4up

### qe_iyaFal_2023_day02_t4
	* Rewards:	Z3:20
	* ScheduleType:	Locked
	* XPMod:	432
	* EndOffset:	-5:0:0
	* EventId:	event_season_iyaFal_2023_t4
	* Tier:	4
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	1:0:0
	* GoalParameters:	Tags&Salvage_T4up;Amount&5;ExcludedSources&MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_iyaFal_2023_day03_t4
	* Rewards:	Z3:20
	* ScheduleType:	Locked
	* XPMod:	459
	* EndOffset:	-5:0:0
	* EventId:	event_season_iyaFal_2023_t4
	* Tier:	4
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	2:0:0
	* GoalParameters:	Category&Crafting;Tags&Part_T4up;Amount&100

### qe_iyaFal_2023_day04_t4
	* Rewards:	Z3:20
	* ScheduleType:	Locked
	* XPMod:	486
	* EndOffset:	-5:0:0
	* EventId:	event_season_iyaFal_2023_t4
	* MailsOnCompletion:	m_iyaFal_day4_log
	* Tier:	4
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	3:0:0
	* GoalParameters:	Amount&3;Tags&T4up;Mode&Generated

### qe_iyaFal_2023_day05_t4
	* Rewards:	Z3:20
	* ScheduleType:	Locked
	* XPMod:	513
	* EndOffset:	-5:0:0
	* EventId:	event_season_iyaFal_2023_t4
	* Tier:	4
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	4:0:0
	* GoalParameters:	Amount&3;Mode&Faction;Tags&T4up

### qe_iyaFal_2023_day06_t4
	* Rewards:	Z3:20
	* ScheduleType:	Locked
	* XPMod:	540
	* EndOffset:	-5:0:0
	* EventId:	event_season_iyaFal_2023_t4
	* Tier:	4
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	5:0:0
	* GoalParameters:	Tags&Insignia_T4up;Amount&50;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_iyaFal_2023_day07_t4
	* Rewards:	Z3:20
	* ScheduleType:	Locked
	* XPMod:	567
	* EndOffset:	-5:0:0
	* EventId:	event_season_iyaFal_2023_t4
	* Tier:	4
	* Goals:	UpgradeOfficer,0
	* Type:	Event
	* StartOffset:	6:0:0
	* GoalParameters:	Amount&5

### qe_iyaFal_2023_day08_t4
	* Rewards:	Z3:20
	* ScheduleType:	Locked
	* XPMod:	594
	* EndOffset:	-5:0:0
	* EventId:	event_season_iyaFal_2023_t4
	* MailsOnCompletion:	m_iyaFal_day8_log
	* Tier:	4
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	7:0:0
	* GoalParameters:	Tags&ProgenitorRelic_T4up;Amount&1;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_iyaFal_2023_day09_t4
	* Rewards:	Z3:20
	* ScheduleType:	Locked
	* XPMod:	621
	* EndOffset:	-5:0:0
	* EventId:	event_season_iyaFal_2023_t4
	* Tier:	4
	* Goals:	CompleteQuest,0
	* Type:	Event
	* StartOffset:	8:0:0
	* GoalParameters:	Amount&5;Tags&Faction_T4up

### qe_iyaFal_2023_day10_t4
	* Rewards:	Z3:20
	* ScheduleType:	Locked
	* XPMod:	648
	* EndOffset:	-5:0:0
	* EventId:	event_season_iyaFal_2023_t4
	* Tier:	4
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	9:0:0
	* GoalParameters:	Tags&Salvage_T4up;Amount&5;ExcludedSources&MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_iyaFal_2023_day11_t4
	* Rewards:	Z3:20
	* ScheduleType:	Locked
	* XPMod:	675
	* EndOffset:	-5:0:0
	* EventId:	event_season_iyaFal_2023_t4
	* Tier:	4
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	10:0:0
	* GoalParameters:	Id&RP;Amount&400;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_iyaFal_2023_day12_t4
	* Rewards:	Z3:20
	* ScheduleType:	Locked
	* XPMod:	702
	* EndOffset:	-5:0:0
	* EventId:	event_season_iyaFal_2023_t4
	* MailsOnCompletion:	m_iyaFal_day12_log
	* Tier:	4
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	11:0:0
	* GoalParameters:	Amount&1;Tags&Epic_T4up;Mode&Generated

### qe_iyaFal_2023_day13_t4
	* Rewards:	Z3:20
	* ScheduleType:	Locked
	* XPMod:	729
	* EndOffset:	-5:0:0
	* EventId:	event_season_iyaFal_2023_t4
	* Tier:	4
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	12:0:0
	* GoalParameters:	Ids&RepTr1;Amount&225

### qe_iyaFal_2023_day14_t4
	* Rewards:	Z3:20
	* ScheduleType:	Locked
	* XPMod:	756
	* EndOffset:	-5:0:0
	* EventId:	event_season_iyaFal_2023_t4
	* Tier:	4
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	13:0:0
	* GoalParameters:	Tags&ProgenitorRelic_T4up;Amount&1;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_iyaFal_2023_day15_t4
	* Rewards:	Z3:20	HC:100	officer_iyatequaFall_2023:1
	* ScheduleType:	Locked
	* XPMod:	945
	* EndOffset:	-5:0:0
	* EventId:	event_season_iyaFal_2023_t4
	* Tier:	4
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	14:0:0
	* GoalParameters:	Id&event_iyaFal2023_Escort_t4

## ql_event_iyaFal_2023_epilog_t4

### qe_iyaFal_2023_epi01_t4
	* Rewards:	insig_r4:50
	* ScheduleType:	Locked
	* XPMod:	567
	* EndOffset:	0:0:0
	* EventId:	event_season_iyaFal_2023_t4
	* Tier:	4
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	15:0:0
	* GoalParameters:	Tags&Gas_T4up;Amount&1200;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_iyaFal_2023_epi02_t4
	* Rewards:	4Q:500
	* ScheduleType:	Locked
	* XPMod:	621
	* EndOffset:	0:0:0
	* EventId:	event_season_iyaFal_2023_t4
	* Tier:	4
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	16:0:0
	* GoalParameters:	Ids&ShipsDestroyedProgenitorT4;Amount&10

### qe_iyaFal_2023_epi03_t4
	* Rewards:	4H:500
	* ScheduleType:	Locked
	* XPMod:	675
	* EndOffset:	0:0:0
	* EventId:	event_season_iyaFal_2023_t4
	* Tier:	4
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	17:0:0
	* GoalParameters:	Tags&Insignia_T4up;Amount&50;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_iyaFal_2023_epi04_t4
	* Rewards:	4U:50
	* ScheduleType:	Locked
	* XPMod:	729
	* EndOffset:	0:0:0
	* EventId:	event_season_iyaFal_2023_t4
	* Tier:	4
	* Goals:	UpgradeOfficer,0
	* Type:	Event
	* StartOffset:	18:0:0
	* GoalParameters:	Amount&5

### qe_iyaFal_2023_epi05_t4
	* Rewards:	rw_recruitToken_hiig_minEpic:1
	* ScheduleType:	Locked
	* XPMod:	945
	* EndOffset:	0:0:0
	* EventId:	event_season_iyaFal_2023_t4
	* Tier:	4
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	19:0:0
	* GoalParameters:	Amount&5;Mode&Strike;Tags&T3up

## ql_event_anniversary_2023_t1

### qe_anniversary_2023_day01_A_t1
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	5
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t1
	* Tier:	1
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Category&Crafting;Tags&T1up;Amount&1

### qe_anniversary_2023_day01_B_t1
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	5
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t1
	* Tier:	1
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Ids&ShipsDestroyedProgenitorT1_ShipsDestroyedProgenitorT2_ShipsDestroyedProgenitorT3_ShipsDestroyedProgenitorT4;Amount&7

### qe_anniversary_2023_day01_C_t1
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	5
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t1
	* Tier:	1
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Tags&ProgenitorRelic_T1up;Amount&1;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_anniversary_2023_day02_A_t1
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	6
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t1
	* Tier:	1
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	1:0:0
	* GoalParameters:	Tags&Asteroid_Crud_T1up;Amount&800;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_anniversary_2023_day02_B_t1
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	6
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t1
	* Tier:	1
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	1:0:0
	* GoalParameters:	Tags&Insignia_T1up;Amount&25;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_anniversary_2023_day02_C_t1
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	6
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t1
	* Tier:	1
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	1:0:0
	* GoalParameters:	Id&CR;Amount&1250;ExcludedSources&BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

### qe_anniversary_2023_day03_A_t1
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	7
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t1
	* Tier:	1
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	2:0:0
	* GoalParameters:	Ids&ShipsDestroyedT1_ShipsDestroyedT2_ShipsDestroyedT3_ShipsDestroyedT4;Amount&15

### qe_anniversary_2023_day03_B_t1
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	7
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t1
	* Tier:	1
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	2:0:0
	* GoalParameters:	Tags&Salvage_T1up;Amount&3;ExcludedSources&MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_OpenContainer

### qe_anniversary_2023_day03_C_t1
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	7
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t1
	* Tier:	1
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	2:0:0
	* GoalParameters:	Amount&1;Tags&Rare_T1up;Mode&Generated

### qe_anniversary_2023_day04_A_t1
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	8
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t1
	* Tier:	1
	* Goals:	Scan,0
	* Type:	Event
	* StartOffset:	3:0:0
	* GoalParameters:	Tags&InSystem_T1up;Amount&5;Analyzed&True

### qe_anniversary_2023_day04_B_t1
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	8
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t1
	* Tier:	1
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	3:0:0
	* GoalParameters:	Tags&Asteroid_Crud_T1up;Amount&800;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_anniversary_2023_day04_C_t1
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	8
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t1
	* Tier:	1
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	3:0:0
	* GoalParameters:	Amount&1;Tags&Rare_T1up;Mode&Generated

### qe_anniversary_2023_day05_A_t1
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	9
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t1
	* Tier:	1
	* Goals:	CompleteQuest,0
	* Type:	Event
	* StartOffset:	4:0:0
	* GoalParameters:	Amount&5;Tags&T1up

### qe_anniversary_2023_day05_B_t1
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	9
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t1
	* Tier:	1
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	4:0:0
	* GoalParameters:	Ids&ShipsDestroyedT1_ShipsDestroyedT2_ShipsDestroyedT3_ShipsDestroyedT4;Amount&15

### qe_anniversary_2023_day05_C_t1
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	9
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t1
	* Tier:	1
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	4:0:0
	* GoalParameters:	Tags&Salvage_T1up;Amount&3;ExcludedSources&MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_OpenContainer

### qe_anniversary_2023_day06_A_t1
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	10
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t1
	* Tier:	1
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	5:0:0
	* GoalParameters:	Tags&Insignia_T1up;Amount&25;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_anniversary_2023_day06_B_t1
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	10
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t1
	* Tier:	1
	* Goals:	UpgradeOfficer,0
	* Type:	Event
	* StartOffset:	5:0:0
	* GoalParameters:	Amount&1

### qe_anniversary_2023_day06_C_t1
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	10
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t1
	* Tier:	1
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	5:0:0
	* GoalParameters:	Amount&1;Tags&Rare_T1up;Mode&Generated

### qe_anniversary_2023_day07_A_t1
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	11
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t1
	* Tier:	1
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	6:0:0
	* GoalParameters:	Tags&Asteroid_Crud_T1up;Amount&800;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_anniversary_2023_day07_B_t1
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	11
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t1
	* Tier:	1
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	6:0:0
	* GoalParameters:	Category&Refining;Tags&Asteroid_Refined_T1up;Amount&500

### qe_anniversary_2023_day07_C_t1
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	11
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t1
	* Tier:	1
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	6:0:0
	* GoalParameters:	Category&Crafting;Tags&T1up;Amount&1

### qe_anniversary_2023_day08_A_t1
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	12
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t1
	* Tier:	1
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	7:0:0
	* GoalParameters:	Ids&ShipsDestroyedP1T1_ShipsDestroyedP1T2_ShipsDestroyedP1T3_ShipsDestroyedP1T4;Amount&10

### qe_anniversary_2023_day08_B_t1
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	12
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t1
	* Tier:	1
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	7:0:0
	* GoalParameters:	Tags&Salvage_T1up;Amount&3;ExcludedSources&MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_OpenContainer

### qe_anniversary_2023_day08_C_t1
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	12
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t1
	* Tier:	1
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	7:0:0
	* GoalParameters:	Ids&ShipsDestroyedP1T1_ShipsDestroyedP1T2_ShipsDestroyedP1T3_ShipsDestroyedP1T4;Amount&20

### qe_anniversary_2023_day09_A_t1
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	13
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t1
	* Tier:	1
	* Goals:	UpgradeOfficer,0
	* Type:	Event
	* StartOffset:	8:0:0
	* GoalParameters:	Amount&1

### qe_anniversary_2023_day09_B_t1
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	13
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t1
	* Tier:	1
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	8:0:0
	* GoalParameters:	Category&Crafting;Tags&T1up;Amount&1

### qe_anniversary_2023_day09_C_t1
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	13
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t1
	* Tier:	1
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	8:0:0
	* GoalParameters:	Amount&1;Tags&Rare_T1up;Mode&Generated

### qe_anniversary_2023_day10_A_t1
	* Rewards:	Z0:30	LP:50
	* ScheduleType:	Locked
	* XPMod:	20
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t1
	* MailsOnCompletion:	m_anniversary_enoch_log
	* Tier:	1
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	9:0:0
	* GoalParameters:	Id&event_anniversary2023_Wiracoda_t1

## ql_event_anniversary_2023_t2

### qe_anniversary_2023_day01_A_t2
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	15
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t2
	* Tier:	2
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Id&RP;Amount&200;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_anniversary_2023_day01_B_t2
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	15
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t2
	* Tier:	2
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Ids&ShipsDestroyedProgenitorT2_ShipsDestroyedProgenitorT3_ShipsDestroyedProgenitorT4;Amount&7

### qe_anniversary_2023_day01_C_t2
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	15
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t2
	* Tier:	2
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Tags&ProgenitorRelic_T2up;Amount&1;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_anniversary_2023_day02_A_t2
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	18
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t2
	* Tier:	2
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	1:0:0
	* GoalParameters:	Tags&AsteroidD_Crud_T2up;Amount&400;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_anniversary_2023_day02_B_t2
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	18
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t2
	* Tier:	2
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	1:0:0
	* GoalParameters:	Ids&RepTr1;Amount&135

### qe_anniversary_2023_day02_C_t2
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	18
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t2
	* Tier:	2
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	1:0:0
	* GoalParameters:	Id&CR;Amount&2500;ExcludedSources&BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

### qe_anniversary_2023_day03_A_t2
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	21
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t2
	* Tier:	2
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	2:0:0
	* GoalParameters:	Ids&ShipsDestroyedT2_ShipsDestroyedT3_ShipsDestroyedT4;Amount&15

### qe_anniversary_2023_day03_B_t2
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	21
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t2
	* Tier:	2
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	2:0:0
	* GoalParameters:	Tags&Salvage_T2up;Amount&3;ExcludedSources&MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_OpenContainer

### qe_anniversary_2023_day03_C_t2
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	21
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t2
	* Tier:	2
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	2:0:0
	* GoalParameters:	Amount&1;Mode&Strike;Tags&T1up

### qe_anniversary_2023_day04_A_t2
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	24
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t2
	* Tier:	2
	* Goals:	Scan,0
	* Type:	Event
	* StartOffset:	3:0:0
	* GoalParameters:	Tags&InSystem_T2up;Amount&5;Analyzed&True

### qe_anniversary_2023_day04_B_t2
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	24
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t2
	* Tier:	2
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	3:0:0
	* GoalParameters:	Tags&Asteroid_Crud_T2up;Amount&1000;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_anniversary_2023_day04_C_t2
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	24
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t2
	* Tier:	2
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	3:0:0
	* GoalParameters:	Amount&1;Tags&Epic_T2up;Mode&Generated

### qe_anniversary_2023_day05_A_t2
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	27
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t2
	* Tier:	2
	* Goals:	CompleteQuest,0
	* Type:	Event
	* StartOffset:	4:0:0
	* GoalParameters:	Amount&5;Tags&Faction_T2up

### qe_anniversary_2023_day05_B_t2
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	27
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t2
	* Tier:	2
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	4:0:0
	* GoalParameters:	Amount&3;Mode&Faction;Tags&T2up_Tanoch

### qe_anniversary_2023_day05_C_t2
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	27
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t2
	* Tier:	2
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	4:0:0
	* GoalParameters:	Id&RepTanoch;Amount&135

### qe_anniversary_2023_day06_A_t2
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	30
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t2
	* Tier:	2
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	5:0:0
	* GoalParameters:	Tags&Insignia_T2up;Amount&25;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_anniversary_2023_day06_B_t2
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	30
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t2
	* Tier:	2
	* Goals:	UpgradeOfficer,0
	* Type:	Event
	* StartOffset:	5:0:0
	* GoalParameters:	Amount&2

### qe_anniversary_2023_day06_C_t2
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	30
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t2
	* Tier:	2
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	5:0:0
	* GoalParameters:	Amount&1;Mode&Strike;Tags&T1up

### qe_anniversary_2023_day07_A_t2
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	33
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t2
	* Tier:	2
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	6:0:0
	* GoalParameters:	Tags&Asteroid_Crud_T2up;Amount&1000;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_anniversary_2023_day07_B_t2
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	33
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t2
	* Tier:	2
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	6:0:0
	* GoalParameters:	Category&Refining;Tags&Asteroid_Refined_T2up;Amount&500

### qe_anniversary_2023_day07_C_t2
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	33
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t2
	* Tier:	2
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	6:0:0
	* GoalParameters:	Category&Crafting;Tags&Part_T2up;Amount&50

### qe_anniversary_2023_day08_A_t2
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	36
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t2
	* Tier:	2
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	7:0:0
	* GoalParameters:	Ids&ShipsDestroyedP1T2_ShipsDestroyedP1T3_ShipsDestroyedP1T4;Amount&10

### qe_anniversary_2023_day08_B_t2
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	36
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t2
	* Tier:	2
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	7:0:0
	* GoalParameters:	Tags&Salvage_T2up;Amount&3;ExcludedSources&MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_OpenContainer

### qe_anniversary_2023_day08_C_t2
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	36
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t2
	* Tier:	2
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	7:0:0
	* GoalParameters:	Ids&ShipsDestroyedP1T2_ShipsDestroyedP1T3_ShipsDestroyedP1T4;Amount&20

### qe_anniversary_2023_day09_A_t2
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	39
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t2
	* Tier:	2
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	8:0:0
	* GoalParameters:	Category&Upgrade;Tags&External_Module_T1up;Amount&1

### qe_anniversary_2023_day09_B_t2
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	39
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t2
	* Tier:	2
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	8:0:0
	* GoalParameters:	Category&Crafting;Tags&Part_T2up;Amount&50

### qe_anniversary_2023_day09_C_t2
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	39
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t2
	* Tier:	2
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	8:0:0
	* GoalParameters:	Amount&1;Mode&Strike;Tags&T1up

### qe_anniversary_2023_day10_A_t2
	* Rewards:	Z0:30	LP:50
	* ScheduleType:	Locked
	* XPMod:	60
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t2
	* MailsOnCompletion:	m_anniversary_enoch_log
	* Tier:	2
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	9:0:0
	* GoalParameters:	Id&event_anniversary2023_Wiracoda_t2

## ql_event_anniversary_2023_t3

### qe_anniversary_2023_day01_A_t3
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	45
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t3
	* Tier:	3
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Id&RP;Amount&200;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_anniversary_2023_day01_B_t3
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	45
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t3
	* Tier:	3
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Ids&ShipsDestroyedProgenitorT3_ShipsDestroyedProgenitorT4;Amount&7

### qe_anniversary_2023_day01_C_t3
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	45
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t3
	* Tier:	3
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Tags&ProgenitorRelic_T3up;Amount&1;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_anniversary_2023_day02_A_t3
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	54
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t3
	* Tier:	3
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	1:0:0
	* GoalParameters:	Tags&AsteroidD_Crud_T3up;Amount&500;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_anniversary_2023_day02_B_t3
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	54
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t3
	* Tier:	3
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	1:0:0
	* GoalParameters:	Ids&RepTr1;Amount&180

### qe_anniversary_2023_day02_C_t3
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	54
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t3
	* Tier:	3
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	1:0:0
	* GoalParameters:	Id&CR;Amount&5000;ExcludedSources&BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

### qe_anniversary_2023_day03_A_t3
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	63
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t3
	* Tier:	3
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	2:0:0
	* GoalParameters:	Ids&ShipsDestroyedT3_ShipsDestroyedT4;Amount&15

### qe_anniversary_2023_day03_B_t3
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	63
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t3
	* Tier:	3
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	2:0:0
	* GoalParameters:	Tags&Salvage_T3up;Amount&3;ExcludedSources&MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_OpenContainer

### qe_anniversary_2023_day03_C_t3
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	63
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t3
	* Tier:	3
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	2:0:0
	* GoalParameters:	Amount&1;Mode&Strike;Tags&T2up

### qe_anniversary_2023_day04_A_t3
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	72
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t3
	* Tier:	3
	* Goals:	Scan,0
	* Type:	Event
	* StartOffset:	3:0:0
	* GoalParameters:	Tags&InSystem_T3up;Amount&5;Analyzed&True

### qe_anniversary_2023_day04_B_t3
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	72
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t3
	* Tier:	3
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	3:0:0
	* GoalParameters:	Tags&Gas_T3up;Amount&800;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_anniversary_2023_day04_C_t3
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	72
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t3
	* Tier:	3
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	3:0:0
	* GoalParameters:	Amount&1;Tags&Epic_T3up;Mode&Generated

### qe_anniversary_2023_day05_A_t3
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	81
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t3
	* Tier:	3
	* Goals:	CompleteQuest,0
	* Type:	Event
	* StartOffset:	4:0:0
	* GoalParameters:	Amount&5;Tags&Faction_T3up

### qe_anniversary_2023_day05_B_t3
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	81
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t3
	* Tier:	3
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	4:0:0
	* GoalParameters:	Amount&3;Mode&Faction;Tags&T3up_Tanoch

### qe_anniversary_2023_day05_C_t3
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	81
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t3
	* Tier:	3
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	4:0:0
	* GoalParameters:	Id&RepTanoch;Amount&180

### qe_anniversary_2023_day06_A_t3
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	90
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t3
	* Tier:	3
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	5:0:0
	* GoalParameters:	Tags&Insignia_T3up;Amount&25;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_anniversary_2023_day06_B_t3
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	90
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t3
	* Tier:	3
	* Goals:	UpgradeOfficer,0
	* Type:	Event
	* StartOffset:	5:0:0
	* GoalParameters:	Amount&3

### qe_anniversary_2023_day06_C_t3
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	90
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t3
	* Tier:	3
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	5:0:0
	* GoalParameters:	Amount&1;Mode&Strike;Tags&T2up

### qe_anniversary_2023_day07_A_t3
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	99
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t3
	* Tier:	3
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	6:0:0
	* GoalParameters:	Tags&Asteroid_Crud_T3up;Amount&1200;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_anniversary_2023_day07_B_t3
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	99
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t3
	* Tier:	3
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	6:0:0
	* GoalParameters:	Category&Refining;Tags&Asteroid_Refined_T3up;Amount&500

### qe_anniversary_2023_day07_C_t3
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	99
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t3
	* Tier:	3
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	6:0:0
	* GoalParameters:	Category&Crafting;Tags&Part_T3up;Amount&50

### qe_anniversary_2023_day08_A_t3
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	108
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t3
	* Tier:	3
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	7:0:0
	* GoalParameters:	Ids&ShipsDestroyedP1T3_ShipsDestroyedP1T4;Amount&10

### qe_anniversary_2023_day08_B_t3
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	108
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t3
	* Tier:	3
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	7:0:0
	* GoalParameters:	Tags&Salvage_T3up;Amount&3;ExcludedSources&MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_OpenContainer

### qe_anniversary_2023_day08_C_t3
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	108
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t3
	* Tier:	3
	* Goals:	CompleteQuest,0
	* Type:	Event
	* StartOffset:	7:0:0
	* GoalParameters:	Id&qr_015

### qe_anniversary_2023_day09_A_t3
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	117
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t3
	* Tier:	3
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	8:0:0
	* GoalParameters:	Category&Upgrade;Tags&External_Module_T2up;Amount&1

### qe_anniversary_2023_day09_B_t3
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	117
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t3
	* Tier:	3
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	8:0:0
	* GoalParameters:	Category&Upgrade;Tags&Internal_Module_T2up;Amount&1

### qe_anniversary_2023_day09_C_t3
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	117
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t3
	* Tier:	3
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	8:0:0
	* GoalParameters:	Amount&1;Mode&Strike;Tags&T2up

### qe_anniversary_2023_day10_A_t3
	* Rewards:	Z0:30	LP:50
	* ScheduleType:	Locked
	* XPMod:	180
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t3
	* MailsOnCompletion:	m_anniversary_enoch_log
	* Tier:	3
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	9:0:0
	* GoalParameters:	Id&event_anniversary2023_Wiracoda_t3

## ql_event_anniversary_2023_t4

### qe_anniversary_2023_day01_A_t4
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	135
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t4
	* Tier:	4
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Id&RP;Amount&200;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_anniversary_2023_day01_B_t4
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	135
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t4
	* Tier:	4
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Ids&ShipsDestroyedProgenitorT4;Amount&7

### qe_anniversary_2023_day01_C_t4
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	135
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t4
	* Tier:	4
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Tags&ProgenitorRelic_T4up;Amount&1;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_anniversary_2023_day02_A_t4
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	162
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t4
	* Tier:	4
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	1:0:0
	* GoalParameters:	Tags&AsteroidD_Crud_T4up;Amount&600;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_anniversary_2023_day02_B_t4
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	162
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t4
	* Tier:	4
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	1:0:0
	* GoalParameters:	Ids&RepTr1;Amount&225

### qe_anniversary_2023_day02_C_t4
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	162
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t4
	* Tier:	4
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	1:0:0
	* GoalParameters:	Id&CR;Amount&10000;ExcludedSources&BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

### qe_anniversary_2023_day03_A_t4
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	189
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t4
	* Tier:	4
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	2:0:0
	* GoalParameters:	Ids&ShipsDestroyedT4;Amount&15

### qe_anniversary_2023_day03_B_t4
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	189
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t4
	* Tier:	4
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	2:0:0
	* GoalParameters:	Tags&Salvage_T4up;Amount&3;ExcludedSources&MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_OpenContainer

### qe_anniversary_2023_day03_C_t4
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	189
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t4
	* Tier:	4
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	2:0:0
	* GoalParameters:	Amount&1;Mode&Strike;Tags&T3up

### qe_anniversary_2023_day04_A_t4
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	216
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t4
	* Tier:	4
	* Goals:	Scan,0
	* Type:	Event
	* StartOffset:	3:0:0
	* GoalParameters:	Tags&InSystem_T4up;Amount&5;Analyzed&True

### qe_anniversary_2023_day04_B_t4
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	216
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t4
	* Tier:	4
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	3:0:0
	* GoalParameters:	Tags&Gas_T4up;Amount&1000;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_anniversary_2023_day04_C_t4
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	216
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t4
	* Tier:	4
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	3:0:0
	* GoalParameters:	Amount&1;Tags&Epic_T4up;Mode&Generated

### qe_anniversary_2023_day05_A_t4
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	243
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t4
	* Tier:	4
	* Goals:	CompleteQuest,0
	* Type:	Event
	* StartOffset:	4:0:0
	* GoalParameters:	Amount&5;Tags&Faction_T4up

### qe_anniversary_2023_day05_B_t4
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	243
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t4
	* Tier:	4
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	4:0:0
	* GoalParameters:	Amount&3;Mode&Faction;Tags&T4up_Tanoch

### qe_anniversary_2023_day05_C_t4
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	243
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t4
	* Tier:	4
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	4:0:0
	* GoalParameters:	Id&RepTanoch;Amount&225

### qe_anniversary_2023_day06_A_t4
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	270
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t4
	* Tier:	4
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	5:0:0
	* GoalParameters:	Tags&Insignia_T4up;Amount&25;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_anniversary_2023_day06_B_t4
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	270
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t4
	* Tier:	4
	* Goals:	UpgradeOfficer,0
	* Type:	Event
	* StartOffset:	5:0:0
	* GoalParameters:	Amount&5

### qe_anniversary_2023_day06_C_t4
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	270
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t4
	* Tier:	4
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	5:0:0
	* GoalParameters:	Amount&1;Mode&Strike;Tags&T3up

### qe_anniversary_2023_day07_A_t4
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	297
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t4
	* Tier:	4
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	6:0:0
	* GoalParameters:	Tags&Asteroid_Crud_T4up;Amount&1400;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_anniversary_2023_day07_B_t4
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	297
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t4
	* Tier:	4
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	6:0:0
	* GoalParameters:	Category&Refining;Tags&Asteroid_Refined_T4up;Amount&500

### qe_anniversary_2023_day07_C_t4
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	297
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t4
	* Tier:	4
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	6:0:0
	* GoalParameters:	Category&Crafting;Tags&Part_T4up;Amount&50

### qe_anniversary_2023_day08_A_t4
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	324
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t4
	* Tier:	4
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	7:0:0
	* GoalParameters:	Ids&ShipsDestroyedP1T4;Amount&10

### qe_anniversary_2023_day08_B_t4
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	324
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t4
	* Tier:	4
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	7:0:0
	* GoalParameters:	Tags&Salvage_T4up;Amount&3;ExcludedSources&MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_OpenContainer

### qe_anniversary_2023_day08_C_t4
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	324
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t4
	* Tier:	4
	* Goals:	CompleteQuest,0
	* Type:	Event
	* StartOffset:	7:0:0
	* GoalParameters:	Id&qr_018

### qe_anniversary_2023_day09_A_t4
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	351
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t4
	* Tier:	4
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	8:0:0
	* GoalParameters:	Category&Upgrade;Tags&External_Module_T3up;Amount&1

### qe_anniversary_2023_day09_B_t4
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	351
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t4
	* Tier:	4
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	8:0:0
	* GoalParameters:	Category&Upgrade;Tags&Internal_Module_T3up;Amount&1

### qe_anniversary_2023_day09_C_t4
	* Rewards:	Z0:10
	* ScheduleType:	Locked
	* XPMod:	351
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t4
	* Tier:	4
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	8:0:0
	* GoalParameters:	Amount&1;Mode&Strike;Tags&T3up

### qe_anniversary_2023_day10_A_t4
	* Rewards:	Z0:30	LP:50
	* ScheduleType:	Locked
	* XPMod:	540
	* EndOffset:	0:0:0
	* EventId:	event_anniversary_2023_t4
	* MailsOnCompletion:	m_anniversary_enoch_log
	* Tier:	4
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	9:0:0
	* GoalParameters:	Id&event_anniversary2023_Wiracoda_t4

## ql_event_halloween_2023_t1

### qe_halloween_2023_day01_t1
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	15
	* EndOffset:	0:0:0
	* EventId:	event_halloween_2023_t1
	* Tier:	1
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Ids&ShipsDestroyedProgenitorT1_ShipsDestroyedProgenitorT2_ShipsDestroyedProgenitorT3_ShipsDestroyedProgenitorT4;Amount&10

### qe_halloween_2023_day02_t1
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	16
	* EndOffset:	0:0:0
	* EventId:	event_halloween_2023_t1
	* Tier:	1
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	1:0:0
	* GoalParameters:	Tags&Asteroid_Crud_T1up;Amount&800;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_halloween_2023_day03_t1
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	17
	* EndOffset:	0:0:0
	* EventId:	event_halloween_2023_t1
	* Tier:	1
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	2:0:0
	* GoalParameters:	Tags&Salvage_T1up;Amount&5;ExcludedSources&MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_OpenContainer

### qe_halloween_2023_day04_t1
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	18
	* EndOffset:	0:0:0
	* EventId:	event_halloween_2023_t1
	* Tier:	1
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	3:0:0
	* GoalParameters:	Tags&RareEarth_T1up;Amount&20;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_halloween_2023_day05_t1
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	19
	* EndOffset:	0:0:0
	* EventId:	event_halloween_2023_t1
	* Tier:	1
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	4:0:0
	* GoalParameters:	Tags&ProgenitorRelic_T1up;Amount&1;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_halloween_2023_day06_t1
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	20
	* EndOffset:	0:0:0
	* EventId:	event_halloween_2023_t1
	* Tier:	1
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	5:0:0
	* GoalParameters:	Category&Crafting;Tags&T1up;Amount&5

### qe_halloween_2023_day07_t1
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	21
	* EndOffset:	0:0:0
	* EventId:	event_halloween_2023_t1
	* Tier:	1
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	6:0:0
	* GoalParameters:	Ids&ShipsDestroyedProgenitorT1_ShipsDestroyedProgenitorT2_ShipsDestroyedProgenitorT3_ShipsDestroyedProgenitorT4;Amount&10

### qe_halloween_2023_day08_t1
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	22
	* EndOffset:	0:0:0
	* EventId:	event_halloween_2023_t1
	* Tier:	1
	* Goals:	UpgradeOfficer,0
	* Type:	Event
	* StartOffset:	7:0:0
	* GoalParameters:	Amount&1

### qe_halloween_2023_day09_t1
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	23
	* EndOffset:	0:0:0
	* EventId:	event_halloween_2023_t1
	* Tier:	1
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	8:0:0
	* GoalParameters:	Amount&1;Tags&Rare_T1up;Mode&Generated

### qe_halloween_2023_day10_t1
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	24
	* EndOffset:	0:0:0
	* EventId:	event_halloween_2023_t1
	* Tier:	1
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	9:0:0
	* GoalParameters:	Id&CR;Amount&1250;ExcludedSources&BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

### qe_halloween_2023_day11_t1
	* Rewards:	Z0:20	LP:50
	* ScheduleType:	Locked
	* XPMod:	30
	* EndOffset:	0:0:0
	* EventId:	event_halloween_2023_t1
	* Tier:	1
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	10:0:0
	* GoalParameters:	Id&event_halloween2023_Rashidun_t1

## ql_event_halloween_2023_t2

### qe_halloween_2023_day01_t2
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	45
	* EndOffset:	0:0:0
	* EventId:	event_halloween_2023_t2
	* Tier:	2
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Ids&ShipsDestroyedProgenitorT2_ShipsDestroyedProgenitorT3_ShipsDestroyedProgenitorT4;Amount&10

### qe_halloween_2023_day02_t2
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	48
	* EndOffset:	0:0:0
	* EventId:	event_halloween_2023_t2
	* Tier:	2
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	1:0:0
	* GoalParameters:	Tags&Asteroid_Crud_T2up;Amount&1000;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_halloween_2023_day03_t2
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	51
	* EndOffset:	0:0:0
	* EventId:	event_halloween_2023_t2
	* Tier:	2
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	2:0:0
	* GoalParameters:	Tags&Salvage_T2up;Amount&5;ExcludedSources&MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_OpenContainer

### qe_halloween_2023_day04_t2
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	54
	* EndOffset:	0:0:0
	* EventId:	event_halloween_2023_t2
	* Tier:	2
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	3:0:0
	* GoalParameters:	Tags&RareEarth_T2up;Amount&20;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_halloween_2023_day05_t2
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	57
	* EndOffset:	0:0:0
	* EventId:	event_halloween_2023_t2
	* Tier:	2
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	4:0:0
	* GoalParameters:	Tags&ProgenitorRelic_T2up;Amount&1;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_halloween_2023_day06_t2
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	60
	* EndOffset:	0:0:0
	* EventId:	event_halloween_2023_t2
	* Tier:	2
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	5:0:0
	* GoalParameters:	Category&Crafting;Tags&Part_T2up;Amount&100

### qe_halloween_2023_day07_t2
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	63
	* EndOffset:	0:0:0
	* EventId:	event_halloween_2023_t2
	* Tier:	2
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	6:0:0
	* GoalParameters:	Ids&ShipsDestroyedProgenitorT2_ShipsDestroyedProgenitorT3_ShipsDestroyedProgenitorT4;Amount&10

### qe_halloween_2023_day08_t2
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	66
	* EndOffset:	0:0:0
	* EventId:	event_halloween_2023_t2
	* Tier:	2
	* Goals:	UpgradeOfficer,0
	* Type:	Event
	* StartOffset:	7:0:0
	* GoalParameters:	Amount&2

### qe_halloween_2023_day09_t2
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	69
	* EndOffset:	0:0:0
	* EventId:	event_halloween_2023_t2
	* Tier:	2
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	8:0:0
	* GoalParameters:	Amount&1;Mode&Strike;Tags&T1up

### qe_halloween_2023_day10_t2
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	72
	* EndOffset:	0:0:0
	* EventId:	event_halloween_2023_t2
	* Tier:	2
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	9:0:0
	* GoalParameters:	Id&CR;Amount&2500;ExcludedSources&BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

### qe_halloween_2023_day11_t2
	* Rewards:	Z0:20	LP:50
	* ScheduleType:	Locked
	* XPMod:	90
	* EndOffset:	0:0:0
	* EventId:	event_halloween_2023_t2
	* Tier:	2
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	10:0:0
	* GoalParameters:	Id&event_halloween2023_Rashidun_t2

## ql_event_halloween_2023_t3

### qe_halloween_2023_day01_t3
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	135
	* EndOffset:	0:0:0
	* EventId:	event_halloween_2023_t3
	* Tier:	3
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Ids&ShipsDestroyedProgenitorT3_ShipsDestroyedProgenitorT4;Amount&10

### qe_halloween_2023_day02_t3
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	144
	* EndOffset:	0:0:0
	* EventId:	event_halloween_2023_t3
	* Tier:	3
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	1:0:0
	* GoalParameters:	Tags&Gas_T3up;Amount&1000;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_halloween_2023_day03_t3
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	153
	* EndOffset:	0:0:0
	* EventId:	event_halloween_2023_t3
	* Tier:	3
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	2:0:0
	* GoalParameters:	Tags&Salvage_T3up;Amount&5;ExcludedSources&MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_OpenContainer

### qe_halloween_2023_day04_t3
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	162
	* EndOffset:	0:0:0
	* EventId:	event_halloween_2023_t3
	* Tier:	3
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	3:0:0
	* GoalParameters:	Tags&RareEarth_T3up;Amount&20;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_halloween_2023_day05_t3
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	171
	* EndOffset:	0:0:0
	* EventId:	event_halloween_2023_t3
	* Tier:	3
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	4:0:0
	* GoalParameters:	Tags&ProgenitorRelic_T3up;Amount&1;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_halloween_2023_day06_t3
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	180
	* EndOffset:	0:0:0
	* EventId:	event_halloween_2023_t3
	* Tier:	3
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	5:0:0
	* GoalParameters:	Category&Crafting;Tags&Part_T3up;Amount&100

### qe_halloween_2023_day07_t3
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	189
	* EndOffset:	0:0:0
	* EventId:	event_halloween_2023_t3
	* Tier:	3
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	6:0:0
	* GoalParameters:	Ids&ShipsDestroyedProgenitorT3_ShipsDestroyedProgenitorT4;Amount&10

### qe_halloween_2023_day08_t3
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	198
	* EndOffset:	0:0:0
	* EventId:	event_halloween_2023_t3
	* Tier:	3
	* Goals:	UpgradeOfficer,0
	* Type:	Event
	* StartOffset:	7:0:0
	* GoalParameters:	Amount&3

### qe_halloween_2023_day09_t3
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	207
	* EndOffset:	0:0:0
	* EventId:	event_halloween_2023_t3
	* Tier:	3
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	8:0:0
	* GoalParameters:	Amount&3;Mode&Strike;Tags&T2up

### qe_halloween_2023_day10_t3
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	216
	* EndOffset:	0:0:0
	* EventId:	event_halloween_2023_t3
	* Tier:	3
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	9:0:0
	* GoalParameters:	Id&CR;Amount&5000;ExcludedSources&BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

### qe_halloween_2023_day11_t3
	* Rewards:	Z0:20	LP:50
	* ScheduleType:	Locked
	* XPMod:	270
	* EndOffset:	0:0:0
	* EventId:	event_halloween_2023_t3
	* Tier:	3
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	10:0:0
	* GoalParameters:	Id&event_halloween2023_Rashidun_t3

## ql_event_halloween_2023_t4

### qe_halloween_2023_day01_t4
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	405
	* EndOffset:	0:0:0
	* EventId:	event_halloween_2023_t4
	* Tier:	4
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Ids&ShipsDestroyedProgenitorT4;Amount&10

### qe_halloween_2023_day02_t4
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	432
	* EndOffset:	0:0:0
	* EventId:	event_halloween_2023_t4
	* Tier:	4
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	1:0:0
	* GoalParameters:	Tags&Gas_T4up;Amount&1200;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_halloween_2023_day03_t4
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	459
	* EndOffset:	0:0:0
	* EventId:	event_halloween_2023_t4
	* Tier:	4
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	2:0:0
	* GoalParameters:	Tags&Salvage_T4up;Amount&5;ExcludedSources&MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_OpenContainer

### qe_halloween_2023_day04_t4
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	486
	* EndOffset:	0:0:0
	* EventId:	event_halloween_2023_t4
	* Tier:	4
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	3:0:0
	* GoalParameters:	Tags&RareEarth_T4up;Amount&20;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_halloween_2023_day05_t4
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	513
	* EndOffset:	0:0:0
	* EventId:	event_halloween_2023_t4
	* Tier:	4
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	4:0:0
	* GoalParameters:	Tags&ProgenitorRelic_T4up;Amount&1;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_halloween_2023_day06_t4
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	540
	* EndOffset:	0:0:0
	* EventId:	event_halloween_2023_t4
	* Tier:	4
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	5:0:0
	* GoalParameters:	Category&Crafting;Tags&Part_T4up;Amount&100

### qe_halloween_2023_day07_t4
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	567
	* EndOffset:	0:0:0
	* EventId:	event_halloween_2023_t4
	* Tier:	4
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	6:0:0
	* GoalParameters:	Ids&ShipsDestroyedProgenitorT4;Amount&10

### qe_halloween_2023_day08_t4
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	594
	* EndOffset:	0:0:0
	* EventId:	event_halloween_2023_t4
	* Tier:	4
	* Goals:	UpgradeOfficer,0
	* Type:	Event
	* StartOffset:	7:0:0
	* GoalParameters:	Amount&5

### qe_halloween_2023_day09_t4
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	621
	* EndOffset:	0:0:0
	* EventId:	event_halloween_2023_t4
	* Tier:	4
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	8:0:0
	* GoalParameters:	Amount&5;Mode&Strike;Tags&T3up

### qe_halloween_2023_day10_t4
	* Rewards:	Z0:20
	* ScheduleType:	Locked
	* XPMod:	648
	* EndOffset:	0:0:0
	* EventId:	event_halloween_2023_t4
	* Tier:	4
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	9:0:0
	* GoalParameters:	Id&CR;Amount&10000;ExcludedSources&BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

### qe_halloween_2023_day11_t4
	* Rewards:	Z0:20	LP:50
	* ScheduleType:	Locked
	* XPMod:	810
	* EndOffset:	0:0:0
	* EventId:	event_halloween_2023_t4
	* Tier:	4
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	10:0:0
	* GoalParameters:	Id&event_halloween2023_Rashidun_t4

## ql_event_tanochWinter_2023_t1

### qe_tanWin_2023_day01_t1
	* Rewards:	Z2:20
	* ScheduleType:	Hidden
	* XPMod:	15
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t1
	* MailsOnCompletion:	m_tanWin_2023_d01_log
	* Tier:	1
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Tags&Asteroid_Crud_T1up;Amount&1000;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_tanWin_2023_day02_t1
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	16
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t1
	* Tier:	1
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	1:0:0
	* GoalParameters:	Tags&RareEarth_T1up;Amount&50;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_tanWin_2023_day03_t1
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	17
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t1
	* Tier:	1
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	2:0:0
	* GoalParameters:	Tags&Salvage_T1up;Amount&5;ExcludedSources&MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_OpenContainer

### qe_tanWin_2023_day04_t1
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	18
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t1
	* Tier:	1
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	3:0:0
	* GoalParameters:	Id&CR;Amount&1250;ExcludedSources&BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

### qe_tanWin_2023_day05_t1
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	19
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t1
	* Tier:	1
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	4:0:0
	* GoalParameters:	Id&event_tanWin2023_DefendBase_t1

### qe_tanWin_2023_day06_t1
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	20
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t1
	* MailsOnCompletion:	m_tanWin_2023_d06_log
	* Tier:	1
	* Goals:	CompleteQuest,0
	* Type:	Event
	* StartOffset:	5:0:0
	* GoalParameters:	Amount&5;Tags&T1up

### qe_tanWin_2023_day07_t1
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	21
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t1
	* Tier:	1
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	6:0:0
	* GoalParameters:	Ids&ShipsDestroyedT1_ShipsDestroyedT2_ShipsDestroyedT3_ShipsDestroyedT4;Amount&15

### qe_tanWin_2023_day08_t1
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	22
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t1
	* Tier:	1
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	7:0:0
	* GoalParameters:	Amount&1;Tags&Rare_T1up;Mode&Generated

### qe_tanWin_2023_day09_t1
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	23
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t1
	* Tier:	1
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	8:0:0
	* GoalParameters:	Tags&RareEarth_T1up;Amount&50;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_tanWin_2023_day10_t1
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	24
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t1
	* Tier:	1
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	9:0:0
	* GoalParameters:	Id&event_tanWin2023_AttackBase_t1

### qe_tanWin_2023_day11_t1
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	25
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t1
	* MailsOnCompletion:	m_tanWin_2023_d11_log
	* Tier:	1
	* Goals:	CompleteQuest,0
	* Type:	Event
	* StartOffset:	10:0:0
	* GoalParameters:	Amount&5;Tags&T1up

### qe_tanWin_2023_day12_t1
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	26
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t1
	* Tier:	1
	* Goals:	Scan,0
	* Type:	Event
	* StartOffset:	11:0:0
	* GoalParameters:	Tags&InSystem_T1up;Amount&10;Analyzed&True

### qe_tanWin_2023_day13_t1
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	29
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t1
	* Tier:	1
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	12:0:0
	* GoalParameters:	Tags&Insignia_T1up;Amount&25;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_tanWin_2023_day14_t1
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	27
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t1
	* Tier:	1
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	13:0:0
	* GoalParameters:	Amount&1;Tags&Rare_T1up;Mode&Generated

### qe_tanWin_2023_day15_t1
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	28
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t1
	* Tier:	1
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	14:0:0
	* GoalParameters:	Ids&ShipsDestroyedT1_ShipsDestroyedT2_ShipsDestroyedT3_ShipsDestroyedT4;Amount&15

### qe_tanWin_2023_day16_t1
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	30
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t1
	* Tier:	1
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	15:0:0
	* GoalParameters:	Id&event_tanWin2023_Relic_t1

### qe_tanWin_2023_day17_t1
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	31
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t1
	* MailsOnCompletion:	m_tanWin_2023_d17_log
	* Tier:	1
	* Goals:	CompleteQuest,0
	* Type:	Event
	* StartOffset:	16:0:0
	* GoalParameters:	Amount&5;Tags&T1up

### qe_tanWin_2023_day18_t1
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	32
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t1
	* Tier:	1
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	17:0:0
	* GoalParameters:	Id&CR;Amount&1250;ExcludedSources&BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

### qe_tanWin_2023_day19_t1
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	33
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t1
	* Tier:	1
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	18:0:0
	* GoalParameters:	Amount&1;Tags&Rare_T1up;Mode&Generated

### qe_tanWin_2023_day20_t1
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	34
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t1
	* Tier:	1
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	19:0:0
	* GoalParameters:	Ids&ShipsDestroyedT1_ShipsDestroyedT2_ShipsDestroyedT3_ShipsDestroyedT4;Amount&15

### qe_tanWin_2023_day21_t1
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	35
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t1
	* Tier:	1
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	20:0:0
	* GoalParameters:	Ids&ShipsDestroyedProgenitorT1_ShipsDestroyedProgenitorT2_ShipsDestroyedProgenitorT3_ShipsDestroyedProgenitorT4;Amount&10

### qe_tanWin_2023_day22_t1
	* Rewards:	Z2:20	officer_tanochWinter_2023:1
	* ScheduleType:	Locked
	* XPMod:	36
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t1
	* MailsOnCompletion:	m_tanWin_2023_d22_log
	* Tier:	1
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	21:0:0
	* GoalParameters:	Id&event_tanWin2023_Academy_t1

## ql_event_tanochWinter_2023_t2

### qe_tanWin_2023_day01_t2
	* Rewards:	Z2:20
	* ScheduleType:	Hidden
	* XPMod:	45
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t2
	* MailsOnCompletion:	m_tanWin_2023_d01_log
	* Tier:	2
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Tags&Asteroid_Crud_T2up;Amount&1200;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_tanWin_2023_day02_t2
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	48
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t2
	* Tier:	2
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	1:0:0
	* GoalParameters:	Tags&RareEarth_T2up;Amount&50;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_tanWin_2023_day03_t2
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	51
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t2
	* Tier:	2
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	2:0:0
	* GoalParameters:	Tags&Salvage_T2up;Amount&5;ExcludedSources&MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_OpenContainer

### qe_tanWin_2023_day04_t2
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	54
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t2
	* Tier:	2
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	3:0:0
	* GoalParameters:	Id&CR;Amount&2500;ExcludedSources&BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

### qe_tanWin_2023_day05_t2
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	57
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t2
	* Tier:	2
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	4:0:0
	* GoalParameters:	Id&event_tanWin2023_DefendBase_t2

### qe_tanWin_2023_day06_t2
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	60
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t2
	* MailsOnCompletion:	m_tanWin_2023_d06_log
	* Tier:	2
	* Goals:	CompleteQuest,0
	* Type:	Event
	* StartOffset:	5:0:0
	* GoalParameters:	Amount&5;Tags&Faction_Tanoch_T2up

### qe_tanWin_2023_day07_t2
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	63
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t2
	* Tier:	2
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	6:0:0
	* GoalParameters:	Ids&ShipsDestroyedTanochT2_ShipsDestroyedTanochT3_ShipsDestroyedTanochT4;Amount&10

### qe_tanWin_2023_day08_t2
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	66
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t2
	* Tier:	2
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	7:0:0
	* GoalParameters:	Amount&1;Tags&Epic_T2up;Mode&Generated

### qe_tanWin_2023_day09_t2
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	69
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t2
	* Tier:	2
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	8:0:0
	* GoalParameters:	Category&Upgrade;Tags&External_Module_T1up;Amount&1

### qe_tanWin_2023_day10_t2
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	72
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t2
	* Tier:	2
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	9:0:0
	* GoalParameters:	Id&event_tanWin2023_AttackBase_t2

### qe_tanWin_2023_day11_t2
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	75
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t2
	* MailsOnCompletion:	m_tanWin_2023_d11_log
	* Tier:	2
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	10:0:0
	* GoalParameters:	Id&RepTanoch;Amount&135

### qe_tanWin_2023_day12_t2
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	78
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t2
	* Tier:	2
	* Goals:	Scan,0
	* Type:	Event
	* StartOffset:	11:0:0
	* GoalParameters:	Tags&InSystem_T2up;Amount&10;Analyzed&True

### qe_tanWin_2023_day13_t2
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	87
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t2
	* Tier:	2
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	12:0:0
	* GoalParameters:	Tags&Insignia_T2up;Amount&25;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_tanWin_2023_day14_t2
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	81
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t2
	* Tier:	2
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	13:0:0
	* GoalParameters:	Amount&1;Tags&Epic_T2up;Mode&Generated

### qe_tanWin_2023_day15_t2
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	84
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t2
	* Tier:	2
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	14:0:0
	* GoalParameters:	Ids&ShipsDestroyedTanochT2_ShipsDestroyedTanochT3_ShipsDestroyedTanochT4;Amount&10

### qe_tanWin_2023_day16_t2
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	90
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t2
	* Tier:	2
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	15:0:0
	* GoalParameters:	Id&event_tanWin2023_Relic_t2

### qe_tanWin_2023_day17_t2
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	93
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t2
	* MailsOnCompletion:	m_tanWin_2023_d17_log
	* Tier:	2
	* Goals:	CompleteQuest,0
	* Type:	Event
	* StartOffset:	16:0:0
	* GoalParameters:	Amount&5;Tags&Faction_Tanoch_T2up

### qe_tanWin_2023_day18_t2
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	96
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t2
	* Tier:	2
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	17:0:0
	* GoalParameters:	Id&CR;Amount&2500;ExcludedSources&BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

### qe_tanWin_2023_day19_t2
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	99
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t2
	* Tier:	2
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	18:0:0
	* GoalParameters:	Amount&1;Tags&Epic_T2up;Mode&Generated

### qe_tanWin_2023_day20_t2
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	102
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t2
	* Tier:	2
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	19:0:0
	* GoalParameters:	Ids&ShipsDestroyedTanochT2_ShipsDestroyedTanochT3_ShipsDestroyedTanochT4;Amount&10

### qe_tanWin_2023_day21_t2
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	105
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t2
	* Tier:	2
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	20:0:0
	* GoalParameters:	Id&RP;Amount&200;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_tanWin_2023_day22_t2
	* Rewards:	Z2:20	officer_tanochWinter_2023:1
	* ScheduleType:	Locked
	* XPMod:	108
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t2
	* MailsOnCompletion:	m_tanWin_2023_d22_log
	* Tier:	2
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	21:0:0
	* GoalParameters:	Id&event_tanWin2023_Academy_t2

## ql_event_tanochWinter_2023_t3

### qe_tanWin_2023_day01_t3
	* Rewards:	Z2:20
	* ScheduleType:	Hidden
	* XPMod:	135
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t3
	* MailsOnCompletion:	m_tanWin_2023_d01_log
	* Tier:	3
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Tags&Gas_T3up;Amount&1000;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_tanWin_2023_day02_t3
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	144
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t3
	* Tier:	3
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	1:0:0
	* GoalParameters:	Tags&RareEarth_T3up;Amount&50;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_tanWin_2023_day03_t3
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	153
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t3
	* Tier:	3
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	2:0:0
	* GoalParameters:	Tags&Salvage_T3up;Amount&5;ExcludedSources&MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_OpenContainer

### qe_tanWin_2023_day04_t3
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	162
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t3
	* Tier:	3
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	3:0:0
	* GoalParameters:	Id&CR;Amount&5000;ExcludedSources&BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

### qe_tanWin_2023_day05_t3
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	171
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t3
	* Tier:	3
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	4:0:0
	* GoalParameters:	Id&event_tanWin2023_DefendBase_t3

### qe_tanWin_2023_day06_t3
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	180
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t3
	* MailsOnCompletion:	m_tanWin_2023_d06_log
	* Tier:	3
	* Goals:	CompleteQuest,0
	* Type:	Event
	* StartOffset:	5:0:0
	* GoalParameters:	Amount&5;Tags&Faction_Tanoch_T3up

### qe_tanWin_2023_day07_t3
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	189
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t3
	* Tier:	3
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	6:0:0
	* GoalParameters:	Ids&ShipsDestroyedTanochT3_ShipsDestroyedTanochT4;Amount&10

### qe_tanWin_2023_day08_t3
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	198
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t3
	* Tier:	3
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	7:0:0
	* GoalParameters:	Amount&1;Tags&Epic_T3up;Mode&Generated

### qe_tanWin_2023_day09_t3
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	207
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t3
	* Tier:	3
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	8:0:0
	* GoalParameters:	Category&Upgrade;Tags&External_Module_T2up;Amount&1

### qe_tanWin_2023_day10_t3
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	216
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t3
	* Tier:	3
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	9:0:0
	* GoalParameters:	Id&event_tanWin2023_AttackBase_t3

### qe_tanWin_2023_day11_t3
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	225
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t3
	* MailsOnCompletion:	m_tanWin_2023_d11_log
	* Tier:	3
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	10:0:0
	* GoalParameters:	Id&RepTanoch;Amount&180

### qe_tanWin_2023_day12_t3
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	234
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t3
	* Tier:	3
	* Goals:	Scan,0
	* Type:	Event
	* StartOffset:	11:0:0
	* GoalParameters:	Tags&InSystem_T3up;Amount&10;Analyzed&True

### qe_tanWin_2023_day13_t3
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	261
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t3
	* Tier:	3
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	12:0:0
	* GoalParameters:	Tags&Insignia_T3up;Amount&25;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_tanWin_2023_day14_t3
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	243
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t3
	* Tier:	3
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	13:0:0
	* GoalParameters:	Amount&1;Tags&Epic_T3up;Mode&Generated

### qe_tanWin_2023_day15_t3
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	252
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t3
	* Tier:	3
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	14:0:0
	* GoalParameters:	Ids&ShipsDestroyedTanochT3_ShipsDestroyedTanochT4;Amount&10

### qe_tanWin_2023_day16_t3
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	270
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t3
	* Tier:	3
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	15:0:0
	* GoalParameters:	Id&event_tanWin2023_Relic_t3

### qe_tanWin_2023_day17_t3
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	279
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t3
	* MailsOnCompletion:	m_tanWin_2023_d17_log
	* Tier:	3
	* Goals:	CompleteQuest,0
	* Type:	Event
	* StartOffset:	16:0:0
	* GoalParameters:	Amount&5;Tags&Faction_Tanoch_T3up

### qe_tanWin_2023_day18_t3
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	288
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t3
	* Tier:	3
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	17:0:0
	* GoalParameters:	Id&CR;Amount&5000;ExcludedSources&BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

### qe_tanWin_2023_day19_t3
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	297
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t3
	* Tier:	3
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	18:0:0
	* GoalParameters:	Amount&1;Tags&Epic_T3up;Mode&Generated

### qe_tanWin_2023_day20_t3
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	306
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t3
	* Tier:	3
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	19:0:0
	* GoalParameters:	Ids&ShipsDestroyedTanochT3_ShipsDestroyedTanochT4;Amount&10

### qe_tanWin_2023_day21_t3
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	315
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t3
	* Tier:	3
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	20:0:0
	* GoalParameters:	Id&RP;Amount&200;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_tanWin_2023_day22_t3
	* Rewards:	Z2:20	officer_tanochWinter_2023:1
	* ScheduleType:	Locked
	* XPMod:	324
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t3
	* MailsOnCompletion:	m_tanWin_2023_d22_log
	* Tier:	3
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	21:0:0
	* GoalParameters:	Id&event_tanWin2023_Academy_t3

## ql_event_tanochWinter_2023_t4

### qe_tanWin_2023_day01_t4
	* Rewards:	Z2:20
	* ScheduleType:	Hidden
	* XPMod:	405
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t4
	* MailsOnCompletion:	m_tanWin_2023_d01_log
	* Tier:	4
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Tags&Gas_T4up;Amount&1200;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_tanWin_2023_day02_t4
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	432
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t4
	* Tier:	4
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	1:0:0
	* GoalParameters:	Tags&RareEarth_T4up;Amount&50;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_tanWin_2023_day03_t4
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	459
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t4
	* Tier:	4
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	2:0:0
	* GoalParameters:	Tags&Salvage_T4up;Amount&5;ExcludedSources&MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_OpenContainer

### qe_tanWin_2023_day04_t4
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	486
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t4
	* Tier:	4
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	3:0:0
	* GoalParameters:	Id&CR;Amount&10000;ExcludedSources&BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

### qe_tanWin_2023_day05_t4
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	513
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t4
	* Tier:	4
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	4:0:0
	* GoalParameters:	Id&event_tanWin2023_DefendBase_t4

### qe_tanWin_2023_day06_t4
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	540
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t4
	* MailsOnCompletion:	m_tanWin_2023_d06_log
	* Tier:	4
	* Goals:	CompleteQuest,0
	* Type:	Event
	* StartOffset:	5:0:0
	* GoalParameters:	Amount&5;Tags&Faction_Tanoch_T4up

### qe_tanWin_2023_day07_t4
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	567
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t4
	* Tier:	4
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	6:0:0
	* GoalParameters:	Ids&ShipsDestroyedTanochT4;Amount&10

### qe_tanWin_2023_day08_t4
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	594
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t4
	* Tier:	4
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	7:0:0
	* GoalParameters:	Amount&1;Tags&Epic_T4up;Mode&Generated

### qe_tanWin_2023_day09_t4
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	621
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t4
	* Tier:	4
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	8:0:0
	* GoalParameters:	Category&Upgrade;Tags&External_Module_T3up;Amount&1

### qe_tanWin_2023_day10_t4
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	648
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t4
	* Tier:	4
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	9:0:0
	* GoalParameters:	Id&event_tanWin2023_AttackBase_t4

### qe_tanWin_2023_day11_t4
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	675
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t4
	* MailsOnCompletion:	m_tanWin_2023_d11_log
	* Tier:	4
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	10:0:0
	* GoalParameters:	Id&RepTanoch;Amount&225

### qe_tanWin_2023_day12_t4
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	702
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t4
	* Tier:	4
	* Goals:	Scan,0
	* Type:	Event
	* StartOffset:	11:0:0
	* GoalParameters:	Tags&InSystem_T4up;Amount&10;Analyzed&True

### qe_tanWin_2023_day13_t4
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	783
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t4
	* Tier:	4
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	12:0:0
	* GoalParameters:	Tags&Insignia_T4up;Amount&25;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_tanWin_2023_day14_t4
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	729
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t4
	* Tier:	4
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	13:0:0
	* GoalParameters:	Amount&1;Tags&Epic_T4up;Mode&Generated

### qe_tanWin_2023_day15_t4
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	756
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t4
	* Tier:	4
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	14:0:0
	* GoalParameters:	Ids&ShipsDestroyedTanochT4;Amount&10

### qe_tanWin_2023_day16_t4
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	810
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t4
	* Tier:	4
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	15:0:0
	* GoalParameters:	Id&event_tanWin2023_Relic_t4

### qe_tanWin_2023_day17_t4
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	837
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t4
	* MailsOnCompletion:	m_tanWin_2023_d17_log
	* Tier:	4
	* Goals:	CompleteQuest,0
	* Type:	Event
	* StartOffset:	16:0:0
	* GoalParameters:	Amount&5;Tags&Faction_Tanoch_T4up

### qe_tanWin_2023_day18_t4
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	864
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t4
	* Tier:	4
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	17:0:0
	* GoalParameters:	Id&CR;Amount&10000;ExcludedSources&BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

### qe_tanWin_2023_day19_t4
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	891
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t4
	* Tier:	4
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	18:0:0
	* GoalParameters:	Amount&1;Tags&Epic_T4up;Mode&Generated

### qe_tanWin_2023_day20_t4
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	918
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t4
	* Tier:	4
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	19:0:0
	* GoalParameters:	Ids&ShipsDestroyedTanochT4;Amount&10

### qe_tanWin_2023_day21_t4
	* Rewards:	Z2:20
	* ScheduleType:	Locked
	* XPMod:	945
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t4
	* Tier:	4
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	20:0:0
	* GoalParameters:	Id&RP;Amount&200;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_tanWin_2023_day22_t4
	* Rewards:	Z2:20	officer_tanochWinter_2023:1
	* ScheduleType:	Locked
	* XPMod:	972
	* EndOffset:	0:0:0
	* EventId:	event_tanochWinter_2023_t4
	* MailsOnCompletion:	m_tanWin_2023_d22_log
	* Tier:	4
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	21:0:0
	* GoalParameters:	Id&event_tanWin2023_Academy_t4

## ql_event_YaotSpring_2024_t1

### qe_yaoSpr_2024_day01_t1
	* Rewards:	Z1:20
	* ScheduleType:	Hidden
	* XPMod:	15
	* EndOffset:	0:0:0
	* EventId:	event_yaotSpring_2024_t1
	* Tier:	1
	* Goals:	CompleteQuest,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Amount&5;Tags&T1up

### qe_yaoSpr_2024_day02_t1
	* Rewards:	Z1:20
	* ScheduleType:	Locked
	* XPMod:	16
	* EndOffset:	0:0:0
	* EventId:	event_yaotSpring_2024_t1
	* Tier:	1
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	1:0:0
	* GoalParameters:	Id&CR;Amount&1250;ExcludedSources&BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

### qe_yaoSpr_2024_day03_t1
	* Rewards:	Z1:20
	* ScheduleType:	Locked
	* XPMod:	17
	* EndOffset:	0:0:0
	* EventId:	event_yaotSpring_2024_t1
	* Tier:	1
	* Goals:	Scan,0
	* Type:	Event
	* StartOffset:	2:0:0
	* GoalParameters:	Tags&InSystem_T1up;Amount&5;Analyzed&True

### qe_yaoSpr_2024_day04_t1
	* Rewards:	Z1:20
	* ScheduleType:	Locked
	* XPMod:	18
	* EndOffset:	0:0:0
	* EventId:	event_yaotSpring_2024_t1
	* Tier:	1
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	3:0:0
	* GoalParameters:	Tags&Salvage_T1up;Amount&5;ExcludedSources&MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_OpenContainer

### qe_yaoSpr_2024_day05_t1
	* Rewards:	Z1:20
	* ScheduleType:	Locked
	* XPMod:	19
	* EndOffset:	0:0:0
	* EventId:	event_yaotSpring_2024_t1
	* Tier:	1
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	4:0:0
	* GoalParameters:	Id&LP;Amount&10;ExcludedSources&BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem

### qe_yaoSpr_2024_day06_t1
	* Rewards:	Z1:20
	* ScheduleType:	Locked
	* XPMod:	20
	* EndOffset:	0:0:0
	* EventId:	event_yaotSpring_2024_t1
	* Tier:	1
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	5:0:0
	* GoalParameters:	Category&Crafting;Tags&T1up;Amount&1

### qe_yaoSpr_2024_day07_t1
	* Rewards:	Z1:20
	* ScheduleType:	Locked
	* XPMod:	21
	* EndOffset:	0:0:0
	* EventId:	event_yaotSpring_2024_t1
	* Tier:	1
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	6:0:0
	* GoalParameters:	Amount&1;Tags&Rare_T1up;Mode&Generated

### qe_yaoSpr_2024_day08_t1
	* Rewards:	Z1:20
	* ScheduleType:	Locked
	* XPMod:	22
	* EndOffset:	0:0:0
	* EventId:	event_yaotSpring_2024_t1
	* Tier:	1
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	7:0:0
	* GoalParameters:	Tags&Insignia_T1up;Amount&50;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_yaoSpr_2024_day09_t1
	* Rewards:	Z1:20
	* ScheduleType:	Locked
	* XPMod:	23
	* EndOffset:	0:0:0
	* EventId:	event_yaotSpring_2024_t1
	* Tier:	1
	* Goals:	CompleteQuest,0
	* Type:	Event
	* StartOffset:	8:0:0
	* GoalParameters:	Amount&5;Tags&T1up

### qe_yaoSpr_2024_day10_t1
	* Rewards:	Z1:20
	* ScheduleType:	Locked
	* XPMod:	24
	* EndOffset:	0:0:0
	* EventId:	event_yaotSpring_2024_t1
	* Tier:	1
	* Goals:	Pay,0
	* Type:	Event
	* StartOffset:	9:0:0
	* GoalParameters:	Id&questItem_progenitorRelic_t1;Amount&1

### qe_yaoSpr_2024_day11_t1
	* Rewards:	Z1:20
	* ScheduleType:	Locked
	* XPMod:	25
	* EndOffset:	0:0:0
	* EventId:	event_yaotSpring_2024_t1
	* Tier:	1
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	10:0:0
	* GoalParameters:	Amount&1;Tags&Rare_T1up;Mode&Generated

### qe_yaoSpr_2024_day12_t1
	* Rewards:	Z1:20
	* ScheduleType:	Locked
	* XPMod:	26
	* EndOffset:	0:0:0
	* EventId:	event_yaotSpring_2024_t1
	* Tier:	1
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	11:0:0
	* GoalParameters:	Tags&Asteroid_Crud_T1up;Amount&1000;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_yaoSpr_2024_day13_t1
	* Rewards:	Z1:20
	* ScheduleType:	Locked
	* XPMod:	29
	* EndOffset:	0:0:0
	* EventId:	event_yaotSpring_2024_t1
	* Tier:	1
	* Goals:	UpgradeOfficer,0
	* Type:	Event
	* StartOffset:	12:0:0
	* GoalParameters:	Amount&1

### qe_yaoSpr_2024_day14_t1
	* Rewards:	Z1:20	officer_yaotSpring_2024:1
	* ScheduleType:	Locked
	* XPMod:	27
	* EndOffset:	0:0:0
	* EventId:	event_yaotSpring_2024_t1
	* Tier:	1
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	13:0:0
	* GoalParameters:	Id&event_yaoSpr2024_Conjunction_t1

## ql_event_YaotSpring_2024_t2

### qe_yaoSpr_2024_day01_t2
	* Rewards:	Z1:20
	* ScheduleType:	Hidden
	* XPMod:	45
	* EndOffset:	0:0:0
	* EventId:	event_yaotSpring_2024_t2
	* Tier:	2
	* Goals:	CompleteQuest,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Amount&5;Tags&Faction_Tr1_T2up

### qe_yaoSpr_2024_day02_t2
	* Rewards:	Z1:20
	* ScheduleType:	Locked
	* XPMod:	48
	* EndOffset:	0:0:0
	* EventId:	event_yaotSpring_2024_t2
	* Tier:	2
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	1:0:0
	* GoalParameters:	Id&CR;Amount&2500;ExcludedSources&BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

### qe_yaoSpr_2024_day03_t2
	* Rewards:	Z1:20
	* ScheduleType:	Locked
	* XPMod:	51
	* EndOffset:	0:0:0
	* EventId:	event_yaotSpring_2024_t2
	* Tier:	2
	* Goals:	Scan,0
	* Type:	Event
	* StartOffset:	2:0:0
	* GoalParameters:	Tags&InSystem_T2up;Amount&5;Analyzed&True

### qe_yaoSpr_2024_day04_t2
	* Rewards:	Z1:20
	* ScheduleType:	Locked
	* XPMod:	54
	* EndOffset:	0:0:0
	* EventId:	event_yaotSpring_2024_t2
	* Tier:	2
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	3:0:0
	* GoalParameters:	Tags&Salvage_T2up;Amount&5;ExcludedSources&MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_OpenContainer

### qe_yaoSpr_2024_day05_t2
	* Rewards:	Z1:20
	* ScheduleType:	Locked
	* XPMod:	57
	* EndOffset:	0:0:0
	* EventId:	event_yaotSpring_2024_t2
	* Tier:	2
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	4:0:0
	* GoalParameters:	Id&LP;Amount&10;ExcludedSources&BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem

### qe_yaoSpr_2024_day06_t2
	* Rewards:	Z1:20
	* ScheduleType:	Locked
	* XPMod:	60
	* EndOffset:	0:0:0
	* EventId:	event_yaotSpring_2024_t2
	* Tier:	2
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	5:0:0
	* GoalParameters:	Category&Crafting;Tags&Part_T2up;Amount&100

### qe_yaoSpr_2024_day07_t2
	* Rewards:	Z1:20
	* ScheduleType:	Locked
	* XPMod:	63
	* EndOffset:	0:0:0
	* EventId:	event_yaotSpring_2024_t2
	* Tier:	2
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	6:0:0
	* GoalParameters:	Amount&1;Tags&Epic_T2up;Mode&Generated

### qe_yaoSpr_2024_day08_t2
	* Rewards:	Z1:20
	* ScheduleType:	Locked
	* XPMod:	66
	* EndOffset:	0:0:0
	* EventId:	event_yaotSpring_2024_t2
	* Tier:	2
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	7:0:0
	* GoalParameters:	Tags&Insignia_T2up;Amount&50;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_yaoSpr_2024_day09_t2
	* Rewards:	Z1:20
	* ScheduleType:	Locked
	* XPMod:	69
	* EndOffset:	0:0:0
	* EventId:	event_yaotSpring_2024_t2
	* Tier:	2
	* Goals:	CompleteQuest,0
	* Type:	Event
	* StartOffset:	8:0:0
	* GoalParameters:	Amount&5;Tags&T2up

### qe_yaoSpr_2024_day10_t2
	* Rewards:	Z1:20
	* ScheduleType:	Locked
	* XPMod:	72
	* EndOffset:	0:0:0
	* EventId:	event_yaotSpring_2024_t2
	* Tier:	2
	* Goals:	Pay,0
	* Type:	Event
	* StartOffset:	9:0:0
	* GoalParameters:	Id&questItem_progenitorRelic_t2;Amount&1

### qe_yaoSpr_2024_day11_t2
	* Rewards:	Z1:20
	* ScheduleType:	Locked
	* XPMod:	75
	* EndOffset:	0:0:0
	* EventId:	event_yaotSpring_2024_t2
	* Tier:	2
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	10:0:0
	* GoalParameters:	Amount&1;Tags&Epic_T2up;Mode&Generated

### qe_yaoSpr_2024_day12_t2
	* Rewards:	Z1:20
	* ScheduleType:	Locked
	* XPMod:	78
	* EndOffset:	0:0:0
	* EventId:	event_yaotSpring_2024_t2
	* Tier:	2
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	11:0:0
	* GoalParameters:	Tags&Asteroid_Crud_T2up;Amount&1200;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_yaoSpr_2024_day13_t2
	* Rewards:	Z1:20
	* ScheduleType:	Locked
	* XPMod:	87
	* EndOffset:	0:0:0
	* EventId:	event_yaotSpring_2024_t2
	* Tier:	2
	* Goals:	UpgradeOfficer,0
	* Type:	Event
	* StartOffset:	12:0:0
	* GoalParameters:	Amount&2

### qe_yaoSpr_2024_day14_t2
	* Rewards:	Z1:20	officer_yaotSpring_2024:1
	* ScheduleType:	Locked
	* XPMod:	81
	* EndOffset:	0:0:0
	* EventId:	event_yaotSpring_2024_t2
	* Tier:	2
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	13:0:0
	* GoalParameters:	Id&event_yaoSpr2024_Conjunction_t2

## ql_event_YaotSpring_2024_t3

### qe_yaoSpr_2024_day01_t3
	* Rewards:	Z1:20
	* ScheduleType:	Hidden
	* XPMod:	135
	* EndOffset:	0:0:0
	* EventId:	event_yaotSpring_2024_t3
	* Tier:	3
	* Goals:	CompleteQuest,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Amount&5;Tags&Faction_Tr1_T3up

### qe_yaoSpr_2024_day02_t3
	* Rewards:	Z1:20
	* ScheduleType:	Locked
	* XPMod:	144
	* EndOffset:	0:0:0
	* EventId:	event_yaotSpring_2024_t3
	* Tier:	3
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	1:0:0
	* GoalParameters:	Id&CR;Amount&5000;ExcludedSources&BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

### qe_yaoSpr_2024_day03_t3
	* Rewards:	Z1:20
	* ScheduleType:	Locked
	* XPMod:	153
	* EndOffset:	0:0:0
	* EventId:	event_yaotSpring_2024_t3
	* Tier:	3
	* Goals:	Scan,0
	* Type:	Event
	* StartOffset:	2:0:0
	* GoalParameters:	Tags&InSystem_T3up;Amount&5;Analyzed&True

### qe_yaoSpr_2024_day04_t3
	* Rewards:	Z1:20
	* ScheduleType:	Locked
	* XPMod:	162
	* EndOffset:	0:0:0
	* EventId:	event_yaotSpring_2024_t3
	* Tier:	3
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	3:0:0
	* GoalParameters:	Tags&Salvage_T3up;Amount&5;ExcludedSources&MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_OpenContainer

### qe_yaoSpr_2024_day05_t3
	* Rewards:	Z1:20
	* ScheduleType:	Locked
	* XPMod:	171
	* EndOffset:	0:0:0
	* EventId:	event_yaotSpring_2024_t3
	* Tier:	3
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	4:0:0
	* GoalParameters:	Id&LP;Amount&10;ExcludedSources&BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem

### qe_yaoSpr_2024_day06_t3
	* Rewards:	Z1:20
	* ScheduleType:	Locked
	* XPMod:	180
	* EndOffset:	0:0:0
	* EventId:	event_yaotSpring_2024_t3
	* Tier:	3
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	5:0:0
	* GoalParameters:	Category&Crafting;Tags&Part_T3up;Amount&100

### qe_yaoSpr_2024_day07_t3
	* Rewards:	Z1:20
	* ScheduleType:	Locked
	* XPMod:	189
	* EndOffset:	0:0:0
	* EventId:	event_yaotSpring_2024_t3
	* Tier:	3
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	6:0:0
	* GoalParameters:	Amount&1;Tags&Epic_T3up;Mode&Generated

### qe_yaoSpr_2024_day08_t3
	* Rewards:	Z1:20
	* ScheduleType:	Locked
	* XPMod:	198
	* EndOffset:	0:0:0
	* EventId:	event_yaotSpring_2024_t3
	* Tier:	3
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	7:0:0
	* GoalParameters:	Tags&Insignia_T3up;Amount&50;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_yaoSpr_2024_day09_t3
	* Rewards:	Z1:20
	* ScheduleType:	Locked
	* XPMod:	207
	* EndOffset:	0:0:0
	* EventId:	event_yaotSpring_2024_t3
	* Tier:	3
	* Goals:	CompleteQuest,0
	* Type:	Event
	* StartOffset:	8:0:0
	* GoalParameters:	Amount&5;Tags&Faction_Yaot_T3up

### qe_yaoSpr_2024_day10_t3
	* Rewards:	Z1:20
	* ScheduleType:	Locked
	* XPMod:	216
	* EndOffset:	0:0:0
	* EventId:	event_yaotSpring_2024_t3
	* Tier:	3
	* Goals:	Pay,0
	* Type:	Event
	* StartOffset:	9:0:0
	* GoalParameters:	Id&questItem_progenitorRelic_t3;Amount&1

### qe_yaoSpr_2024_day11_t3
	* Rewards:	Z1:20
	* ScheduleType:	Locked
	* XPMod:	225
	* EndOffset:	0:0:0
	* EventId:	event_yaotSpring_2024_t3
	* Tier:	3
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	10:0:0
	* GoalParameters:	Amount&1;Tags&Epic_T3up;Mode&Generated

### qe_yaoSpr_2024_day12_t3
	* Rewards:	Z1:20
	* ScheduleType:	Locked
	* XPMod:	234
	* EndOffset:	0:0:0
	* EventId:	event_yaotSpring_2024_t3
	* Tier:	3
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	11:0:0
	* GoalParameters:	Tags&Asteroid_Crud_T3up;Amount&1400;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_yaoSpr_2024_day13_t3
	* Rewards:	Z1:20
	* ScheduleType:	Locked
	* XPMod:	261
	* EndOffset:	0:0:0
	* EventId:	event_yaotSpring_2024_t3
	* Tier:	3
	* Goals:	UpgradeOfficer,0
	* Type:	Event
	* StartOffset:	12:0:0
	* GoalParameters:	Amount&3

### qe_yaoSpr_2024_day14_t3
	* Rewards:	Z1:20	officer_yaotSpring_2024:1
	* ScheduleType:	Locked
	* XPMod:	243
	* EndOffset:	0:0:0
	* EventId:	event_yaotSpring_2024_t3
	* Tier:	3
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	13:0:0
	* GoalParameters:	Id&event_yaoSpr2024_Conjunction_t3

## ql_event_YaotSpring_2024_t4

### qe_yaoSpr_2024_day01_t4
	* Rewards:	Z1:20
	* ScheduleType:	Hidden
	* XPMod:	405
	* EndOffset:	0:0:0
	* EventId:	event_yaotSpring_2024_t4
	* Tier:	4
	* Goals:	CompleteQuest,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Amount&5;Tags&Faction_Tr1_T4up

### qe_yaoSpr_2024_day02_t4
	* Rewards:	Z1:20
	* ScheduleType:	Locked
	* XPMod:	432
	* EndOffset:	0:0:0
	* EventId:	event_yaotSpring_2024_t4
	* Tier:	4
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	1:0:0
	* GoalParameters:	Id&CR;Amount&10000;ExcludedSources&BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

### qe_yaoSpr_2024_day03_t4
	* Rewards:	Z1:20
	* ScheduleType:	Locked
	* XPMod:	459
	* EndOffset:	0:0:0
	* EventId:	event_yaotSpring_2024_t4
	* Tier:	4
	* Goals:	Scan,0
	* Type:	Event
	* StartOffset:	2:0:0
	* GoalParameters:	Tags&InSystem_T4up;Amount&5;Analyzed&True

### qe_yaoSpr_2024_day04_t4
	* Rewards:	Z1:20
	* ScheduleType:	Locked
	* XPMod:	486
	* EndOffset:	0:0:0
	* EventId:	event_yaotSpring_2024_t4
	* Tier:	4
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	3:0:0
	* GoalParameters:	Tags&Salvage_T4up;Amount&5;ExcludedSources&MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_OpenContainer

### qe_yaoSpr_2024_day05_t4
	* Rewards:	Z1:20
	* ScheduleType:	Locked
	* XPMod:	513
	* EndOffset:	0:0:0
	* EventId:	event_yaotSpring_2024_t4
	* Tier:	4
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	4:0:0
	* GoalParameters:	Id&LP;Amount&10;ExcludedSources&BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem

### qe_yaoSpr_2024_day06_t4
	* Rewards:	Z1:20
	* ScheduleType:	Locked
	* XPMod:	540
	* EndOffset:	0:0:0
	* EventId:	event_yaotSpring_2024_t4
	* Tier:	4
	* Goals:	Craft,0
	* Type:	Event
	* StartOffset:	5:0:0
	* GoalParameters:	Category&Crafting;Tags&Part_T4up;Amount&100

### qe_yaoSpr_2024_day07_t4
	* Rewards:	Z1:20
	* ScheduleType:	Locked
	* XPMod:	567
	* EndOffset:	0:0:0
	* EventId:	event_yaotSpring_2024_t4
	* Tier:	4
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	6:0:0
	* GoalParameters:	Amount&1;Tags&Epic_T4up;Mode&Generated

### qe_yaoSpr_2024_day08_t4
	* Rewards:	Z1:20
	* ScheduleType:	Locked
	* XPMod:	594
	* EndOffset:	0:0:0
	* EventId:	event_yaotSpring_2024_t4
	* Tier:	4
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	7:0:0
	* GoalParameters:	Tags&Insignia_T4up;Amount&50;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_yaoSpr_2024_day09_t4
	* Rewards:	Z1:20
	* ScheduleType:	Locked
	* XPMod:	621
	* EndOffset:	0:0:0
	* EventId:	event_yaotSpring_2024_t4
	* Tier:	4
	* Goals:	CompleteQuest,0
	* Type:	Event
	* StartOffset:	8:0:0
	* GoalParameters:	Amount&5;Tags&Faction_Yaot_T4up

### qe_yaoSpr_2024_day10_t4
	* Rewards:	Z1:20
	* ScheduleType:	Locked
	* XPMod:	648
	* EndOffset:	0:0:0
	* EventId:	event_yaotSpring_2024_t4
	* Tier:	4
	* Goals:	Pay,0
	* Type:	Event
	* StartOffset:	9:0:0
	* GoalParameters:	Id&questItem_progenitorRelic_t4;Amount&1

### qe_yaoSpr_2024_day11_t4
	* Rewards:	Z1:20
	* ScheduleType:	Locked
	* XPMod:	675
	* EndOffset:	0:0:0
	* EventId:	event_yaotSpring_2024_t4
	* Tier:	4
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	10:0:0
	* GoalParameters:	Amount&1;Tags&Epic_T4up;Mode&Generated

### qe_yaoSpr_2024_day12_t4
	* Rewards:	Z1:20
	* ScheduleType:	Locked
	* XPMod:	702
	* EndOffset:	0:0:0
	* EventId:	event_yaotSpring_2024_t4
	* Tier:	4
	* Goals:	GainItem,0
	* Type:	Event
	* StartOffset:	11:0:0
	* GoalParameters:	Tags&Asteroid_Crud_T4up;Amount&1600;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_yaoSpr_2024_day13_t4
	* Rewards:	Z1:20
	* ScheduleType:	Locked
	* XPMod:	783
	* EndOffset:	0:0:0
	* EventId:	event_yaotSpring_2024_t4
	* Tier:	4
	* Goals:	UpgradeOfficer,0
	* Type:	Event
	* StartOffset:	12:0:0
	* GoalParameters:	Amount&5

### qe_yaoSpr_2024_day14_t4
	* Rewards:	Z1:20	officer_yaotSpring_2024:1
	* ScheduleType:	Locked
	* XPMod:	729
	* EndOffset:	0:0:0
	* EventId:	event_yaotSpring_2024_t4
	* Tier:	4
	* Goals:	CompleteMission,0
	* Type:	Event
	* StartOffset:	13:0:0
	* GoalParameters:	Id&event_yaoSpr2024_Conjunction_t4

## ql_test

### qt_001
	* Rewards:	rw_co_cryo:1
	* ScheduleType:	Hidden
	* XPMod:	1
	* EndOffset:	0:0:0
	* MailsOnCompletion:	m_qt_001
	* Goals:	Pay,0	Pay,0
	* Type:	Side
	* StartOffset:	0:0:0
	* GoalParameters:	Id&1A;Amount&500	Id&1B;Amount&250

## ql_test2

### qt_002
	* Rewards:	rw_co_cryo:1
	* XPMod:	1
	* Goals:	CompleteMission,0
	* Type:	Side
	* GoalParameters:	Ids&story_A02_WiracodaGate|story_A03_GulfTaln

## ql_test3

### qt_003
	* Rewards:	AC:100	AS:200
	* XPMod:	1
	* Goals:	GainItem,0
	* Type:	Side
	* GoalParameters:	Id&CR;Amount&100;ExcludedSources&Shop_Reward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

## ql_test4

### qt_004
	* Rewards:	insig_r1:6
	* XPMod:	1
	* Goals:	CompleteMission,0
	* Type:	Side
	* GoalParameters:	Amount&3;Mode&Faction;Tags&Tanoch_T3up

## ql_testQuestDialog

### qm_testQuestDialog
	* Rewards:	CR:500
	* XPMod:	5
	* Tier:	0
	* Goals:	Goto,0	Goto,1	Goto,2	Goto,2
	* Type:	Main
	* GoalParameters:	Target&[-1785, -690]	Target&[-1844, -690]	Target&[-1785, -690]	Target&[-1844, -690]

## ql_testDismissOfficers

### qt_testDismissOfficers
	* Rewards:	CR:500
	* XPMod:	1
	* Tier:	1
	* Goals:	GainItem,0
	* Type:	Side
	* GoalParameters:	Tags&Insignia;Amount&1;ExcludedSources&OpenContainer_QuestReward_MissionReward_ClaimMail_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_BuyItem_SellItem

## ql_test_strike_13

### qt_test_strike_13
	* Rewards:	CR:12345
	* XPMod:	1
	* Tier:	1
	* Goals:	CompleteQuest,0
	* Type:	Main
	* GoalParameters:	Ids&qr_013

## ql_test_strike_16

### qt_test_strike_16
	* Rewards:	CR:12345
	* XPMod:	1
	* Tier:	1
	* Goals:	CompleteQuest,0
	* Type:	Main
	* GoalParameters:	Ids&qr_016

## ql_test_strike_14

### qt_test_strike_14
	* Rewards:	CR:12345
	* XPMod:	1
	* Tier:	1
	* Goals:	CompleteQuest,0
	* Type:	Main
	* GoalParameters:	Ids&qr_014

## ql_test_strike_17

### qt_test_strike_17
	* Rewards:	CR:12345
	* XPMod:	1
	* Tier:	1
	* Goals:	CompleteQuest,0
	* Type:	Main
	* GoalParameters:	Ids&qr_017

## ql_test_strike_21

### qt_test_strike_21
	* Rewards:	CR:12345
	* XPMod:	1
	* Tier:	1
	* Goals:	CompleteQuest,0
	* Type:	Main
	* GoalParameters:	Ids&qr_021

## ql_test_strike_15

### qt_test_strike_15
	* Rewards:	CR:12345
	* XPMod:	1
	* Tier:	1
	* Goals:	CompleteQuest,0
	* Type:	Main
	* GoalParameters:	Ids&qr_015

## ql_test_strike_18

### qt_test_strike_18
	* Rewards:	CR:12345
	* XPMod:	1
	* Tier:	1
	* Goals:	CompleteQuest,0
	* Type:	Main
	* GoalParameters:	Ids&qr_018

## ql_test_strike_22

### qt_test_strike_22
	* Rewards:	CR:12345
	* XPMod:	1
	* Tier:	1
	* Goals:	CompleteQuest,0
	* Type:	Main
	* GoalParameters:	Ids&qr_022

## ql_test_strike_19

### qt_test_strike_19
	* Rewards:	CR:12345
	* XPMod:	1
	* Tier:	1
	* Goals:	CompleteQuest,0
	* Type:	Main
	* GoalParameters:	Ids&qr_019

## ql_test_strike_20

### qt_test_strike_20
	* Rewards:	CR:12345
	* XPMod:	1
	* Tier:	1
	* Goals:	CompleteQuest,0
	* Type:	Main
	* GoalParameters:	Ids&qr_020

## ql_a_001

### qa_001
	* Goals:	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&Mined1A;Total&3000

### qa_002
	* Goals:	Statistic,0
	* Type:	Achievement
	* GoalParameters:	Id&Upgrade;Amount&5

## ql_test_ggf_story

### qs_s2_01_sijinLighthouse
	* Rewards:	rw_rbox_qr_large:1
	* XPMod:	0
	* Tier:	3
	* Goals:	CompleteMission,0
	* Type:	Side
	* GoalParameters:	Id&story_D01_SijinLighthouse
	* FollowUpLines:	ql_raid_019

### qs_s2_01_iliyinLighthouse
	* Rewards:	rw_rbox_qr_large:1
	* XPMod:	0
	* Tier:	4
	* Goals:	CompleteMission,0
	* Type:	Side
	* GoalParameters:	Id&story_D02_IliyinLighthouse

### qs_s2_01_bTemple
	* Rewards:	rw_rbox_qr_large:1
	* XPMod:	0
	* Tier:	4
	* Goals:	CompleteMission,0
	* Type:	Side
	* GoalParameters:	Id&story_D03_BrightTemple

### qs_s2_01_hataldan
	* Rewards:	rw_rbox_qr_large:1
	* XPMod:	15
	* Tier:	4
	* Goals:	CompleteMission,0
	* Type:	Side
	* GoalParameters:	Id&story_D04_Hataldan
	* FollowUpLines:	ql_raid_020

## ql_compensation_lvlup

### q_compensation_lvl_10
	* Rewards:	LP:200
	* ScheduleType:	Hidden
	* XPMod:	1
	* EndOffset:	0:0:0
	* EventId:	event_levelUpCompensationQuests
	* Tier:	0
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Id&PlayerXP;Total&12600

### q_compensation_lvl_20
	* Rewards:	LP:300
	* ScheduleType:	Hidden
	* XPMod:	2
	* EndOffset:	0:0:0
	* EventId:	event_levelUpCompensationQuests
	* Tier:	1
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Id&PlayerXP;Total&36100

### q_compensation_lvl_35
	* Rewards:	LP:400
	* ScheduleType:	Hidden
	* XPMod:	3
	* EndOffset:	0:0:0
	* EventId:	event_levelUpCompensationQuests
	* Tier:	2
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Id&PlayerXP;Total&90100

### q_compensation_lvl_50
	* Rewards:	LP:500
	* ScheduleType:	Hidden
	* XPMod:	4
	* EndOffset:	0:0:0
	* EventId:	event_levelUpCompensationQuests
	* Tier:	3
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Id&PlayerXP;Total&166600

### q_compensation_lvl_75
	* Rewards:	LP:500	rw_crystals_1000_t4:1
	* ScheduleType:	Hidden
	* XPMod:	5
	* EndOffset:	0:0:0
	* EventId:	event_levelUpCompensationQuests
	* Tier:	4
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Id&PlayerXP;Total&344100

### q_compensation_lvl_100
	* Rewards:	LP:500	rw_crystals_1000_t4:1
	* ScheduleType:	Hidden
	* XPMod:	6
	* EndOffset:	0:0:0
	* EventId:	event_levelUpCompensationQuests
	* Tier:	4
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Id&PlayerXP;Total&584100

### q_compensation_lvl_150
	* Rewards:	LP:500	rw_crystals_1000_t4:1
	* ScheduleType:	Hidden
	* XPMod:	7
	* EndOffset:	0:0:0
	* EventId:	event_levelUpCompensationQuests
	* Tier:	4
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Id&PlayerXP;Total&1251600

### q_compensation_lvl_200
	* Rewards:	LP:500	rw_crystals_1000_t4:1
	* ScheduleType:	Hidden
	* XPMod:	8
	* EndOffset:	0:0:0
	* EventId:	event_levelUpCompensationQuests
	* Tier:	4
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Id&PlayerXP;Total&2169100

### q_compensation_lvl_300
	* Rewards:	LP:500	rw_crystals_1000_t4:1
	* ScheduleType:	Hidden
	* XPMod:	9
	* EndOffset:	0:0:0
	* EventId:	event_levelUpCompensationQuests
	* Tier:	4
	* Goals:	Statistic,0
	* Type:	Event
	* StartOffset:	0:0:0
	* GoalParameters:	Id&PlayerXP;Total&4754100

## q_test_yao_spring

### q_test_yaoSpr_2024_day04_t4
	* XPMod:	486
	* Tier:	4
	* Goals:	GainItem,0
	* Type:	Side
	* GoalParameters:	Tags&Salvage_T4up;Amount&5;ExcludedSources&MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_OpenContainer