# HWM QUESTLINES WITH QUESTS


## QL_MAIN_T0_TUTORIAL
### qm_t0_tutMissions
* Type:	Main
* CinematicIds:	20:10:25
* FollowUps: ql_main_t0_station
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Ids:
				* story_A01_DuzumiGate
				* story_A01_DuzumiGateTut
	* 1:
		* GoalType: CompleteMission
			* Id: story_A02_WiracodaGate
	* 2:
		* GoalType: CompleteMission
			* Id: story_A03_GulfTaln

## QL_MAIN_T0_STATION
### qm_t0_introStation
* Type:	Main
* Goals:
	* 0:
		* GoalType: Goto
			* Target: [-1822, -636]
			* TargetMode: Station

### qm_t0_introMarket
* Type:	Main
* FollowUps: ql_main_t0_strikeCraft
* Goals:
	* 0:
		* GoalType: Buy
			* Id: pack_market_freeHC_insta

## QL_MAIN_T0_STRIKECRAFT
### qm_t0_introFabricator
* Type:	Main
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: Interceptor
			* Amount: 1

### qm_t0_introEquipStrikecraft
* Type:	Main
* FollowUps: ql_main_t0_v2_signals
* Goals:
	* 0:
		* GoalType: Equip
			* Type: Squad

## QL_MAIN_T0_V2_SIGNALS
### qm_t0_v2_introScanning
* Type:	Main
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_Generated
			* Amount: 1
	* 1:
		* GoalType: Scan
			* Tags: InSystem_Generated
			* Amount: 1
			* Analyzed: True

### qm_t0_v2_introSignals
* Type:	Main
* FollowUps: ql_main_t0_mining
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Mode: Generated
			* Amount: 1
	* 1:
		* GoalType: Goto
			* Target: [-1822, -636]
			* TargetMode: Station

## QL_MAIN_T0_MINING
### qm_t0_introScanBelts
* Type:	Main
* Goals:
	* 0:
		* GoalType: Goto
			* Target: [-1747, -653]
	* 1:
		* GoalType: Statistic
			* Id: ScannedBelt
			* Total: 1

### qm_t0_introMining
* Type:	Main
* FollowUps: ql_main_t0_support
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: Mined0A
			* Amount: 50

## QL_MAIN_T0_SUPPORT
### qm_t0_support
* Type:	Main
* FollowUps: ql_main_t0_officer
* Goals:
	* 0:
		* GoalType: Pay
			* Id: 0A
			* Amount: 25
			* SysId: [-1822, -636]
			* Mode: Station

## QL_MAIN_T0_OFFICER
### qm_t0_introBridge
* Type:	Main
* FollowUps: ql_main_t0_escorts
* Goals:
	* 0:
		* GoalType: Equip
			* Type: Officer
			* Location: Bridge

## QL_MAIN_T0_ESCORTS
### qm_t0_introShipyard
* Type:	Main
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: AssaultFrigate
			* Amount: 1

### qm_t0_introEquipEscorts
* Type:	Main
* FollowUps: ql_main_t0_sideProg
* Goals:
	* 0:
		* GoalType: Equip
			* Type: Escort

## QL_MAIN_T0_SIDEPROG
### qm_t0_scientist_Baaekh_A
* Type:	Main
* Goals:
	* 0:
		* GoalType: Goto
			* Target: [-1785, -690]
	* 1:
		* GoalType: Goto
			* Target: [-1844, -690]
	* 2:
		* GoalType: Statistic
			* Id: ScannedBelt
			* Total: 4
		* GoalType: Statistic
			* Id: ScannedGenerated
			* Amount: 1

### qm_t0_scientist_Baaekh_B
* Type:	Main
* FollowUps: ql_main_t0_relic
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Mode: Generated
			* Amount: 1
	* 1:
		* GoalType: Goto
			* Target: [-1785, -690]

## QL_MAIN_T0_RELIC
### qm_t0_relic
* Type:	Main
* FollowUps: ql_main_t0_moreMining
* Goals:
	* 0:
		* GoalType: Goto
			* Target: [-1832, -619]
	* 1:
		* GoalType: Scan
			* Tags: InSystem
			* Amount: 1
	*  2:
		* GoalType: CompleteMission
			* Id: story_A04_RelicSignature

## QL_MAIN_T0_MOREMINING
### qm_t0_scientist_Hyeaa_A
* Type:	Main
* FollowUps: ql_main_t0_jolja
* Goals:
	* 0:
		* GoalType: Goto
			* Target: [-1800, -623]
	* 1:
		* GoalType: Craft
			* Category: Crafting
			* Tags: RCol
			* Amount: 1
	* 2:
		* GoalType: Equip
			* Type: Squad
			* Tags: RCol
	* 3:
		* GoalType: Statistic
			* Id: Mined0A
			* Amount: 225

## NO_QL
### qm_t0_scientist_Hyeaa_B
* Type:	Main
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: RCol
			* Amount: 1
		* GoalType: Craft
			* Category: Crafting
			* Tags: PlasmaBomber
			* Amount: 1
		* GoalType: Craft
			* Category: Crafting
			* Tags: Interceptor
			* Amount: 1
	* 1:
		* GoalType: Craft
			* Category: Crafting
			* Tags: Frigate
			* Amount: 1

### qm_t1_facHiigaran_A
* Type:	Side
* Goals:
	* 0:
		* GoalType: Goto
			* Target: [-1558, -672]
	* 1:
		* GoalType: Statistic
			* Id: ScannedGenerated
			* Amount: 3
		* GoalType: CompleteMission
			* Mode: Generated
			* Amount: 3
	* 2:
		* GoalType: Pay
			* Id: 1A
			* Amount: 500

### qm_t1_facHiigaran_B
* Type:	Side
* Goals:
	* 0:
		* GoalType: Goto
			* Target: [-1429, -553]
	* 1:
		* GoalType: Statistic
			* Id: ScannedBelt
			* Total: 10
	* 2:
		* GoalType: Statistic
			* Ids:
				* Mined1A
				* Mined1B
				* Mined1C
			* Amount: 500
		* GoalType: Statistic
			* Id: ShipsDestroyed
			* Amount: 15
	* 3:
		* GoalType: Goto
			* Target: [-1429, -553]

### qm_t1_facHiigaran_C
* Type:	Side
* Goals:
	* 0:
		* GoalType: Goto
			* Target: [-1552, -610]
	* 1:
		* GoalType: Statistic
			* Id: Mined1A
			* Amount: 500
	* 2:
		* GoalType: Pay
			* Id: 1A
			* Amount: 150
	* 3:
		* GoalType: Pay
			* Id: hgn_su_rcol_01_t0
			* Amount: 3
	* 4:
		* GoalType: Pay
			* Id: hgn_sf_intc_01_t0
			* Amount: 1

### qm_t1_facHiigaran_D
* Type:	Side
* Goals:
	* 0:
		* GoalType: Goto
			* Target: [-1525, -731]
	* 1:
		* GoalType: Scan
			* Tags: InSystem
			* Amount: 3
			* Analyzed: True
	* 2:
		* GoalType: Statistic
			* Id: ShipsDestroyed
			* Amount: 15
		* GoalType: CompleteMission
			* Mode: Generated
			* Amount: 3
	* 3:
		* GoalType: Goto
			* Target: [-1525, -731]

### qm_t1_facCangacian_A
* Type:	Side
* Goals:
	* 0:
		* GoalType: Goto
			* Target: [-1376, -709]
	* 1:
		* GoalType: Statistic
			* Id: ShipsDestroyedP1
			* Amount: 15
	* 2:
		* GoalType: Statistic
			* Ids:
				* Mined1A
				* Mined1B
				* Mined1C
			* Amount: 1000
		* GoalType: Statistic
			* Ids:
				* Refining1N
				* Refining1O
				* Refining1P
			* Amount: 500
	* 3:
		* GoalType: Goto
			* Target: [-1376, -709]

### qm_t1_facCangacian_B
* Type:	Side
* Goals:
	* 0:
		* GoalType: Goto
			* Target: [-1497, -628]
	* 1:
		* GoalType: Statistic
			* Id: ScannedGenerated
			* Amount: 4
		* GoalType: CompleteMission
			* Mode: Generated
			* Amount: 4
		* GoalType: Statistic
			* Id: ShipsDestroyedP1
			* Amount: 15
	* 2:
		* GoalType: Goto
			* Target: [-1497, -628]

### qm_t1_facCangacian_C
* Type:	Side
* Goals:
	* 0:
		* GoalType: Goto
			* Target: [-1793, -424]
	* 1:
		* GoalType: Statistic
			* Id: ScannedBelt
			* Total: 15
	* 2:
		* GoalType: Statistic
			* Id: Mined1A
			* Amount: 1000
		* GoalType: Statistic
			* Id: Refining1N
			* Amount: 500
	* 3:
		* GoalType: Pay
			* Id: 1N
			* Amount: 300

### qm_t1_facCangacian_D
* Type:	Side
* Goals:
	* 0:
		* GoalType: Goto
			* Target: [-1752, -861]
	* 1:
		* GoalType: Scan
			* Tags: InSystem
			* Amount: 2
			* Analyzed: True
	* 2:
		* GoalType: Pay
			* Id: hgn_sf_intc_01_t1
			* Amount: 1
	* 3:
		* GoalType: CompleteMission
			* Mode: Generated
			* Amount: 4
	* 4:
		* GoalType: Goto
			* Target: [-1752, -861]

### qm_t1_facProgenitors_A
* Type:	Side
* Goals:
	* 0:
		* GoalType: Goto
			* Target: [-1497, -628]
	* 1:
		* GoalType: Statistic
			* Id: ShipsDestroyedProgenitor
			* Amount: 10
		* GoalType: Statistic
			* Ids:
				* Mined1A
				* Mined1B
				* Mined1C
			* Amount: 3000
		* GoalType: Statistic
			* Ids:
				* Refining1N
				* Refining1O
				* Refining1P
			* Amount: 1500
	* 2:
		* GoalType: Goto
			* Target: [-1497, -628]

### qm_t1_facProgenitors_B
* Type:	Side
* Goals:
	* 0:
		* GoalType: Goto
			* Target: [-1376, -709]
	* 1:
		* GoalType: Statistic
			* Id: ScannedGenerated
			* Amount: 5
		* GoalType: Craft
			* Category: Upgrade
			* Tags: Weapon_Module
			* Amount: 1
		* GoalType: CompleteMission
			* Mode: Generated
			* Amount: 5
			* Tier: 1
	* 2:
		* GoalType: Goto
			* Target: [-1376, -709]

### qm_t1_facProgenitors_C
* Type:	Side
* Goals:
	* 0:
		* GoalType: Goto
			* Target: [-1543, -626]
	* 1:
		* GoalType: GainItem
			* Id: AA
			* Amount: 30
			* ExcludedSources:
				* SellItem
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
	* 2:
		* GoalType: Craft
			* Category: Upgrade
			* Tags: Weapon_Module
			* Amount: 2
	* 3:
		* GoalType: CompleteMission
			* Mode: Generated
			* Amount: 5
			* Tier: 1
	* 4:
		* GoalType: Goto
			* Target: [-1543, -626]

### qm_t1_facProgenitors_D
* Type:	Side
* Goals:
	* 0:
		* GoalType: Goto
			* Target: [-1793, -424]
	* 1:
		* GoalType: Statistic
			* Id: ScannedBelt
			* Total: 20
	* 2:
		* GoalType: GainItem
			* Id: AB
			* Amount: 10
			* ExcludedSources:
				* SellItem
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
		* GoalType: Statistic
			* Id: ShipsDestroyedProgenitor
			* Amount: 10
	* 3:
		* GoalType: Goto
			* Target: [-1793, -424]

### qm_t1_facIyatequa_A
* Type:	Side
* Goals:
	* 0:
		* GoalType: Goto
			* Target: [-1825, -480]
	* 1:
		* GoalType: Statistic
			* Ids:
				* Mined1A
				* Mined1B
				* Mined1C
			* Amount: 3000
		* GoalType: GainItem
			* Tags: RareEarth
			* Amount: 60
			* ExcludedSources:
				* SellItem
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
		* GoalType: Craft
			* Category: Upgrade
			* Tags: Weapon_Module
			* Amount: 2
	* 2:
		* GoalType: Goto
			* Target: [-1825, -480]

### qm_t1_facIyatequa_B
* Type:	Side
* Goals:
	* 0:
		* GoalType: Goto
			* Target: [-1525, -731]
	* 1:
		* GoalType: Statistic
			* Ids:
				* Refining1N
				* Refining1O
				* Refining1P
			* Amount: 1500
		* GoalType: Craft
			* Category: Upgrade
			* Tags: Weapon_Module
			* Amount: 1
	* 2:
		* GoalType: Statistic
			* Id: ShipsDestroyed
			* Amount: 25
	* 3:
		* GoalType: Goto
			* Target: [-1525, -731]

### qm_t1_facIyatequa_C
* Type:	Side
* Goals:
	* 0:
		* GoalType: Goto
			* Target: [-1429, -553]
	* 1:
		* GoalType: Scan
			* Tags: InSystem
			* Amount: 5
			* Analyzed: True
		* GoalType: CompleteMission
			* Mode: Generated
			* Amount: 5
			* Tier: 1
		* GoalType: Statistic
			* Id: ShipsDestroyed
			* Amount: 25
	* 2:
		* GoalType: Goto
			* Target: [-1429, -553]

### qm_t1_facIyatequa_D
* Type:	Side
* Goals:
	* 0:
		* GoalType: Goto
			* Target: [-1552, -610]
	* 1:
		* GoalType: Goto
			* Target: [-1558, -672]
	* 2:
		* GoalType: Scan
			* Tags: InSystem
			* Amount: 5
			* Analyzed: True
		* GoalType: CompleteMission
			* Mode: Generated
			* Amount: 5
			* Tier: 1
	* 3:
		* GoalType: Pay
			* Id: 1O
			* Amount: 1000
	* 4:
		* GoalType: Goto
			* Target: [-1552, -610]

### qm_t2_facCangacian_A
* Type:	Side
* Goals:
	* 0:
		* GoalType: Goto
			* Target: [-1491, -596]
	* 1:
		* GoalType: Statistic
			* Id: ShipsDestroyed
			* Amount: 35
	* 2:
		* GoalType: GainItem
			* Id: RP
			* Amount: 45
			* ExcludedSources:
				* SellItem
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
	* 3:
		* GoalType: Craft
			* Tags: Research
			* Amount: 1
	* 4:
		* GoalType: Goto
			* Target: [-1491, -596]

### qm_t2_facCangacian_B
* Type:	Side
* Goals:
	* 0:
		* GoalType: Goto
			* Target: [-1643, -552]
	* 1:
		* GoalType: CompleteMission
			* Mode: Generated
			* Amount: 10
			* Tier: 1
	* 2:
		* GoalType: Pay
			* Id: 2A
			* Amount: 650
		* GoalType: Pay
			* Id: 2B
			* Amount: 650
		* GoalType: Pay
			* Id: 2C
			* Amount: 650
	* 3:
		* GoalType: GainItem
			* Id: RP
			* Amount: 45
			* ExcludedSources:
				* SellItem
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
	* 4:
		* GoalType: Goto
			* Target: [-1643, -552]

### qm_t2_facCangacian_C
* Type:	Side
* Goals:
	* 0:
		* GoalType: Goto
			* Target: [-1784, -564]
	* 1:
		* GoalType: GainItem
			* Id: RP
			* Amount: 45
			* ExcludedSources:
				* SellItem
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
	* 2:
		* GoalType: Statistic
			* Id: ScannedBelt
			* Total: 30
		* GoalType: Statistic
			* Id: ShipsDestroyed
			* Amount: 35
	* 3:
		* GoalType: Goto
			* Target: [-1784, -564]

### qm_t2_facCangacian_D
* Type:	Side
* Goals:
	* 0:
		* GoalType: Goto
			* Target: [-1559, -788]
	* 1:
		* GoalType: Pay
			* Id: 2O
			* Amount: 1000
	* 2:
		* GoalType: Statistic
			* Id: ScannedGenerated
			* Amount: 10
		* GoalType: CompleteMission
			* Mode: Generated
			* Amount: 10
			* Tier: 1
	* 3:
		* GoalType: Goto
			* Target: [-1559, -788]

### qm_t2_facHiigaran_A
* Type:	Side
* Goals:
	* 0:
		* GoalType: Goto
			* Target: [-1784, -564]
	* 1:
		* GoalType: Scan
			* Tags: InSystem_T2up
			* Amount: 5
			* Analyzed: True
	* 2:
		* GoalType: Craft
			* Category: Crafting
			* Tags: Part
			* Amount: 450
	* 3:
		* GoalType: Pay
			* Id: 2P
			* Amount: 1000

### qm_t2_facHiigaran_B
* Type:	Side
* Goals:
	* 0:
		* GoalType: Goto
			* Target: [-1659, -561]
	* 1:
		* GoalType: CompleteMission
			* Mode: Generated
			* Amount: 10
			* Tier: 1
	* 2:
		* GoalType: Craft
			* Category: Crafting
			* Tags: Part
			* Amount: 180
	* 3:
		* GoalType: Pay
			* Id: intmed_ship_small_t2
			* Amount: 60

### qm_t2_facHiigaran_C
* Type:	Side
* Goals:
	* 0:
		* GoalType: Goto
			* Target: [-1491, -596]
	* 1:
		* GoalType: CompleteMission
			* Mode: Strike
			* Amount: 1
		* GoalType: Statistic
			* Id: ShipsDestroyed
			* Amount: 35
	* 2:
		* GoalType: Pay
			* Id: intmed_weapon_small_t2
			* Amount: 60

### qm_t2_facHiigaran_D
* Type:	Side
* Goals:
	* 0:
		* GoalType: Goto
			* Target: [-1780, -457]
	* 1:
		* GoalType: Statistic
			* Id: ScannedBelt
			* Total: 35
		* GoalType: Statistic
			* Id: ShipsDestroyed
			* Amount: 35
	* 2:
		* GoalType: Pay
			* Id: 2A
			* Amount: 650
		* GoalType: Pay
			* Id: 2B
			* Amount: 650
		* GoalType: Pay
			* Id: 2C
			* Amount: 650

### qm_t2_facIyatequa_A
* Type:	Side
* Goals:
	* 0:
		* GoalType: Goto
			* Target: [-1643, -552]
	* 1:
		* GoalType: Pay
			* Id: 2O
			* Amount: 1000
		* GoalType: Pay
			* Id: 2P
			* Amount: 1000
		* GoalType: Pay
			* Id: intmed_ship_large_t2
			* Amount: 20
	* 2:
		* GoalType: CompleteQuest
			* Amount: 7
			* Tags: Faction_Tr1_T2up
	* 3:
		* GoalType: Goto
			* Target: [-1643, -552]

### qm_t2_facIyatequa_B
* Type:	Side
* Goals:
	* 0:
		* GoalType: Goto
			* Target: [-1659, -561]
	* 1:
		* GoalType: Statistic
			* Id: ShipsDestroyedProgenitor
			* Amount: 15
	* 2:
		* GoalType: CompleteQuest
			* Amount: 15
			* Tags: Faction_Tr1_T2up
	* 3:
		* GoalType: Goto
			* Target: [-1659, -561]

### qm_t2_facIyatequa_C
* Type:	Side
* Goals:
	* 0:
		* GoalType: Goto
			* Target: [-1780, -457]
	* 1:
		* GoalType: Statistic
			* Id: ShipsDestroyedP1
			* Amount: 30
	* 2:
		* GoalType: Statistic
			* Id: ShipsDestroyed
			* Amount: 30
		* GoalType: CompleteQuest
			* Amount: 7
			* Tags: Faction_Tr1_T2up
	* 3:
		* GoalType: Goto
			* Target: [-1780, -457]

### qm_t2_facIyatequa_D
* Type:	Side
* Goals:
	* 0:
		* GoalType: Goto
			* Target: [-1559, -788]
	* 1:
		* GoalType: Scan
			* Tags: InSystem_T2up
			* Amount: 10
			* Analyzed: True
	* 2:
		* GoalType: GainItem
			* Id: RP
			* Amount: 45
			* ExcludedSources:
				* SellItem
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
	* 3:
		* GoalType: Pay
			* Id: hgn_su_rcol_01_t2
			* Amount: 1
		* GoalType: Pay
			* Id: 2D
			* Amount: 500
	* 4:
		* GoalType: Goto
			* Target: [-1559, -788]

### qm_t2_internalRefinery
* Type:	Main
* Goals:
	* 0:
		* GoalType: Craft
			* Tags: Refining_Factory
	* 1:
		* GoalType: Equip
			* Type: Internal
			* Tags: Refining_Factory

### qm_t2_facTanoch_A
* Type:	Side
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ScannedBelt
			* Total: 40
	* 1:
		* GoalType: Pay
			* Id: 2N
			* Amount: 350
		* GoalType: Pay
			* Id: 2O
			* Amount: 350
		* GoalType: Pay
			* Id: 2P
			* Amount: 350

### qm_t2_facTanoch_B
* Type:	Side
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: RepTanoch
			* Amount: 350
		* GoalType: Statistic
			* Id: ShipsDestroyedP1
			* Amount: 15

### qm_t2_facTanoch_C
* Type:	Side
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Refining
			* Amount: 2000
			* Tags: T2
		* GoalType: Craft
			* Category: Crafting
			* Tags: Part
			* Amount: 150
	* 1:
		* GoalType: Pay
			* Id: 2O
			* Amount: 350
		* GoalType: Pay
			* Id: intmed_module_small_t2
			* Amount: 50
		* GoalType: Pay
			* Id: hgn_su_rcol_01_t2
			* Amount: 1

### qm_t2_facTanoch_D
* Type:	Side
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_Generated_T2up
			* Amount: 10
			* Analyzed: True
		* GoalType: Statistic
			* Id: ShipsDestroyedYaot
			* Amount: 15

### qm_t2_facYaot_A
* Type:	Side
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedYaot
			* Amount: 30

### qm_t2_facYaot_B
* Type:	Side
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ScannedBelt
			* Total: 45
		* GoalType: Statistic
			* Ids:
				* Mined2A
				* Mined2B
				* Mined2C
				* Mined2D
			* Amount: 1800

### qm_t2_facYaot_C
* Type:	Side
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_Generated_T2up
			* Amount: 10
			* Analyzed: True
		* GoalType: CompleteMission
			* Mode: Generated
			* Tags: T2up
			* Amount: 10
		* GoalType: Scan
			* Tags: InGalaxy_T2up
			* Amount: 7

### qm_t2_facYaot_D
* Type:	Side
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Insignia
			* Amount: 80
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
		* GoalType: UpgradeOfficer
			* Amount: 15

### qs_unlockStrikes_t1
* Type:	Side
* Goals:
	* 0:
		* GoalType: Goto
			* Target: [-1535, -436]
			* MoveType: InSystem
	* 1:
		* GoalType: Scan
			* : 

### qt_daily_buy
* Type:	Daily
* Goals:
	* 0:
		* GoalType: Buy
			* Amount: 1

### qt_daily_mine
* Type:	Daily
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: Mined
			* Amount: 1500

### qt_daily_refine
* Type:	Daily
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Refining
			* Amount: 500

### qt_daily_craft
* Type:	Daily
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Amount: 10

### qt_daily_gainRP
* Type:	Daily
* Goals:
	* 0:
		* GoalType: GainItem
			* Id: RP
			* Amount: 400
			* ExcludedSources:
				* SellItem
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qt_daily_insignias
* Type:	Daily
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Insignia
			* Amount: 5
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qt_daily_liaison
* Type:	Daily
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3

### qt_daily_destroy
* Type:	Daily
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyed
			* Amount: 15

### qt_daily_signals
* Type:	Daily
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem
			* Amount: 5
			* Analyzed: True

### qt_daily_dailyMission
* Type:	Daily
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Mode: Strike

### qt_daily_dailies
* Type:	Daily
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 8
			* Tags: Daily

### qt_weekly_dailies
* Type:	Weekly
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 40
			* Tags: Daily

### qt_weekly_reputation
* Type:	Weekly
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 9
			* Tags: Faction

### qt_weekly_clanQuests
* Type:	Weekly
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 10
			* Tags: Clan

### qt_weekly_levelOfficers
* Type:	Weekly
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 7

### qt_weekly_upgrades
* Type:	Weekly
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Upgrade
			* Amount: 10

### qt_weekly_missions
* Type:	Weekly
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 9
			* Mode: Generated

### qt_weekly_research
* Type:	Weekly
* Goals:
	* 0:
		* GoalType: Craft
			* Tags: Research
			* Amount: 5

### qe_amaSum_2023_daily_A_t1
* Type:	Event
* EventId:	event_season_amaSum_2023_t1
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Asteroid_Crud_T1up
			* Amount: 350
			* ExcludedSources:
				* PayGoal
				* QuestReward
				* MissionReward
				* BuyItem
				* SellItem
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer

### qe_amaSum_2023_daily_B_t1
* Type:	Event
* EventId:	event_season_amaSum_2023_t1
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: T1up
			* Amount: 1

### qe_amaSum_2023_daily_C_t1
* Type:	Event
* EventId:	event_season_amaSum_2023_t1
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedDarkHiigaranT1
				* ShipsDestroyedDarkHiigaranT2
				* ShipsDestroyedDarkHiigaranT3
				* ShipsDestroyedDarkHiigaranT4
			* Amount: 10

### qe_amaSum_2023_daily_D_t1
* Type:	Event
* EventId:	event_season_amaSum_2023_t1
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: ProgenitorRelic_T1up
			* Amount: 1
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_amaSum_2023_daily_A_t2
* Type:	Event
* EventId:	event_season_amaSum_2023_t2
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Asteroid_Crud_T2up
			* Amount: 400
			* ExcludedSources:
				* PayGoal
				* QuestReward
				* MissionReward
				* BuyItem
				* SellItem
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer

### qe_amaSum_2023_daily_B_t2
* Type:	Event
* EventId:	event_season_amaSum_2023_t2
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: Part_T2up
			* Amount: 25

### qe_amaSum_2023_daily_C_t2
* Type:	Event
* EventId:	event_season_amaSum_2023_t2
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedDarkHiigaranT2
				* ShipsDestroyedDarkHiigaranT3
				* ShipsDestroyedDarkHiigaranT4
			* Amount: 10

### qe_amaSum_2023_daily_D_t2
* Type:	Event
* EventId:	event_season_amaSum_2023_t2
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: ProgenitorRelic_T2up
			* Amount: 1
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_amaSum_2023_daily_A_t3
* Type:	Event
* EventId:	event_season_amaSum_2023_t3
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Asteroid_Crud_T3up
			* Amount: 450
			* ExcludedSources:
				* PayGoal
				* QuestReward
				* MissionReward
				* BuyItem
				* SellItem
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer

### qe_amaSum_2023_daily_B_t3
* Type:	Event
* EventId:	event_season_amaSum_2023_t3
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: Part_T3up
			* Amount: 25

### qe_amaSum_2023_daily_C_t3
* Type:	Event
* EventId:	event_season_amaSum_2023_t3
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedDarkHiigaranT3
				* ShipsDestroyedDarkHiigaranT4
			* Amount: 10

### qe_amaSum_2023_daily_D_t3
* Type:	Event
* EventId:	event_season_amaSum_2023_t3
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: ProgenitorRelic_T3up
			* Amount: 1
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_amaSum_2023_daily_A_t4
* Type:	Event
* EventId:	event_season_amaSum_2023_t4
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Asteroid_Crud_T4up
			* Amount: 500
			* ExcludedSources:
				* PayGoal
				* QuestReward
				* MissionReward
				* BuyItem
				* SellItem
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer

### qe_amaSum_2023_daily_B_t4
* Type:	Event
* EventId:	event_season_amaSum_2023_t4
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: Part_T4up
			* Amount: 25

### qe_amaSum_2023_daily_C_t4
* Type:	Event
* EventId:	event_season_amaSum_2023_t4
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* PayGoal
				* QuestReward
				* MissionReward
				* BuyItem
				* SellItem
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer
			* Amount: 10

### qe_amaSum_2023_daily_D_t4
* Type:	Event
* EventId:	event_season_amaSum_2023_t4
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: ProgenitorRelic_T4up
			* Amount: 1
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_7days_mar_2024_daily_A_t1
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t1
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_Container_T1up
			* Amount: 1
			* Analyzed: True

### qe_7days_mar_2024_daily_A_t2
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t2
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_Container_T2up
			* Amount: 1
			* Analyzed: True

### qe_7days_mar_2024_daily_A_t3
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t3
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_Container_T3up
			* Amount: 1
			* Analyzed: True

### qe_7days_mar_2024_daily_A_t4
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t4
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_Container_T4up
			* Amount: 1
			* Analyzed: True

### qe_7days_mar_2024_daily_B_t1
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t1
* Goals:
	* 0:
		* GoalType: Pay
			* Id: questItem_progenitorRelic_t1
			* Amount: 1

### qe_7days_mar_2024_daily_B_t2
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t2
* Goals:
	* 0:
		* GoalType: Pay
			* Id: questItem_progenitorRelic_t2
			* Amount: 1

### qe_7days_mar_2024_daily_B_t3
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t3
* Goals:
	* 0:
		* GoalType: Pay
			* Id: questItem_progenitorRelic_t3
			* Amount: 1

### qe_7days_mar_2024_daily_B_t4
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t4
* Goals:
	* 0:
		* GoalType: Pay
			* Id: questItem_progenitorRelic_t4
			* Amount: 1

### qe_7days_mar_2024_daily_C_t1
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Rare_T1up
			* Mode: Generated

### qe_7days_mar_2024_daily_C_t2
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Epic_T2up
			* Mode: Generated

### qe_7days_mar_2024_daily_C_t3
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Epic_T3up
			* Mode: Generated

### qe_7days_mar_2024_daily_C_t4
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Epic_T4up
			* Mode: Generated

### qe_7days_mar_2024_daily_D_t1
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t1
* Goals:
	* 0:
		* GoalType: GainItem
			* Id: LP
			* Amount: 10
			* ExcludedSources:
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
				* DismissOfficer
				* OpenContainer
				* ClaimMail
				* DismantleItem

### qe_7days_mar_2024_daily_D_t2
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t2
* Goals:
	* 0:
		* GoalType: GainItem
			* Id: LP
			* Amount: 10
			* ExcludedSources:
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
				* DismissOfficer
				* OpenContainer
				* ClaimMail
				* DismantleItem

### qe_7days_mar_2024_daily_D_t3
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t3
* Goals:
	* 0:
		* GoalType: GainItem
			* Id: LP
			* Amount: 10
			* ExcludedSources:
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
				* DismissOfficer
				* OpenContainer
				* ClaimMail
				* DismantleItem

### qe_7days_mar_2024_daily_D_t4
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t4
* Goals:
	* 0:
		* GoalType: GainItem
			* Id: LP
			* Amount: 10
			* ExcludedSources:
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
				* DismissOfficer
				* OpenContainer
				* ClaimMail
				* DismantleItem

### qe_iyaFal_2023_daily_A_t1
* Type:	Event
* EventId:	event_season_iyaFal_2023_t1
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedP1T1
				* ShipsDestroyedP1T2
				* ShipsDestroyedP1T3
				* ShipsDestroyedP1T4
			* Amount: 10

### qe_iyaFal_2023_daily_B_t1
* Type:	Event
* EventId:	event_season_iyaFal_2023_t1
* Goals:
	* 0:
		* GoalType: GainItem
			* Id: CR
			* Amount: 1250
			* ExcludedSources:
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
				* DismissOfficer
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer

### qe_iyaFal_2023_daily_C_t1
* Type:	Event
* EventId:	event_season_iyaFal_2023_t1
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_T1up
			* Amount: 10
			* Analyzed: True

### qe_iyaFal_2023_daily_D_t1
* Type:	Event
* EventId:	event_season_iyaFal_2023_t1
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: RareEarth_T1up
			* Amount: 20
			* ExcludedSources:
				* SellItem
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_iyaFal_2023_daily_A_t2
* Type:	Event
* EventId:	event_season_iyaFal_2023_t2
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedP1T2
				* ShipsDestroyedP1T3
				* ShipsDestroyedP1T4
			* Amount: 10

### qe_iyaFal_2023_daily_B_t2
* Type:	Event
* EventId:	event_season_iyaFal_2023_t2
* Goals:
	* 0:
		* GoalType: GainItem
			* Id: CR
			* Amount: 2500
			* ExcludedSources:
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
				* DismissOfficer
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer

### qe_iyaFal_2023_daily_C_t2
* Type:	Event
* EventId:	event_season_iyaFal_2023_t2
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_T2up
			* Amount: 10
			* Analyzed: True

### qe_iyaFal_2023_daily_D_t2
* Type:	Event
* EventId:	event_season_iyaFal_2023_t2
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: RareEarth_T2up
			* Amount: 20
			* ExcludedSources:
				* SellItem
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_iyaFal_2023_daily_A_t3
* Type:	Event
* EventId:	event_season_iyaFal_2023_t3
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedP1T3
				* ShipsDestroyedP1T4
			* Amount: 10

### qe_iyaFal_2023_daily_B_t3
* Type:	Event
* EventId:	event_season_iyaFal_2023_t3
* Goals:
	* 0:
		* GoalType: GainItem
			* Id: CR
			* Amount: 5000
			* ExcludedSources:
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
				* DismissOfficer
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer

### qe_iyaFal_2023_daily_C_t3
* Type:	Event
* EventId:	event_season_iyaFal_2023_t3
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_T3up
			* Amount: 10
			* Analyzed: True

### qe_iyaFal_2023_daily_D_t3
* Type:	Event
* EventId:	event_season_iyaFal_2023_t3
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: RareEarth_T3up
			* Amount: 20
			* ExcludedSources:
				* SellItem
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_iyaFal_2023_daily_A_t4
* Type:	Event
* EventId:	event_season_iyaFal_2023_t4
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* SellItem
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
			* Amount: 10

### qe_iyaFal_2023_daily_B_t4
* Type:	Event
* EventId:	event_season_iyaFal_2023_t4
* Goals:
	* 0:
		* GoalType: GainItem
			* Id: CR
			* Amount: 10000
			* ExcludedSources:
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
				* DismissOfficer
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer

### qe_iyaFal_2023_daily_C_t4
* Type:	Event
* EventId:	event_season_iyaFal_2023_t4
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_T4up
			* Amount: 10
			* Analyzed: True

### qe_iyaFal_2023_daily_D_t4
* Type:	Event
* EventId:	event_season_iyaFal_2023_t4
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: RareEarth_T4up
			* Amount: 20
			* ExcludedSources:
				* SellItem
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_anniversary_2023_daily_A_t1
* Type:	Event
* EventId:	event_anniversary_2023_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 5
			* Tags: T1up
			* Mode: Generated

### qe_anniversary_2023_daily_B_t1
* Type:	Event
* EventId:	event_anniversary_2023_t1
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: RareEarth_T1up
			* Amount: 50
			* ExcludedSources:
				* SellItem
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_anniversary_2023_daily_A_t2
* Type:	Event
* EventId:	event_anniversary_2023_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 5
			* Tags: T2up
			* Mode: Generated

### qe_anniversary_2023_daily_B_t2
* Type:	Event
* EventId:	event_anniversary_2023_t2
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: RareEarth_T2up
			* Amount: 50
			* ExcludedSources:
				* SellItem
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_anniversary_2023_daily_A_t3
* Type:	Event
* EventId:	event_anniversary_2023_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 5
			* Tags: T3up
			* Mode: Generated

### qe_anniversary_2023_daily_B_t3
* Type:	Event
* EventId:	event_anniversary_2023_t3
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: RareEarth_T3up
			* Amount: 50
			* ExcludedSources:
				* SellItem
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_anniversary_2023_daily_A_t4
* Type:	Event
* EventId:	event_anniversary_2023_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 5
			* Tags: T4up
			* Mode: Generated

### qe_anniversary_2023_daily_B_t4
* Type:	Event
* EventId:	event_anniversary_2023_t4
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: RareEarth_T4up
			* Amount: 50
			* ExcludedSources:
				* SellItem
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_halloween_2023_daily_A_t1
* Type:	Event
* EventId:	event_halloween_2023_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: ProgenitorInvasion_T1up
			* Mode: Generated

### qe_halloween_2023_daily_B_t1
* Type:	Event
* EventId:	event_halloween_2023_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 2
			* Tags: ProgenitorInvasion_T1up
			* Mode: Generated

### qe_halloween_2023_daily_C_t1
* Type:	Event
* EventId:	event_halloween_2023_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 5
			* Tags: ProgenitorInvasion_T1up
			* Mode: Generated

### qe_halloween_2023_daily_D_t1
* Type:	Event
* EventId:	event_halloween_2023_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 10
			* Tags: ProgenitorInvasion_T1up
			* Mode: Generated

### qe_halloween_2023_daily_A_t2
* Type:	Event
* EventId:	event_halloween_2023_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: ProgenitorInvasion_T2up
			* Mode: Generated

### qe_halloween_2023_daily_B_t2
* Type:	Event
* EventId:	event_halloween_2023_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 2
			* Tags: ProgenitorInvasion_T2up
			* Mode: Generated

### qe_halloween_2023_daily_C_t2
* Type:	Event
* EventId:	event_halloween_2023_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 5
			* Tags: ProgenitorInvasion_T2up
			* Mode: Generated

### qe_halloween_2023_daily_D_t2
* Type:	Event
* EventId:	event_halloween_2023_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 10
			* Tags: ProgenitorInvasion_T2up
			* Mode: Generated

### qe_halloween_2023_daily_A_t3
* Type:	Event
* EventId:	event_halloween_2023_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: ProgenitorInvasion_T3up
			* Mode: Generated

### qe_halloween_2023_daily_B_t3
* Type:	Event
* EventId:	event_halloween_2023_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 2
			* Tags: ProgenitorInvasion_T3up
			* Mode: Generated

### qe_halloween_2023_daily_C_t3
* Type:	Event
* EventId:	event_halloween_2023_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 5
			* Tags: ProgenitorInvasion_T3up
			* Mode: Generated

### qe_halloween_2023_daily_D_t3
* Type:	Event
* EventId:	event_halloween_2023_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 10
			* Tags: ProgenitorInvasion_T3up
			* Mode: Generated

### qe_halloween_2023_daily_A_t4
* Type:	Event
* EventId:	event_halloween_2023_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: ProgenitorInvasion_T4up
			* Mode: Generated

### qe_halloween_2023_daily_B_t4
* Type:	Event
* EventId:	event_halloween_2023_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 2
			* Tags: ProgenitorInvasion_T4up
			* Mode: Generated

### qe_halloween_2023_daily_C_t4
* Type:	Event
* EventId:	event_halloween_2023_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 5
			* Tags: ProgenitorInvasion_T4up
			* Mode: Generated

### qe_halloween_2023_daily_D_t4
* Type:	Event
* EventId:	event_halloween_2023_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 10
			* Tags: ProgenitorInvasion_T4up
			* Mode: Generated

### qe_tanWin_2023_daily_A_t1
* Type:	Event
* EventId:	event_tanochWinter_2023_t1
* Goals:
	* 0:
		* GoalType: Pay
			* Id: questItem_progenitorRelic_t1
			* Amount: 1

### qe_tanWin_2023_daily_B_t1
* Type:	Event
* EventId:	event_tanochWinter_2023_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 5
			* Tags: T1up
			* Mode: Generated

### qe_tanWin_2023_daily_C_t1
* Type:	Event
* EventId:	event_tanochWinter_2023_t1
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: T1up
			* Amount: 1

### qe_tanWin_2023_daily_D_t1
* Type:	Event
* EventId:	event_tanochWinter_2023_t1
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 1

### qe_tanWin_2023_daily_A_t2
* Type:	Event
* EventId:	event_tanochWinter_2023_t2
* Goals:
	* 0:
		* GoalType: Pay
			* Id: questItem_progenitorRelic_t2
			* Amount: 1

### qe_tanWin_2023_daily_B_t2
* Type:	Event
* EventId:	event_tanochWinter_2023_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 5
			* Mode: Faction
			* Tags: T2up_Tanoch

### qe_tanWin_2023_daily_C_t2
* Type:	Event
* EventId:	event_tanochWinter_2023_t2
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: Part_T2up
			* Amount: 100

### qe_tanWin_2023_daily_D_t2
* Type:	Event
* EventId:	event_tanochWinter_2023_t2
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 2

### qe_tanWin_2023_daily_A_t3
* Type:	Event
* EventId:	event_tanochWinter_2023_t3
* Goals:
	* 0:
		* GoalType: Pay
			* Id: questItem_progenitorRelic_t3
			* Amount: 1

### qe_tanWin_2023_daily_B_t3
* Type:	Event
* EventId:	event_tanochWinter_2023_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 5
			* Mode: Faction
			* Tags: T3up_Tanoch

### qe_tanWin_2023_daily_C_t3
* Type:	Event
* EventId:	event_tanochWinter_2023_t3
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: Part_T3up
			* Amount: 100

### qe_tanWin_2023_daily_D_t3
* Type:	Event
* EventId:	event_tanochWinter_2023_t3
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 3

### qe_tanWin_2023_daily_A_t4
* Type:	Event
* EventId:	event_tanochWinter_2023_t4
* Goals:
	* 0:
		* GoalType: Pay
			* Id: questItem_progenitorRelic_t4
			* Amount: 1

### qe_tanWin_2023_daily_B_t4
* Type:	Event
* EventId:	event_tanochWinter_2023_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 5
			* Mode: Faction
			* Tags: T4up_Tanoch

### qe_tanWin_2023_daily_C_t4
* Type:	Event
* EventId:	event_tanochWinter_2023_t4
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: Part_T4up
			* Amount: 100

### qe_tanWin_2023_daily_D_t4
* Type:	Event
* EventId:	event_tanochWinter_2023_t4
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 5

### qe_nimbusTreasures_2024_daily_A_t1
* Type:	Event
* EventId:	event_nimbusTreasures_2024_t1
* Goals:
	* 0:
		* GoalType: ChargeScanner
			* NewCharge: 1.5

### qe_nimbusTreasures_2024_daily_B_t1
* Type:	Event
* EventId:	event_nimbusTreasures_2024_t1
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_Container_T1up
			* Amount: 3
			* Analyzed: True

### qe_nimbusTreasures_2024_daily_C1_t1
* Type:	Event
* EventId:	event_nimbusTreasures_2024_t1
* Goals:
	* 0:
		* GoalType: Pay
			* Id: questItem_alienProbe_t1
			* Amount: 1

### qe_nimbusTreasures_2024_daily_C2_t1
* Type:	Event
* EventId:	event_nimbusTreasures_2024_t1
* Goals:
	* 0:
		* GoalType: Pay
			* Id: questItem_alienProbe_t1
			* Amount: 2

### qe_nimbusTreasures_2024_daily_C3_t1
* Type:	Event
* EventId:	event_nimbusTreasures_2024_t1
* Goals:
	* 0:
		* GoalType: Pay
			* Id: questItem_alienProbe_t1
			* Amount: 3

### qe_nimbusTreasures_2024_daily_C4_t1
* Type:	Event
* EventId:	event_nimbusTreasures_2024_t1
* Goals:
	* 0:
		* GoalType: Pay
			* Id: questItem_alienProbe_t1
			* Amount: 4

### qe_nimbusTreasures_2024_daily_A_t2
* Type:	Event
* EventId:	event_nimbusTreasures_2024_t2
* Goals:
	* 0:
		* GoalType: ChargeScanner
			* NewCharge: 1.5

### qe_nimbusTreasures_2024_daily_B_t2
* Type:	Event
* EventId:	event_nimbusTreasures_2024_t2
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_Container_T2up
			* Amount: 3
			* Analyzed: True

### qe_nimbusTreasures_2024_daily_C1_t2
* Type:	Event
* EventId:	event_nimbusTreasures_2024_t2
* Goals:
	* 0:
		* GoalType: Pay
			* Id: questItem_alienProbe_t2
			* Amount: 1

### qe_nimbusTreasures_2024_daily_C2_t2
* Type:	Event
* EventId:	event_nimbusTreasures_2024_t2
* Goals:
	* 0:
		* GoalType: Pay
			* Id: questItem_alienProbe_t2
			* Amount: 2

### qe_nimbusTreasures_2024_daily_C3_t2
* Type:	Event
* EventId:	event_nimbusTreasures_2024_t2
* Goals:
	* 0:
		* GoalType: Pay
			* Id: questItem_alienProbe_t2
			* Amount: 3

### qe_nimbusTreasures_2024_daily_C4_t2
* Type:	Event
* EventId:	event_nimbusTreasures_2024_t2
* Goals:
	* 0:
		* GoalType: Pay
			* Id: questItem_alienProbe_t2
			* Amount: 4

### qe_nimbusTreasures_2024_daily_A_t3
* Type:	Event
* EventId:	event_nimbusTreasures_2024_t3
* Goals:
	* 0:
		* GoalType: ChargeScanner
			* NewCharge: 1.5

### qe_nimbusTreasures_2024_daily_B_t3
* Type:	Event
* EventId:	event_nimbusTreasures_2024_t3
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_Container_T3up
			* Amount: 3
			* Analyzed: True

### qe_nimbusTreasures_2024_daily_C1_t3
* Type:	Event
* EventId:	event_nimbusTreasures_2024_t3
* Goals:
	* 0:
		* GoalType: Pay
			* Id: questItem_alienProbe_t3
			* Amount: 1

### qe_nimbusTreasures_2024_daily_C2_t3
* Type:	Event
* EventId:	event_nimbusTreasures_2024_t3
* Goals:
	* 0:
		* GoalType: Pay
			* Id: questItem_alienProbe_t3
			* Amount: 2

### qe_nimbusTreasures_2024_daily_C3_t3
* Type:	Event
* EventId:	event_nimbusTreasures_2024_t3
* Goals:
	* 0:
		* GoalType: Pay
			* Id: questItem_alienProbe_t3
			* Amount: 3

### qe_nimbusTreasures_2024_daily_C4_t3
* Type:	Event
* EventId:	event_nimbusTreasures_2024_t3
* Goals:
	* 0:
		* GoalType: Pay
			* Id: questItem_alienProbe_t3
			* Amount: 4

### qe_nimbusTreasures_2024_daily_A_t4
* Type:	Event
* EventId:	event_nimbusTreasures_2024_t4
* Goals:
	* 0:
		* GoalType: ChargeScanner
			* NewCharge: 1.5

### qe_nimbusTreasures_2024_daily_B_t4
* Type:	Event
* EventId:	event_nimbusTreasures_2024_t4
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_Container_T4up
			* Amount: 3
			* Analyzed: True

### qe_nimbusTreasures_2024_daily_C1_t4
* Type:	Event
* EventId:	event_nimbusTreasures_2024_t4
* Goals:
	* 0:
		* GoalType: Pay
			* Id: questItem_alienProbe_t4
			* Amount: 1

### qe_nimbusTreasures_2024_daily_C2_t4
* Type:	Event
* EventId:	event_nimbusTreasures_2024_t4
* Goals:
	* 0:
		* GoalType: Pay
			* Id: questItem_alienProbe_t4
			* Amount: 2

### qe_nimbusTreasures_2024_daily_C3_t4
* Type:	Event
* EventId:	event_nimbusTreasures_2024_t4
* Goals:
	* 0:
		* GoalType: Pay
			* Id: questItem_alienProbe_t4
			* Amount: 3

### qe_nimbusTreasures_2024_daily_C4_t4
* Type:	Event
* EventId:	event_nimbusTreasures_2024_t4
* Goals:
	* 0:
		* GoalType: Pay
			* Id: questItem_alienProbe_t4
			* Amount: 4

### qe_yaoSpr_2024_daily_A_t1
* Type:	Event
* EventId:	event_yaotSpring_2024_t1
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedP1T1
				* ShipsDestroyedP1T2
				* ShipsDestroyedP1T3
				* ShipsDestroyedP1T4
			* Amount: 10

### qe_yaoSpr_2024_daily_A_t2
* Type:	Event
* EventId:	event_yaotSpring_2024_t2
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedP1T2
				* ShipsDestroyedP1T3
				* ShipsDestroyedP1T4
			* Amount: 10

### qe_yaoSpr_2024_daily_A_t3
* Type:	Event
* EventId:	event_yaotSpring_2024_t3
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedP1T3
				* ShipsDestroyedP1T4
			* Amount: 10

### qe_yaoSpr_2024_daily_A_t4
* Type:	Event
* EventId:	event_yaotSpring_2024_t4
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedP1T3
				* ShipsDestroyedP1T4
			* Amount: 10

### qe_yaoSpr_2024_daily_B_t1
* Type:	Event
* EventId:	event_yaotSpring_2024_t1
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_Container_T1up
			* Amount: 1
			* Analyzed: True

### qe_yaoSpr_2024_daily_B_t2
* Type:	Event
* EventId:	event_yaotSpring_2024_t2
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_Container_T2up
			* Amount: 1
			* Analyzed: True

### qe_yaoSpr_2024_daily_B_t3
* Type:	Event
* EventId:	event_yaotSpring_2024_t3
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_Container_T3up
			* Amount: 1
			* Analyzed: True

### qe_yaoSpr_2024_daily_B_t4
* Type:	Event
* EventId:	event_yaotSpring_2024_t4
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_Container_T4up
			* Amount: 1
			* Analyzed: True

### qe_yaoSpr_2024_daily_C_t1
* Type:	Event
* EventId:	event_yaotSpring_2024_t1
* Goals:
	* 0:
		* GoalType: Pay
			* Id: 1N
			* Amount: 100
		* GoalType: Pay
			* Id: 1O
			* Amount: 100
		* GoalType: Pay
			* Id: 1P
			* Amount: 100

### qe_yaoSpr_2024_daily_C_t2
* Type:	Event
* EventId:	event_yaotSpring_2024_t2
* Goals:
	* 0:
		* GoalType: Pay
			* Id: 2N
			* Amount: 100
		* GoalType: Pay
			* Id: 2O
			* Amount: 100
		* GoalType: Pay
			* Id: 2P
			* Amount: 100

### qe_yaoSpr_2024_daily_C_t3
* Type:	Event
* EventId:	event_yaotSpring_2024_t3
* Goals:
	* 0:
		* GoalType: Pay
			* Id: yao_collectable_u_01
			* Amount: 1

### qe_yaoSpr_2024_daily_C_t4
* Type:	Event
* EventId:	event_yaotSpring_2024_t4
* Goals:
	* 0:
		* GoalType: Pay
			* Id: yao_collectable_u_01
			* Amount: 3

### qe_yaoSpr_2024_daily_D_t1
* Type:	Event
* EventId:	event_yaotSpring_2024_t1
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_Generated_T1up
			* Amount: 5
			* Analyzed: True

### qe_yaoSpr_2024_daily_D_t2
* Type:	Event
* EventId:	event_yaotSpring_2024_t2
* Goals:
	* 0:
		* GoalType: GainItem
			* Id: RP
			* Amount: 400
			* ExcludedSources:
				* SellItem
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_yaoSpr_2024_daily_D_t3
* Type:	Event
* EventId:	event_yaotSpring_2024_t3
* Goals:
	* 0:
		* GoalType: GainItem
			* Id: RP
			* Amount: 400
			* ExcludedSources:
				* SellItem
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_yaoSpr_2024_daily_D_t4
* Type:	Event
* EventId:	event_yaotSpring_2024_t4
* Goals:
	* 0:
		* GoalType: GainItem
			* Id: RP
			* Amount: 400
			* ExcludedSources:
				* SellItem
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

## QL_MAIN_T0_JOLJA
### qm_t0_Jolja
* Type:	Main
* FollowUps: ql_main_t0_setupPlayer
* Goals:
	* 0:
		* GoalType: Goto
			* Target: [-1764, -703]
	* 1:
		* GoalType: Scan
			* Tags: InSystem
			* Amount: 1
	* 2:
		* GoalType: CompleteMission
			* Id: story_A05_Jolja
	* 3:
		* GoalType: Goto
			* Target: [-1822, -636]
			* TargetMode: Station

## QL_MAIN_T0_SETUPPLAYER
### qm_t0_pickKiith
* Type:	Main
* Goals:
	* 0:
		* Type: SelectKiith

### qm_t0_pickName
* Type:	Main
* FollowUps:
	* ql_main_t1_newOres
	* ql_main_t0_joinClan
* Goals:
	* 0:
		* Type: ChangeName

## QL_MAIN_T0_JOINCLAN
### qm_t0_joinClan
* Type:	Main
* Goals:
	* 0:
		* Type: JoinClan

## QL_MAIN_T1_NEWORES
### qm_t1_newOres
* Type:	Main
* FollowUps: ql_esca_mineT1
* Goals:
	* 0:
		* GoalType: Goto
			* Target: [-1793, -424]
	* 1:
		* GoalType: Statistic
			* Id: ScannedBelt
			* Total: 6
	* 2:
		* GoalType: Statistic
			* Ids:
				* Mined1A
				* Mined1B
				* Mined1C
			* Amount: 200

### qm_t1_introRefining
* Type:	Main
* FollowUps:
	* ql_main_t1_sideHiig
	* qm_t1_facHiigaran_A
	* qm_t1_facHiigaran_B
	* qm_t1_facHiigaran_C
	* qm_t1_facHiigaran_D
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* Refining1N
				* Refining1O
				* Refining1P
			* Amount: 100
	* 1:
		* GoalType: Goto
			* Target: [-1822, -636]
			* TargetMode: Station

## QL_MAIN_T1_SIDEHIIG
### qm_t1_facHiigaran
* Type:	Main
* FollowUps: ql_main_t1_strikeCraft
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 3
			* Ids:
				* qm_t1_facHiigaran_A
				* qm_t1_facHiigaran_B
				* qm_t1_facHiigaran_C
				* qm_t1_facHiigaran_D
	* 1:
		* GoalType: Goto
			* Target: [-1822, -636]
			* TargetMode: Station

## QL_MAIN_T1_STRIKECRAFT
### qm_t1_strikeCraft
* Type:	Main
* FollowUps:
	* ql_main_t1_advCombat_01
	* ql_main_t1_RCol
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: Interceptor_T1
			* Amount: 1
		* GoalType: Craft
			* Category: Crafting
			* Tags: PlasmaBomber_T1
			* Amount: 1
	* 1:
		* GoalType: Equip
			* Type: Squad
			* Tags: Interceptor_T1up
		* GoalType: Equip
			* Type: Squad
			* Tags: PlasmaBomber_T1up

## QL_MAIN_T1_RCOL
### qm_t1_RColEquip
* Type:	Main
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: RCol_T1
			* Amount: 1
	* 1:
		* GoalType: Equip
			* Type: Squad
			* Tags: RCol_T1up

### qm_t1_RColMine
* Type:	Main
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* Mined1A
				* Mined1B
				* Mined1C
			* Amount: 4500

## QL_MAIN_T1_ADVCOMBAT_01
### qm_t1_advCombat_01
* Type:	Main
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: story_B01_CombatTrials

### qm_t1_killEnemyShips
* Type:	Main
* FollowUps: ql_main_t1_promoteOfficer
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyed
			* Amount: 25

## QL_MAIN_T1_PROMOTEOFFICER
### qm_t1_introPromoteOfficer
* Type:	Main
* FollowUps: ql_main_t1_escorts
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 1

### qm_t1_rankUpOfficer
* Type:	Side
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 1
			* MinLevel: 10

## QL_MAIN_T1_ESCORTS
### qm_t1_escort
* Type:	Main
* FollowUps: ql_main_t1_advCombat_02
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: AssaultFrigate_T1
			* Amount: 1
	* 1:
		* GoalType: Equip
			* Type: Escort
			* Tags: AssaultFrigate_T1up

## QL_MAIN_T1_ADVCOMBAT_02
### qm_t1_advCombat_02
* Type:	Main
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: story_B02_MeropisDefense

### qm_t1_doSignals
* Type:	Main
* FollowUps:
	* ql_main_t1_sideCang
	* ql_esca_killPirate1
	* qm_t1_facCangacian_A
	* qm_t1_facCangacian_B
	* qm_t1_facCangacian_C
	* qm_t1_facCangacian_D
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Mode: Generated
			* Amount: 1
			* Tier: 1

## QL_MAIN_T1_SIDECANG
### qm_t1_facCangacian
* Type:	Main
* FollowUps: ql_main_t1_flagship
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 3
			* Ids:
				* qm_t1_facCangacian_A
				* qm_t1_facCangacian_B
				* qm_t1_facCangacian_C
				* qm_t1_facCangacian_D
	* 1:
		* GoalType: Goto
			* Target: [-1822, -636]
			* TargetMode: Station

## QL_MAIN_T1_FLAGSHIP
### qm_t1_introCraftFlagship
* Type:	Main
* FollowUps: ql_main_t1_killCangacians
* Goals:
	* 0:
		* GoalType: StartCraft
			* Category: Crafting
			* Tags: Flagship_Ship
			* Amount: 1

### qm_t1_introEquipFlagship
* Type:	Main
* FollowUps: ql_main_t1_advCombat_03
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: Flagship_Ship
			* Amount: 1
	* 1:
		* GoalType: Equip
			* Type: Flagship
	* 2:
		* GoalType: Equip
			* Type: Squad
		* GoalType: Equip
			* Type: Escort
		* GoalType: Equip
			* Type: Officer
			* Location: Bridge

## QL_MAIN_T1_KILLCANGACIANS
### qm_t1_killCangacians
* Type:	Side
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedP1
			* Amount: 20

## QL_MAIN_T1_ADVCOMBAT_03
### qm_t1_advCombat_03
* Type:	Main
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: story_B03_ThePool

### qm_t1_killProgenitors
* Type:	Main
* FollowUps: ql_main_t1_turrets
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedProgenitor
			* Amount: 10

## QL_MAIN_T1_TURRETS
### qm_t1_craftTurret
* Type:	Main
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: Weapon_Module_T1
			* Amount: 1

### qm_t1_mountTurret
* Type:	Main
* FollowUps: ql_main_t1_upgrades
* Goals:
	* 0:
		* GoalType: Equip
			* Type: Weapon

## QL_MAIN_T1_UPGRADES
### qm_t1_rareEarths
* Type:	Main
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: RareEarth
			* Amount: 5
			* ExcludedSources:
				* SellItem
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qm_t1_upgradeTurret
* Type:	Main
* FollowUps:
	* ql_main_t1_sideProg
	* qm_t1_facProgenitors_A
	* qm_t1_facProgenitors_B
	* qm_t1_facProgenitors_C
	* qm_t1_facProgenitors_D
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Upgrade
			* Tags: Weapon_Module
			* Amount: 1

### qm_t1_upgradeTurret_3
* Type:	Side
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Upgrade
			* Tags: Weapon_Module
			* Amount: 1
			* MinLevel: 3

### qm_t1_upgradeTurret_4
* Type:	Side
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Upgrade
			* Tags: Weapon_Module
			* Amount: 1
			* MinLevel: 4

### qm_t1_upgradeTurret_5
* Type:	Side
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Upgrade
			* Tags: Weapon_Module
			* Amount: 1
			* MinLevel: 5

### qm_t1_upgradeTurret_6
* Type:	Side
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Upgrade
			* Tags: Weapon_Module
			* Amount: 1
			* MinLevel: 6

### qm_t1_upgradeTurret_7
* Type:	Side
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Upgrade
			* Tags: Weapon_Module
			* Amount: 1
			* MinLevel: 7

### qm_t1_upgradeTurret_8
* Type:	Side
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Upgrade
			* Tags: Weapon_Module
			* Amount: 1
			* MinLevel: 8

### qm_t1_upgradeTurretMax
* Type:	Side
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Upgrade
			* Tags: Weapon_Module
			* Amount: 1
			* MinLevel: 9

## QL_MAIN_T1_SIDEPROG
### qm_t1_facProgenitors
* Type:	Main
* FollowUps: ql_main_t1_scanner
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 3
			* Ids:
				* qm_t1_facProgenitors_A
				* qm_t1_facProgenitors_B
				* qm_t1_facProgenitors_C
				* qm_t1_facProgenitors_D
	* 1:
		* GoalType: Goto
			* Target: [-1822, -636]
			* TargetMode: Station

## QL_MAIN_T1_SCANNER
### qm_t1_scannerModule
* Type:	Main
* FollowUps:
	* ql_main_t2_strike
	* ql_esca_scan
	* ql_main_t1_scannerCharge
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: Sensor_Module_T1
			* Amount: 1
	* 1:
		* GoalType: Equip
			* Type: Sensor
			* Tags: T1up

## QL_MAIN_T1_SCANNERCHARGE
### qm_t1_scannerOvercharge
* Type:	Side
* Goals:
	* 0:
		* GoalType: ChargeScanner
			* NewCharge: 1.25
	* 1:
		* GoalType: Scan
			* Tags: InSystem_Rare
			* Amount: 1

## QL_MAIN_T2_STRIKE
### qm_t2_findPirateHideout
* Type:	Main
* FollowUps:
	* ql_raid_013
	* ql_main_t1_upgradeExternals
	* ql_main_t1_introLiaison
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InGalaxy_T1up
			* Amount: 1
			* Analyzed: True
		* GoalType: Goto
			* Target: [-1793, -424]

### qm_t2_strikePirateHideout
* Type:	Main
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Ids:
				* qr
				* 013
			* Amount: 1

## QL_MAIN_T1_UPGRADEEXTERNALS
### qm_t1_upgradeModules
* Type:	Main
* FollowUps: ql_main_t1_introInternals
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Upgrade
			* Tags: Sensor
			* Amount: 1
			* MinLevel: 5
		* GoalType: Craft
			* Category: Upgrade
			* Tags: Engine
			* Amount: 1
			* MinLevel: 5

## QL_MAIN_T1_INTROLIAISON
### qm_t1_introLiaison
* Type:	Side
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 3
			* Tags: Faction

## QL_MAIN_T1_INTROINTERNALS
### qm_t1_introInternals
* Type:	Main
* Goals:
	* 0:
		* GoalType: Craft
			* Tags: Crafting_Factory
	* 1:
		* GoalType: Equip
			* Type: Internal
			* Tags: Crafting_Factory

### qm_t1_upgradeInternals
* Type:	Main
* FollowUps:
	* ql_main_t1_sideIyat
	* qm_t1_facIyatequa_A
	* qm_t1_facIyatequa_B
	* qm_t1_facIyatequa_C
	* qm_t1_facIyatequa_D
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Upgrade
			* Tags: Factory
			* MinLevel: 2

## QL_MAIN_T1_SIDEIYAT
### qm_t1_facIyatequa
* Type:	Main
* FollowUps: ql_main_t2_research
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 3
			* Ids:
				* qm_t1_facIyatequa_A
				* qm_t1_facIyatequa_B
				* qm_t1_facIyatequa_C
				* qm_t1_facIyatequa_D
	* 1:
		* GoalType: Goto
			* Target: [-1822, -636]
			* TargetMode: Station

## QL_MAIN_T2_RESEARCH
### qm_t2_introRP
* Type:	Main
* Goals:
	* 0:
		* GoalType: GainItem
			* Id: RP
			* Amount: 15
			* ExcludedSources:
				* SellItem
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qm_t2_introResearch
* Type:	Main
* FollowUps: ql_main_t2_newResources
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Research
			* Id: rp_catExpl_hyperCap_t2_c
			* Tags: T2

## QL_MAIN_T2_NEWRESOURCES
### qm_t2_newResources
* Type:	Main
* FollowUps:
	* ql_main_t2_sideCang
	* qm_t2_facCangacian_A
	* qm_t2_facCangacian_B
	* qm_t2_facCangacian_C
	* qm_t2_facCangacian_D
* Goals:
	* 0:
		* GoalType: Goto
			* Target: [-1491, -596]
	* 1:
		* GoalType: Statistic
			* Id: ScannedBelt
			* Total: 25
	* 2:
		* GoalType: Statistic
			* Ids:
				* Mined2A
				* Mined2B
				* Mined2C
				* Mined2D
			* Amount: 3000
	* 3:
		* GoalType: Craft
			* Category: Refining
			* Amount: 1500
			* Tags: T2
	* 4:
		* GoalType: Goto
			* Target: [-1822, -636]
			* TargetMode: Station

## QL_MAIN_T2_SIDECANG
### qm_t2_facCangacian
* Type:	Main
* FollowUps: ql_main_t2_strikeCraftResearch
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 3
			* Ids:
				* qm_t2_facCangacian_A
				* qm_t2_facCangacian_B
				* qm_t2_facCangacian_C
				* qm_t2_facCangacian_D
	* 1:
		* GoalType: Goto
			* Target: [-1822, -636]
			* TargetMode: Station

## QL_MAIN_T2_STRIKECRAFTRESEARCH
### qm_t2_startResearchT2Intc
* Type:	Main
* FollowUps: ql_main_t2_strikeCraftCraft
* Goals:
	* 0:
		* GoalType: StartCraft
			* Category: Research
			* Id: rp_catStrCraft_bp_sf_intc_t2_c

### qm_t2_finResearchT2Intc
* Type:	Main
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Research
			* Id: rp_catStrCraft_bp_sf_intc_t2_c

## QL_MAIN_T2_STRIKECRAFTCRAFT
### qm_t2_introParts
* Type:	Main
* Goals:
	* 0:
		* GoalType: Buy
			* Id: bp_intmed_ship_small_t2
	* 1:
		* GoalType: Craft
			* Tags: Part_Ship_S_T2
			* Amount: 400
			* Category: Crafting

### qm_t2_strikeCraft
* Type:	Main
* FollowUps:
	* ql_main_t2_sideHiig
	* ql_main_t2_RCol
	* ql_raid_016
	* qm_t2_facHiigaran_A
	* qm_t2_facHiigaran_B
	* qm_t2_facHiigaran_C
	* qm_t2_facHiigaran_D
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Ids:
				* qm
				* t2
				* finResearchT2Intc
			* Amount: 1
	* 1:
		* GoalType: Craft
			* Category: Crafting
			* Tags: Interceptor_T2
			* Amount: 1

## QL_MAIN_T2_SIDEHIIG
### qm_t2_facHiigaran
* Type:	Main
* FollowUps: ql_main_t2_researchEscort
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 3
			* Ids:
				* qm_t2_facHiigaran_A
				* qm_t2_facHiigaran_B
				* qm_t2_facHiigaran_C
				* qm_t2_facHiigaran_D

## QL_MAIN_T2_RCOL
### qm_t2_craftRCol
* Type:	Side
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: RCol_T2
			* Amount: 1

### qm_t2_RColMining
* Type:	Side
* FollowUps: ql_main_t2_RCon
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* Mined2A
				* Mined2B
				* Mined2C
				* Mined2D
			* Amount: 9000

## QL_MAIN_T2_RCON
### qm_t2_craftRCon
* Type:	Side
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: RCon
			* Amount: 1

### qm_t2_introIdleMine
* Type:	Side
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* Mined2A
				* Mined2B
				* Mined2C
				* Mined2D
			* Amount: 5000

## QL_MAIN_T2_RESEARCHESCORT
### qm_t2_startResearchT2Frig
* Type:	Main
* FollowUps: ql_main_t2_oreD
* Goals:
	* 0:
		* GoalType: StartCraft
			* Category: Research
			* Id: rp_catEscorts_bp_cf_assa_t2_c

### qm_t2_finResearchT2Frig
* Type:	Main
* FollowUps:
	* ql_main_t2_craftEscort
	* ql_main_t2_researchPulsarCorvette
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Research
			* Id: rp_catEscorts_bp_cf_assa_t2_c

## QL_MAIN_T2_ORED
### qm_t2_introOreD
* Type:	Side
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: Mined2D
			* Amount: 3500
	* 1:
		* GoalType: Craft
			* Category: Refining
			* Amount: 1500
			* Id: 2Q

### qm_t2_craftUncShip
* Type:	Side
* Goals:
	* 0:
		* GoalType: Craft
			* Id: hgn_sf_intc_01_u_t2

## QL_MAIN_T2_RESEARCHPULSARCORVETTE
### qm_t2_researchPulsarCorvette
* Type:	Side
* FollowUps: ql_main_t2_pulsarCorvette
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Research
			* Id: rp_catStrCraft_bp_sc_puls_t2_c
			* MinLevel: 1

## QL_MAIN_T2_PULSARCORVETTE
### qm_t2_pulsarCorvette
* Type:	Side
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: PulsarCorvette_T2
			* Amount: 1

## QL_MAIN_T2_CRAFTESCORT
### qm_t2_largeHullParts
* Type:	Main
* Goals:
	* 0:
		* GoalType: Buy
			* Id: bp_intmed_ship_large_t2
	* 1:
		* GoalType: Craft
			* Tags: Part_Ship_L_T2
			* Amount: 400
			* Category: Crafting

### qm_t2_escort
* Type:	Main
* FollowUps:
	* ql_main_t2_introLiaison
	* ql_main_t2_strikeStationDefense
	* ql_raid_014
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: AssaultFrigate_T2
			* Amount: 1

## QL_MAIN_T2_INTROLIAISON
### qm_t2_introLiaison
* Type:	Main
* FollowUps:
	* ql_main_t2_sideIyat
	* qm_t2_facIyatequa_A
	* qm_t2_facIyatequa_B
	* qm_t2_facIyatequa_C
	* qm_t2_facIyatequa_D
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 3
			* Tags: Faction

## QL_MAIN_T2_SIDEIYAT
### qm_t2_facIyatequa
* Type:	Main
* FollowUps:
	* ql_main_t2_largeWpnParts
	* ql_main_t2_largeMchParts
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 3
			* Ids:
				* qm_t2_facIyatequa_A
				* qm_t2_facIyatequa_B
				* qm_t2_facIyatequa_C
				* qm_t2_facIyatequa_D
	* 1:
		* GoalType: Goto
			* Target: [-1822, -636]
			* TargetMode: Station

## QL_MAIN_T2_STRIKESTATIONDEFENSE
### qm_t2_strikeStationDefense
* Type:	Side
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Ids:
				* qr
				* 014
			* Amount: 1

## QL_MAIN_T2_LARGEWPNPARTS
### qm_t2_liaisonTanoch
* Type:	Main
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 10
			* Tags: Faction_Tanoch_T2up

### qm_t2_largeWeaponParts
* Type:	Main
* FollowUps: ql_main_t2_flagship
* Goals:
	* 0:
		* GoalType: Craft
			* Tags: Part_Weapon_L_T2
			* Amount: 100
			* Category: Crafting

## QL_MAIN_T2_LARGEMCHPARTS
### qm_t2_liaisonIyatequa
* Type:	Main
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 10
			* Tags: Faction_Tr1_T2up

### qm_t2_largeMachineParts
* Type:	Main
* FollowUps: ql_main_t2_flagship
* Goals:
	* 0:
		* GoalType: Craft
			* Tags: Part_Module_L_T2
			* Amount: 100
			* Category: Crafting

## QL_MAIN_T2_FLAGSHIP
### qm_t2_startCraftFlagship
* Type:	Main
* FollowUps:
	* ql_Keid
	* ql_main_t2_strikePahrasRock
	* ql_raid_015
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 2
			* Ids:
				* qm_t2_largeWeaponParts
				* qm_t2_largeMachineParts
	* 1:
		* GoalType: StartCraft
			* Category: Crafting
			* Tags: Flagship_Ship_T2

### qm_t2_finCraftFlagship
* Type:	Main
* FollowUps:
	* ql_main_t2_tanochet
	* ql_main_t2_turrets
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: Flagship_Ship_T2

## QL_MAIN_T2_STRIKEPAHRASROCK
### qm_t2_strikePahrasRock
* Type:	Side
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Ids:
				* qr
				* 015
			* Amount: 1

## QL_MAIN_T2_TURRETS
### qm_t2_turrets
* Type:	Side
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Research
			* Id: rp_catTurrets1_bp_kinetic_t2_c
	* 1:
		* GoalType: Craft
			* Category: Crafting
			* Tags: Weapon_Module_T2
			* Amount: 1
	* 2:
		* GoalType: Equip
			* Type: Weapon
			* Tags: T2up

## QL_MAIN_T2_TANOCHET
### qm_t2_tanochet
* Type:	Main
* CinematicIds:	30
* FollowUps:
	* ql_main_t2_sideTano
	* ql_main_t2_epicSignals
	* qm_t2_facTanoch_A
	* qm_t2_facTanoch_B
	* qm_t2_facTanoch_C
	* qm_t2_facTanoch_D
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: story_C01_Tanochet

## QL_MAIN_T2_INTERNALS
### qm_t2_internalFabricator
* Type:	Main
* Goals:
	* 0:
		* GoalType: Craft
			* Tags: Crafting_Factory
	* 1:
		* GoalType: Equip
			* Type: Internal
			* Tags: Crafting_Factory

## QL_MAIN_T2_EPICSIGNALS
### qm_t2_epicSignals
* Type:	Side
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InGalaxy_T2up
			* Amount: 1
			* Analyzed: True
		* GoalType: CompleteMission
			* Mode: Generated
			* Tags: Epic_T2up
			* Amount: 1

## QL_MAIN_T2_SIDETANO
### qm_t2_facTanoch
* Type:	Main
* FollowUps:
	* ql_main_t2_sideYaot
	* ql_main_t2_compartments
	* qm_t2_facYaot_A
	* qm_t2_facYaot_B
	* qm_t2_facYaot_C
	* qm_t2_facYaot_D
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 3
			* Ids:
				* qm_t2_facTanoch_A
				* qm_t2_facTanoch_B
				* qm_t2_facTanoch_C
				* qm_t2_facTanoch_D
	* 1:
		* GoalType: Goto
			* Target: [-1240, -410]

## QL_MAIN_T2_UPGRADEINTERNALS
### qm_t2_upgradeInternals
* Type:	Main
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Upgrade
			* Tags: Factory
			* Amount: 2
			* MinLevel: 5

### qm_t2_otherInternals
* Type:	Side
* Goals:
	* 0:
		* GoalType: Equip
			* Type: Internal
			* Tags: Front
		* GoalType: Equip
			* Type: Internal
			* Tags: Back

## QL_MAIN_T2_COMPARTMENTS
### qm_t2_compartments
* Type:	Side
* Goals:
	* 0:
		* GoalType: Equip
			* Type: Internal
			* Tags: Front
		* GoalType: Equip
			* Type: Internal
			* Tags: Back

## QL_MAIN_T2_SIDEYAOT
### qm_t2_facYaot
* Type:	Main
* FollowUps: ql_main_t2_templeTonaati
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 3
			* Ids:
				* qm_t2_facYaot_A
				* qm_t2_facYaot_B
				* qm_t2_facYaot_C
				* qm_t2_facYaot_D
	* 1:
		* GoalType: Goto
			* Target: [-1240, -410]

## QL_MAIN_T2_TEMPLETONAATI
### qm_t2_templeTonaati
* Type:	Main
* FollowUps:
	* ql_Exile
	* ql_side_exploration
	* ql_main_t3_jumpCap
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: story_C02_TempleTonaati

## QL_MAIN_T3_JUMPCAP
### qm_t3_researchJumpCap
* Type:	Main
* FollowUps: ql_main_t3_intro
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Research
			* Id: rp_catExpl_hyperCap_t3_c
			* MinLevel: 1

## QL_MAIN_T3_INTRO
### qm_t3_scouting
* Type:	Main
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Upgrade
			* Tags: Engine
			* Amount: 1
			* MinLevel: 6
		* GoalType: Craft
			* Category: Upgrade
			* Tags: Sensor
			* Amount: 1
			* MinLevel: 6

### qm_t3_scouting_scanBelts
* Type:	Main
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ScannedBelt
			* Total: 55

### qm_t3_scouting_scanJovian
* Type:	Main
* FollowUps:
	* ql_main_t3_gasMining
	* ql_main_t3_yaotLiaison
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ScannedJovian
			* Total: 1

## QL_MAIN_T3_GASMINING
### qm_t3_gasMining
* Type:	Main
* FollowUps:
	* ql_main_t3_sideYaot
	* ql_main_t3_sideYaot_A
	* ql_main_t3_sideYaot_B
	* ql_main_t3_sideYaot_C
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: GCol
			* Amount: 1
	* 1:
		* GoalType: Statistic
			* Ids:
				* Mined3E
				* Mined3F
				* Mined3G
				* Mined3H
			* Amount: 1000

## QL_MAIN_T3_YAOTLIAISON
### qm_t3_yaotLiaison
* Type:	Side
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: RepYaot
			* Total: 1000

## QL_MAIN_T3_SIDEYAOT
### qm_t3_facYaot
* Type:	Main
* FollowUps:
	* ql_raid_017
	* ql_main_t3_sideTanoch
	* ql_main_t3_sideTanoch_A
	* ql_main_t3_sideTanoch_B
	* ql_main_t3_sideTanoch_C
	* ql_orb_t3_intro
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 2
			* Ids:
				* qm_t3_sideYaot_A_3
				* qm_t3_sideYaot_B_3
				* qm_t3_sideYaot_C_3
	* 1:
		* GoalType: Goto
			* Target: [-942, -820]

## QL_MAIN_T3_SIDEYAOT_A
### qm_t3_sideYaot_A_1
* Type:	Side
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ScannedBelt
			* Total: 65
		* GoalType: Pay
			* Id: 3O
			* Amount: 50

### qm_t3_sideYaot_A_2
* Type:	Side
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: Mined3C
			* Amount: 2500
		* GoalType: Statistic
			* Id: ShipsDestroyed
			* Amount: 30

### qm_t3_sideYaot_A_3
* Type:	Side
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: Refining3N
			* Amount: 300
		* GoalType: Pay
			* Id: 3N
			* Amount: 100

## QL_MAIN_T3_SIDEYAOT_B
### qm_t3_sideYaot_B_1
* Type:	Side
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_Generated_T3up
			* Amount: 5
			* Analyzed: True
		* GoalType: CompleteMission
			* Amount: 6
			* Tags: T2up
			* Mode: Generated

### qm_t3_sideYaot_B_2
* Type:	Side
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyed
			* Amount: 30
		* GoalType: GainItem
			* Tags: Insignia
			* Amount: 50
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qm_t3_sideYaot_B_3
* Type:	Side
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T2up
			* Mode: Strike

## QL_MAIN_T3_SIDEYAOT_C
### qm_t3_sideYaot_C_1
* Type:	Side
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: Faction_Yaot_T3up

### qm_t3_sideYaot_C_2
* Type:	Side
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: RepYaot
			* Amount: 250
		* GoalType: Statistic
			* Id: ShipsDestroyed
			* Amount: 30

### qm_t3_sideYaot_C_3
* Type:	Side
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Insignia
			* Amount: 65
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
		* GoalType: Statistic
			* Id: RepYaot
			* Total: 4050

## QL_MAIN_T3_SIDETANOCH
### qm_t3_facTanoch
* Type:	Main
* FollowUps:
	* ql_raid_018
	* ql_main_t3_starTotek
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 2
			* Ids:
				* qm_t3_sideTanoch_A_3
				* qm_t3_sideTanoch_B_3
				* qm_t3_sideTanoch_C_3
	* 1:
		* GoalType: Goto
			* Target: [-1240, -410]

## QL_MAIN_T3_SIDETANOCH_A
### qm_t3_sideTanoch_A_1
* Type:	Side
* Goals:
	* 0:
		* GoalType: Pay
			* Id: 3A
			* Amount: 400
		* GoalType: Pay
			* Id: 3B
			* Amount: 200
		* GoalType: Pay
			* Id: 3C
			* Amount: 1400

### qm_t3_sideTanoch_A_2
* Type:	Side
* Goals:
	* 0:
		* GoalType: Pay
			* Id: intmed_module_large_t2
			* Amount: 15

### qm_t3_sideTanoch_A_3
* Type:	Side
* Goals:
	* 0:
		* GoalType: Pay
			* Id: intmed_ship_small_t3
			* Amount: 50
		* GoalType: Pay
			* Id: intmed_weapon_small_t3
			* Amount: 50
	* 1:
		* GoalType: CompleteMission
			* Amount: 5

## QL_MAIN_T3_SIDETANOCH_B
### qm_t3_sideTanoch_B_1
* Type:	Side
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_T3up
			* Amount: 6
			* Analyzed: True
		* GoalType: Statistic
			* Id: ShipsDestroyed
			* Amount: 35

### qm_t3_sideTanoch_B_2
* Type:	Side
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 7
		* GoalType: Statistic
			* Id: ShipsDestroyedP1
			* Amount: 25

### qm_t3_sideTanoch_B_3
* Type:	Side
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T2up
			* Mode: Strike
		* GoalType: GainItem
			* Tags: StrikeToken
			* Amount: 6
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

## QL_MAIN_T3_SIDETANOCH_C
### qm_t3_sideTanoch_C_1
* Type:	Side
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: RepTanoch
			* Amount: 500

### qm_t3_sideTanoch_C_2
* Type:	Side
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 15
		* GoalType: CompleteQuest
			* Amount: 7
			* Tags: Faction_Tanoch_T2up

### qm_t3_sideTanoch_C_3
* Type:	Side
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: RepTanoch
			* Total: 8500
		* GoalType: Statistic
			* Ids:
				* Refining3N
				* Refining3O
				* Refining3P
				* Refining3Q
			* Amount: 600

## QL_MAIN_T3_STARTOTEK
### qm_t3_starTotek
* Type:	Main
* FollowUps:
	* ql_main_t3_sideHiig
	* ql_main_t3_sideHiig_A
	* ql_main_t3_sideHiig_B
	* ql_main_t3_sideHiig_C
	* ql_main_t3_strikeBreach
	* ql_raid_019
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: story_C03_StarTotek

## QL_MAIN_T3_STRIKEBREACH
### qm_t3_strikeBreach
* Type:	Side
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Ids:
				* qr
				* 019
			* Amount: 1

## QL_MAIN_T3_SIDEHIIG
### qm_t3_facHiigaran
* Type:	Main
* FollowUps:
	* ql_main_t3_sideIyat
	* ql_main_t3_sideIyat_A
	* ql_main_t3_sideIyat_B
	* ql_main_t3_sideIyat_C
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 2
			* Ids:
				* qm_t3_sideHiigaran_A_3
				* qm_t3_sideHiigaran_B_3
				* qm_t3_sideHiigaran_C_3
	* 1:
		* GoalType: Goto
			* Target: [-1822, -636]

## QL_MAIN_T3_SIDEHIIG_A
### qm_t3_sideHiigaran_A_1
* Type:	Side
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ScannedJovian
			* Total: 20
		* GoalType: Statistic
			* Ids:
				* Mined3E
				* Mined3F
				* Mined3G
				* Mined3H
			* Amount: 600

### qm_t3_sideHiigaran_A_2
* Type:	Side
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* Mined3A
				* Mined3B
				* Mined3C
				* Mined3D
			* Amount: 5000
		* GoalType: GainItem
			* Id: RP
			* Amount: 35
			* ExcludedSources:
				* SellItem
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qm_t3_sideHiigaran_A_3
* Type:	Side
* Goals:
	* 0:
		* GoalType: Pay
			* Id: 3G
			* Amount: 100
		* GoalType: Pay
			* Id: 3O
			* Amount: 200
		* GoalType: Pay
			* Id: intmed_ship_small_t3
			* Amount: 40

## QL_MAIN_T3_SIDEHIIG_B
### qm_t3_sideHiigaran_B_1
* Type:	Side
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedP1
			* Amount: 30
		* GoalType: GainItem
			* Tags: Insignia
			* Amount: 40
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qm_t3_sideHiigaran_B_2
* Type:	Side
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_Generated_T3up
			* Amount: 7
			* Analyzed: True
		* GoalType: CompleteMission
			* Amount: 5
			* Tags: T3up
			* Mode: Generated

### qm_t3_sideHiigaran_B_3
* Type:	Side
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedProgenitor
			* Amount: 15
		* GoalType: GainItem
			* Id: RP
			* Amount: 45
			* ExcludedSources:
				* SellItem
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

## QL_MAIN_T3_SIDEHIIG_C
### qm_t3_sideHiigaran_C_1
* Type:	Side
* Goals:
	* 0:
		* GoalType: GainItem
			* Id: LP
			* Amount: 12
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
		* GoalType: Statistic
			* Id: PlayerXP
			* Amount: 2000

### qm_t3_sideHiigaran_C_2
* Type:	Side
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: Ship_Unit_T3up
			* Amount: 5
		* GoalType: UpgradeOfficer
			* Amount: 20

### qm_t3_sideHiigaran_C_3
* Type:	Side
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 10
	* 1:
		* GoalType: UpgradeOfficer
			* Amount: 5
			* MinLevel: 20

## QL_MAIN_T3_SIDEIYAT
### qm_t3_facIyatequa
* Type:	Main
* FollowUps:
	* ql_main_t3_Cang
	* ql_main_t3_Cang_A
	* ql_main_t3_Cang_B
	* ql_main_t3_Cang_C
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 2
			* Ids:
				* qm_t3_sideIyatequa_A_3
				* qm_t3_sideIyatequa_B_3
				* qm_t3_sideIyatequa_C_3
	* 1:
		* GoalType: Goto
			* Target: [-1543, -626]

## QL_MAIN_T3_SIDEIYAT_A
### qm_t3_sideIyatequa_A_1
* Type:	Side
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 7
			* Tags: Faction_Tr1_T3up
		* GoalType: Statistic
			* Id: PlayerXP
			* Amount: 2250

### qm_t3_sideIyatequa_A_2
* Type:	Side
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: RepTr1
			* Amount: 500
		* GoalType: Statistic
			* Ids:
				* Refining3N
				* Refining3O
				* Refining3P
				* Refining3Q
			* Amount: 1000

### qm_t3_sideIyatequa_A_3
* Type:	Side
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: RepTr1
			* Total: 8500
		* GoalType: Scan
			* Tags: InGalaxy_T3up
			* Amount: 5
			* Analyzed: True

## QL_MAIN_T3_SIDEIYAT_B
### qm_t3_sideIyatequa_B_1
* Type:	Side
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_Generated_T3up
			* Amount: 8
			* Analyzed: True
		* GoalType: Statistic
			* Id: ShipsDestroyedP1
			* Amount: 35

### qm_t3_sideIyatequa_B_2
* Type:	Side
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 8
			* Tags: T3up
			* Mode: Generated
		* GoalType: GainItem
			* Tags: Insignia
			* Amount: 60
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qm_t3_sideIyatequa_B_3
* Type:	Side
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 5
			* Tags: T2up
			* Mode: Strike
		* GoalType: CompleteMission
			* Amount: 2
			* Tags: T3up
			* Mode: Strike

## QL_MAIN_T3_SIDEIYAT_C
### qm_t3_sideIyatequa_C_1
* Type:	Side
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* Mined3A
				* Mined3B
				* Mined3C
				* Mined3D
			* Amount: 6000
		* GoalType: Statistic
			* Id: ShipsDestroyed
			* Amount: 55

### qm_t3_sideIyatequa_C_2
* Type:	Side
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* Mined3E
				* Mined3F
				* Mined3G
				* Mined3H
			* Amount: 600
		* GoalType: Statistic
			* Id: Mined3H
			* Amount: 100

### qm_t3_sideIyatequa_C_3
* Type:	Side
* Goals:
	* 0:
		* GoalType: Pay
			* Id: 3G
			* Amount: 150
		* GoalType: Pay
			* Id: 3O
			* Amount: 300
		* GoalType: Pay
			* Id: intmed_ship_small_t3
			* Amount: 50

## QL_MAIN_T3_CANG
### qm_t3_facCangacian
* Type:	Main
* FollowUps: ql_main_t3_sijinLighthouse
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 2
			* Ids:
				* qm_t3_sideCangacian_A_3
				* qm_t3_sideCangacian_B_3
				* qm_t3_sideCangacian_C_3

## QL_MAIN_T3_CANG_A
### qm_t3_sideCangacian_A_1
* Type:	Side
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedP1
			* Amount: 40
		* GoalType: GainItem
			* Id: LP
			* Amount: 12
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qm_t3_sideCangacian_A_2
* Type:	Side
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_Generated_T3up
			* Amount: 9
			* Analyzed: True
		* GoalType: CompleteMission
			* Amount: 9
			* Tags: T3up
			* Mode: Generated

### qm_t3_sideCangacian_A_3
* Type:	Side
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 4
			* Tags: T3up
			* Mode: Strike
		* GoalType: Scan
			* Tags: InGalaxy_T3up
			* Amount: 10
			* Analyzed: True

## QL_MAIN_T3_CANG_B
### qm_t3_sideCangacian_B_1
* Type:	Side
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Insignia
			* Amount: 80
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
		* GoalType: UpgradeOfficer
			* Amount: 25

### qm_t3_sideCangacian_B_2
* Type:	Side
* Goals:
	* 0:
		* GoalType: GainItem
			* Id: RP
			* Amount: 50
			* ExcludedSources:
				* SellItem
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
		* GoalType: Statistic
			* Id: PlayerXP
			* Amount: 2500

### qm_t3_sideCangacian_B_3
* Type:	Side
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 10
	* 1:
		* GoalType: UpgradeOfficer
			* Amount: 5
			* MinLevel: 25

## QL_MAIN_T3_CANG_C
### qm_t3_sideCangacian_C_1
* Type:	Side
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ScannedBelt
			* Total: 80
		* GoalType: Statistic
			* Ids:
				* Refining3N
				* Refining3O
				* Refining3P
				* Refining3Q
			* Amount: 1500

### qm_t3_sideCangacian_C_2
* Type:	Side
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ScannedJovian
			* Total: 40
		* GoalType: Statistic
			* Ids:
				* Mined3E
				* Mined3F
				* Mined3G
				* Mined3H
			* Amount: 750

### qm_t3_sideCangacian_C_3
* Type:	Side
* Goals:
	* 0:
		* GoalType: Pay
			* Id: intmed_ship_small_t3
			* Amount: 20
		* GoalType: Pay
			* Id: intmed_weapon_small_t3
			* Amount: 20
		* GoalType: Pay
			* Id: intmed_module_small_t3
			* Amount: 20

## QL_MAIN_T3_SIJINLIGHTHOUSE
### qm_t3_sijinLighthouse
* Type:	Main
* CinematicIds:	40
* FollowUps: ql_main_t4_intro
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: story_D01_SijinLighthouse

## QL_MAIN_T4_INTRO
### qm_t4_researchJumpCap
* Type:	Main
* FollowUps: ql_main_t4_iliyinLighthouse
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Research
			* Id: rp_catExpl_hyperCap_t4_c
			* MinLevel: 1

## QL_MAIN_T4_ILIYINLIGHTHOUSE
### qm_t4_iliyinLighthouse
* Type:	Main
* FollowUps:
	* ql_raid_020
	* ql_raid_021
	* ql_raid_022
	* ql_main_t4_amassariLiaison
	* ql_main_t4_moonResources
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: story_D02_IliyinLighthouse

## QL_MAIN_T4_AMASSARILIAISON
### qm_t4_amassariLiaison
* Type:	Side
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: RepAmassari
			* Total: 1000

## QL_MAIN_T4_MOONRESOURCES
### qm_t4_moonResources
* Type:	Main
* FollowUps: ql_main_t4_brightTemple
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Moon_Crud
			* Amount: 200
			* ExcludedSources:
				* PayGoal
				* BuyItem
				* SellItem
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
	* 1:
		* GoalType: Statistic
			* Ids:
				* Refining4V
				* Refining4W
				* Refining4X
				* Refining4Y
			* Amount: 100

## QL_MAIN_T4_BRIGHTTEMPLE
### qm_t4_brightTemple
* Type:	Main
* FollowUps: ql_main_t4_postBrightTemple
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: story_D03_BrightTemple

## QL_MAIN_T4_POSTBRIGHTTEMPLE
### qm_t4_postBrightTemple_1
* Type:	Main
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: RepAmassari
			* Amount: 1000

### qm_t4_postBrightTemple_2
* Type:	Main
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: RareEarth_T4up
			* Amount: 300
			* ExcludedSources:
				* SellItem
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qm_t4_postBrightTemple_3
* Type:	Main
* FollowUps: ql_main_t4_hataldan
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Insignia
			* Amount: 600
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

## QL_MAIN_T4_HATALDAN
### qm_t4_hataldan
* Type:	Main
* FollowUps: ql_main_t4_postHataldan
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: story_D04_Hataldan

## QL_MAIN_T4_POSTHATALDAN
### qm_t4_postHataldan_1
* Type:	Main
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_Container_T4up
			* Amount: 10
			* Analyzed: True

### qm_t4_postHataldan_2
* Type:	Main
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
			* Amount: 50

### qm_t4_postHataldan_3
* Type:	Main
* FollowUps: ql_main_t4_nightmareGulf
* Goals:
	* 0:
		* GoalType: GainItem
			* Id: ama_collectable_u_01
			* Amount: 15
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

## QL_MAIN_T4_NIGHTMAREGULF
### qm_t4_nightmareGulf
* Type:	Main
* FollowUps:
	* ql_raid_023
	* ql_main_t4_strikeNightmareGulf
	* ql_main_t4_tanWin
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: story_D05_NightmareGulf

## QL_MAIN_T4_STRIKENIGHTMAREGULF
### qm_t4_strikeNightmareGulf
* Type:	Side
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Ids:
				* qr
				* 023
			* Amount: 1

## QL_MAIN_T4_TANWIN
### qm_t4_tanWin_DefendBase
* Type:	Main
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_tanWin2023_DefendBase_t4

### qm_t4_tanWin_AttackBase
* Type:	Main
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_tanWin2023_AttackBase_t4

### qm_t4_tanWin_Relic
* Type:	Main
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_tanWin2023_Relic_t4

### qm_t4_tanWin_Academy
* Type:	Main
* FollowUps: ql_main_t4_yaoSpr
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_tanWin2023_Academy_t4

## QL_MAIN_T4_YAOSPR
### qm_t4_yaoSpr_Conjunction
* Type:	Main
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_yaoSpr2024_Conjunction_t4

## QL_ORB_T3_INTRO
### qm_orb_t3_components
* Type:	Side
* Goals:
	* 0:
		* GoalType: Craft
			* Id: playerOrb_comp_stabilizer_t3
		* GoalType: Craft
			* Id: playerOrb_comp_frame_t3
		* GoalType: Craft
			* Id: playerOrb_comp_lifeSupport_t3

### qm_orb_t3_orbital
* Type:	Side
* Goals:
	* 0:
		* GoalType: Craft
			* Id: hgn_co_orbi_01_t1

### qm_orb_t3_placeOrbital
* Type:	Side
* Goals:
	* 0:
		* GoalType: PlaceOrbital
			* NoParameter: None

### qm_orb_t3_modules
* Type:	Side
* Goals:
	* 0:
		* GoalType: Equip
			* Type: Internal
			* Tags: Orbital
			* Target: hgn_co_orbi_01_t1

## QL_SIDE_EXPLORATION
### qs_exploration_01
* Type:	Side
* FollowUps: ql_side_001
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem
			* Amount: 15
			* Analyzed: True
		* GoalType: CompleteMission
			* Amount: 10
			* Tier: 2
			* Mode: Generated

### qs_exploration_02
* Type:	Side
* FollowUps: ql_side_002
* Goals:
	* 0:
		* GoalType: GainItem
			* Id: RP
			* Amount: 900
			* ExcludedSources:
				* SellItem
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qs_exploration_03
* Type:	Side
* FollowUps: ql_Ytep
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem
			* Amount: 25
			* Analyzed: True
	* 1:
		* GoalType: Pay
			* Id: 2P
			* Amount: 5000

## QL_SIDE_001
### qs_economy_01
* Type:	Side
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Refining
			* Amount: 2000
		* GoalType: CompleteMission
			* Amount: 5
			* Tier: 2
			* Mode: Generated

### qs_economy_02
* Type:	Side
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Amount: 50

### qs_economy_03
* Type:	Side
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Refining
			* Amount: 4500
	* 1:
		* GoalType: Pay
			* Id: 2N
			* Amount: 5000

## QL_SIDE_002
### qs_battle_01
* Type:	Side
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Upgrade
			* Amount: 10
		* GoalType: CompleteMission
			* Amount: 15
			* Tier: 2
			* Mode: Generated

### qs_battle_02
* Type:	Side
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 25
			* Tags: Faction_T2up

### qs_battle_03
* Type:	Side
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tier: 2
			* Mode: Strike
	* 1:
		* GoalType: Pay
			* Id: 2O
			* Amount: 5000

## QL_SIDE_UNLOCKSTRIKES_T2
### qs_unlockStrikes_t2
* Type:	Side
* FollowUps:
	* ql_raid_014
	* ql_raid_015
	* ql_raid_016
* Goals:
	* 0:
		* GoalType: Equip
			* Type: Flagship
			* Tags: T1

## QL_SIDE_UNLOCKSTRIKES_T3
### qs_unlockStrikes_t3
* Type:	Side
* FollowUps:
	* ql_raid_017
	* ql_raid_018
* Goals:
	* 0:
		* GoalType: Equip
			* Type: Flagship
			* Tags: T2

## QL_KEID
### qs_Keid_01
* Type:	Side
* Goals:
	* 0:
		* GoalType: Goto
			* Target: [-1784, -564]
			* TargetMode: Station
	* 1:
		* GoalType: Scan
			* Tags: InSystem_T2up
			* Amount: 10
			* Analyzed: True
		* GoalType: CompleteMission
			* Mode: Generated
			* Tier: 2
			* Amount: 10
		* GoalType: Statistic
			* Id: ShipsDestroyedT2
			* Amount: 50

### qs_Keid_02
* Type:	Side
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: Mined2A
			* Amount: 2000
		* GoalType: Statistic
			* Id: Mined2B
			* Amount: 2000
		* GoalType: Statistic
			* Id: Mined2C
			* Amount: 2000
		* GoalType: Statistic
			* Id: Mined2D
			* Amount: 1500
	* 1:
		* GoalType: Statistic
			* Id: Refining2N
			* Amount: 1000
		* GoalType: Statistic
			* Id: Refining2O
			* Amount: 1000
		* GoalType: Statistic
			* Id: Refining2P
			* Amount: 1000
		* GoalType: Statistic
			* Id: Refining2Q
			* Amount: 700

### qs_Keid_03
* Type:	Side
* Goals:
	* 0:
		* GoalType: Pay
			* Id: 2N
			* Amount: 1000
			* SysId: [-1784, -564]
		* GoalType: Pay
			* Id: 2O
			* Amount: 1000
			* SysId: [-1784, -564]
		* GoalType: Pay
			* Id: 2P
			* Amount: 1000
			* SysId: [-1784, -564]
	* 1:
		* GoalType: Pay
			* Id: 2Q
			* Amount: 700
			* SysId: [-1784, -564]
		* GoalType: Pay
			* Id: CR
			* Amount: 10000
			* SysId: [-1784, -564]

## QL_EXILE
### qs_Exile_01
* Type:	Side
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 10
			* Tier: 2
			* Mode: Strike
		* GoalType: Statistic
			* Id: ShipsDestroyedP1
			* Amount: 150

### qs_Exile_02
* Type:	Side
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: Mined2A
			* Amount: 15000
		* GoalType: Statistic
			* Id: Mined2B
			* Amount: 15000
		* GoalType: Statistic
			* Id: Mined2C
			* Amount: 15000
	* 1:
		* GoalType: Craft
			* Category: Crafting
			* Amount: 10
			* Tags: Squad_T2up

### qs_Exile_03
* Type:	Side
* Goals:
	* 0:
		* GoalType: Goto
			* Target: [-1752, -861]
			* TargetMode: Station
		* GoalType: Goto
			* Target: [-1020, -650]
			* TargetMode: Station
		* GoalType: Goto
			* Target: [-1665, 176]
			* TargetMode: Station
	* 1:
		* GoalType: Scan
			* Tags: InSystem_T2up
			* Amount: 50
			* Analyzed: True

## QL_YTEP
### qs_Ytep_01
* Type:	Side
* Goals:
	* 0:
		* GoalType: Goto
			* Target: [-946, -690]
			* TargetMode: Station
	* 1:
		* GoalType: Scan
			* Tags: InSystem_T3up
			* Amount: 10
			* Analyzed: True
		* GoalType: CompleteMission
			* Mode: Generated
			* Tier: 3
			* Amount: 10
		* GoalType: Statistic
			* Id: ShipsDestroyedT3
			* Amount: 75

### qs_Ytep_02
* Type:	Side
* Goals:
	* 0:
		* GoalType: Craft
			* Tags: Part_Ship_S_T2
			* Amount: 2000
			* Category: Crafting
		* GoalType: Craft
			* Tags: Part_Weapon_S_T2
			* Amount: 2000
			* Category: Crafting
		* GoalType: Craft
			* Tags: Part_Module_S_T2
			* Amount: 2000
			* Category: Crafting
	* 1:
		* GoalType: Craft
			* Type: Squad
			* Tags: Interceptor_T2
			* Amount: 1
			* Category: Crafting
		* GoalType: Craft
			* Type: Squad
			* Tags: AssaultCorvette_T2
			* Amount: 1
			* Category: Crafting

### qs_Ytep_03
* Type:	Side
* Goals:
	* 0:
		* GoalType: Pay
			* Id: intmed_ship_small_t2
			* Amount: 20
			* SysId: [-946, -690]
		* GoalType: Pay
			* Id: intmed_weapon_small_t2
			* Amount: 800
			* SysId: [-946, -690]
		* GoalType: Pay
			* Id: intmed_module_small_t2
			* Amount: 800
			* SysId: [-946, -690]
	* 1:
		* GoalType: Pay
			* Id: hgn_sf_intc_01_t2
			* Amount: 1
			* SysId: [-946, -690]
		* GoalType: Pay
			* Id: hgn_sc_assa_01_t2
			* Amount: 1
			* SysId: [-946, -690]

## QL_ESCA_KILLPIRATE1
### qs_killPirate1_pre01
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedP1
			* Total: 10

### qs_killPirate1_00
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedP1
			* Total: 25

### qs_killPirate1_01
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedP1
			* Total: 50

### qs_killPirate1_02
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedP1
			* Total: 100

### qs_killPirate1_03
* Type:	Achievement
* FollowUps: ql_esca_killYaot
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedP1
			* Total: 200

### qs_killPirate1_04
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedP1
			* Total: 400

### qs_killPirate1_05
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedP1
			* Total: 800

### qs_killPirate1_06
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedP1
			* Total: 1600

### qs_killPirate1_07
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedP1
			* Total: 3200

### qs_killPirate1_08
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedP1
			* Total: 6400

## QL_ESCA_KILLTANOCH
### qs_killTanoch_pre01
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedTanoch
			* Total: 10

### qs_killTanoch_00
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedTanoch
			* Total: 25

### qs_killTanoch_01
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedTanoch
			* Total: 50

### qs_killTanoch_02
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedTanoch
			* Total: 100

### qs_killTanoch_03
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedTanoch
			* Total: 200

### qs_killTanoch_04
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedTanoch
			* Total: 400

### qs_killTanoch_05
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedTanoch
			* Total: 800

### qs_killTanoch_06
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedTanoch
			* Total: 1600

### qs_killTanoch_07
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedTanoch
			* Total: 3200

### qs_killTanoch_08
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedTanoch
			* Total: 6400

## QL_ESCA_KILLYAOT
### qs_killYaot_pre01
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedYaot
			* Total: 10

### qs_killYaot_00
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedYaot
			* Total: 25

### qs_killYaot_01
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedYaot
			* Total: 50

### qs_killYaot_02
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedYaot
			* Total: 100

### qs_killYaot_03
* Type:	Achievement
* FollowUps: ql_esca_killTanoch
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedYaot
			* Total: 200

### qs_killYaot_04
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedYaot
			* Total: 400

### qs_killYaot_05
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedYaot
			* Total: 800

### qs_killYaot_06
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedYaot
			* Total: 1600

### qs_killYaot_07
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedYaot
			* Total: 3200

### qs_killYaot_08
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedYaot
			* Total: 6400

## QL_ESCA_MINET1
### qs_mineT1ABC_pre01
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: Mined1A
			* Total: 1000
		* GoalType: Statistic
			* Id: Mined1B
			* Total: 1000
		* GoalType: Statistic
			* Id: Mined1C
			* Total: 1000

### qs_mineT1ABC_00
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: Mined1A
			* Total: 3000
		* GoalType: Statistic
			* Id: Mined1B
			* Total: 3000
		* GoalType: Statistic
			* Id: Mined1C
			* Total: 3000

### qs_mineT1ABC_01
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: Mined1A
			* Total: 6000
		* GoalType: Statistic
			* Id: Mined1B
			* Total: 6000
		* GoalType: Statistic
			* Id: Mined1C
			* Total: 6000

### qs_mineT1ABC_02
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: Mined1A
			* Total: 12000
		* GoalType: Statistic
			* Id: Mined1B
			* Total: 12000
		* GoalType: Statistic
			* Id: Mined1C
			* Total: 12000

### qs_mineT1ABC_03
* Type:	Achievement
* FollowUps: ql_esca_mineT2
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: Mined1A
			* Total: 24000
		* GoalType: Statistic
			* Id: Mined1B
			* Total: 24000
		* GoalType: Statistic
			* Id: Mined1C
			* Total: 24000

### qs_mineT1ABC_04
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: Mined1A
			* Total: 48000
		* GoalType: Statistic
			* Id: Mined1B
			* Total: 48000
		* GoalType: Statistic
			* Id: Mined1C
			* Total: 48000

### qs_mineT1ABC_05
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: Mined1A
			* Total: 96000
		* GoalType: Statistic
			* Id: Mined1B
			* Total: 96000
		* GoalType: Statistic
			* Id: Mined1C
			* Total: 96000

### qs_mineT1ABC_06
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: Mined1A
			* Total: 192000
		* GoalType: Statistic
			* Id: Mined1B
			* Total: 192000
		* GoalType: Statistic
			* Id: Mined1C
			* Total: 192000

### qs_mineT1ABC_07
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: Mined1A
			* Total: 384000
		* GoalType: Statistic
			* Id: Mined1B
			* Total: 384000
		* GoalType: Statistic
			* Id: Mined1C
			* Total: 384000

### qs_mineT1ABC_08
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: Mined1A
			* Total: 768000
		* GoalType: Statistic
			* Id: Mined1B
			* Total: 768000
		* GoalType: Statistic
			* Id: Mined1C
			* Total: 768000

## QL_ESCA_MINET2
### qs_mineT2ABC_pre01
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: Mined2A
			* Total: 1000
		* GoalType: Statistic
			* Id: Mined2B
			* Total: 1000
		* GoalType: Statistic
			* Id: Mined2C
			* Total: 1000

### qs_mineT2ABC_00
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: Mined2A
			* Total: 3000
		* GoalType: Statistic
			* Id: Mined2B
			* Total: 3000
		* GoalType: Statistic
			* Id: Mined2C
			* Total: 3000

### qs_mineT2ABC_01
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: Mined2A
			* Total: 6000
		* GoalType: Statistic
			* Id: Mined2B
			* Total: 6000
		* GoalType: Statistic
			* Id: Mined2C
			* Total: 6000

### qs_mineT2ABC_02
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: Mined2A
			* Total: 12000
		* GoalType: Statistic
			* Id: Mined2B
			* Total: 12000
		* GoalType: Statistic
			* Id: Mined2C
			* Total: 12000

### qs_mineT2ABC_03
* Type:	Achievement
* FollowUps: ql_esca_mineT3
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: Mined2A
			* Total: 24000
		* GoalType: Statistic
			* Id: Mined2B
			* Total: 24000
		* GoalType: Statistic
			* Id: Mined2C
			* Total: 24000

### qs_mineT2ABC_04
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: Mined2A
			* Total: 48000
		* GoalType: Statistic
			* Id: Mined2B
			* Total: 48000
		* GoalType: Statistic
			* Id: Mined2C
			* Total: 48000

### qs_mineT2ABC_05
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: Mined2A
			* Total: 96000
		* GoalType: Statistic
			* Id: Mined2B
			* Total: 96000
		* GoalType: Statistic
			* Id: Mined2C
			* Total: 96000

### qs_mineT2ABC_06
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: Mined2A
			* Total: 192000
		* GoalType: Statistic
			* Id: Mined2B
			* Total: 192000
		* GoalType: Statistic
			* Id: Mined2C
			* Total: 192000

### qs_mineT2ABC_07
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: Mined2A
			* Total: 384000
		* GoalType: Statistic
			* Id: Mined2B
			* Total: 384000
		* GoalType: Statistic
			* Id: Mined2C
			* Total: 384000

### qs_mineT2ABC_08
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: Mined2A
			* Total: 768000
		* GoalType: Statistic
			* Id: Mined2B
			* Total: 768000
		* GoalType: Statistic
			* Id: Mined2C
			* Total: 768000

## QL_ESCA_MINET3
### qs_mineT3ABC_pre01
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: Mined3A
			* Total: 1000
		* GoalType: Statistic
			* Id: Mined3B
			* Total: 1000
		* GoalType: Statistic
			* Id: Mined3C
			* Total: 1000

### qs_mineT3ABC_00
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: Mined3A
			* Total: 3000
		* GoalType: Statistic
			* Id: Mined3B
			* Total: 3000
		* GoalType: Statistic
			* Id: Mined3C
			* Total: 3000

### qs_mineT3ABC_01
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: Mined3A
			* Total: 6000
		* GoalType: Statistic
			* Id: Mined3B
			* Total: 6000
		* GoalType: Statistic
			* Id: Mined3C
			* Total: 6000

### qs_mineT3ABC_02
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: Mined3A
			* Total: 12000
		* GoalType: Statistic
			* Id: Mined3B
			* Total: 12000
		* GoalType: Statistic
			* Id: Mined3C
			* Total: 12000

### qs_mineT3ABC_03
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: Mined3A
			* Total: 24000
		* GoalType: Statistic
			* Id: Mined3B
			* Total: 24000
		* GoalType: Statistic
			* Id: Mined3C
			* Total: 24000

### qs_mineT3ABC_04
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: Mined3A
			* Total: 48000
		* GoalType: Statistic
			* Id: Mined3B
			* Total: 48000
		* GoalType: Statistic
			* Id: Mined3C
			* Total: 48000

### qs_mineT3ABC_05
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: Mined3A
			* Total: 96000
		* GoalType: Statistic
			* Id: Mined3B
			* Total: 96000
		* GoalType: Statistic
			* Id: Mined3C
			* Total: 96000

### qs_mineT3ABC_06
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: Mined3A
			* Total: 192000
		* GoalType: Statistic
			* Id: Mined3B
			* Total: 192000
		* GoalType: Statistic
			* Id: Mined3C
			* Total: 192000

### qs_mineT3ABC_07
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: Mined3A
			* Total: 384000
		* GoalType: Statistic
			* Id: Mined3B
			* Total: 384000
		* GoalType: Statistic
			* Id: Mined3C
			* Total: 384000

### qs_mineT3ABC_08
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: Mined3A
			* Total: 768000
		* GoalType: Statistic
			* Id: Mined3B
			* Total: 768000
		* GoalType: Statistic
			* Id: Mined3C
			* Total: 768000

## QL_ESCA_SCAN
### qs_scan_pre01
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: Scanned
			* Total: 50

### qs_scan_00
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: Scanned
			* Total: 150

### qs_scan_01
* Type:	Achievement
* FollowUps: ql_esca_generated
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: Scanned
			* Total: 300

### qs_scan_02
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: Scanned
			* Total: 600

### qs_scan_03
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: Scanned
			* Total: 1200

### qs_scan_04
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: Scanned
			* Total: 2500

### qs_scan_05
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: Scanned
			* Total: 5000

### qs_scan_06
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: Scanned
			* Total: 10000

### qs_scan_07
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: Scanned
			* Total: 20000

### qs_scan_08
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: Scanned
			* Total: 40000

## QL_ESCA_GENERATED
### qs_finishGenerated_pre01
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: MissionsDoneGenerated
			* Total: 2

### qs_finishGenerated_00
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: MissionsDoneGenerated
			* Total: 5

### qs_finishGenerated_01
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: MissionsDoneGenerated
			* Total: 10

### qs_finishGenerated_02
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: MissionsDoneGenerated
			* Total: 20

### qs_finishGenerated_03
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: MissionsDoneGenerated
			* Total: 40

### qs_finishGenerated_04
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: MissionsDoneGenerated
			* Total: 80

### qs_finishGenerated_05
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: MissionsDoneGenerated
			* Total: 160

### qs_finishGenerated_06
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: MissionsDoneGenerated
			* Total: 320

### qs_finishGenerated_07
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: MissionsDoneGenerated
			* Total: 640

### qs_finishGenerated_08
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: MissionsDoneGenerated
			* Total: 1300

## QL_RAID_013
### qr_013
* Type:	Strike
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: strike_01_PirateHideout

## QL_RAID_016
### qr_016
* Type:	Strike
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: strike_01_PirateHideout_heroic

## QL_RAID_014
### qr_014
* Type:	Strike
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: strike_02_StationDefense

## QL_RAID_017
### qr_017
* Type:	Strike
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: strike_02_StationDefense_heroic

## QL_RAID_021
### qr_021
* Type:	Strike
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: strike_02_StationDefense_mythic

## QL_RAID_015
### qr_015
* Type:	Strike
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: strike_03_PahrasRock

## QL_RAID_018
### qr_018
* Type:	Strike
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: strike_03_PahrasRock_heroic

## QL_RAID_022
### qr_022
* Type:	Strike
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: strike_03_PahrasRock_mythic

## QL_RAID_019
### qr_019
* Type:	Strike
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: strike_04_Breach

## QL_RAID_020
### qr_020
* Type:	Strike
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: strike_04_Breach_heroic

## QL_RAID_023
### qr_023
* Type:	Strike
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: strike_05_NightmareGulf

## QL_EVENT_TEST_1
### qe_test_eventtestquest_1
* Type:	Event
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Amount: 10

## QL_EVENT_TEST_2
### qe_test_eventtestquest_2
* Type:	Event
* Goals:
	* 0:
		* GoalType: Pay
			* Id: CR
			* Amount: 10

## QL_EVENT_TEST_3
### qe_test_eventtestquest_3
* Type:	Event
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1

## QL_YAOT_SPRING_2023_DAILY_A_T2
### qe_yaot_spring_2023_daily_A_t2
* Type:	Event
* EventId:	event_season_yaoSpr_2023
* Goals:
	* 0:
		* GoalType: GainItem
			* Id: RP
			* Amount: 200
			* ExcludedSources:
				* SellItem
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

## QL_YAOT_SPRING_2023_DAILY_B_T2
### qe_yaot_spring_2023_daily_B_t2
* Type:	Event
* EventId:	event_season_yaoSpr_2023
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedTanoch
			* Amount: 10

## QL_YAOT_SPRING_2023_DAILY_C_T3
### qe_yaot_spring_2023_daily_C_t3
* Type:	Event
* EventId:	event_season_yaoSpr_2023
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* Mined3E
				* Mined3F
				* Mined3G
				* Mined3H
				* Mined4E
				* Mined4F
				* Mined4G
				* Mined4H
			* Amount: 100

## QL_YAOT_SPRING_2023_DAILY_D_T3
### qe_yaot_spring_2023_daily_D_t3
* Type:	Event
* EventId:	event_season_yaoSpr_2023
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: Faction_Yaot

## QL_EVENT_YAOT_SPRING_2023
### qe_yaot_spring_2023_day1
* Type:	Event
* EventId:	event_season_yaoSpr_2023
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: Mined
			* Amount: 750

### qe_yaot_spring_2023_day2
* Type:	Event
* EventId:	event_season_yaoSpr_2023
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Mode: Generated

### qe_yaot_spring_2023_day3
* Type:	Event
* EventId:	event_season_yaoSpr_2023
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Refining
			* Amount: 500

### qe_yaot_spring_2023_day4
* Type:	Event
* EventId:	event_season_yaoSpr_2023
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Insignia
			* Amount: 15
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_yaot_spring_2023_day5
* Type:	Event
* EventId:	event_season_yaoSpr_2023
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 3

### qe_yaot_spring_2023_day6
* Type:	Event
* EventId:	event_season_yaoSpr_2023
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Mode: Generated

### qe_yaot_spring_2023_day7
* Type:	Event
* EventId:	event_season_yaoSpr_2023
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: Mined
			* Amount: 750

### qe_yaot_spring_2023_day8
* Type:	Event
* EventId:	event_season_yaoSpr_2023
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: ProgenitorRelic
			* Amount: 1
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_yaot_spring_2023_day9
* Type:	Event
* EventId:	event_season_yaoSpr_2023
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Refining
			* Amount: 500

### qe_yaot_spring_2023_day10
* Type:	Event
* EventId:	event_season_yaoSpr_2023
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Mode: Generated

### qe_yaot_spring_2023_day11
* Type:	Event
* EventId:	event_season_yaoSpr_2023
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: Mined
			* Amount: 750

### qe_yaot_spring_2023_day12
* Type:	Event
* EventId:	event_season_yaoSpr_2023
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Insignia
			* Amount: 15
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_yaot_spring_2023_day13
* Type:	Event
* EventId:	event_season_yaoSpr_2023
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 3

### qe_yaot_spring_2023_day14
* Type:	Event
* EventId:	event_season_yaoSpr_2023
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: story_C01_Tanochet_event_heroic

## QL_EVENT_AMASUM_2023_T1
### qe_amaSum_2023_day1_t1
* Type:	Event
* EventId:	event_season_amaSum_2023_t1
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Refining
			* Tags: Asteroid_Refined_T1up
			* Amount: 350

### qe_amaSum_2023_day2_t1
* Type:	Event
* EventId:	event_season_amaSum_2023_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T1up
			* Mode: Generated

### qe_amaSum_2023_day3_t1
* Type:	Event
* EventId:	event_season_amaSum_2023_t1
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 3

### qe_amaSum_2023_day4_t1
* Type:	Event
* EventId:	event_season_amaSum_2023_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T1up
			* Mode: Generated

### qe_amaSum_2023_day5_t1
* Type:	Event
* EventId:	event_season_amaSum_2023_t1
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Refining
			* Tags: Asteroid_Refined_T1up
			* Amount: 350

### qe_amaSum_2023_day6_t1
* Type:	Event
* EventId:	event_season_amaSum_2023_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T1up
			* Mode: Generated

### qe_amaSum_2023_day7_t1
* Type:	Event
* EventId:	event_season_amaSum_2023_t1
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Insignia_T1up
			* Amount: 15
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_amaSum_2023_day8_t1
* Type:	Event
* EventId:	event_season_amaSum_2023_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T1up
			* Mode: Generated

### qe_amaSum_2023_day9_t1
* Type:	Event
* EventId:	event_season_amaSum_2023_t1
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Refining
			* Tags: Asteroid_Refined_T1up
			* Amount: 350

### qe_amaSum_2023_day10_t1
* Type:	Event
* EventId:	event_season_amaSum_2023_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T1up
			* Mode: Generated

### qe_amaSum_2023_day11_t1
* Type:	Event
* EventId:	event_season_amaSum_2023_t1
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 3

### qe_amaSum_2023_day12_t1
* Type:	Event
* EventId:	event_season_amaSum_2023_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T1up
			* Mode: Generated

### qe_amaSum_2023_day13_t1
* Type:	Event
* EventId:	event_season_amaSum_2023_t1
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Refining
			* Tags: Asteroid_Refined_T1up
			* Amount: 350

### qe_amaSum_2023_day14_t1
* Type:	Event
* EventId:	event_season_amaSum_2023_t1
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Insignia_T1up
			* Amount: 15
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_amaSum_2023_day15_t1
* Type:	Event
* EventId:	event_season_amaSum_2023_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_01_StationDefense

## QL_EVENT_AMASUM_2023_T2
### qe_amaSum_2023_day1_t2
* Type:	Event
* EventId:	event_season_amaSum_2023_t2
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Refining
			* Tags: Asteroid_Refined_T2up
			* Amount: 400

### qe_amaSum_2023_day2_t2
* Type:	Event
* EventId:	event_season_amaSum_2023_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T2up
			* Mode: Generated

### qe_amaSum_2023_day3_t2
* Type:	Event
* EventId:	event_season_amaSum_2023_t2
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 3

### qe_amaSum_2023_day4_t2
* Type:	Event
* EventId:	event_season_amaSum_2023_t2
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: Faction_T2up

### qe_amaSum_2023_day5_t2
* Type:	Event
* EventId:	event_season_amaSum_2023_t2
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Refining
			* Tags: Asteroid_Refined_T2up
			* Amount: 400

### qe_amaSum_2023_day6_t2
* Type:	Event
* EventId:	event_season_amaSum_2023_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T2up
			* Mode: Generated

### qe_amaSum_2023_day7_t2
* Type:	Event
* EventId:	event_season_amaSum_2023_t2
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Insignia_T2up
			* Amount: 15
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_amaSum_2023_day8_t2
* Type:	Event
* EventId:	event_season_amaSum_2023_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Mode: Strike
			* Tags: T1up

### qe_amaSum_2023_day9_t2
* Type:	Event
* EventId:	event_season_amaSum_2023_t2
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Refining
			* Tags: Asteroid_Refined_T2up
			* Amount: 400

### qe_amaSum_2023_day10_t2
* Type:	Event
* EventId:	event_season_amaSum_2023_t2
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: Faction_T2up

### qe_amaSum_2023_day11_t2
* Type:	Event
* EventId:	event_season_amaSum_2023_t2
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 3

### qe_amaSum_2023_day12_t2
* Type:	Event
* EventId:	event_season_amaSum_2023_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Mode: Strike
			* Tags: T1up

### qe_amaSum_2023_day13_t2
* Type:	Event
* EventId:	event_season_amaSum_2023_t2
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Refining
			* Tags: Asteroid_Refined_T2up
			* Amount: 400

### qe_amaSum_2023_day14_t2
* Type:	Event
* EventId:	event_season_amaSum_2023_t2
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Insignia_T2up
			* Amount: 15
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_amaSum_2023_day15_t2
* Type:	Event
* EventId:	event_season_amaSum_2023_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_02_StationDefense

## QL_EVENT_AMASUM_2023_T3
### qe_amaSum_2023_day1_t3
* Type:	Event
* EventId:	event_season_amaSum_2023_t3
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Refining
			* Tags: Asteroid_Refined_T3up
			* Amount: 450

### qe_amaSum_2023_day2_t3
* Type:	Event
* EventId:	event_season_amaSum_2023_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T3up
			* Mode: Generated

### qe_amaSum_2023_day3_t3
* Type:	Event
* EventId:	event_season_amaSum_2023_t3
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 3

### qe_amaSum_2023_day4_t3
* Type:	Event
* EventId:	event_season_amaSum_2023_t3
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: Faction_T3up

### qe_amaSum_2023_day5_t3
* Type:	Event
* EventId:	event_season_amaSum_2023_t3
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Gas_T3up
			* Amount: 800
			* ExcludedSources:
				* PayGoal
				* QuestReward
				* MissionReward
				* BuyItem
				* SellItem
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer

### qe_amaSum_2023_day6_t3
* Type:	Event
* EventId:	event_season_amaSum_2023_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T3up
			* Mode: Generated

### qe_amaSum_2023_day7_t3
* Type:	Event
* EventId:	event_season_amaSum_2023_t3
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Insignia_T3up
			* Amount: 15
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_amaSum_2023_day8_t3
* Type:	Event
* EventId:	event_season_amaSum_2023_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Mode: Strike
			* Tags: T2up

### qe_amaSum_2023_day9_t3
* Type:	Event
* EventId:	event_season_amaSum_2023_t3
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Refining
			* Tags: Asteroid_Refined_T3up
			* Amount: 450

### qe_amaSum_2023_day10_t3
* Type:	Event
* EventId:	event_season_amaSum_2023_t3
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: Faction_T3up

### qe_amaSum_2023_day11_t3
* Type:	Event
* EventId:	event_season_amaSum_2023_t3
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 3

### qe_amaSum_2023_day12_t3
* Type:	Event
* EventId:	event_season_amaSum_2023_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Mode: Strike
			* Tags: T2up

### qe_amaSum_2023_day13_t3
* Type:	Event
* EventId:	event_season_amaSum_2023_t3
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Gas_T3up
			* Amount: 800
			* ExcludedSources:
				* PayGoal
				* QuestReward
				* MissionReward
				* BuyItem
				* SellItem
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer

### qe_amaSum_2023_day14_t3
* Type:	Event
* EventId:	event_season_amaSum_2023_t3
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Insignia_T3up
			* Amount: 15
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_amaSum_2023_day15_t3
* Type:	Event
* EventId:	event_season_amaSum_2023_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_03_StationDefense

## QL_EVENT_AMASUM_2023_T4
### qe_amaSum_2023_day1_t4
* Type:	Event
* EventId:	event_season_amaSum_2023_t4
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Refining
			* Tags: Asteroid_Refined_T4up
			* Amount: 500

### qe_amaSum_2023_day2_t4
* Type:	Event
* EventId:	event_season_amaSum_2023_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T4up
			* Mode: Generated

### qe_amaSum_2023_day3_t4
* Type:	Event
* EventId:	event_season_amaSum_2023_t4
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 3

### qe_amaSum_2023_day4_t4
* Type:	Event
* EventId:	event_season_amaSum_2023_t4
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: Faction_Amassari_T4up

### qe_amaSum_2023_day5_t4
* Type:	Event
* EventId:	event_season_amaSum_2023_t4
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Gas_T4up
			* Amount: 1000
			* ExcludedSources:
				* PayGoal
				* QuestReward
				* MissionReward
				* BuyItem
				* SellItem
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer

### qe_amaSum_2023_day6_t4
* Type:	Event
* EventId:	event_season_amaSum_2023_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T4up
			* Mode: Generated

### qe_amaSum_2023_day7_t4
* Type:	Event
* EventId:	event_season_amaSum_2023_t4
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Insignia_T4up
			* Amount: 15
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_amaSum_2023_day8_t4
* Type:	Event
* EventId:	event_season_amaSum_2023_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 5
			* Mode: Strike
			* Tags: T3up

### qe_amaSum_2023_day9_t4
* Type:	Event
* EventId:	event_season_amaSum_2023_t4
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Refining
			* Tags: Asteroid_Refined_T4up
			* Amount: 500

### qe_amaSum_2023_day10_t4
* Type:	Event
* EventId:	event_season_amaSum_2023_t4
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: Faction_Amassari_T4up

### qe_amaSum_2023_day11_t4
* Type:	Event
* EventId:	event_season_amaSum_2023_t4
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 3

### qe_amaSum_2023_day12_t4
* Type:	Event
* EventId:	event_season_amaSum_2023_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 5
			* Mode: Strike
			* Tags: T3up

### qe_amaSum_2023_day13_t4
* Type:	Event
* EventId:	event_season_amaSum_2023_t4
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Gas_T4up
			* Amount: 1000
			* ExcludedSources:
				* PayGoal
				* QuestReward
				* MissionReward
				* BuyItem
				* SellItem
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer

### qe_amaSum_2023_day14_t4
* Type:	Event
* EventId:	event_season_amaSum_2023_t4
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Insignia_T4up
			* Amount: 15
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_amaSum_2023_day15_t4
* Type:	Event
* EventId:	event_season_amaSum_2023_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_04_StationDefense

## QL_7DAYS_MAR_2024_DAY1_T1
### qe_7days_mar_2024_day1_a_t1
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t1
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_T1up
			* Amount: 10
			* Analyzed: True

### qe_7days_mar_2024_day1_b_t1
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t1
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedT1
				* ShipsDestroyedT2
				* ShipsDestroyedT3
				* ShipsDestroyedT4
			* Amount: 15

### qe_7days_mar_2024_day1_c_t1
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t1
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Asteroid_Crud_T1up
			* Amount: 800
			* ExcludedSources:
				* PayGoal
				* QuestReward
				* MissionReward
				* BuyItem
				* SellItem
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_7days_mar_2024_day1_d_t1
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t1
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: RareEarth_T1up
			* Amount: 15
			* ExcludedSources:
				* SellItem
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

## QL_7DAYS_MAR_2024_DAY1_T2
### qe_7days_mar_2024_day1_a_t2
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t2
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_T2up
			* Amount: 10
			* Analyzed: True

### qe_7days_mar_2024_day1_b_t2
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t2
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedT2
				* ShipsDestroyedT3
				* ShipsDestroyedT4
			* Amount: 15

### qe_7days_mar_2024_day1_c_t2
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t2
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Asteroid_Crud_T2up
			* Amount: 1000
			* ExcludedSources:
				* PayGoal
				* QuestReward
				* MissionReward
				* BuyItem
				* SellItem
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_7days_mar_2024_day1_d_t2
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t2
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: RareEarth_T2up
			* Amount: 15
			* ExcludedSources:
				* SellItem
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

## QL_7DAYS_MAR_2024_DAY1_T3
### qe_7days_mar_2024_day1_a_t3
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t3
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_T3up
			* Amount: 10
			* Analyzed: True

### qe_7days_mar_2024_day1_b_t3
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t3
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedT3
				* ShipsDestroyedT4
			* Amount: 15

### qe_7days_mar_2024_day1_c_t3
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t3
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Gas_T3up
			* Amount: 800
			* ExcludedSources:
				* PayGoal
				* QuestReward
				* MissionReward
				* BuyItem
				* SellItem
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_7days_mar_2024_day1_d_t3
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t3
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: RareEarth_T3up
			* Amount: 15
			* ExcludedSources:
				* SellItem
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

## QL_7DAYS_MAR_2024_DAY1_T4
### qe_7days_mar_2024_day1_a_t4
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t4
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_T4up
			* Amount: 10
			* Analyzed: True

### qe_7days_mar_2024_day1_b_t4
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t4
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedT4
			* Amount: 15

### qe_7days_mar_2024_day1_c_t4
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t4
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Gas_T4up
			* Amount: 1000
			* ExcludedSources:
				* PayGoal
				* QuestReward
				* MissionReward
				* BuyItem
				* SellItem
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_7days_mar_2024_day1_d_t4
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t4
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: RareEarth_T4up
			* Amount: 15
			* ExcludedSources:
				* SellItem
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

## QL_7DAYS_MAR_2024_DAY2_T1
### qe_7days_mar_2024_day2_a_t1
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t1
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: T1up

### qe_7days_mar_2024_day2_b_t1
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T1up

### qe_7days_mar_2024_day2_c_t1
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t1
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Insignia_T1up
			* Amount: 50
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_7days_mar_2024_day2_d_t1
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t1
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 1

## QL_7DAYS_MAR_2024_DAY2_T2
### qe_7days_mar_2024_day2_a_t2
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t2
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: Faction_T2up

### qe_7days_mar_2024_day2_b_t2
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Mode: Faction
			* Tags: T2up

### qe_7days_mar_2024_day2_c_t2
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t2
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* RepTr1
				* RepTanoch
				* RepYaot
				* RepAmassari
			* Amount: 135

### qe_7days_mar_2024_day2_d_t2
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t2
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 2

## QL_7DAYS_MAR_2024_DAY2_T3
### qe_7days_mar_2024_day2_a_t3
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t3
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: Faction_T3up

### qe_7days_mar_2024_day2_b_t3
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Mode: Faction
			* Tags: T3up

### qe_7days_mar_2024_day2_c_t3
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t3
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* RepTr1
				* RepTanoch
				* RepYaot
				* RepAmassari
			* Amount: 180

### qe_7days_mar_2024_day2_d_t3
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t3
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 3

## QL_7DAYS_MAR_2024_DAY2_T4
### qe_7days_mar_2024_day2_a_t4
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t4
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: Faction_T4up

### qe_7days_mar_2024_day2_b_t4
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Mode: Faction
			* Tags: T4up

### qe_7days_mar_2024_day2_c_t4
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t4
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* RepTr1
				* RepTanoch
				* RepYaot
				* RepAmassari
			* Amount: 225

### qe_7days_mar_2024_day2_d_t4
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t4
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 5

## QL_7DAYS_MAR_2024_DAY3_T1
### qe_7days_mar_2024_day3_a_t1
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t1
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Asteroid_Crud_T1up
			* Amount: 800
			* ExcludedSources:
				* PayGoal
				* QuestReward
				* MissionReward
				* BuyItem
				* SellItem
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_7days_mar_2024_day3_b_t1
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t1
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Refining
			* Tags: Asteroid_Refined_T1up
			* Amount: 500

### qe_7days_mar_2024_day3_c_t1
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t1
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: T1up
			* Amount: 1

### qe_7days_mar_2024_day3_d_t1
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t1
* Goals:
	* 0:
		* GoalType: GainItem
			* Id: CR
			* Amount: 150
			* ExcludedSources:
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
				* DismissOfficer
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer

## QL_7DAYS_MAR_2024_DAY3_T2
### qe_7days_mar_2024_day3_a_t2
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t2
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Asteroid_Crud_T2up
			* Amount: 1000
			* ExcludedSources:
				* PayGoal
				* QuestReward
				* MissionReward
				* BuyItem
				* SellItem
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_7days_mar_2024_day3_b_t2
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t2
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Refining
			* Tags: Asteroid_Refined_T2up
			* Amount: 500

### qe_7days_mar_2024_day3_c_t2
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t2
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: Part_T2up
			* Amount: 25

### qe_7days_mar_2024_day3_d_t2
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t2
* Goals:
	* 0:
		* GoalType: GainItem
			* Id: CR
			* Amount: 300
			* ExcludedSources:
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
				* DismissOfficer
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer

## QL_7DAYS_MAR_2024_DAY3_T3
### qe_7days_mar_2024_day3_a_t3
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t3
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Asteroid_Crud_T3up
			* Amount: 1200
			* ExcludedSources:
				* PayGoal
				* QuestReward
				* MissionReward
				* BuyItem
				* SellItem
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_7days_mar_2024_day3_b_t3
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t3
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Refining
			* Tags: Asteroid_Refined_T3up
			* Amount: 500

### qe_7days_mar_2024_day3_c_t3
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t3
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: Part_T3up
			* Amount: 25

### qe_7days_mar_2024_day3_d_t3
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t3
* Goals:
	* 0:
		* GoalType: GainItem
			* Id: CR
			* Amount: 600
			* ExcludedSources:
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
				* DismissOfficer
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer

## QL_7DAYS_MAR_2024_DAY3_T4
### qe_7days_mar_2024_day3_a_t4
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t4
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Asteroid_Crud_T4up
			* Amount: 1400
			* ExcludedSources:
				* PayGoal
				* QuestReward
				* MissionReward
				* BuyItem
				* SellItem
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_7days_mar_2024_day3_b_t4
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t4
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Refining
			* Tags: Asteroid_Refined_T4up
			* Amount: 500

### qe_7days_mar_2024_day3_c_t4
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t4
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: Part_T4up
			* Amount: 25

### qe_7days_mar_2024_day3_d_t4
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t4
* Goals:
	* 0:
		* GoalType: GainItem
			* Id: CR
			* Amount: 1200
			* ExcludedSources:
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
				* DismissOfficer
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer

## QL_7DAYS_MAR_2024_DAY4_T1
### qe_7days_mar_2024_day4_a_t1
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T1up
			* Mode: Generated

### qe_7days_mar_2024_day4_b_t1
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t1
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: ProgenitorRelic_T1up
			* Amount: 1
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_7days_mar_2024_day4_c_t1
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t1
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedProgenitorT1
				* ShipsDestroyedProgenitorT2
				* ShipsDestroyedProgenitorT3
				* ShipsDestroyedProgenitorT4
			* Amount: 7

### qe_7days_mar_2024_day4_d_t1
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Rare_T1up
			* Mode: Generated

## QL_7DAYS_MAR_2024_DAY4_T2
### qe_7days_mar_2024_day4_a_t2
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t2
* Goals:
	* 0:
		* GoalType: GainItem
			* Id: RP
			* Amount: 200
			* ExcludedSources:
				* SellItem
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_7days_mar_2024_day4_b_t2
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t2
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: ProgenitorRelic_T2up
			* Amount: 1
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_7days_mar_2024_day4_c_t2
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t2
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedProgenitorT2
				* ShipsDestroyedProgenitorT3
				* ShipsDestroyedProgenitorT4
			* Amount: 7

### qe_7days_mar_2024_day4_d_t2
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Epic_T2up
			* Mode: Generated

## QL_7DAYS_MAR_2024_DAY4_T3
### qe_7days_mar_2024_day4_a_t3
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t3
* Goals:
	* 0:
		* GoalType: GainItem
			* Id: RP
			* Amount: 200
			* ExcludedSources:
				* SellItem
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_7days_mar_2024_day4_b_t3
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t3
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: ProgenitorRelic_T3up
			* Amount: 1
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_7days_mar_2024_day4_c_t3
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t3
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedProgenitorT3
				* ShipsDestroyedProgenitorT4
			* Amount: 7

### qe_7days_mar_2024_day4_d_t3
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Epic_T3up
			* Mode: Generated

## QL_7DAYS_MAR_2024_DAY4_T4
### qe_7days_mar_2024_day4_a_t4
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t4
* Goals:
	* 0:
		* GoalType: GainItem
			* Id: RP
			* Amount: 200
			* ExcludedSources:
				* SellItem
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_7days_mar_2024_day4_b_t4
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t4
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: ProgenitorRelic_T4up
			* Amount: 1
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_7days_mar_2024_day4_c_t4
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t4
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
			* Amount: 7

### qe_7days_mar_2024_day4_d_t4
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Epic_T4up
			* Mode: Generated

## QL_7DAYS_MAR_2024_DAY5_T1
### qe_7days_mar_2024_day5_a_t1
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T1up
			* Mode: Generated

### qe_7days_mar_2024_day5_b_t1
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t1
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Insignia_T1up
			* Amount: 50
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_7days_mar_2024_day5_c_t1
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t1
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 1

### qe_7days_mar_2024_day5_d_t1
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t1
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Insignia
			* Amount: 2
			* ExcludedSources:
				* OpenContainer
				* QuestReward
				* MissionReward
				* ClaimMail
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
				* BuyItem
				* SellItem

## QL_7DAYS_MAR_2024_DAY5_T2
### qe_7days_mar_2024_day5_a_t2
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T2up
			* Mode: Generated

### qe_7days_mar_2024_day5_b_t2
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t2
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Insignia_T2up
			* Amount: 50
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_7days_mar_2024_day5_c_t2
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t2
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 2

### qe_7days_mar_2024_day5_d_t2
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t2
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Insignia
			* Amount: 4
			* ExcludedSources:
				* OpenContainer
				* QuestReward
				* MissionReward
				* ClaimMail
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
				* BuyItem
				* SellItem

## QL_7DAYS_MAR_2024_DAY5_T3
### qe_7days_mar_2024_day5_a_t3
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T3up
			* Mode: Generated

### qe_7days_mar_2024_day5_b_t3
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t3
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Insignia_T3up
			* Amount: 50
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_7days_mar_2024_day5_c_t3
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t3
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 3

### qe_7days_mar_2024_day5_d_t3
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t3
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Insignia
			* Amount: 6
			* ExcludedSources:
				* OpenContainer
				* QuestReward
				* MissionReward
				* ClaimMail
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
				* BuyItem
				* SellItem

## QL_7DAYS_MAR_2024_DAY5_T4
### qe_7days_mar_2024_day5_a_t4
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T4up
			* Mode: Generated

### qe_7days_mar_2024_day5_b_t4
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t4
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Insignia_T4up
			* Amount: 50
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_7days_mar_2024_day5_c_t4
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t4
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 5

### qe_7days_mar_2024_day5_d_t4
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t4
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Insignia
			* Amount: 10
			* ExcludedSources:
				* OpenContainer
				* QuestReward
				* MissionReward
				* ClaimMail
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
				* BuyItem
				* SellItem

## QL_7DAYS_MAR_2024_DAY6_T1
### qe_7days_mar_2024_day6_a_t1
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t1
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: RareEarth_T1up
			* Amount: 15
			* ExcludedSources:
				* SellItem
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_7days_mar_2024_day6_b_t1
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t1
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 1

### qe_7days_mar_2024_day6_c_t1
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t1
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: T1up
			* Amount: 1

### qe_7days_mar_2024_day6_d_t1
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t1
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedT1
				* ShipsDestroyedT2
				* ShipsDestroyedT3
				* ShipsDestroyedT4
			* Amount: 15

## QL_7DAYS_MAR_2024_DAY6_T2
### qe_7days_mar_2024_day6_a_t2
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t2
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: RareEarth_T2up
			* Amount: 15
			* ExcludedSources:
				* SellItem
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_7days_mar_2024_day6_b_t2
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t2
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Upgrade
			* Tags: External_Module_T1up
			* Amount: 1

### qe_7days_mar_2024_day6_c_t2
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t2
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: Part_T2up
			* Amount: 25

### qe_7days_mar_2024_day6_d_t2
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t2
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedT2
				* ShipsDestroyedT3
				* ShipsDestroyedT4
			* Amount: 15

## QL_7DAYS_MAR_2024_DAY6_T3
### qe_7days_mar_2024_day6_a_t3
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t3
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: RareEarth_T3up
			* Amount: 15
			* ExcludedSources:
				* SellItem
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_7days_mar_2024_day6_b_t3
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t3
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Upgrade
			* Tags: External_Module_T2up
			* Amount: 1

### qe_7days_mar_2024_day6_c_t3
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t3
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Upgrade
			* Tags: Internal_Module_T2up
			* Amount: 1

### qe_7days_mar_2024_day6_d_t3
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t3
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedT3
				* ShipsDestroyedT4
			* Amount: 15

## QL_7DAYS_MAR_2024_DAY6_T4
### qe_7days_mar_2024_day6_a_t4
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t4
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: RareEarth_T4up
			* Amount: 15
			* ExcludedSources:
				* SellItem
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_7days_mar_2024_day6_b_t4
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t4
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Upgrade
			* Tags: External_Module_T3up
			* Amount: 1

### qe_7days_mar_2024_day6_c_t4
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t4
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Upgrade
			* Tags: Internal_Module_T3up
			* Amount: 1

### qe_7days_mar_2024_day6_d_t4
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t4
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedT4
			* Amount: 15

## QL_7DAYS_MAR_2024_DAY7_T1
### qe_7days_mar_2024_day7_a_t1
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T1up
			* Mode: Generated

### qe_7days_mar_2024_day7_b_t1
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t1
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedT1
				* ShipsDestroyedT2
				* ShipsDestroyedT3
				* ShipsDestroyedT4
			* Amount: 15

### qe_7days_mar_2024_day7_c_t1
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t1
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Salvage_T1up
			* Amount: 3
			* ExcludedSources:
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_7days_mar_2024_day7_d_t1
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T1up
			* Mode: Generated

## QL_7DAYS_MAR_2024_DAY7_T2
### qe_7days_mar_2024_day7_a_t2
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T2up
			* Mode: Generated

### qe_7days_mar_2024_day7_b_t2
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t2
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedT2
				* ShipsDestroyedT3
				* ShipsDestroyedT4
			* Amount: 15

### qe_7days_mar_2024_day7_c_t2
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t2
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Salvage_T2up
			* Amount: 3
			* ExcludedSources:
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_7days_mar_2024_day7_d_t2
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Mode: Strike
			* Tags: T1up

## QL_7DAYS_MAR_2024_DAY7_T3
### qe_7days_mar_2024_day7_a_t3
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T3up
			* Mode: Generated

### qe_7days_mar_2024_day7_b_t3
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t3
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedT3
				* ShipsDestroyedT4
			* Amount: 15

### qe_7days_mar_2024_day7_c_t3
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t3
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Salvage_T3up
			* Amount: 3
			* ExcludedSources:
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_7days_mar_2024_day7_d_t3
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Mode: Strike
			* Tags: T2up

## QL_7DAYS_MAR_2024_DAY7_T4
### qe_7days_mar_2024_day7_a_t4
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T4up
			* Mode: Generated

### qe_7days_mar_2024_day7_b_t4
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t4
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedT4
			* Amount: 15

### qe_7days_mar_2024_day7_c_t4
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t4
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Salvage_T4up
			* Amount: 3
			* ExcludedSources:
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_7days_mar_2024_day7_d_t4
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Mode: Strike
			* Tags: T3up

## QL_7DAYS_2023_08_DAY1_T1
### qe_7days_2023_08_day1_a_t1
* Type:	Event
* EventId:	event_7days_2023_08_21_t1
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_T1up
			* Amount: 10
			* Analyzed: True

### qe_7days_2023_08_day1_b_t1
* Type:	Event
* EventId:	event_7days_2023_08_21_t1
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedT1
				* ShipsDestroyedT2
				* ShipsDestroyedT3
				* ShipsDestroyedT4
			* Amount: 15

### qe_7days_2023_08_day1_c_t1
* Type:	Event
* EventId:	event_7days_2023_08_21_t1
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Asteroid_Crud_T1up
			* Amount: 800
			* ExcludedSources:
				* PayGoal
				* QuestReward
				* MissionReward
				* BuyItem
				* SellItem
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_7days_2023_08_day1_d_t1
* Type:	Event
* EventId:	event_7days_2023_08_21_t1
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: RareEarth_T1up
			* Amount: 15
			* ExcludedSources:
				* SellItem
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

## QL_7DAYS_2023_08_DAY1_T2
### qe_7days_2023_08_day1_a_t2
* Type:	Event
* EventId:	event_7days_2023_08_21_t2
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_T2up
			* Amount: 10
			* Analyzed: True

### qe_7days_2023_08_day1_b_t2
* Type:	Event
* EventId:	event_7days_2023_08_21_t2
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedT2
				* ShipsDestroyedT3
				* ShipsDestroyedT4
			* Amount: 15

### qe_7days_2023_08_day1_c_t2
* Type:	Event
* EventId:	event_7days_2023_08_21_t2
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Asteroid_Crud_T2up
			* Amount: 1000
			* ExcludedSources:
				* PayGoal
				* QuestReward
				* MissionReward
				* BuyItem
				* SellItem
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_7days_2023_08_day1_d_t2
* Type:	Event
* EventId:	event_7days_2023_08_21_t2
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: RareEarth_T2up
			* Amount: 15
			* ExcludedSources:
				* SellItem
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

## QL_7DAYS_2023_08_DAY1_T3
### qe_7days_2023_08_day1_a_t3
* Type:	Event
* EventId:	event_7days_2023_08_21_t3
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_T3up
			* Amount: 10
			* Analyzed: True

### qe_7days_2023_08_day1_b_t3
* Type:	Event
* EventId:	event_7days_2023_08_21_t3
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedT3
				* ShipsDestroyedT4
			* Amount: 15

### qe_7days_2023_08_day1_c_t3
* Type:	Event
* EventId:	event_7days_2023_08_21_t3
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Gas_T3up
			* Amount: 800
			* ExcludedSources:
				* PayGoal
				* QuestReward
				* MissionReward
				* BuyItem
				* SellItem
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_7days_2023_08_day1_d_t3
* Type:	Event
* EventId:	event_7days_2023_08_21_t3
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: RareEarth_T3up
			* Amount: 15
			* ExcludedSources:
				* SellItem
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

## QL_7DAYS_2023_08_DAY1_T4
### qe_7days_2023_08_day1_a_t4
* Type:	Event
* EventId:	event_7days_2023_08_21_t4
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_T4up
			* Amount: 10
			* Analyzed: True

### qe_7days_2023_08_day1_b_t4
* Type:	Event
* EventId:	event_7days_2023_08_21_t4
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedT4
			* Amount: 15

### qe_7days_2023_08_day1_c_t4
* Type:	Event
* EventId:	event_7days_2023_08_21_t4
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Gas_T4up
			* Amount: 1000
			* ExcludedSources:
				* PayGoal
				* QuestReward
				* MissionReward
				* BuyItem
				* SellItem
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_7days_2023_08_day1_d_t4
* Type:	Event
* EventId:	event_7days_2023_08_21_t4
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: RareEarth_T4up
			* Amount: 15
			* ExcludedSources:
				* SellItem
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

## QL_7DAYS_2023_08_DAY2_T1
### qe_7days_2023_08_day2_a_t1
* Type:	Event
* EventId:	event_7days_2023_08_21_t1
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: T1up

### qe_7days_2023_08_day2_b_t1
* Type:	Event
* EventId:	event_7days_2023_08_21_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T1up

### qe_7days_2023_08_day2_c_t1
* Type:	Event
* EventId:	event_7days_2023_08_21_t1
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Insignia_T1up
			* Amount: 50
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_7days_2023_08_day2_d_t1
* Type:	Event
* EventId:	event_7days_2023_08_21_t1
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 1

## QL_7DAYS_2023_08_DAY2_T2
### qe_7days_2023_08_day2_a_t2
* Type:	Event
* EventId:	event_7days_2023_08_21_t2
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: Faction_T2up

### qe_7days_2023_08_day2_b_t2
* Type:	Event
* EventId:	event_7days_2023_08_21_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Mode: Faction
			* Tags: T2up

### qe_7days_2023_08_day2_c_t2
* Type:	Event
* EventId:	event_7days_2023_08_21_t2
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* RepTr1
				* RepTanoch
				* RepYaot
				* RepAmassari
			* Amount: 135

### qe_7days_2023_08_day2_d_t2
* Type:	Event
* EventId:	event_7days_2023_08_21_t2
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 2

## QL_7DAYS_2023_08_DAY2_T3
### qe_7days_2023_08_day2_a_t3
* Type:	Event
* EventId:	event_7days_2023_08_21_t3
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: Faction_T3up

### qe_7days_2023_08_day2_b_t3
* Type:	Event
* EventId:	event_7days_2023_08_21_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Mode: Faction
			* Tags: T3up

### qe_7days_2023_08_day2_c_t3
* Type:	Event
* EventId:	event_7days_2023_08_21_t3
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* RepTr1
				* RepTanoch
				* RepYaot
				* RepAmassari
			* Amount: 180

### qe_7days_2023_08_day2_d_t3
* Type:	Event
* EventId:	event_7days_2023_08_21_t3
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 3

## QL_7DAYS_2023_08_DAY2_T4
### qe_7days_2023_08_day2_a_t4
* Type:	Event
* EventId:	event_7days_2023_08_21_t4
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: Faction_T4up

### qe_7days_2023_08_day2_b_t4
* Type:	Event
* EventId:	event_7days_2023_08_21_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Mode: Faction
			* Tags: T4up

### qe_7days_2023_08_day2_c_t4
* Type:	Event
* EventId:	event_7days_2023_08_21_t4
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* RepTr1
				* RepTanoch
				* RepYaot
				* RepAmassari
			* Amount: 225

### qe_7days_2023_08_day2_d_t4
* Type:	Event
* EventId:	event_7days_2023_08_21_t4
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 5

## QL_7DAYS_2023_08_DAY3_T1
### qe_7days_2023_08_day3_a_t1
* Type:	Event
* EventId:	event_7days_2023_08_21_t1
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Asteroid_Crud_T1up
			* Amount: 800
			* ExcludedSources:
				* PayGoal
				* QuestReward
				* MissionReward
				* BuyItem
				* SellItem
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_7days_2023_08_day3_b_t1
* Type:	Event
* EventId:	event_7days_2023_08_21_t1
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Refining
			* Tags: Asteroid_Refined_T1up
			* Amount: 500

### qe_7days_2023_08_day3_c_t1
* Type:	Event
* EventId:	event_7days_2023_08_21_t1
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: T1up
			* Amount: 1

### qe_7days_2023_08_day3_d_t1
* Type:	Event
* EventId:	event_7days_2023_08_21_t1
* Goals:
	* 0:
		* GoalType: GainItem
			* Id: CR
			* Amount: 150
			* ExcludedSources:
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
				* DismissOfficer
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer

## QL_7DAYS_2023_08_DAY3_T2
### qe_7days_2023_08_day3_a_t2
* Type:	Event
* EventId:	event_7days_2023_08_21_t2
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Asteroid_Crud_T2up
			* Amount: 1000
			* ExcludedSources:
				* PayGoal
				* QuestReward
				* MissionReward
				* BuyItem
				* SellItem
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_7days_2023_08_day3_b_t2
* Type:	Event
* EventId:	event_7days_2023_08_21_t2
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Refining
			* Tags: Asteroid_Refined_T2up
			* Amount: 500

### qe_7days_2023_08_day3_c_t2
* Type:	Event
* EventId:	event_7days_2023_08_21_t2
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: Part_T2up
			* Amount: 25

### qe_7days_2023_08_day3_d_t2
* Type:	Event
* EventId:	event_7days_2023_08_21_t2
* Goals:
	* 0:
		* GoalType: GainItem
			* Id: CR
			* Amount: 300
			* ExcludedSources:
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
				* DismissOfficer
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer

## QL_7DAYS_2023_08_DAY3_T3
### qe_7days_2023_08_day3_a_t3
* Type:	Event
* EventId:	event_7days_2023_08_21_t3
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Asteroid_Crud_T3up
			* Amount: 1200
			* ExcludedSources:
				* PayGoal
				* QuestReward
				* MissionReward
				* BuyItem
				* SellItem
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_7days_2023_08_day3_b_t3
* Type:	Event
* EventId:	event_7days_2023_08_21_t3
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Refining
			* Tags: Asteroid_Refined_T3up
			* Amount: 500

### qe_7days_2023_08_day3_c_t3
* Type:	Event
* EventId:	event_7days_2023_08_21_t3
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: Part_T3up
			* Amount: 25

### qe_7days_2023_08_day3_d_t3
* Type:	Event
* EventId:	event_7days_2023_08_21_t3
* Goals:
	* 0:
		* GoalType: GainItem
			* Id: CR
			* Amount: 600
			* ExcludedSources:
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
				* DismissOfficer
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer

## QL_7DAYS_2023_08_DAY3_T4
### qe_7days_2023_08_day3_a_t4
* Type:	Event
* EventId:	event_7days_2023_08_21_t4
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Asteroid_Crud_T4up
			* Amount: 1400
			* ExcludedSources:
				* PayGoal
				* QuestReward
				* MissionReward
				* BuyItem
				* SellItem
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_7days_2023_08_day3_b_t4
* Type:	Event
* EventId:	event_7days_2023_08_21_t4
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Refining
			* Tags: Asteroid_Refined_T4up
			* Amount: 500

### qe_7days_2023_08_day3_c_t4
* Type:	Event
* EventId:	event_7days_2023_08_21_t4
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: Part_T4up
			* Amount: 25

### qe_7days_2023_08_day3_d_t4
* Type:	Event
* EventId:	event_7days_2023_08_21_t4
* Goals:
	* 0:
		* GoalType: GainItem
			* Id: CR
			* Amount: 1200
			* ExcludedSources:
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
				* DismissOfficer
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer

## QL_7DAYS_2023_08_DAY4_T1
### qe_7days_2023_08_day4_a_t1
* Type:	Event
* EventId:	event_7days_2023_08_21_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T1up
			* Mode: Generated

### qe_7days_2023_08_day4_b_t1
* Type:	Event
* EventId:	event_7days_2023_08_21_t1
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: ProgenitorRelic_T1up
			* Amount: 1
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_7days_2023_08_day4_c_t1
* Type:	Event
* EventId:	event_7days_2023_08_21_t1
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedProgenitorT1
				* ShipsDestroyedProgenitorT2
				* ShipsDestroyedProgenitorT3
				* ShipsDestroyedProgenitorT4
			* Amount: 7

### qe_7days_2023_08_day4_d_t1
* Type:	Event
* EventId:	event_7days_2023_08_21_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Rare_T1up
			* Mode: Generated

## QL_7DAYS_2023_08_DAY4_T2
### qe_7days_2023_08_day4_a_t2
* Type:	Event
* EventId:	event_7days_2023_08_21_t2
* Goals:
	* 0:
		* GoalType: GainItem
			* Id: RP
			* Amount: 200
			* ExcludedSources:
				* SellItem
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_7days_2023_08_day4_b_t2
* Type:	Event
* EventId:	event_7days_2023_08_21_t2
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: ProgenitorRelic_T2up
			* Amount: 1
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_7days_2023_08_day4_c_t2
* Type:	Event
* EventId:	event_7days_2023_08_21_t2
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedProgenitorT2
				* ShipsDestroyedProgenitorT3
				* ShipsDestroyedProgenitorT4
			* Amount: 7

### qe_7days_2023_08_day4_d_t2
* Type:	Event
* EventId:	event_7days_2023_08_21_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Epic_T2up
			* Mode: Generated

## QL_7DAYS_2023_08_DAY4_T3
### qe_7days_2023_08_day4_a_t3
* Type:	Event
* EventId:	event_7days_2023_08_21_t3
* Goals:
	* 0:
		* GoalType: GainItem
			* Id: RP
			* Amount: 200
			* ExcludedSources:
				* SellItem
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_7days_2023_08_day4_b_t3
* Type:	Event
* EventId:	event_7days_2023_08_21_t3
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: ProgenitorRelic_T3up
			* Amount: 1
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_7days_2023_08_day4_c_t3
* Type:	Event
* EventId:	event_7days_2023_08_21_t3
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedProgenitorT3
				* ShipsDestroyedProgenitorT4
			* Amount: 7

### qe_7days_2023_08_day4_d_t3
* Type:	Event
* EventId:	event_7days_2023_08_21_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Epic_T3up
			* Mode: Generated

## QL_7DAYS_2023_08_DAY4_T4
### qe_7days_2023_08_day4_a_t4
* Type:	Event
* EventId:	event_7days_2023_08_21_t4
* Goals:
	* 0:
		* GoalType: GainItem
			* Id: RP
			* Amount: 200
			* ExcludedSources:
				* SellItem
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_7days_2023_08_day4_b_t4
* Type:	Event
* EventId:	event_7days_2023_08_21_t4
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: ProgenitorRelic_T4up
			* Amount: 1
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_7days_2023_08_day4_c_t4
* Type:	Event
* EventId:	event_7days_2023_08_21_t4
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
			* Amount: 7

### qe_7days_2023_08_day4_d_t4
* Type:	Event
* EventId:	event_7days_2023_08_21_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Epic_T4up
			* Mode: Generated

## QL_7DAYS_2023_08_DAY5_T1
### qe_7days_2023_08_day5_a_t1
* Type:	Event
* EventId:	event_7days_2023_08_21_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T1up
			* Mode: Generated

### qe_7days_2023_08_day5_b_t1
* Type:	Event
* EventId:	event_7days_2023_08_21_t1
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Insignia_T1up
			* Amount: 50
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_7days_2023_08_day5_c_t1
* Type:	Event
* EventId:	event_7days_2023_08_21_t1
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 1

### qe_7days_2023_08_day5_d_t1
* Type:	Event
* EventId:	event_7days_2023_08_21_t1
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Insignia
			* Amount: 2
			* ExcludedSources:
				* OpenContainer
				* QuestReward
				* MissionReward
				* ClaimMail
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
				* BuyItem
				* SellItem

## QL_7DAYS_2023_08_DAY5_T2
### qe_7days_2023_08_day5_a_t2
* Type:	Event
* EventId:	event_7days_2023_08_21_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T2up
			* Mode: Generated

### qe_7days_2023_08_day5_b_t2
* Type:	Event
* EventId:	event_7days_2023_08_21_t2
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Insignia_T2up
			* Amount: 50
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_7days_2023_08_day5_c_t2
* Type:	Event
* EventId:	event_7days_2023_08_21_t2
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 2

### qe_7days_2023_08_day5_d_t2
* Type:	Event
* EventId:	event_7days_2023_08_21_t2
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Insignia
			* Amount: 4
			* ExcludedSources:
				* OpenContainer
				* QuestReward
				* MissionReward
				* ClaimMail
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
				* BuyItem
				* SellItem

## QL_7DAYS_2023_08_DAY5_T3
### qe_7days_2023_08_day5_a_t3
* Type:	Event
* EventId:	event_7days_2023_08_21_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T3up
			* Mode: Generated

### qe_7days_2023_08_day5_b_t3
* Type:	Event
* EventId:	event_7days_2023_08_21_t3
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Insignia_T3up
			* Amount: 50
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_7days_2023_08_day5_c_t3
* Type:	Event
* EventId:	event_7days_2023_08_21_t3
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 3

### qe_7days_2023_08_day5_d_t3
* Type:	Event
* EventId:	event_7days_2023_08_21_t3
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Insignia
			* Amount: 6
			* ExcludedSources:
				* OpenContainer
				* QuestReward
				* MissionReward
				* ClaimMail
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
				* BuyItem
				* SellItem

## QL_7DAYS_2023_08_DAY5_T4
### qe_7days_2023_08_day5_a_t4
* Type:	Event
* EventId:	event_7days_2023_08_21_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T4up
			* Mode: Generated

### qe_7days_2023_08_day5_b_t4
* Type:	Event
* EventId:	event_7days_2023_08_21_t4
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Insignia_T4up
			* Amount: 50
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_7days_2023_08_day5_c_t4
* Type:	Event
* EventId:	event_7days_2023_08_21_t4
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 5

### qe_7days_2023_08_day5_d_t4
* Type:	Event
* EventId:	event_7days_2023_08_21_t4
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Insignia
			* Amount: 10
			* ExcludedSources:
				* OpenContainer
				* QuestReward
				* MissionReward
				* ClaimMail
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
				* BuyItem
				* SellItem

## QL_7DAYS_2023_08_DAY6_T1
### qe_7days_2023_08_day6_a_t1
* Type:	Event
* EventId:	event_7days_2023_08_21_t1
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: RareEarth_T1up
			* Amount: 15
			* ExcludedSources:
				* SellItem
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_7days_2023_08_day6_b_t1
* Type:	Event
* EventId:	event_7days_2023_08_21_t1
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 1

### qe_7days_2023_08_day6_c_t1
* Type:	Event
* EventId:	event_7days_2023_08_21_t1
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: T1up
			* Amount: 1

### qe_7days_2023_08_day6_d_t1
* Type:	Event
* EventId:	event_7days_2023_08_21_t1
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedT1
				* ShipsDestroyedT2
				* ShipsDestroyedT3
				* ShipsDestroyedT4
			* Amount: 15

## QL_7DAYS_2023_08_DAY6_T2
### qe_7days_2023_08_day6_a_t2
* Type:	Event
* EventId:	event_7days_2023_08_21_t2
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: RareEarth_T2up
			* Amount: 15
			* ExcludedSources:
				* SellItem
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_7days_2023_08_day6_b_t2
* Type:	Event
* EventId:	event_7days_2023_08_21_t2
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Upgrade
			* Tags: External_Module_T1up
			* Amount: 1

### qe_7days_2023_08_day6_c_t2
* Type:	Event
* EventId:	event_7days_2023_08_21_t2
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: Part_T2up
			* Amount: 25

### qe_7days_2023_08_day6_d_t2
* Type:	Event
* EventId:	event_7days_2023_08_21_t2
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedT2
				* ShipsDestroyedT3
				* ShipsDestroyedT4
			* Amount: 15

## QL_7DAYS_2023_08_DAY6_T3
### qe_7days_2023_08_day6_a_t3
* Type:	Event
* EventId:	event_7days_2023_08_21_t3
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: RareEarth_T3up
			* Amount: 15
			* ExcludedSources:
				* SellItem
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_7days_2023_08_day6_b_t3
* Type:	Event
* EventId:	event_7days_2023_08_21_t3
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Upgrade
			* Tags: External_Module_T2up
			* Amount: 1

### qe_7days_2023_08_day6_c_t3
* Type:	Event
* EventId:	event_7days_2023_08_21_t3
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Upgrade
			* Tags: Internal_Module_T2up
			* Amount: 1

### qe_7days_2023_08_day6_d_t3
* Type:	Event
* EventId:	event_7days_2023_08_21_t3
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedT3
				* ShipsDestroyedT4
			* Amount: 15

## QL_7DAYS_2023_08_DAY6_T4
### qe_7days_2023_08_day6_a_t4
* Type:	Event
* EventId:	event_7days_2023_08_21_t4
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: RareEarth_T4up
			* Amount: 15
			* ExcludedSources:
				* SellItem
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_7days_2023_08_day6_b_t4
* Type:	Event
* EventId:	event_7days_2023_08_21_t4
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Upgrade
			* Tags: External_Module_T3up
			* Amount: 1

### qe_7days_2023_08_day6_c_t4
* Type:	Event
* EventId:	event_7days_2023_08_21_t4
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Upgrade
			* Tags: Internal_Module_T3up
			* Amount: 1

### qe_7days_2023_08_day6_d_t4
* Type:	Event
* EventId:	event_7days_2023_08_21_t4
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedT4
			* Amount: 15

## QL_7DAYS_2023_08_DAY7_T1
### qe_7days_2023_08_day7_a_t1
* Type:	Event
* EventId:	event_7days_2023_08_21_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T1up
			* Mode: Generated

### qe_7days_2023_08_day7_b_t1
* Type:	Event
* EventId:	event_7days_2023_08_21_t1
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedT1
				* ShipsDestroyedT2
				* ShipsDestroyedT3
				* ShipsDestroyedT4
			* Amount: 15

### qe_7days_2023_08_day7_c_t1
* Type:	Event
* EventId:	event_7days_2023_08_21_t1
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Salvage_T1up
			* Amount: 3
			* ExcludedSources:
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_7days_2023_08_day7_d_t1
* Type:	Event
* EventId:	event_7days_2023_08_21_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T1up
			* Mode: Generated

## QL_7DAYS_2023_08_DAY7_T2
### qe_7days_2023_08_day7_a_t2
* Type:	Event
* EventId:	event_7days_2023_08_21_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T2up
			* Mode: Generated

### qe_7days_2023_08_day7_b_t2
* Type:	Event
* EventId:	event_7days_2023_08_21_t2
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedT2
				* ShipsDestroyedT3
				* ShipsDestroyedT4
			* Amount: 15

### qe_7days_2023_08_day7_c_t2
* Type:	Event
* EventId:	event_7days_2023_08_21_t2
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Salvage_T2up
			* Amount: 3
			* ExcludedSources:
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_7days_2023_08_day7_d_t2
* Type:	Event
* EventId:	event_7days_2023_08_21_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Mode: Strike
			* Tags: T1up

## QL_7DAYS_2023_08_DAY7_T3
### qe_7days_2023_08_day7_a_t3
* Type:	Event
* EventId:	event_7days_2023_08_21_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T3up
			* Mode: Generated

### qe_7days_2023_08_day7_b_t3
* Type:	Event
* EventId:	event_7days_2023_08_21_t3
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedT3
				* ShipsDestroyedT4
			* Amount: 15

### qe_7days_2023_08_day7_c_t3
* Type:	Event
* EventId:	event_7days_2023_08_21_t3
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Salvage_T3up
			* Amount: 3
			* ExcludedSources:
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_7days_2023_08_day7_d_t3
* Type:	Event
* EventId:	event_7days_2023_08_21_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Mode: Strike
			* Tags: T2up

## QL_7DAYS_2023_08_DAY7_T4
### qe_7days_2023_08_day7_a_t4
* Type:	Event
* EventId:	event_7days_2023_08_21_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T4up
			* Mode: Generated

### qe_7days_2023_08_day7_b_t4
* Type:	Event
* EventId:	event_7days_2023_08_21_t4
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedT4
			* Amount: 15

### qe_7days_2023_08_day7_c_t4
* Type:	Event
* EventId:	event_7days_2023_08_21_t4
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Salvage_T4up
			* Amount: 3
			* ExcludedSources:
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_7days_2023_08_day7_d_t4
* Type:	Event
* EventId:	event_7days_2023_08_21_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Mode: Strike
			* Tags: T3up

## QL_EVENT_IYAFAL_2023_T1
### qe_iyaFal_2023_day01_t1
* Type:	Event
* EventId:	event_season_iyaFal_2023_t1
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: T1up

### qe_iyaFal_2023_day02_t1
* Type:	Event
* EventId:	event_season_iyaFal_2023_t1
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Salvage_T1up
			* Amount: 5
			* ExcludedSources:
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_iyaFal_2023_day03_t1
* Type:	Event
* EventId:	event_season_iyaFal_2023_t1
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: T1up
			* Amount: 5

### qe_iyaFal_2023_day04_t1
* Type:	Event
* EventId:	event_season_iyaFal_2023_t1
* MailsOnCompletion:	m_iyaFal_day4_log
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T1up
			* Mode: Generated

### qe_iyaFal_2023_day05_t1
* Type:	Event
* EventId:	event_season_iyaFal_2023_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T1up

### qe_iyaFal_2023_day06_t1
* Type:	Event
* EventId:	event_season_iyaFal_2023_t1
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Insignia_T1up
			* Amount: 50
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_iyaFal_2023_day07_t1
* Type:	Event
* EventId:	event_season_iyaFal_2023_t1
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 1

### qe_iyaFal_2023_day08_t1
* Type:	Event
* EventId:	event_season_iyaFal_2023_t1
* MailsOnCompletion:	m_iyaFal_day8_log
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: ProgenitorRelic_T1up
			* Amount: 1
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_iyaFal_2023_day09_t1
* Type:	Event
* EventId:	event_season_iyaFal_2023_t1
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: T1up

### qe_iyaFal_2023_day10_t1
* Type:	Event
* EventId:	event_season_iyaFal_2023_t1
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Salvage_T1up
			* Amount: 5
			* ExcludedSources:
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_iyaFal_2023_day11_t1
* Type:	Event
* EventId:	event_season_iyaFal_2023_t1
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: T1up
			* Amount: 5

### qe_iyaFal_2023_day12_t1
* Type:	Event
* EventId:	event_season_iyaFal_2023_t1
* MailsOnCompletion:	m_iyaFal_day12_log
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Rare_T1up
			* Mode: Generated

### qe_iyaFal_2023_day13_t1
* Type:	Event
* EventId:	event_season_iyaFal_2023_t1
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Insignia_T1up
			* Amount: 50
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_iyaFal_2023_day14_t1
* Type:	Event
* EventId:	event_season_iyaFal_2023_t1
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: ProgenitorRelic_T1up
			* Amount: 1
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_iyaFal_2023_day15_t1
* Type:	Event
* EventId:	event_season_iyaFal_2023_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_iyaFal2023_Escort_t1

## QL_EVENT_IYAFAL_2023_EPILOG_T1
### qe_iyaFal_2023_epi01_t1
* Type:	Event
* EventId:	event_season_iyaFal_2023_t1
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Asteroid_Crud_T1up
			* Amount: 1000
			* ExcludedSources:
				* PayGoal
				* QuestReward
				* MissionReward
				* BuyItem
				* SellItem
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_iyaFal_2023_epi02_t1
* Type:	Event
* EventId:	event_season_iyaFal_2023_t1
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedProgenitorT1
				* ShipsDestroyedProgenitorT2
				* ShipsDestroyedProgenitorT3
				* ShipsDestroyedProgenitorT4
			* Amount: 10

### qe_iyaFal_2023_epi03_t1
* Type:	Event
* EventId:	event_season_iyaFal_2023_t1
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Insignia_T1up
			* Amount: 50
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_iyaFal_2023_epi04_t1
* Type:	Event
* EventId:	event_season_iyaFal_2023_t1
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 1

### qe_iyaFal_2023_epi05_t1
* Type:	Event
* EventId:	event_season_iyaFal_2023_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Rare_T1up
			* Mode: Generated

## QL_EVENT_IYAFAL_2023_T2
### qe_iyaFal_2023_day01_t2
* Type:	Event
* EventId:	event_season_iyaFal_2023_t2
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: Faction_Tr1_T2up

### qe_iyaFal_2023_day02_t2
* Type:	Event
* EventId:	event_season_iyaFal_2023_t2
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Salvage_T2up
			* Amount: 5
			* ExcludedSources:
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_iyaFal_2023_day03_t2
* Type:	Event
* EventId:	event_season_iyaFal_2023_t2
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: Part_T2up
			* Amount: 100

### qe_iyaFal_2023_day04_t2
* Type:	Event
* EventId:	event_season_iyaFal_2023_t2
* MailsOnCompletion:	m_iyaFal_day4_log
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T2up
			* Mode: Generated

### qe_iyaFal_2023_day05_t2
* Type:	Event
* EventId:	event_season_iyaFal_2023_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Mode: Faction
			* Tags: T2up

### qe_iyaFal_2023_day06_t2
* Type:	Event
* EventId:	event_season_iyaFal_2023_t2
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Insignia_T2up
			* Amount: 50
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_iyaFal_2023_day07_t2
* Type:	Event
* EventId:	event_season_iyaFal_2023_t2
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 2

### qe_iyaFal_2023_day08_t2
* Type:	Event
* EventId:	event_season_iyaFal_2023_t2
* MailsOnCompletion:	m_iyaFal_day8_log
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: ProgenitorRelic_T2up
			* Amount: 1
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_iyaFal_2023_day09_t2
* Type:	Event
* EventId:	event_season_iyaFal_2023_t2
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: Faction_Tr1_T2up

### qe_iyaFal_2023_day10_t2
* Type:	Event
* EventId:	event_season_iyaFal_2023_t2
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Salvage_T2up
			* Amount: 5
			* ExcludedSources:
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_iyaFal_2023_day11_t2
* Type:	Event
* EventId:	event_season_iyaFal_2023_t2
* Goals:
	* 0:
		* GoalType: GainItem
			* Id: RP
			* Amount: 400
			* ExcludedSources:
				* SellItem
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_iyaFal_2023_day12_t2
* Type:	Event
* EventId:	event_season_iyaFal_2023_t2
* MailsOnCompletion:	m_iyaFal_day12_log
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Epic_T2up
			* Mode: Generated

### qe_iyaFal_2023_day13_t2
* Type:	Event
* EventId:	event_season_iyaFal_2023_t2
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* SellItem
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
			* Amount: 135

### qe_iyaFal_2023_day14_t2
* Type:	Event
* EventId:	event_season_iyaFal_2023_t2
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: ProgenitorRelic_T2up
			* Amount: 1
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_iyaFal_2023_day15_t2
* Type:	Event
* EventId:	event_season_iyaFal_2023_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_iyaFal2023_Escort_t2

## QL_EVENT_IYAFAL_2023_EPILOG_T2
### qe_iyaFal_2023_epi01_t2
* Type:	Event
* EventId:	event_season_iyaFal_2023_t2
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Asteroid_Crud_T2up
			* Amount: 1200
			* ExcludedSources:
				* PayGoal
				* QuestReward
				* MissionReward
				* BuyItem
				* SellItem
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_iyaFal_2023_epi02_t2
* Type:	Event
* EventId:	event_season_iyaFal_2023_t2
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedProgenitorT2
				* ShipsDestroyedProgenitorT3
				* ShipsDestroyedProgenitorT4
			* Amount: 10

### qe_iyaFal_2023_epi03_t2
* Type:	Event
* EventId:	event_season_iyaFal_2023_t2
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Insignia_T2up
			* Amount: 50
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_iyaFal_2023_epi04_t2
* Type:	Event
* EventId:	event_season_iyaFal_2023_t2
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 2

### qe_iyaFal_2023_epi05_t2
* Type:	Event
* EventId:	event_season_iyaFal_2023_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Mode: Strike
			* Tags: T1up

## QL_EVENT_IYAFAL_2023_T3
### qe_iyaFal_2023_day01_t3
* Type:	Event
* EventId:	event_season_iyaFal_2023_t3
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: Faction_Tr1_T3up

### qe_iyaFal_2023_day02_t3
* Type:	Event
* EventId:	event_season_iyaFal_2023_t3
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Salvage_T3up
			* Amount: 5
			* ExcludedSources:
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_iyaFal_2023_day03_t3
* Type:	Event
* EventId:	event_season_iyaFal_2023_t3
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: Part_T3up
			* Amount: 100

### qe_iyaFal_2023_day04_t3
* Type:	Event
* EventId:	event_season_iyaFal_2023_t3
* MailsOnCompletion:	m_iyaFal_day4_log
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T3up
			* Mode: Generated

### qe_iyaFal_2023_day05_t3
* Type:	Event
* EventId:	event_season_iyaFal_2023_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Mode: Faction
			* Tags: T3up

### qe_iyaFal_2023_day06_t3
* Type:	Event
* EventId:	event_season_iyaFal_2023_t3
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Insignia_T3up
			* Amount: 50
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_iyaFal_2023_day07_t3
* Type:	Event
* EventId:	event_season_iyaFal_2023_t3
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 3

### qe_iyaFal_2023_day08_t3
* Type:	Event
* EventId:	event_season_iyaFal_2023_t3
* MailsOnCompletion:	m_iyaFal_day8_log
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: ProgenitorRelic_T3up
			* Amount: 1
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_iyaFal_2023_day09_t3
* Type:	Event
* EventId:	event_season_iyaFal_2023_t3
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: Faction_Tr1_T3up

### qe_iyaFal_2023_day10_t3
* Type:	Event
* EventId:	event_season_iyaFal_2023_t3
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Salvage_T3up
			* Amount: 5
			* ExcludedSources:
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_iyaFal_2023_day11_t3
* Type:	Event
* EventId:	event_season_iyaFal_2023_t3
* Goals:
	* 0:
		* GoalType: GainItem
			* Id: RP
			* Amount: 400
			* ExcludedSources:
				* SellItem
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_iyaFal_2023_day12_t3
* Type:	Event
* EventId:	event_season_iyaFal_2023_t3
* MailsOnCompletion:	m_iyaFal_day12_log
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Epic_T3up
			* Mode: Generated

### qe_iyaFal_2023_day13_t3
* Type:	Event
* EventId:	event_season_iyaFal_2023_t3
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* SellItem
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
			* Amount: 180

### qe_iyaFal_2023_day14_t3
* Type:	Event
* EventId:	event_season_iyaFal_2023_t3
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: ProgenitorRelic_T3up
			* Amount: 1
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_iyaFal_2023_day15_t3
* Type:	Event
* EventId:	event_season_iyaFal_2023_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_iyaFal2023_Escort_t3

## QL_EVENT_IYAFAL_2023_EPILOG_T3
### qe_iyaFal_2023_epi01_t3
* Type:	Event
* EventId:	event_season_iyaFal_2023_t3
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Gas_T3up
			* Amount: 1000
			* ExcludedSources:
				* PayGoal
				* QuestReward
				* MissionReward
				* BuyItem
				* SellItem
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_iyaFal_2023_epi02_t3
* Type:	Event
* EventId:	event_season_iyaFal_2023_t3
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedProgenitorT3
				* ShipsDestroyedProgenitorT4
			* Amount: 10

### qe_iyaFal_2023_epi03_t3
* Type:	Event
* EventId:	event_season_iyaFal_2023_t3
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Insignia_T3up
			* Amount: 50
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_iyaFal_2023_epi04_t3
* Type:	Event
* EventId:	event_season_iyaFal_2023_t3
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 3

### qe_iyaFal_2023_epi05_t3
* Type:	Event
* EventId:	event_season_iyaFal_2023_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Mode: Strike
			* Tags: T2up

## QL_EVENT_IYAFAL_2023_T4
### qe_iyaFal_2023_day01_t4
* Type:	Event
* EventId:	event_season_iyaFal_2023_t4
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: Faction_T4up

### qe_iyaFal_2023_day02_t4
* Type:	Event
* EventId:	event_season_iyaFal_2023_t4
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Salvage_T4up
			* Amount: 5
			* ExcludedSources:
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_iyaFal_2023_day03_t4
* Type:	Event
* EventId:	event_season_iyaFal_2023_t4
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: Part_T4up
			* Amount: 100

### qe_iyaFal_2023_day04_t4
* Type:	Event
* EventId:	event_season_iyaFal_2023_t4
* MailsOnCompletion:	m_iyaFal_day4_log
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T4up
			* Mode: Generated

### qe_iyaFal_2023_day05_t4
* Type:	Event
* EventId:	event_season_iyaFal_2023_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Mode: Faction
			* Tags: T4up

### qe_iyaFal_2023_day06_t4
* Type:	Event
* EventId:	event_season_iyaFal_2023_t4
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Insignia_T4up
			* Amount: 50
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_iyaFal_2023_day07_t4
* Type:	Event
* EventId:	event_season_iyaFal_2023_t4
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 5

### qe_iyaFal_2023_day08_t4
* Type:	Event
* EventId:	event_season_iyaFal_2023_t4
* MailsOnCompletion:	m_iyaFal_day8_log
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: ProgenitorRelic_T4up
			* Amount: 1
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_iyaFal_2023_day09_t4
* Type:	Event
* EventId:	event_season_iyaFal_2023_t4
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: Faction_T4up

### qe_iyaFal_2023_day10_t4
* Type:	Event
* EventId:	event_season_iyaFal_2023_t4
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Salvage_T4up
			* Amount: 5
			* ExcludedSources:
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_iyaFal_2023_day11_t4
* Type:	Event
* EventId:	event_season_iyaFal_2023_t4
* Goals:
	* 0:
		* GoalType: GainItem
			* Id: RP
			* Amount: 400
			* ExcludedSources:
				* SellItem
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_iyaFal_2023_day12_t4
* Type:	Event
* EventId:	event_season_iyaFal_2023_t4
* MailsOnCompletion:	m_iyaFal_day12_log
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Epic_T4up
			* Mode: Generated

### qe_iyaFal_2023_day13_t4
* Type:	Event
* EventId:	event_season_iyaFal_2023_t4
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* SellItem
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
			* Amount: 225

### qe_iyaFal_2023_day14_t4
* Type:	Event
* EventId:	event_season_iyaFal_2023_t4
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: ProgenitorRelic_T4up
			* Amount: 1
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_iyaFal_2023_day15_t4
* Type:	Event
* EventId:	event_season_iyaFal_2023_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_iyaFal2023_Escort_t4

## QL_EVENT_IYAFAL_2023_EPILOG_T4
### qe_iyaFal_2023_epi01_t4
* Type:	Event
* EventId:	event_season_iyaFal_2023_t4
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Gas_T4up
			* Amount: 1200
			* ExcludedSources:
				* PayGoal
				* QuestReward
				* MissionReward
				* BuyItem
				* SellItem
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_iyaFal_2023_epi02_t4
* Type:	Event
* EventId:	event_season_iyaFal_2023_t4
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* PayGoal
				* QuestReward
				* MissionReward
				* BuyItem
				* SellItem
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
			* Amount: 10

### qe_iyaFal_2023_epi03_t4
* Type:	Event
* EventId:	event_season_iyaFal_2023_t4
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Insignia_T4up
			* Amount: 50
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_iyaFal_2023_epi04_t4
* Type:	Event
* EventId:	event_season_iyaFal_2023_t4
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 5

### qe_iyaFal_2023_epi05_t4
* Type:	Event
* EventId:	event_season_iyaFal_2023_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 5
			* Mode: Strike
			* Tags: T3up

## QL_EVENT_ANNIVERSARY_2023_T1
### qe_anniversary_2023_day01_A_t1
* Type:	Event
* EventId:	event_anniversary_2023_t1
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: T1up
			* Amount: 1

### qe_anniversary_2023_day01_B_t1
* Type:	Event
* EventId:	event_anniversary_2023_t1
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedProgenitorT1
				* ShipsDestroyedProgenitorT2
				* ShipsDestroyedProgenitorT3
				* ShipsDestroyedProgenitorT4
			* Amount: 7

### qe_anniversary_2023_day01_C_t1
* Type:	Event
* EventId:	event_anniversary_2023_t1
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: ProgenitorRelic_T1up
			* Amount: 1
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_anniversary_2023_day02_A_t1
* Type:	Event
* EventId:	event_anniversary_2023_t1
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Asteroid_Crud_T1up
			* Amount: 800
			* ExcludedSources:
				* PayGoal
				* QuestReward
				* MissionReward
				* BuyItem
				* SellItem
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_anniversary_2023_day02_B_t1
* Type:	Event
* EventId:	event_anniversary_2023_t1
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Insignia_T1up
			* Amount: 25
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_anniversary_2023_day02_C_t1
* Type:	Event
* EventId:	event_anniversary_2023_t1
* Goals:
	* 0:
		* GoalType: GainItem
			* Id: CR
			* Amount: 1250
			* ExcludedSources:
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
				* DismissOfficer
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer

### qe_anniversary_2023_day03_A_t1
* Type:	Event
* EventId:	event_anniversary_2023_t1
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedT1
				* ShipsDestroyedT2
				* ShipsDestroyedT3
				* ShipsDestroyedT4
			* Amount: 15

### qe_anniversary_2023_day03_B_t1
* Type:	Event
* EventId:	event_anniversary_2023_t1
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Salvage_T1up
			* Amount: 3
			* ExcludedSources:
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
				* OpenContainer

### qe_anniversary_2023_day03_C_t1
* Type:	Event
* EventId:	event_anniversary_2023_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Rare_T1up
			* Mode: Generated

### qe_anniversary_2023_day04_A_t1
* Type:	Event
* EventId:	event_anniversary_2023_t1
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_T1up
			* Amount: 5
			* Analyzed: True

### qe_anniversary_2023_day04_B_t1
* Type:	Event
* EventId:	event_anniversary_2023_t1
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Asteroid_Crud_T1up
			* Amount: 800
			* ExcludedSources:
				* PayGoal
				* QuestReward
				* MissionReward
				* BuyItem
				* SellItem
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_anniversary_2023_day04_C_t1
* Type:	Event
* EventId:	event_anniversary_2023_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Rare_T1up
			* Mode: Generated

### qe_anniversary_2023_day05_A_t1
* Type:	Event
* EventId:	event_anniversary_2023_t1
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: T1up

### qe_anniversary_2023_day05_B_t1
* Type:	Event
* EventId:	event_anniversary_2023_t1
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedT1
				* ShipsDestroyedT2
				* ShipsDestroyedT3
				* ShipsDestroyedT4
			* Amount: 15

### qe_anniversary_2023_day05_C_t1
* Type:	Event
* EventId:	event_anniversary_2023_t1
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Salvage_T1up
			* Amount: 3
			* ExcludedSources:
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
				* OpenContainer

### qe_anniversary_2023_day06_A_t1
* Type:	Event
* EventId:	event_anniversary_2023_t1
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Insignia_T1up
			* Amount: 25
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_anniversary_2023_day06_B_t1
* Type:	Event
* EventId:	event_anniversary_2023_t1
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 1

### qe_anniversary_2023_day06_C_t1
* Type:	Event
* EventId:	event_anniversary_2023_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Rare_T1up
			* Mode: Generated

### qe_anniversary_2023_day07_A_t1
* Type:	Event
* EventId:	event_anniversary_2023_t1
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Asteroid_Crud_T1up
			* Amount: 800
			* ExcludedSources:
				* PayGoal
				* QuestReward
				* MissionReward
				* BuyItem
				* SellItem
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_anniversary_2023_day07_B_t1
* Type:	Event
* EventId:	event_anniversary_2023_t1
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Refining
			* Tags: Asteroid_Refined_T1up
			* Amount: 500

### qe_anniversary_2023_day07_C_t1
* Type:	Event
* EventId:	event_anniversary_2023_t1
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: T1up
			* Amount: 1

### qe_anniversary_2023_day08_A_t1
* Type:	Event
* EventId:	event_anniversary_2023_t1
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedP1T1
				* ShipsDestroyedP1T2
				* ShipsDestroyedP1T3
				* ShipsDestroyedP1T4
			* Amount: 10

### qe_anniversary_2023_day08_B_t1
* Type:	Event
* EventId:	event_anniversary_2023_t1
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Salvage_T1up
			* Amount: 3
			* ExcludedSources:
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
				* OpenContainer

### qe_anniversary_2023_day08_C_t1
* Type:	Event
* EventId:	event_anniversary_2023_t1
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedP1T1
				* ShipsDestroyedP1T2
				* ShipsDestroyedP1T3
				* ShipsDestroyedP1T4
			* Amount: 20

### qe_anniversary_2023_day09_A_t1
* Type:	Event
* EventId:	event_anniversary_2023_t1
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 1

### qe_anniversary_2023_day09_B_t1
* Type:	Event
* EventId:	event_anniversary_2023_t1
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: T1up
			* Amount: 1

### qe_anniversary_2023_day09_C_t1
* Type:	Event
* EventId:	event_anniversary_2023_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Rare_T1up
			* Mode: Generated

### qe_anniversary_2023_day10_A_t1
* Type:	Event
* EventId:	event_anniversary_2023_t1
* MailsOnCompletion:	m_anniversary_enoch_log
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_anniversary2023_Wiracoda_t1

## QL_EVENT_ANNIVERSARY_2023_T2
### qe_anniversary_2023_day01_A_t2
* Type:	Event
* EventId:	event_anniversary_2023_t2
* Goals:
	* 0:
		* GoalType: GainItem
			* Id: RP
			* Amount: 200
			* ExcludedSources:
				* SellItem
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_anniversary_2023_day01_B_t2
* Type:	Event
* EventId:	event_anniversary_2023_t2
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedProgenitorT2
				* ShipsDestroyedProgenitorT3
				* ShipsDestroyedProgenitorT4
			* Amount: 7

### qe_anniversary_2023_day01_C_t2
* Type:	Event
* EventId:	event_anniversary_2023_t2
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: ProgenitorRelic_T2up
			* Amount: 1
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_anniversary_2023_day02_A_t2
* Type:	Event
* EventId:	event_anniversary_2023_t2
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: AsteroidD_Crud_T2up
			* Amount: 400
			* ExcludedSources:
				* PayGoal
				* QuestReward
				* MissionReward
				* BuyItem
				* SellItem
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_anniversary_2023_day02_B_t2
* Type:	Event
* EventId:	event_anniversary_2023_t2
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* PayGoal
				* QuestReward
				* MissionReward
				* BuyItem
				* SellItem
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
			* Amount: 135

### qe_anniversary_2023_day02_C_t2
* Type:	Event
* EventId:	event_anniversary_2023_t2
* Goals:
	* 0:
		* GoalType: GainItem
			* Id: CR
			* Amount: 2500
			* ExcludedSources:
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
				* DismissOfficer
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer

### qe_anniversary_2023_day03_A_t2
* Type:	Event
* EventId:	event_anniversary_2023_t2
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedT2
				* ShipsDestroyedT3
				* ShipsDestroyedT4
			* Amount: 15

### qe_anniversary_2023_day03_B_t2
* Type:	Event
* EventId:	event_anniversary_2023_t2
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Salvage_T2up
			* Amount: 3
			* ExcludedSources:
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
				* OpenContainer

### qe_anniversary_2023_day03_C_t2
* Type:	Event
* EventId:	event_anniversary_2023_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Mode: Strike
			* Tags: T1up

### qe_anniversary_2023_day04_A_t2
* Type:	Event
* EventId:	event_anniversary_2023_t2
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_T2up
			* Amount: 5
			* Analyzed: True

### qe_anniversary_2023_day04_B_t2
* Type:	Event
* EventId:	event_anniversary_2023_t2
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Asteroid_Crud_T2up
			* Amount: 1000
			* ExcludedSources:
				* PayGoal
				* QuestReward
				* MissionReward
				* BuyItem
				* SellItem
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_anniversary_2023_day04_C_t2
* Type:	Event
* EventId:	event_anniversary_2023_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Epic_T2up
			* Mode: Generated

### qe_anniversary_2023_day05_A_t2
* Type:	Event
* EventId:	event_anniversary_2023_t2
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: Faction_T2up

### qe_anniversary_2023_day05_B_t2
* Type:	Event
* EventId:	event_anniversary_2023_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Mode: Faction
			* Tags: T2up_Tanoch

### qe_anniversary_2023_day05_C_t2
* Type:	Event
* EventId:	event_anniversary_2023_t2
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: RepTanoch
			* Amount: 135

### qe_anniversary_2023_day06_A_t2
* Type:	Event
* EventId:	event_anniversary_2023_t2
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Insignia_T2up
			* Amount: 25
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_anniversary_2023_day06_B_t2
* Type:	Event
* EventId:	event_anniversary_2023_t2
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 2

### qe_anniversary_2023_day06_C_t2
* Type:	Event
* EventId:	event_anniversary_2023_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Mode: Strike
			* Tags: T1up

### qe_anniversary_2023_day07_A_t2
* Type:	Event
* EventId:	event_anniversary_2023_t2
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Asteroid_Crud_T2up
			* Amount: 1000
			* ExcludedSources:
				* PayGoal
				* QuestReward
				* MissionReward
				* BuyItem
				* SellItem
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_anniversary_2023_day07_B_t2
* Type:	Event
* EventId:	event_anniversary_2023_t2
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Refining
			* Tags: Asteroid_Refined_T2up
			* Amount: 500

### qe_anniversary_2023_day07_C_t2
* Type:	Event
* EventId:	event_anniversary_2023_t2
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: Part_T2up
			* Amount: 50

### qe_anniversary_2023_day08_A_t2
* Type:	Event
* EventId:	event_anniversary_2023_t2
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedP1T2
				* ShipsDestroyedP1T3
				* ShipsDestroyedP1T4
			* Amount: 10

### qe_anniversary_2023_day08_B_t2
* Type:	Event
* EventId:	event_anniversary_2023_t2
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Salvage_T2up
			* Amount: 3
			* ExcludedSources:
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
				* OpenContainer

### qe_anniversary_2023_day08_C_t2
* Type:	Event
* EventId:	event_anniversary_2023_t2
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedP1T2
				* ShipsDestroyedP1T3
				* ShipsDestroyedP1T4
			* Amount: 20

### qe_anniversary_2023_day09_A_t2
* Type:	Event
* EventId:	event_anniversary_2023_t2
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Upgrade
			* Tags: External_Module_T1up
			* Amount: 1

### qe_anniversary_2023_day09_B_t2
* Type:	Event
* EventId:	event_anniversary_2023_t2
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: Part_T2up
			* Amount: 50

### qe_anniversary_2023_day09_C_t2
* Type:	Event
* EventId:	event_anniversary_2023_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Mode: Strike
			* Tags: T1up

### qe_anniversary_2023_day10_A_t2
* Type:	Event
* EventId:	event_anniversary_2023_t2
* MailsOnCompletion:	m_anniversary_enoch_log
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_anniversary2023_Wiracoda_t2

## QL_EVENT_ANNIVERSARY_2023_T3
### qe_anniversary_2023_day01_A_t3
* Type:	Event
* EventId:	event_anniversary_2023_t3
* Goals:
	* 0:
		* GoalType: GainItem
			* Id: RP
			* Amount: 200
			* ExcludedSources:
				* SellItem
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_anniversary_2023_day01_B_t3
* Type:	Event
* EventId:	event_anniversary_2023_t3
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedProgenitorT3
				* ShipsDestroyedProgenitorT4
			* Amount: 7

### qe_anniversary_2023_day01_C_t3
* Type:	Event
* EventId:	event_anniversary_2023_t3
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: ProgenitorRelic_T3up
			* Amount: 1
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_anniversary_2023_day02_A_t3
* Type:	Event
* EventId:	event_anniversary_2023_t3
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: AsteroidD_Crud_T3up
			* Amount: 500
			* ExcludedSources:
				* PayGoal
				* QuestReward
				* MissionReward
				* BuyItem
				* SellItem
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_anniversary_2023_day02_B_t3
* Type:	Event
* EventId:	event_anniversary_2023_t3
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* PayGoal
				* QuestReward
				* MissionReward
				* BuyItem
				* SellItem
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
			* Amount: 180

### qe_anniversary_2023_day02_C_t3
* Type:	Event
* EventId:	event_anniversary_2023_t3
* Goals:
	* 0:
		* GoalType: GainItem
			* Id: CR
			* Amount: 5000
			* ExcludedSources:
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
				* DismissOfficer
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer

### qe_anniversary_2023_day03_A_t3
* Type:	Event
* EventId:	event_anniversary_2023_t3
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedT3
				* ShipsDestroyedT4
			* Amount: 15

### qe_anniversary_2023_day03_B_t3
* Type:	Event
* EventId:	event_anniversary_2023_t3
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Salvage_T3up
			* Amount: 3
			* ExcludedSources:
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
				* OpenContainer

### qe_anniversary_2023_day03_C_t3
* Type:	Event
* EventId:	event_anniversary_2023_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Mode: Strike
			* Tags: T2up

### qe_anniversary_2023_day04_A_t3
* Type:	Event
* EventId:	event_anniversary_2023_t3
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_T3up
			* Amount: 5
			* Analyzed: True

### qe_anniversary_2023_day04_B_t3
* Type:	Event
* EventId:	event_anniversary_2023_t3
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Gas_T3up
			* Amount: 800
			* ExcludedSources:
				* PayGoal
				* QuestReward
				* MissionReward
				* BuyItem
				* SellItem
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_anniversary_2023_day04_C_t3
* Type:	Event
* EventId:	event_anniversary_2023_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Epic_T3up
			* Mode: Generated

### qe_anniversary_2023_day05_A_t3
* Type:	Event
* EventId:	event_anniversary_2023_t3
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: Faction_T3up

### qe_anniversary_2023_day05_B_t3
* Type:	Event
* EventId:	event_anniversary_2023_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Mode: Faction
			* Tags: T3up_Tanoch

### qe_anniversary_2023_day05_C_t3
* Type:	Event
* EventId:	event_anniversary_2023_t3
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: RepTanoch
			* Amount: 180

### qe_anniversary_2023_day06_A_t3
* Type:	Event
* EventId:	event_anniversary_2023_t3
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Insignia_T3up
			* Amount: 25
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_anniversary_2023_day06_B_t3
* Type:	Event
* EventId:	event_anniversary_2023_t3
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 3

### qe_anniversary_2023_day06_C_t3
* Type:	Event
* EventId:	event_anniversary_2023_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Mode: Strike
			* Tags: T2up

### qe_anniversary_2023_day07_A_t3
* Type:	Event
* EventId:	event_anniversary_2023_t3
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Asteroid_Crud_T3up
			* Amount: 1200
			* ExcludedSources:
				* PayGoal
				* QuestReward
				* MissionReward
				* BuyItem
				* SellItem
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_anniversary_2023_day07_B_t3
* Type:	Event
* EventId:	event_anniversary_2023_t3
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Refining
			* Tags: Asteroid_Refined_T3up
			* Amount: 500

### qe_anniversary_2023_day07_C_t3
* Type:	Event
* EventId:	event_anniversary_2023_t3
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: Part_T3up
			* Amount: 50

### qe_anniversary_2023_day08_A_t3
* Type:	Event
* EventId:	event_anniversary_2023_t3
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedP1T3
				* ShipsDestroyedP1T4
			* Amount: 10

### qe_anniversary_2023_day08_B_t3
* Type:	Event
* EventId:	event_anniversary_2023_t3
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Salvage_T3up
			* Amount: 3
			* ExcludedSources:
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
				* OpenContainer

### qe_anniversary_2023_day08_C_t3
* Type:	Event
* EventId:	event_anniversary_2023_t3
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Id: qr_015

### qe_anniversary_2023_day09_A_t3
* Type:	Event
* EventId:	event_anniversary_2023_t3
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Upgrade
			* Tags: External_Module_T2up
			* Amount: 1

### qe_anniversary_2023_day09_B_t3
* Type:	Event
* EventId:	event_anniversary_2023_t3
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Upgrade
			* Tags: Internal_Module_T2up
			* Amount: 1

### qe_anniversary_2023_day09_C_t3
* Type:	Event
* EventId:	event_anniversary_2023_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Mode: Strike
			* Tags: T2up

### qe_anniversary_2023_day10_A_t3
* Type:	Event
* EventId:	event_anniversary_2023_t3
* MailsOnCompletion:	m_anniversary_enoch_log
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_anniversary2023_Wiracoda_t3

## QL_EVENT_ANNIVERSARY_2023_T4
### qe_anniversary_2023_day01_A_t4
* Type:	Event
* EventId:	event_anniversary_2023_t4
* Goals:
	* 0:
		* GoalType: GainItem
			* Id: RP
			* Amount: 200
			* ExcludedSources:
				* SellItem
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_anniversary_2023_day01_B_t4
* Type:	Event
* EventId:	event_anniversary_2023_t4
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* SellItem
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
			* Amount: 7

### qe_anniversary_2023_day01_C_t4
* Type:	Event
* EventId:	event_anniversary_2023_t4
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: ProgenitorRelic_T4up
			* Amount: 1
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_anniversary_2023_day02_A_t4
* Type:	Event
* EventId:	event_anniversary_2023_t4
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: AsteroidD_Crud_T4up
			* Amount: 600
			* ExcludedSources:
				* PayGoal
				* QuestReward
				* MissionReward
				* BuyItem
				* SellItem
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_anniversary_2023_day02_B_t4
* Type:	Event
* EventId:	event_anniversary_2023_t4
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* PayGoal
				* QuestReward
				* MissionReward
				* BuyItem
				* SellItem
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
			* Amount: 225

### qe_anniversary_2023_day02_C_t4
* Type:	Event
* EventId:	event_anniversary_2023_t4
* Goals:
	* 0:
		* GoalType: GainItem
			* Id: CR
			* Amount: 10000
			* ExcludedSources:
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
				* DismissOfficer
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer

### qe_anniversary_2023_day03_A_t4
* Type:	Event
* EventId:	event_anniversary_2023_t4
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
				* DismissOfficer
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer
			* Amount: 15

### qe_anniversary_2023_day03_B_t4
* Type:	Event
* EventId:	event_anniversary_2023_t4
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Salvage_T4up
			* Amount: 3
			* ExcludedSources:
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
				* OpenContainer

### qe_anniversary_2023_day03_C_t4
* Type:	Event
* EventId:	event_anniversary_2023_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Mode: Strike
			* Tags: T3up

### qe_anniversary_2023_day04_A_t4
* Type:	Event
* EventId:	event_anniversary_2023_t4
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_T4up
			* Amount: 5
			* Analyzed: True

### qe_anniversary_2023_day04_B_t4
* Type:	Event
* EventId:	event_anniversary_2023_t4
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Gas_T4up
			* Amount: 1000
			* ExcludedSources:
				* PayGoal
				* QuestReward
				* MissionReward
				* BuyItem
				* SellItem
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_anniversary_2023_day04_C_t4
* Type:	Event
* EventId:	event_anniversary_2023_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Epic_T4up
			* Mode: Generated

### qe_anniversary_2023_day05_A_t4
* Type:	Event
* EventId:	event_anniversary_2023_t4
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: Faction_T4up

### qe_anniversary_2023_day05_B_t4
* Type:	Event
* EventId:	event_anniversary_2023_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Mode: Faction
			* Tags: T4up_Tanoch

### qe_anniversary_2023_day05_C_t4
* Type:	Event
* EventId:	event_anniversary_2023_t4
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: RepTanoch
			* Amount: 225

### qe_anniversary_2023_day06_A_t4
* Type:	Event
* EventId:	event_anniversary_2023_t4
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Insignia_T4up
			* Amount: 25
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_anniversary_2023_day06_B_t4
* Type:	Event
* EventId:	event_anniversary_2023_t4
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 5

### qe_anniversary_2023_day06_C_t4
* Type:	Event
* EventId:	event_anniversary_2023_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Mode: Strike
			* Tags: T3up

### qe_anniversary_2023_day07_A_t4
* Type:	Event
* EventId:	event_anniversary_2023_t4
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Asteroid_Crud_T4up
			* Amount: 1400
			* ExcludedSources:
				* PayGoal
				* QuestReward
				* MissionReward
				* BuyItem
				* SellItem
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_anniversary_2023_day07_B_t4
* Type:	Event
* EventId:	event_anniversary_2023_t4
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Refining
			* Tags: Asteroid_Refined_T4up
			* Amount: 500

### qe_anniversary_2023_day07_C_t4
* Type:	Event
* EventId:	event_anniversary_2023_t4
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: Part_T4up
			* Amount: 50

### qe_anniversary_2023_day08_A_t4
* Type:	Event
* EventId:	event_anniversary_2023_t4
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* PayGoal
				* QuestReward
				* MissionReward
				* BuyItem
				* SellItem
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
			* Amount: 10

### qe_anniversary_2023_day08_B_t4
* Type:	Event
* EventId:	event_anniversary_2023_t4
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Salvage_T4up
			* Amount: 3
			* ExcludedSources:
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
				* OpenContainer

### qe_anniversary_2023_day08_C_t4
* Type:	Event
* EventId:	event_anniversary_2023_t4
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Id: qr_018

### qe_anniversary_2023_day09_A_t4
* Type:	Event
* EventId:	event_anniversary_2023_t4
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Upgrade
			* Tags: External_Module_T3up
			* Amount: 1

### qe_anniversary_2023_day09_B_t4
* Type:	Event
* EventId:	event_anniversary_2023_t4
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Upgrade
			* Tags: Internal_Module_T3up
			* Amount: 1

### qe_anniversary_2023_day09_C_t4
* Type:	Event
* EventId:	event_anniversary_2023_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Mode: Strike
			* Tags: T3up

### qe_anniversary_2023_day10_A_t4
* Type:	Event
* EventId:	event_anniversary_2023_t4
* MailsOnCompletion:	m_anniversary_enoch_log
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_anniversary2023_Wiracoda_t4

## QL_EVENT_HALLOWEEN_2023_T1
### qe_halloween_2023_day01_t1
* Type:	Event
* EventId:	event_halloween_2023_t1
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedProgenitorT1
				* ShipsDestroyedProgenitorT2
				* ShipsDestroyedProgenitorT3
				* ShipsDestroyedProgenitorT4
			* Amount: 10

### qe_halloween_2023_day02_t1
* Type:	Event
* EventId:	event_halloween_2023_t1
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Asteroid_Crud_T1up
			* Amount: 800
			* ExcludedSources:
				* PayGoal
				* QuestReward
				* MissionReward
				* BuyItem
				* SellItem
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_halloween_2023_day03_t1
* Type:	Event
* EventId:	event_halloween_2023_t1
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Salvage_T1up
			* Amount: 5
			* ExcludedSources:
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
				* OpenContainer

### qe_halloween_2023_day04_t1
* Type:	Event
* EventId:	event_halloween_2023_t1
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: RareEarth_T1up
			* Amount: 20
			* ExcludedSources:
				* SellItem
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_halloween_2023_day05_t1
* Type:	Event
* EventId:	event_halloween_2023_t1
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: ProgenitorRelic_T1up
			* Amount: 1
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_halloween_2023_day06_t1
* Type:	Event
* EventId:	event_halloween_2023_t1
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: T1up
			* Amount: 5

### qe_halloween_2023_day07_t1
* Type:	Event
* EventId:	event_halloween_2023_t1
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedProgenitorT1
				* ShipsDestroyedProgenitorT2
				* ShipsDestroyedProgenitorT3
				* ShipsDestroyedProgenitorT4
			* Amount: 10

### qe_halloween_2023_day08_t1
* Type:	Event
* EventId:	event_halloween_2023_t1
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 1

### qe_halloween_2023_day09_t1
* Type:	Event
* EventId:	event_halloween_2023_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Rare_T1up
			* Mode: Generated

### qe_halloween_2023_day10_t1
* Type:	Event
* EventId:	event_halloween_2023_t1
* Goals:
	* 0:
		* GoalType: GainItem
			* Id: CR
			* Amount: 1250
			* ExcludedSources:
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
				* DismissOfficer
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer

### qe_halloween_2023_day11_t1
* Type:	Event
* EventId:	event_halloween_2023_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_halloween2023_Rashidun_t1

## QL_EVENT_HALLOWEEN_2023_T2
### qe_halloween_2023_day01_t2
* Type:	Event
* EventId:	event_halloween_2023_t2
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedProgenitorT2
				* ShipsDestroyedProgenitorT3
				* ShipsDestroyedProgenitorT4
			* Amount: 10

### qe_halloween_2023_day02_t2
* Type:	Event
* EventId:	event_halloween_2023_t2
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Asteroid_Crud_T2up
			* Amount: 1000
			* ExcludedSources:
				* PayGoal
				* QuestReward
				* MissionReward
				* BuyItem
				* SellItem
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_halloween_2023_day03_t2
* Type:	Event
* EventId:	event_halloween_2023_t2
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Salvage_T2up
			* Amount: 5
			* ExcludedSources:
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
				* OpenContainer

### qe_halloween_2023_day04_t2
* Type:	Event
* EventId:	event_halloween_2023_t2
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: RareEarth_T2up
			* Amount: 20
			* ExcludedSources:
				* SellItem
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_halloween_2023_day05_t2
* Type:	Event
* EventId:	event_halloween_2023_t2
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: ProgenitorRelic_T2up
			* Amount: 1
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_halloween_2023_day06_t2
* Type:	Event
* EventId:	event_halloween_2023_t2
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: Part_T2up
			* Amount: 100

### qe_halloween_2023_day07_t2
* Type:	Event
* EventId:	event_halloween_2023_t2
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedProgenitorT2
				* ShipsDestroyedProgenitorT3
				* ShipsDestroyedProgenitorT4
			* Amount: 10

### qe_halloween_2023_day08_t2
* Type:	Event
* EventId:	event_halloween_2023_t2
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 2

### qe_halloween_2023_day09_t2
* Type:	Event
* EventId:	event_halloween_2023_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Mode: Strike
			* Tags: T1up

### qe_halloween_2023_day10_t2
* Type:	Event
* EventId:	event_halloween_2023_t2
* Goals:
	* 0:
		* GoalType: GainItem
			* Id: CR
			* Amount: 2500
			* ExcludedSources:
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
				* DismissOfficer
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer

### qe_halloween_2023_day11_t2
* Type:	Event
* EventId:	event_halloween_2023_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_halloween2023_Rashidun_t2

## QL_EVENT_HALLOWEEN_2023_T3
### qe_halloween_2023_day01_t3
* Type:	Event
* EventId:	event_halloween_2023_t3
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedProgenitorT3
				* ShipsDestroyedProgenitorT4
			* Amount: 10

### qe_halloween_2023_day02_t3
* Type:	Event
* EventId:	event_halloween_2023_t3
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Gas_T3up
			* Amount: 1000
			* ExcludedSources:
				* PayGoal
				* QuestReward
				* MissionReward
				* BuyItem
				* SellItem
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_halloween_2023_day03_t3
* Type:	Event
* EventId:	event_halloween_2023_t3
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Salvage_T3up
			* Amount: 5
			* ExcludedSources:
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
				* OpenContainer

### qe_halloween_2023_day04_t3
* Type:	Event
* EventId:	event_halloween_2023_t3
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: RareEarth_T3up
			* Amount: 20
			* ExcludedSources:
				* SellItem
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_halloween_2023_day05_t3
* Type:	Event
* EventId:	event_halloween_2023_t3
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: ProgenitorRelic_T3up
			* Amount: 1
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_halloween_2023_day06_t3
* Type:	Event
* EventId:	event_halloween_2023_t3
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: Part_T3up
			* Amount: 100

### qe_halloween_2023_day07_t3
* Type:	Event
* EventId:	event_halloween_2023_t3
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedProgenitorT3
				* ShipsDestroyedProgenitorT4
			* Amount: 10

### qe_halloween_2023_day08_t3
* Type:	Event
* EventId:	event_halloween_2023_t3
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 3

### qe_halloween_2023_day09_t3
* Type:	Event
* EventId:	event_halloween_2023_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Mode: Strike
			* Tags: T2up

### qe_halloween_2023_day10_t3
* Type:	Event
* EventId:	event_halloween_2023_t3
* Goals:
	* 0:
		* GoalType: GainItem
			* Id: CR
			* Amount: 5000
			* ExcludedSources:
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
				* DismissOfficer
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer

### qe_halloween_2023_day11_t3
* Type:	Event
* EventId:	event_halloween_2023_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_halloween2023_Rashidun_t3

## QL_EVENT_HALLOWEEN_2023_T4
### qe_halloween_2023_day01_t4
* Type:	Event
* EventId:	event_halloween_2023_t4
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
				* DismissOfficer
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer
			* Amount: 10

### qe_halloween_2023_day02_t4
* Type:	Event
* EventId:	event_halloween_2023_t4
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Gas_T4up
			* Amount: 1200
			* ExcludedSources:
				* PayGoal
				* QuestReward
				* MissionReward
				* BuyItem
				* SellItem
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_halloween_2023_day03_t4
* Type:	Event
* EventId:	event_halloween_2023_t4
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Salvage_T4up
			* Amount: 5
			* ExcludedSources:
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
				* OpenContainer

### qe_halloween_2023_day04_t4
* Type:	Event
* EventId:	event_halloween_2023_t4
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: RareEarth_T4up
			* Amount: 20
			* ExcludedSources:
				* SellItem
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_halloween_2023_day05_t4
* Type:	Event
* EventId:	event_halloween_2023_t4
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: ProgenitorRelic_T4up
			* Amount: 1
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_halloween_2023_day06_t4
* Type:	Event
* EventId:	event_halloween_2023_t4
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: Part_T4up
			* Amount: 100

### qe_halloween_2023_day07_t4
* Type:	Event
* EventId:	event_halloween_2023_t4
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
			* Amount: 10

### qe_halloween_2023_day08_t4
* Type:	Event
* EventId:	event_halloween_2023_t4
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 5

### qe_halloween_2023_day09_t4
* Type:	Event
* EventId:	event_halloween_2023_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 5
			* Mode: Strike
			* Tags: T3up

### qe_halloween_2023_day10_t4
* Type:	Event
* EventId:	event_halloween_2023_t4
* Goals:
	* 0:
		* GoalType: GainItem
			* Id: CR
			* Amount: 10000
			* ExcludedSources:
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
				* DismissOfficer
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer

### qe_halloween_2023_day11_t4
* Type:	Event
* EventId:	event_halloween_2023_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_halloween2023_Rashidun_t4

## QL_EVENT_TANOCHWINTER_2023_T1
### qe_tanWin_2023_day01_t1
* Type:	Event
* EventId:	event_tanochWinter_2023_t1
* MailsOnCompletion:	m_tanWin_2023_d01_log
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Asteroid_Crud_T1up
			* Amount: 1000
			* ExcludedSources:
				* PayGoal
				* QuestReward
				* MissionReward
				* BuyItem
				* SellItem
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_tanWin_2023_day02_t1
* Type:	Event
* EventId:	event_tanochWinter_2023_t1
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: RareEarth_T1up
			* Amount: 50
			* ExcludedSources:
				* SellItem
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_tanWin_2023_day03_t1
* Type:	Event
* EventId:	event_tanochWinter_2023_t1
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Salvage_T1up
			* Amount: 5
			* ExcludedSources:
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
				* OpenContainer

### qe_tanWin_2023_day04_t1
* Type:	Event
* EventId:	event_tanochWinter_2023_t1
* Goals:
	* 0:
		* GoalType: GainItem
			* Id: CR
			* Amount: 1250
			* ExcludedSources:
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
				* DismissOfficer
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer

### qe_tanWin_2023_day05_t1
* Type:	Event
* EventId:	event_tanochWinter_2023_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_tanWin2023_DefendBase_t1

### qe_tanWin_2023_day06_t1
* Type:	Event
* EventId:	event_tanochWinter_2023_t1
* MailsOnCompletion:	m_tanWin_2023_d06_log
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: T1up

### qe_tanWin_2023_day07_t1
* Type:	Event
* EventId:	event_tanochWinter_2023_t1
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedT1
				* ShipsDestroyedT2
				* ShipsDestroyedT3
				* ShipsDestroyedT4
			* Amount: 15

### qe_tanWin_2023_day08_t1
* Type:	Event
* EventId:	event_tanochWinter_2023_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Rare_T1up
			* Mode: Generated

### qe_tanWin_2023_day09_t1
* Type:	Event
* EventId:	event_tanochWinter_2023_t1
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: RareEarth_T1up
			* Amount: 50
			* ExcludedSources:
				* SellItem
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_tanWin_2023_day10_t1
* Type:	Event
* EventId:	event_tanochWinter_2023_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_tanWin2023_AttackBase_t1

### qe_tanWin_2023_day11_t1
* Type:	Event
* EventId:	event_tanochWinter_2023_t1
* MailsOnCompletion:	m_tanWin_2023_d11_log
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: T1up

### qe_tanWin_2023_day12_t1
* Type:	Event
* EventId:	event_tanochWinter_2023_t1
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_T1up
			* Amount: 10
			* Analyzed: True

### qe_tanWin_2023_day13_t1
* Type:	Event
* EventId:	event_tanochWinter_2023_t1
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Insignia_T1up
			* Amount: 25
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_tanWin_2023_day14_t1
* Type:	Event
* EventId:	event_tanochWinter_2023_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Rare_T1up
			* Mode: Generated

### qe_tanWin_2023_day15_t1
* Type:	Event
* EventId:	event_tanochWinter_2023_t1
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedT1
				* ShipsDestroyedT2
				* ShipsDestroyedT3
				* ShipsDestroyedT4
			* Amount: 15

### qe_tanWin_2023_day16_t1
* Type:	Event
* EventId:	event_tanochWinter_2023_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_tanWin2023_Relic_t1

### qe_tanWin_2023_day17_t1
* Type:	Event
* EventId:	event_tanochWinter_2023_t1
* MailsOnCompletion:	m_tanWin_2023_d17_log
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: T1up

### qe_tanWin_2023_day18_t1
* Type:	Event
* EventId:	event_tanochWinter_2023_t1
* Goals:
	* 0:
		* GoalType: GainItem
			* Id: CR
			* Amount: 1250
			* ExcludedSources:
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
				* DismissOfficer
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer

### qe_tanWin_2023_day19_t1
* Type:	Event
* EventId:	event_tanochWinter_2023_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Rare_T1up
			* Mode: Generated

### qe_tanWin_2023_day20_t1
* Type:	Event
* EventId:	event_tanochWinter_2023_t1
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedT1
				* ShipsDestroyedT2
				* ShipsDestroyedT3
				* ShipsDestroyedT4
			* Amount: 15

### qe_tanWin_2023_day21_t1
* Type:	Event
* EventId:	event_tanochWinter_2023_t1
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedProgenitorT1
				* ShipsDestroyedProgenitorT2
				* ShipsDestroyedProgenitorT3
				* ShipsDestroyedProgenitorT4
			* Amount: 10

### qe_tanWin_2023_day22_t1
* Type:	Event
* EventId:	event_tanochWinter_2023_t1
* MailsOnCompletion:	m_tanWin_2023_d22_log
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_tanWin2023_Academy_t1

## QL_EVENT_TANOCHWINTER_2023_T2
### qe_tanWin_2023_day01_t2
* Type:	Event
* EventId:	event_tanochWinter_2023_t2
* MailsOnCompletion:	m_tanWin_2023_d01_log
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Asteroid_Crud_T2up
			* Amount: 1200
			* ExcludedSources:
				* PayGoal
				* QuestReward
				* MissionReward
				* BuyItem
				* SellItem
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_tanWin_2023_day02_t2
* Type:	Event
* EventId:	event_tanochWinter_2023_t2
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: RareEarth_T2up
			* Amount: 50
			* ExcludedSources:
				* SellItem
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_tanWin_2023_day03_t2
* Type:	Event
* EventId:	event_tanochWinter_2023_t2
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Salvage_T2up
			* Amount: 5
			* ExcludedSources:
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
				* OpenContainer

### qe_tanWin_2023_day04_t2
* Type:	Event
* EventId:	event_tanochWinter_2023_t2
* Goals:
	* 0:
		* GoalType: GainItem
			* Id: CR
			* Amount: 2500
			* ExcludedSources:
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
				* DismissOfficer
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer

### qe_tanWin_2023_day05_t2
* Type:	Event
* EventId:	event_tanochWinter_2023_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_tanWin2023_DefendBase_t2

### qe_tanWin_2023_day06_t2
* Type:	Event
* EventId:	event_tanochWinter_2023_t2
* MailsOnCompletion:	m_tanWin_2023_d06_log
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: Faction_Tanoch_T2up

### qe_tanWin_2023_day07_t2
* Type:	Event
* EventId:	event_tanochWinter_2023_t2
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedTanochT2
				* ShipsDestroyedTanochT3
				* ShipsDestroyedTanochT4
			* Amount: 10

### qe_tanWin_2023_day08_t2
* Type:	Event
* EventId:	event_tanochWinter_2023_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Epic_T2up
			* Mode: Generated

### qe_tanWin_2023_day09_t2
* Type:	Event
* EventId:	event_tanochWinter_2023_t2
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Upgrade
			* Tags: External_Module_T1up
			* Amount: 1

### qe_tanWin_2023_day10_t2
* Type:	Event
* EventId:	event_tanochWinter_2023_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_tanWin2023_AttackBase_t2

### qe_tanWin_2023_day11_t2
* Type:	Event
* EventId:	event_tanochWinter_2023_t2
* MailsOnCompletion:	m_tanWin_2023_d11_log
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: RepTanoch
			* Amount: 135

### qe_tanWin_2023_day12_t2
* Type:	Event
* EventId:	event_tanochWinter_2023_t2
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_T2up
			* Amount: 10
			* Analyzed: True

### qe_tanWin_2023_day13_t2
* Type:	Event
* EventId:	event_tanochWinter_2023_t2
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Insignia_T2up
			* Amount: 25
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_tanWin_2023_day14_t2
* Type:	Event
* EventId:	event_tanochWinter_2023_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Epic_T2up
			* Mode: Generated

### qe_tanWin_2023_day15_t2
* Type:	Event
* EventId:	event_tanochWinter_2023_t2
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedTanochT2
				* ShipsDestroyedTanochT3
				* ShipsDestroyedTanochT4
			* Amount: 10

### qe_tanWin_2023_day16_t2
* Type:	Event
* EventId:	event_tanochWinter_2023_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_tanWin2023_Relic_t2

### qe_tanWin_2023_day17_t2
* Type:	Event
* EventId:	event_tanochWinter_2023_t2
* MailsOnCompletion:	m_tanWin_2023_d17_log
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: Faction_Tanoch_T2up

### qe_tanWin_2023_day18_t2
* Type:	Event
* EventId:	event_tanochWinter_2023_t2
* Goals:
	* 0:
		* GoalType: GainItem
			* Id: CR
			* Amount: 2500
			* ExcludedSources:
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
				* DismissOfficer
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer

### qe_tanWin_2023_day19_t2
* Type:	Event
* EventId:	event_tanochWinter_2023_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Epic_T2up
			* Mode: Generated

### qe_tanWin_2023_day20_t2
* Type:	Event
* EventId:	event_tanochWinter_2023_t2
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedTanochT2
				* ShipsDestroyedTanochT3
				* ShipsDestroyedTanochT4
			* Amount: 10

### qe_tanWin_2023_day21_t2
* Type:	Event
* EventId:	event_tanochWinter_2023_t2
* Goals:
	* 0:
		* GoalType: GainItem
			* Id: RP
			* Amount: 200
			* ExcludedSources:
				* SellItem
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_tanWin_2023_day22_t2
* Type:	Event
* EventId:	event_tanochWinter_2023_t2
* MailsOnCompletion:	m_tanWin_2023_d22_log
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_tanWin2023_Academy_t2

## QL_EVENT_TANOCHWINTER_2023_T3
### qe_tanWin_2023_day01_t3
* Type:	Event
* EventId:	event_tanochWinter_2023_t3
* MailsOnCompletion:	m_tanWin_2023_d01_log
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Gas_T3up
			* Amount: 1000
			* ExcludedSources:
				* PayGoal
				* QuestReward
				* MissionReward
				* BuyItem
				* SellItem
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_tanWin_2023_day02_t3
* Type:	Event
* EventId:	event_tanochWinter_2023_t3
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: RareEarth_T3up
			* Amount: 50
			* ExcludedSources:
				* SellItem
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_tanWin_2023_day03_t3
* Type:	Event
* EventId:	event_tanochWinter_2023_t3
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Salvage_T3up
			* Amount: 5
			* ExcludedSources:
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
				* OpenContainer

### qe_tanWin_2023_day04_t3
* Type:	Event
* EventId:	event_tanochWinter_2023_t3
* Goals:
	* 0:
		* GoalType: GainItem
			* Id: CR
			* Amount: 5000
			* ExcludedSources:
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
				* DismissOfficer
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer

### qe_tanWin_2023_day05_t3
* Type:	Event
* EventId:	event_tanochWinter_2023_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_tanWin2023_DefendBase_t3

### qe_tanWin_2023_day06_t3
* Type:	Event
* EventId:	event_tanochWinter_2023_t3
* MailsOnCompletion:	m_tanWin_2023_d06_log
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: Faction_Tanoch_T3up

### qe_tanWin_2023_day07_t3
* Type:	Event
* EventId:	event_tanochWinter_2023_t3
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedTanochT3
				* ShipsDestroyedTanochT4
			* Amount: 10

### qe_tanWin_2023_day08_t3
* Type:	Event
* EventId:	event_tanochWinter_2023_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Epic_T3up
			* Mode: Generated

### qe_tanWin_2023_day09_t3
* Type:	Event
* EventId:	event_tanochWinter_2023_t3
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Upgrade
			* Tags: External_Module_T2up
			* Amount: 1

### qe_tanWin_2023_day10_t3
* Type:	Event
* EventId:	event_tanochWinter_2023_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_tanWin2023_AttackBase_t3

### qe_tanWin_2023_day11_t3
* Type:	Event
* EventId:	event_tanochWinter_2023_t3
* MailsOnCompletion:	m_tanWin_2023_d11_log
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: RepTanoch
			* Amount: 180

### qe_tanWin_2023_day12_t3
* Type:	Event
* EventId:	event_tanochWinter_2023_t3
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_T3up
			* Amount: 10
			* Analyzed: True

### qe_tanWin_2023_day13_t3
* Type:	Event
* EventId:	event_tanochWinter_2023_t3
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Insignia_T3up
			* Amount: 25
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_tanWin_2023_day14_t3
* Type:	Event
* EventId:	event_tanochWinter_2023_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Epic_T3up
			* Mode: Generated

### qe_tanWin_2023_day15_t3
* Type:	Event
* EventId:	event_tanochWinter_2023_t3
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedTanochT3
				* ShipsDestroyedTanochT4
			* Amount: 10

### qe_tanWin_2023_day16_t3
* Type:	Event
* EventId:	event_tanochWinter_2023_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_tanWin2023_Relic_t3

### qe_tanWin_2023_day17_t3
* Type:	Event
* EventId:	event_tanochWinter_2023_t3
* MailsOnCompletion:	m_tanWin_2023_d17_log
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: Faction_Tanoch_T3up

### qe_tanWin_2023_day18_t3
* Type:	Event
* EventId:	event_tanochWinter_2023_t3
* Goals:
	* 0:
		* GoalType: GainItem
			* Id: CR
			* Amount: 5000
			* ExcludedSources:
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
				* DismissOfficer
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer

### qe_tanWin_2023_day19_t3
* Type:	Event
* EventId:	event_tanochWinter_2023_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Epic_T3up
			* Mode: Generated

### qe_tanWin_2023_day20_t3
* Type:	Event
* EventId:	event_tanochWinter_2023_t3
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedTanochT3
				* ShipsDestroyedTanochT4
			* Amount: 10

### qe_tanWin_2023_day21_t3
* Type:	Event
* EventId:	event_tanochWinter_2023_t3
* Goals:
	* 0:
		* GoalType: GainItem
			* Id: RP
			* Amount: 200
			* ExcludedSources:
				* SellItem
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_tanWin_2023_day22_t3
* Type:	Event
* EventId:	event_tanochWinter_2023_t3
* MailsOnCompletion:	m_tanWin_2023_d22_log
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_tanWin2023_Academy_t3

## QL_EVENT_TANOCHWINTER_2023_T4
### qe_tanWin_2023_day01_t4
* Type:	Event
* EventId:	event_tanochWinter_2023_t4
* MailsOnCompletion:	m_tanWin_2023_d01_log
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Gas_T4up
			* Amount: 1200
			* ExcludedSources:
				* PayGoal
				* QuestReward
				* MissionReward
				* BuyItem
				* SellItem
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_tanWin_2023_day02_t4
* Type:	Event
* EventId:	event_tanochWinter_2023_t4
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: RareEarth_T4up
			* Amount: 50
			* ExcludedSources:
				* SellItem
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_tanWin_2023_day03_t4
* Type:	Event
* EventId:	event_tanochWinter_2023_t4
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Salvage_T4up
			* Amount: 5
			* ExcludedSources:
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
				* OpenContainer

### qe_tanWin_2023_day04_t4
* Type:	Event
* EventId:	event_tanochWinter_2023_t4
* Goals:
	* 0:
		* GoalType: GainItem
			* Id: CR
			* Amount: 10000
			* ExcludedSources:
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
				* DismissOfficer
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer

### qe_tanWin_2023_day05_t4
* Type:	Event
* EventId:	event_tanochWinter_2023_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_tanWin2023_DefendBase_t4

### qe_tanWin_2023_day06_t4
* Type:	Event
* EventId:	event_tanochWinter_2023_t4
* MailsOnCompletion:	m_tanWin_2023_d06_log
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: Faction_Tanoch_T4up

### qe_tanWin_2023_day07_t4
* Type:	Event
* EventId:	event_tanochWinter_2023_t4
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
				* DismissOfficer
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer
			* Amount: 10

### qe_tanWin_2023_day08_t4
* Type:	Event
* EventId:	event_tanochWinter_2023_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Epic_T4up
			* Mode: Generated

### qe_tanWin_2023_day09_t4
* Type:	Event
* EventId:	event_tanochWinter_2023_t4
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Upgrade
			* Tags: External_Module_T3up
			* Amount: 1

### qe_tanWin_2023_day10_t4
* Type:	Event
* EventId:	event_tanochWinter_2023_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_tanWin2023_AttackBase_t4

### qe_tanWin_2023_day11_t4
* Type:	Event
* EventId:	event_tanochWinter_2023_t4
* MailsOnCompletion:	m_tanWin_2023_d11_log
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: RepTanoch
			* Amount: 225

### qe_tanWin_2023_day12_t4
* Type:	Event
* EventId:	event_tanochWinter_2023_t4
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_T4up
			* Amount: 10
			* Analyzed: True

### qe_tanWin_2023_day13_t4
* Type:	Event
* EventId:	event_tanochWinter_2023_t4
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Insignia_T4up
			* Amount: 25
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_tanWin_2023_day14_t4
* Type:	Event
* EventId:	event_tanochWinter_2023_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Epic_T4up
			* Mode: Generated

### qe_tanWin_2023_day15_t4
* Type:	Event
* EventId:	event_tanochWinter_2023_t4
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
			* Amount: 10

### qe_tanWin_2023_day16_t4
* Type:	Event
* EventId:	event_tanochWinter_2023_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_tanWin2023_Relic_t4

### qe_tanWin_2023_day17_t4
* Type:	Event
* EventId:	event_tanochWinter_2023_t4
* MailsOnCompletion:	m_tanWin_2023_d17_log
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: Faction_Tanoch_T4up

### qe_tanWin_2023_day18_t4
* Type:	Event
* EventId:	event_tanochWinter_2023_t4
* Goals:
	* 0:
		* GoalType: GainItem
			* Id: CR
			* Amount: 10000
			* ExcludedSources:
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
				* DismissOfficer
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer

### qe_tanWin_2023_day19_t4
* Type:	Event
* EventId:	event_tanochWinter_2023_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Epic_T4up
			* Mode: Generated

### qe_tanWin_2023_day20_t4
* Type:	Event
* EventId:	event_tanochWinter_2023_t4
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
				* DismissOfficer
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer
			* Amount: 10

### qe_tanWin_2023_day21_t4
* Type:	Event
* EventId:	event_tanochWinter_2023_t4
* Goals:
	* 0:
		* GoalType: GainItem
			* Id: RP
			* Amount: 200
			* ExcludedSources:
				* SellItem
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_tanWin_2023_day22_t4
* Type:	Event
* EventId:	event_tanochWinter_2023_t4
* MailsOnCompletion:	m_tanWin_2023_d22_log
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_tanWin2023_Academy_t4

## QL_EVENT_YAOTSPRING_2024_T1
### qe_yaoSpr_2024_day01_t1
* Type:	Event
* EventId:	event_yaotSpring_2024_t1
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: T1up

### qe_yaoSpr_2024_day02_t1
* Type:	Event
* EventId:	event_yaotSpring_2024_t1
* Goals:
	* 0:
		* GoalType: GainItem
			* Id: CR
			* Amount: 1250
			* ExcludedSources:
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
				* DismissOfficer
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer

### qe_yaoSpr_2024_day03_t1
* Type:	Event
* EventId:	event_yaotSpring_2024_t1
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_T1up
			* Amount: 5
			* Analyzed: True

### qe_yaoSpr_2024_day04_t1
* Type:	Event
* EventId:	event_yaotSpring_2024_t1
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Salvage_T1up
			* Amount: 5
			* ExcludedSources:
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
				* OpenContainer

### qe_yaoSpr_2024_day05_t1
* Type:	Event
* EventId:	event_yaotSpring_2024_t1
* Goals:
	* 0:
		* GoalType: GainItem
			* Id: LP
			* Amount: 10
			* ExcludedSources:
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
				* DismissOfficer
				* OpenContainer
				* ClaimMail
				* DismantleItem

### qe_yaoSpr_2024_day06_t1
* Type:	Event
* EventId:	event_yaotSpring_2024_t1
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: T1up
			* Amount: 1

### qe_yaoSpr_2024_day07_t1
* Type:	Event
* EventId:	event_yaotSpring_2024_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Rare_T1up
			* Mode: Generated

### qe_yaoSpr_2024_day08_t1
* Type:	Event
* EventId:	event_yaotSpring_2024_t1
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Insignia_T1up
			* Amount: 50
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_yaoSpr_2024_day09_t1
* Type:	Event
* EventId:	event_yaotSpring_2024_t1
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: T1up

### qe_yaoSpr_2024_day10_t1
* Type:	Event
* EventId:	event_yaotSpring_2024_t1
* Goals:
	* 0:
		* GoalType: Pay
			* Id: questItem_progenitorRelic_t1
			* Amount: 1

### qe_yaoSpr_2024_day11_t1
* Type:	Event
* EventId:	event_yaotSpring_2024_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Rare_T1up
			* Mode: Generated

### qe_yaoSpr_2024_day12_t1
* Type:	Event
* EventId:	event_yaotSpring_2024_t1
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Asteroid_Crud_T1up
			* Amount: 1000
			* ExcludedSources:
				* PayGoal
				* QuestReward
				* MissionReward
				* BuyItem
				* SellItem
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_yaoSpr_2024_day13_t1
* Type:	Event
* EventId:	event_yaotSpring_2024_t1
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 1

### qe_yaoSpr_2024_day14_t1
* Type:	Event
* EventId:	event_yaotSpring_2024_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_yaoSpr2024_Conjunction_t1

## QL_EVENT_YAOTSPRING_2024_T2
### qe_yaoSpr_2024_day01_t2
* Type:	Event
* EventId:	event_yaotSpring_2024_t2
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: Faction_Tr1_T2up

### qe_yaoSpr_2024_day02_t2
* Type:	Event
* EventId:	event_yaotSpring_2024_t2
* Goals:
	* 0:
		* GoalType: GainItem
			* Id: CR
			* Amount: 2500
			* ExcludedSources:
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
				* DismissOfficer
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer

### qe_yaoSpr_2024_day03_t2
* Type:	Event
* EventId:	event_yaotSpring_2024_t2
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_T2up
			* Amount: 5
			* Analyzed: True

### qe_yaoSpr_2024_day04_t2
* Type:	Event
* EventId:	event_yaotSpring_2024_t2
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Salvage_T2up
			* Amount: 5
			* ExcludedSources:
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
				* OpenContainer

### qe_yaoSpr_2024_day05_t2
* Type:	Event
* EventId:	event_yaotSpring_2024_t2
* Goals:
	* 0:
		* GoalType: GainItem
			* Id: LP
			* Amount: 10
			* ExcludedSources:
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
				* DismissOfficer
				* OpenContainer
				* ClaimMail
				* DismantleItem

### qe_yaoSpr_2024_day06_t2
* Type:	Event
* EventId:	event_yaotSpring_2024_t2
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: Part_T2up
			* Amount: 100

### qe_yaoSpr_2024_day07_t2
* Type:	Event
* EventId:	event_yaotSpring_2024_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Epic_T2up
			* Mode: Generated

### qe_yaoSpr_2024_day08_t2
* Type:	Event
* EventId:	event_yaotSpring_2024_t2
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Insignia_T2up
			* Amount: 50
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_yaoSpr_2024_day09_t2
* Type:	Event
* EventId:	event_yaotSpring_2024_t2
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: T2up

### qe_yaoSpr_2024_day10_t2
* Type:	Event
* EventId:	event_yaotSpring_2024_t2
* Goals:
	* 0:
		* GoalType: Pay
			* Id: questItem_progenitorRelic_t2
			* Amount: 1

### qe_yaoSpr_2024_day11_t2
* Type:	Event
* EventId:	event_yaotSpring_2024_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Epic_T2up
			* Mode: Generated

### qe_yaoSpr_2024_day12_t2
* Type:	Event
* EventId:	event_yaotSpring_2024_t2
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Asteroid_Crud_T2up
			* Amount: 1200
			* ExcludedSources:
				* PayGoal
				* QuestReward
				* MissionReward
				* BuyItem
				* SellItem
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_yaoSpr_2024_day13_t2
* Type:	Event
* EventId:	event_yaotSpring_2024_t2
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 2

### qe_yaoSpr_2024_day14_t2
* Type:	Event
* EventId:	event_yaotSpring_2024_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_yaoSpr2024_Conjunction_t2

## QL_EVENT_YAOTSPRING_2024_T3
### qe_yaoSpr_2024_day01_t3
* Type:	Event
* EventId:	event_yaotSpring_2024_t3
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: Faction_Tr1_T3up

### qe_yaoSpr_2024_day02_t3
* Type:	Event
* EventId:	event_yaotSpring_2024_t3
* Goals:
	* 0:
		* GoalType: GainItem
			* Id: CR
			* Amount: 5000
			* ExcludedSources:
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
				* DismissOfficer
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer

### qe_yaoSpr_2024_day03_t3
* Type:	Event
* EventId:	event_yaotSpring_2024_t3
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_T3up
			* Amount: 5
			* Analyzed: True

### qe_yaoSpr_2024_day04_t3
* Type:	Event
* EventId:	event_yaotSpring_2024_t3
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Salvage_T3up
			* Amount: 5
			* ExcludedSources:
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
				* OpenContainer

### qe_yaoSpr_2024_day05_t3
* Type:	Event
* EventId:	event_yaotSpring_2024_t3
* Goals:
	* 0:
		* GoalType: GainItem
			* Id: LP
			* Amount: 10
			* ExcludedSources:
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
				* DismissOfficer
				* OpenContainer
				* ClaimMail
				* DismantleItem

### qe_yaoSpr_2024_day06_t3
* Type:	Event
* EventId:	event_yaotSpring_2024_t3
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: Part_T3up
			* Amount: 100

### qe_yaoSpr_2024_day07_t3
* Type:	Event
* EventId:	event_yaotSpring_2024_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Epic_T3up
			* Mode: Generated

### qe_yaoSpr_2024_day08_t3
* Type:	Event
* EventId:	event_yaotSpring_2024_t3
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Insignia_T3up
			* Amount: 50
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_yaoSpr_2024_day09_t3
* Type:	Event
* EventId:	event_yaotSpring_2024_t3
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: Faction_Yaot_T3up

### qe_yaoSpr_2024_day10_t3
* Type:	Event
* EventId:	event_yaotSpring_2024_t3
* Goals:
	* 0:
		* GoalType: Pay
			* Id: questItem_progenitorRelic_t3
			* Amount: 1

### qe_yaoSpr_2024_day11_t3
* Type:	Event
* EventId:	event_yaotSpring_2024_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Epic_T3up
			* Mode: Generated

### qe_yaoSpr_2024_day12_t3
* Type:	Event
* EventId:	event_yaotSpring_2024_t3
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Asteroid_Crud_T3up
			* Amount: 1400
			* ExcludedSources:
				* PayGoal
				* QuestReward
				* MissionReward
				* BuyItem
				* SellItem
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_yaoSpr_2024_day13_t3
* Type:	Event
* EventId:	event_yaotSpring_2024_t3
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 3

### qe_yaoSpr_2024_day14_t3
* Type:	Event
* EventId:	event_yaotSpring_2024_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_yaoSpr2024_Conjunction_t3

## QL_EVENT_YAOTSPRING_2024_T4
### qe_yaoSpr_2024_day01_t4
* Type:	Event
* EventId:	event_yaotSpring_2024_t4
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: Faction_Tr1_T4up

### qe_yaoSpr_2024_day02_t4
* Type:	Event
* EventId:	event_yaotSpring_2024_t4
* Goals:
	* 0:
		* GoalType: GainItem
			* Id: CR
			* Amount: 10000
			* ExcludedSources:
				* BuyItem
				* QuestReward
				* MissionReward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
				* DismissOfficer
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer

### qe_yaoSpr_2024_day03_t4
* Type:	Event
* EventId:	event_yaotSpring_2024_t4
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_T4up
			* Amount: 5
			* Analyzed: True

### qe_yaoSpr_2024_day04_t4
* Type:	Event
* EventId:	event_yaotSpring_2024_t4
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Salvage_T4up
			* Amount: 5
			* ExcludedSources:
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
				* OpenContainer

### qe_yaoSpr_2024_day05_t4
* Type:	Event
* EventId:	event_yaotSpring_2024_t4
* Goals:
	* 0:
		* GoalType: GainItem
			* Id: LP
			* Amount: 10
			* ExcludedSources:
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
				* DismissOfficer
				* OpenContainer
				* ClaimMail
				* DismantleItem

### qe_yaoSpr_2024_day06_t4
* Type:	Event
* EventId:	event_yaotSpring_2024_t4
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: Part_T4up
			* Amount: 100

### qe_yaoSpr_2024_day07_t4
* Type:	Event
* EventId:	event_yaotSpring_2024_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Epic_T4up
			* Mode: Generated

### qe_yaoSpr_2024_day08_t4
* Type:	Event
* EventId:	event_yaotSpring_2024_t4
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Insignia_T4up
			* Amount: 50
			* ExcludedSources:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_yaoSpr_2024_day09_t4
* Type:	Event
* EventId:	event_yaotSpring_2024_t4
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: Faction_Yaot_T4up

### qe_yaoSpr_2024_day10_t4
* Type:	Event
* EventId:	event_yaotSpring_2024_t4
* Goals:
	* 0:
		* GoalType: Pay
			* Id: questItem_progenitorRelic_t4
			* Amount: 1

### qe_yaoSpr_2024_day11_t4
* Type:	Event
* EventId:	event_yaotSpring_2024_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Epic_T4up
			* Mode: Generated

### qe_yaoSpr_2024_day12_t4
* Type:	Event
* EventId:	event_yaotSpring_2024_t4
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Asteroid_Crud_T4up
			* Amount: 1600
			* ExcludedSources:
				* PayGoal
				* QuestReward
				* MissionReward
				* BuyItem
				* SellItem
				* OpenContainer
				* ClaimMail
				* DismantleItem
				* LevelUpPlayer
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

### qe_yaoSpr_2024_day13_t4
* Type:	Event
* EventId:	event_yaotSpring_2024_t4
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 5

### qe_yaoSpr_2024_day14_t4
* Type:	Event
* EventId:	event_yaotSpring_2024_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_yaoSpr2024_Conjunction_t4

## QL_TEST
### qt_001
* Type:	Side
* MailsOnCompletion:	m_qt_001
* Goals:
	* 0:
		* GoalType: Pay
			* Id: 1A
			* Amount: 500
		* GoalType: Pay
			* Id: 1B
			* Amount: 250

## QL_TEST2
### qt_002
* Type:	Side
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Ids:
				* story_A02_WiracodaGate
				* story_A03_GulfTaln

## QL_TEST3
### qt_003
* Type:	Side
* Goals:
	* 0:
		* GoalType: GainItem
			* Id: CR
			* Amount: 100
			* ExcludedSources:
				* Shop
				* Reward
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash

## QL_TEST4
### qt_004
* Type:	Side
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Mode: Faction
			* Tags: Tanoch_T3up

## QL_TESTQUESTDIALOG
### qm_testQuestDialog
* Type:	Main
* Goals:
	* 0:
		* GoalType: Goto
			* Target: [-1785, -690]
	* 1:
		* GoalType: Goto
			* Target: [-1844, -690]
	* 2:
		* GoalType: Goto
			* Target: [-1785, -690]
		* GoalType: Goto
			* Target: [-1844, -690]

## QL_TESTDISMISSOFFICERS
### qt_testDismissOfficers
* Type:	Side
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Insignia
			* Amount: 1
			* ExcludedSources:
				* OpenContainer
				* QuestReward
				* MissionReward
				* ClaimMail
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
				* BuyItem
				* SellItem

## QL_TEST_STRIKE_13
### qt_test_strike_13
* Type:	Main
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Ids:
				* qr
				* 013

## QL_TEST_STRIKE_16
### qt_test_strike_16
* Type:	Main
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Ids:
				* qr
				* 016

## QL_TEST_STRIKE_14
### qt_test_strike_14
* Type:	Main
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Ids:
				* qr
				* 014

## QL_TEST_STRIKE_17
### qt_test_strike_17
* Type:	Main
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Ids:
				* qr
				* 017

## QL_TEST_STRIKE_21
### qt_test_strike_21
* Type:	Main
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Ids:
				* qr
				* 021

## QL_TEST_STRIKE_15
### qt_test_strike_15
* Type:	Main
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Ids:
				* qr
				* 015

## QL_TEST_STRIKE_18
### qt_test_strike_18
* Type:	Main
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Ids:
				* qr
				* 018

## QL_TEST_STRIKE_22
### qt_test_strike_22
* Type:	Main
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Ids:
				* qr
				* 022

## QL_TEST_STRIKE_19
### qt_test_strike_19
* Type:	Main
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Ids:
				* qr
				* 019

## QL_TEST_STRIKE_20
### qt_test_strike_20
* Type:	Main
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Ids:
				* qr
				* 020

## QL_A_001
### qa_001
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: Mined1A
			* Total: 3000

### qa_002
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: Upgrade
			* Amount: 5

## QL_TEST_GGF_STORY
### qs_s2_01_sijinLighthouse
* Type:	Side
* FollowUps: ql_raid_019
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: story_D01_SijinLighthouse

### qs_s2_01_iliyinLighthouse
* Type:	Side
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: story_D02_IliyinLighthouse

### qs_s2_01_bTemple
* Type:	Side
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: story_D03_BrightTemple

### qs_s2_01_hataldan
* Type:	Side
* FollowUps: ql_raid_020
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: story_D04_Hataldan

## QL_COMPENSATION_LVLUP
### q_compensation_lvl_10
* Type:	Event
* EventId:	event_levelUpCompensationQuests
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: PlayerXP
			* Total: 12600

### q_compensation_lvl_20
* Type:	Event
* EventId:	event_levelUpCompensationQuests
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: PlayerXP
			* Total: 36100

### q_compensation_lvl_35
* Type:	Event
* EventId:	event_levelUpCompensationQuests
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: PlayerXP
			* Total: 90100

### q_compensation_lvl_50
* Type:	Event
* EventId:	event_levelUpCompensationQuests
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: PlayerXP
			* Total: 166600

### q_compensation_lvl_75
* Type:	Event
* EventId:	event_levelUpCompensationQuests
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: PlayerXP
			* Total: 344100

### q_compensation_lvl_100
* Type:	Event
* EventId:	event_levelUpCompensationQuests
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: PlayerXP
			* Total: 584100

### q_compensation_lvl_150
* Type:	Event
* EventId:	event_levelUpCompensationQuests
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: PlayerXP
			* Total: 1251600

### q_compensation_lvl_200
* Type:	Event
* EventId:	event_levelUpCompensationQuests
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: PlayerXP
			* Total: 2169100

### q_compensation_lvl_300
* Type:	Event
* EventId:	event_levelUpCompensationQuests
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: PlayerXP
			* Total: 4754100

## Q_TEST_YAO_SPRING
### q_test_yaoSpr_2024_day04_t4
* Type:	Side
* Goals:
	* 0:
		* GoalType: GainItem
			* Tags: Salvage_T4up
			* Amount: 5
			* ExcludedSources:
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
				* OpenContainer
