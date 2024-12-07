# HWM QUESTLINES WITH QUESTS


## QL_SIDE_EXPLORATION
### qs_exploration_01:
* Name: Exploration I
* Description: We should explore this galaxy further. Who knows what we could find.
* QuestLine: ql_side_exploration
* Type: Side
* FollowUps: ql_side_001
* Goals:
	* Task 1: 
		* Scan
		* Complete 10 side missions

### qs_exploration_02:
* Name: Exploration II
* Description: We have made discoveries that will keep our scientists busy for months.
* QuestLine: ql_side_exploration
* Type: Side
* FollowUps: ql_side_002
* Goals:
	* Task 1: GainItem

### qs_exploration_03:
* Name: Exploration III
* Description: This galaxy is full of danger and opportunity. We should analyze and prepare.
* QuestLine: ql_side_exploration
* Type: Side
* FollowUps: ql_Ytep
* Goals:
	* Task 1: Scan
	* Task 2: Pay 5000 RU Type C Refined T2

## QL_SIDE_001
### qs_economy_01:
* Name: Production I
* Description: Building up a fleet requires a constant supply of materials.
* QuestLine: ql_side_001
* Type: Side
* Goals:
	* Task 1: 
		* Craft
		* Complete 5 side missions

### qs_economy_02:
* Name: Production II
* Description: We should not let our fabrication modules go idle.
* QuestLine: ql_side_001
* Type: Side
* Goals:
	* Task 1: Craft

### qs_economy_03:
* Name: Production III
* Description: Building bigger and greater ships will require bigger and greater materials.
* QuestLine: ql_side_001
* Type: Side
* Goals:
	* Task 1: Craft
	* Task 2: Pay 5000 RU Type A Refined T2

## QL_SIDE_002
### qs_battle_01:
* Name: Combat I
* Description: Space is full of danger. We need to be prepared.
* QuestLine: ql_side_002
* Type: Side
* Goals:
	* Task 1: 
		* Craft
		* Complete 15 side missions

### qs_battle_02:
* Name: Combat II
* Description: We need allies if we are to survive in this galaxy.
* QuestLine: ql_side_002
* Type: Side
* Goals:
	* Task 1: 25 Faction_T2up

### qs_battle_03:
* Name: Combat III
* Description: Only great challenges yield great rewards.
* QuestLine: ql_side_002
* Type: Side
* Goals:
	* Task 1: Complete side mission
	* Task 2: Pay 5000 RU Type B Refined T2

## QL_SIDE_UNLOCKSTRIKES_T2
### qs_unlockStrikes_t2:
* Name: Rising to the Challenge
* Description: As we venture further into this galaxy, we will encounter greater and greater threats. We need to be prepared.
* QuestLine: ql_side_unlockStrikes_t2
* Type: Side
* FollowUps:
	* ql_raid_014
	* ql_raid_015
	* ql_raid_016
* Goals:
	* Task 1: Equip Flagship

## QL_SIDE_UNLOCKSTRIKES_T3
### qs_unlockStrikes_t3:
* Name: Rising to the Challenge
* Description: As we venture further into this galaxy, we will encounter greater and greater threats. We need to be prepared.
* QuestLine: ql_side_unlockStrikes_t3
* Type: Side
* FollowUps:
	* ql_raid_017
	* ql_raid_018
* Goals:
	* Task 1: Equip Flagship

## QL_MAIN_T0_TUTORIAL
### qm_t0_tutMissions:
* Name: Landing
* Description: Our arrival in this galaxy was met with tragedy.
* QuestLine: ql_main_t0_tutorial
* Type: Main
* CinematicIds: 20:10:25
* FollowUps: ql_main_t0_station
* Goals:
	* Task 1: Complete missions:
		* 'Duzumi Gate'
		* 'Duzumi Gate'
	* Task 2: Complete mission 'Wiracoda Gate'
	* Task 3: Complete mission 'Gulf Taln'

## QL_MAIN_T0_STATION
### qm_t0_introStation:
* Name: Lazarus Station
* Description: We were given the coordinates of a local Hiigaran settlement. We should go there.
* QuestLine: ql_main_t0_station
* Type: Main
* Goals:
	* Task 1: Goto Medeans's system LAZARUS

### qm_t0_introMarket:
* Name: Local Currency
* Description: The market can be accessed at stations and inside the flagship, though the selection of items in the flagship market is smaller. For now, we need to pick up some local currency to barter with the locals.
* QuestLine: ql_main_t0_station
* Type: Main
* FollowUps: ql_main_t0_strikeCraft
* Goals:
	* Task 1: Buy: pack_market_freeHC_insta

## QL_MAIN_T0_STRIKECRAFT
### qm_t0_introFabricator:
* Name: Fabricator
* Description: Our fabricators are operational again. We should produce more strike craft in case we run into more hostiles.
* QuestLine: ql_main_t0_strikeCraft
* Type: Main
* Goals:
	* Task 1: Craft

### qm_t0_introEquipStrikecraft:
* Name: Strike Craft
* Description: We need to ready our strike craft inside our hangars.
* QuestLine: ql_main_t0_strikeCraft
* Type: Main
* FollowUps: ql_main_t0_v2_signals
* Goals:
	* Task 1: Equip Squad

## QL_MAIN_T0_V2_SIGNALS
### qm_t0_v2_introScanning:
* Name: Scanning
* Description: We have been asked to take care of a local threat to the Lazarus Station. We need to find out where it is.
* QuestLine: ql_main_t0_v2_signals
* Type: Main
* Goals:
	* Task 1: Scan
	* Task 2: Scan

### qm_t0_v2_introSignals:
* Name: Signals
* Description: We have found hostile signals in the system. We need to clear it out and return to Lazarus Station.
* QuestLine: ql_main_t0_v2_signals
* Type: Main
* FollowUps: ql_main_t0_mining
* Goals:
	* Task 1: Complete side mission
	* Task 2: Goto Medeans's system LAZARUS

## QL_MAIN_T0_MINING
### qm_t0_introScanBelts:
* Name: Asteroid Clusters
* Description: We've been asked by Lazarus Station to help with resource scarcity. We'll need to find suitable mining opportunities by scanning for mineral-rich asteroids in nearby systems.
* QuestLine: ql_main_t0_mining
* Type: Main
* Goals:
	* Task 1: Goto Medeans's system JONALLI
	* Task 2: 1 ScannedBelt

### qm_t0_introMining:
* Name: Mining
* Description: We found a suitable spot for mining. Use the resource collector to mine the mineral rich asteroids.
* QuestLine: ql_main_t0_mining
* Type: Main
* FollowUps: ql_main_t0_support
* Goals:
	* Task 1: 50 Mined0A

## QL_MAIN_T0_SUPPORT
### qm_t0_support:
* Name: Support
* Description: Now that we have the needed minerals, we should go back to Lazarus Station to deliver them.
* QuestLine: ql_main_t0_support
* Type: Main
* FollowUps: ql_main_t0_officer
* Goals:
	* Task 1: Pay 25 RU Type M Ore in Medeans's system LAZARUS

## QL_MAIN_T0_OFFICER
### qm_t0_introBridge:
* Name: Bridge
* Description: Gideon S'jet has offered his Progenitor expertise. We should appoint him as head of science on the bridge.
* QuestLine: ql_main_t0_officer
* Type: Main
* FollowUps: ql_main_t0_escorts
* Goals:
	* Task 1: Equip Officer

## QL_MAIN_T0_ESCORTS
### qm_t0_introShipyard:
* Name: Shipyard
* Description: We have clearance to use the shipyards of Lazarus Station. We should build an additional assault frigate there to bolster our fleet.
* QuestLine: ql_main_t0_escorts
* Type: Main
* Goals:
	* Task 1: Craft

### qm_t0_introEquipEscorts:
* Name: Escort Ships
* Description: Our new assault frigate needs to be staffed and readied. We can do that at any station through Fleet Configuration.
* QuestLine: ql_main_t0_escorts
* Type: Main
* FollowUps: ql_main_t0_sideProg
* Goals:
	* Task 1: Equip Escort

## QL_MAIN_T0_SIDEPROG
### qm_t0_scientist_Baaekh_A:
* Name: Baaekh S’jet
* Description: Baaekh S’jet was one of the foremost scientists on Progenitor culture. According to Gideon she has data that can help us with our own research into the Progenitors.
* QuestLine: ql_main_t0_sideProg
* Type: Main
* Goals:
	* Task 1: Goto Medeans's system ROA TISAAD
	* Task 2: Goto Medeans's system SAARET
	* Task 3: 
		* 4 ScannedBelt
		* 1 ScannedGenerated

### qm_t0_scientist_Baaekh_B:
* Name: Rescue Mission
* Description: We found Baaekh S'jet, but she can't come out of hiding until we have distracted the hostiles in the area.
* QuestLine: ql_main_t0_sideProg
* Type: Main
* FollowUps: ql_main_t0_relic
* Goals:
	* Task 1: Complete side mission
	* Task 2: Goto Medeans's system ROA TISAAD

## QL_MAIN_T0_RELIC
### qm_t0_relic:
* Name: Relic Retrieval
* Description: With information provided by Baaekh S’jet, we now know a potential location of a Progenitor Relic in Toasiim that must be retrieved.
* QuestLine: ql_main_t0_relic
* Type: Main
* FollowUps: ql_main_t0_moreMining
* Goals:
	* Task 1: Goto Medeans's system TOASIIM
	* Task 2: Scan
	* Task 3: Complete mission 'Relic Signature'

## QL_MAIN_T0_MOREMINING
### qm_t0_scientist_Hyeaa_A:
* Name: Hyeaa Somtaaw
* Description: Hyeaa Somtaaw was an expert in Progenitor Materials sciences. He has established an independent lab at Nokuuna. According to Gideon, he has data that can help us with our own research into the Progenitors.
* QuestLine: ql_main_t0_moreMining
* Type: Main
* FollowUps: ql_main_t0_jolja
* Goals:
	* Task 1: Goto Medeans's system NOKUUNA
	* Task 2: Craft
	* Task 3: Equip Squad
	* Task 4: 225 Mined0A

## QL_MAIN_T0_JOLJA
### qm_t0_Jolja:
* Name: Delver
* Description: After examining the Progenitor Relic, Gideon wants us to find a Progenitor Terminal in Iniim. If we access this, we may have some answers about what happened at Wiracoda Gate.
* QuestLine: ql_main_t0_jolja
* Type: Main
* FollowUps: ql_main_t0_setupPlayer
* Goals:
	* Task 1: Goto Medeans's system INIIM
	* Task 2: Scan
	* Task 3: Complete mission 'Jolja'
	* Task 4: Goto Medeans's system LAZARUS

## QL_MAIN_T0_SETUPPLAYER
### qm_t0_pickKiith:
* Name: Blood Ties
* Description: The local Hiigaran survivors wish to know what Kiith we affiliate with. There are advantages for declaring for a specific Kiith.
* QuestLine: ql_main_t0_setupPlayer
* Type: Main
* Goals:
	* Task 1: SelectKiith

### qm_t0_pickName:
* Name: Declaration
* Description: The Hiigaran survivors want to know your name, commander.
* QuestLine: ql_main_t0_setupPlayer
* Type: Main
* FollowUps:
	* ql_main_t1_newOres
	* ql_main_t0_joinClan
* Goals:
	* Task 1: ChangeName

## QL_MAIN_T0_JOINCLAN
### qm_t0_joinClan:
* Name: A Clan of Choice
* Description: We can increase our firepower and capabilities by joining with other battle groups.
* QuestLine: ql_main_t0_joinClan
* Type: Main
* Goals:
	* Task 1: JoinClan

## QL_MAIN_T1_NEWORES
### qm_t1_newOres:
* Name: New Minerals
* Description: The inner systems may have different resources. We should check out the asteroids for mining spots.
* QuestLine: ql_main_t1_newOres
* Type: Main
* FollowUps: ql_esca_mineT1
* Goals:
	* Task 1: Goto Iyatequa's system DEVADAASI
	* Task 2: 6 ScannedBelt
	* Task 3: 200 Mined1A_Mined1B_Mined1C

### qm_t1_introRefining:
* Name: Refinery
* Description: The new ores require refining to be usable for construction purposes. Luckily we have refining facilities on board.
* QuestLine: ql_main_t1_newOres
* Type: Main
* FollowUps:
	* ql_main_t1_sideHiig
	* qm_t1_facHiigaran_A
	* qm_t1_facHiigaran_B
	* qm_t1_facHiigaran_C
	* qm_t1_facHiigaran_D
* Goals:
	* Task 1: 100 Refining1N_Refining1O_Refining1P
	* Task 2: Goto Medeans's system LAZARUS

## QL_MAIN_T1_SIDEHIIG
### qm_t1_facHiigaran:
* Name: Hiigaran Outposts
* Description: Lazarus station asked us to help some Hiigaran outposts on the frontier.
* QuestLine: ql_main_t1_sideHiig
* Type: Main
* FollowUps: ql_main_t1_strikeCraft
* Goals:
	* Task 1: Complete 3 of qm_t1_facHiigaran_A|qm_t1_facHiigaran_B|qm_t1_facHiigaran_C|qm_t1_facHiigaran_D
	* Task 2: Goto Medeans's system LAZARUS

## QL_MAIN_T1_STRIKECRAFT
### qm_t1_strikeCraft:
* Name: New Strike Craft
* Description: We have found a way to incorporate the new materials into our ship design.
* QuestLine: ql_main_t1_strikeCraft
* Type: Main
* FollowUps:
	* ql_main_t1_advCombat_01
	* ql_main_t1_RCol
* Goals:
	* Task 1: 
		* Craft
		* Craft
	* Task 2: 
		* Equip Squad
		* Equip Squad

## QL_MAIN_T1_RCOL
### qm_t1_RColEquip:
* Name: New Resource Collector
* Description: The new ores are more difficult to mine. We should build resource collectors that are equipped to deal with these denser metals.
* QuestLine: ql_main_t1_RCol
* Type: Main
* Goals:
	* Task 1: Craft
	* Task 2: Equip Squad

### qm_t1_RColMine:
* Name: Mining Spree
* Description: We should put our new resource collectors to the test and stockpile some ores.
* QuestLine: ql_main_t1_RCol
* Type: Main
* Goals:
	* Task 1: 4500 Mined1A_Mined1B_Mined1C

## QL_MAIN_T1_ADVCOMBAT_01
### qm_t1_advCombat_01:
* Name: Combat Trials
* Description: Our Hiigaran allies have prepared a combat area to test our improved strike craft.
* QuestLine: ql_main_t1_advCombat_01
* Type: Main
* Goals:
	* Task 1: Complete mission 'Combat Trials'

### qm_t1_killEnemyShips:
* Name: Hostiles
* Description: These inner systems are crawling with enemies. We should thin their numbers. Enemies are found in asteroid clusters and signals.
* QuestLine: ql_main_t1_advCombat_01
* Type: Main
* FollowUps: ql_main_t1_promoteOfficer
* Goals:
	* Task 1: 25 ShipsDestroyed

## QL_MAIN_T1_PROMOTEOFFICER
### qm_t1_introPromoteOfficer:
* Name: Crew Experience
* Description: Training our officers will increase their performance significantly. To train an officer we need to find insignias. Insignias can be gained from discharging officers and may be rewarded from completing signals.
* QuestLine: ql_main_t1_promoteOfficer
* Type: Main
* FollowUps: ql_main_t1_escorts
* Goals:
	* Task 1: UpgradeOfficer

### qm_t1_rankUpOfficer:
* Name: Crew Promotion
* Description: We should promote our most experienced officers to further improve their performance. Promoting an officer increase their special ability or may even grant them a second.
* QuestLine: ql_main_t1_promoteOfficer
* Type: Side
* Goals:
	* Task 1: UpgradeOfficer

## QL_MAIN_T1_ESCORTS
### qm_t1_escort:
* Name: New Escorts
* Description: We should bolster our fleet with frigates made from the new metals.
* QuestLine: ql_main_t1_escorts
* Type: Main
* FollowUps: ql_main_t1_advCombat_02
* Goals:
	* Task 1: Craft
	* Task 2: Equip Escort

## QL_MAIN_T1_ADVCOMBAT_02
### qm_t1_advCombat_02:
* Name: Meropis Defense
* Description: We received a message that Meropis, a Iyatequa communications station, is asking for support in an expected Cangacian attack.
* QuestLine: ql_main_t1_advCombat_02
* Type: Main
* Goals:
	* Task 1: Complete mission 'Meropis Defense'

### qm_t1_doSignals:
* Name: Signal Tracking
* Description: The Cangacians have been repelled, but we should disrupt their activities by hunting down hostile signals in the area.
* QuestLine: ql_main_t1_advCombat_02
* Type: Main
* FollowUps:
	* ql_main_t1_sideCang
	* ql_esca_killPirate1
	* qm_t1_facCangacian_A
	* qm_t1_facCangacian_B
	* qm_t1_facCangacian_C
	* qm_t1_facCangacian_D
* Goals:
	* Task 1: Complete side mission

## QL_MAIN_T1_SIDECANG
### qm_t1_facCangacian:
* Name: Cangacian Troubles
* Description: Cangacians are attacking colonies. We should help them in whatever way we can.
* QuestLine: ql_main_t1_sideCang
* Type: Main
* FollowUps: ql_main_t1_flagship
* Goals:
	* Task 1: Complete 3 of qm_t1_facCangacian_A|qm_t1_facCangacian_B|qm_t1_facCangacian_C|qm_t1_facCangacian_D
	* Task 2: Goto Medeans's system LAZARUS

## QL_MAIN_T1_FLAGSHIP
### qm_t1_introCraftFlagship:
* Name: Flagship Construction
* Description: We have an Explorer-class flagship blueprint utilizing the new minerals found in this region.
* QuestLine: ql_main_t1_flagship
* Type: Main
* FollowUps: ql_main_t1_killCangacians
* Goals:
	* Task 1: Start Crafting - Flagship_Ship

### qm_t1_introEquipFlagship:
* Name: New Flagship
* Description: Once the flagship construction has finished, we should move over to the new flagship, including our ships and officers. This is done via the fleet configuration.
* QuestLine: ql_main_t1_flagship
* Type: Main
* FollowUps: ql_main_t1_advCombat_03
* Goals:
	* Task 1: Craft
	* Task 2: Equip Flagship
	* Task 3: 
		* Equip Squad
		* Equip Escort
		* Equip Officer

## QL_MAIN_T1_KILLCANGACIANS
### qm_t1_killCangacians:
* Name: Pest Control
* Description: While we wait for the flagship construction to finish, we might as well make this galaxy a safer place.
* QuestLine: ql_main_t1_killCangacians
* Type: Side
* Goals:
	* Task 1: 20 ShipsDestroyedP1

## QL_MAIN_T1_ADVCOMBAT_03
### qm_t1_advCombat_03:
* Name: The Pool
* Description: The Iyatequa have flagged a location for suspicious hostile activity. They've asked us to investigate on their behalf.
* QuestLine: ql_main_t1_advCombat_03
* Type: Main
* Goals:
	* Task 1: Complete mission 'The Pool'

### qm_t1_killProgenitors:
* Name: Hostile History
* Description: The Progenitor remnants present a danger to the people living in this galaxy. We should thin their numbers.
* QuestLine: ql_main_t1_advCombat_03
* Type: Main
* FollowUps: ql_main_t1_turrets
* Goals:
	* Task 1: 10 ShipsDestroyedProgenitor

## QL_MAIN_T1_TURRETS
### qm_t1_craftTurret:
* Name: Weapon Turrets
* Description: The new flagship follows modular design principles, allowing us to outfit it with turrets as we choose. First we should build a weapon turret.
* QuestLine: ql_main_t1_turrets
* Type: Main
* Goals:
	* Task 1: Craft

### qm_t1_mountTurret:
* Name: Mounting Turrets
* Description: Now that we have a turret module, we should mount it on our flagship. Turrets can be managed in the external module view of our flagship.
* QuestLine: ql_main_t1_turrets
* Type: Main
* FollowUps: ql_main_t1_upgrades
* Goals:
	* Task 1: Equip Weapon

## QL_MAIN_T1_UPGRADES
### qm_t1_rareEarths:
* Name: Rare Elements
* Description: When refining ores in the refinery there is a chance for rare earths to appear in addition to the refined metals.
* QuestLine: ql_main_t1_upgrades
* Type: Main
* Goals:
	* Task 1: GainItem

### qm_t1_upgradeTurret:
* Name: Turret Upgrades
* Description: The rare minerals we have extracted can be used to improve our modules.
* QuestLine: ql_main_t1_upgrades
* Type: Main
* FollowUps:
	* ql_main_t1_sideProg
	* qm_t1_facProgenitors_A
	* qm_t1_facProgenitors_B
	* qm_t1_facProgenitors_C
	* qm_t1_facProgenitors_D
* Goals:
	* Task 1: Craft

### qm_t1_upgradeTurret_3:
* Name: Turret Upgrades Level 3
* Description: A module can be upgraded multiple times, vastly increasing its power.
* QuestLine: ql_main_t1_upgrades
* Type: Side
* Goals:
	* Task 1: Craft

### qm_t1_upgradeTurret_4:
* Name: Turret Upgrades Level 4
* Description: A module can be upgraded multiple times, vastly increasing its power.
* QuestLine: ql_main_t1_upgrades
* Type: Side
* Goals:
	* Task 1: Craft

### qm_t1_upgradeTurret_5:
* Name: Turret Upgrades Level 5
* Description: A module can be upgraded multiple times, vastly increasing its power.
* QuestLine: ql_main_t1_upgrades
* Type: Side
* Goals:
	* Task 1: Craft

### qm_t1_upgradeTurret_6:
* Name: Turret Upgrades Level 6
* Description: A module can be upgraded multiple times, vastly increasing its power.
* QuestLine: ql_main_t1_upgrades
* Type: Side
* Goals:
	* Task 1: Craft

### qm_t1_upgradeTurret_7:
* Name: Turret Upgrades Level 7
* Description: A module can be upgraded multiple times, vastly increasing its power.
* QuestLine: ql_main_t1_upgrades
* Type: Side
* Goals:
	* Task 1: Craft

### qm_t1_upgradeTurret_8:
* Name: Turret Upgrades Level 8
* Description: A module can be upgraded multiple times, vastly increasing its power.
* QuestLine: ql_main_t1_upgrades
* Type: Side
* Goals:
	* Task 1: Craft

### qm_t1_upgradeTurretMax:
* Name: Final Turret Upgrades
* Description: Once a module has been upgraded to level 9, it is at its maximum level and cannot be upgraded further.
* QuestLine: ql_main_t1_upgrades
* Type: Side
* Goals:
	* Task 1: Craft

## QL_MAIN_T1_SIDEPROG
### qm_t1_facProgenitors:
* Name: Progenitor Components
* Description: To improve our scanner, we should gather data on Progenitor vessels. Once we have enough data, we can create a new scanner blueprint.
* QuestLine: ql_main_t1_sideProg
* Type: Main
* FollowUps: ql_main_t1_scanner
* Goals:
	* Task 1: Complete 3 of qm_t1_facProgenitors_A|qm_t1_facProgenitors_B|qm_t1_facProgenitors_C|qm_t1_facProgenitors_D
	* Task 2: Goto Medeans's system LAZARUS

## QL_MAIN_T1_SCANNER
### qm_t1_scannerModule:
* Name: New Scanner
* Description: Based on the data from the Progenitor fragments, our engineers have created a new scanner blueprint.
* QuestLine: ql_main_t1_scanner
* Type: Main
* FollowUps:
	* ql_main_t2_strike
	* ql_esca_scan
	* ql_main_t1_scannerCharge
* Goals:
	* Task 1: Craft
	* Task 2: Equip Sensor

## QL_MAIN_T1_SCANNERCHARGE
### qm_t1_scannerOvercharge:
* Name: Rare Find
* Description: Some objects are too hidden to find them with our scanner under regular circumstances. Luckily, we can use special batteries to overcharge the scanner beyond its normal abilities to be able to find those.
* QuestLine: ql_main_t1_scannerCharge
* Type: Side
* Goals:
	* Task 1: ChargeScanner
	* Task 2: Scan

## QL_MAIN_T1_UPGRADEEXTERNALS
### qm_t1_upgradeModules:
* Name: Exploration Upgrades
* Description: In order to move deeper into the galaxy we should upgrade our scanner and drives core.
* QuestLine: ql_main_t1_upgradeExternals
* Type: Main
* FollowUps: ql_main_t1_introInternals
* Goals:
	* Task 1: 
		* Craft
		* Craft

## QL_MAIN_T1_INTROLIAISON
### qm_t1_introLiaison:
* Name: Reaching Out
* Description: The Iyatequa are interested in doing business with us. Completing liaison assignments for them will allow us to increase our reputation, which allows us to buy special items and blueprints in their liaison requisitions office.
* QuestLine: ql_main_t1_introLiaison
* Type: Side
* Goals:
	* Task 1: 3 Faction

## QL_MAIN_T1_INTROINTERNALS
### qm_t1_introInternals:
* Name: Internal Modules
* Description: Our flagship has a configurable interior, which we can use to boost our exploration, production or combat abilities using internal modules.
* QuestLine: ql_main_t1_introInternals
* Type: Main
* Goals:
	* Task 1: Craft
	* Task 2: Equip Internal

### qm_t1_upgradeInternals:
* Name: Internal Module Upgrades
* Description: Just like with weapon turrets, we can improve our internal module's performance through upgrades.
* QuestLine: ql_main_t1_introInternals
* Type: Main
* FollowUps:
	* ql_main_t1_sideIyat
	* qm_t1_facIyatequa_A
	* qm_t1_facIyatequa_B
	* qm_t1_facIyatequa_C
	* qm_t1_facIyatequa_D
* Goals:
	* Task 1: Craft

## QL_MAIN_T1_SIDEIYAT
### qm_t1_facIyatequa:
* Name: Iyatequa Business
* Description: The Iyatequa have heard of our plan to meet the Tanoch and agreed to help us set up our science facilities to research better drives. For a price, of course.
* QuestLine: ql_main_t1_sideIyat
* Type: Main
* FollowUps: ql_main_t2_research
* Goals:
	* Task 1: Complete 3 of qm_t1_facIyatequa_A|qm_t1_facIyatequa_B|qm_t1_facIyatequa_C|qm_t1_facIyatequa_D
	* Task 2: Goto Medeans's system LAZARUS

## QL_MAIN_T2_RESEARCH
### qm_t2_introRP:
* Name: Laboratories
* Description: Our scientists have brought our on-ship laboratories online. We can collect the data of their findings there.
* QuestLine: ql_main_t2_research
* Type: Main
* Goals:
	* Task 1: GainItem

### qm_t2_introResearch:
* Name: Research Center
* Description: Lazarus Base has given us access to a workshop module attached to the station. We can perform further research there and develop new technologies.
* QuestLine: ql_main_t2_research
* Type: Main
* FollowUps: ql_main_t2_newResources
* Goals:
	* Task 1: Craft

## QL_MAIN_T2_NEWRESOURCES
### qm_t2_newResources:
* Name: New Resources T2
* Description: It seems the deeper we move into the galaxy the more minerals we find.
* QuestLine: ql_main_t2_newResources
* Type: Main
* FollowUps:
	* ql_main_t2_sideCang
	* qm_t2_facCangacian_A
	* qm_t2_facCangacian_B
	* qm_t2_facCangacian_C
	* qm_t2_facCangacian_D
* Goals:
	* Task 1: Goto Iyatequa's system BISHAAN TEL
	* Task 2: 25 ScannedBelt
	* Task 3: 3000 Mined2A_Mined2B_Mined2C_Mined2D
	* Task 4: Craft
	* Task 5: Goto Medeans's system LAZARUS

## QL_MAIN_T2_SIDECANG
### qm_t2_facCangacian:
* Name: Cangacian Incursion
* Description: Several Hiigaran colonies are under attack by Cangacians. Lazarus command has asked us to help as much as we can.
* QuestLine: ql_main_t2_sideCang
* Type: Main
* FollowUps: ql_main_t2_strikeCraftResearch
* Goals:
	* Task 1: Complete 3 of qm_t2_facCangacian_A|qm_t2_facCangacian_B|qm_t2_facCangacian_C|qm_t2_facCangacian_D
	* Task 2: Goto Medeans's system LAZARUS

## QL_MAIN_T2_STRIKE
### qm_t2_findPirateHideout:
* Name: Hidden in the Dark
* Description: We need to find the system from where the recent Cangacian activity originates. Reports indicate the system might be near Saraal. We should go there and use our long range scanners.
* QuestLine: ql_main_t2_strike
* Type: Main
* FollowUps:
	* ql_raid_013
	* ql_main_t1_upgradeExternals
	* ql_main_t1_introLiaison
* Goals:
	* Task 1: 
		* Scan
		* Goto Iyatequa's system DEVADAASI

### qm_t2_strikePirateHideout:
* Name: Cangacian Hideout
* Description: We have located the pirate hideout. Now is the time to strike.
* QuestLine: ql_main_t2_strike
* Type: Main
* Goals:
	* Task 1: Complete 1 of qr_013

## QL_MAIN_T2_STRIKECRAFTRESEARCH
### qm_t2_startResearchT2Intc:
* Name: Interceptor T2
* Description: We can research better ship blueprints using the new materials found in this region.
* QuestLine: ql_main_t2_strikeCraftResearch
* Type: Main
* FollowUps: ql_main_t2_strikeCraftCraft
* Goals:
	* Task 1: Start Research - rp_catStrCraft_bp_sf_intc_t2_c

### qm_t2_finResearchT2Intc:
* Name: Interceptor Schematics
* Description: Schematics research unlock new blueprints for the fabricators and shipyard.
* QuestLine: ql_main_t2_strikeCraftResearch
* Type: Main
* Goals:
	* Task 1: Craft

## QL_MAIN_T2_STRIKECRAFTCRAFT
### qm_t2_introParts:
* Name: Ship Parts Assembly
* Description: The new constructions will require the use of specially fabricated parts.

The blueprints for small Hull, Weapon and Machinery parts can be found in the market.
* QuestLine: ql_main_t2_strikeCraftCraft
* Type: Main
* Goals:
	* Task 1: Buy: bp_intmed_ship_small_t2
	* Task 2: Craft

### qm_t2_strikeCraft:
* Name: Strike Craft T2
* Description: Now that we have finished the research and crafted the necessary parts, we can craft an interceptor squadron.
* QuestLine: ql_main_t2_strikeCraftCraft
* Type: Main
* FollowUps:
	* ql_main_t2_sideHiig
	* ql_main_t2_RCol
	* ql_raid_016
	* qm_t2_facHiigaran_A
	* qm_t2_facHiigaran_B
	* qm_t2_facHiigaran_C
	* qm_t2_facHiigaran_D
* Goals:
	* Task 1: Complete 1 of qm_t2_finResearchT2Intc
	* Task 2: Craft

## QL_MAIN_T2_SIDEHIIG
### qm_t2_facHiigaran:
* Name: Lazarus Repairs
* Description: Lazarus Station was recently attacked. Command asked us to help with rebuilding efforts.
* QuestLine: ql_main_t2_sideHiig
* Type: Main
* FollowUps: ql_main_t2_researchEscort
* Goals:
	* Task 1: Complete 3 of qm_t2_facHiigaran_A|qm_t2_facHiigaran_B|qm_t2_facHiigaran_C|qm_t2_facHiigaran_D

## QL_MAIN_T2_RCOL
### qm_t2_craftRCol:
* Name: Resource Collector T2
* Description: Mining the new ores can be done faster with special resource collectors equipped with better mining gear.
* QuestLine: ql_main_t2_RCol
* Type: Side
* Goals:
	* Task 1: Craft

### qm_t2_RColMining:
* Name: Ore Deal
* Description: With our new resource collectors, we can mine ores much faster than before.
* QuestLine: ql_main_t2_RCol
* Type: Side
* FollowUps: ql_main_t2_RCon
* Goals:
	* Task 1: 9000 Mined2A_Mined2B_Mined2C_Mined2D

## QL_MAIN_T2_RCON
### qm_t2_craftRCon:
* Name: Resource Controller
* Description: We acquired a blueprint for the Resource Controller, an escort ship we can send on independent mining missions. Like other escort ships, it must be built in the shipyard.
* QuestLine: ql_main_t2_RCon
* Type: Side
* Goals:
	* Task 1: Craft

### qm_t2_introIdleMine:
* Name: Remote Mining
* Description: Resource Controllers can be sent away to mine ores without our supervision. To do that, it must be assigned to an escort slot in fleet configuration.
* QuestLine: ql_main_t2_RCon
* Type: Side
* Goals:
	* Task 1: 5000 IdleMined

## QL_MAIN_T2_RESEARCHESCORT
### qm_t2_startResearchT2Frig:
* Name: Assault Frigate T2
* Description: We can research a better assault frigate blueprint using the new minerals.
* QuestLine: ql_main_t2_researchEscort
* Type: Main
* FollowUps: ql_main_t2_oreD
* Goals:
	* Task 1: Start Research - rp_catEscorts_bp_cf_assa_t2_c

### qm_t2_finResearchT2Frig:
* Name: Assault Frigate Schematics
* Description: Our scientists are at work developing new schematics for the assault frigate.
* QuestLine: ql_main_t2_researchEscort
* Type: Main
* FollowUps:
	* ql_main_t2_craftEscort
	* ql_main_t2_researchPulsarCorvette
* Goals:
	* Task 1: Craft

## QL_MAIN_T2_ORED
### qm_t2_introOreD:
* Name: Gold Rush
* Description: Some asteroids in this region contain a rare ore we can use for advanced constructions.
* QuestLine: ql_main_t2_oreD
* Type: Side
* Goals:
	* Task 1: 3500 Mined2D
	* Task 2: Craft

### qm_t2_craftUncShip:
* Name: Elite Ships
* Description: We acquired a blueprint for an advanced ship design. It requires the rare ore to be built.
* QuestLine: ql_main_t2_oreD
* Type: Side
* Goals:
	* Task 1: Craft

## QL_MAIN_T2_CRAFTESCORT
### qm_t2_largeHullParts:
* Name: Large Hull Parts Assembly
* Description: The frigate blueprint requires a large version of the hull parts.

The blueprint for large hull parts can be found in the market.
* QuestLine: ql_main_t2_craftEscort
* Type: Main
* Goals:
	* Task 1: Buy: bp_intmed_ship_large_t2
	* Task 2: Craft

### qm_t2_escort:
* Name: Escort Ships T2
* Description: With the large hull parts we can finally construct the frigate.
* QuestLine: ql_main_t2_craftEscort
* Type: Main
* FollowUps:
	* ql_main_t2_introLiaison
	* ql_main_t2_strikeStationDefense
	* ql_raid_014
* Goals:
	* Task 1: Craft

## QL_MAIN_T2_INTROLIAISON
### qm_t2_introLiaison:
* Name: Liaison Office
* Description: Doing assignments for the liaison office will allow us to requisition better blueprints and better equipment.
* QuestLine: ql_main_t2_introLiaison
* Type: Main
* FollowUps:
	* ql_main_t2_sideIyat
	* qm_t2_facIyatequa_A
	* qm_t2_facIyatequa_B
	* qm_t2_facIyatequa_C
	* qm_t2_facIyatequa_D
* Goals:
	* Task 1: 3 Faction

## QL_MAIN_T2_RESEARCHPULSARCORVETTE
### qm_t2_researchPulsarCorvette:
* Name: Pulsar Corvette Schematics
* Description: Uncommon, rare and epic researches are not part of the central research path and must be found in order to be researched.

The Pulsar Corvette Schematics can be found in the code fragment market.
* QuestLine: ql_main_t2_researchPulsarCorvette
* Type: Side
* FollowUps: ql_main_t2_pulsarCorvette
* Goals:
	* Task 1: Craft

## QL_MAIN_T2_PULSARCORVETTE
### qm_t2_pulsarCorvette:
* Name: Pulsar Corvette
* Description: Pulsar Corvettes are effective against other corvettes and small escort ships.
* QuestLine: ql_main_t2_pulsarCorvette
* Type: Side
* Goals:
	* Task 1: Craft

## QL_MAIN_T2_SIDEIYAT
### qm_t2_facIyatequa:
* Name: Iyatequa Intermediary
* Description: The Iyatequa have offered to liaison between us and the Tanoch if we agree to run some errands for them.
* QuestLine: ql_main_t2_sideIyat
* Type: Main
* FollowUps:
	* ql_main_t2_largeWpnParts
	* ql_main_t2_largeMchParts
* Goals:
	* Task 1: Complete 3 of qm_t2_facIyatequa_A|qm_t2_facIyatequa_B|qm_t2_facIyatequa_C|qm_t2_facIyatequa_D
	* Task 2: Goto Medeans's system LAZARUS

## QL_MAIN_T2_LARGEWPNPARTS
### qm_t2_liaisonTanoch:
* Name: Tanoch Relations
* Description: The Tanoch liaison office will offer better items the higher our reputation is.
* QuestLine: ql_main_t2_largeWpnParts
* Type: Main
* Goals:
	* Task 1: 10 Faction_Tanoch_T2up

### qm_t2_largeWeaponParts:
* Name: Large Weapon Parts Assembly
* Description: Large weapon parts are required for building flagships and weapon modules.

The blueprint for large weapon parts can be found in the Tanoch liaison requisitions office.
* QuestLine: ql_main_t2_largeWpnParts
* Type: Main
* FollowUps: ql_main_t2_flagship
* Goals:
	* Task 1: Craft

## QL_MAIN_T2_LARGEMCHPARTS
### qm_t2_liaisonIyatequa:
* Name: Iyatequa Relations
* Description: The Iyatequa liaison office will offer better items the higher our reputation is.
* QuestLine: ql_main_t2_largeMchParts
* Type: Main
* Goals:
	* Task 1: 10 Faction_Tr1_T2up

### qm_t2_largeMachineParts:
* Name: Large Machinery Parts Assembly
* Description: Large machinery parts are required for building flagships and non-weapon modules.

The blueprint for large machinery parts can be found in the Iyatequa liaison requisitions office.
* QuestLine: ql_main_t2_largeMchParts
* Type: Main
* FollowUps: ql_main_t2_flagship
* Goals:
	* Task 1: Craft

## QL_MAIN_T2_FLAGSHIP
### qm_t2_startCraftFlagship:
* Name: Flagship Construction T2
* Description: Now that we have the necessary resources, we can start building our new flagship. Its larger drive core will allow us to enter Tanoch territory. Flagship blueprints are available in the market.
* QuestLine: ql_main_t2_flagship
* Type: Main
* FollowUps:
	* ql_Keid
	* ql_main_t2_strikePahrasRock
	* ql_raid_015
* Goals:
	* Task 1: Complete 2 of qm_t2_largeWeaponParts|qm_t2_largeMachineParts
	* Task 2: Start Crafting - Flagship_Ship_T2

### qm_t2_finCraftFlagship:
* Name: Flagship T2
* Description: The construction of our new flagship is under way. Once it's finished, we can switch over and move our squadrons and officers as well as modules to the new flagship.
* QuestLine: ql_main_t2_flagship
* Type: Main
* FollowUps:
	* ql_main_t2_tanochet
	* ql_main_t2_turrets
* Goals:
	* Task 1: Craft

## QL_MAIN_T2_TURRETS
### qm_t2_turrets:
* Name: Weapon Turrets T2
* Description: We should stay up to date on weapon technology. Researching new weapon schematics will unlock better modules.
* QuestLine: ql_main_t2_turrets
* Type: Side
* Goals:
	* Task 1: Craft
	* Task 2: Craft
	* Task 3: Equip Weapon

## QL_MAIN_T2_TANOCHET
### qm_t2_tanochet:
* Name: Tanochet
* Description: We can finally reach the Tanoch capital. It is time to meet the emperor.
* QuestLine: ql_main_t2_tanochet
* Type: Main
* CinematicIds: 30
* FollowUps:
	* ql_main_t2_sideTano
	* ql_main_t2_epicSignals
	* qm_t2_facTanoch_A
	* qm_t2_facTanoch_B
	* qm_t2_facTanoch_C
	* qm_t2_facTanoch_D
* Goals:
	* Task 1: Complete mission 'Tanochet'

## QL_MAIN_T2_INTERNALS
### qm_t2_internalFabricator:
* Name: Fabricator Module
* Description: Our new flagship offers the ability to reconfigure its internal layout.
* QuestLine: ql_main_t2_internals
* Type: Main
* Goals:
	* Task 1: Craft
	* Task 2: Equip Internal

## QL_MAIN_T2_STRIKESTATIONDEFENSE
### qm_t2_strikeStationDefense:
* Name: Station Defense
* Description: A large Tanoch station is under attack by a large fleet of pirates. We should band together with other fleets to repel the attackers.
* QuestLine: ql_main_t2_strikeStationDefense
* Type: Side
* Goals:
	* Task 1: Complete 1 of qr_014

## QL_MAIN_T2_STRIKEPAHRASROCK
### qm_t2_strikePahrasRock:
* Name: Pahra's Rock
* Description: Pirate's major Asteroid Base in the area has been threatening the Hiigaran settlements. Hiigaran Flagships have been gathered to strike on this Base.​
* QuestLine: ql_main_t2_strikePahrasRock
* Type: Side
* Goals:
	* Task 1: Complete 1 of qr_015

## QL_MAIN_T2_SIDETANO
### qm_t2_facTanoch:
* Name: Tanoch Errands
* Description: The Tanoch have asked us to run some errands for them. This could be a chance for us to gain their trust.
* QuestLine: ql_main_t2_sideTano
* Type: Main
* FollowUps:
	* ql_main_t2_sideYaot
	* ql_main_t2_compartments
	* qm_t2_facYaot_A
	* qm_t2_facYaot_B
	* qm_t2_facYaot_C
	* qm_t2_facYaot_D
* Goals:
	* Task 1: Complete 3 of qm_t2_facTanoch_A|qm_t2_facTanoch_B|qm_t2_facTanoch_C|qm_t2_facTanoch_D
	* Task 2: Goto Tanoch's system TANOCHETLAN

## QL_MAIN_T2_UPGRADEINTERNALS
### qm_t2_upgradeInternals:
* Name: Internal Module Upgrades
* Description: Just like with weapon turrets, we can improve our internal module's performance through upgrades.
* QuestLine: ql_main_t2_upgradeInternals
* Type: Main
* Goals:
	* Task 1: Craft

### qm_t2_otherInternals:
* Name: Compartments
* Description: Our flagship is sectioned into three compartments. We can install different modules in different compartments.
* QuestLine: ql_main_t2_upgradeInternals
* Type: Side
* Goals:
	* Task 1: 
		* Equip Internal
		* Equip Internal

## QL_MAIN_T2_COMPARTMENTS
### qm_t2_compartments:
* Name: Compartments
* Description: Our flagship is sectioned into three compartments. We can install different modules in different compartments.
* QuestLine: ql_main_t2_compartments
* Type: Side
* Goals:
	* Task 1: 
		* Equip Internal
		* Equip Internal

## QL_MAIN_T2_EPICSIGNALS
### qm_t2_epicSignals:
* Name: High Risk High Reward
* Description: Occasionally we come across high energy signals. It might be worth checking out, but it could also be a potential danger. We should proceed with caution.
* QuestLine: ql_main_t2_epicSignals
* Type: Side
* Goals:
	* Task 1: 
		* Scan
		* Complete side mission

## QL_MAIN_T2_SIDEYAOT
### qm_t2_facYaot:
* Name: Yaot Conflict
* Description: We have received assignments from both Tanochetlan and Lazarus station. They asked us to investigate the Yaot threat.
* QuestLine: ql_main_t2_sideYaot
* Type: Main
* FollowUps: ql_main_t2_templeTonaati
* Goals:
	* Task 1: Complete 3 of qm_t2_facYaot_A|qm_t2_facYaot_B|qm_t2_facYaot_C|qm_t2_facYaot_D
	* Task 2: Goto Tanoch's system TANOCHETLAN

## QL_MAIN_T2_TEMPLETONAATI
### qm_t2_templeTonaati:
* Name: Temple Tonaati
* Description: We are following Vaygr fleet to find out their hidden plan.
* QuestLine: ql_main_t2_templeTonaati
* Type: Main
* FollowUps:
	* ql_Exile
	* ql_side_exploration
	* ql_main_t3_jumpCap
* Goals:
	* Task 1: Complete mission 'Temple Tonaati'

## QL_MAIN_T3_JUMPCAP
### qm_t3_researchJumpCap:
* Name: Expanding the Horizon
* Description: Our scientists have come up with new theories on how to increase the power of our engines. With the new technology we should be able to enter space that was previously inaccessible to us.
* QuestLine: ql_main_t3_jumpCap
* Type: Main
* FollowUps: ql_main_t3_intro
* Goals:
	* Task 1: Craft

## QL_MAIN_T3_INTRO
### qm_t3_scouting:
* Name: New Frontiers
* Description: With our improved hyperjump technology, we should upgrade our engines and sensors to explore the new areas.
* QuestLine: ql_main_t3_intro
* Type: Main
* Goals:
	* Task 1: 
		* Craft
		* Craft

### qm_t3_scouting_scanBelts:
* Name: Resource Scouting
* Description: Fleet command wants accurate maps of nearby asteroid clusters in order to chart resources and hazards. Contribute to this effort by scanning asteroid clusters.
* QuestLine: ql_main_t3_intro
* Type: Main
* Goals:
	* Task 1: 55 ScannedBelt

### qm_t3_scouting_scanJovian:
* Name: Gas Giant Scan
* Description: New scanning protocols for scanning gas giants are being tested. Contribute to this test by fully scanning a gas giant.
* QuestLine: ql_main_t3_intro
* Type: Main
* FollowUps:
	* ql_main_t3_gasMining
	* ql_main_t3_yaotLiaison
* Goals:
	* Task 1: 1 ScannedJovian

## QL_MAIN_T3_GASMINING
### qm_t3_gasMining:
* Name: A New Resource
* Description: We found a new type of resource that warrants a closer look. We should take some samples for study. To harvest gas, simply send a Gas Collector into the atmosphere of a gas planet. Be careful. Deeper layers will deal more damage to your ships! The blueprint for the Gas Collector can be found in the Market.
* QuestLine: ql_main_t3_gasMining
* Type: Main
* FollowUps:
	* ql_main_t3_sideYaot
	* ql_main_t3_sideYaot_A
	* ql_main_t3_sideYaot_B
	* ql_main_t3_sideYaot_C
* Goals:
	* Task 1: Craft
	* Task 2: 1000 Mined3E_Mined3F_Mined3G_Mined3H

## QL_MAIN_T3_YAOTLIAISON
### qm_t3_yaotLiaison:
* Name: Yaot Relations
* Description: The Yaot have opened their liaison office to us.
* QuestLine: ql_main_t3_yaotLiaison
* Type: Side
* Goals:
	* Task 1: 1000 RepYaot

## QL_MAIN_T3_SIDEYAOT
### qm_t3_facYaot:
* Name: Uneasy Allies
* Description: The Yaot are interested in opening relations with us and wish to begin a dialogue.
* QuestLine: ql_main_t3_sideYaot
* Type: Main
* FollowUps:
	* ql_raid_017
	* ql_main_t3_sideTanoch
	* ql_main_t3_sideTanoch_A
	* ql_main_t3_sideTanoch_B
	* ql_main_t3_sideTanoch_C
	* ql_orb_t3_intro
* Goals:
	* Task 1: Complete 2 of qm_t3_sideYaot_A_3|qm_t3_sideYaot_B_3|qm_t3_sideYaot_C_3
	* Task 2: Goto Yaot's system YAOTL

## QL_MAIN_T3_SIDEYAOT_A
### qm_t3_sideYaot_A_1:
* Name: Truce: Loadstones I
* Description: The Yaot present a simple request to map and gather resources in order to test our capabilities and their trust in us.
* QuestLine: ql_main_t3_sideYaot_A
* Type: Side
* Goals:
	* Task 1: 
		* 65 ScannedBelt
		* Pay 50 RU Type B Refined T3

### qm_t3_sideYaot_A_2:
* Name: Truce: Loadstones II
* Description: The Yaot have asked us to collect further resources and clear the mining areas of hostiles.
* QuestLine: ql_main_t3_sideYaot_A
* Type: Side
* Goals:
	* Task 1: 
		* 2500 Mined3C
		* 30 ShipsDestroyed

### qm_t3_sideYaot_A_3:
* Name: Truce: Loadstones III
* Description: The Yaot are interested in learning our capacity for materials refining. We'll be compensated well.
* QuestLine: ql_main_t3_sideYaot_A
* Type: Side
* Goals:
	* Task 1: 
		* 300 Refining3N
		* Pay 100 RU Type A Refined T3

## QL_MAIN_T3_SIDEYAOT_B
### qm_t3_sideYaot_B_1:
* Name: Truce: The Privateer I
* Description: The Yaot have a supply line they want protected, and are willing to hire us to clear it of hostiles.
* QuestLine: ql_main_t3_sideYaot_B
* Type: Side
* Goals:
	* Task 1: 
		* Scan
		* Complete 6 side missions

### qm_t3_sideYaot_B_2:
* Name: Truce: The Privateer II
* Description: The Yaot wish to commission us to guard this patrol route until their own patrols can relieve us.
* QuestLine: ql_main_t3_sideYaot_B
* Type: Side
* Goals:
	* Task 1: 
		* 30 ShipsDestroyed
		* GainItem

### qm_t3_sideYaot_B_3:
* Name: Truce: The Privateer III
* Description: The Yaot are impressed with our combat capabilities and want to see how we fare against stronger enemies.
* QuestLine: ql_main_t3_sideYaot_B
* Type: Side
* Goals:
	* Task 1: Complete 3 side missions

## QL_MAIN_T3_SIDEYAOT_C
### qm_t3_sideYaot_C_1:
* Name: Truce: Exchange of Ideas I
* Description: The Yaot have made more contracts available to us on a trial basis. We should engage them.
* QuestLine: ql_main_t3_sideYaot_C
* Type: Side
* Goals:
	* Task 1: 5 Faction_Yaot_T3up

### qm_t3_sideYaot_C_2:
* Name: Truce: Exchange of Ideas II
* Description: The Yaot are becoming more comfortable with employing us. More work for them will go a long way to improving relations.
* QuestLine: ql_main_t3_sideYaot_C
* Type: Side
* Goals:
	* Task 1: 
		* 250 RepYaot
		* 30 ShipsDestroyed

### qm_t3_sideYaot_C_3:
* Name: Truce: Exchange of Ideas III
* Description: The Yaot trust us enough to employ our services on a contract basis. More work is available.
* QuestLine: ql_main_t3_sideYaot_C
* Type: Side
* Goals:
	* Task 1: 
		* GainItem
		* 4050 RepYaot

## QL_MAIN_T3_SIDETANOCH
### qm_t3_facTanoch:
* Name: Inside the Empire
* Description: We have been contacted by the Chicuat people within the Tanoch empire. They have been denied Imperial services and are asking us for help.
* QuestLine: ql_main_t3_sideTanoch
* Type: Main
* FollowUps:
	* ql_raid_018
	* ql_main_t3_starTotek
* Goals:
	* Task 1: Complete 2 of qm_t3_sideTanoch_A_3|qm_t3_sideTanoch_B_3|qm_t3_sideTanoch_C_3
	* Task 2: Goto Tanoch's system TANOCHETLAN

## QL_MAIN_T3_SIDETANOCH_A
### qm_t3_sideTanoch_A_1:
* Name: Chicuat: Dry Well I
* Description: Next to no Imperial resources are reaching the Chicuat worlds. They are asking us to provide what we spare.
* QuestLine: ql_main_t3_sideTanoch_A
* Type: Side
* Goals:
	* Task 1: 
		* Pay 400 RU Type A Ore T3
		* Pay 200 RU Type B Ore T3
		* Pay 1400 RU Type C Ore T3

### qm_t3_sideTanoch_A_2:
* Name: Chicuat: Dry Well II
* Description: The Chicuat refineries are busy with the ores we have provided. Meanwhile, an agricultural colony providing most of the food in the sector is running on systems that are barely holding together. They have asked us for spare parts.
* QuestLine: ql_main_t3_sideTanoch_A
* Type: Side
* Goals:
	* Task 1: Pay 15 Large Machinery Parts

### qm_t3_sideTanoch_A_3:
* Name: Chicuat: Dry Well III
* Description: The economic system has been stabilized, but without proper defenses, raiders will undo everything we've done. We should provide them with some fighters of their own and give their militia some training.
* QuestLine: ql_main_t3_sideTanoch_A
* Type: Side
* Goals:
	* Task 1: 
		* Pay 50 Small Hull Parts
		* Pay 50 Small Weapon Parts
	* Task 2: Complete 5 side missions

## QL_MAIN_T3_SIDETANOCH_B
### qm_t3_sideTanoch_B_1:
* Name: Chicuat: Exposed I
* Description: Without Imperial patrols, Chicuat space is vulnerable against raiders. They have asked us to make a sweep across their space to clear the sector of hostiles.
* QuestLine: ql_main_t3_sideTanoch_B
* Type: Side
* Goals:
	* Task 1: 
		* Scan
		* 35 ShipsDestroyed

### qm_t3_sideTanoch_B_2:
* Name: Chicuat: Exposed II
* Description: Most hostiles have been chased off, but some bold bands of the Fleet of Rams have refused to be intimidated. It is time to make a statement.
* QuestLine: ql_main_t3_sideTanoch_B
* Type: Side
* Goals:
	* Task 1: 
		* Complete 7 side missions
		* 25 ShipsDestroyedP1

### qm_t3_sideTanoch_B_3:
* Name: Chicuat: Exposed III
* Description: The Chicuat officials have seen our results and several of them want to see us in action. They hope to learn from us how to organize their defenses better.
* QuestLine: ql_main_t3_sideTanoch_B
* Type: Side
* Goals:
	* Task 1: 
		* Complete 3 side missions
		* GainItem

## QL_MAIN_T3_SIDETANOCH_C
### qm_t3_sideTanoch_C_1:
* Name: Chicuat: Favors I
* Description: Our contact has suggested running some errands for the Tanoch in the name of the Chicuat people. Doing so would hopefully increase the Chicuat's standing within the Empire.
* QuestLine: ql_main_t3_sideTanoch_C
* Type: Side
* Goals:
	* Task 1: 500 RepTanoch

### qm_t3_sideTanoch_C_2:
* Name: Chicuat: Favors II
* Description: The Empire is reacting to our support of the Chicuat people. While we wait to learn more about the outcome, the Chicuat have asked if their officers can cross-train with ours.
* QuestLine: ql_main_t3_sideTanoch_C
* Type: Side
* Goals:
	* Task 1: 
		* UpgradeOfficer
		* 7 Faction_Tanoch_T2up

### qm_t3_sideTanoch_C_3:
* Name: Chicuat: Favors III
* Description: After lengthy negotiations with the Chicuat, the Empire reluctantly has agreed to a relief operation, sending resources to worlds in need. Naturally they ask us for support instead of sending their own materials...
* QuestLine: ql_main_t3_sideTanoch_C
* Type: Side
* Goals:
	* Task 1: 
		* 8500 RepTanoch
		* 600 Refining3N_Refining3O_Refining3P_Refining3Q

## QL_MAIN_T3_STARTOTEK
### qm_t3_starTotek:
* Name: Star Totek
* Description: We are closing in on possible Vaygr transmissions close to the star.
* QuestLine: ql_main_t3_starTotek
* Type: Main
* FollowUps:
	* ql_main_t3_sideHiig
	* ql_main_t3_sideHiig_A
	* ql_main_t3_sideHiig_B
	* ql_main_t3_sideHiig_C
	* ql_main_t3_strikeBreach
	* ql_raid_019
* Goals:
	* Task 1: Complete mission 'Star Totek'

## QL_MAIN_T3_STRIKEBREACH
### qm_t3_strikeBreach:
* Name: Breach
* Description: We found an enemy base that is heavily fortified. Breaching its defenses will not be easy.
* QuestLine: ql_main_t3_strikeBreach
* Type: Side
* Goals:
	* Task 1: Complete 1 of qr_019

## QL_MAIN_T3_SIDEHIIG
### qm_t3_facHiigaran:
* Name: Planting the Flag
* Description: Lazarus Base calls us back to the Hiigaran colonies to establish a presence there and keep the peace.
* QuestLine: ql_main_t3_sideHiig
* Type: Main
* FollowUps:
	* ql_main_t3_sideIyat
	* ql_main_t3_sideIyat_A
	* ql_main_t3_sideIyat_B
	* ql_main_t3_sideIyat_C
* Goals:
	* Task 1: Complete 2 of qm_t3_sideHiigaran_A_3|qm_t3_sideHiigaran_B_3|qm_t3_sideHiigaran_C_3
	* Task 2: Goto Medeans's system LAZARUS

## QL_MAIN_T3_SIDEHIIG_A
### qm_t3_sideHiigaran_A_1:
* Name: Colonies: Brick Making I
* Description: Hiigaran resource efforts are very short handed, so we’ll be going to assist gas collection in deep space.
* QuestLine: ql_main_t3_sideHiig_A
* Type: Side
* Goals:
	* Task 1: 
		* 20 ScannedJovian
		* 600 Mined3E_Mined3F_Mined3G_Mined3H

### qm_t3_sideHiigaran_A_2:
* Name: Colonies: Brick Making II
* Description: Our assistance has been helpful so far, but we are asked to provide and analyze some ore samples from the deeper regions of the galaxy.
* QuestLine: ql_main_t3_sideHiig_A
* Type: Side
* Goals:
	* Task 1: 
		* 5000 Mined3A_Mined3B_Mined3C_Mined3D
		* GainItem

### qm_t3_sideHiigaran_A_3:
* Name: Colonies: Brick Making III
* Description: The logistics have been set up for the most part, but we are asked to help with some deliveries.
* QuestLine: ql_main_t3_sideHiig_A
* Type: Side
* Goals:
	* Task 1: 
		* Pay 100 GU Type G Gas T3
		* Pay 200 RU Type B Refined T3
		* Pay 40 Small Hull Parts

## QL_MAIN_T3_SIDEHIIG_B
### qm_t3_sideHiigaran_B_1:
* Name: Colonies: Security Blanket I
* Description: Lazarus base has established a quota for all commanders hunting loose pirates in Hiigaran space.
* QuestLine: ql_main_t3_sideHiig_B
* Type: Side
* Goals:
	* Task 1: 
		* 30 ShipsDestroyedP1
		* GainItem

### qm_t3_sideHiigaran_B_2:
* Name: Colonies: Security Blanket II
* Description: Most pirates have gone into hiding, but we are asked to make sweeps of local space, to flush out the remaining hostiles.
* QuestLine: ql_main_t3_sideHiig_B
* Type: Side
* Goals:
	* Task 1: 
		* Scan
		* Complete 5 side missions

### qm_t3_sideHiigaran_B_3:
* Name: Colonies: Security Blanket III
* Description: The hostile presence has been reduced to a manageable level, but Progenitor craft threaten research vessels. We need to get rid of them and analyze some of the debris.
* QuestLine: ql_main_t3_sideHiig_B
* Type: Side
* Goals:
	* Task 1: 
		* 15 ShipsDestroyedProgenitor
		* GainItem

## QL_MAIN_T3_SIDEHIIG_C
### qm_t3_sideHiigaran_C_1:
* Name: Colonies: The Next Generation I
* Description: Lazarus has sent us some trainees to get some practical experience on our ship.
* QuestLine: ql_main_t3_sideHiig_C
* Type: Side
* Goals:
	* Task 1: 
		* GainItem
		* 2000 PlayerXP

### qm_t3_sideHiigaran_C_2:
* Name: Colonies: The Next Generation II
* Description: Many of the trainees are going to become pilots and navigators, but have so far trained in controlled or virtual flight simulators. They need some real experience.
* QuestLine: ql_main_t3_sideHiig_C
* Type: Side
* Goals:
	* Task 1: 
		* Craft
		* UpgradeOfficer

### qm_t3_sideHiigaran_C_3:
* Name: Colonies: The Next Generation III
* Description: The final course is the graduation level for the trainees, who must see actual combat. You are to take the crew into battle and complete the course. Once finished, they return to Lazarus to finish up their coursework.
* QuestLine: ql_main_t3_sideHiig_C
* Type: Side
* Goals:
	* Task 1: Complete 10 side missions
	* Task 2: UpgradeOfficer

## QL_MAIN_T3_SIDEIYAT
### qm_t3_facIyatequa:
* Name: Blue Collar Work
* Description: Ekekko informed us about exclusive work needed by the Iyatequa, and the traders will pay well for this assistance. This is below the table work on various jobs they don’t widely advertise for. They do not say what the ultimate purpose of this work is, though.
* QuestLine: ql_main_t3_sideIyat
* Type: Main
* FollowUps:
	* ql_main_t3_Cang
	* ql_main_t3_Cang_A
	* ql_main_t3_Cang_B
	* ql_main_t3_Cang_C
* Goals:
	* Task 1: Complete 2 of qm_t3_sideIyatequa_A_3|qm_t3_sideIyatequa_B_3|qm_t3_sideIyatequa_C_3
	* Task 2: Goto Iyatequa's system SARAAL

## QL_MAIN_T3_SIDEIYAT_A
### qm_t3_sideIyatequa_A_1:
* Name: Contracts: The Empty Quarter I
* Description: A small world in the Empty Quarter is looking for trustworthy connections. They offer an assortment of various tasks.
* QuestLine: ql_main_t3_sideIyat_A
* Type: Side
* Goals:
	* Task 1: 
		* 7 Faction_Tr1_T3up
		* 2250 PlayerXP

### qm_t3_sideIyatequa_A_2:
* Name: Contracts: The Empty Quarter II
* Description: A wealthy socialite has heard of our accomplishments and wants some things done. Discreetly, of course.
* QuestLine: ql_main_t3_sideIyat_A
* Type: Side
* Goals:
	* Task 1: 
		* 500 RepTr1
		* 1000 Refining3N_Refining3O_Refining3P_Refining3Q

### qm_t3_sideIyatequa_A_3:
* Name: Contracts: The Empty Quarter III
* Description: Our contact in the Empty Quarter is looking for new opportunities and has been pleased with our work so far. They want us to scout out new areas of space in order to expand their influence.
* QuestLine: ql_main_t3_sideIyat_A
* Type: Side
* Goals:
	* Task 1: 
		* 8500 RepTr1
		* Scan

## QL_MAIN_T3_SIDEIYAT_B
### qm_t3_sideIyatequa_B_1:
* Name: Contracts: Territory Claim I
* Description: The Iyatequa plan to set up new trading routes in space currently riddled by pirates. They asked us to clean up the area.
* QuestLine: ql_main_t3_sideIyat_B
* Type: Side
* Goals:
	* Task 1: 
		* Scan
		* 35 ShipsDestroyedP1

### qm_t3_sideIyatequa_B_2:
* Name: Contracts: Territory Claim II
* Description: Some pirates apparently didn't get the hint yet. We should show them the Iyatequa mean business.
* QuestLine: ql_main_t3_sideIyat_B
* Type: Side
* Goals:
	* Task 1: 
		* Complete 8 side missions
		* GainItem

### qm_t3_sideIyatequa_B_3:
* Name: Contracts: Territory Claim III
* Description: Most pirates have dispersed, but just to make sure they do not come back we should increase our reputation so future raiders will think twice before setting up nests here.
* QuestLine: ql_main_t3_sideIyat_B
* Type: Side
* Goals:
	* Task 1: 
		* Complete 5 side missions
		* Complete 2 side missions

## QL_MAIN_T3_SIDEIYAT_C
### qm_t3_sideIyatequa_C_1:
* Name: Contracts: Supplies I
* Description: A local world wants help building and supplying a space station. We are asked to test possible mining sites and clear them of hostiles.
* QuestLine: ql_main_t3_sideIyat_C
* Type: Side
* Goals:
	* Task 1: 
		* 6000 Mined3A_Mined3B_Mined3C_Mined3D
		* 55 ShipsDestroyed

### qm_t3_sideIyatequa_C_2:
* Name: Contracts: Supplies II
* Description: Mining ships have departed for the asteroids we have charted, but the internal systems require special gases. We are asked to sample the gases at promising jovians.
* QuestLine: ql_main_t3_sideIyat_C
* Type: Side
* Goals:
	* Task 1: 
		* 600 Mined3E_Mined3F_Mined3G_Mined3H
		* 100 Mined3H

### qm_t3_sideIyatequa_C_3:
* Name: Contracts: Supplies III
* Description: The mining sites have been prepared, but the Iyatequa asked us with further assistance through supplies and mining craft.
* QuestLine: ql_main_t3_sideIyat_C
* Type: Side
* Goals:
	* Task 1: 
		* Pay 150 GU Type G Gas T3
		* Pay 300 RU Type B Refined T3
		* Pay 50 Small Hull Parts

## QL_MAIN_T3_CANG
### qm_t3_facCangacian:
* Name: Roadblocks
* Description: Reports at the Tanoch border are coming in stating that the Fleet of Rams, Supay’s army, is on the move at last.
* QuestLine: ql_main_t3_Cang
* Type: Main
* FollowUps: ql_main_t3_sijinLighthouse
* Goals:
	* Task 1: Complete 2 of qm_t3_sideCangacian_A_3|qm_t3_sideCangacian_B_3|qm_t3_sideCangacian_C_3

## QL_MAIN_T3_CANG_A
### qm_t3_sideCangacian_A_1:
* Name: Defense: Intercept I
* Description: We are asked to intercept as many Cangacian fleets as we can.
* QuestLine: ql_main_t3_Cang_A
* Type: Side
* Goals:
	* Task 1: 
		* 40 ShipsDestroyedP1
		* GainItem

### qm_t3_sideCangacian_A_2:
* Name: Defense: Intercept II
* Description: The Cangacians continue to probe the Tanoch defenses. We should look for suspicious activity.
* QuestLine: ql_main_t3_Cang_A
* Type: Side
* Goals:
	* Task 1: 
		* Scan
		* Complete 9 side missions

### qm_t3_sideCangacian_A_3:
* Name: Defense: Intercept III
* Description: Supay's fleets may have holdouts in systems we have not been looking yet. We should find those and flush them out.
* QuestLine: ql_main_t3_Cang_A
* Type: Side
* Goals:
	* Task 1: 
		* Complete 4 side missions
		* Scan

## QL_MAIN_T3_CANG_B
### qm_t3_sideCangacian_B_1:
* Name: Defense: Assist I
* Description: To counter these attacks our crew must be well trained.
* QuestLine: ql_main_t3_Cang_B
* Type: Side
* Goals:
	* Task 1: 
		* GainItem
		* UpgradeOfficer

### qm_t3_sideCangacian_B_2:
* Name: Defense: Assist II
* Description: Our crew is analyzing the attack patterns to find ways to predict where the Fleet of Rams may strike next.
* QuestLine: ql_main_t3_Cang_B
* Type: Side
* Goals:
	* Task 1: 
		* GainItem
		* 2500 PlayerXP

### qm_t3_sideCangacian_B_3:
* Name: Defense: Assist III
* Description: Several smaller worlds on the border have sent us some of their recruits, in hopes they could get some practical experience from our battles with the Cangacians.
* QuestLine: ql_main_t3_Cang_B
* Type: Side
* Goals:
	* Task 1: Complete 10 side missions
	* Task 2: UpgradeOfficer

## QL_MAIN_T3_CANG_C
### qm_t3_sideCangacian_C_1:
* Name: Defense: Barricade I
* Description: Several mining fleets of the border systems have taken losses and are asking us to provide them with safe locations to find resources.
* QuestLine: ql_main_t3_Cang_C
* Type: Side
* Goals:
	* Task 1: 
		* 80 ScannedBelt
		* 1500 Refining3N_Refining3O_Refining3P_Refining3Q

### qm_t3_sideCangacian_C_2:
* Name: Defense: Barricade II
* Description: The remaining mining fleets are flocking to the new mining spots, but they require gases for advanced weaponry.
* QuestLine: ql_main_t3_Cang_C
* Type: Side
* Goals:
	* Task 1: 
		* 40 ScannedJovian
		* 750 Mined3E_Mined3F_Mined3G_Mined3H

### qm_t3_sideCangacian_C_3:
* Name: Defense: Barricade III
* Description: The border worlds' new mining lanes are buzzing with activity, but they need supplies to build up defenses against future raids.
* QuestLine: ql_main_t3_Cang_C
* Type: Side
* Goals:
	* Task 1: 
		* Pay 20 Small Hull Parts
		* Pay 20 Small Weapon Parts
		* Pay 20 Small Machinery Parts

## QL_MAIN_T3_SIJINLIGHTHOUSE
### qm_t3_sijinLighthouse:
* Name: Sijin Lighthouse
* Description: We detected a possible signal from the missing Khar-Kalaad.
* QuestLine: ql_main_t3_sijinLighthouse
* Type: Main
* CinematicIds: 40
* FollowUps: ql_main_t4_intro
* Goals:
	* Task 1: Complete mission 'Sijin Lighthouse'

## QL_MAIN_T4_INTRO
### qm_t4_researchJumpCap:
* Name: Mind the Gap
* Description: Crossing the Nightmare Gulf requires an upgrade to our hyperjump technology. After some scans of the gate at Sijin Lighthouse, our scientists think they are able to make the leap possible.
* QuestLine: ql_main_t4_intro
* Type: Main
* FollowUps: ql_main_t4_iliyinLighthouse
* Goals:
	* Task 1: Craft

## QL_MAIN_T4_ILIYINLIGHTHOUSE
### qm_t4_iliyinLighthouse:
* Name: Iliyin Lighthouse
* Description: We have arrived at another lighthouse in uncharted territory. Be prepared for anything.
* QuestLine: ql_main_t4_iliyinLighthouse
* Type: Main
* FollowUps:
	* ql_raid_020
	* ql_raid_021
	* ql_raid_022
	* ql_main_t4_amassariLiaison
	* ql_main_t4_moonResources
* Goals:
	* Task 1: Complete mission 'Iliyin Lighthouse'

## QL_MAIN_T4_AMASSARILIAISON
### qm_t4_amassariLiaison:
* Name: Amassari Relations
* Description: The Amassari have opened their liaison office to us.
* QuestLine: ql_main_t4_amassariLiaison
* Type: Side
* Goals:
	* Task 1: 1000 RepAmassari

## QL_MAIN_T4_MOONRESOURCES
### qm_t4_moonResources:
* Name: Crystals
* Description: Crystals are a new type of resource that can be combined with refined metals into a composite material needed for advanced constructions. So far we have only been able to find them by chance in <color=#FBB03F>signals and liaison missions</color>.
* QuestLine: ql_main_t4_moonResources
* Type: Main
* FollowUps: ql_main_t4_brightTemple
* Goals:
	* Task 1: GainItem
	* Task 2: 100 Refining4V_Refining4W_Refining4X_Refining4Y

## QL_MAIN_T4_BRIGHTTEMPLE
### qm_t4_brightTemple:
* Name: Bright Temple
* Description: The Amassari here may contain answers about the nature of the Progenitor observer.
* QuestLine: ql_main_t4_brightTemple
* Type: Main
* FollowUps: ql_main_t4_postBrightTemple
* Goals:
	* Task 1: Complete mission 'Bright Temple'

## QL_MAIN_T4_POSTBRIGHTTEMPLE
### qm_t4_postBrightTemple_1:
* Name: Among the People
* Description: We should take this time to become better acquainted with the Amassari and their culture. Performing tasks for the assorted groups will accomplish this.
* QuestLine: ql_main_t4_postBrightTemple
* Type: Main
* Goals:
	* Task 1: 1000 RepAmassari

### qm_t4_postBrightTemple_2:
* Name: Fabrication Methods
* Description: A new technique for refining was discovered from the Amassari. Test this process by refining rare earths.
* QuestLine: ql_main_t4_postBrightTemple
* Type: Main
* Goals:
	* Task 1: GainItem

### qm_t4_postBrightTemple_3:
* Name: Experience and Knowledge
* Description: Our crews need a new round of training to become familiar with Amassari practices and tactics.
* QuestLine: ql_main_t4_postBrightTemple
* Type: Main
* FollowUps: ql_main_t4_hataldan
* Goals:
	* Task 1: GainItem

## QL_MAIN_T4_HATALDAN
### qm_t4_hataldan:
* Name: Hataldan
* Description: The fallen capital of the Amassari, and last known position of the Observer.
* QuestLine: ql_main_t4_hataldan
* Type: Main
* FollowUps: ql_main_t4_postHataldan
* Goals:
	* Task 1: Complete mission 'Hataldan'

## QL_MAIN_T4_POSTHATALDAN
### qm_t4_postHataldan_1:
* Name: The Hunt Begins
* Description: The search begins for Kidara and the stolen Observer. We must examine any objects we can find scattered around for clues about her whereabouts.
* QuestLine: ql_main_t4_postHataldan
* Type: Main
* Goals:
	* Task 1: Scan

### qm_t4_postHataldan_2:
* Name: Forcible Interrogation
* Description: Destroying Kiithless ships and scavenging their databanks could fill some gaps in our intelligence about the Kiithless. The hunt continues!
* QuestLine: ql_main_t4_postHataldan
* Type: Main
* Goals:
	* Task 1: 50 ShipsDestroyedDarkHiigaranT4

### qm_t4_postHataldan_3:
* Name: Pieces of the Puzzle
* Description: A cryptic clue that emerged from harvesting Kiithless vessels may have a solution if we can piece together a saga from the Hagthar Empire. Collect relics from these ancient people.
* QuestLine: ql_main_t4_postHataldan
* Type: Main
* FollowUps: ql_main_t4_nightmareGulf
* Goals:
	* Task 1: GainItem

## QL_MAIN_T4_NIGHTMAREGULF
### qm_t4_nightmareGulf:
* Name: Nightmare Gulf
* Description: The Hagthar knew of pockets and safe regions close to this massive interstellar storm. We now know the way to Kidara's hideout in The Nightmare Gulf. It's time to end this.
* QuestLine: ql_main_t4_nightmareGulf
* Type: Main
* FollowUps:
	* ql_raid_023
	* ql_main_t4_strikeNightmareGulf
	* ql_main_t4_tanWin
* Goals:
	* Task 1: Complete mission 'Nightmare Gulf'

## QL_MAIN_T4_STRIKENIGHTMAREGULF
### qm_t4_strikeNightmareGulf:
* Name: Strike at Nightmare Gulf
* Description: The Hagthar knew of pockets and safe regions close to this massive interstellar storm. We now know the way to Kidara's hideout in The Nightmare Gulf. It's time to end this.
* QuestLine: ql_main_t4_strikeNightmareGulf
* Type: Side
* Goals:
	* Task 1: Complete 1 of qr_023

## QL_MAIN_T4_TANWIN
### qm_t4_tanWin_DefendBase:
* Name: Gesture of Aid
* Description: We received emergency communication from the Chicuat Elders. They anticipate a raid on one of their remote trading stations. Toci asks us to take on the defense in order to relieve the weakened and overextended Chicuat forces.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* QuestLine: ql_main_t4_tanWin
* Type: Main
* Goals:
	* Task 1: Complete mission 'Repulse Raid T4'

### qm_t4_tanWin_AttackBase:
* Name: In the Shadows
* Description: Intelligence from the Chicuat points to a Tecuban base operating around an uninhabited planet. We must go there and eliminate this base to stop the raids.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* QuestLine: ql_main_t4_tanWin
* Type: Main
* Goals:
	* Task 1: Complete mission 'Base Busting T4'

### qm_t4_tanWin_Relic:
* Name: Attack the Vaygr
* Description: In our search for the Vaygr involved with the Tecuban, we aquired one of their communication frequencies. If we contact the Vaygr now, we should be able to trace their signal and hyper jump to their exact location.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* QuestLine: ql_main_t4_tanWin
* Type: Main
* Goals:
	* Task 1: Complete mission 'Destination T4'

### qm_t4_tanWin_Academy:
* Name: Showdown at the Academy
* Description: We finally learned Jochik Kaan's intentions. He sparked the flames of war to weaken the Chicuat defenses and steal the Baetyl from Tlapallan Academy, one of their key centers of learning. We must travel there at once, before it is too late.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* QuestLine: ql_main_t4_tanWin
* Type: Main
* FollowUps: ql_main_t4_yaoSpr
* Goals:
	* Task 1: Complete mission 'Tlapallan Academy T4'

## QL_MAIN_T4_YAOSPR
### qm_t4_yaoSpr_Conjunction:
* Name: The Promised Place
* Description: Chocoan has provided the coordinates to the next astral conjunction event. Strong hostile forces are to be expected in this system. Our goal is to both protect the civilian pilgrims and find out more about the suspected secret agenda of the Yaot Elders.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* QuestLine: ql_main_t4_yaoSpr
* Type: Main
* Goals:
	* Task 1: Complete mission 'Conjunction T4'

## QL_ORB_T3_INTRO
### qm_orb_t3_components:
* Name: Starbase Components
* Description: <color=#FBB03F>The blueprints for starbase components can be found in the liaison requisitions offices.</color>

Our engineers have come up with a plan to build a starbase, which will serve as our base of operations. Before we can do that, however, we need to construct the necessary components.
* QuestLine: ql_orb_t3_intro
* Type: Side
* Goals:
	* Task 1: 
		* Craft
		* Craft
		* Craft

### qm_orb_t3_orbital:
* Name: Starbase
* Description: <color=#FBB03F>The blueprint for the starbase can be found in the regular market.</color>

Now that we have the components, we can build the starbase proper. Once the pieces have been constructed, it can be quickly assembled in orbit around celestial objects.
* QuestLine: ql_orb_t3_intro
* Type: Side
* Goals:
	* Task 1: Craft

### qm_orb_t3_placeOrbital:
* Name: Starbase Placement
* Description: <color=#FBB03F>Place or relocate your starbase by selecting a celestial object in the target list inside the star system view.</color>

Our finished starbase is ready and can be placed in orbit of a planet or moon.
* QuestLine: ql_orb_t3_intro
* Type: Side
* Goals:
	* Task 1: PlaceOrbital

### qm_orb_t3_modules:
* Name: Starbase Modules
* Description: <color=#FBB03F>The regular fabricator and refinery module can be mounted on the starbase, but there are specialized starbase modules. Blueprints for some of those can be found in the liaison requisitions offices.</color>

Now that our starbase is finished, we can start filling it up with modules.
* QuestLine: ql_orb_t3_intro
* Type: Side
* Goals:
	* Task 1: Equip Internal

## QL_EXAMPLE
### quest_example:

## QL_ESCA_KILLPIRATE1
### qs_killPirate1_pre01:
* Name: Cangacian Raider Fleets I
* Description: Pirates known as the Cangacians are harassing trade fleets of the Iyatequa.
* QuestLine: ql_esca_killPirate1
* Type: Achievement
* Goals:
	* Task 1: 10 ShipsDestroyedP1

### qs_killPirate1_00:
* Name: Cangacian Raider Fleets II
* Description: More Cangacian activity is being reported.
* QuestLine: ql_esca_killPirate1
* Type: Achievement
* Goals:
	* Task 1: 25 ShipsDestroyedP1

### qs_killPirate1_01:
* Name: Cangacian Raider Fleets III
* Description: Give the pirates a bloody nose. Show them you're no pushover.
* QuestLine: ql_esca_killPirate1
* Type: Achievement
* Goals:
	* Task 1: 50 ShipsDestroyedP1

### qs_killPirate1_02:
* Name: Cangacian Raider Fleets IV
* Description: Hunt down pirate ships to suppress their activities in the area.
* QuestLine: ql_esca_killPirate1
* Type: Achievement
* Goals:
	* Task 1: 100 ShipsDestroyedP1

### qs_killPirate1_03:
* Name: Cangacian Raider Fleets V
* Description: Beat back the local pirates by eliminating most of their forces.
* QuestLine: ql_esca_killPirate1
* Type: Achievement
* FollowUps: ql_esca_killYaot
* Goals:
	* Task 1: 200 ShipsDestroyedP1

### qs_killPirate1_04:
* Name: Cangacian Raider Fleets VI
* Description: An organized pirate force has moved into the area. Show them they are not welcome.
* QuestLine: ql_esca_killPirate1
* Type: Achievement
* Goals:
	* Task 1: 400 ShipsDestroyedP1

### qs_killPirate1_05:
* Name: Cangacian Raider Fleets VII
* Description: The Fleet of Rams has increased their presence. Meet them with equal enmity.
* QuestLine: ql_esca_killPirate1
* Type: Achievement
* Goals:
	* Task 1: 800 ShipsDestroyedP1

### qs_killPirate1_06:
* Name: Cangacian Raider Fleets VIII
* Description: The Fleet of Rams is hunting the local defenders. Oppose them with force!
* QuestLine: ql_esca_killPirate1
* Type: Achievement
* Goals:
	* Task 1: 1600 ShipsDestroyedP1

### qs_killPirate1_07:
* Name: Cangacian Raider Fleets IX
* Description: Supay himself has routed one of his fleets to the area. Engage them at will!
* QuestLine: ql_esca_killPirate1
* Type: Achievement
* Goals:
	* Task 1: 3200 ShipsDestroyedP1

### qs_killPirate1_08:
* Name: Cangacian Raider Fleets X
* Description: Send a message to Supay, warlord of the Fleet of Rams. Destroy one of his fleets.
* QuestLine: ql_esca_killPirate1
* Type: Achievement
* Goals:
	* Task 1: 6400 ShipsDestroyedP1

## QL_ESCA_KILLYAOT
### qs_killYaot_pre01:
* Name: Yaot Rebel Fleets I
* Description: Some Yaot that are dissatisfied with the government have begun causing chaos in regional space.
* QuestLine: ql_esca_killYaot
* Type: Achievement
* Goals:
	* Task 1: 10 ShipsDestroyedYaot

### qs_killYaot_00:
* Name: Yaot Rebel Fleets II
* Description: More Yaot rebels have been reported.
* QuestLine: ql_esca_killYaot
* Type: Achievement
* Goals:
	* Task 1: 25 ShipsDestroyedYaot

### qs_killYaot_01:
* Name: Yaot Rebel Fleets III
* Description: Attack the Yaot patrols to drive them from this area.
* QuestLine: ql_esca_killYaot
* Type: Achievement
* Goals:
	* Task 1: 50 ShipsDestroyedYaot

### qs_killYaot_02:
* Name: Yaot Rebel Fleets IV
* Description: Continue attacking the Yaot to drive them from the region.
* QuestLine: ql_esca_killYaot
* Type: Achievement
* Goals:
	* Task 1: 100 ShipsDestroyedYaot

### qs_killYaot_03:
* Name: Yaot Rebel Fleets V
* Description: Yaot Fleet captains recognize your silhouette. Continue the attack.
* QuestLine: ql_esca_killYaot
* Type: Achievement
* FollowUps: ql_esca_killTanoch
* Goals:
	* Task 1: 200 ShipsDestroyedYaot

### qs_killYaot_04:
* Name: Yaot Rebel Fleets VI
* Description: Yaot sensors are alerted to your presence. Continue the attack!
* QuestLine: ql_esca_killYaot
* Type: Achievement
* Goals:
	* Task 1: 400 ShipsDestroyedYaot

### qs_killYaot_05:
* Name: Yaot Rebel Fleets VII
* Description: Yaot Fleet commanders are watching out for you. Continue your assaults against them!
* QuestLine: ql_esca_killYaot
* Type: Achievement
* Goals:
	* Task 1: 800 ShipsDestroyedYaot

### qs_killYaot_06:
* Name: Yaot Rebel Fleets VIII
* Description: Your name is mentioned between Yaot Fleet commanders. Continue your attacks!
* QuestLine: ql_esca_killYaot
* Type: Achievement
* Goals:
	* Task 1: 1600 ShipsDestroyedYaot

### qs_killYaot_07:
* Name: Yaot Rebel Fleets IX
* Description: You are impacting Yaot fleet operations in this area. Continue your attack!
* QuestLine: ql_esca_killYaot
* Type: Achievement
* Goals:
	* Task 1: 3200 ShipsDestroyedYaot

### qs_killYaot_08:
* Name: Yaot Rebel Fleets X
* Description: Your threat level among the Yaot is higher than most Tanoch fleets. Continue the attack!
* QuestLine: ql_esca_killYaot
* Type: Achievement
* Goals:
	* Task 1: 6400 ShipsDestroyedYaot

## QL_ESCA_KILLTANOCH
### qs_killTanoch_pre01:
* Name: Tanoch Renegade Fleets I
* Description: Renegades of the Tanoch nation are disrupting the peace of the empire.
* QuestLine: ql_esca_killTanoch
* Type: Achievement
* Goals:
	* Task 1: 10 ShipsDestroyedTanoch

### qs_killTanoch_00:
* Name: Tanoch Renegade Fleets II
* Description: More renegade fleets are being reported.
* QuestLine: ql_esca_killTanoch
* Type: Achievement
* Goals:
	* Task 1: 25 ShipsDestroyedTanoch

### qs_killTanoch_01:
* Name: Tanoch Renegade Fleets III
* Description: Poach Tanoch patrols to weaken their activities in the area. Hostile Tanoch signals have been located in T2 systems and higher.
* QuestLine: ql_esca_killTanoch
* Type: Achievement
* Goals:
	* Task 1: 50 ShipsDestroyedTanoch

### qs_killTanoch_02:
* Name: Tanoch Renegade Fleets IV
* Description: Continue to attack Tanoch patrols to weaken their local status. Hostile Tanoch signals have been located in T2 systems and higher.
* QuestLine: ql_esca_killTanoch
* Type: Achievement
* Goals:
	* Task 1: 100 ShipsDestroyedTanoch

### qs_killTanoch_03:
* Name: Tanoch Renegade Fleets V
* Description: Tanoch freighter crews fear your arrival. Continue the attacks! Hostile Tanoch signals have been located in T2 systems and higher.
* QuestLine: ql_esca_killTanoch
* Type: Achievement
* Goals:
	* Task 1: 200 ShipsDestroyedTanoch

### qs_killTanoch_04:
* Name: Tanoch Renegade Fleets VI
* Description: Tanoch freighters request action against you. Continue the attacks! Hostile Tanoch signals have been located in T2 systems and higher.
* QuestLine: ql_esca_killTanoch
* Type: Achievement
* Goals:
	* Task 1: 400 ShipsDestroyedTanoch

### qs_killTanoch_05:
* Name: Tanoch Renegade Fleets VII
* Description: The Tanoch patrol force recognizes you on sight. Continue the attacks! Hostile Tanoch signals have been located in T2 systems and higher.
* QuestLine: ql_esca_killTanoch
* Type: Achievement
* Goals:
	* Task 1: 800 ShipsDestroyedTanoch

### qs_killTanoch_06:
* Name: Tanoch Renegade Fleets VIII
* Description: Tanoch warning stations alert the Empire to your presence. Continue your attacks! Hostile Tanoch signals have been located in T2 systems and higher.
* QuestLine: ql_esca_killTanoch
* Type: Achievement
* Goals:
	* Task 1: 1600 ShipsDestroyedTanoch

### qs_killTanoch_07:
* Name: Tanoch Renegade Fleets IX
* Description: The Tanoch regard you as a fleet-level threat. Continue your assaults against them! Hostile Tanoch signals have been located in T2 systems and higher.
* QuestLine: ql_esca_killTanoch
* Type: Achievement
* Goals:
	* Task 1: 3200 ShipsDestroyedTanoch

### qs_killTanoch_08:
* Name: Tanoch Renegade Fleets X
* Description: The Emperor will know your name. Hostile Tanoch signals have been located in T2 systems and higher.
* QuestLine: ql_esca_killTanoch
* Type: Achievement
* Goals:
	* Task 1: 6400 ShipsDestroyedTanoch

## QL_ESCA_MINET1
### qs_mineT1ABC_pre01:
* Name: Mining Procedures I
* Description: We need to test our mining equipment.
* QuestLine: ql_esca_mineT1
* Type: Achievement
* Goals:
	* Task 1: 
		* 1000 Mined1A
		* 1000 Mined1B
		* 1000 Mined1C

### qs_mineT1ABC_00:
* Name: Mining Procedures II
* Description: We should check our mining procedures and see if we could streamline the process.
* QuestLine: ql_esca_mineT1
* Type: Achievement
* Goals:
	* Task 1: 
		* 3000 Mined1A
		* 3000 Mined1B
		* 3000 Mined1C

### qs_mineT1ABC_01:
* Name: Mining Procedures III
* Description: Start collecting asteroids to calibrate our resource refinery methods.
* QuestLine: ql_esca_mineT1
* Type: Achievement
* Goals:
	* Task 1: 
		* 6000 Mined1A
		* 6000 Mined1B
		* 6000 Mined1C

### qs_mineT1ABC_02:
* Name: Mining Procedures IV
* Description: More materials are necessary to establish our baseline. Harvest more asteroids.
* QuestLine: ql_esca_mineT1
* Type: Achievement
* Goals:
	* Task 1: 
		* 12000 Mined1A
		* 12000 Mined1B
		* 12000 Mined1C

### qs_mineT1ABC_03:
* Name: Mining Procedures V
* Description: Our refineries have been calibrated to local nimbus materials. Begin our first production haul.
* QuestLine: ql_esca_mineT1
* Type: Achievement
* FollowUps: ql_esca_mineT2
* Goals:
	* Task 1: 
		* 24000 Mined1A
		* 24000 Mined1B
		* 24000 Mined1C

### qs_mineT1ABC_04:
* Name: Mining Procedures VI
* Description: Begin our second production haul for processing.
* QuestLine: ql_esca_mineT1
* Type: Achievement
* Goals:
	* Task 1: 
		* 48000 Mined1A
		* 48000 Mined1B
		* 48000 Mined1C

### qs_mineT1ABC_05:
* Name: Mining Procedures VII
* Description: Begin our third production haul for processing.
* QuestLine: ql_esca_mineT1
* Type: Achievement
* Goals:
	* Task 1: 
		* 96000 Mined1A
		* 96000 Mined1B
		* 96000 Mined1C

### qs_mineT1ABC_06:
* Name: Mining Procedures VIII
* Description: Begin our fourth production haul for processing.
* QuestLine: ql_esca_mineT1
* Type: Achievement
* Goals:
	* Task 1: 
		* 192000 Mined1A
		* 192000 Mined1B
		* 192000 Mined1C

### qs_mineT1ABC_07:
* Name: Mining Procedures IX
* Description: One final haul is needed to certify the refinery for full operations.
* QuestLine: ql_esca_mineT1
* Type: Achievement
* Goals:
	* Task 1: 
		* 384000 Mined1A
		* 384000 Mined1B
		* 384000 Mined1C

### qs_mineT1ABC_08:
* Name: Mining Procedures X
* Description: One last production haul is needed to certify the refinery for Grade 1 Procesing.
* QuestLine: ql_esca_mineT1
* Type: Achievement
* Goals:
	* Task 1: 
		* 768000 Mined1A
		* 768000 Mined1B
		* 768000 Mined1C

## QL_ESCA_MINET2
### qs_mineT2ABC_pre01:
* Name: New Mining Procedures I
* Description: We need to test our mining equipment on these new types of minerals.
* QuestLine: ql_esca_mineT2
* Type: Achievement
* Goals:
	* Task 1: 
		* 1000 Mined2A
		* 1000 Mined2B
		* 1000 Mined2C

### qs_mineT2ABC_00:
* Name: New Mining Procedures II
* Description: We should check our mining procedures on these new types of minerals.
* QuestLine: ql_esca_mineT2
* Type: Achievement
* Goals:
	* Task 1: 
		* 3000 Mined2A
		* 3000 Mined2B
		* 3000 Mined2C

### qs_mineT2ABC_01:
* Name: New Mining Procedures III
* Description: Engineering has proposed minor upgrades to the refinery process. Harvest larger asteroids for testing.
* QuestLine: ql_esca_mineT2
* Type: Achievement
* Goals:
	* Task 1: 
		* 6000 Mined2A
		* 6000 Mined2B
		* 6000 Mined2C

### qs_mineT2ABC_02:
* Name: New Mining Procedures IV
* Description: Engineering is ready to implement these minor changes. Continue supplying larger resources.
* QuestLine: ql_esca_mineT2
* Type: Achievement
* Goals:
	* Task 1: 
		* 12000 Mined2A
		* 12000 Mined2B
		* 12000 Mined2C

### qs_mineT2ABC_03:
* Name: New Mining Procedures V
* Description: Engineering wants to test further refits to the refinery. Supply additional resources for testing.
* QuestLine: ql_esca_mineT2
* Type: Achievement
* FollowUps: ql_esca_mineT3
* Goals:
	* Task 1: 
		* 24000 Mined2A
		* 24000 Mined2B
		* 24000 Mined2C

### qs_mineT2ABC_04:
* Name: New Mining Procedures VI
* Description: Continue refinery trials. Provide larger resources.
* QuestLine: ql_esca_mineT2
* Type: Achievement
* Goals:
	* Task 1: 
		* 48000 Mined2A
		* 48000 Mined2B
		* 48000 Mined2C

### qs_mineT2ABC_05:
* Name: New Mining Procedures VII
* Description: Continue refinery trials. Provide larger resources.
* QuestLine: ql_esca_mineT2
* Type: Achievement
* Goals:
	* Task 1: 
		* 96000 Mined2A
		* 96000 Mined2B
		* 96000 Mined2C

### qs_mineT2ABC_06:
* Name: New Mining Procedures VIII
* Description: Continue refinery trials. Provide larger resources.
* QuestLine: ql_esca_mineT2
* Type: Achievement
* Goals:
	* Task 1: 
		* 192000 Mined2A
		* 192000 Mined2B
		* 192000 Mined2C

### qs_mineT2ABC_07:
* Name: New Mining Procedures IX
* Description: Continue refinery trials. Provide larger resources.
* QuestLine: ql_esca_mineT2
* Type: Achievement
* Goals:
	* Task 1: 
		* 384000 Mined2A
		* 384000 Mined2B
		* 384000 Mined2C

### qs_mineT2ABC_08:
* Name: New Mining Procedures X
* Description: One final load is necessary to approve the new refit to the refinery.
* QuestLine: ql_esca_mineT2
* Type: Achievement
* Goals:
	* Task 1: 
		* 768000 Mined2A
		* 768000 Mined2B
		* 768000 Mined2C

## QL_ESCA_MINET3
### qs_mineT3ABC_pre01:
* Name: Advanced Mining Procedures I
* Description: We need to test our mining equipment on these new types of minerals.
* QuestLine: ql_esca_mineT3
* Type: Achievement
* Goals:
	* Task 1: 
		* 1000 Mined3A
		* 1000 Mined3B
		* 1000 Mined3C

### qs_mineT3ABC_00:
* Name: Advanced Mining Procedures II
* Description: We should check our mining procedures on these new types of minerals.
* QuestLine: ql_esca_mineT3
* Type: Achievement
* Goals:
	* Task 1: 
		* 3000 Mined3A
		* 3000 Mined3B
		* 3000 Mined3C

### qs_mineT3ABC_01:
* Name: Advanced Mining Procedures III
* Description: Refinery teams propose a new chemical process for resource extraction.
* QuestLine: ql_esca_mineT3
* Type: Achievement
* Goals:
	* Task 1: 
		* 6000 Mined3A
		* 6000 Mined3B
		* 6000 Mined3C

### qs_mineT3ABC_02:
* Name: Advanced Mining Procedures IV
* Description: Supply reduced manpower tests by harvesting further resources.
* QuestLine: ql_esca_mineT3
* Type: Achievement
* Goals:
	* Task 1: 
		* 12000 Mined3A
		* 12000 Mined3B
		* 12000 Mined3C

### qs_mineT3ABC_03:
* Name: Advanced Mining Procedures V
* Description: Conducting reduced manpower stress test on refinery complex.
* QuestLine: ql_esca_mineT3
* Type: Achievement
* Goals:
	* Task 1: 
		* 24000 Mined3A
		* 24000 Mined3B
		* 24000 Mined3C

### qs_mineT3ABC_04:
* Name: Advanced Mining Procedures VI
* Description: Conducting reduced manpower stress test on refinery complex.
* QuestLine: ql_esca_mineT3
* Type: Achievement
* Goals:
	* Task 1: 
		* 48000 Mined3A
		* 48000 Mined3B
		* 48000 Mined3C

### qs_mineT3ABC_05:
* Name: Advanced Mining Procedures VII
* Description: Conducting reduced manpower stress test on refinery complex.
* QuestLine: ql_esca_mineT3
* Type: Achievement
* Goals:
	* Task 1: 
		* 96000 Mined3A
		* 96000 Mined3B
		* 96000 Mined3C

### qs_mineT3ABC_06:
* Name: Advanced Mining Procedures VIII
* Description: Conducting reduced manpower stress test on refinery complex.
* QuestLine: ql_esca_mineT3
* Type: Achievement
* Goals:
	* Task 1: 
		* 192000 Mined3A
		* 192000 Mined3B
		* 192000 Mined3C

### qs_mineT3ABC_07:
* Name: Advanced Mining Procedures IX
* Description: Final test of reduced crew capacity through new refinery process. Procure resources.
* QuestLine: ql_esca_mineT3
* Type: Achievement
* Goals:
	* Task 1: 
		* 384000 Mined3A
		* 384000 Mined3B
		* 384000 Mined3C

### qs_mineT3ABC_08:
* Name: Advanced Mining Procedures X
* Description: Final certification of refinery postprocessing procedure. Supply resources for this test.
* QuestLine: ql_esca_mineT3
* Type: Achievement
* Goals:
	* Task 1: 
		* 768000 Mined3A
		* 768000 Mined3B
		* 768000 Mined3C

## QL_ESCA_SCAN
### qs_scan_pre01:
* Name: System Charts I
* Description: We should explore the star systems in this new galaxy.
* QuestLine: ql_esca_scan
* Type: Achievement
* Goals:
	* Task 1: 50 Scanned

### qs_scan_00:
* Name: System Charts II
* Description: We need to fill our system charts with actual data.
* QuestLine: ql_esca_scan
* Type: Achievement
* Goals:
	* Task 1: 150 Scanned

### qs_scan_01:
* Name: System Charts III
* Description: The new sensor suite needs raw data to begin configuring the array. Begin scanning.
* QuestLine: ql_esca_scan
* Type: Achievement
* FollowUps: ql_esca_generated
* Goals:
	* Task 1: 300 Scanned

### qs_scan_02:
* Name: System Charts IV
* Description: The array is ready to begin trials. Begin scanning targets.
* QuestLine: ql_esca_scan
* Type: Achievement
* Goals:
	* Task 1: 600 Scanned

### qs_scan_03:
* Name: System Charts V
* Description: Begin testing short range detection sensors. Begin scanning targets.
* QuestLine: ql_esca_scan
* Type: Achievement
* Goals:
	* Task 1: 1200 Scanned

### qs_scan_04:
* Name: System Charts VI
* Description: Conduct scans. Calibration will focus on short range performance.
* QuestLine: ql_esca_scan
* Type: Achievement
* Goals:
	* Task 1: 2500 Scanned

### qs_scan_05:
* Name: System Charts VII
* Description: Conduct scans. Calibration will focus on long range performance.
* QuestLine: ql_esca_scan
* Type: Achievement
* Goals:
	* Task 1: 5000 Scanned

### qs_scan_06:
* Name: System Charts VIII
* Description: Conduct Scans. Calibration will focus on hyperspace oddities.
* QuestLine: ql_esca_scan
* Type: Achievement
* Goals:
	* Task 1: 10000 Scanned

### qs_scan_07:
* Name: System Charts IX
* Description: Conduct scans. Calibration will focus on signals moving at distance.
* QuestLine: ql_esca_scan
* Type: Achievement
* Goals:
	* Task 1: 20000 Scanned

### qs_scan_08:
* Name: System Charts X
* Description: Final comprehensive test of all sensor systems.
* QuestLine: ql_esca_scan
* Type: Achievement
* Goals:
	* Task 1: 40000 Scanned

## QL_ESCA_GENERATED
### qs_finishGenerated_pre01:
* Name: Signal Search I
* Description: We should look out for possible signals in deep space. They could represent opportunities for us.
* QuestLine: ql_esca_generated
* Type: Achievement
* Goals:
	* Task 1: 2 MissionsDoneGenerated

### qs_finishGenerated_00:
* Name: Signal Search II
* Description: We should actively search for signals in deep space.
* QuestLine: ql_esca_generated
* Type: Achievement
* Goals:
	* Task 1: 5 MissionsDoneGenerated

### qs_finishGenerated_01:
* Name: Signal Search III
* Description: Signals investigation for pathfinding and reconnaissance.
* QuestLine: ql_esca_generated
* Type: Achievement
* Goals:
	* Task 1: 10 MissionsDoneGenerated

### qs_finishGenerated_02:
* Name: Signal Search IV
* Description: Further investigate mysterious signals for pathfinding and reconnaissance.
* QuestLine: ql_esca_generated
* Type: Achievement
* Goals:
	* Task 1: 20 MissionsDoneGenerated

### qs_finishGenerated_03:
* Name: Signal Search V
* Description: Hunt for anomalous signals to unlock further discoveries and rewards.
* QuestLine: ql_esca_generated
* Type: Achievement
* Goals:
	* Task 1: 40 MissionsDoneGenerated

### qs_finishGenerated_04:
* Name: Signal Search VI
* Description: Establish signal gain and investigation methods.
* QuestLine: ql_esca_generated
* Type: Achievement
* Goals:
	* Task 1: 80 MissionsDoneGenerated

### qs_finishGenerated_05:
* Name: Signal Search VII
* Description: Routine investigation of anomalous signals.
* QuestLine: ql_esca_generated
* Type: Achievement
* Goals:
	* Task 1: 160 MissionsDoneGenerated

### qs_finishGenerated_06:
* Name: Signal Search VIII
* Description: Special teams designated for signal investigations response.
* QuestLine: ql_esca_generated
* Type: Achievement
* Goals:
	* Task 1: 320 MissionsDoneGenerated

### qs_finishGenerated_07:
* Name: Signal Search IX
* Description: Catalogue of anomalous activities established.
* QuestLine: ql_esca_generated
* Type: Achievement
* Goals:
	* Task 1: 640 MissionsDoneGenerated

### qs_finishGenerated_08:
* Name: Signal Search X
* Description: Investigative mastery.
* QuestLine: ql_esca_generated
* Type: Achievement
* Goals:
	* Task 1: 1300 MissionsDoneGenerated

## QL_KEID
### qs_Keid_01:
* Name: The Siege of Keid
* Description: Keid is struggling under the weight of enemy attacks and depleted resources. Help them take back control of the system.
* QuestLine: ql_Keid
* Type: Side
* Goals:
	* Task 1: Goto Iyatequa's system KEID
	* Task 2: 
		* Scan
		* Complete 10 side missions
		* 50 ShipsDestroyedT2

### qs_Keid_02:
* Name: Rebuilding Keid
* Description: The people of Keid suffer from a lack of resources. Support them by collecting and refining resources.
* QuestLine: ql_Keid
* Type: Side
* Goals:
	* Task 1: 
		* 2000 Mined2A
		* 2000 Mined2B
		* 2000 Mined2C
		* 1500 Mined2D
	* Task 2: 
		* 1000 Refining2N
		* 1000 Refining2O
		* 1000 Refining2P
		* 700 Refining2Q

### qs_Keid_03:
* Name: The Future of Keid
* Description: Donate your hard-earned resources and credits so that the people of Keid may fight on.
* QuestLine: ql_Keid
* Type: Side
* Goals:
	* Task 1: 
		* Pay 1000 RU Type A Refined T2 in Iyatequa's system KEID
		* Pay 1000 RU Type B Refined T2 in Iyatequa's system KEID
		* Pay 1000 RU Type C Refined T2 in Iyatequa's system KEID
	* Task 2: 
		* Pay 700 RU Type D Refined T2 in Iyatequa's system KEID
		* Pay 10000 Credits in Iyatequa's system KEID

## QL_YTEP
### qs_Ytep_01:
* Name: Ytep Under Fire
* Description: Help the people of Ytep take back control of the system by pushing back enemies.
* QuestLine: ql_Ytep
* Type: Side
* Goals:
	* Task 1: Goto Yaot's system YTEP
	* Task 2: 
		* Scan
		* Complete 10 side missions
		* 75 ShipsDestroyedT3

### qs_Ytep_02:
* Name: Supplying the War Effort
* Description: Collect enough parts and ships to support the war effort in Ytep.
* QuestLine: ql_Ytep
* Type: Side
* Goals:
	* Task 1: 
		* Craft
		* Craft
		* Craft
	* Task 2: 
		* Craft
		* Craft

### qs_Ytep_03:
* Name: To Strengthen Ytep
* Description: Donate T2 parts and ships to help the people of Ytep fight after you are gone.
* QuestLine: ql_Ytep
* Type: Side
* Goals:
	* Task 1: 
		* Pay 20 Small Hull Parts in Yaot's system YTEP
		* Pay 800 Small Weapon Parts in Yaot's system YTEP
		* Pay 800 Small Machinery Parts in Yaot's system YTEP
	* Task 2: 
		* Pay 1 Interceptor Squadron in Yaot's system YTEP
		* Pay 1 Assault Corvette Squadron in Yaot's system YTEP

## QL_EXILE
### qs_Exile_01:
* Name: A Test of Might
* Description: Destroy pirates and complete strikes to prove your strength.
* QuestLine: ql_Exile
* Type: Side
* Goals:
	* Task 1: 
		* Complete 10 side missions
		* 150 ShipsDestroyedP1

### qs_Exile_02:
* Name: The Nomad's Walk
* Description: Gather resources and craft units to demonstrate your independence and self-reliance.
* QuestLine: ql_Exile
* Type: Side
* Goals:
	* Task 1: 
		* 15000 Mined2A
		* 15000 Mined2B
		* 15000 Mined2C
	* Task 2: Craft

### qs_Exile_03:
* Name: The Cartographer's Promise
* Description: Travel across the galaxy and discover new locations to help chart the unknown.
* QuestLine: ql_Exile
* Type: Side
* Goals:
	* Task 1: 
		* Goto Iyatequa's system ESTRAIIR
		* Goto Yaot's system TUNDA MIRAAN
		* Goto Tanoch's system AXOCOTIL
	* Task 2: Scan

## QL_RAID_013
### qr_013:
* Name: Pirate Hideout
* Description: A lot of pirate activity has been reported in this region. The local pirate faction must have a major base here. Our task is to find the base, and destroy any pirate vessel and structure in this sector.
* QuestLine: ql_raid_013
* Type: Strike
* Goals:
	* Task 1: Complete mission 'Pirate Hideout'

## QL_RAID_014
### qr_014:
* Name: Station Defense
* Description: We have received intel that enemy forces are planning to attack a local trading station. In order to defend the station, we must immediately move our fleet into defensive position.
* QuestLine: ql_raid_014
* Type: Strike
* Goals:
	* Task 1: Complete mission 'Station Defense'

## QL_RAID_015
### qr_015:
* Name: Pahra's Rock
* Description: The presence of a large Cangacian asteroid base in this area has been threatening the Hiigaran settlements. Our task is to perform an attack on this base, destroy it and any Cangacian fleet nearby.
* QuestLine: ql_raid_015
* Type: Strike
* Goals:
	* Task 1: Complete mission 'Pahra's Rock'

## QL_RAID_016
### qr_016:
* Name: Pirate Hideout (Heroic)
* Description: A lot of pirate activity has been reported in this region. The local pirate faction must have a major base here. Our task is to find the base, and destroy any pirate vessel and structure in this sector.
* QuestLine: ql_raid_016
* Type: Strike
* Goals:
	* Task 1: Complete mission 'Pirate Hideout (Heroic)'

## QL_RAID_017
### qr_017:
* Name: Station Defense (Heroic)
* Description: We have received intel that enemy forces are planning to attack a local trading station. In order to defend the station, we must immediately move our fleet into defensive position.
* QuestLine: ql_raid_017
* Type: Strike
* Goals:
	* Task 1: Complete mission 'Station Defense (Heroic)'

## QL_RAID_018
### qr_018:
* Name: Pahra's Rock (Heroic)
* Description: The presence of a large Cangacian asteroid base in this area has been threatening the Hiigaran settlements. Our task is to perform an attack on this base, destroy it and any Cangacian fleet nearby.
* QuestLine: ql_raid_018
* Type: Strike
* Goals:
	* Task 1: Complete mission 'Pahra's Rock (Heroic)'

## QL_RAID_019
### qr_019:
* Name: Breach
* Description: Sitting in a safe pocket inside an electromagnetic asteroid field, this station is a crucial base of operation. As it is heavily defended, we came up with the cunning plan to fill an old freighter with explosives and escort it to the base.
* QuestLine: ql_raid_019
* Type: Strike
* Goals:
	* Task 1: Complete mission 'Breach'

## QL_RAID_020
### qr_020:
* Name: Breach (Heroic)
* Description: Sitting in a safe pocket inside an electromagnetic asteroid field, this station is a crucial base of operation. As it is heavily defended, we came up with the cunning plan to fill an old freighter with explosives and escort it to the base.
* QuestLine: ql_raid_020
* Type: Strike
* Goals:
	* Task 1: Complete mission 'Breach (Heroic)'

## QL_RAID_021
### qr_021:
* Name: Station Defense (Mythic)
* Description: We have received intel that enemy forces are planning to attack a local trading station. In order to defend the station, we must immediately move our fleet into defensive position.
* QuestLine: ql_raid_021
* Type: Strike
* Goals:
	* Task 1: Complete mission 'Station Defense (Mythic)'

## QL_RAID_022
### qr_022:
* Name: Pahra's Rock (Mythic)
* Description: The presence of a large Cangacian asteroid base in this area has been threatening the Hiigaran settlements. Our task is to perform an attack on this base, destroy it and any Cangacian fleet nearby.
* QuestLine: ql_raid_022
* Type: Strike
* Goals:
	* Task 1: Complete mission 'Pahra's Rock (Mythic)'

## QL_RAID_023
### qr_023:
* Name: Nightmare Gulf
* Description: A base used by Kiithless raiders has been located in this area of the nightmare gulf. A large attack force will be needed to destroy it and free the Progenitor assets held at this location.
* QuestLine: ql_raid_023
* Type: Strike
* Goals:
	* Task 1: Complete mission 'Nightmare Gulf'

## QL_EVENT_TEST_1
### qe_test_eventtestquest_1:
* Name: No header for quest qe_test_eventtestquest_1
* Description: No description for quest qe_test_eventtestquest_1
* QuestLine: ql_event_test_1
* Type: Event
* Goals:
	* Task 1: Craft

## QL_EVENT_TEST_2
### qe_test_eventtestquest_2:
* Name: No header for quest qe_test_eventtestquest_2
* Description: No description for quest qe_test_eventtestquest_2
* QuestLine: ql_event_test_2
* Type: Event
* Goals:
	* Task 1: Pay 10 Credits

## QL_EVENT_TEST_3
### qe_test_eventtestquest_3:
* Name: No header for quest qe_test_eventtestquest_3
* Description: No description for quest qe_test_eventtestquest_3
* QuestLine: ql_event_test_3
* Type: Event
* Goals:
	* Task 1: Complete side mission

## QL_YAOT_SPRING_2023_DAILY_A_T2
### qe_yaot_spring_2023_daily_A_t2:
* Name: No header for quest qe_yaot_spring_2023_daily_A_t2
* Description: No description for quest qe_yaot_spring_2023_daily_A_t2
* QuestLine: ql_yaot_spring_2023_daily_A_t2
* Type: Event
* EventId: event_season_yaoSpr_2023
* Goals:
	* Task 1: GainItem

## QL_YAOT_SPRING_2023_DAILY_B_T2
### qe_yaot_spring_2023_daily_B_t2:
* Name: No header for quest qe_yaot_spring_2023_daily_B_t2
* Description: No description for quest qe_yaot_spring_2023_daily_B_t2
* QuestLine: ql_yaot_spring_2023_daily_B_t2
* Type: Event
* EventId: event_season_yaoSpr_2023
* Goals:
	* Task 1: 10 ShipsDestroyedTanoch

## QL_YAOT_SPRING_2023_DAILY_C_T3
### qe_yaot_spring_2023_daily_C_t3:
* Name: No header for quest qe_yaot_spring_2023_daily_C_t3
* Description: No description for quest qe_yaot_spring_2023_daily_C_t3
* QuestLine: ql_yaot_spring_2023_daily_C_t3
* Type: Event
* EventId: event_season_yaoSpr_2023
* Goals:
	* Task 1: 100 Mined3E_Mined3F_Mined3G_Mined3H_Mined4E_Mined4F_Mined4G_Mined4H

## QL_YAOT_SPRING_2023_DAILY_D_T3
### qe_yaot_spring_2023_daily_D_t3:
* Name: No header for quest qe_yaot_spring_2023_daily_D_t3
* Description: No description for quest qe_yaot_spring_2023_daily_D_t3
* QuestLine: ql_yaot_spring_2023_daily_D_t3
* Type: Event
* EventId: event_season_yaoSpr_2023
* Goals:
	* Task 1: 5 Faction_Yaot

## QL_EVENT_YAOT_SPRING_2023
### qe_yaot_spring_2023_day1:
* Name: No header for quest qe_yaot_spring_2023_day1
* Description: No description for quest qe_yaot_spring_2023_day1
* QuestLine: ql_event_yaot_spring_2023
* Type: Event
* EventId: event_season_yaoSpr_2023
* Goals:
	* Task 1: 750 Mined

### qe_yaot_spring_2023_day2:
* Name: No header for quest qe_yaot_spring_2023_day2
* Description: No description for quest qe_yaot_spring_2023_day2
* QuestLine: ql_event_yaot_spring_2023
* Type: Event
* EventId: event_season_yaoSpr_2023
* Goals:
	* Task 1: Complete 3 side missions

### qe_yaot_spring_2023_day3:
* Name: No header for quest qe_yaot_spring_2023_day3
* Description: No description for quest qe_yaot_spring_2023_day3
* QuestLine: ql_event_yaot_spring_2023
* Type: Event
* EventId: event_season_yaoSpr_2023
* Goals:
	* Task 1: Craft

### qe_yaot_spring_2023_day4:
* Name: No header for quest qe_yaot_spring_2023_day4
* Description: No description for quest qe_yaot_spring_2023_day4
* QuestLine: ql_event_yaot_spring_2023
* Type: Event
* EventId: event_season_yaoSpr_2023
* Goals:
	* Task 1: GainItem

### qe_yaot_spring_2023_day5:
* Name: No header for quest qe_yaot_spring_2023_day5
* Description: No description for quest qe_yaot_spring_2023_day5
* QuestLine: ql_event_yaot_spring_2023
* Type: Event
* EventId: event_season_yaoSpr_2023
* Goals:
	* Task 1: UpgradeOfficer

### qe_yaot_spring_2023_day6:
* Name: No header for quest qe_yaot_spring_2023_day6
* Description: No description for quest qe_yaot_spring_2023_day6
* QuestLine: ql_event_yaot_spring_2023
* Type: Event
* EventId: event_season_yaoSpr_2023
* Goals:
	* Task 1: Complete 3 side missions

### qe_yaot_spring_2023_day7:
* Name: No header for quest qe_yaot_spring_2023_day7
* Description: No description for quest qe_yaot_spring_2023_day7
* QuestLine: ql_event_yaot_spring_2023
* Type: Event
* EventId: event_season_yaoSpr_2023
* Goals:
	* Task 1: 750 Mined

### qe_yaot_spring_2023_day8:
* Name: No header for quest qe_yaot_spring_2023_day8
* Description: No description for quest qe_yaot_spring_2023_day8
* QuestLine: ql_event_yaot_spring_2023
* Type: Event
* EventId: event_season_yaoSpr_2023
* Goals:
	* Task 1: GainItem

### qe_yaot_spring_2023_day9:
* Name: No header for quest qe_yaot_spring_2023_day9
* Description: No description for quest qe_yaot_spring_2023_day9
* QuestLine: ql_event_yaot_spring_2023
* Type: Event
* EventId: event_season_yaoSpr_2023
* Goals:
	* Task 1: Craft

### qe_yaot_spring_2023_day10:
* Name: No header for quest qe_yaot_spring_2023_day10
* Description: No description for quest qe_yaot_spring_2023_day10
* QuestLine: ql_event_yaot_spring_2023
* Type: Event
* EventId: event_season_yaoSpr_2023
* Goals:
	* Task 1: Complete 3 side missions

### qe_yaot_spring_2023_day11:
* Name: No header for quest qe_yaot_spring_2023_day11
* Description: No description for quest qe_yaot_spring_2023_day11
* QuestLine: ql_event_yaot_spring_2023
* Type: Event
* EventId: event_season_yaoSpr_2023
* Goals:
	* Task 1: 750 Mined

### qe_yaot_spring_2023_day12:
* Name: No header for quest qe_yaot_spring_2023_day12
* Description: No description for quest qe_yaot_spring_2023_day12
* QuestLine: ql_event_yaot_spring_2023
* Type: Event
* EventId: event_season_yaoSpr_2023
* Goals:
	* Task 1: GainItem

### qe_yaot_spring_2023_day13:
* Name: No header for quest qe_yaot_spring_2023_day13
* Description: No description for quest qe_yaot_spring_2023_day13
* QuestLine: ql_event_yaot_spring_2023
* Type: Event
* EventId: event_season_yaoSpr_2023
* Goals:
	* Task 1: UpgradeOfficer

### qe_yaot_spring_2023_day14:
* Name: No header for quest qe_yaot_spring_2023_day14
* Description: No description for quest qe_yaot_spring_2023_day14
* QuestLine: ql_event_yaot_spring_2023
* Type: Event
* EventId: event_season_yaoSpr_2023
* Goals:
	* Task 1: Complete mission 'Tanochet (Event)'

## QL_EVENT_AMASUM_2023_T1
### qe_amaSum_2023_day1_t1:
* Name: No header for quest qe_amaSum_2023_day1_t1
* Description: No description for quest qe_amaSum_2023_day1_t1
* QuestLine: ql_event_amaSum_2023_t1
* Type: Event
* EventId: event_season_amaSum_2023_t1
* Goals:
	* Task 1: Craft

### qe_amaSum_2023_day2_t1:
* Name: No header for quest qe_amaSum_2023_day2_t1
* Description: No description for quest qe_amaSum_2023_day2_t1
* QuestLine: ql_event_amaSum_2023_t1
* Type: Event
* EventId: event_season_amaSum_2023_t1
* Goals:
	* Task 1: Complete 3 side missions

### qe_amaSum_2023_day3_t1:
* Name: No header for quest qe_amaSum_2023_day3_t1
* Description: No description for quest qe_amaSum_2023_day3_t1
* QuestLine: ql_event_amaSum_2023_t1
* Type: Event
* EventId: event_season_amaSum_2023_t1
* Goals:
	* Task 1: UpgradeOfficer

### qe_amaSum_2023_day4_t1:
* Name: No header for quest qe_amaSum_2023_day4_t1
* Description: No description for quest qe_amaSum_2023_day4_t1
* QuestLine: ql_event_amaSum_2023_t1
* Type: Event
* EventId: event_season_amaSum_2023_t1
* Goals:
	* Task 1: Complete 3 side missions

### qe_amaSum_2023_day5_t1:
* Name: No header for quest qe_amaSum_2023_day5_t1
* Description: No description for quest qe_amaSum_2023_day5_t1
* QuestLine: ql_event_amaSum_2023_t1
* Type: Event
* EventId: event_season_amaSum_2023_t1
* Goals:
	* Task 1: Craft

### qe_amaSum_2023_day6_t1:
* Name: No header for quest qe_amaSum_2023_day6_t1
* Description: No description for quest qe_amaSum_2023_day6_t1
* QuestLine: ql_event_amaSum_2023_t1
* Type: Event
* EventId: event_season_amaSum_2023_t1
* Goals:
	* Task 1: Complete 3 side missions

### qe_amaSum_2023_day7_t1:
* Name: No header for quest qe_amaSum_2023_day7_t1
* Description: No description for quest qe_amaSum_2023_day7_t1
* QuestLine: ql_event_amaSum_2023_t1
* Type: Event
* EventId: event_season_amaSum_2023_t1
* Goals:
	* Task 1: GainItem

### qe_amaSum_2023_day8_t1:
* Name: No header for quest qe_amaSum_2023_day8_t1
* Description: No description for quest qe_amaSum_2023_day8_t1
* QuestLine: ql_event_amaSum_2023_t1
* Type: Event
* EventId: event_season_amaSum_2023_t1
* Goals:
	* Task 1: Complete 3 side missions

### qe_amaSum_2023_day9_t1:
* Name: No header for quest qe_amaSum_2023_day9_t1
* Description: No description for quest qe_amaSum_2023_day9_t1
* QuestLine: ql_event_amaSum_2023_t1
* Type: Event
* EventId: event_season_amaSum_2023_t1
* Goals:
	* Task 1: Craft

### qe_amaSum_2023_day10_t1:
* Name: No header for quest qe_amaSum_2023_day10_t1
* Description: No description for quest qe_amaSum_2023_day10_t1
* QuestLine: ql_event_amaSum_2023_t1
* Type: Event
* EventId: event_season_amaSum_2023_t1
* Goals:
	* Task 1: Complete 3 side missions

### qe_amaSum_2023_day11_t1:
* Name: No header for quest qe_amaSum_2023_day11_t1
* Description: No description for quest qe_amaSum_2023_day11_t1
* QuestLine: ql_event_amaSum_2023_t1
* Type: Event
* EventId: event_season_amaSum_2023_t1
* Goals:
	* Task 1: UpgradeOfficer

### qe_amaSum_2023_day12_t1:
* Name: No header for quest qe_amaSum_2023_day12_t1
* Description: No description for quest qe_amaSum_2023_day12_t1
* QuestLine: ql_event_amaSum_2023_t1
* Type: Event
* EventId: event_season_amaSum_2023_t1
* Goals:
	* Task 1: Complete 3 side missions

### qe_amaSum_2023_day13_t1:
* Name: No header for quest qe_amaSum_2023_day13_t1
* Description: No description for quest qe_amaSum_2023_day13_t1
* QuestLine: ql_event_amaSum_2023_t1
* Type: Event
* EventId: event_season_amaSum_2023_t1
* Goals:
	* Task 1: Craft

### qe_amaSum_2023_day14_t1:
* Name: No header for quest qe_amaSum_2023_day14_t1
* Description: No description for quest qe_amaSum_2023_day14_t1
* QuestLine: ql_event_amaSum_2023_t1
* Type: Event
* EventId: event_season_amaSum_2023_t1
* Goals:
	* Task 1: GainItem

### qe_amaSum_2023_day15_t1:
* Name: No header for quest qe_amaSum_2023_day15_t1
* Description: No description for quest qe_amaSum_2023_day15_t1
* QuestLine: ql_event_amaSum_2023_t1
* Type: Event
* EventId: event_season_amaSum_2023_t1
* Goals:
	* Task 1: Complete mission 'event_01_StationDefense'

## QL_EVENT_AMASUM_2023_T2
### qe_amaSum_2023_day1_t2:
* Name: No header for quest qe_amaSum_2023_day1_t2
* Description: No description for quest qe_amaSum_2023_day1_t2
* QuestLine: ql_event_amaSum_2023_t2
* Type: Event
* EventId: event_season_amaSum_2023_t2
* Goals:
	* Task 1: Craft

### qe_amaSum_2023_day2_t2:
* Name: No header for quest qe_amaSum_2023_day2_t2
* Description: No description for quest qe_amaSum_2023_day2_t2
* QuestLine: ql_event_amaSum_2023_t2
* Type: Event
* EventId: event_season_amaSum_2023_t2
* Goals:
	* Task 1: Complete 3 side missions

### qe_amaSum_2023_day3_t2:
* Name: No header for quest qe_amaSum_2023_day3_t2
* Description: No description for quest qe_amaSum_2023_day3_t2
* QuestLine: ql_event_amaSum_2023_t2
* Type: Event
* EventId: event_season_amaSum_2023_t2
* Goals:
	* Task 1: UpgradeOfficer

### qe_amaSum_2023_day4_t2:
* Name: No header for quest qe_amaSum_2023_day4_t2
* Description: No description for quest qe_amaSum_2023_day4_t2
* QuestLine: ql_event_amaSum_2023_t2
* Type: Event
* EventId: event_season_amaSum_2023_t2
* Goals:
	* Task 1: 5 Faction_T2up

### qe_amaSum_2023_day5_t2:
* Name: No header for quest qe_amaSum_2023_day5_t2
* Description: No description for quest qe_amaSum_2023_day5_t2
* QuestLine: ql_event_amaSum_2023_t2
* Type: Event
* EventId: event_season_amaSum_2023_t2
* Goals:
	* Task 1: Craft

### qe_amaSum_2023_day6_t2:
* Name: No header for quest qe_amaSum_2023_day6_t2
* Description: No description for quest qe_amaSum_2023_day6_t2
* QuestLine: ql_event_amaSum_2023_t2
* Type: Event
* EventId: event_season_amaSum_2023_t2
* Goals:
	* Task 1: Complete 3 side missions

### qe_amaSum_2023_day7_t2:
* Name: No header for quest qe_amaSum_2023_day7_t2
* Description: No description for quest qe_amaSum_2023_day7_t2
* QuestLine: ql_event_amaSum_2023_t2
* Type: Event
* EventId: event_season_amaSum_2023_t2
* Goals:
	* Task 1: GainItem

### qe_amaSum_2023_day8_t2:
* Name: No header for quest qe_amaSum_2023_day8_t2
* Description: No description for quest qe_amaSum_2023_day8_t2
* QuestLine: ql_event_amaSum_2023_t2
* Type: Event
* EventId: event_season_amaSum_2023_t2
* Goals:
	* Task 1: Complete side mission

### qe_amaSum_2023_day9_t2:
* Name: No header for quest qe_amaSum_2023_day9_t2
* Description: No description for quest qe_amaSum_2023_day9_t2
* QuestLine: ql_event_amaSum_2023_t2
* Type: Event
* EventId: event_season_amaSum_2023_t2
* Goals:
	* Task 1: Craft

### qe_amaSum_2023_day10_t2:
* Name: No header for quest qe_amaSum_2023_day10_t2
* Description: No description for quest qe_amaSum_2023_day10_t2
* QuestLine: ql_event_amaSum_2023_t2
* Type: Event
* EventId: event_season_amaSum_2023_t2
* Goals:
	* Task 1: 5 Faction_T2up

### qe_amaSum_2023_day11_t2:
* Name: No header for quest qe_amaSum_2023_day11_t2
* Description: No description for quest qe_amaSum_2023_day11_t2
* QuestLine: ql_event_amaSum_2023_t2
* Type: Event
* EventId: event_season_amaSum_2023_t2
* Goals:
	* Task 1: UpgradeOfficer

### qe_amaSum_2023_day12_t2:
* Name: No header for quest qe_amaSum_2023_day12_t2
* Description: No description for quest qe_amaSum_2023_day12_t2
* QuestLine: ql_event_amaSum_2023_t2
* Type: Event
* EventId: event_season_amaSum_2023_t2
* Goals:
	* Task 1: Complete side mission

### qe_amaSum_2023_day13_t2:
* Name: No header for quest qe_amaSum_2023_day13_t2
* Description: No description for quest qe_amaSum_2023_day13_t2
* QuestLine: ql_event_amaSum_2023_t2
* Type: Event
* EventId: event_season_amaSum_2023_t2
* Goals:
	* Task 1: Craft

### qe_amaSum_2023_day14_t2:
* Name: No header for quest qe_amaSum_2023_day14_t2
* Description: No description for quest qe_amaSum_2023_day14_t2
* QuestLine: ql_event_amaSum_2023_t2
* Type: Event
* EventId: event_season_amaSum_2023_t2
* Goals:
	* Task 1: GainItem

### qe_amaSum_2023_day15_t2:
* Name: No header for quest qe_amaSum_2023_day15_t2
* Description: No description for quest qe_amaSum_2023_day15_t2
* QuestLine: ql_event_amaSum_2023_t2
* Type: Event
* EventId: event_season_amaSum_2023_t2
* Goals:
	* Task 1: Complete mission 'event_02_StationDefense'

## QL_EVENT_AMASUM_2023_T3
### qe_amaSum_2023_day1_t3:
* Name: No header for quest qe_amaSum_2023_day1_t3
* Description: No description for quest qe_amaSum_2023_day1_t3
* QuestLine: ql_event_amaSum_2023_t3
* Type: Event
* EventId: event_season_amaSum_2023_t3
* Goals:
	* Task 1: Craft

### qe_amaSum_2023_day2_t3:
* Name: No header for quest qe_amaSum_2023_day2_t3
* Description: No description for quest qe_amaSum_2023_day2_t3
* QuestLine: ql_event_amaSum_2023_t3
* Type: Event
* EventId: event_season_amaSum_2023_t3
* Goals:
	* Task 1: Complete 3 side missions

### qe_amaSum_2023_day3_t3:
* Name: No header for quest qe_amaSum_2023_day3_t3
* Description: No description for quest qe_amaSum_2023_day3_t3
* QuestLine: ql_event_amaSum_2023_t3
* Type: Event
* EventId: event_season_amaSum_2023_t3
* Goals:
	* Task 1: UpgradeOfficer

### qe_amaSum_2023_day4_t3:
* Name: No header for quest qe_amaSum_2023_day4_t3
* Description: No description for quest qe_amaSum_2023_day4_t3
* QuestLine: ql_event_amaSum_2023_t3
* Type: Event
* EventId: event_season_amaSum_2023_t3
* Goals:
	* Task 1: 5 Faction_T3up

### qe_amaSum_2023_day5_t3:
* Name: No header for quest qe_amaSum_2023_day5_t3
* Description: No description for quest qe_amaSum_2023_day5_t3
* QuestLine: ql_event_amaSum_2023_t3
* Type: Event
* EventId: event_season_amaSum_2023_t3
* Goals:
	* Task 1: GainItem

### qe_amaSum_2023_day6_t3:
* Name: No header for quest qe_amaSum_2023_day6_t3
* Description: No description for quest qe_amaSum_2023_day6_t3
* QuestLine: ql_event_amaSum_2023_t3
* Type: Event
* EventId: event_season_amaSum_2023_t3
* Goals:
	* Task 1: Complete 3 side missions

### qe_amaSum_2023_day7_t3:
* Name: No header for quest qe_amaSum_2023_day7_t3
* Description: No description for quest qe_amaSum_2023_day7_t3
* QuestLine: ql_event_amaSum_2023_t3
* Type: Event
* EventId: event_season_amaSum_2023_t3
* Goals:
	* Task 1: GainItem

### qe_amaSum_2023_day8_t3:
* Name: No header for quest qe_amaSum_2023_day8_t3
* Description: No description for quest qe_amaSum_2023_day8_t3
* QuestLine: ql_event_amaSum_2023_t3
* Type: Event
* EventId: event_season_amaSum_2023_t3
* Goals:
	* Task 1: Complete 3 side missions

### qe_amaSum_2023_day9_t3:
* Name: No header for quest qe_amaSum_2023_day9_t3
* Description: No description for quest qe_amaSum_2023_day9_t3
* QuestLine: ql_event_amaSum_2023_t3
* Type: Event
* EventId: event_season_amaSum_2023_t3
* Goals:
	* Task 1: Craft

### qe_amaSum_2023_day10_t3:
* Name: No header for quest qe_amaSum_2023_day10_t3
* Description: No description for quest qe_amaSum_2023_day10_t3
* QuestLine: ql_event_amaSum_2023_t3
* Type: Event
* EventId: event_season_amaSum_2023_t3
* Goals:
	* Task 1: 5 Faction_T3up

### qe_amaSum_2023_day11_t3:
* Name: No header for quest qe_amaSum_2023_day11_t3
* Description: No description for quest qe_amaSum_2023_day11_t3
* QuestLine: ql_event_amaSum_2023_t3
* Type: Event
* EventId: event_season_amaSum_2023_t3
* Goals:
	* Task 1: UpgradeOfficer

### qe_amaSum_2023_day12_t3:
* Name: No header for quest qe_amaSum_2023_day12_t3
* Description: No description for quest qe_amaSum_2023_day12_t3
* QuestLine: ql_event_amaSum_2023_t3
* Type: Event
* EventId: event_season_amaSum_2023_t3
* Goals:
	* Task 1: Complete 3 side missions

### qe_amaSum_2023_day13_t3:
* Name: No header for quest qe_amaSum_2023_day13_t3
* Description: No description for quest qe_amaSum_2023_day13_t3
* QuestLine: ql_event_amaSum_2023_t3
* Type: Event
* EventId: event_season_amaSum_2023_t3
* Goals:
	* Task 1: GainItem

### qe_amaSum_2023_day14_t3:
* Name: No header for quest qe_amaSum_2023_day14_t3
* Description: No description for quest qe_amaSum_2023_day14_t3
* QuestLine: ql_event_amaSum_2023_t3
* Type: Event
* EventId: event_season_amaSum_2023_t3
* Goals:
	* Task 1: GainItem

### qe_amaSum_2023_day15_t3:
* Name: No header for quest qe_amaSum_2023_day15_t3
* Description: No description for quest qe_amaSum_2023_day15_t3
* QuestLine: ql_event_amaSum_2023_t3
* Type: Event
* EventId: event_season_amaSum_2023_t3
* Goals:
	* Task 1: Complete mission 'event_03_StationDefense'

## QL_EVENT_AMASUM_2023_T4
### qe_amaSum_2023_day1_t4:
* Name: No header for quest qe_amaSum_2023_day1_t4
* Description: No description for quest qe_amaSum_2023_day1_t4
* QuestLine: ql_event_amaSum_2023_t4
* Type: Event
* EventId: event_season_amaSum_2023_t4
* Goals:
	* Task 1: Craft

### qe_amaSum_2023_day2_t4:
* Name: No header for quest qe_amaSum_2023_day2_t4
* Description: No description for quest qe_amaSum_2023_day2_t4
* QuestLine: ql_event_amaSum_2023_t4
* Type: Event
* EventId: event_season_amaSum_2023_t4
* Goals:
	* Task 1: Complete 3 side missions

### qe_amaSum_2023_day3_t4:
* Name: No header for quest qe_amaSum_2023_day3_t4
* Description: No description for quest qe_amaSum_2023_day3_t4
* QuestLine: ql_event_amaSum_2023_t4
* Type: Event
* EventId: event_season_amaSum_2023_t4
* Goals:
	* Task 1: UpgradeOfficer

### qe_amaSum_2023_day4_t4:
* Name: No header for quest qe_amaSum_2023_day4_t4
* Description: No description for quest qe_amaSum_2023_day4_t4
* QuestLine: ql_event_amaSum_2023_t4
* Type: Event
* EventId: event_season_amaSum_2023_t4
* Goals:
	* Task 1: 5 Faction_Amassari_T4up

### qe_amaSum_2023_day5_t4:
* Name: No header for quest qe_amaSum_2023_day5_t4
* Description: No description for quest qe_amaSum_2023_day5_t4
* QuestLine: ql_event_amaSum_2023_t4
* Type: Event
* EventId: event_season_amaSum_2023_t4
* Goals:
	* Task 1: GainItem

### qe_amaSum_2023_day6_t4:
* Name: No header for quest qe_amaSum_2023_day6_t4
* Description: No description for quest qe_amaSum_2023_day6_t4
* QuestLine: ql_event_amaSum_2023_t4
* Type: Event
* EventId: event_season_amaSum_2023_t4
* Goals:
	* Task 1: Complete 3 side missions

### qe_amaSum_2023_day7_t4:
* Name: No header for quest qe_amaSum_2023_day7_t4
* Description: No description for quest qe_amaSum_2023_day7_t4
* QuestLine: ql_event_amaSum_2023_t4
* Type: Event
* EventId: event_season_amaSum_2023_t4
* Goals:
	* Task 1: GainItem

### qe_amaSum_2023_day8_t4:
* Name: No header for quest qe_amaSum_2023_day8_t4
* Description: No description for quest qe_amaSum_2023_day8_t4
* QuestLine: ql_event_amaSum_2023_t4
* Type: Event
* EventId: event_season_amaSum_2023_t4
* Goals:
	* Task 1: Complete 5 side missions

### qe_amaSum_2023_day9_t4:
* Name: No header for quest qe_amaSum_2023_day9_t4
* Description: No description for quest qe_amaSum_2023_day9_t4
* QuestLine: ql_event_amaSum_2023_t4
* Type: Event
* EventId: event_season_amaSum_2023_t4
* Goals:
	* Task 1: Craft

### qe_amaSum_2023_day10_t4:
* Name: No header for quest qe_amaSum_2023_day10_t4
* Description: No description for quest qe_amaSum_2023_day10_t4
* QuestLine: ql_event_amaSum_2023_t4
* Type: Event
* EventId: event_season_amaSum_2023_t4
* Goals:
	* Task 1: 5 Faction_Amassari_T4up

### qe_amaSum_2023_day11_t4:
* Name: No header for quest qe_amaSum_2023_day11_t4
* Description: No description for quest qe_amaSum_2023_day11_t4
* QuestLine: ql_event_amaSum_2023_t4
* Type: Event
* EventId: event_season_amaSum_2023_t4
* Goals:
	* Task 1: UpgradeOfficer

### qe_amaSum_2023_day12_t4:
* Name: No header for quest qe_amaSum_2023_day12_t4
* Description: No description for quest qe_amaSum_2023_day12_t4
* QuestLine: ql_event_amaSum_2023_t4
* Type: Event
* EventId: event_season_amaSum_2023_t4
* Goals:
	* Task 1: Complete 5 side missions

### qe_amaSum_2023_day13_t4:
* Name: No header for quest qe_amaSum_2023_day13_t4
* Description: No description for quest qe_amaSum_2023_day13_t4
* QuestLine: ql_event_amaSum_2023_t4
* Type: Event
* EventId: event_season_amaSum_2023_t4
* Goals:
	* Task 1: GainItem

### qe_amaSum_2023_day14_t4:
* Name: No header for quest qe_amaSum_2023_day14_t4
* Description: No description for quest qe_amaSum_2023_day14_t4
* QuestLine: ql_event_amaSum_2023_t4
* Type: Event
* EventId: event_season_amaSum_2023_t4
* Goals:
	* Task 1: GainItem

### qe_amaSum_2023_day15_t4:
* Name: No header for quest qe_amaSum_2023_day15_t4
* Description: No description for quest qe_amaSum_2023_day15_t4
* QuestLine: ql_event_amaSum_2023_t4
* Type: Event
* EventId: event_season_amaSum_2023_t4
* Goals:
	* Task 1: Complete mission 'event_04_StationDefense'

## QL_EVENT_IYAFAL_2023_T1
### qe_iyaFal_2023_day01_t1:
* Name: No header for quest qe_iyaFal_2023_day01_t1
* Description: No description for quest qe_iyaFal_2023_day01_t1
* QuestLine: ql_event_iyaFal_2023_t1
* Type: Event
* EventId: event_season_iyaFal_2023_t1
* Goals:
	* Task 1: 5 T1up

### qe_iyaFal_2023_day02_t1:
* Name: No header for quest qe_iyaFal_2023_day02_t1
* Description: No description for quest qe_iyaFal_2023_day02_t1
* QuestLine: ql_event_iyaFal_2023_t1
* Type: Event
* EventId: event_season_iyaFal_2023_t1
* Goals:
	* Task 1: GainItem

### qe_iyaFal_2023_day03_t1:
* Name: No header for quest qe_iyaFal_2023_day03_t1
* Description: No description for quest qe_iyaFal_2023_day03_t1
* QuestLine: ql_event_iyaFal_2023_t1
* Type: Event
* EventId: event_season_iyaFal_2023_t1
* Goals:
	* Task 1: Craft

### qe_iyaFal_2023_day04_t1:
* Name: No header for quest qe_iyaFal_2023_day04_t1
* Description: No description for quest qe_iyaFal_2023_day04_t1
* QuestLine: ql_event_iyaFal_2023_t1
* Type: Event
* EventId: event_season_iyaFal_2023_t1
* MailsOnCompletion: m_iyaFal_day4_log
* Goals:
	* Task 1: Complete 3 side missions

### qe_iyaFal_2023_day05_t1:
* Name: No header for quest qe_iyaFal_2023_day05_t1
* Description: No description for quest qe_iyaFal_2023_day05_t1
* QuestLine: ql_event_iyaFal_2023_t1
* Type: Event
* EventId: event_season_iyaFal_2023_t1
* Goals:
	* Task 1: Complete 3 side missions

### qe_iyaFal_2023_day06_t1:
* Name: No header for quest qe_iyaFal_2023_day06_t1
* Description: No description for quest qe_iyaFal_2023_day06_t1
* QuestLine: ql_event_iyaFal_2023_t1
* Type: Event
* EventId: event_season_iyaFal_2023_t1
* Goals:
	* Task 1: GainItem

### qe_iyaFal_2023_day07_t1:
* Name: No header for quest qe_iyaFal_2023_day07_t1
* Description: No description for quest qe_iyaFal_2023_day07_t1
* QuestLine: ql_event_iyaFal_2023_t1
* Type: Event
* EventId: event_season_iyaFal_2023_t1
* Goals:
	* Task 1: UpgradeOfficer

### qe_iyaFal_2023_day08_t1:
* Name: No header for quest qe_iyaFal_2023_day08_t1
* Description: No description for quest qe_iyaFal_2023_day08_t1
* QuestLine: ql_event_iyaFal_2023_t1
* Type: Event
* EventId: event_season_iyaFal_2023_t1
* MailsOnCompletion: m_iyaFal_day8_log
* Goals:
	* Task 1: GainItem

### qe_iyaFal_2023_day09_t1:
* Name: No header for quest qe_iyaFal_2023_day09_t1
* Description: No description for quest qe_iyaFal_2023_day09_t1
* QuestLine: ql_event_iyaFal_2023_t1
* Type: Event
* EventId: event_season_iyaFal_2023_t1
* Goals:
	* Task 1: 5 T1up

### qe_iyaFal_2023_day10_t1:
* Name: No header for quest qe_iyaFal_2023_day10_t1
* Description: No description for quest qe_iyaFal_2023_day10_t1
* QuestLine: ql_event_iyaFal_2023_t1
* Type: Event
* EventId: event_season_iyaFal_2023_t1
* Goals:
	* Task 1: GainItem

### qe_iyaFal_2023_day11_t1:
* Name: No header for quest qe_iyaFal_2023_day11_t1
* Description: No description for quest qe_iyaFal_2023_day11_t1
* QuestLine: ql_event_iyaFal_2023_t1
* Type: Event
* EventId: event_season_iyaFal_2023_t1
* Goals:
	* Task 1: Craft

### qe_iyaFal_2023_day12_t1:
* Name: No header for quest qe_iyaFal_2023_day12_t1
* Description: No description for quest qe_iyaFal_2023_day12_t1
* QuestLine: ql_event_iyaFal_2023_t1
* Type: Event
* EventId: event_season_iyaFal_2023_t1
* MailsOnCompletion: m_iyaFal_day12_log
* Goals:
	* Task 1: Complete side mission

### qe_iyaFal_2023_day13_t1:
* Name: No header for quest qe_iyaFal_2023_day13_t1
* Description: No description for quest qe_iyaFal_2023_day13_t1
* QuestLine: ql_event_iyaFal_2023_t1
* Type: Event
* EventId: event_season_iyaFal_2023_t1
* Goals:
	* Task 1: GainItem

### qe_iyaFal_2023_day14_t1:
* Name: No header for quest qe_iyaFal_2023_day14_t1
* Description: No description for quest qe_iyaFal_2023_day14_t1
* QuestLine: ql_event_iyaFal_2023_t1
* Type: Event
* EventId: event_season_iyaFal_2023_t1
* Goals:
	* Task 1: GainItem

### qe_iyaFal_2023_day15_t1:
* Name: No header for quest qe_iyaFal_2023_day15_t1
* Description: No description for quest qe_iyaFal_2023_day15_t1
* QuestLine: ql_event_iyaFal_2023_t1
* Type: Event
* EventId: event_season_iyaFal_2023_t1
* Goals:
	* Task 1: Complete mission 'Trader's Bargain T1'

## QL_EVENT_IYAFAL_2023_EPILOG_T1
### qe_iyaFal_2023_epi01_t1:
* Name: No header for quest qe_iyaFal_2023_epi01_t1
* Description: No description for quest qe_iyaFal_2023_epi01_t1
* QuestLine: ql_event_iyaFal_2023_epilog_t1
* Type: Event
* EventId: event_season_iyaFal_2023_t1
* Goals:
	* Task 1: GainItem

### qe_iyaFal_2023_epi02_t1:
* Name: No header for quest qe_iyaFal_2023_epi02_t1
* Description: No description for quest qe_iyaFal_2023_epi02_t1
* QuestLine: ql_event_iyaFal_2023_epilog_t1
* Type: Event
* EventId: event_season_iyaFal_2023_t1
* Goals:
	* Task 1: 10 ShipsDestroyedProgenitorT1_ShipsDestroyedProgenitorT2_ShipsDestroyedProgenitorT3_ShipsDestroyedProgenitorT4

### qe_iyaFal_2023_epi03_t1:
* Name: No header for quest qe_iyaFal_2023_epi03_t1
* Description: No description for quest qe_iyaFal_2023_epi03_t1
* QuestLine: ql_event_iyaFal_2023_epilog_t1
* Type: Event
* EventId: event_season_iyaFal_2023_t1
* Goals:
	* Task 1: GainItem

### qe_iyaFal_2023_epi04_t1:
* Name: No header for quest qe_iyaFal_2023_epi04_t1
* Description: No description for quest qe_iyaFal_2023_epi04_t1
* QuestLine: ql_event_iyaFal_2023_epilog_t1
* Type: Event
* EventId: event_season_iyaFal_2023_t1
* Goals:
	* Task 1: UpgradeOfficer

### qe_iyaFal_2023_epi05_t1:
* Name: No header for quest qe_iyaFal_2023_epi05_t1
* Description: No description for quest qe_iyaFal_2023_epi05_t1
* QuestLine: ql_event_iyaFal_2023_epilog_t1
* Type: Event
* EventId: event_season_iyaFal_2023_t1
* Goals:
	* Task 1: Complete side mission

## QL_EVENT_IYAFAL_2023_T2
### qe_iyaFal_2023_day01_t2:
* Name: No header for quest qe_iyaFal_2023_day01_t2
* Description: No description for quest qe_iyaFal_2023_day01_t2
* QuestLine: ql_event_iyaFal_2023_t2
* Type: Event
* EventId: event_season_iyaFal_2023_t2
* Goals:
	* Task 1: 5 Faction_Tr1_T2up

### qe_iyaFal_2023_day02_t2:
* Name: No header for quest qe_iyaFal_2023_day02_t2
* Description: No description for quest qe_iyaFal_2023_day02_t2
* QuestLine: ql_event_iyaFal_2023_t2
* Type: Event
* EventId: event_season_iyaFal_2023_t2
* Goals:
	* Task 1: GainItem

### qe_iyaFal_2023_day03_t2:
* Name: No header for quest qe_iyaFal_2023_day03_t2
* Description: No description for quest qe_iyaFal_2023_day03_t2
* QuestLine: ql_event_iyaFal_2023_t2
* Type: Event
* EventId: event_season_iyaFal_2023_t2
* Goals:
	* Task 1: Craft

### qe_iyaFal_2023_day04_t2:
* Name: No header for quest qe_iyaFal_2023_day04_t2
* Description: No description for quest qe_iyaFal_2023_day04_t2
* QuestLine: ql_event_iyaFal_2023_t2
* Type: Event
* EventId: event_season_iyaFal_2023_t2
* MailsOnCompletion: m_iyaFal_day4_log
* Goals:
	* Task 1: Complete 3 side missions

### qe_iyaFal_2023_day05_t2:
* Name: No header for quest qe_iyaFal_2023_day05_t2
* Description: No description for quest qe_iyaFal_2023_day05_t2
* QuestLine: ql_event_iyaFal_2023_t2
* Type: Event
* EventId: event_season_iyaFal_2023_t2
* Goals:
	* Task 1: Complete 3 side missions

### qe_iyaFal_2023_day06_t2:
* Name: No header for quest qe_iyaFal_2023_day06_t2
* Description: No description for quest qe_iyaFal_2023_day06_t2
* QuestLine: ql_event_iyaFal_2023_t2
* Type: Event
* EventId: event_season_iyaFal_2023_t2
* Goals:
	* Task 1: GainItem

### qe_iyaFal_2023_day07_t2:
* Name: No header for quest qe_iyaFal_2023_day07_t2
* Description: No description for quest qe_iyaFal_2023_day07_t2
* QuestLine: ql_event_iyaFal_2023_t2
* Type: Event
* EventId: event_season_iyaFal_2023_t2
* Goals:
	* Task 1: UpgradeOfficer

### qe_iyaFal_2023_day08_t2:
* Name: No header for quest qe_iyaFal_2023_day08_t2
* Description: No description for quest qe_iyaFal_2023_day08_t2
* QuestLine: ql_event_iyaFal_2023_t2
* Type: Event
* EventId: event_season_iyaFal_2023_t2
* MailsOnCompletion: m_iyaFal_day8_log
* Goals:
	* Task 1: GainItem

### qe_iyaFal_2023_day09_t2:
* Name: No header for quest qe_iyaFal_2023_day09_t2
* Description: No description for quest qe_iyaFal_2023_day09_t2
* QuestLine: ql_event_iyaFal_2023_t2
* Type: Event
* EventId: event_season_iyaFal_2023_t2
* Goals:
	* Task 1: 5 Faction_Tr1_T2up

### qe_iyaFal_2023_day10_t2:
* Name: No header for quest qe_iyaFal_2023_day10_t2
* Description: No description for quest qe_iyaFal_2023_day10_t2
* QuestLine: ql_event_iyaFal_2023_t2
* Type: Event
* EventId: event_season_iyaFal_2023_t2
* Goals:
	* Task 1: GainItem

### qe_iyaFal_2023_day11_t2:
* Name: No header for quest qe_iyaFal_2023_day11_t2
* Description: No description for quest qe_iyaFal_2023_day11_t2
* QuestLine: ql_event_iyaFal_2023_t2
* Type: Event
* EventId: event_season_iyaFal_2023_t2
* Goals:
	* Task 1: GainItem

### qe_iyaFal_2023_day12_t2:
* Name: No header for quest qe_iyaFal_2023_day12_t2
* Description: No description for quest qe_iyaFal_2023_day12_t2
* QuestLine: ql_event_iyaFal_2023_t2
* Type: Event
* EventId: event_season_iyaFal_2023_t2
* MailsOnCompletion: m_iyaFal_day12_log
* Goals:
	* Task 1: Complete side mission

### qe_iyaFal_2023_day13_t2:
* Name: No header for quest qe_iyaFal_2023_day13_t2
* Description: No description for quest qe_iyaFal_2023_day13_t2
* QuestLine: ql_event_iyaFal_2023_t2
* Type: Event
* EventId: event_season_iyaFal_2023_t2
* Goals:
	* Task 1: 135 RepTr1

### qe_iyaFal_2023_day14_t2:
* Name: No header for quest qe_iyaFal_2023_day14_t2
* Description: No description for quest qe_iyaFal_2023_day14_t2
* QuestLine: ql_event_iyaFal_2023_t2
* Type: Event
* EventId: event_season_iyaFal_2023_t2
* Goals:
	* Task 1: GainItem

### qe_iyaFal_2023_day15_t2:
* Name: No header for quest qe_iyaFal_2023_day15_t2
* Description: No description for quest qe_iyaFal_2023_day15_t2
* QuestLine: ql_event_iyaFal_2023_t2
* Type: Event
* EventId: event_season_iyaFal_2023_t2
* Goals:
	* Task 1: Complete mission 'Trader's Bargain T2'

## QL_EVENT_IYAFAL_2023_EPILOG_T2
### qe_iyaFal_2023_epi01_t2:
* Name: No header for quest qe_iyaFal_2023_epi01_t2
* Description: No description for quest qe_iyaFal_2023_epi01_t2
* QuestLine: ql_event_iyaFal_2023_epilog_t2
* Type: Event
* EventId: event_season_iyaFal_2023_t2
* Goals:
	* Task 1: GainItem

### qe_iyaFal_2023_epi02_t2:
* Name: No header for quest qe_iyaFal_2023_epi02_t2
* Description: No description for quest qe_iyaFal_2023_epi02_t2
* QuestLine: ql_event_iyaFal_2023_epilog_t2
* Type: Event
* EventId: event_season_iyaFal_2023_t2
* Goals:
	* Task 1: 10 ShipsDestroyedProgenitorT2_ShipsDestroyedProgenitorT3_ShipsDestroyedProgenitorT4

### qe_iyaFal_2023_epi03_t2:
* Name: No header for quest qe_iyaFal_2023_epi03_t2
* Description: No description for quest qe_iyaFal_2023_epi03_t2
* QuestLine: ql_event_iyaFal_2023_epilog_t2
* Type: Event
* EventId: event_season_iyaFal_2023_t2
* Goals:
	* Task 1: GainItem

### qe_iyaFal_2023_epi04_t2:
* Name: No header for quest qe_iyaFal_2023_epi04_t2
* Description: No description for quest qe_iyaFal_2023_epi04_t2
* QuestLine: ql_event_iyaFal_2023_epilog_t2
* Type: Event
* EventId: event_season_iyaFal_2023_t2
* Goals:
	* Task 1: UpgradeOfficer

### qe_iyaFal_2023_epi05_t2:
* Name: No header for quest qe_iyaFal_2023_epi05_t2
* Description: No description for quest qe_iyaFal_2023_epi05_t2
* QuestLine: ql_event_iyaFal_2023_epilog_t2
* Type: Event
* EventId: event_season_iyaFal_2023_t2
* Goals:
	* Task 1: Complete side mission

## QL_EVENT_IYAFAL_2023_T3
### qe_iyaFal_2023_day01_t3:
* Name: No header for quest qe_iyaFal_2023_day01_t3
* Description: No description for quest qe_iyaFal_2023_day01_t3
* QuestLine: ql_event_iyaFal_2023_t3
* Type: Event
* EventId: event_season_iyaFal_2023_t3
* Goals:
	* Task 1: 5 Faction_Tr1_T3up

### qe_iyaFal_2023_day02_t3:
* Name: No header for quest qe_iyaFal_2023_day02_t3
* Description: No description for quest qe_iyaFal_2023_day02_t3
* QuestLine: ql_event_iyaFal_2023_t3
* Type: Event
* EventId: event_season_iyaFal_2023_t3
* Goals:
	* Task 1: GainItem

### qe_iyaFal_2023_day03_t3:
* Name: No header for quest qe_iyaFal_2023_day03_t3
* Description: No description for quest qe_iyaFal_2023_day03_t3
* QuestLine: ql_event_iyaFal_2023_t3
* Type: Event
* EventId: event_season_iyaFal_2023_t3
* Goals:
	* Task 1: Craft

### qe_iyaFal_2023_day04_t3:
* Name: No header for quest qe_iyaFal_2023_day04_t3
* Description: No description for quest qe_iyaFal_2023_day04_t3
* QuestLine: ql_event_iyaFal_2023_t3
* Type: Event
* EventId: event_season_iyaFal_2023_t3
* MailsOnCompletion: m_iyaFal_day4_log
* Goals:
	* Task 1: Complete 3 side missions

### qe_iyaFal_2023_day05_t3:
* Name: No header for quest qe_iyaFal_2023_day05_t3
* Description: No description for quest qe_iyaFal_2023_day05_t3
* QuestLine: ql_event_iyaFal_2023_t3
* Type: Event
* EventId: event_season_iyaFal_2023_t3
* Goals:
	* Task 1: Complete 3 side missions

### qe_iyaFal_2023_day06_t3:
* Name: No header for quest qe_iyaFal_2023_day06_t3
* Description: No description for quest qe_iyaFal_2023_day06_t3
* QuestLine: ql_event_iyaFal_2023_t3
* Type: Event
* EventId: event_season_iyaFal_2023_t3
* Goals:
	* Task 1: GainItem

### qe_iyaFal_2023_day07_t3:
* Name: No header for quest qe_iyaFal_2023_day07_t3
* Description: No description for quest qe_iyaFal_2023_day07_t3
* QuestLine: ql_event_iyaFal_2023_t3
* Type: Event
* EventId: event_season_iyaFal_2023_t3
* Goals:
	* Task 1: UpgradeOfficer

### qe_iyaFal_2023_day08_t3:
* Name: No header for quest qe_iyaFal_2023_day08_t3
* Description: No description for quest qe_iyaFal_2023_day08_t3
* QuestLine: ql_event_iyaFal_2023_t3
* Type: Event
* EventId: event_season_iyaFal_2023_t3
* MailsOnCompletion: m_iyaFal_day8_log
* Goals:
	* Task 1: GainItem

### qe_iyaFal_2023_day09_t3:
* Name: No header for quest qe_iyaFal_2023_day09_t3
* Description: No description for quest qe_iyaFal_2023_day09_t3
* QuestLine: ql_event_iyaFal_2023_t3
* Type: Event
* EventId: event_season_iyaFal_2023_t3
* Goals:
	* Task 1: 5 Faction_Tr1_T3up

### qe_iyaFal_2023_day10_t3:
* Name: No header for quest qe_iyaFal_2023_day10_t3
* Description: No description for quest qe_iyaFal_2023_day10_t3
* QuestLine: ql_event_iyaFal_2023_t3
* Type: Event
* EventId: event_season_iyaFal_2023_t3
* Goals:
	* Task 1: GainItem

### qe_iyaFal_2023_day11_t3:
* Name: No header for quest qe_iyaFal_2023_day11_t3
* Description: No description for quest qe_iyaFal_2023_day11_t3
* QuestLine: ql_event_iyaFal_2023_t3
* Type: Event
* EventId: event_season_iyaFal_2023_t3
* Goals:
	* Task 1: GainItem

### qe_iyaFal_2023_day12_t3:
* Name: No header for quest qe_iyaFal_2023_day12_t3
* Description: No description for quest qe_iyaFal_2023_day12_t3
* QuestLine: ql_event_iyaFal_2023_t3
* Type: Event
* EventId: event_season_iyaFal_2023_t3
* MailsOnCompletion: m_iyaFal_day12_log
* Goals:
	* Task 1: Complete side mission

### qe_iyaFal_2023_day13_t3:
* Name: No header for quest qe_iyaFal_2023_day13_t3
* Description: No description for quest qe_iyaFal_2023_day13_t3
* QuestLine: ql_event_iyaFal_2023_t3
* Type: Event
* EventId: event_season_iyaFal_2023_t3
* Goals:
	* Task 1: 180 RepTr1

### qe_iyaFal_2023_day14_t3:
* Name: No header for quest qe_iyaFal_2023_day14_t3
* Description: No description for quest qe_iyaFal_2023_day14_t3
* QuestLine: ql_event_iyaFal_2023_t3
* Type: Event
* EventId: event_season_iyaFal_2023_t3
* Goals:
	* Task 1: GainItem

### qe_iyaFal_2023_day15_t3:
* Name: No header for quest qe_iyaFal_2023_day15_t3
* Description: No description for quest qe_iyaFal_2023_day15_t3
* QuestLine: ql_event_iyaFal_2023_t3
* Type: Event
* EventId: event_season_iyaFal_2023_t3
* Goals:
	* Task 1: Complete mission 'Trader's Bargain T3'

## QL_EVENT_IYAFAL_2023_EPILOG_T3
### qe_iyaFal_2023_epi01_t3:
* Name: No header for quest qe_iyaFal_2023_epi01_t3
* Description: No description for quest qe_iyaFal_2023_epi01_t3
* QuestLine: ql_event_iyaFal_2023_epilog_t3
* Type: Event
* EventId: event_season_iyaFal_2023_t3
* Goals:
	* Task 1: GainItem

### qe_iyaFal_2023_epi02_t3:
* Name: No header for quest qe_iyaFal_2023_epi02_t3
* Description: No description for quest qe_iyaFal_2023_epi02_t3
* QuestLine: ql_event_iyaFal_2023_epilog_t3
* Type: Event
* EventId: event_season_iyaFal_2023_t3
* Goals:
	* Task 1: 10 ShipsDestroyedProgenitorT3_ShipsDestroyedProgenitorT4

### qe_iyaFal_2023_epi03_t3:
* Name: No header for quest qe_iyaFal_2023_epi03_t3
* Description: No description for quest qe_iyaFal_2023_epi03_t3
* QuestLine: ql_event_iyaFal_2023_epilog_t3
* Type: Event
* EventId: event_season_iyaFal_2023_t3
* Goals:
	* Task 1: GainItem

### qe_iyaFal_2023_epi04_t3:
* Name: No header for quest qe_iyaFal_2023_epi04_t3
* Description: No description for quest qe_iyaFal_2023_epi04_t3
* QuestLine: ql_event_iyaFal_2023_epilog_t3
* Type: Event
* EventId: event_season_iyaFal_2023_t3
* Goals:
	* Task 1: UpgradeOfficer

### qe_iyaFal_2023_epi05_t3:
* Name: No header for quest qe_iyaFal_2023_epi05_t3
* Description: No description for quest qe_iyaFal_2023_epi05_t3
* QuestLine: ql_event_iyaFal_2023_epilog_t3
* Type: Event
* EventId: event_season_iyaFal_2023_t3
* Goals:
	* Task 1: Complete 3 side missions

## QL_EVENT_IYAFAL_2023_T4
### qe_iyaFal_2023_day01_t4:
* Name: No header for quest qe_iyaFal_2023_day01_t4
* Description: No description for quest qe_iyaFal_2023_day01_t4
* QuestLine: ql_event_iyaFal_2023_t4
* Type: Event
* EventId: event_season_iyaFal_2023_t4
* Goals:
	* Task 1: 5 Faction_T4up

### qe_iyaFal_2023_day02_t4:
* Name: No header for quest qe_iyaFal_2023_day02_t4
* Description: No description for quest qe_iyaFal_2023_day02_t4
* QuestLine: ql_event_iyaFal_2023_t4
* Type: Event
* EventId: event_season_iyaFal_2023_t4
* Goals:
	* Task 1: GainItem

### qe_iyaFal_2023_day03_t4:
* Name: No header for quest qe_iyaFal_2023_day03_t4
* Description: No description for quest qe_iyaFal_2023_day03_t4
* QuestLine: ql_event_iyaFal_2023_t4
* Type: Event
* EventId: event_season_iyaFal_2023_t4
* Goals:
	* Task 1: Craft

### qe_iyaFal_2023_day04_t4:
* Name: No header for quest qe_iyaFal_2023_day04_t4
* Description: No description for quest qe_iyaFal_2023_day04_t4
* QuestLine: ql_event_iyaFal_2023_t4
* Type: Event
* EventId: event_season_iyaFal_2023_t4
* MailsOnCompletion: m_iyaFal_day4_log
* Goals:
	* Task 1: Complete 3 side missions

### qe_iyaFal_2023_day05_t4:
* Name: No header for quest qe_iyaFal_2023_day05_t4
* Description: No description for quest qe_iyaFal_2023_day05_t4
* QuestLine: ql_event_iyaFal_2023_t4
* Type: Event
* EventId: event_season_iyaFal_2023_t4
* Goals:
	* Task 1: Complete 3 side missions

### qe_iyaFal_2023_day06_t4:
* Name: No header for quest qe_iyaFal_2023_day06_t4
* Description: No description for quest qe_iyaFal_2023_day06_t4
* QuestLine: ql_event_iyaFal_2023_t4
* Type: Event
* EventId: event_season_iyaFal_2023_t4
* Goals:
	* Task 1: GainItem

### qe_iyaFal_2023_day07_t4:
* Name: No header for quest qe_iyaFal_2023_day07_t4
* Description: No description for quest qe_iyaFal_2023_day07_t4
* QuestLine: ql_event_iyaFal_2023_t4
* Type: Event
* EventId: event_season_iyaFal_2023_t4
* Goals:
	* Task 1: UpgradeOfficer

### qe_iyaFal_2023_day08_t4:
* Name: No header for quest qe_iyaFal_2023_day08_t4
* Description: No description for quest qe_iyaFal_2023_day08_t4
* QuestLine: ql_event_iyaFal_2023_t4
* Type: Event
* EventId: event_season_iyaFal_2023_t4
* MailsOnCompletion: m_iyaFal_day8_log
* Goals:
	* Task 1: GainItem

### qe_iyaFal_2023_day09_t4:
* Name: No header for quest qe_iyaFal_2023_day09_t4
* Description: No description for quest qe_iyaFal_2023_day09_t4
* QuestLine: ql_event_iyaFal_2023_t4
* Type: Event
* EventId: event_season_iyaFal_2023_t4
* Goals:
	* Task 1: 5 Faction_T4up

### qe_iyaFal_2023_day10_t4:
* Name: No header for quest qe_iyaFal_2023_day10_t4
* Description: No description for quest qe_iyaFal_2023_day10_t4
* QuestLine: ql_event_iyaFal_2023_t4
* Type: Event
* EventId: event_season_iyaFal_2023_t4
* Goals:
	* Task 1: GainItem

### qe_iyaFal_2023_day11_t4:
* Name: No header for quest qe_iyaFal_2023_day11_t4
* Description: No description for quest qe_iyaFal_2023_day11_t4
* QuestLine: ql_event_iyaFal_2023_t4
* Type: Event
* EventId: event_season_iyaFal_2023_t4
* Goals:
	* Task 1: GainItem

### qe_iyaFal_2023_day12_t4:
* Name: No header for quest qe_iyaFal_2023_day12_t4
* Description: No description for quest qe_iyaFal_2023_day12_t4
* QuestLine: ql_event_iyaFal_2023_t4
* Type: Event
* EventId: event_season_iyaFal_2023_t4
* MailsOnCompletion: m_iyaFal_day12_log
* Goals:
	* Task 1: Complete side mission

### qe_iyaFal_2023_day13_t4:
* Name: No header for quest qe_iyaFal_2023_day13_t4
* Description: No description for quest qe_iyaFal_2023_day13_t4
* QuestLine: ql_event_iyaFal_2023_t4
* Type: Event
* EventId: event_season_iyaFal_2023_t4
* Goals:
	* Task 1: 225 RepTr1

### qe_iyaFal_2023_day14_t4:
* Name: No header for quest qe_iyaFal_2023_day14_t4
* Description: No description for quest qe_iyaFal_2023_day14_t4
* QuestLine: ql_event_iyaFal_2023_t4
* Type: Event
* EventId: event_season_iyaFal_2023_t4
* Goals:
	* Task 1: GainItem

### qe_iyaFal_2023_day15_t4:
* Name: No header for quest qe_iyaFal_2023_day15_t4
* Description: No description for quest qe_iyaFal_2023_day15_t4
* QuestLine: ql_event_iyaFal_2023_t4
* Type: Event
* EventId: event_season_iyaFal_2023_t4
* Goals:
	* Task 1: Complete mission 'Trader's Bargain T4'

## QL_EVENT_IYAFAL_2023_EPILOG_T4
### qe_iyaFal_2023_epi01_t4:
* Name: No header for quest qe_iyaFal_2023_epi01_t4
* Description: No description for quest qe_iyaFal_2023_epi01_t4
* QuestLine: ql_event_iyaFal_2023_epilog_t4
* Type: Event
* EventId: event_season_iyaFal_2023_t4
* Goals:
	* Task 1: GainItem

### qe_iyaFal_2023_epi02_t4:
* Name: No header for quest qe_iyaFal_2023_epi02_t4
* Description: No description for quest qe_iyaFal_2023_epi02_t4
* QuestLine: ql_event_iyaFal_2023_epilog_t4
* Type: Event
* EventId: event_season_iyaFal_2023_t4
* Goals:
	* Task 1: 10 ShipsDestroyedProgenitorT4

### qe_iyaFal_2023_epi03_t4:
* Name: No header for quest qe_iyaFal_2023_epi03_t4
* Description: No description for quest qe_iyaFal_2023_epi03_t4
* QuestLine: ql_event_iyaFal_2023_epilog_t4
* Type: Event
* EventId: event_season_iyaFal_2023_t4
* Goals:
	* Task 1: GainItem

### qe_iyaFal_2023_epi04_t4:
* Name: No header for quest qe_iyaFal_2023_epi04_t4
* Description: No description for quest qe_iyaFal_2023_epi04_t4
* QuestLine: ql_event_iyaFal_2023_epilog_t4
* Type: Event
* EventId: event_season_iyaFal_2023_t4
* Goals:
	* Task 1: UpgradeOfficer

### qe_iyaFal_2023_epi05_t4:
* Name: No header for quest qe_iyaFal_2023_epi05_t4
* Description: No description for quest qe_iyaFal_2023_epi05_t4
* QuestLine: ql_event_iyaFal_2023_epilog_t4
* Type: Event
* EventId: event_season_iyaFal_2023_t4
* Goals:
	* Task 1: Complete 5 side missions

## QL_EVENT_ANNIVERSARY_2023_T1
### qe_anniversary_2023_day01_A_t1:
* Name: Day 1: Research Directive
* Description: We received priority communication from Lazarus Base concerning Gideon S'jet. The transmission is encrypted with a specific vibration that can only be found on Hiigaran fabricators. We need to construct any item to match the encryption.

<color=#FBB03F>Small items such as strike craft, modules and parts can be built in the fabricator. Larger items such as escort ships and flagships must be constructed at shipyards provided at larger stations.</color>
* QuestLine: ql_event_anniversary_2023_t1
* Type: Event
* EventId: event_anniversary_2023_t1
* Goals:
	* Task 1: Craft

### qe_anniversary_2023_day01_B_t1:
* Name: The list given to us by Gideon includes many components found only in Progenitor ships. The easiest way to collect them is to harvest them from downed Progenitor units.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
* Description: The list given to us by Gideon includes many components found only in Progenitor ships. The easiest way to collect them is to harvest them from downed Progenitor units.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
* QuestLine: ql_event_anniversary_2023_t1
* Type: Event
* EventId: event_anniversary_2023_t1
* Goals:
	* Task 1: 7 ShipsDestroyedProgenitorT1_ShipsDestroyedProgenitorT2_ShipsDestroyedProgenitorT3_ShipsDestroyedProgenitorT4

### qe_anniversary_2023_day01_C_t1:
* Name: Progenitor Cognition Nodes are a fragile component often found floating in free space near ancient wreckages.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
* Description: Progenitor Cognition Nodes are a fragile component often found floating in free space near ancient wreckages.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
* QuestLine: ql_event_anniversary_2023_t1
* Type: Event
* EventId: event_anniversary_2023_t1
* Goals:
	* Task 1: GainItem

### qe_anniversary_2023_day02_A_t1:
* Name: Day 2: Cash Money
* Description: Ekekko can bring us in contact with traders specialized in Progenitor technology. But knowing the Iyatequa, everything has a price. We should mine minerals to recuperate the losses we'll have to pay.

<color=#FBB03F>Ore can be mined from asteroids in asteroid fields. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
* QuestLine: ql_event_anniversary_2023_t1
* Type: Event
* EventId: event_anniversary_2023_t1
* Goals:
	* Task 1: GainItem

### qe_anniversary_2023_day02_B_t1:
* Name: To impress the Iyatequa traders and procure the Progenitor components for Gideon, we will have to work on our reputation among a certain clientele.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Description: To impress the Iyatequa traders and buy the Progenitor components for Gideon, we will have to work on our reputation.

<color=#FBB03F>You can earn insignias by completing missions.</color>
* QuestLine: ql_event_anniversary_2023_t1
* Type: Event
* EventId: event_anniversary_2023_t1
* Goals:
	* Task 1: GainItem

### qe_anniversary_2023_day02_C_t1:
* Name: In order to raise funds to acquire the needed Progenitor components for Gideon, we must sell some of our stored items on the local market.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
* Description: In order to raise funds to acquire the needed Progenitor components for Gideon, we must sell some of our stored items on the local market.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
* QuestLine: ql_event_anniversary_2023_t1
* Type: Event
* EventId: event_anniversary_2023_t1
* Goals:
	* Task 1: GainItem

### qe_anniversary_2023_day03_A_t1:
* Name: Day 3: Stop Scouting
* Description: We need to search for recent communications data in this sector to pick up a lead on Guahai's Yaot fleet. We should find what we are looking for on recently destroyed ships.

<color=#FBB03F>The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.</color>
* QuestLine: ql_event_anniversary_2023_t1
* Type: Event
* EventId: event_anniversary_2023_t1
* Goals:
	* Task 1: 15 ShipsDestroyedT1_ShipsDestroyedT2_ShipsDestroyedT3_ShipsDestroyedT4

### qe_anniversary_2023_day03_B_t1:
* Name: We are in search of the missing data disk Guahai mentioned in his transmission. We might be able to find it in salvage crates from local outlaws.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
* Description: We are in search of the missing data disk Guahai mentioned in his transmission. We might be able to find it in salvage crates from local outlaws.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
* QuestLine: ql_event_anniversary_2023_t1
* Type: Event
* EventId: event_anniversary_2023_t1
* Goals:
	* Task 1: GainItem

### qe_anniversary_2023_day03_C_t1:
* Name: The reconnaissance disk gave us a lead on the Progenitor component the Yaot call the Stambha. Enemy activity is high in the target location.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* Description: The data disk gave us a lead on the Progenitor component the Yaot call the Stambah. It seems to be located inside a sector with strong enemy activity.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* QuestLine: ql_event_anniversary_2023_t1
* Type: Event
* EventId: event_anniversary_2023_t1
* Goals:
	* Task 1: Complete side mission

### qe_anniversary_2023_day04_A_t1:
* Name: Day 4: Lost and Found
* Description: Gideon has emerged from his laboratory. He talks of the possibility to build a device that could change the fortunes of Hiigarans in Nimbus. However, we must search for a final component.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
* QuestLine: ql_event_anniversary_2023_t1
* Type: Event
* EventId: event_anniversary_2023_t1
* Goals:
	* Task 1: Scan

### qe_anniversary_2023_day04_B_t1:
* Name: Gideon is in need of raw materials to construct a secret device. We should look for a jovian planet to collect some gas.

<color=#FBB03F>Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.</color>
* Description: Gideon is in need of raw materials to construct his secret device. We have to mine some minerals for him.

<color=#FBB03F>Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
* QuestLine: ql_event_anniversary_2023_t1
* Type: Event
* EventId: event_anniversary_2023_t1
* Goals:
	* Task 1: GainItem

### qe_anniversary_2023_day04_C_t1:
* Name: According to Ekekko, the last component on Gideon's list might be in the hands of a powerful enemy. The search for additional information is sending us into the most dangerous areas of this sector.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Description: According to Ekekko, the last component on Gideon's list might be in the hands of a powerful enemy. The search for additional information is sending us into the most dangerous areas of this sector.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* QuestLine: ql_event_anniversary_2023_t1
* Type: Event
* EventId: event_anniversary_2023_t1
* Goals:
	* Task 1: Complete side mission

### qe_anniversary_2023_day05_A_t1:
* Name: Day 5: Help Wanted
* Description: We want to make contact with Tepin Papan, commander of the Tanoch Empire. To open up a communication channel, we should do some hired work for the local authorities.

<color=#FBB03F>There are different types of assignments available in your assignment log.</color>
* QuestLine: ql_event_anniversary_2023_t1
* Type: Event
* EventId: event_anniversary_2023_t1
* Goals:
	* Task 1: 5 T1up

### qe_anniversary_2023_day05_B_t1:
* Name: Tepin Papan has offered to provide information on Gideon's last component if we help him with a security issue he currently faces.

<color=#FBB03F>Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.</color>
* Description: Tepin Papan has offered to provide information on Gideon's last component if we help him with a security issue he currently faces.

<color=#FBB03F>The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.</color>
* QuestLine: ql_event_anniversary_2023_t1
* Type: Event
* EventId: event_anniversary_2023_t1
* Goals:
	* Task 1: 15 ShipsDestroyedT1_ShipsDestroyedT2_ShipsDestroyedT3_ShipsDestroyedT4

### qe_anniversary_2023_day05_C_t1:
* Name: According to Tepin Papan, some of the Tanoch sectors require assistance. We should seek out their liaison offices and complete assignments.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Description: Tepin Papan wants us to retrieve some stolen goods. We should begin salvaging crates in the areas indicated by Tanoch data.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
* QuestLine: ql_event_anniversary_2023_t1
* Type: Event
* EventId: event_anniversary_2023_t1
* Goals:
	* Task 1: GainItem

### qe_anniversary_2023_day06_A_t1:
* Name: Day 6: Training Day
* Description: While Lazarus Base is processing the reports on the stolen Progenitor component, Gideon wants us to train a crew to handle the device he's constructing.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.</color>
* QuestLine: ql_event_anniversary_2023_t1
* Type: Event
* EventId: event_anniversary_2023_t1
* Goals:
	* Task 1: GainItem

### qe_anniversary_2023_day06_B_t1:
* Name: With Gideon's new program, we should start training the crew that will man his enigmatic device.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* Description: With Gideon's new program, we should start training the crew that will man his enigmatic device.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* QuestLine: ql_event_anniversary_2023_t1
* Type: Event
* EventId: event_anniversary_2023_t1
* Goals:
	* Task 1: UpgradeOfficer

### qe_anniversary_2023_day06_C_t1:
* Name: It is time to put our newly trained crew to the test. We received a task from Lazarus Base to engage a hostile fleet nearby.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* Description: It is time to put our newly trained crew to the test. We received a task from Lazarus Base to engage a hostile fleet nearby.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* QuestLine: ql_event_anniversary_2023_t1
* Type: Event
* EventId: event_anniversary_2023_t1
* Goals:
	* Task 1: Complete side mission

### qe_anniversary_2023_day07_A_t1:
* Name: Day 7: Simple Collection
* Description: Guhai is a high ranking Yaot official and Lazarus Base has advised us to follow his instructions for now. His first transmitted task needs us to mine resources.

<color=#FBB03F>Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
* QuestLine: ql_event_anniversary_2023_t1
* Type: Event
* EventId: event_anniversary_2023_t1
* Goals:
	* Task 1: GainItem

### qe_anniversary_2023_day07_B_t1:
* Name: We continue to follow Guahai’s orders. His next task for us is to produce refined material.

<color=#FBB03F>Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.</color>
* Description: We continue to follow Guahai’s orders. His next task for us is to produce refined material.

<color=#FBB03F>Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.</color>
* QuestLine: ql_event_anniversary_2023_t1
* Type: Event
* EventId: event_anniversary_2023_t1
* Goals:
	* Task 1: Craft

### qe_anniversary_2023_day07_C_t1:
* Name: Guahai requires us to build specific items for his fleet, as repayment for stealing their cultural item.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
* Description: Guahai requires us to build specific items for his fleet, as repayment for stealing their cultural item.

<color=#FBB03F>Small items such as strike craft, modules and parts can be built in the fabricator. Larger items such as escort ships and flagships must be constructed at shipyards provided at larger stations.</color>
* QuestLine: ql_event_anniversary_2023_t1
* Type: Event
* EventId: event_anniversary_2023_t1
* Goals:
	* Task 1: Craft

### qe_anniversary_2023_day08_A_t1:
* Name: Day 8: Cangacian Patrol
* Description: Lazarus Base has informed us that the Tanoch reports on the stolen Progenitor component point towards an infamous pirate group called The Fleet of Rams. We should hunt down Cangacian vessels for more information.

<color=#FBB03F>The Cangacians are pirates that harass trade routes and colonies. We may find them in signals in most areas of the galaxy. They have been sighted raiding mining fleets in asteroid clusters as well.</color>
* QuestLine: ql_event_anniversary_2023_t1
* Type: Event
* EventId: event_anniversary_2023_t1
* Goals:
	* Task 1: 10 ShipsDestroyedP1T1_ShipsDestroyedP1T2_ShipsDestroyedP1T3_ShipsDestroyedP1T4

### qe_anniversary_2023_day08_B_t1:
* Name: The last item Gideon needs to build his device is in the possession of Catequil, Lieutenant of the Fleet of Rams. We have to find communications data from hostile ships to locate his position.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
* Description: The last item Gideon needs to build his device is in the possession of Catequil, Lieutenant of the Fleet of Rams. We have to find communications data from hostile ships to locate his position.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
* QuestLine: ql_event_anniversary_2023_t1
* Type: Event
* EventId: event_anniversary_2023_t1
* Goals:
	* Task 1: GainItem

### qe_anniversary_2023_day08_C_t1:
* Name: Our engineers were able to triangulate Catequil's transmission. We must chase him down to attain the last Progenitor component for Gideon.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* Description: Our engineers were able to triangulate Catequil's transmission. We must chase him down to attain the last Progenitor component for Gideon.

<color=#FBB03F>The Cangacians are pirates that harass trade routes and colonies. We may find them in signals in most areas of the galaxy. They have been sighted raiding mining fleets in asteroid clusters as well.</color>
* QuestLine: ql_event_anniversary_2023_t1
* Type: Event
* EventId: event_anniversary_2023_t1
* Goals:
	* Task 1: 20 ShipsDestroyedP1T1_ShipsDestroyedP1T2_ShipsDestroyedP1T3_ShipsDestroyedP1T4

### qe_anniversary_2023_day09_A_t1:
* Name: Day 9: Special Instructions
* Description: While Gideon is finalizing the construction of the Progenitor Negotiator, one of our officers must be trained to utilize it in action.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* QuestLine: ql_event_anniversary_2023_t1
* Type: Event
* EventId: event_anniversary_2023_t1
* Goals:
	* Task 1: UpgradeOfficer

### qe_anniversary_2023_day09_B_t1:
* Name: Before we embark on Gideon's special operation, we should further increase our fleet's power to ensure we are ready for any eventuality.

<color=#FBB03F>Internal Modules can be upgraded in the Internal Module screen which increases their attributes. Upgrading one level costs credits and RE.</color>
* Description: We have to fabricate several items to modify a common freighter for Gideon's special operation.

<color=#FBB03F>Small items such as strike craft, modules and parts can be built in the fabricator. Larger items such as escort ships and flagships must be constructed at shipyards provided at larger stations.</color>
* QuestLine: ql_event_anniversary_2023_t1
* Type: Event
* EventId: event_anniversary_2023_t1
* Goals:
	* Task 1: Craft

### qe_anniversary_2023_day09_C_t1:
* Name: We are instructed to perform one final operations readiness test. All forces must be fully prepared for whatever Gideon is planning.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* Description: We are instructed to perform one final operations readiness test. All forces must be fully prepared for whatever Gideon is planning.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* QuestLine: ql_event_anniversary_2023_t1
* Type: Event
* EventId: event_anniversary_2023_t1
* Goals:
	* Task 1: Complete side mission

### qe_anniversary_2023_day10_A_t1:
* Name: Day 10: The Special Operation
* Description: Gideon has finally revealed his plan. From the Progenitor components we collected he constructed a communication device to retake control of Wiracoda Gate. We are trying to go home.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* QuestLine: ql_event_anniversary_2023_t1
* Type: Event
* EventId: event_anniversary_2023_t1
* MailsOnCompletion: m_anniversary_enoch_log
* Goals:
	* Task 1: Complete mission 'Return to Wiracoda Gate T1'

## QL_EVENT_ANNIVERSARY_2023_T2
### qe_anniversary_2023_day01_A_t2:
* Name: We received priority communication from Hiigaran Command of Lazarus Base concerning Gideon S'jet. We need to decrypt it in our laboratory first before we can read it.

<color=#FBB03F>Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.</color>
* Description: We received priority communication from Hiigaran Command of Lazarus Base concerning Gideon S'jet. We need to decrypt it in our laboratory first before we can read it.

<color=#FBB03F>Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.</color>
* QuestLine: ql_event_anniversary_2023_t2
* Type: Event
* EventId: event_anniversary_2023_t2
* Goals:
	* Task 1: GainItem

### qe_anniversary_2023_day01_B_t2:
* Name: The list given to us by Gideon includes many components found only in Progenitor ships. The easiest way to collect them is to harvest them from downed Progenitor units.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
* Description: The list given to us by Gideon includes many components found only in Progenitor ships. The easiest way to collect them is to harvest them from downed Progenitor units.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
* QuestLine: ql_event_anniversary_2023_t2
* Type: Event
* EventId: event_anniversary_2023_t2
* Goals:
	* Task 1: 7 ShipsDestroyedProgenitorT2_ShipsDestroyedProgenitorT3_ShipsDestroyedProgenitorT4

### qe_anniversary_2023_day01_C_t2:
* Name: Progenitor Cognition Nodes are a fragile component often found floating in free space near ancient wreckages.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
* Description: Progenitor Cognition Nodes are a fragile component often found floating in free space near ancient wreckages.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
* QuestLine: ql_event_anniversary_2023_t2
* Type: Event
* EventId: event_anniversary_2023_t2
* Goals:
	* Task 1: GainItem

### qe_anniversary_2023_day02_A_t2:
* Name: Ekekko can bring us in contact with traders specialized in Progenitor technology. But knowing the Iyatequa, everything has a price. We should mine minerals to recuperate the losses we'll have to pay.

<color=#FBB03F>Type D ore is not abundant enough to form asteroid clusters on its own. Instead, asteroids with D type ore can be found within clusters rich with other types of ore.</color>
* Description: Ekekko can bring us in contact with traders specialized in Progenitor technology. But knowing the Iyatequa, everything has a price. We should mine minerals to recuperate the losses we'll have to pay.

<color=#FBB03F>Type D ore is not abundant enough to form asteroid clusters on its own. Instead, asteroids with D type ore can be found within clusters rich with other types of ore.</color>
* QuestLine: ql_event_anniversary_2023_t2
* Type: Event
* EventId: event_anniversary_2023_t2
* Goals:
	* Task 1: GainItem

### qe_anniversary_2023_day02_B_t2:
* Name: To impress the Iyatequa traders and procure the Progenitor components for Gideon, we will have to work on our reputation among a certain clientele.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Description: To impress the Iyatequa traders and procure the Progenitor components for Gideon, we will have to work on our reputation among a certain clientele.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* QuestLine: ql_event_anniversary_2023_t2
* Type: Event
* EventId: event_anniversary_2023_t2
* Goals:
	* Task 1: 135 RepTr1

### qe_anniversary_2023_day02_C_t2:
* Name: In order to raise funds to acquire the needed Progenitor components for Gideon, we must sell some of our stored items on the local market.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
* Description: In order to raise funds to acquire the needed Progenitor components for Gideon, we must sell some of our stored items on the local market.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
* QuestLine: ql_event_anniversary_2023_t2
* Type: Event
* EventId: event_anniversary_2023_t2
* Goals:
	* Task 1: GainItem

### qe_anniversary_2023_day03_A_t2:
* Name: We need to search for recent communications data in this sector to pick up a lead on Guahai's Yaot fleet. We should find what we are looking for on recently destroyed ships.

<color=#FBB03F>The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.</color>
* Description: We need to search for recent communications data in this sector to pick up a lead on Guahai's Yaot fleet. We should find what we are looking for on recently destroyed ships.

<color=#FBB03F>The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.</color>
* QuestLine: ql_event_anniversary_2023_t2
* Type: Event
* EventId: event_anniversary_2023_t2
* Goals:
	* Task 1: 15 ShipsDestroyedT2_ShipsDestroyedT3_ShipsDestroyedT4

### qe_anniversary_2023_day03_B_t2:
* Name: We are in search of the missing data disk Guahai mentioned in his transmission. We might be able to find it in salvage crates from local outlaws.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
* Description: We are in search of the missing data disk Guahai mentioned in his transmission. We might be able to find it in salvage crates from local outlaws.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
* QuestLine: ql_event_anniversary_2023_t2
* Type: Event
* EventId: event_anniversary_2023_t2
* Goals:
	* Task 1: GainItem

### qe_anniversary_2023_day03_C_t2:
* Name: The reconnaissance disk gave us a lead on the Progenitor component the Yaot call the Stambha. Enemy activity is high in the target location.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* Description: The reconnaissance disk gave us a lead on the Progenitor component the Yaot call the Stambha. Enemy activity is high in the target location.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* QuestLine: ql_event_anniversary_2023_t2
* Type: Event
* EventId: event_anniversary_2023_t2
* Goals:
	* Task 1: Complete side mission

### qe_anniversary_2023_day04_A_t2:
* Name: Gideon has emerged from his laboratory. He talks of the possibility to build a device that could change the fortunes of Hiigarans in Nimbus. However, we must search for a final component.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
* Description: Gideon has emerged from his laboratory. He talks of the possibility to build a device that could change the fortunes of Hiigarans in Nimbus. However, we must search for a final component.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
* QuestLine: ql_event_anniversary_2023_t2
* Type: Event
* EventId: event_anniversary_2023_t2
* Goals:
	* Task 1: Scan

### qe_anniversary_2023_day04_B_t2:
* Name: Gideon is in need of raw materials to construct a secret device. We should look for a jovian planet to collect some gas.

<color=#FBB03F>Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.</color>
* Description: Gideon is in need of raw materials to construct his secret device. We have to mine some minerals for him.

<color=#FBB03F>Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
* QuestLine: ql_event_anniversary_2023_t2
* Type: Event
* EventId: event_anniversary_2023_t2
* Goals:
	* Task 1: GainItem

### qe_anniversary_2023_day04_C_t2:
* Name: According to Ekekko, the last component on Gideon's list might be in the hands of a powerful enemy. The search for additional information is sending us into the most dangerous areas of this sector.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Description: According to Ekekko, the last component on Gideon's list might be in the hands of a powerful enemy. The search for additional information is sending us into the most dangerous areas of this sector.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* QuestLine: ql_event_anniversary_2023_t2
* Type: Event
* EventId: event_anniversary_2023_t2
* Goals:
	* Task 1: Complete side mission

### qe_anniversary_2023_day05_A_t2:
* Name: We want to make contact with Tepin Papan, commander of the Tanoch Empire. To find a communication channel, we should do some hired work for the local authorities.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Description: We want to make contact with Tepin Papan, commander of the Tanoch Empire. To find a communication channel, we should do some hired work for the local authorities.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* QuestLine: ql_event_anniversary_2023_t2
* Type: Event
* EventId: event_anniversary_2023_t2
* Goals:
	* Task 1: 5 Faction_T2up

### qe_anniversary_2023_day05_B_t2:
* Name: Tepin Papan has offered to provide information on Gideon's last component if we help him with a security issue he currently faces.

<color=#FBB03F>Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.</color>
* Description: Tepin Papan has offered to provide information on Gideon's last component if we help him with a security issue he currently faces.

<color=#FBB03F>Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.</color>
* QuestLine: ql_event_anniversary_2023_t2
* Type: Event
* EventId: event_anniversary_2023_t2
* Goals:
	* Task 1: Complete 3 side missions

### qe_anniversary_2023_day05_C_t2:
* Name: According to Tepin Papan, some of the Tanoch sectors require assistance. We should seek out their liaison offices and complete assignments.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Description: According to Tepin Papan, some of the Tanoch sectors require assistance. We should seek out their liaison offices and complete assignments.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* QuestLine: ql_event_anniversary_2023_t2
* Type: Event
* EventId: event_anniversary_2023_t2
* Goals:
	* Task 1: 135 RepTanoch

### qe_anniversary_2023_day06_A_t2:
* Name: While Lazarus Base is processing the reports on the stolen Progenitor component, Gideon wants us to train a crew to handle the device he's constructing.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.</color>
* Description: While Lazarus Base is processing the reports on the stolen Progenitor component, Gideon wants us to train a crew to handle the device he's constructing.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.</color>
* QuestLine: ql_event_anniversary_2023_t2
* Type: Event
* EventId: event_anniversary_2023_t2
* Goals:
	* Task 1: GainItem

### qe_anniversary_2023_day06_B_t2:
* Name: With Gideon's new program, we should start training the crew that will man his enigmatic device.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* Description: With Gideon's new program, we should start training the crew that will man his enigmatic device.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* QuestLine: ql_event_anniversary_2023_t2
* Type: Event
* EventId: event_anniversary_2023_t2
* Goals:
	* Task 1: UpgradeOfficer

### qe_anniversary_2023_day06_C_t2:
* Name: It is time to put our newly trained crew to the test. We received a task from Lazarus Base to engage a hostile fleet nearby.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* Description: It is time to put our newly trained crew to the test. We received a task from Lazarus Base to engage a hostile fleet nearby.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* QuestLine: ql_event_anniversary_2023_t2
* Type: Event
* EventId: event_anniversary_2023_t2
* Goals:
	* Task 1: Complete side mission

### qe_anniversary_2023_day07_A_t2:
* Name: Guhai is a high ranking Yaot official and Lazarus Base has advised us to follow his instructions for now. His first transmitted task needs us to mine resources.

<color=#FBB03F>Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
* Description: Guhai is a high ranking Yaot official and Lazarus Base has advised us to follow his instructions for now. His first transmitted task needs us to mine resources.

<color=#FBB03F>Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
* QuestLine: ql_event_anniversary_2023_t2
* Type: Event
* EventId: event_anniversary_2023_t2
* Goals:
	* Task 1: GainItem

### qe_anniversary_2023_day07_B_t2:
* Name: We continue to follow Guahai’s orders. His next task for us is to produce refined material.

<color=#FBB03F>Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.</color>
* Description: We continue to follow Guahai’s orders. His next task for us is to produce refined material.

<color=#FBB03F>Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.</color>
* QuestLine: ql_event_anniversary_2023_t2
* Type: Event
* EventId: event_anniversary_2023_t2
* Goals:
	* Task 1: Craft

### qe_anniversary_2023_day07_C_t2:
* Name: Guahai requires us to build specific items for his fleet, as repayment for stealing their cultural item.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
* Description: Guahai requires us to build specific items for his fleet, as repayment for stealing their cultural item.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
* QuestLine: ql_event_anniversary_2023_t2
* Type: Event
* EventId: event_anniversary_2023_t2
* Goals:
	* Task 1: Craft

### qe_anniversary_2023_day08_A_t2:
* Name: Lazarus Base has informed us that the Tanoch reports on the stolen Progenitor component point towards an infamous pirate group called The Fleet of Rams. We should hunt down Cangacian vessels for more information.

<color=#FBB03F>The Cangacians are pirates that harass trade routes and colonies. We may find them in signals in most areas of the galaxy. They have been sighted raiding mining fleets in asteroid clusters as well.</color>
* Description: Lazarus Base has informed us that the Tanoch reports on the stolen Progenitor component point towards an infamous pirate group called The Fleet of Rams. We should hunt down Cangacian vessels for more information.

<color=#FBB03F>The Cangacians are pirates that harass trade routes and colonies. We may find them in signals in most areas of the galaxy. They have been sighted raiding mining fleets in asteroid clusters as well.</color>
* QuestLine: ql_event_anniversary_2023_t2
* Type: Event
* EventId: event_anniversary_2023_t2
* Goals:
	* Task 1: 10 ShipsDestroyedP1T2_ShipsDestroyedP1T3_ShipsDestroyedP1T4

### qe_anniversary_2023_day08_B_t2:
* Name: The last item Gideon needs to build his device is in the possession of Catequil, Lieutenant of the Fleet of Rams. We have to find communications data from hostile ships to locate his position.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
* Description: The last item Gideon needs to build his device is in the possession of Catequil, Lieutenant of the Fleet of Rams. We have to find communications data from hostile ships to locate his position.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
* QuestLine: ql_event_anniversary_2023_t2
* Type: Event
* EventId: event_anniversary_2023_t2
* Goals:
	* Task 1: GainItem

### qe_anniversary_2023_day08_C_t2:
* Name: Our engineers were able to triangulate Catequil's transmission. We must chase him down to attain the last Progenitor component for Gideon.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* Description: Our engineers were able to triangulate Catequil's transmission. We must chase him down to attain the last Progenitor component for Gideon.

<color=#FBB03F>The Cangacians are pirates that harass trade routes and colonies. We may find them in signals in most areas of the galaxy. They have been sighted raiding mining fleets in asteroid clusters as well.</color>
* QuestLine: ql_event_anniversary_2023_t2
* Type: Event
* EventId: event_anniversary_2023_t2
* Goals:
	* Task 1: 20 ShipsDestroyedP1T2_ShipsDestroyedP1T3_ShipsDestroyedP1T4

### qe_anniversary_2023_day09_A_t2:
* Name: While Gideon is finalizing the construction of the Progenitor Negotiator, we should increase our fleet's power to protect it in action.

<color=#FBB03F>External modules, such as turrets or sensors, can be upgraded in the External Module screen which will increase their power. Upgrading one level costs credits and RE.</color>
* Description: While Gideon is finalizing the construction of the Progenitor Negotiator, we should increase our fleet's power to protect it in action.

<color=#FBB03F>External modules, such as turrets or sensors, can be upgraded in the External Module screen which will increase their power. Upgrading one level costs credits and RE.</color>
* QuestLine: ql_event_anniversary_2023_t2
* Type: Event
* EventId: event_anniversary_2023_t2
* Goals:
	* Task 1: Craft

### qe_anniversary_2023_day09_B_t2:
* Name: Before we embark on Gideon's special operation, we should further increase our fleet's power to ensure we are ready for any eventuality.

<color=#FBB03F>Internal Modules can be upgraded in the Internal Module screen which increases their attributes. Upgrading one level costs credits and RE.</color>
* Description: We have to fabricate several items to modify a common freighter for Gideon's special operation.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
* QuestLine: ql_event_anniversary_2023_t2
* Type: Event
* EventId: event_anniversary_2023_t2
* Goals:
	* Task 1: Craft

### qe_anniversary_2023_day09_C_t2:
* Name: We are instructed to perform one final operations readiness test. All forces must be fully prepared for whatever Gideon is planning.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* Description: We are instructed to perform one final operations readiness test. All forces must be fully prepared for whatever Gideon is planning.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* QuestLine: ql_event_anniversary_2023_t2
* Type: Event
* EventId: event_anniversary_2023_t2
* Goals:
	* Task 1: Complete side mission

### qe_anniversary_2023_day10_A_t2:
* Name: Gideon has finally revealed his plan. From the Progenitor components we collected he constructed a communication device to retake control of Wiracoda Gate. We are trying to go home.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Description: Gideon has finally revealed his plan. From the Progenitor components we collected he constructed a communication device to retake control of Wiracoda Gate. We are trying to go home.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* QuestLine: ql_event_anniversary_2023_t2
* Type: Event
* EventId: event_anniversary_2023_t2
* MailsOnCompletion: m_anniversary_enoch_log
* Goals:
	* Task 1: Complete mission 'Return to Wiracoda Gate T2'

## QL_EVENT_ANNIVERSARY_2023_T3
### qe_anniversary_2023_day01_A_t3:
* Name: We received priority communication from Hiigaran Command of Lazarus Base concerning Gideon S'jet. We need to decrypt it in our laboratory first before we can read it.

<color=#FBB03F>Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.</color>
* Description: We received priority communication from Hiigaran Command of Lazarus Base concerning Gideon S'jet. We need to decrypt it in our laboratory first before we can read it.

<color=#FBB03F>Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.</color>
* QuestLine: ql_event_anniversary_2023_t3
* Type: Event
* EventId: event_anniversary_2023_t3
* Goals:
	* Task 1: GainItem

### qe_anniversary_2023_day01_B_t3:
* Name: The list given to us by Gideon includes many components found only in Progenitor ships. The easiest way to collect them is to harvest them from downed Progenitor units.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
* Description: The list given to us by Gideon includes many components found only in Progenitor ships. The easiest way to collect them is to harvest them from downed Progenitor units.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
* QuestLine: ql_event_anniversary_2023_t3
* Type: Event
* EventId: event_anniversary_2023_t3
* Goals:
	* Task 1: 7 ShipsDestroyedProgenitorT3_ShipsDestroyedProgenitorT4

### qe_anniversary_2023_day01_C_t3:
* Name: Progenitor Cognition Nodes are a fragile component often found floating in free space near ancient wreckages.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
* Description: Progenitor Cognition Nodes are a fragile component often found floating in free space near ancient wreckages.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
* QuestLine: ql_event_anniversary_2023_t3
* Type: Event
* EventId: event_anniversary_2023_t3
* Goals:
	* Task 1: GainItem

### qe_anniversary_2023_day02_A_t3:
* Name: Ekekko can bring us in contact with traders specialized in Progenitor technology. But knowing the Iyatequa, everything has a price. We should mine minerals to recuperate the losses we'll have to pay.

<color=#FBB03F>Type D ore is not abundant enough to form asteroid clusters on its own. Instead, asteroids with D type ore can be found within clusters rich with other types of ore.</color>
* Description: Ekekko can bring us in contact with traders specialized in Progenitor technology. But knowing the Iyatequa, everything has a price. We should mine minerals to recuperate the losses we'll have to pay.

<color=#FBB03F>Type D ore is not abundant enough to form asteroid clusters on its own. Instead, asteroids with D type ore can be found within clusters rich with other types of ore.</color>
* QuestLine: ql_event_anniversary_2023_t3
* Type: Event
* EventId: event_anniversary_2023_t3
* Goals:
	* Task 1: GainItem

### qe_anniversary_2023_day02_B_t3:
* Name: To impress the Iyatequa traders and procure the Progenitor components for Gideon, we will have to work on our reputation among a certain clientele.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Description: To impress the Iyatequa traders and procure the Progenitor components for Gideon, we will have to work on our reputation among a certain clientele.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* QuestLine: ql_event_anniversary_2023_t3
* Type: Event
* EventId: event_anniversary_2023_t3
* Goals:
	* Task 1: 180 RepTr1

### qe_anniversary_2023_day02_C_t3:
* Name: In order to raise funds to acquire the needed Progenitor components for Gideon, we must sell some of our stored items on the local market.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
* Description: In order to raise funds to acquire the needed Progenitor components for Gideon, we must sell some of our stored items on the local market.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
* QuestLine: ql_event_anniversary_2023_t3
* Type: Event
* EventId: event_anniversary_2023_t3
* Goals:
	* Task 1: GainItem

### qe_anniversary_2023_day03_A_t3:
* Name: We need to search for recent communications data in this sector to pick up a lead on Guahai's Yaot fleet. We should find what we are looking for on recently destroyed ships.

<color=#FBB03F>The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.</color>
* Description: We need to search for recent communications data in this sector to pick up a lead on Guahai's Yaot fleet. We should find what we are looking for on recently destroyed ships.

<color=#FBB03F>The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.</color>
* QuestLine: ql_event_anniversary_2023_t3
* Type: Event
* EventId: event_anniversary_2023_t3
* Goals:
	* Task 1: 15 ShipsDestroyedT3_ShipsDestroyedT4

### qe_anniversary_2023_day03_B_t3:
* Name: We are in search of the missing data disk Guahai mentioned in his transmission. We might be able to find it in salvage crates from local outlaws.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
* Description: We are in search of the missing data disk Guahai mentioned in his transmission. We might be able to find it in salvage crates from local outlaws.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
* QuestLine: ql_event_anniversary_2023_t3
* Type: Event
* EventId: event_anniversary_2023_t3
* Goals:
	* Task 1: GainItem

### qe_anniversary_2023_day03_C_t3:
* Name: The reconnaissance disk gave us a lead on the Progenitor component the Yaot call the Stambha. Enemy activity is high in the target location.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* Description: The reconnaissance disk gave us a lead on the Progenitor component the Yaot call the Stambha. Enemy activity is high in the target location.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* QuestLine: ql_event_anniversary_2023_t3
* Type: Event
* EventId: event_anniversary_2023_t3
* Goals:
	* Task 1: Complete side mission

### qe_anniversary_2023_day04_A_t3:
* Name: Gideon has emerged from his laboratory. He talks of the possibility to build a device that could change the fortunes of Hiigarans in Nimbus. However, we must search for a final component.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
* Description: Gideon has emerged from his laboratory. He talks of the possibility to build a device that could change the fortunes of Hiigarans in Nimbus. However, we must search for a final component.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
* QuestLine: ql_event_anniversary_2023_t3
* Type: Event
* EventId: event_anniversary_2023_t3
* Goals:
	* Task 1: Scan

### qe_anniversary_2023_day04_B_t3:
* Name: Gideon is in need of raw materials to construct a secret device. We should look for a jovian planet to collect some gas.

<color=#FBB03F>Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.</color>
* Description: Gideon is in need of raw materials to construct a secret device. We should look for a jovian planet to collect some gas.

<color=#FBB03F>Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.</color>
* QuestLine: ql_event_anniversary_2023_t3
* Type: Event
* EventId: event_anniversary_2023_t3
* Goals:
	* Task 1: GainItem

### qe_anniversary_2023_day04_C_t3:
* Name: According to Ekekko, the last component on Gideon's list might be in the hands of a powerful enemy. The search for additional information is sending us into the most dangerous areas of this sector.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Description: According to Ekekko, the last component on Gideon's list might be in the hands of a powerful enemy. The search for additional information is sending us into the most dangerous areas of this sector.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* QuestLine: ql_event_anniversary_2023_t3
* Type: Event
* EventId: event_anniversary_2023_t3
* Goals:
	* Task 1: Complete side mission

### qe_anniversary_2023_day05_A_t3:
* Name: We want to make contact with Tepin Papan, commander of the Tanoch Empire. To find a communication channel, we should do some hired work for the local authorities.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Description: We want to make contact with Tepin Papan, commander of the Tanoch Empire. To find a communication channel, we should do some hired work for the local authorities.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* QuestLine: ql_event_anniversary_2023_t3
* Type: Event
* EventId: event_anniversary_2023_t3
* Goals:
	* Task 1: 5 Faction_T3up

### qe_anniversary_2023_day05_B_t3:
* Name: Tepin Papan has offered to provide information on Gideon's last component if we help him with a security issue he currently faces.

<color=#FBB03F>Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.</color>
* Description: Tepin Papan has offered to provide information on Gideon's last component if we help him with a security issue he currently faces.

<color=#FBB03F>Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.</color>
* QuestLine: ql_event_anniversary_2023_t3
* Type: Event
* EventId: event_anniversary_2023_t3
* Goals:
	* Task 1: Complete 3 side missions

### qe_anniversary_2023_day05_C_t3:
* Name: According to Tepin Papan, some of the Tanoch sectors require assistance. We should seek out their liaison offices and complete assignments.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Description: According to Tepin Papan, some of the Tanoch sectors require assistance. We should seek out their liaison offices and complete assignments.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* QuestLine: ql_event_anniversary_2023_t3
* Type: Event
* EventId: event_anniversary_2023_t3
* Goals:
	* Task 1: 180 RepTanoch

### qe_anniversary_2023_day06_A_t3:
* Name: While Lazarus Base is processing the reports on the stolen Progenitor component, Gideon wants us to train a crew to handle the device he's constructing.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.</color>
* Description: While Lazarus Base is processing the reports on the stolen Progenitor component, Gideon wants us to train a crew to handle the device he's constructing.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.</color>
* QuestLine: ql_event_anniversary_2023_t3
* Type: Event
* EventId: event_anniversary_2023_t3
* Goals:
	* Task 1: GainItem

### qe_anniversary_2023_day06_B_t3:
* Name: With Gideon's new program, we should start training the crew that will man his enigmatic device.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* Description: With Gideon's new program, we should start training the crew that will man his enigmatic device.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* QuestLine: ql_event_anniversary_2023_t3
* Type: Event
* EventId: event_anniversary_2023_t3
* Goals:
	* Task 1: UpgradeOfficer

### qe_anniversary_2023_day06_C_t3:
* Name: It is time to put our newly trained crew to the test. We received a task from Lazarus Base to engage a hostile fleet nearby.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* Description: It is time to put our newly trained crew to the test. We received a task from Lazarus Base to engage a hostile fleet nearby.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* QuestLine: ql_event_anniversary_2023_t3
* Type: Event
* EventId: event_anniversary_2023_t3
* Goals:
	* Task 1: Complete side mission

### qe_anniversary_2023_day07_A_t3:
* Name: Guhai is a high ranking Yaot official and Lazarus Base has advised us to follow his instructions for now. His first transmitted task needs us to mine resources.

<color=#FBB03F>Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
* Description: Guhai is a high ranking Yaot official and Lazarus Base has advised us to follow his instructions for now. His first transmitted task needs us to mine resources.

<color=#FBB03F>Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
* QuestLine: ql_event_anniversary_2023_t3
* Type: Event
* EventId: event_anniversary_2023_t3
* Goals:
	* Task 1: GainItem

### qe_anniversary_2023_day07_B_t3:
* Name: We continue to follow Guahai’s orders. His next task for us is to produce refined material.

<color=#FBB03F>Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.</color>
* Description: We continue to follow Guahai’s orders. His next task for us is to produce refined material.

<color=#FBB03F>Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.</color>
* QuestLine: ql_event_anniversary_2023_t3
* Type: Event
* EventId: event_anniversary_2023_t3
* Goals:
	* Task 1: Craft

### qe_anniversary_2023_day07_C_t3:
* Name: Guahai requires us to build specific items for his fleet, as repayment for stealing their cultural item.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
* Description: Guahai requires us to build specific items for his fleet, as repayment for stealing their cultural item.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
* QuestLine: ql_event_anniversary_2023_t3
* Type: Event
* EventId: event_anniversary_2023_t3
* Goals:
	* Task 1: Craft

### qe_anniversary_2023_day08_A_t3:
* Name: Lazarus Base has informed us that the Tanoch reports on the stolen Progenitor component point towards an infamous pirate group called The Fleet of Rams. We should hunt down Cangacian vessels for more information.

<color=#FBB03F>The Cangacians are pirates that harass trade routes and colonies. We may find them in signals in most areas of the galaxy. They have been sighted raiding mining fleets in asteroid clusters as well.</color>
* Description: Lazarus Base has informed us that the Tanoch reports on the stolen Progenitor component point towards an infamous pirate group called The Fleet of Rams. We should hunt down Cangacian vessels for more information.

<color=#FBB03F>The Cangacians are pirates that harass trade routes and colonies. We may find them in signals in most areas of the galaxy. They have been sighted raiding mining fleets in asteroid clusters as well.</color>
* QuestLine: ql_event_anniversary_2023_t3
* Type: Event
* EventId: event_anniversary_2023_t3
* Goals:
	* Task 1: 10 ShipsDestroyedP1T3_ShipsDestroyedP1T4

### qe_anniversary_2023_day08_B_t3:
* Name: The last item Gideon needs to build his device is in the possession of Catequil, Lieutenant of the Fleet of Rams. We have to find communications data from hostile ships to locate his position.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
* Description: The last item Gideon needs to build his device is in the possession of Catequil, Lieutenant of the Fleet of Rams. We have to find communications data from hostile ships to locate his position.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
* QuestLine: ql_event_anniversary_2023_t3
* Type: Event
* EventId: event_anniversary_2023_t3
* Goals:
	* Task 1: GainItem

### qe_anniversary_2023_day08_C_t3:
* Name: Our engineers were able to triangulate Catequil's transmission. We must chase him down to attain the last Progenitor component for Gideon.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* Description: Our engineers were able to triangulate Catequil's transmission. We must chase him down to attain the last Progenitor component for Gideon.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* QuestLine: ql_event_anniversary_2023_t3
* Type: Event
* EventId: event_anniversary_2023_t3
* Goals:
	* Task 1: Complete quest 'Pahra's Rock'

### qe_anniversary_2023_day09_A_t3:
* Name: While Gideon is finalizing the construction of the Progenitor Negotiator, we should increase our fleet's power to protect it in action.

<color=#FBB03F>External modules, such as turrets or sensors, can be upgraded in the External Module screen which will increase their power. Upgrading one level costs credits and RE.</color>
* Description: While Gideon is finalizing the construction of the Progenitor Negotiator, we should increase our fleet's power to protect it in action.

<color=#FBB03F>External modules, such as turrets or sensors, can be upgraded in the External Module screen which will increase their power. Upgrading one level costs credits and RE.</color>
* QuestLine: ql_event_anniversary_2023_t3
* Type: Event
* EventId: event_anniversary_2023_t3
* Goals:
	* Task 1: Craft

### qe_anniversary_2023_day09_B_t3:
* Name: Before we embark on Gideon's special operation, we should further increase our fleet's power to ensure we are ready for any eventuality.

<color=#FBB03F>Internal Modules can be upgraded in the Internal Module screen which increases their attributes. Upgrading one level costs credits and RE.</color>
* Description: Before we embark on Gideon's special operation, we should further increase our fleet's power to ensure we are ready for any eventuality.

<color=#FBB03F>Internal Modules can be upgraded in the Internal Module screen which increases their attributes. Upgrading one level costs credits and RE.</color>
* QuestLine: ql_event_anniversary_2023_t3
* Type: Event
* EventId: event_anniversary_2023_t3
* Goals:
	* Task 1: Craft

### qe_anniversary_2023_day09_C_t3:
* Name: We are instructed to perform one final operations readiness test. All forces must be fully prepared for whatever Gideon is planning.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* Description: We are instructed to perform one final operations readiness test. All forces must be fully prepared for whatever Gideon is planning.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* QuestLine: ql_event_anniversary_2023_t3
* Type: Event
* EventId: event_anniversary_2023_t3
* Goals:
	* Task 1: Complete side mission

### qe_anniversary_2023_day10_A_t3:
* Name: Gideon has finally revealed his plan. From the Progenitor components we collected he constructed a communication device to retake control of Wiracoda Gate. We are trying to go home.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Description: Gideon has finally revealed his plan. From the Progenitor components we collected he constructed a communication device to retake control of Wiracoda Gate. We are trying to go home.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* QuestLine: ql_event_anniversary_2023_t3
* Type: Event
* EventId: event_anniversary_2023_t3
* MailsOnCompletion: m_anniversary_enoch_log
* Goals:
	* Task 1: Complete mission 'Return to Wiracoda Gate T3'

## QL_EVENT_ANNIVERSARY_2023_T4
### qe_anniversary_2023_day01_A_t4:
* Name: We received priority communication from Hiigaran Command of Lazarus Base concerning Gideon S'jet. We need to decrypt it in our laboratory first before we can read it.

<color=#FBB03F>Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.</color>
* Description: We received priority communication from Hiigaran Command of Lazarus Base concerning Gideon S'jet. We need to decrypt it in our laboratory first before we can read it.

<color=#FBB03F>Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.</color>
* QuestLine: ql_event_anniversary_2023_t4
* Type: Event
* EventId: event_anniversary_2023_t4
* Goals:
	* Task 1: GainItem

### qe_anniversary_2023_day01_B_t4:
* Name: The list given to us by Gideon includes many components found only in Progenitor ships. The easiest way to collect them is to harvest them from downed Progenitor units.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
* Description: The list given to us by Gideon includes many components found only in Progenitor ships. The easiest way to collect them is to harvest them from downed Progenitor units.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
* QuestLine: ql_event_anniversary_2023_t4
* Type: Event
* EventId: event_anniversary_2023_t4
* Goals:
	* Task 1: 7 ShipsDestroyedProgenitorT4

### qe_anniversary_2023_day01_C_t4:
* Name: Progenitor Cognition Nodes are a fragile component often found floating in free space near ancient wreckages.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
* Description: Progenitor Cognition Nodes are a fragile component often found floating in free space near ancient wreckages.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
* QuestLine: ql_event_anniversary_2023_t4
* Type: Event
* EventId: event_anniversary_2023_t4
* Goals:
	* Task 1: GainItem

### qe_anniversary_2023_day02_A_t4:
* Name: Ekekko can bring us in contact with traders specialized in Progenitor technology. But knowing the Iyatequa, everything has a price. We should mine minerals to recuperate the losses we'll have to pay.

<color=#FBB03F>Type D ore is not abundant enough to form asteroid clusters on its own. Instead, asteroids with D type ore can be found within clusters rich with other types of ore.</color>
* Description: Ekekko can bring us in contact with traders specialized in Progenitor technology. But knowing the Iyatequa, everything has a price. We should mine minerals to recuperate the losses we'll have to pay.

<color=#FBB03F>Type D ore is not abundant enough to form asteroid clusters on its own. Instead, asteroids with D type ore can be found within clusters rich with other types of ore.</color>
* QuestLine: ql_event_anniversary_2023_t4
* Type: Event
* EventId: event_anniversary_2023_t4
* Goals:
	* Task 1: GainItem

### qe_anniversary_2023_day02_B_t4:
* Name: To impress the Iyatequa traders and procure the Progenitor components for Gideon, we will have to work on our reputation among a certain clientele.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Description: To impress the Iyatequa traders and procure the Progenitor components for Gideon, we will have to work on our reputation among a certain clientele.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* QuestLine: ql_event_anniversary_2023_t4
* Type: Event
* EventId: event_anniversary_2023_t4
* Goals:
	* Task 1: 225 RepTr1

### qe_anniversary_2023_day02_C_t4:
* Name: In order to raise funds to acquire the needed Progenitor components for Gideon, we must sell some of our stored items on the local market.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
* Description: In order to raise funds to acquire the needed Progenitor components for Gideon, we must sell some of our stored items on the local market.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
* QuestLine: ql_event_anniversary_2023_t4
* Type: Event
* EventId: event_anniversary_2023_t4
* Goals:
	* Task 1: GainItem

### qe_anniversary_2023_day03_A_t4:
* Name: We need to search for recent communications data in this sector to pick up a lead on Guahai's Yaot fleet. We should find what we are looking for on recently destroyed ships.

<color=#FBB03F>The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.</color>
* Description: We need to search for recent communications data in this sector to pick up a lead on Guahai's Yaot fleet. We should find what we are looking for on recently destroyed ships.

<color=#FBB03F>The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.</color>
* QuestLine: ql_event_anniversary_2023_t4
* Type: Event
* EventId: event_anniversary_2023_t4
* Goals:
	* Task 1: 15 ShipsDestroyedT4

### qe_anniversary_2023_day03_B_t4:
* Name: We are in search of the missing data disk Guahai mentioned in his transmission. We might be able to find it in salvage crates from local outlaws.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
* Description: We are in search of the missing data disk Guahai mentioned in his transmission. We might be able to find it in salvage crates from local outlaws.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
* QuestLine: ql_event_anniversary_2023_t4
* Type: Event
* EventId: event_anniversary_2023_t4
* Goals:
	* Task 1: GainItem

### qe_anniversary_2023_day03_C_t4:
* Name: The reconnaissance disk gave us a lead on the Progenitor component the Yaot call the Stambha. Enemy activity is high in the target location.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* Description: The reconnaissance disk gave us a lead on the Progenitor component the Yaot call the Stambha. Enemy activity is high in the target location.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* QuestLine: ql_event_anniversary_2023_t4
* Type: Event
* EventId: event_anniversary_2023_t4
* Goals:
	* Task 1: Complete side mission

### qe_anniversary_2023_day04_A_t4:
* Name: Gideon has emerged from his laboratory. He talks of the possibility to build a device that could change the fortunes of Hiigarans in Nimbus. However, we must search for a final component.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
* Description: Gideon has emerged from his laboratory. He talks of the possibility to build a device that could change the fortunes of Hiigarans in Nimbus. However, we must search for a final component.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
* QuestLine: ql_event_anniversary_2023_t4
* Type: Event
* EventId: event_anniversary_2023_t4
* Goals:
	* Task 1: Scan

### qe_anniversary_2023_day04_B_t4:
* Name: Gideon is in need of raw materials to construct a secret device. We should look for a jovian planet to collect some gas.

<color=#FBB03F>Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.</color>
* Description: Gideon is in need of raw materials to construct a secret device. We should look for a jovian planet to collect some gas.

<color=#FBB03F>Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.</color>
* QuestLine: ql_event_anniversary_2023_t4
* Type: Event
* EventId: event_anniversary_2023_t4
* Goals:
	* Task 1: GainItem

### qe_anniversary_2023_day04_C_t4:
* Name: According to Ekekko, the last component on Gideon's list might be in the hands of a powerful enemy. The search for additional information is sending us into the most dangerous areas of this sector.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Description: According to Ekekko, the last component on Gideon's list might be in the hands of a powerful enemy. The search for additional information is sending us into the most dangerous areas of this sector.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* QuestLine: ql_event_anniversary_2023_t4
* Type: Event
* EventId: event_anniversary_2023_t4
* Goals:
	* Task 1: Complete side mission

### qe_anniversary_2023_day05_A_t4:
* Name: We want to make contact with Tepin Papan, commander of the Tanoch Empire. To find a communication channel, we should do some hired work for the local authorities.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Description: We want to make contact with Tepin Papan, commander of the Tanoch Empire. To find a communication channel, we should do some hired work for the local authorities.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* QuestLine: ql_event_anniversary_2023_t4
* Type: Event
* EventId: event_anniversary_2023_t4
* Goals:
	* Task 1: 5 Faction_T4up

### qe_anniversary_2023_day05_B_t4:
* Name: Tepin Papan has offered to provide information on Gideon's last component if we help him with a security issue he currently faces.

<color=#FBB03F>Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.</color>
* Description: Tepin Papan has offered to provide information on Gideon's last component if we help him with a security issue he currently faces.

<color=#FBB03F>Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.</color>
* QuestLine: ql_event_anniversary_2023_t4
* Type: Event
* EventId: event_anniversary_2023_t4
* Goals:
	* Task 1: Complete 3 side missions

### qe_anniversary_2023_day05_C_t4:
* Name: According to Tepin Papan, some of the Tanoch sectors require assistance. We should seek out their liaison offices and complete assignments.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Description: According to Tepin Papan, some of the Tanoch sectors require assistance. We should seek out their liaison offices and complete assignments.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* QuestLine: ql_event_anniversary_2023_t4
* Type: Event
* EventId: event_anniversary_2023_t4
* Goals:
	* Task 1: 225 RepTanoch

### qe_anniversary_2023_day06_A_t4:
* Name: While Lazarus Base is processing the reports on the stolen Progenitor component, Gideon wants us to train a crew to handle the device he's constructing.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.</color>
* Description: While Lazarus Base is processing the reports on the stolen Progenitor component, Gideon wants us to train a crew to handle the device he's constructing.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.</color>
* QuestLine: ql_event_anniversary_2023_t4
* Type: Event
* EventId: event_anniversary_2023_t4
* Goals:
	* Task 1: GainItem

### qe_anniversary_2023_day06_B_t4:
* Name: With Gideon's new program, we should start training the crew that will man his enigmatic device.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* Description: With Gideon's new program, we should start training the crew that will man his enigmatic device.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* QuestLine: ql_event_anniversary_2023_t4
* Type: Event
* EventId: event_anniversary_2023_t4
* Goals:
	* Task 1: UpgradeOfficer

### qe_anniversary_2023_day06_C_t4:
* Name: It is time to put our newly trained crew to the test. We received a task from Lazarus Base to engage a hostile fleet nearby.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* Description: It is time to put our newly trained crew to the test. We received a task from Lazarus Base to engage a hostile fleet nearby.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* QuestLine: ql_event_anniversary_2023_t4
* Type: Event
* EventId: event_anniversary_2023_t4
* Goals:
	* Task 1: Complete side mission

### qe_anniversary_2023_day07_A_t4:
* Name: Guhai is a high ranking Yaot official and Lazarus Base has advised us to follow his instructions for now. His first transmitted task needs us to mine resources.

<color=#FBB03F>Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
* Description: Guhai is a high ranking Yaot official and Lazarus Base has advised us to follow his instructions for now. His first transmitted task needs us to mine resources.

<color=#FBB03F>Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
* QuestLine: ql_event_anniversary_2023_t4
* Type: Event
* EventId: event_anniversary_2023_t4
* Goals:
	* Task 1: GainItem

### qe_anniversary_2023_day07_B_t4:
* Name: We continue to follow Guahai’s orders. His next task for us is to produce refined material.

<color=#FBB03F>Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.</color>
* Description: We continue to follow Guahai’s orders. His next task for us is to produce refined material.

<color=#FBB03F>Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.</color>
* QuestLine: ql_event_anniversary_2023_t4
* Type: Event
* EventId: event_anniversary_2023_t4
* Goals:
	* Task 1: Craft

### qe_anniversary_2023_day07_C_t4:
* Name: Guahai requires us to build specific items for his fleet, as repayment for stealing their cultural item.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
* Description: Guahai requires us to build specific items for his fleet, as repayment for stealing their cultural item.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
* QuestLine: ql_event_anniversary_2023_t4
* Type: Event
* EventId: event_anniversary_2023_t4
* Goals:
	* Task 1: Craft

### qe_anniversary_2023_day08_A_t4:
* Name: Lazarus Base has informed us that the Tanoch reports on the stolen Progenitor component point towards an infamous pirate group called The Fleet of Rams. We should hunt down Cangacian vessels for more information.

<color=#FBB03F>The Cangacians are pirates that harass trade routes and colonies. We may find them in signals in most areas of the galaxy. They have been sighted raiding mining fleets in asteroid clusters as well.</color>
* Description: Lazarus Base has informed us that the Tanoch reports on the stolen Progenitor component point towards an infamous pirate group called The Fleet of Rams. We should hunt down Cangacian vessels for more information.

<color=#FBB03F>The Cangacians are pirates that harass trade routes and colonies. We may find them in signals in most areas of the galaxy. They have been sighted raiding mining fleets in asteroid clusters as well.</color>
* QuestLine: ql_event_anniversary_2023_t4
* Type: Event
* EventId: event_anniversary_2023_t4
* Goals:
	* Task 1: 10 ShipsDestroyedP1T4

### qe_anniversary_2023_day08_B_t4:
* Name: The last item Gideon needs to build his device is in the possession of Catequil, Lieutenant of the Fleet of Rams. We have to find communications data from hostile ships to locate his position.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
* Description: The last item Gideon needs to build his device is in the possession of Catequil, Lieutenant of the Fleet of Rams. We have to find communications data from hostile ships to locate his position.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
* QuestLine: ql_event_anniversary_2023_t4
* Type: Event
* EventId: event_anniversary_2023_t4
* Goals:
	* Task 1: GainItem

### qe_anniversary_2023_day08_C_t4:
* Name: Our engineers were able to triangulate Catequil's transmission. We must chase him down to attain the last Progenitor component for Gideon.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* Description: Our engineers were able to triangulate Catequil's transmission. We must chase him down to attain the last Progenitor component for Gideon.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* QuestLine: ql_event_anniversary_2023_t4
* Type: Event
* EventId: event_anniversary_2023_t4
* Goals:
	* Task 1: Complete quest 'Pahra's Rock (Heroic)'

### qe_anniversary_2023_day09_A_t4:
* Name: While Gideon is finalizing the construction of the Progenitor Negotiator, we should increase our fleet's power to protect it in action.

<color=#FBB03F>External modules, such as turrets or sensors, can be upgraded in the External Module screen which will increase their power. Upgrading one level costs credits and RE.</color>
* Description: While Gideon is finalizing the construction of the Progenitor Negotiator, we should increase our fleet's power to protect it in action.

<color=#FBB03F>External modules, such as turrets or sensors, can be upgraded in the External Module screen which will increase their power. Upgrading one level costs credits and RE.</color>
* QuestLine: ql_event_anniversary_2023_t4
* Type: Event
* EventId: event_anniversary_2023_t4
* Goals:
	* Task 1: Craft

### qe_anniversary_2023_day09_B_t4:
* Name: Before we embark on Gideon's special operation, we should further increase our fleet's power to ensure we are ready for any eventuality.

<color=#FBB03F>Internal Modules can be upgraded in the Internal Module screen which increases their attributes. Upgrading one level costs credits and RE.</color>
* Description: Before we embark on Gideon's special operation, we should further increase our fleet's power to ensure we are ready for any eventuality.

<color=#FBB03F>Internal Modules can be upgraded in the Internal Module screen which increases their attributes. Upgrading one level costs credits and RE.</color>
* QuestLine: ql_event_anniversary_2023_t4
* Type: Event
* EventId: event_anniversary_2023_t4
* Goals:
	* Task 1: Craft

### qe_anniversary_2023_day09_C_t4:
* Name: We are instructed to perform one final operations readiness test. All forces must be fully prepared for whatever Gideon is planning.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* Description: We are instructed to perform one final operations readiness test. All forces must be fully prepared for whatever Gideon is planning.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* QuestLine: ql_event_anniversary_2023_t4
* Type: Event
* EventId: event_anniversary_2023_t4
* Goals:
	* Task 1: Complete side mission

### qe_anniversary_2023_day10_A_t4:
* Name: Gideon has finally revealed his plan. From the Progenitor components we collected he constructed a communication device to retake control of Wiracoda Gate. We are trying to go home.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Description: Gideon has finally revealed his plan. From the Progenitor components we collected he constructed a communication device to retake control of Wiracoda Gate. We are trying to go home.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* QuestLine: ql_event_anniversary_2023_t4
* Type: Event
* EventId: event_anniversary_2023_t4
* MailsOnCompletion: m_anniversary_enoch_log
* Goals:
	* Task 1: Complete mission 'Return to Wiracoda Gate T4'

## QL_EVENT_HALLOWEEN_2023_T1
### qe_halloween_2023_day01_t1:
* Name: Day 1: Sentinel Duty
* Description: We are receiving disturbing reports from all over the galaxy. The disaster at Wiracoda Gate has sent the Progenitors into a frenzy! We must assist the defensive efforts wherever we can until we understand what is happening.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
* QuestLine: ql_event_halloween_2023_t1
* Type: Event
* EventId: event_halloween_2023_t1
* Goals:
	* Task 1: 10 ShipsDestroyedProgenitorT1_ShipsDestroyedProgenitorT2_ShipsDestroyedProgenitorT3_ShipsDestroyedProgenitorT4

### qe_halloween_2023_day02_t1:
* Name: Day 2: Prospector
* Description: Refineries are being targeted by the Progenitors in many sectors of Nimbus. Stocks need to be replenished if the defenders are to hold off this calamity.

<color=#FBB03F>Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
* QuestLine: ql_event_halloween_2023_t1
* Type: Event
* EventId: event_halloween_2023_t1
* Goals:
	* Task 1: GainItem

### qe_halloween_2023_day03_t1:
* Name: Day 3: Deep Space Recovery
* Description: Gideon wants to collect any evidence which points to the Progenitor’s current activity. We should collect data from ships that were in combat with the abnormal Progenitor vessels.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
* QuestLine: ql_event_halloween_2023_t1
* Type: Event
* EventId: event_halloween_2023_t1
* Goals:
	* Task 1: GainItem

### qe_halloween_2023_day04_t1:
* Name: Day 4: Smelt and Refine
* Description: Many planets are still in desperate need of resources to hold off the Progenitors. Especially rare resources have been in high demand to increase defensive capabilities.

<color=#FBB03F>Rare earths are an occasional by-product of refining. They are required for upgrading modules.</color>
* QuestLine: ql_event_halloween_2023_t1
* Type: Event
* EventId: event_halloween_2023_t1
* Goals:
	* Task 1: GainItem

### qe_halloween_2023_day05_t1:
* Name: Day 5: The Guidepost
* Description: Gideon has identified a specific Progenitor component we must find in order to decrypt the errant Keeper's command frequency.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
* QuestLine: ql_event_halloween_2023_t1
* Type: Event
* EventId: event_halloween_2023_t1
* Goals:
	* Task 1: GainItem

### qe_halloween_2023_day06_t1:
* Name: Day 6: Replacement Parts
* Description: Many sectors have suffered heavy damages from the ongoing Progenitor attacks. More parts are needed to replenish the defending fleets.

<color=#FBB03F>Small items such as strike craft, modules and parts can be built in the fabricator. Larger items such as escort ships and flagships must be constructed at shipyards provided at larger stations.</color>
* QuestLine: ql_event_halloween_2023_t1
* Type: Event
* EventId: event_halloween_2023_t1
* Goals:
	* Task 1: Craft

### qe_halloween_2023_day07_t1:
* Name: Day 7: Triangulation
* Description: In order for Gideon to triangulate the location of the errant Keeper we need to hunt down Progenitor vessels receiving its command signal.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
* QuestLine: ql_event_halloween_2023_t1
* Type: Event
* EventId: event_halloween_2023_t1
* Goals:
	* Task 1: 10 ShipsDestroyedProgenitorT1_ShipsDestroyedProgenitorT2_ShipsDestroyedProgenitorT3_ShipsDestroyedProgenitorT4

### qe_halloween_2023_day08_t1:
* Name: Day 8: Officer Training
* Description: We are unsure what awaits us when we'll face the corrupted Keeper once again. Gideon has advised us to train our officers in Progenitor communication theory to effectively analyze the situation in the field.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* QuestLine: ql_event_halloween_2023_t1
* Type: Event
* EventId: event_halloween_2023_t1
* Goals:
	* Task 1: UpgradeOfficer

### qe_halloween_2023_day09_t1:
* Name: Day 9: Military Exercise
* Description: In order to be fully prepared for the confrontation with the corrupted Keeper, we need to perform a fleet wide ready-check for all systems. We can engage enemies that have been preying on the local area lately due to the diminished security situation.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* QuestLine: ql_event_halloween_2023_t1
* Type: Event
* EventId: event_halloween_2023_t1
* Goals:
	* Task 1: Complete side mission

### qe_halloween_2023_day10_t1:
* Name: Day 10: Safe Passage
* Description: The Iyatequa promised to negotiate a deal for safe passage into Cangacian space. However, even though the galaxy is at stake, the traders still insist on receiving a hefty price.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
* QuestLine: ql_event_halloween_2023_t1
* Type: Event
* EventId: event_halloween_2023_t1
* Goals:
	* Task 1: GainItem

### qe_halloween_2023_day11_t1:
* Name: Day 11: Confrontation
* Description: We must confront the corrupted Keeper Malik and end the Progenitor incursion.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* QuestLine: ql_event_halloween_2023_t1
* Type: Event
* EventId: event_halloween_2023_t1
* Goals:
	* Task 1: Complete mission 'Rashidun T1'

## QL_EVENT_HALLOWEEN_2023_T2
### qe_halloween_2023_day01_t2:
* Name: We are receiving disturbing reports from all over the galaxy. The disaster at Wiracoda Gate has sent the Progenitors into a frenzy! We must assist the defensive efforts wherever we can until we understand what is happening.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
* Description: We are receiving disturbing reports from all over the galaxy. The disaster at Wiracoda Gate has sent the Progenitors into a frenzy! We must assist the defensive efforts wherever we can until we understand what is happening.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
* QuestLine: ql_event_halloween_2023_t2
* Type: Event
* EventId: event_halloween_2023_t2
* Goals:
	* Task 1: 10 ShipsDestroyedProgenitorT2_ShipsDestroyedProgenitorT3_ShipsDestroyedProgenitorT4

### qe_halloween_2023_day02_t2:
* Name: Gas refineries are being targeted by the Progenitors in many sectors of Nimbus. Stocks need to be replenished if the defenders are to hold off this calamity.

<color=#FBB03F>Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.</color>
* Description: Refineries are being targeted by the Progenitors in many sectors of Nimbus. Stocks need to be replenished if the defenders are to hold off this calamity.

<color=#FBB03F>Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
* QuestLine: ql_event_halloween_2023_t2
* Type: Event
* EventId: event_halloween_2023_t2
* Goals:
	* Task 1: GainItem

### qe_halloween_2023_day03_t2:
* Name: Gideon wants to collect any evidence which points to the Progenitor’s current activity. We should collect data from ships that were in combat with the abnormal Progenitor vessels.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
* Description: Gideon wants to collect any evidence which points to the Progenitor’s current activity. We should collect data from ships that were in combat with the abnormal Progenitor vessels.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
* QuestLine: ql_event_halloween_2023_t2
* Type: Event
* EventId: event_halloween_2023_t2
* Goals:
	* Task 1: GainItem

### qe_halloween_2023_day04_t2:
* Name: Many planets are still in desperate need of resources to hold off the Progenitors. Especially rare resources have been in high demand to increase defensive capabilities.

<color=#FBB03F>Rare earths are an occasional by-product of refining. They are required for upgrading modules.</color>
* Description: Many planets are still in desperate need of resources to hold off the Progenitors. Especially rare resources have been in high demand to increase defensive capabilities.

<color=#FBB03F>Rare earths are an occasional by-product of refining. They are required for upgrading modules.</color>
* QuestLine: ql_event_halloween_2023_t2
* Type: Event
* EventId: event_halloween_2023_t2
* Goals:
	* Task 1: GainItem

### qe_halloween_2023_day05_t2:
* Name: Gideon has identified a specific Progenitor component we must find in order to decrypt the errant Keeper's command frequency.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
* Description: Gideon has identified a specific Progenitor component we must find in order to decrypt the errant Keeper's command frequency.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
* QuestLine: ql_event_halloween_2023_t2
* Type: Event
* EventId: event_halloween_2023_t2
* Goals:
	* Task 1: GainItem

### qe_halloween_2023_day06_t2:
* Name: Many sectors have suffered heavy damages from the ongoing Progenitor attacks. More parts are needed to replenish the defending fleets.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
* Description: Many sectors have suffered heavy damages from the ongoing Progenitor attacks. More parts are needed to replenish the defending fleets.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
* QuestLine: ql_event_halloween_2023_t2
* Type: Event
* EventId: event_halloween_2023_t2
* Goals:
	* Task 1: Craft

### qe_halloween_2023_day07_t2:
* Name: In order for Gideon to triangulate the location of the errant Keeper we need to hunt down Progenitor vessels receiving its command signal.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
* Description: In order for Gideon to triangulate the location of the errant Keeper we need to hunt down Progenitor vessels receiving its command signal.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
* QuestLine: ql_event_halloween_2023_t2
* Type: Event
* EventId: event_halloween_2023_t2
* Goals:
	* Task 1: 10 ShipsDestroyedProgenitorT2_ShipsDestroyedProgenitorT3_ShipsDestroyedProgenitorT4

### qe_halloween_2023_day08_t2:
* Name: We are unsure what awaits us when we'll face the corrupted Keeper once again. Gideon has advised us to train our officers in Progenitor communication theory to effectively analyze the situation in the field.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* Description: We are unsure what awaits us when we'll face the corrupted Keeper once again. Gideon has advised us to train our officers in Progenitor communication theory to effectively analyze the situation in the field.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* QuestLine: ql_event_halloween_2023_t2
* Type: Event
* EventId: event_halloween_2023_t2
* Goals:
	* Task 1: UpgradeOfficer

### qe_halloween_2023_day09_t2:
* Name: In order to be fully prepared for the confrontation with the corrupted Keeper, we need to perform a fleet wide ready-check for all systems. We can engage enemies that have been preying on the local area lately due to the diminished security situation.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* Description: In order to be fully prepared for the confrontation with the corrupted Keeper, we need to perform a fleet wide ready-check for all systems. We can engage enemies that have been preying on the local area lately due to the diminished security situation.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* QuestLine: ql_event_halloween_2023_t2
* Type: Event
* EventId: event_halloween_2023_t2
* Goals:
	* Task 1: Complete side mission

### qe_halloween_2023_day10_t2:
* Name: The Iyatequa promised to negotiate a deal for safe passage into Cangacian space. However, even though the galaxy is at stake, the traders still insist on receiving a hefty price.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
* Description: The Iyatequa promised to negotiate a deal for safe passage into Cangacian space. However, even though the galaxy is at stake, the traders still insist on receiving a hefty price.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
* QuestLine: ql_event_halloween_2023_t2
* Type: Event
* EventId: event_halloween_2023_t2
* Goals:
	* Task 1: GainItem

### qe_halloween_2023_day11_t2:
* Name: We must confront the corrupted Keeper Malik and end the Progenitor incursion.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Description: We must confront the corrupted Keeper Malik and end the Progenitor incursion.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* QuestLine: ql_event_halloween_2023_t2
* Type: Event
* EventId: event_halloween_2023_t2
* Goals:
	* Task 1: Complete mission 'Rashidun T2'

## QL_EVENT_HALLOWEEN_2023_T3
### qe_halloween_2023_day01_t3:
* Name: We are receiving disturbing reports from all over the galaxy. The disaster at Wiracoda Gate has sent the Progenitors into a frenzy! We must assist the defensive efforts wherever we can until we understand what is happening.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
* Description: We are receiving disturbing reports from all over the galaxy. The disaster at Wiracoda Gate has sent the Progenitors into a frenzy! We must assist the defensive efforts wherever we can until we understand what is happening.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
* QuestLine: ql_event_halloween_2023_t3
* Type: Event
* EventId: event_halloween_2023_t3
* Goals:
	* Task 1: 10 ShipsDestroyedProgenitorT3_ShipsDestroyedProgenitorT4

### qe_halloween_2023_day02_t3:
* Name: Gas refineries are being targeted by the Progenitors in many sectors of Nimbus. Stocks need to be replenished if the defenders are to hold off this calamity.

<color=#FBB03F>Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.</color>
* Description: Gas refineries are being targeted by the Progenitors in many sectors of Nimbus. Stocks need to be replenished if the defenders are to hold off this calamity.

<color=#FBB03F>Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.</color>
* QuestLine: ql_event_halloween_2023_t3
* Type: Event
* EventId: event_halloween_2023_t3
* Goals:
	* Task 1: GainItem

### qe_halloween_2023_day03_t3:
* Name: Gideon wants to collect any evidence which points to the Progenitor’s current activity. We should collect data from ships that were in combat with the abnormal Progenitor vessels.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
* Description: Gideon wants to collect any evidence which points to the Progenitor’s current activity. We should collect data from ships that were in combat with the abnormal Progenitor vessels.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
* QuestLine: ql_event_halloween_2023_t3
* Type: Event
* EventId: event_halloween_2023_t3
* Goals:
	* Task 1: GainItem

### qe_halloween_2023_day04_t3:
* Name: Many planets are still in desperate need of resources to hold off the Progenitors. Especially rare resources have been in high demand to increase defensive capabilities.

<color=#FBB03F>Rare earths are an occasional by-product of refining. They are required for upgrading modules.</color>
* Description: Many planets are still in desperate need of resources to hold off the Progenitors. Especially rare resources have been in high demand to increase defensive capabilities.

<color=#FBB03F>Rare earths are an occasional by-product of refining. They are required for upgrading modules.</color>
* QuestLine: ql_event_halloween_2023_t3
* Type: Event
* EventId: event_halloween_2023_t3
* Goals:
	* Task 1: GainItem

### qe_halloween_2023_day05_t3:
* Name: Gideon has identified a specific Progenitor component we must find in order to decrypt the errant Keeper's command frequency.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
* Description: Gideon has identified a specific Progenitor component we must find in order to decrypt the errant Keeper's command frequency.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
* QuestLine: ql_event_halloween_2023_t3
* Type: Event
* EventId: event_halloween_2023_t3
* Goals:
	* Task 1: GainItem

### qe_halloween_2023_day06_t3:
* Name: Many sectors have suffered heavy damages from the ongoing Progenitor attacks. More parts are needed to replenish the defending fleets.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
* Description: Many sectors have suffered heavy damages from the ongoing Progenitor attacks. More parts are needed to replenish the defending fleets.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
* QuestLine: ql_event_halloween_2023_t3
* Type: Event
* EventId: event_halloween_2023_t3
* Goals:
	* Task 1: Craft

### qe_halloween_2023_day07_t3:
* Name: In order for Gideon to triangulate the location of the errant Keeper we need to hunt down Progenitor vessels receiving its command signal.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
* Description: In order for Gideon to triangulate the location of the errant Keeper we need to hunt down Progenitor vessels receiving its command signal.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
* QuestLine: ql_event_halloween_2023_t3
* Type: Event
* EventId: event_halloween_2023_t3
* Goals:
	* Task 1: 10 ShipsDestroyedProgenitorT3_ShipsDestroyedProgenitorT4

### qe_halloween_2023_day08_t3:
* Name: We are unsure what awaits us when we'll face the corrupted Keeper once again. Gideon has advised us to train our officers in Progenitor communication theory to effectively analyze the situation in the field.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* Description: We are unsure what awaits us when we'll face the corrupted Keeper once again. Gideon has advised us to train our officers in Progenitor communication theory to effectively analyze the situation in the field.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* QuestLine: ql_event_halloween_2023_t3
* Type: Event
* EventId: event_halloween_2023_t3
* Goals:
	* Task 1: UpgradeOfficer

### qe_halloween_2023_day09_t3:
* Name: In order to be fully prepared for the confrontation with the corrupted Keeper, we need to perform a fleet wide ready-check for all systems. We can engage enemies that have been preying on the local area lately due to the diminished security situation.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* Description: In order to be fully prepared for the confrontation with the corrupted Keeper, we need to perform a fleet wide ready-check for all systems. We can engage enemies that have been preying on the local area lately due to the diminished security situation.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* QuestLine: ql_event_halloween_2023_t3
* Type: Event
* EventId: event_halloween_2023_t3
* Goals:
	* Task 1: Complete 3 side missions

### qe_halloween_2023_day10_t3:
* Name: The Iyatequa promised to negotiate a deal for safe passage into Cangacian space. However, even though the galaxy is at stake, the traders still insist on receiving a hefty price.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
* Description: The Iyatequa promised to negotiate a deal for safe passage into Cangacian space. However, even though the galaxy is at stake, the traders still insist on receiving a hefty price.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
* QuestLine: ql_event_halloween_2023_t3
* Type: Event
* EventId: event_halloween_2023_t3
* Goals:
	* Task 1: GainItem

### qe_halloween_2023_day11_t3:
* Name: We must confront the corrupted Keeper Malik and end the Progenitor incursion.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Description: We must confront the corrupted Keeper Malik and end the Progenitor incursion.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* QuestLine: ql_event_halloween_2023_t3
* Type: Event
* EventId: event_halloween_2023_t3
* Goals:
	* Task 1: Complete mission 'Rashidun T3'

## QL_EVENT_HALLOWEEN_2023_T4
### qe_halloween_2023_day01_t4:
* Name: We are receiving disturbing reports from all over the galaxy. The disaster at Wiracoda Gate has sent the Progenitors into a frenzy! We must assist the defensive efforts wherever we can until we understand what is happening.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
* Description: We are receiving disturbing reports from all over the galaxy. The disaster at Wiracoda Gate has sent the Progenitors into a frenzy! We must assist the defensive efforts wherever we can until we understand what is happening.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
* QuestLine: ql_event_halloween_2023_t4
* Type: Event
* EventId: event_halloween_2023_t4
* Goals:
	* Task 1: 10 ShipsDestroyedProgenitorT4

### qe_halloween_2023_day02_t4:
* Name: Gas refineries are being targeted by the Progenitors in many sectors of Nimbus. Stocks need to be replenished if the defenders are to hold off this calamity.

<color=#FBB03F>Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.</color>
* Description: Gas refineries are being targeted by the Progenitors in many sectors of Nimbus. Stocks need to be replenished if the defenders are to hold off this calamity.

<color=#FBB03F>Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.</color>
* QuestLine: ql_event_halloween_2023_t4
* Type: Event
* EventId: event_halloween_2023_t4
* Goals:
	* Task 1: GainItem

### qe_halloween_2023_day03_t4:
* Name: Gideon wants to collect any evidence which points to the Progenitor’s current activity. We should collect data from ships that were in combat with the abnormal Progenitor vessels.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
* Description: Gideon wants to collect any evidence which points to the Progenitor’s current activity. We should collect data from ships that were in combat with the abnormal Progenitor vessels.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
* QuestLine: ql_event_halloween_2023_t4
* Type: Event
* EventId: event_halloween_2023_t4
* Goals:
	* Task 1: GainItem

### qe_halloween_2023_day04_t4:
* Name: Many planets are still in desperate need of resources to hold off the Progenitors. Especially rare resources have been in high demand to increase defensive capabilities.

<color=#FBB03F>Rare earths are an occasional by-product of refining. They are required for upgrading modules.</color>
* Description: Many planets are still in desperate need of resources to hold off the Progenitors. Especially rare resources have been in high demand to increase defensive capabilities.

<color=#FBB03F>Rare earths are an occasional by-product of refining. They are required for upgrading modules.</color>
* QuestLine: ql_event_halloween_2023_t4
* Type: Event
* EventId: event_halloween_2023_t4
* Goals:
	* Task 1: GainItem

### qe_halloween_2023_day05_t4:
* Name: Gideon has identified a specific Progenitor component we must find in order to decrypt the errant Keeper's command frequency.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
* Description: Gideon has identified a specific Progenitor component we must find in order to decrypt the errant Keeper's command frequency.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
* QuestLine: ql_event_halloween_2023_t4
* Type: Event
* EventId: event_halloween_2023_t4
* Goals:
	* Task 1: GainItem

### qe_halloween_2023_day06_t4:
* Name: Many sectors have suffered heavy damages from the ongoing Progenitor attacks. More parts are needed to replenish the defending fleets.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
* Description: Many sectors have suffered heavy damages from the ongoing Progenitor attacks. More parts are needed to replenish the defending fleets.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
* QuestLine: ql_event_halloween_2023_t4
* Type: Event
* EventId: event_halloween_2023_t4
* Goals:
	* Task 1: Craft

### qe_halloween_2023_day07_t4:
* Name: In order for Gideon to triangulate the location of the errant Keeper we need to hunt down Progenitor vessels receiving its command signal.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
* Description: In order for Gideon to triangulate the location of the errant Keeper we need to hunt down Progenitor vessels receiving its command signal.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
* QuestLine: ql_event_halloween_2023_t4
* Type: Event
* EventId: event_halloween_2023_t4
* Goals:
	* Task 1: 10 ShipsDestroyedProgenitorT4

### qe_halloween_2023_day08_t4:
* Name: We are unsure what awaits us when we'll face the corrupted Keeper once again. Gideon has advised us to train our officers in Progenitor communication theory to effectively analyze the situation in the field.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* Description: We are unsure what awaits us when we'll face the corrupted Keeper once again. Gideon has advised us to train our officers in Progenitor communication theory to effectively analyze the situation in the field.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* QuestLine: ql_event_halloween_2023_t4
* Type: Event
* EventId: event_halloween_2023_t4
* Goals:
	* Task 1: UpgradeOfficer

### qe_halloween_2023_day09_t4:
* Name: In order to be fully prepared for the confrontation with the corrupted Keeper, we need to perform a fleet wide ready-check for all systems. We can engage enemies that have been preying on the local area lately due to the diminished security situation.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* Description: In order to be fully prepared for the confrontation with the corrupted Keeper, we need to perform a fleet wide ready-check for all systems. We can engage enemies that have been preying on the local area lately due to the diminished security situation.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* QuestLine: ql_event_halloween_2023_t4
* Type: Event
* EventId: event_halloween_2023_t4
* Goals:
	* Task 1: Complete 5 side missions

### qe_halloween_2023_day10_t4:
* Name: The Iyatequa promised to negotiate a deal for safe passage into Cangacian space. However, even though the galaxy is at stake, the traders still insist on receiving a hefty price.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
* Description: The Iyatequa promised to negotiate a deal for safe passage into Cangacian space. However, even though the galaxy is at stake, the traders still insist on receiving a hefty price.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
* QuestLine: ql_event_halloween_2023_t4
* Type: Event
* EventId: event_halloween_2023_t4
* Goals:
	* Task 1: GainItem

### qe_halloween_2023_day11_t4:
* Name: We must confront the corrupted Keeper Malik and end the Progenitor incursion.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Description: We must confront the corrupted Keeper Malik and end the Progenitor incursion.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* QuestLine: ql_event_halloween_2023_t4
* Type: Event
* EventId: event_halloween_2023_t4
* Goals:
	* Task 1: Complete mission 'Rashidun T4'

## QL_EVENT_TANOCHWINTER_2023_T1
### qe_tanWin_2023_day01_t1:
* Name: Day 1: Resource Relief
* Description: We received priority communication from Lazarus Base. A subfaction of the Tanoch, the Chicuat, have made contact with Hiigaran representatives and requested aid. Fleet Command wants us to support the Chicuat and establish friendly ties. Our first task is to provide basic resources.

<color=#FBB03F>Ore can be mined from asteroids in asteroid fields. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
* QuestLine: ql_event_tanochWinter_2023_t1
* Type: Event
* EventId: event_tanochWinter_2023_t1
* MailsOnCompletion: m_tanWin_2023_d01_log
* Goals:
	* Task 1: GainItem

### qe_tanWin_2023_day02_t1:
* Name: Day 2: Processor Surrogate
* Description: The Chicuat infrastructure is badly degraded with age and suffered heavy damage in recent attacks. We're asked to refine materials to support their restoration efforts.

<color=#FBB03F>Rare earths are an occasional by-product of refining. They are required for upgrading modules.</color>
* QuestLine: ql_event_tanochWinter_2023_t1
* Type: Event
* EventId: event_tanochWinter_2023_t1
* Goals:
	* Task 1: GainItem

### qe_tanWin_2023_day03_t1:
* Name: Day 3: Wayward Cargo
* Description: The Chicuat have informed us several critical supply convoys have gone missing. We should try to retrieve any goods by hunting down local bandits.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
* QuestLine: ql_event_tanochWinter_2023_t1
* Type: Event
* EventId: event_tanochWinter_2023_t1
* Goals:
	* Task 1: GainItem

### qe_tanWin_2023_day04_t1:
* Name: Day 4: Relief Package
* Description: Ekekko, our Iyatequa liaison, has suggested to negotiate a trade deal with his contacts to support the Chicuat's need for basic supplies. We should sell some of our own items to get the traders interested.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
* QuestLine: ql_event_tanochWinter_2023_t1
* Type: Event
* EventId: event_tanochWinter_2023_t1
* Goals:
	* Task 1: GainItem

### qe_tanWin_2023_day05_t1:
* Name: Day 5: Gesture of Aid
* Description: We received emergency communication from the Chicuat Elders. They anticipate a raid on one of their remote trading stations. Toci asks us to take on the defense in order to relieve the weakened and overextended Chicuat forces.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* QuestLine: ql_event_tanochWinter_2023_t1
* Type: Event
* EventId: event_tanochWinter_2023_t1
* Goals:
	* Task 1: Complete mission 'Repulse Raid T1'

### qe_tanWin_2023_day06_t1:
* Name: Day 6: Imperial Appeal
* Description: We must find out whether the Tecuban really are behind the recent attacks on the Chicuat. Our contact in the Tanoch Empire might be able to provide information. We should do some assignments to show good faith.

<color=#FBB03F>There are different types of assignments available in your assignment log.</color>
* QuestLine: ql_event_tanochWinter_2023_t1
* Type: Event
* EventId: event_tanochWinter_2023_t1
* MailsOnCompletion: m_tanWin_2023_d06_log
* Goals:
	* Task 1: 5 T1up

### qe_tanWin_2023_day07_t1:
* Name: Day 7: Black Eye
* Description: Lazarus Base has processed Tepin Papan's information. There are reports about the rising influence of an ambitous leader named Heyoka. He is promoting expansionist ideas and has a particular disdain for the Chicuat. We should find out if the name is familiar in the criminal underworld here.

<color=#FBB03F>The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.</color>
* QuestLine: ql_event_tanochWinter_2023_t1
* Type: Event
* EventId: event_tanochWinter_2023_t1
* Goals:
	* Task 1: 15 ShipsDestroyedT1_ShipsDestroyedT2_ShipsDestroyedT3_ShipsDestroyedT4

### qe_tanWin_2023_day08_t1:
* Name: Day 8: Catch and Kill
* Description: Our investigations produced evidence for contact between the Tecuban leader Heyoka and high profile criminals. We must hunt down these outlaws to learn more.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* QuestLine: ql_event_tanochWinter_2023_t1
* Type: Event
* EventId: event_tanochWinter_2023_t1
* Goals:
	* Task 1: Complete side mission

### qe_tanWin_2023_day09_t1:
* Name: Day 9: Raise the Stakes
* Description: The Chicuat Elders have asked us to wait for their intelligence report on possible Tecuban forces within Acatla. In the meanwhile we should strengthen our forces to prepare for battle.

<color=#FBB03F>Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.</color>
* QuestLine: ql_event_tanochWinter_2023_t1
* Type: Event
* EventId: event_tanochWinter_2023_t1
* Goals:
	* Task 1: GainItem

### qe_tanWin_2023_day10_t1:
* Name: Day 10: In the Shadows
* Description: Intelligence from the Chicuat points to a Tecuban base operating around an uninhabited planet. We must go there and eliminate this base to stop the raids.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* QuestLine: ql_event_tanochWinter_2023_t1
* Type: Event
* EventId: event_tanochWinter_2023_t1
* Goals:
	* Task 1: Complete mission 'Base Busting T1'

### qe_tanWin_2023_day11_t1:
* Name: Day 11: Imperial Rumors
* Description: In order to gather information about the Vaygr's activity we must contact Tepin Papan once more. We should do some assignments to compensate him for his assistance.

<color=#FBB03F>There are different types of assignments available in your assignment log.</color>
* QuestLine: ql_event_tanochWinter_2023_t1
* Type: Event
* EventId: event_tanochWinter_2023_t1
* MailsOnCompletion: m_tanWin_2023_d11_log
* Goals:
	* Task 1: 5 T1up

### qe_tanWin_2023_day12_t1:
* Name: Day 12: Seek and Recover
* Description: While Tepin Papan is trying to gather information about the Vaygr's involvement with the Tecuban, we should scan some systems and see if we can find any clues about their whereabouts.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
* QuestLine: ql_event_tanochWinter_2023_t1
* Type: Event
* EventId: event_tanochWinter_2023_t1
* Goals:
	* Task 1: Scan

### qe_tanWin_2023_day13_t1:
* Name: Day 13: Among the People
* Description: We hope to learn more about the Vaygr's activity from the local people. We should do some good deeds around here to gain their trust.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.</color>
* QuestLine: ql_event_tanochWinter_2023_t1
* Type: Event
* EventId: event_tanochWinter_2023_t1
* Goals:
	* Task 1: GainItem

### qe_tanWin_2023_day14_t1:
* Name: Day 14: Active Search
* Description: Some local folks have agreed to provide information that could lead to the Vaygr. However, before they hand it over, they want us help them with a particularly challenging mission.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* QuestLine: ql_event_tanochWinter_2023_t1
* Type: Event
* EventId: event_tanochWinter_2023_t1
* Goals:
	* Task 1: Complete side mission

### qe_tanWin_2023_day15_t1:
* Name: Day 15: Hunting Party
* Description: We must hunt down a group of thugs that is suspected to be working for the Vaygr.

<color=#FBB03F>The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.</color>
* QuestLine: ql_event_tanochWinter_2023_t1
* Type: Event
* EventId: event_tanochWinter_2023_t1
* Goals:
	* Task 1: 15 ShipsDestroyedT1_ShipsDestroyedT2_ShipsDestroyedT3_ShipsDestroyedT4

### qe_tanWin_2023_day16_t1:
* Name: Day 16: Attack the Vaygr
* Description: In our search for the Vaygr involved with the Tecuban, we aquired one of their communication frequencies. If we contact the Vaygr now, we should be able to trace their signal and hyper jump to their exact location.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* QuestLine: ql_event_tanochWinter_2023_t1
* Type: Event
* EventId: event_tanochWinter_2023_t1
* Goals:
	* Task 1: Complete mission 'Destination T1'

### qe_tanWin_2023_day17_t1:
* Name: Day 17: Polite Inquiries
* Description: There is still no answer from Tepin Papan since we last spoke with him. We should do some more assignments to gain his attention and see if he was able to gather any information about the Vaygr's intentions.

<color=#FBB03F>There are different types of assignments available in your assignment log.</color>
* QuestLine: ql_event_tanochWinter_2023_t1
* Type: Event
* EventId: event_tanochWinter_2023_t1
* MailsOnCompletion: m_tanWin_2023_d17_log
* Goals:
	* Task 1: 5 T1up

### qe_tanWin_2023_day18_t1:
* Name: Day 18: Purchased Whispers
* Description: Ekekko wants us to trade on the local markets and see if we find someone who's willing to sell information on Jochik Kaan's motives.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
* QuestLine: ql_event_tanochWinter_2023_t1
* Type: Event
* EventId: event_tanochWinter_2023_t1
* Goals:
	* Task 1: GainItem

### qe_tanWin_2023_day19_t1:
* Name: Day 19: Getting There First
* Description: We contacted the Chicuat Elders and told them about Jochik Kaan's possible intention to obtain a particular Progenitor object. They have given us intel about a criminal organization that deals with Progenitor objects within the Tanoch Empire. We should investigate.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* QuestLine: ql_event_tanochWinter_2023_t1
* Type: Event
* EventId: event_tanochWinter_2023_t1
* Goals:
	* Task 1: Complete side mission

### qe_tanWin_2023_day20_t1:
* Name: Day 20: Providing Protection
* Description: While Gideon S'jet is researching the data set of Progenitor objects, the Chicuat Elders have informed us of a resurgance of Tecuban activity within their territory. We should support the defensive efforts.

<color=#FBB03F>The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.</color>
* QuestLine: ql_event_tanochWinter_2023_t1
* Type: Event
* EventId: event_tanochWinter_2023_t1
* Goals:
	* Task 1: 15 ShipsDestroyedT1_ShipsDestroyedT2_ShipsDestroyedT3_ShipsDestroyedT4

### qe_tanWin_2023_day21_t1:
* Name: Day 21: Hunt for Knowledge
* Description: Gideon S'jet's research into the data set of Progenitor objects turned out more difficult than expected. He asked us to support him to accelerate the process.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
* QuestLine: ql_event_tanochWinter_2023_t1
* Type: Event
* EventId: event_tanochWinter_2023_t1
* Goals:
	* Task 1: 10 ShipsDestroyedProgenitorT1_ShipsDestroyedProgenitorT2_ShipsDestroyedProgenitorT3_ShipsDestroyedProgenitorT4

### qe_tanWin_2023_day22_t1:
* Name: Day 22: Showdown at the Academy
* Description: We finally learned Jochik Kaan's intentions. He sparked the flames of war to weaken the Chicuat defenses and steal the Baetyl from Tlapallan Academy, one of their key centers of learning. We must travel there at once, before it is too late.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* QuestLine: ql_event_tanochWinter_2023_t1
* Type: Event
* EventId: event_tanochWinter_2023_t1
* MailsOnCompletion: m_tanWin_2023_d22_log
* Goals:
	* Task 1: Complete mission 'Tlapallan Academy T1'

## QL_EVENT_TANOCHWINTER_2023_T2
### qe_tanWin_2023_day01_t2:
* Name: We received priority communication from Lazarus Base. A subfaction of the Tanoch, the Chicuat, have made contact with Hiigaran representatives and requested aid. Fleet Command wants us to support the Chicuat and establish friendly ties. Our first task is to provide basic resources.

<color=#FBB03F>Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.</color>
* Description: We received priority communication from Lazarus Base. A subfaction of the Tanoch, the Chicuat, have made contact with Hiigaran representatives and requested aid. Fleet Command wants us to support the Chicuat and establish friendly ties. Our first task is to provide basic resources.

<color=#FBB03F>Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.</color>
* QuestLine: ql_event_tanochWinter_2023_t2
* Type: Event
* EventId: event_tanochWinter_2023_t2
* MailsOnCompletion: m_tanWin_2023_d01_log
* Goals:
	* Task 1: GainItem

### qe_tanWin_2023_day02_t2:
* Name: The Chicuat infrastructure is badly degraded with age and suffered heavy damage in recent attacks. We're asked to refine materials to support their restoration efforts.

<color=#FBB03F>Rare earths are an occasional by-product of refining. They are required for upgrading modules.</color>
* Description: The Chicuat infrastructure is badly degraded with age and suffered heavy damage in recent attacks. We're asked to refine materials to support their restoration efforts.

<color=#FBB03F>Rare earths are an occasional by-product of refining. They are required for upgrading modules.</color>
* QuestLine: ql_event_tanochWinter_2023_t2
* Type: Event
* EventId: event_tanochWinter_2023_t2
* Goals:
	* Task 1: GainItem

### qe_tanWin_2023_day03_t2:
* Name: The Chicuat have informed us several critical supply convoys have gone missing. We should try to retrieve any goods by hunting down local bandits.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
* Description: The Chicuat have informed us several critical supply convoys have gone missing. We should try to retrieve any goods by hunting down local bandits.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
* QuestLine: ql_event_tanochWinter_2023_t2
* Type: Event
* EventId: event_tanochWinter_2023_t2
* Goals:
	* Task 1: GainItem

### qe_tanWin_2023_day04_t2:
* Name: Ekekko, our Iyatequa liaison, has suggested to negotiate a trade deal with his contacts to support the Chicuat's need for basic supplies. We should sell some of our own items to get the traders interested.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
* Description: Ekekko, our Iyatequa liaison, has suggested to negotiate a trade deal with his contacts to support the Chicuat's need for basic supplies. We should sell some of our own items to get the traders interested.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
* QuestLine: ql_event_tanochWinter_2023_t2
* Type: Event
* EventId: event_tanochWinter_2023_t2
* Goals:
	* Task 1: GainItem

### qe_tanWin_2023_day05_t2:
* Name: We received emergency communication from the Chicuat Elders. They anticipate a raid on one of their remote trading stations. Toci asks us to take on the defense in order to relieve the weakened and overextended Chicuat forces.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Description: We received emergency communication from the Chicuat Elders. They anticipate a raid on one of their remote trading stations. Toci asks us to take on the defense in order to relieve the weakened and overextended Chicuat forces.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* QuestLine: ql_event_tanochWinter_2023_t2
* Type: Event
* EventId: event_tanochWinter_2023_t2
* Goals:
	* Task 1: Complete mission 'Repulse Raid T2'

### qe_tanWin_2023_day06_t2:
* Name: We must find out whether the Tecuban really are behind the recent attacks on the Chicuat. Our contact in the Tanoch Empire might be able to provide information. We should do some assignments to show good faith.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Description: We must find out whether the Tecuban really are behind the recent attacks on the Chicuat. Our contact in the Tanoch Empire might be able to provide information. We should do some assignments to show good faith.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* QuestLine: ql_event_tanochWinter_2023_t2
* Type: Event
* EventId: event_tanochWinter_2023_t2
* MailsOnCompletion: m_tanWin_2023_d06_log
* Goals:
	* Task 1: 5 Faction_Tanoch_T2up

### qe_tanWin_2023_day07_t2:
* Name: Lazarus Base has processed Tepin Papan's information. There are reports about the rising influence of an ambitous leader named Heyoka. He is promoting expansionist ideas and has a particular disdain for the Chicuat. We should find out if the name is familiar in the criminal underworld here.

<color=#FBB03F>Some Tanoch fleets have broken away from the Tanoch empire to pursue their own agenda. These renegades can be found in signals, prowling Yaot space to continue ancient feuds.</color>
* Description: Lazarus Base has processed Tepin Papan's information. There are reports about the rising influence of an ambitous leader named Heyoka. He is promoting expansionist ideas and has a particular disdain for the Chicuat. We should find out if the name is familiar in the criminal underworld here.

<color=#FBB03F>Some Tanoch fleets have broken away from the Tanoch empire to pursue their own agenda. These renegades can be found in signals, prowling Yaot space to continue ancient feuds.</color>
* QuestLine: ql_event_tanochWinter_2023_t2
* Type: Event
* EventId: event_tanochWinter_2023_t2
* Goals:
	* Task 1: 10 ShipsDestroyedTanochT2_ShipsDestroyedTanochT3_ShipsDestroyedTanochT4

### qe_tanWin_2023_day08_t2:
* Name: Our investigations produced evidence for contact between the Tecuban leader Heyoka and high profile criminals. We must hunt down these outlaws to learn more.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Description: Our investigations produced evidence for contact between the Tecuban leader Heyoka and high profile criminals. We must hunt down these outlaws to learn more.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* QuestLine: ql_event_tanochWinter_2023_t2
* Type: Event
* EventId: event_tanochWinter_2023_t2
* Goals:
	* Task 1: Complete side mission

### qe_tanWin_2023_day09_t2:
* Name: The Chicuat Elders have asked us to wait for their intelligence report on possible Tecuban forces within Acatla. In the meanwhile we should strengthen our forces to prepare for battle.

<color=#FBB03F>External modules, such as turrets or sensors, can be upgraded in the External Module screen which will increase their power. Upgrading one level costs credits and RE.</color>
* Description: The Chicuat Elders have asked us to wait for their intelligence report on possible Tecuban forces within Acatla. In the meanwhile we should strengthen our forces to prepare for battle.

<color=#FBB03F>External modules, such as turrets or sensors, can be upgraded in the External Module screen which will increase their power. Upgrading one level costs credits and RE.</color>
* QuestLine: ql_event_tanochWinter_2023_t2
* Type: Event
* EventId: event_tanochWinter_2023_t2
* Goals:
	* Task 1: Craft

### qe_tanWin_2023_day10_t2:
* Name: Intelligence from the Chicuat points to a Tecuban base operating around an uninhabited planet. We must go there and eliminate this base to stop the raids.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Description: Intelligence from the Chicuat points to a Tecuban base operating around an uninhabited planet. We must go there and eliminate this base to stop the raids.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* QuestLine: ql_event_tanochWinter_2023_t2
* Type: Event
* EventId: event_tanochWinter_2023_t2
* Goals:
	* Task 1: Complete mission 'Base Busting T2'

### qe_tanWin_2023_day11_t2:
* Name: In order to gather information about the Vaygr's activity we must contact Tepin Papan once more. We should do some assignments to compensate him for his assistance.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Description: In order to gather information about the Vaygr's activity we must contact Tepin Papan once more. We should do some assignments to compensate him for his assistance.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* QuestLine: ql_event_tanochWinter_2023_t2
* Type: Event
* EventId: event_tanochWinter_2023_t2
* MailsOnCompletion: m_tanWin_2023_d11_log
* Goals:
	* Task 1: 135 RepTanoch

### qe_tanWin_2023_day12_t2:
* Name: While Tepin Papan is trying to gather information about the Vaygr's involvement with the Tecuban, we should scan some systems and see if we can find any clues about their whereabouts.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
* Description: While Tepin Papan is trying to gather information about the Vaygr's involvement with the Tecuban, we should scan some systems and see if we can find any clues about their whereabouts.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
* QuestLine: ql_event_tanochWinter_2023_t2
* Type: Event
* EventId: event_tanochWinter_2023_t2
* Goals:
	* Task 1: Scan

### qe_tanWin_2023_day13_t2:
* Name: We hope to learn more about the Vaygr's activity from the local people. We should do some good deeds around here to gain their trust.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.</color>
* Description: We hope to learn more about the Vaygr's activity from the local people. We should do some good deeds around here to gain their trust.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.</color>
* QuestLine: ql_event_tanochWinter_2023_t2
* Type: Event
* EventId: event_tanochWinter_2023_t2
* Goals:
	* Task 1: GainItem

### qe_tanWin_2023_day14_t2:
* Name: Some local folks have agreed to provide information that could lead to the Vaygr. However, before they hand it over, they want us help them with a particularly challenging mission.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Description: Some local folks have agreed to provide information that could lead to the Vaygr. However, before they hand it over, they want us help them with a particularly challenging mission.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* QuestLine: ql_event_tanochWinter_2023_t2
* Type: Event
* EventId: event_tanochWinter_2023_t2
* Goals:
	* Task 1: Complete side mission

### qe_tanWin_2023_day15_t2:
* Name: We must hunt down a group of thugs that is suspected to be working for the Vaygr.

<color=#FBB03F>Some Tanoch fleets have broken away from the Tanoch empire to pursue their own agenda. These renegades can be found in signals, prowling Yaot space to continue ancient feuds.</color>
* Description: We must hunt down a group of thugs that is suspected to be working for the Vaygr.

<color=#FBB03F>Some Tanoch fleets have broken away from the Tanoch empire to pursue their own agenda. These renegades can be found in signals, prowling Yaot space to continue ancient feuds.</color>
* QuestLine: ql_event_tanochWinter_2023_t2
* Type: Event
* EventId: event_tanochWinter_2023_t2
* Goals:
	* Task 1: 10 ShipsDestroyedTanochT2_ShipsDestroyedTanochT3_ShipsDestroyedTanochT4

### qe_tanWin_2023_day16_t2:
* Name: In our search for the Vaygr involved with the Tecuban, we aquired one of their communication frequencies. If we contact the Vaygr now, we should be able to trace their signal and hyper jump to their exact location.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Description: In our search for the Vaygr involved with the Tecuban, we aquired one of their communication frequencies. If we contact the Vaygr now, we should be able to trace their signal and hyper jump to their exact location.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* QuestLine: ql_event_tanochWinter_2023_t2
* Type: Event
* EventId: event_tanochWinter_2023_t2
* Goals:
	* Task 1: Complete mission 'Destination T2'

### qe_tanWin_2023_day17_t2:
* Name: There is still no answer from Tepin Papan since we last spoke with him. We should do some more assignments to gain his attention and see if he was able to gather any information about the Vaygr's intentions.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Description: There is still no answer from Tepin Papan since we last spoke with him. We should do some more assignments to gain his attention and see if he was able to gather any information about the Vaygr's intentions.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* QuestLine: ql_event_tanochWinter_2023_t2
* Type: Event
* EventId: event_tanochWinter_2023_t2
* MailsOnCompletion: m_tanWin_2023_d17_log
* Goals:
	* Task 1: 5 Faction_Tanoch_T2up

### qe_tanWin_2023_day18_t2:
* Name: Ekekko wants us to trade on the local markets and see if we find someone who's willing to sell information on Jochik Kaan's motives.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
* Description: Ekekko wants us to trade on the local markets and see if we find someone who's willing to sell information on Jochik Kaan's motives.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
* QuestLine: ql_event_tanochWinter_2023_t2
* Type: Event
* EventId: event_tanochWinter_2023_t2
* Goals:
	* Task 1: GainItem

### qe_tanWin_2023_day19_t2:
* Name: We contacted the Chicuat Elders and told them about Jochik Kaan's possible intention to obtain a particular Progenitor object. They have given us intel about a criminal organization that deals with Progenitor objects within the Tanoch Empire. We should investigate.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Description: We contacted the Chicuat Elders and told them about Jochik Kaan's possible intention to obtain a particular Progenitor object. They have given us intel about a criminal organization that deals with Progenitor objects within the Tanoch Empire. We should investigate.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* QuestLine: ql_event_tanochWinter_2023_t2
* Type: Event
* EventId: event_tanochWinter_2023_t2
* Goals:
	* Task 1: Complete side mission

### qe_tanWin_2023_day20_t2:
* Name: While Gideon S'jet is researching the data set of Progenitor objects, the Chicuat Elders have informed us of a resurgance of Tecuban activity within their territory. We should support the defensive efforts.

<color=#FBB03F>Some Tanoch fleets have broken away from the Tanoch empire to pursue their own agenda. These renegades can be found in signals, prowling Yaot space to continue ancient feuds.</color>
* Description: While Gideon S'jet is researching the data set of Progenitor objects, the Chicuat Elders have informed us of a resurgance of Tecuban activity within their territory. We should support the defensive efforts.

<color=#FBB03F>Some Tanoch fleets have broken away from the Tanoch empire to pursue their own agenda. These renegades can be found in signals, prowling Yaot space to continue ancient feuds.</color>
* QuestLine: ql_event_tanochWinter_2023_t2
* Type: Event
* EventId: event_tanochWinter_2023_t2
* Goals:
	* Task 1: 10 ShipsDestroyedTanochT2_ShipsDestroyedTanochT3_ShipsDestroyedTanochT4

### qe_tanWin_2023_day21_t2:
* Name: Gideon S'jet's research into the data set of Progenitor objects turned out more difficult than expected. He asked us to support him to accelerate the process.

<color=#FBB03F>Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.</color>
* Description: Gideon S'jet's research into the data set of Progenitor objects turned out more difficult than expected. He asked us to support him to accelerate the process.

<color=#FBB03F>Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.</color>
* QuestLine: ql_event_tanochWinter_2023_t2
* Type: Event
* EventId: event_tanochWinter_2023_t2
* Goals:
	* Task 1: GainItem

### qe_tanWin_2023_day22_t2:
* Name: We finally learned Jochik Kaan's intentions. He sparked the flames of war to weaken the Chicuat defenses and steal the Baetyl from Tlapallan Academy, one of their key centers of learning. We must travel there at once, before it is too late.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Description: We finally learned Jochik Kaan's intentions. He sparked the flames of war to weaken the Chicuat defenses and steal the Baetyl from Tlapallan Academy, one of their key centers of learning. We must travel there at once, before it is too late.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* QuestLine: ql_event_tanochWinter_2023_t2
* Type: Event
* EventId: event_tanochWinter_2023_t2
* MailsOnCompletion: m_tanWin_2023_d22_log
* Goals:
	* Task 1: Complete mission 'Tlapallan Academy T2'

## QL_EVENT_TANOCHWINTER_2023_T3
### qe_tanWin_2023_day01_t3:
* Name: We received priority communication from Lazarus Base. A subfaction of the Tanoch, the Chicuat, have made contact with Hiigaran representatives and requested aid. Fleet Command wants us to support the Chicuat and establish friendly ties. Our first task is to provide basic resources.

<color=#FBB03F>Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.</color>
* Description: We received priority communication from Lazarus Base. A subfaction of the Tanoch, the Chicuat, have made contact with Hiigaran representatives and requested aid. Fleet Command wants us to support the Chicuat and establish friendly ties. Our first task is to provide basic resources.

<color=#FBB03F>Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.</color>
* QuestLine: ql_event_tanochWinter_2023_t3
* Type: Event
* EventId: event_tanochWinter_2023_t3
* MailsOnCompletion: m_tanWin_2023_d01_log
* Goals:
	* Task 1: GainItem

### qe_tanWin_2023_day02_t3:
* Name: The Chicuat infrastructure is badly degraded with age and suffered heavy damage in recent attacks. We're asked to refine materials to support their restoration efforts.

<color=#FBB03F>Rare earths are an occasional by-product of refining. They are required for upgrading modules.</color>
* Description: The Chicuat infrastructure is badly degraded with age and suffered heavy damage in recent attacks. We're asked to refine materials to support their restoration efforts.

<color=#FBB03F>Rare earths are an occasional by-product of refining. They are required for upgrading modules.</color>
* QuestLine: ql_event_tanochWinter_2023_t3
* Type: Event
* EventId: event_tanochWinter_2023_t3
* Goals:
	* Task 1: GainItem

### qe_tanWin_2023_day03_t3:
* Name: The Chicuat have informed us several critical supply convoys have gone missing. We should try to retrieve any goods by hunting down local bandits.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
* Description: The Chicuat have informed us several critical supply convoys have gone missing. We should try to retrieve any goods by hunting down local bandits.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
* QuestLine: ql_event_tanochWinter_2023_t3
* Type: Event
* EventId: event_tanochWinter_2023_t3
* Goals:
	* Task 1: GainItem

### qe_tanWin_2023_day04_t3:
* Name: Ekekko, our Iyatequa liaison, has suggested to negotiate a trade deal with his contacts to support the Chicuat's need for basic supplies. We should sell some of our own items to get the traders interested.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
* Description: Ekekko, our Iyatequa liaison, has suggested to negotiate a trade deal with his contacts to support the Chicuat's need for basic supplies. We should sell some of our own items to get the traders interested.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
* QuestLine: ql_event_tanochWinter_2023_t3
* Type: Event
* EventId: event_tanochWinter_2023_t3
* Goals:
	* Task 1: GainItem

### qe_tanWin_2023_day05_t3:
* Name: We received emergency communication from the Chicuat Elders. They anticipate a raid on one of their remote trading stations. Toci asks us to take on the defense in order to relieve the weakened and overextended Chicuat forces.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Description: We received emergency communication from the Chicuat Elders. They anticipate a raid on one of their remote trading stations. Toci asks us to take on the defense in order to relieve the weakened and overextended Chicuat forces.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* QuestLine: ql_event_tanochWinter_2023_t3
* Type: Event
* EventId: event_tanochWinter_2023_t3
* Goals:
	* Task 1: Complete mission 'Repulse Raid T3'

### qe_tanWin_2023_day06_t3:
* Name: We must find out whether the Tecuban really are behind the recent attacks on the Chicuat. Our contact in the Tanoch Empire might be able to provide information. We should do some assignments to show good faith.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Description: We must find out whether the Tecuban really are behind the recent attacks on the Chicuat. Our contact in the Tanoch Empire might be able to provide information. We should do some assignments to show good faith.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* QuestLine: ql_event_tanochWinter_2023_t3
* Type: Event
* EventId: event_tanochWinter_2023_t3
* MailsOnCompletion: m_tanWin_2023_d06_log
* Goals:
	* Task 1: 5 Faction_Tanoch_T3up

### qe_tanWin_2023_day07_t3:
* Name: Lazarus Base has processed Tepin Papan's information. There are reports about the rising influence of an ambitous leader named Heyoka. He is promoting expansionist ideas and has a particular disdain for the Chicuat. We should find out if the name is familiar in the criminal underworld here.

<color=#FBB03F>Some Tanoch fleets have broken away from the Tanoch empire to pursue their own agenda. These renegades can be found in signals, prowling Yaot space to continue ancient feuds.</color>
* Description: Lazarus Base has processed Tepin Papan's information. There are reports about the rising influence of an ambitous leader named Heyoka. He is promoting expansionist ideas and has a particular disdain for the Chicuat. We should find out if the name is familiar in the criminal underworld here.

<color=#FBB03F>Some Tanoch fleets have broken away from the Tanoch empire to pursue their own agenda. These renegades can be found in signals, prowling Yaot space to continue ancient feuds.</color>
* QuestLine: ql_event_tanochWinter_2023_t3
* Type: Event
* EventId: event_tanochWinter_2023_t3
* Goals:
	* Task 1: 10 ShipsDestroyedTanochT3_ShipsDestroyedTanochT4

### qe_tanWin_2023_day08_t3:
* Name: Our investigations produced evidence for contact between the Tecuban leader Heyoka and high profile criminals. We must hunt down these outlaws to learn more.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Description: Our investigations produced evidence for contact between the Tecuban leader Heyoka and high profile criminals. We must hunt down these outlaws to learn more.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* QuestLine: ql_event_tanochWinter_2023_t3
* Type: Event
* EventId: event_tanochWinter_2023_t3
* Goals:
	* Task 1: Complete side mission

### qe_tanWin_2023_day09_t3:
* Name: The Chicuat Elders have asked us to wait for their intelligence report on possible Tecuban forces within Acatla. In the meanwhile we should strengthen our forces to prepare for battle.

<color=#FBB03F>External modules, such as turrets or sensors, can be upgraded in the External Module screen which will increase their power. Upgrading one level costs credits and RE.</color>
* Description: The Chicuat Elders have asked us to wait for their intelligence report on possible Tecuban forces within Acatla. In the meanwhile we should strengthen our forces to prepare for battle.

<color=#FBB03F>External modules, such as turrets or sensors, can be upgraded in the External Module screen which will increase their power. Upgrading one level costs credits and RE.</color>
* QuestLine: ql_event_tanochWinter_2023_t3
* Type: Event
* EventId: event_tanochWinter_2023_t3
* Goals:
	* Task 1: Craft

### qe_tanWin_2023_day10_t3:
* Name: Intelligence from the Chicuat points to a Tecuban base operating around an uninhabited planet. We must go there and eliminate this base to stop the raids.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Description: Intelligence from the Chicuat points to a Tecuban base operating around an uninhabited planet. We must go there and eliminate this base to stop the raids.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* QuestLine: ql_event_tanochWinter_2023_t3
* Type: Event
* EventId: event_tanochWinter_2023_t3
* Goals:
	* Task 1: Complete mission 'Base Busting T3'

### qe_tanWin_2023_day11_t3:
* Name: In order to gather information about the Vaygr's activity we must contact Tepin Papan once more. We should do some assignments to compensate him for his assistance.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Description: In order to gather information about the Vaygr's activity we must contact Tepin Papan once more. We should do some assignments to compensate him for his assistance.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* QuestLine: ql_event_tanochWinter_2023_t3
* Type: Event
* EventId: event_tanochWinter_2023_t3
* MailsOnCompletion: m_tanWin_2023_d11_log
* Goals:
	* Task 1: 180 RepTanoch

### qe_tanWin_2023_day12_t3:
* Name: While Tepin Papan is trying to gather information about the Vaygr's involvement with the Tecuban, we should scan some systems and see if we can find any clues about their whereabouts.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
* Description: While Tepin Papan is trying to gather information about the Vaygr's involvement with the Tecuban, we should scan some systems and see if we can find any clues about their whereabouts.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
* QuestLine: ql_event_tanochWinter_2023_t3
* Type: Event
* EventId: event_tanochWinter_2023_t3
* Goals:
	* Task 1: Scan

### qe_tanWin_2023_day13_t3:
* Name: We hope to learn more about the Vaygr's activity from the local people. We should do some good deeds around here to gain their trust.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.</color>
* Description: We hope to learn more about the Vaygr's activity from the local people. We should do some good deeds around here to gain their trust.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.</color>
* QuestLine: ql_event_tanochWinter_2023_t3
* Type: Event
* EventId: event_tanochWinter_2023_t3
* Goals:
	* Task 1: GainItem

### qe_tanWin_2023_day14_t3:
* Name: Some local folks have agreed to provide information that could lead to the Vaygr. However, before they hand it over, they want us help them with a particularly challenging mission.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Description: Some local folks have agreed to provide information that could lead to the Vaygr. However, before they hand it over, they want us help them with a particularly challenging mission.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* QuestLine: ql_event_tanochWinter_2023_t3
* Type: Event
* EventId: event_tanochWinter_2023_t3
* Goals:
	* Task 1: Complete side mission

### qe_tanWin_2023_day15_t3:
* Name: We must hunt down a group of thugs that is suspected to be working for the Vaygr.

<color=#FBB03F>Some Tanoch fleets have broken away from the Tanoch empire to pursue their own agenda. These renegades can be found in signals, prowling Yaot space to continue ancient feuds.</color>
* Description: We must hunt down a group of thugs that is suspected to be working for the Vaygr.

<color=#FBB03F>Some Tanoch fleets have broken away from the Tanoch empire to pursue their own agenda. These renegades can be found in signals, prowling Yaot space to continue ancient feuds.</color>
* QuestLine: ql_event_tanochWinter_2023_t3
* Type: Event
* EventId: event_tanochWinter_2023_t3
* Goals:
	* Task 1: 10 ShipsDestroyedTanochT3_ShipsDestroyedTanochT4

### qe_tanWin_2023_day16_t3:
* Name: In our search for the Vaygr involved with the Tecuban, we aquired one of their communication frequencies. If we contact the Vaygr now, we should be able to trace their signal and hyper jump to their exact location.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Description: In our search for the Vaygr involved with the Tecuban, we aquired one of their communication frequencies. If we contact the Vaygr now, we should be able to trace their signal and hyper jump to their exact location.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* QuestLine: ql_event_tanochWinter_2023_t3
* Type: Event
* EventId: event_tanochWinter_2023_t3
* Goals:
	* Task 1: Complete mission 'Destination T3'

### qe_tanWin_2023_day17_t3:
* Name: There is still no answer from Tepin Papan since we last spoke with him. We should do some more assignments to gain his attention and see if he was able to gather any information about the Vaygr's intentions.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Description: There is still no answer from Tepin Papan since we last spoke with him. We should do some more assignments to gain his attention and see if he was able to gather any information about the Vaygr's intentions.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* QuestLine: ql_event_tanochWinter_2023_t3
* Type: Event
* EventId: event_tanochWinter_2023_t3
* MailsOnCompletion: m_tanWin_2023_d17_log
* Goals:
	* Task 1: 5 Faction_Tanoch_T3up

### qe_tanWin_2023_day18_t3:
* Name: Ekekko wants us to trade on the local markets and see if we find someone who's willing to sell information on Jochik Kaan's motives.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
* Description: Ekekko wants us to trade on the local markets and see if we find someone who's willing to sell information on Jochik Kaan's motives.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
* QuestLine: ql_event_tanochWinter_2023_t3
* Type: Event
* EventId: event_tanochWinter_2023_t3
* Goals:
	* Task 1: GainItem

### qe_tanWin_2023_day19_t3:
* Name: We contacted the Chicuat Elders and told them about Jochik Kaan's possible intention to obtain a particular Progenitor object. They have given us intel about a criminal organization that deals with Progenitor objects within the Tanoch Empire. We should investigate.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Description: We contacted the Chicuat Elders and told them about Jochik Kaan's possible intention to obtain a particular Progenitor object. They have given us intel about a criminal organization that deals with Progenitor objects within the Tanoch Empire. We should investigate.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* QuestLine: ql_event_tanochWinter_2023_t3
* Type: Event
* EventId: event_tanochWinter_2023_t3
* Goals:
	* Task 1: Complete side mission

### qe_tanWin_2023_day20_t3:
* Name: While Gideon S'jet is researching the data set of Progenitor objects, the Chicuat Elders have informed us of a resurgance of Tecuban activity within their territory. We should support the defensive efforts.

<color=#FBB03F>Some Tanoch fleets have broken away from the Tanoch empire to pursue their own agenda. These renegades can be found in signals, prowling Yaot space to continue ancient feuds.</color>
* Description: While Gideon S'jet is researching the data set of Progenitor objects, the Chicuat Elders have informed us of a resurgance of Tecuban activity within their territory. We should support the defensive efforts.

<color=#FBB03F>Some Tanoch fleets have broken away from the Tanoch empire to pursue their own agenda. These renegades can be found in signals, prowling Yaot space to continue ancient feuds.</color>
* QuestLine: ql_event_tanochWinter_2023_t3
* Type: Event
* EventId: event_tanochWinter_2023_t3
* Goals:
	* Task 1: 10 ShipsDestroyedTanochT3_ShipsDestroyedTanochT4

### qe_tanWin_2023_day21_t3:
* Name: Gideon S'jet's research into the data set of Progenitor objects turned out more difficult than expected. He asked us to support him to accelerate the process.

<color=#FBB03F>Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.</color>
* Description: Gideon S'jet's research into the data set of Progenitor objects turned out more difficult than expected. He asked us to support him to accelerate the process.

<color=#FBB03F>Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.</color>
* QuestLine: ql_event_tanochWinter_2023_t3
* Type: Event
* EventId: event_tanochWinter_2023_t3
* Goals:
	* Task 1: GainItem

### qe_tanWin_2023_day22_t3:
* Name: We finally learned Jochik Kaan's intentions. He sparked the flames of war to weaken the Chicuat defenses and steal the Baetyl from Tlapallan Academy, one of their key centers of learning. We must travel there at once, before it is too late.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Description: We finally learned Jochik Kaan's intentions. He sparked the flames of war to weaken the Chicuat defenses and steal the Baetyl from Tlapallan Academy, one of their key centers of learning. We must travel there at once, before it is too late.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* QuestLine: ql_event_tanochWinter_2023_t3
* Type: Event
* EventId: event_tanochWinter_2023_t3
* MailsOnCompletion: m_tanWin_2023_d22_log
* Goals:
	* Task 1: Complete mission 'Tlapallan Academy T3'

## QL_EVENT_TANOCHWINTER_2023_T4
### qe_tanWin_2023_day01_t4:
* Name: We received priority communication from Lazarus Base. A subfaction of the Tanoch, the Chicuat, have made contact with Hiigaran representatives and requested aid. Fleet Command wants us to support the Chicuat and establish friendly ties. Our first task is to provide basic resources.

<color=#FBB03F>Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.</color>
* Description: We received priority communication from Lazarus Base. A subfaction of the Tanoch, the Chicuat, have made contact with Hiigaran representatives and requested aid. Fleet Command wants us to support the Chicuat and establish friendly ties. Our first task is to provide basic resources.

<color=#FBB03F>Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.</color>
* QuestLine: ql_event_tanochWinter_2023_t4
* Type: Event
* EventId: event_tanochWinter_2023_t4
* MailsOnCompletion: m_tanWin_2023_d01_log
* Goals:
	* Task 1: GainItem

### qe_tanWin_2023_day02_t4:
* Name: The Chicuat infrastructure is badly degraded with age and suffered heavy damage in recent attacks. We're asked to refine materials to support their restoration efforts.

<color=#FBB03F>Rare earths are an occasional by-product of refining. They are required for upgrading modules.</color>
* Description: The Chicuat infrastructure is badly degraded with age and suffered heavy damage in recent attacks. We're asked to refine materials to support their restoration efforts.

<color=#FBB03F>Rare earths are an occasional by-product of refining. They are required for upgrading modules.</color>
* QuestLine: ql_event_tanochWinter_2023_t4
* Type: Event
* EventId: event_tanochWinter_2023_t4
* Goals:
	* Task 1: GainItem

### qe_tanWin_2023_day03_t4:
* Name: The Chicuat have informed us several critical supply convoys have gone missing. We should try to retrieve any goods by hunting down local bandits.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
* Description: The Chicuat have informed us several critical supply convoys have gone missing. We should try to retrieve any goods by hunting down local bandits.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
* QuestLine: ql_event_tanochWinter_2023_t4
* Type: Event
* EventId: event_tanochWinter_2023_t4
* Goals:
	* Task 1: GainItem

### qe_tanWin_2023_day04_t4:
* Name: Ekekko, our Iyatequa liaison, has suggested to negotiate a trade deal with his contacts to support the Chicuat's need for basic supplies. We should sell some of our own items to get the traders interested.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
* Description: Ekekko, our Iyatequa liaison, has suggested to negotiate a trade deal with his contacts to support the Chicuat's need for basic supplies. We should sell some of our own items to get the traders interested.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
* QuestLine: ql_event_tanochWinter_2023_t4
* Type: Event
* EventId: event_tanochWinter_2023_t4
* Goals:
	* Task 1: GainItem

### qe_tanWin_2023_day05_t4:
* Name: We received emergency communication from the Chicuat Elders. They anticipate a raid on one of their remote trading stations. Toci asks us to take on the defense in order to relieve the weakened and overextended Chicuat forces.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Description: We received emergency communication from the Chicuat Elders. They anticipate a raid on one of their remote trading stations. Toci asks us to take on the defense in order to relieve the weakened and overextended Chicuat forces.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* QuestLine: ql_event_tanochWinter_2023_t4
* Type: Event
* EventId: event_tanochWinter_2023_t4
* Goals:
	* Task 1: Complete mission 'Repulse Raid T4'

### qe_tanWin_2023_day06_t4:
* Name: We must find out whether the Tecuban really are behind the recent attacks on the Chicuat. Our contact in the Tanoch Empire might be able to provide information. We should do some assignments to show good faith.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Description: We must find out whether the Tecuban really are behind the recent attacks on the Chicuat. Our contact in the Tanoch Empire might be able to provide information. We should do some assignments to show good faith.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* QuestLine: ql_event_tanochWinter_2023_t4
* Type: Event
* EventId: event_tanochWinter_2023_t4
* MailsOnCompletion: m_tanWin_2023_d06_log
* Goals:
	* Task 1: 5 Faction_Tanoch_T4up

### qe_tanWin_2023_day07_t4:
* Name: Lazarus Base has processed Tepin Papan's information. There are reports about the rising influence of an ambitous leader named Heyoka. He is promoting expansionist ideas and has a particular disdain for the Chicuat. We should find out if the name is familiar in the criminal underworld here.

<color=#FBB03F>Some Tanoch fleets have broken away from the Tanoch empire to pursue their own agenda. These renegades can be found in signals, prowling Yaot space to continue ancient feuds.</color>
* Description: Lazarus Base has processed Tepin Papan's information. There are reports about the rising influence of an ambitous leader named Heyoka. He is promoting expansionist ideas and has a particular disdain for the Chicuat. We should find out if the name is familiar in the criminal underworld here.

<color=#FBB03F>Some Tanoch fleets have broken away from the Tanoch empire to pursue their own agenda. These renegades can be found in signals, prowling Yaot space to continue ancient feuds.</color>
* QuestLine: ql_event_tanochWinter_2023_t4
* Type: Event
* EventId: event_tanochWinter_2023_t4
* Goals:
	* Task 1: 10 ShipsDestroyedTanochT4

### qe_tanWin_2023_day08_t4:
* Name: Our investigations produced evidence for contact between the Tecuban leader Heyoka and high profile criminals. We must hunt down these outlaws to learn more.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Description: Our investigations produced evidence for contact between the Tecuban leader Heyoka and high profile criminals. We must hunt down these outlaws to learn more.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* QuestLine: ql_event_tanochWinter_2023_t4
* Type: Event
* EventId: event_tanochWinter_2023_t4
* Goals:
	* Task 1: Complete side mission

### qe_tanWin_2023_day09_t4:
* Name: The Chicuat Elders have asked us to wait for their intelligence report on possible Tecuban forces within Acatla. In the meanwhile we should strengthen our forces to prepare for battle.

<color=#FBB03F>External modules, such as turrets or sensors, can be upgraded in the External Module screen which will increase their power. Upgrading one level costs credits and RE.</color>
* Description: The Chicuat Elders have asked us to wait for their intelligence report on possible Tecuban forces within Acatla. In the meanwhile we should strengthen our forces to prepare for battle.

<color=#FBB03F>External modules, such as turrets or sensors, can be upgraded in the External Module screen which will increase their power. Upgrading one level costs credits and RE.</color>
* QuestLine: ql_event_tanochWinter_2023_t4
* Type: Event
* EventId: event_tanochWinter_2023_t4
* Goals:
	* Task 1: Craft

### qe_tanWin_2023_day10_t4:
* Name: Intelligence from the Chicuat points to a Tecuban base operating around an uninhabited planet. We must go there and eliminate this base to stop the raids.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Description: Intelligence from the Chicuat points to a Tecuban base operating around an uninhabited planet. We must go there and eliminate this base to stop the raids.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* QuestLine: ql_event_tanochWinter_2023_t4
* Type: Event
* EventId: event_tanochWinter_2023_t4
* Goals:
	* Task 1: Complete mission 'Base Busting T4'

### qe_tanWin_2023_day11_t4:
* Name: In order to gather information about the Vaygr's activity we must contact Tepin Papan once more. We should do some assignments to compensate him for his assistance.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Description: In order to gather information about the Vaygr's activity we must contact Tepin Papan once more. We should do some assignments to compensate him for his assistance.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* QuestLine: ql_event_tanochWinter_2023_t4
* Type: Event
* EventId: event_tanochWinter_2023_t4
* MailsOnCompletion: m_tanWin_2023_d11_log
* Goals:
	* Task 1: 225 RepTanoch

### qe_tanWin_2023_day12_t4:
* Name: While Tepin Papan is trying to gather information about the Vaygr's involvement with the Tecuban, we should scan some systems and see if we can find any clues about their whereabouts.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
* Description: While Tepin Papan is trying to gather information about the Vaygr's involvement with the Tecuban, we should scan some systems and see if we can find any clues about their whereabouts.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
* QuestLine: ql_event_tanochWinter_2023_t4
* Type: Event
* EventId: event_tanochWinter_2023_t4
* Goals:
	* Task 1: Scan

### qe_tanWin_2023_day13_t4:
* Name: We hope to learn more about the Vaygr's activity from the local people. We should do some good deeds around here to gain their trust.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.</color>
* Description: We hope to learn more about the Vaygr's activity from the local people. We should do some good deeds around here to gain their trust.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.</color>
* QuestLine: ql_event_tanochWinter_2023_t4
* Type: Event
* EventId: event_tanochWinter_2023_t4
* Goals:
	* Task 1: GainItem

### qe_tanWin_2023_day14_t4:
* Name: Some local folks have agreed to provide information that could lead to the Vaygr. However, before they hand it over, they want us help them with a particularly challenging mission.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Description: Some local folks have agreed to provide information that could lead to the Vaygr. However, before they hand it over, they want us help them with a particularly challenging mission.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* QuestLine: ql_event_tanochWinter_2023_t4
* Type: Event
* EventId: event_tanochWinter_2023_t4
* Goals:
	* Task 1: Complete side mission

### qe_tanWin_2023_day15_t4:
* Name: We must hunt down a group of thugs that is suspected to be working for the Vaygr.

<color=#FBB03F>Some Tanoch fleets have broken away from the Tanoch empire to pursue their own agenda. These renegades can be found in signals, prowling Yaot space to continue ancient feuds.</color>
* Description: We must hunt down a group of thugs that is suspected to be working for the Vaygr.

<color=#FBB03F>Some Tanoch fleets have broken away from the Tanoch empire to pursue their own agenda. These renegades can be found in signals, prowling Yaot space to continue ancient feuds.</color>
* QuestLine: ql_event_tanochWinter_2023_t4
* Type: Event
* EventId: event_tanochWinter_2023_t4
* Goals:
	* Task 1: 10 ShipsDestroyedTanochT4

### qe_tanWin_2023_day16_t4:
* Name: In our search for the Vaygr involved with the Tecuban, we aquired one of their communication frequencies. If we contact the Vaygr now, we should be able to trace their signal and hyper jump to their exact location.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Description: In our search for the Vaygr involved with the Tecuban, we aquired one of their communication frequencies. If we contact the Vaygr now, we should be able to trace their signal and hyper jump to their exact location.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* QuestLine: ql_event_tanochWinter_2023_t4
* Type: Event
* EventId: event_tanochWinter_2023_t4
* Goals:
	* Task 1: Complete mission 'Destination T4'

### qe_tanWin_2023_day17_t4:
* Name: There is still no answer from Tepin Papan since we last spoke with him. We should do some more assignments to gain his attention and see if he was able to gather any information about the Vaygr's intentions.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Description: There is still no answer from Tepin Papan since we last spoke with him. We should do some more assignments to gain his attention and see if he was able to gather any information about the Vaygr's intentions.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* QuestLine: ql_event_tanochWinter_2023_t4
* Type: Event
* EventId: event_tanochWinter_2023_t4
* MailsOnCompletion: m_tanWin_2023_d17_log
* Goals:
	* Task 1: 5 Faction_Tanoch_T4up

### qe_tanWin_2023_day18_t4:
* Name: Ekekko wants us to trade on the local markets and see if we find someone who's willing to sell information on Jochik Kaan's motives.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
* Description: Ekekko wants us to trade on the local markets and see if we find someone who's willing to sell information on Jochik Kaan's motives.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
* QuestLine: ql_event_tanochWinter_2023_t4
* Type: Event
* EventId: event_tanochWinter_2023_t4
* Goals:
	* Task 1: GainItem

### qe_tanWin_2023_day19_t4:
* Name: We contacted the Chicuat Elders and told them about Jochik Kaan's possible intention to obtain a particular Progenitor object. They have given us intel about a criminal organization that deals with Progenitor objects within the Tanoch Empire. We should investigate.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Description: We contacted the Chicuat Elders and told them about Jochik Kaan's possible intention to obtain a particular Progenitor object. They have given us intel about a criminal organization that deals with Progenitor objects within the Tanoch Empire. We should investigate.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* QuestLine: ql_event_tanochWinter_2023_t4
* Type: Event
* EventId: event_tanochWinter_2023_t4
* Goals:
	* Task 1: Complete side mission

### qe_tanWin_2023_day20_t4:
* Name: While Gideon S'jet is researching the data set of Progenitor objects, the Chicuat Elders have informed us of a resurgance of Tecuban activity within their territory. We should support the defensive efforts.

<color=#FBB03F>Some Tanoch fleets have broken away from the Tanoch empire to pursue their own agenda. These renegades can be found in signals, prowling Yaot space to continue ancient feuds.</color>
* Description: While Gideon S'jet is researching the data set of Progenitor objects, the Chicuat Elders have informed us of a resurgance of Tecuban activity within their territory. We should support the defensive efforts.

<color=#FBB03F>Some Tanoch fleets have broken away from the Tanoch empire to pursue their own agenda. These renegades can be found in signals, prowling Yaot space to continue ancient feuds.</color>
* QuestLine: ql_event_tanochWinter_2023_t4
* Type: Event
* EventId: event_tanochWinter_2023_t4
* Goals:
	* Task 1: 10 ShipsDestroyedTanochT4

### qe_tanWin_2023_day21_t4:
* Name: Gideon S'jet's research into the data set of Progenitor objects turned out more difficult than expected. He asked us to support him to accelerate the process.

<color=#FBB03F>Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.</color>
* Description: Gideon S'jet's research into the data set of Progenitor objects turned out more difficult than expected. He asked us to support him to accelerate the process.

<color=#FBB03F>Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.</color>
* QuestLine: ql_event_tanochWinter_2023_t4
* Type: Event
* EventId: event_tanochWinter_2023_t4
* Goals:
	* Task 1: GainItem

### qe_tanWin_2023_day22_t4:
* Name: We finally learned Jochik Kaan's intentions. He sparked the flames of war to weaken the Chicuat defenses and steal the Baetyl from Tlapallan Academy, one of their key centers of learning. We must travel there at once, before it is too late.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Description: We finally learned Jochik Kaan's intentions. He sparked the flames of war to weaken the Chicuat defenses and steal the Baetyl from Tlapallan Academy, one of their key centers of learning. We must travel there at once, before it is too late.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* QuestLine: ql_event_tanochWinter_2023_t4
* Type: Event
* EventId: event_tanochWinter_2023_t4
* MailsOnCompletion: m_tanWin_2023_d22_log
* Goals:
	* Task 1: Complete mission 'Tlapallan Academy T4'

## QL_7DAYS_2023_08_DAY1_T1
### qe_7days_2023_08_day1_a_t1:
* Name: Day 1: Lay of the Land
* Description: Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.
* QuestLine: ql_7days_2023_08_day1_t1
* Type: Event
* EventId: event_7days_2023_08_21_t1
* Goals:
	* Task 1: Scan

### qe_7days_2023_08_day1_b_t1:
* Name: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Description: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* QuestLine: ql_7days_2023_08_day1_t1
* Type: Event
* EventId: event_7days_2023_08_21_t1
* Goals:
	* Task 1: 15 ShipsDestroyedT1_ShipsDestroyedT2_ShipsDestroyedT3_ShipsDestroyedT4

### qe_7days_2023_08_day1_c_t1:
* Name: Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.
* Description: Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.
* QuestLine: ql_7days_2023_08_day1_t1
* Type: Event
* EventId: event_7days_2023_08_21_t1
* Goals:
	* Task 1: GainItem

### qe_7days_2023_08_day1_d_t1:
* Name: Rare earths are an occasional by-product of refining. They are required for upgrading modules.
* Description: Rare earths are an occasional by-product of refining. They are required for upgrading modules.
* QuestLine: ql_7days_2023_08_day1_t1
* Type: Event
* EventId: event_7days_2023_08_21_t1
* Goals:
	* Task 1: GainItem

## QL_7DAYS_2023_08_DAY2_T1
### qe_7days_2023_08_day2_a_t1:
* Name: Day 2: Meet & Greet
* Description: There are different types of assignments available in your assignment log.
* QuestLine: ql_7days_2023_08_day2_t1
* Type: Event
* EventId: event_7days_2023_08_21_t1
* Goals:
	* Task 1: 5 T1up

### qe_7days_2023_08_day2_b_t1:
* Name: Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.
* Description: During missions you will usually fight against enemy ships. They can be part of an assignment, or they can be found as signals through scanning.
* QuestLine: ql_7days_2023_08_day2_t1
* Type: Event
* EventId: event_7days_2023_08_21_t1
* Goals:
	* Task 1: Complete 3 side missions

### qe_7days_2023_08_day2_c_t1:
* Name: Complete liaison assignments to gain reputation for that faction. A higher reputation unlocks more items in that faction's liaison requisitions office.
* Description: Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.
* QuestLine: ql_7days_2023_08_day2_t1
* Type: Event
* EventId: event_7days_2023_08_21_t1
* Goals:
	* Task 1: GainItem

### qe_7days_2023_08_day2_d_t1:
* Name: Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* Description: Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* QuestLine: ql_7days_2023_08_day2_t1
* Type: Event
* EventId: event_7days_2023_08_21_t1
* Goals:
	* Task 1: UpgradeOfficer

## QL_7DAYS_2023_08_DAY3_T1
### qe_7days_2023_08_day3_a_t1:
* Name: Day 3: Raw Materials
* Description: Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.
* QuestLine: ql_7days_2023_08_day3_t1
* Type: Event
* EventId: event_7days_2023_08_21_t1
* Goals:
	* Task 1: GainItem

### qe_7days_2023_08_day3_b_t1:
* Name: Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.
* Description: Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.
* QuestLine: ql_7days_2023_08_day3_t1
* Type: Event
* EventId: event_7days_2023_08_21_t1
* Goals:
	* Task 1: Craft

### qe_7days_2023_08_day3_c_t1:
* Name: Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.
* Description: Small items such as strike craft, modules and parts can be built in the fabricator. Larger items such as escort ships and flagships must be constructed at shipyards provided at larger stations.
* QuestLine: ql_7days_2023_08_day3_t1
* Type: Event
* EventId: event_7days_2023_08_21_t1
* Goals:
	* Task 1: Craft

### qe_7days_2023_08_day3_d_t1:
* Name: Items and resources can be sold for credits in the market at stations.
* Description: Items and resources can be sold for credits in the market at stations.
* QuestLine: ql_7days_2023_08_day3_t1
* Type: Event
* EventId: event_7days_2023_08_21_t1
* Goals:
	* Task 1: GainItem

## QL_7DAYS_2023_08_DAY4_T1
### qe_7days_2023_08_day4_a_t1:
* Name: Day 4: Hypothesis
* Description: Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
* QuestLine: ql_7days_2023_08_day4_t1
* Type: Event
* EventId: event_7days_2023_08_21_t1
* Goals:
	* Task 1: Complete 3 side missions

### qe_7days_2023_08_day4_b_t1:
* Name: Progenitor relics can be found in relic signature signals. Relics can be sold on the market for credits, though some liaison offices may be interested in relics as well.
* Description: Progenitor relics can be found in relic signature signals. Relics can be sold on the market for credits, though some liaison offices may be interested in relics as well.
* QuestLine: ql_7days_2023_08_day4_t1
* Type: Event
* EventId: event_7days_2023_08_21_t1
* Goals:
	* Task 1: GainItem

### qe_7days_2023_08_day4_c_t1:
* Name: Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.
* Description: Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.
* QuestLine: ql_7days_2023_08_day4_t1
* Type: Event
* EventId: event_7days_2023_08_21_t1
* Goals:
	* Task 1: 7 ShipsDestroyedProgenitorT1_ShipsDestroyedProgenitorT2_ShipsDestroyedProgenitorT3_ShipsDestroyedProgenitorT4

### qe_7days_2023_08_day4_d_t1:
* Name: Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.
* Description: Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.
* QuestLine: ql_7days_2023_08_day4_t1
* Type: Event
* EventId: event_7days_2023_08_21_t1
* Goals:
	* Task 1: Complete side mission

## QL_7DAYS_2023_08_DAY5_T1
### qe_7days_2023_08_day5_a_t1:
* Name: Day 5: Lessons
* Description: Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
* QuestLine: ql_7days_2023_08_day5_t1
* Type: Event
* EventId: event_7days_2023_08_21_t1
* Goals:
	* Task 1: Complete 3 side missions

### qe_7days_2023_08_day5_b_t1:
* Name: Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.
* Description: Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.
* QuestLine: ql_7days_2023_08_day5_t1
* Type: Event
* EventId: event_7days_2023_08_21_t1
* Goals:
	* Task 1: GainItem

### qe_7days_2023_08_day5_c_t1:
* Name: Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* Description: Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* QuestLine: ql_7days_2023_08_day5_t1
* Type: Event
* EventId: event_7days_2023_08_21_t1
* Goals:
	* Task 1: UpgradeOfficer

### qe_7days_2023_08_day5_d_t1:
* Name: Discharging officers grants credits and insignias, which can be used to level up other officers.
* Description: Discharging officers grants credits and insignias, which can be used to level up other officers.
* QuestLine: ql_7days_2023_08_day5_t1
* Type: Event
* EventId: event_7days_2023_08_21_t1
* Goals:
	* Task 1: GainItem

## QL_7DAYS_2023_08_DAY6_T1
### qe_7days_2023_08_day6_a_t1:
* Name: Day 6: Stockpile
* Description: Rare earths are an occasional by-product of refining. They are required for upgrading modules.
* QuestLine: ql_7days_2023_08_day6_t1
* Type: Event
* EventId: event_7days_2023_08_21_t1
* Goals:
	* Task 1: GainItem

### qe_7days_2023_08_day6_b_t1:
* Name: The strength of modules can be increased through upgrades, which cost rare earths.
* Description: Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* QuestLine: ql_7days_2023_08_day6_t1
* Type: Event
* EventId: event_7days_2023_08_21_t1
* Goals:
	* Task 1: UpgradeOfficer

### qe_7days_2023_08_day6_c_t1:
* Name: The strength of modules can be increased through upgrades, which cost rare earths.
* Description: Small items such as strike craft, modules and parts can be built in the fabricator. Larger items such as escort ships and flagships must be constructed at shipyards provided at larger stations.
* QuestLine: ql_7days_2023_08_day6_t1
* Type: Event
* EventId: event_7days_2023_08_21_t1
* Goals:
	* Task 1: Craft

### qe_7days_2023_08_day6_d_t1:
* Name: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Description: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* QuestLine: ql_7days_2023_08_day6_t1
* Type: Event
* EventId: event_7days_2023_08_21_t1
* Goals:
	* Task 1: 15 ShipsDestroyedT1_ShipsDestroyedT2_ShipsDestroyedT3_ShipsDestroyedT4

## QL_7DAYS_2023_08_DAY7_T1
### qe_7days_2023_08_day7_a_t1:
* Name: Day 7: Enemy Contact
* Description: Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
* QuestLine: ql_7days_2023_08_day7_t1
* Type: Event
* EventId: event_7days_2023_08_21_t1
* Goals:
	* Task 1: Complete 3 side missions

### qe_7days_2023_08_day7_b_t1:
* Name: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Description: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* QuestLine: ql_7days_2023_08_day7_t1
* Type: Event
* EventId: event_7days_2023_08_21_t1
* Goals:
	* Task 1: 15 ShipsDestroyedT1_ShipsDestroyedT2_ShipsDestroyedT3_ShipsDestroyedT4

### qe_7days_2023_08_day7_c_t1:
* Name: When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.
* Description: When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.
* QuestLine: ql_7days_2023_08_day7_t1
* Type: Event
* EventId: event_7days_2023_08_21_t1
* Goals:
	* Task 1: GainItem

### qe_7days_2023_08_day7_d_t1:
* Name: Strikes are difficult missions that require a strong fleet from several commanders to beat. Completing a strike rewards code fragments, which can be turned in for special blueprints.
* Description: Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
* QuestLine: ql_7days_2023_08_day7_t1
* Type: Event
* EventId: event_7days_2023_08_21_t1
* Goals:
	* Task 1: Complete 3 side missions

## QL_7DAYS_2023_08_DAY1_T2
### qe_7days_2023_08_day1_a_t2:
* Name: Day 1: Lay of the Land
* Description: Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.
* QuestLine: ql_7days_2023_08_day1_t2
* Type: Event
* EventId: event_7days_2023_08_21_t2
* Goals:
	* Task 1: Scan

### qe_7days_2023_08_day1_b_t2:
* Name: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Description: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* QuestLine: ql_7days_2023_08_day1_t2
* Type: Event
* EventId: event_7days_2023_08_21_t2
* Goals:
	* Task 1: 15 ShipsDestroyedT2_ShipsDestroyedT3_ShipsDestroyedT4

### qe_7days_2023_08_day1_c_t2:
* Name: Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.
* Description: Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.
* QuestLine: ql_7days_2023_08_day1_t2
* Type: Event
* EventId: event_7days_2023_08_21_t2
* Goals:
	* Task 1: GainItem

### qe_7days_2023_08_day1_d_t2:
* Name: Rare earths are an occasional by-product of refining. They are required for upgrading modules.
* Description: Rare earths are an occasional by-product of refining. They are required for upgrading modules.
* QuestLine: ql_7days_2023_08_day1_t2
* Type: Event
* EventId: event_7days_2023_08_21_t2
* Goals:
	* Task 1: GainItem

## QL_7DAYS_2023_08_DAY2_T2
### qe_7days_2023_08_day2_a_t2:
* Name: Day 2: Meet & Greet
* Description: Completing liaison assignments for a faction increases your reputation level for that faction. Higher reputation levels unlock additional items in that faction's liaison requisitions office.
* QuestLine: ql_7days_2023_08_day2_t2
* Type: Event
* EventId: event_7days_2023_08_21_t2
* Goals:
	* Task 1: 5 Faction_T2up

### qe_7days_2023_08_day2_b_t2:
* Name: Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.
* Description: Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.
* QuestLine: ql_7days_2023_08_day2_t2
* Type: Event
* EventId: event_7days_2023_08_21_t2
* Goals:
	* Task 1: Complete 3 side missions

### qe_7days_2023_08_day2_c_t2:
* Name: Complete liaison assignments to gain reputation for that faction. A higher reputation unlocks more items in that faction's liaison requisitions office.
* Description: Complete liaison assignments to gain reputation for that faction. A higher reputation unlocks more items in that faction's liaison requisitions office.
* QuestLine: ql_7days_2023_08_day2_t2
* Type: Event
* EventId: event_7days_2023_08_21_t2
* Goals:
	* Task 1: 135 RepTr1_RepTanoch_RepYaot_RepAmassari

### qe_7days_2023_08_day2_d_t2:
* Name: Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* Description: Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* QuestLine: ql_7days_2023_08_day2_t2
* Type: Event
* EventId: event_7days_2023_08_21_t2
* Goals:
	* Task 1: UpgradeOfficer

## QL_7DAYS_2023_08_DAY3_T2
### qe_7days_2023_08_day3_a_t2:
* Name: Day 3: Raw Materials
* Description: Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.
* QuestLine: ql_7days_2023_08_day3_t2
* Type: Event
* EventId: event_7days_2023_08_21_t2
* Goals:
	* Task 1: GainItem

### qe_7days_2023_08_day3_b_t2:
* Name: Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.
* Description: Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.
* QuestLine: ql_7days_2023_08_day3_t2
* Type: Event
* EventId: event_7days_2023_08_21_t2
* Goals:
	* Task 1: Craft

### qe_7days_2023_08_day3_c_t2:
* Name: Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.
* Description: Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.
* QuestLine: ql_7days_2023_08_day3_t2
* Type: Event
* EventId: event_7days_2023_08_21_t2
* Goals:
	* Task 1: Craft

### qe_7days_2023_08_day3_d_t2:
* Name: Items and resources can be sold for credits in the market at stations.
* Description: Items and resources can be sold for credits in the market at stations.
* QuestLine: ql_7days_2023_08_day3_t2
* Type: Event
* EventId: event_7days_2023_08_21_t2
* Goals:
	* Task 1: GainItem

## QL_7DAYS_2023_08_DAY4_T2
### qe_7days_2023_08_day4_a_t2:
* Name: Day 4: Hypothesis
* Description: Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.
* QuestLine: ql_7days_2023_08_day4_t2
* Type: Event
* EventId: event_7days_2023_08_21_t2
* Goals:
	* Task 1: GainItem

### qe_7days_2023_08_day4_b_t2:
* Name: Progenitor relics can be found in relic signature signals. Relics can be sold on the market for credits, though some liaison offices may be interested in relics as well.
* Description: Progenitor relics can be found in relic signature signals. Relics can be sold on the market for credits, though some liaison offices may be interested in relics as well.
* QuestLine: ql_7days_2023_08_day4_t2
* Type: Event
* EventId: event_7days_2023_08_21_t2
* Goals:
	* Task 1: GainItem

### qe_7days_2023_08_day4_c_t2:
* Name: Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.
* Description: Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.
* QuestLine: ql_7days_2023_08_day4_t2
* Type: Event
* EventId: event_7days_2023_08_21_t2
* Goals:
	* Task 1: 7 ShipsDestroyedProgenitorT2_ShipsDestroyedProgenitorT3_ShipsDestroyedProgenitorT4

### qe_7days_2023_08_day4_d_t2:
* Name: Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.
* Description: Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.
* QuestLine: ql_7days_2023_08_day4_t2
* Type: Event
* EventId: event_7days_2023_08_21_t2
* Goals:
	* Task 1: Complete side mission

## QL_7DAYS_2023_08_DAY5_T2
### qe_7days_2023_08_day5_a_t2:
* Name: Day 5: Lessons
* Description: Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
* QuestLine: ql_7days_2023_08_day5_t2
* Type: Event
* EventId: event_7days_2023_08_21_t2
* Goals:
	* Task 1: Complete 3 side missions

### qe_7days_2023_08_day5_b_t2:
* Name: Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.
* Description: Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.
* QuestLine: ql_7days_2023_08_day5_t2
* Type: Event
* EventId: event_7days_2023_08_21_t2
* Goals:
	* Task 1: GainItem

### qe_7days_2023_08_day5_c_t2:
* Name: Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* Description: Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* QuestLine: ql_7days_2023_08_day5_t2
* Type: Event
* EventId: event_7days_2023_08_21_t2
* Goals:
	* Task 1: UpgradeOfficer

### qe_7days_2023_08_day5_d_t2:
* Name: Discharging officers grants credits and insignias, which can be used to level up other officers.
* Description: Discharging officers grants credits and insignias, which can be used to level up other officers.
* QuestLine: ql_7days_2023_08_day5_t2
* Type: Event
* EventId: event_7days_2023_08_21_t2
* Goals:
	* Task 1: GainItem

## QL_7DAYS_2023_08_DAY6_T2
### qe_7days_2023_08_day6_a_t2:
* Name: Day 6: Stockpile
* Description: Rare earths are an occasional by-product of refining. They are required for upgrading modules.
* QuestLine: ql_7days_2023_08_day6_t2
* Type: Event
* EventId: event_7days_2023_08_21_t2
* Goals:
	* Task 1: GainItem

### qe_7days_2023_08_day6_b_t2:
* Name: The strength of modules can be increased through upgrades, which cost rare earths.
* Description: The strength of modules can be increased through upgrades, which cost rare earths.
* QuestLine: ql_7days_2023_08_day6_t2
* Type: Event
* EventId: event_7days_2023_08_21_t2
* Goals:
	* Task 1: Craft

### qe_7days_2023_08_day6_c_t2:
* Name: The strength of modules can be increased through upgrades, which cost rare earths.
* Description: Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.
* QuestLine: ql_7days_2023_08_day6_t2
* Type: Event
* EventId: event_7days_2023_08_21_t2
* Goals:
	* Task 1: Craft

### qe_7days_2023_08_day6_d_t2:
* Name: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Description: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* QuestLine: ql_7days_2023_08_day6_t2
* Type: Event
* EventId: event_7days_2023_08_21_t2
* Goals:
	* Task 1: 15 ShipsDestroyedT2_ShipsDestroyedT3_ShipsDestroyedT4

## QL_7DAYS_2023_08_DAY7_T2
### qe_7days_2023_08_day7_a_t2:
* Name: Day 7: Enemy Contact
* Description: Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
* QuestLine: ql_7days_2023_08_day7_t2
* Type: Event
* EventId: event_7days_2023_08_21_t2
* Goals:
	* Task 1: Complete 3 side missions

### qe_7days_2023_08_day7_b_t2:
* Name: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Description: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* QuestLine: ql_7days_2023_08_day7_t2
* Type: Event
* EventId: event_7days_2023_08_21_t2
* Goals:
	* Task 1: 15 ShipsDestroyedT2_ShipsDestroyedT3_ShipsDestroyedT4

### qe_7days_2023_08_day7_c_t2:
* Name: When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.
* Description: When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.
* QuestLine: ql_7days_2023_08_day7_t2
* Type: Event
* EventId: event_7days_2023_08_21_t2
* Goals:
	* Task 1: GainItem

### qe_7days_2023_08_day7_d_t2:
* Name: Strikes are difficult missions that require a strong fleet from several commanders to beat. Completing a strike rewards code fragments, which can be turned in for special blueprints.
* Description: Strikes are difficult missions that require a strong fleet from several commanders to beat. Completing a strike rewards code fragments, which can be turned in for special blueprints.
* QuestLine: ql_7days_2023_08_day7_t2
* Type: Event
* EventId: event_7days_2023_08_21_t2
* Goals:
	* Task 1: Complete side mission

## QL_7DAYS_2023_08_DAY1_T3
### qe_7days_2023_08_day1_a_t3:
* Name: Day 1: Lay of the Land
* Description: Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.
* QuestLine: ql_7days_2023_08_day1_t3
* Type: Event
* EventId: event_7days_2023_08_21_t3
* Goals:
	* Task 1: Scan

### qe_7days_2023_08_day1_b_t3:
* Name: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Description: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* QuestLine: ql_7days_2023_08_day1_t3
* Type: Event
* EventId: event_7days_2023_08_21_t3
* Goals:
	* Task 1: 15 ShipsDestroyedT3_ShipsDestroyedT4

### qe_7days_2023_08_day1_c_t3:
* Name: Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.
* Description: Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.
* QuestLine: ql_7days_2023_08_day1_t3
* Type: Event
* EventId: event_7days_2023_08_21_t3
* Goals:
	* Task 1: GainItem

### qe_7days_2023_08_day1_d_t3:
* Name: Rare earths are an occasional by-product of refining. They are required for upgrading modules.
* Description: Rare earths are an occasional by-product of refining. They are required for upgrading modules.
* QuestLine: ql_7days_2023_08_day1_t3
* Type: Event
* EventId: event_7days_2023_08_21_t3
* Goals:
	* Task 1: GainItem

## QL_7DAYS_2023_08_DAY2_T3
### qe_7days_2023_08_day2_a_t3:
* Name: Day 2: Meet & Greet
* Description: Completing liaison assignments for a faction increases your reputation level for that faction. Higher reputation levels unlock additional items in that faction's liaison requisitions office.
* QuestLine: ql_7days_2023_08_day2_t3
* Type: Event
* EventId: event_7days_2023_08_21_t3
* Goals:
	* Task 1: 5 Faction_T3up

### qe_7days_2023_08_day2_b_t3:
* Name: Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.
* Description: Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.
* QuestLine: ql_7days_2023_08_day2_t3
* Type: Event
* EventId: event_7days_2023_08_21_t3
* Goals:
	* Task 1: Complete 3 side missions

### qe_7days_2023_08_day2_c_t3:
* Name: Complete liaison assignments to gain reputation for that faction. A higher reputation unlocks more items in that faction's liaison requisitions office.
* Description: Complete liaison assignments to gain reputation for that faction. A higher reputation unlocks more items in that faction's liaison requisitions office.
* QuestLine: ql_7days_2023_08_day2_t3
* Type: Event
* EventId: event_7days_2023_08_21_t3
* Goals:
	* Task 1: 180 RepTr1_RepTanoch_RepYaot_RepAmassari

### qe_7days_2023_08_day2_d_t3:
* Name: Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* Description: Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* QuestLine: ql_7days_2023_08_day2_t3
* Type: Event
* EventId: event_7days_2023_08_21_t3
* Goals:
	* Task 1: UpgradeOfficer

## QL_7DAYS_2023_08_DAY3_T3
### qe_7days_2023_08_day3_a_t3:
* Name: Day 3: Raw Materials
* Description: Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.
* QuestLine: ql_7days_2023_08_day3_t3
* Type: Event
* EventId: event_7days_2023_08_21_t3
* Goals:
	* Task 1: GainItem

### qe_7days_2023_08_day3_b_t3:
* Name: Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.
* Description: Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.
* QuestLine: ql_7days_2023_08_day3_t3
* Type: Event
* EventId: event_7days_2023_08_21_t3
* Goals:
	* Task 1: Craft

### qe_7days_2023_08_day3_c_t3:
* Name: Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.
* Description: Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.
* QuestLine: ql_7days_2023_08_day3_t3
* Type: Event
* EventId: event_7days_2023_08_21_t3
* Goals:
	* Task 1: Craft

### qe_7days_2023_08_day3_d_t3:
* Name: Items and resources can be sold for credits in the market at stations.
* Description: Items and resources can be sold for credits in the market at stations.
* QuestLine: ql_7days_2023_08_day3_t3
* Type: Event
* EventId: event_7days_2023_08_21_t3
* Goals:
	* Task 1: GainItem

## QL_7DAYS_2023_08_DAY4_T3
### qe_7days_2023_08_day4_a_t3:
* Name: Day 4: Hypothesis
* Description: Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.
* QuestLine: ql_7days_2023_08_day4_t3
* Type: Event
* EventId: event_7days_2023_08_21_t3
* Goals:
	* Task 1: GainItem

### qe_7days_2023_08_day4_b_t3:
* Name: Progenitor relics can be found in relic signature signals. Relics can be sold on the market for credits, though some liaison offices may be interested in relics as well.
* Description: Progenitor relics can be found in relic signature signals. Relics can be sold on the market for credits, though some liaison offices may be interested in relics as well.
* QuestLine: ql_7days_2023_08_day4_t3
* Type: Event
* EventId: event_7days_2023_08_21_t3
* Goals:
	* Task 1: GainItem

### qe_7days_2023_08_day4_c_t3:
* Name: Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.
* Description: Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.
* QuestLine: ql_7days_2023_08_day4_t3
* Type: Event
* EventId: event_7days_2023_08_21_t3
* Goals:
	* Task 1: 7 ShipsDestroyedProgenitorT3_ShipsDestroyedProgenitorT4

### qe_7days_2023_08_day4_d_t3:
* Name: Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.
* Description: Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.
* QuestLine: ql_7days_2023_08_day4_t3
* Type: Event
* EventId: event_7days_2023_08_21_t3
* Goals:
	* Task 1: Complete side mission

## QL_7DAYS_2023_08_DAY5_T3
### qe_7days_2023_08_day5_a_t3:
* Name: Day 5: Lessons
* Description: Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
* QuestLine: ql_7days_2023_08_day5_t3
* Type: Event
* EventId: event_7days_2023_08_21_t3
* Goals:
	* Task 1: Complete 3 side missions

### qe_7days_2023_08_day5_b_t3:
* Name: Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.
* Description: Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.
* QuestLine: ql_7days_2023_08_day5_t3
* Type: Event
* EventId: event_7days_2023_08_21_t3
* Goals:
	* Task 1: GainItem

### qe_7days_2023_08_day5_c_t3:
* Name: Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* Description: Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* QuestLine: ql_7days_2023_08_day5_t3
* Type: Event
* EventId: event_7days_2023_08_21_t3
* Goals:
	* Task 1: UpgradeOfficer

### qe_7days_2023_08_day5_d_t3:
* Name: Discharging officers grants credits and insignias, which can be used to level up other officers.
* Description: Discharging officers grants credits and insignias, which can be used to level up other officers.
* QuestLine: ql_7days_2023_08_day5_t3
* Type: Event
* EventId: event_7days_2023_08_21_t3
* Goals:
	* Task 1: GainItem

## QL_7DAYS_2023_08_DAY6_T3
### qe_7days_2023_08_day6_a_t3:
* Name: Day 6: Stockpile
* Description: Rare earths are an occasional by-product of refining. They are required for upgrading modules.
* QuestLine: ql_7days_2023_08_day6_t3
* Type: Event
* EventId: event_7days_2023_08_21_t3
* Goals:
	* Task 1: GainItem

### qe_7days_2023_08_day6_b_t3:
* Name: The strength of modules can be increased through upgrades, which cost rare earths.
* Description: The strength of modules can be increased through upgrades, which cost rare earths.
* QuestLine: ql_7days_2023_08_day6_t3
* Type: Event
* EventId: event_7days_2023_08_21_t3
* Goals:
	* Task 1: Craft

### qe_7days_2023_08_day6_c_t3:
* Name: The strength of modules can be increased through upgrades, which cost rare earths.
* Description: The strength of modules can be increased through upgrades, which cost rare earths.
* QuestLine: ql_7days_2023_08_day6_t3
* Type: Event
* EventId: event_7days_2023_08_21_t3
* Goals:
	* Task 1: Craft

### qe_7days_2023_08_day6_d_t3:
* Name: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Description: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* QuestLine: ql_7days_2023_08_day6_t3
* Type: Event
* EventId: event_7days_2023_08_21_t3
* Goals:
	* Task 1: 15 ShipsDestroyedT3_ShipsDestroyedT4

## QL_7DAYS_2023_08_DAY7_T3
### qe_7days_2023_08_day7_a_t3:
* Name: Day 7: Enemy Contact
* Description: Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
* QuestLine: ql_7days_2023_08_day7_t3
* Type: Event
* EventId: event_7days_2023_08_21_t3
* Goals:
	* Task 1: Complete 3 side missions

### qe_7days_2023_08_day7_b_t3:
* Name: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Description: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* QuestLine: ql_7days_2023_08_day7_t3
* Type: Event
* EventId: event_7days_2023_08_21_t3
* Goals:
	* Task 1: 15 ShipsDestroyedT3_ShipsDestroyedT4

### qe_7days_2023_08_day7_c_t3:
* Name: When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.
* Description: When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.
* QuestLine: ql_7days_2023_08_day7_t3
* Type: Event
* EventId: event_7days_2023_08_21_t3
* Goals:
	* Task 1: GainItem

### qe_7days_2023_08_day7_d_t3:
* Name: Strikes are difficult missions that require a strong fleet from several commanders to beat. Completing a strike rewards code fragments, which can be turned in for special blueprints.
* Description: Strikes are difficult missions that require a strong fleet from several commanders to beat. Completing a strike rewards code fragments, which can be turned in for special blueprints.
* QuestLine: ql_7days_2023_08_day7_t3
* Type: Event
* EventId: event_7days_2023_08_21_t3
* Goals:
	* Task 1: Complete side mission

## QL_7DAYS_2023_08_DAY1_T4
### qe_7days_2023_08_day1_a_t4:
* Name: Day 1: Lay of the Land
* Description: Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.
* QuestLine: ql_7days_2023_08_day1_t4
* Type: Event
* EventId: event_7days_2023_08_21_t4
* Goals:
	* Task 1: Scan

### qe_7days_2023_08_day1_b_t4:
* Name: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Description: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* QuestLine: ql_7days_2023_08_day1_t4
* Type: Event
* EventId: event_7days_2023_08_21_t4
* Goals:
	* Task 1: 15 ShipsDestroyedT4

### qe_7days_2023_08_day1_c_t4:
* Name: Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.
* Description: Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.
* QuestLine: ql_7days_2023_08_day1_t4
* Type: Event
* EventId: event_7days_2023_08_21_t4
* Goals:
	* Task 1: GainItem

### qe_7days_2023_08_day1_d_t4:
* Name: Rare earths are an occasional by-product of refining. They are required for upgrading modules.
* Description: Rare earths are an occasional by-product of refining. They are required for upgrading modules.
* QuestLine: ql_7days_2023_08_day1_t4
* Type: Event
* EventId: event_7days_2023_08_21_t4
* Goals:
	* Task 1: GainItem

## QL_7DAYS_2023_08_DAY2_T4
### qe_7days_2023_08_day2_a_t4:
* Name: Day 2: Meet & Greet
* Description: Completing liaison assignments for a faction increases your reputation level for that faction. Higher reputation levels unlock additional items in that faction's liaison requisitions office.
* QuestLine: ql_7days_2023_08_day2_t4
* Type: Event
* EventId: event_7days_2023_08_21_t4
* Goals:
	* Task 1: 5 Faction_T4up

### qe_7days_2023_08_day2_b_t4:
* Name: Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.
* Description: Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.
* QuestLine: ql_7days_2023_08_day2_t4
* Type: Event
* EventId: event_7days_2023_08_21_t4
* Goals:
	* Task 1: Complete 3 side missions

### qe_7days_2023_08_day2_c_t4:
* Name: Complete liaison assignments to gain reputation for that faction. A higher reputation unlocks more items in that faction's liaison requisitions office.
* Description: Complete liaison assignments to gain reputation for that faction. A higher reputation unlocks more items in that faction's liaison requisitions office.
* QuestLine: ql_7days_2023_08_day2_t4
* Type: Event
* EventId: event_7days_2023_08_21_t4
* Goals:
	* Task 1: 225 RepTr1_RepTanoch_RepYaot_RepAmassari

### qe_7days_2023_08_day2_d_t4:
* Name: Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* Description: Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* QuestLine: ql_7days_2023_08_day2_t4
* Type: Event
* EventId: event_7days_2023_08_21_t4
* Goals:
	* Task 1: UpgradeOfficer

## QL_7DAYS_2023_08_DAY3_T4
### qe_7days_2023_08_day3_a_t4:
* Name: Day 3: Raw Materials
* Description: Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.
* QuestLine: ql_7days_2023_08_day3_t4
* Type: Event
* EventId: event_7days_2023_08_21_t4
* Goals:
	* Task 1: GainItem

### qe_7days_2023_08_day3_b_t4:
* Name: Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.
* Description: Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.
* QuestLine: ql_7days_2023_08_day3_t4
* Type: Event
* EventId: event_7days_2023_08_21_t4
* Goals:
	* Task 1: Craft

### qe_7days_2023_08_day3_c_t4:
* Name: Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.
* Description: Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.
* QuestLine: ql_7days_2023_08_day3_t4
* Type: Event
* EventId: event_7days_2023_08_21_t4
* Goals:
	* Task 1: Craft

### qe_7days_2023_08_day3_d_t4:
* Name: Items and resources can be sold for credits in the market at stations.
* Description: Items and resources can be sold for credits in the market at stations.
* QuestLine: ql_7days_2023_08_day3_t4
* Type: Event
* EventId: event_7days_2023_08_21_t4
* Goals:
	* Task 1: GainItem

## QL_7DAYS_2023_08_DAY4_T4
### qe_7days_2023_08_day4_a_t4:
* Name: Day 4: Hypothesis
* Description: Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.
* QuestLine: ql_7days_2023_08_day4_t4
* Type: Event
* EventId: event_7days_2023_08_21_t4
* Goals:
	* Task 1: GainItem

### qe_7days_2023_08_day4_b_t4:
* Name: Progenitor relics can be found in relic signature signals. Relics can be sold on the market for credits, though some liaison offices may be interested in relics as well.
* Description: Progenitor relics can be found in relic signature signals. Relics can be sold on the market for credits, though some liaison offices may be interested in relics as well.
* QuestLine: ql_7days_2023_08_day4_t4
* Type: Event
* EventId: event_7days_2023_08_21_t4
* Goals:
	* Task 1: GainItem

### qe_7days_2023_08_day4_c_t4:
* Name: Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.
* Description: Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.
* QuestLine: ql_7days_2023_08_day4_t4
* Type: Event
* EventId: event_7days_2023_08_21_t4
* Goals:
	* Task 1: 7 ShipsDestroyedProgenitorT4

### qe_7days_2023_08_day4_d_t4:
* Name: Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.
* Description: Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.
* QuestLine: ql_7days_2023_08_day4_t4
* Type: Event
* EventId: event_7days_2023_08_21_t4
* Goals:
	* Task 1: Complete side mission

## QL_7DAYS_2023_08_DAY5_T4
### qe_7days_2023_08_day5_a_t4:
* Name: Day 5: Lessons
* Description: Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
* QuestLine: ql_7days_2023_08_day5_t4
* Type: Event
* EventId: event_7days_2023_08_21_t4
* Goals:
	* Task 1: Complete 3 side missions

### qe_7days_2023_08_day5_b_t4:
* Name: Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.
* Description: Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.
* QuestLine: ql_7days_2023_08_day5_t4
* Type: Event
* EventId: event_7days_2023_08_21_t4
* Goals:
	* Task 1: GainItem

### qe_7days_2023_08_day5_c_t4:
* Name: Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* Description: Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* QuestLine: ql_7days_2023_08_day5_t4
* Type: Event
* EventId: event_7days_2023_08_21_t4
* Goals:
	* Task 1: UpgradeOfficer

### qe_7days_2023_08_day5_d_t4:
* Name: Discharging officers grants credits and insignias, which can be used to level up other officers.
* Description: Discharging officers grants credits and insignias, which can be used to level up other officers.
* QuestLine: ql_7days_2023_08_day5_t4
* Type: Event
* EventId: event_7days_2023_08_21_t4
* Goals:
	* Task 1: GainItem

## QL_7DAYS_2023_08_DAY6_T4
### qe_7days_2023_08_day6_a_t4:
* Name: Day 6: Stockpile
* Description: Rare earths are an occasional by-product of refining. They are required for upgrading modules.
* QuestLine: ql_7days_2023_08_day6_t4
* Type: Event
* EventId: event_7days_2023_08_21_t4
* Goals:
	* Task 1: GainItem

### qe_7days_2023_08_day6_b_t4:
* Name: The strength of modules can be increased through upgrades, which cost rare earths.
* Description: The strength of modules can be increased through upgrades, which cost rare earths.
* QuestLine: ql_7days_2023_08_day6_t4
* Type: Event
* EventId: event_7days_2023_08_21_t4
* Goals:
	* Task 1: Craft

### qe_7days_2023_08_day6_c_t4:
* Name: The strength of modules can be increased through upgrades, which cost rare earths.
* Description: The strength of modules can be increased through upgrades, which cost rare earths.
* QuestLine: ql_7days_2023_08_day6_t4
* Type: Event
* EventId: event_7days_2023_08_21_t4
* Goals:
	* Task 1: Craft

### qe_7days_2023_08_day6_d_t4:
* Name: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Description: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* QuestLine: ql_7days_2023_08_day6_t4
* Type: Event
* EventId: event_7days_2023_08_21_t4
* Goals:
	* Task 1: 15 ShipsDestroyedT4

## QL_7DAYS_2023_08_DAY7_T4
### qe_7days_2023_08_day7_a_t4:
* Name: Day 7: Enemy Contact
* Description: Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
* QuestLine: ql_7days_2023_08_day7_t4
* Type: Event
* EventId: event_7days_2023_08_21_t4
* Goals:
	* Task 1: Complete 3 side missions

### qe_7days_2023_08_day7_b_t4:
* Name: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Description: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* QuestLine: ql_7days_2023_08_day7_t4
* Type: Event
* EventId: event_7days_2023_08_21_t4
* Goals:
	* Task 1: 15 ShipsDestroyedT4

### qe_7days_2023_08_day7_c_t4:
* Name: When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.
* Description: When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.
* QuestLine: ql_7days_2023_08_day7_t4
* Type: Event
* EventId: event_7days_2023_08_21_t4
* Goals:
	* Task 1: GainItem

### qe_7days_2023_08_day7_d_t4:
* Name: Strikes are difficult missions that require a strong fleet from several commanders to beat. Completing a strike rewards code fragments, which can be turned in for special blueprints.
* Description: Strikes are difficult missions that require a strong fleet from several commanders to beat. Completing a strike rewards code fragments, which can be turned in for special blueprints.
* QuestLine: ql_7days_2023_08_day7_t4
* Type: Event
* EventId: event_7days_2023_08_21_t4
* Goals:
	* Task 1: Complete side mission

## QL_7DAYS_MAR_2024_DAY1_T1
### qe_7days_mar_2024_day1_a_t1:
* Name: Day 1: Lay of the Land
* Description: Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.
* QuestLine: ql_7days_mar_2024_day1_t1
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t1
* Goals:
	* Task 1: Scan

### qe_7days_mar_2024_day1_b_t1:
* Name: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Description: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* QuestLine: ql_7days_mar_2024_day1_t1
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t1
* Goals:
	* Task 1: 15 ShipsDestroyedT1_ShipsDestroyedT2_ShipsDestroyedT3_ShipsDestroyedT4

### qe_7days_mar_2024_day1_c_t1:
* Name: Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.
* Description: Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.
* QuestLine: ql_7days_mar_2024_day1_t1
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t1
* Goals:
	* Task 1: GainItem

### qe_7days_mar_2024_day1_d_t1:
* Name: Rare earths are an occasional by-product of refining. They are required for upgrading modules.
* Description: Rare earths are an occasional by-product of refining. They are required for upgrading modules.
* QuestLine: ql_7days_mar_2024_day1_t1
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t1
* Goals:
	* Task 1: GainItem

## QL_7DAYS_MAR_2024_DAY2_T1
### qe_7days_mar_2024_day2_a_t1:
* Name: Day 2: Meet & Greet
* Description: There are different types of assignments available in your assignment log.
* QuestLine: ql_7days_mar_2024_day2_t1
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t1
* Goals:
	* Task 1: 5 T1up

### qe_7days_mar_2024_day2_b_t1:
* Name: Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.
* Description: During missions you will usually fight against enemy ships. They can be part of an assignment, or they can be found as signals through scanning.
* QuestLine: ql_7days_mar_2024_day2_t1
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t1
* Goals:
	* Task 1: Complete 3 side missions

### qe_7days_mar_2024_day2_c_t1:
* Name: Complete liaison assignments to gain reputation for that faction. A higher reputation unlocks more items in that faction's liaison requisitions office.
* Description: Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.
* QuestLine: ql_7days_mar_2024_day2_t1
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t1
* Goals:
	* Task 1: GainItem

### qe_7days_mar_2024_day2_d_t1:
* Name: Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* Description: Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* QuestLine: ql_7days_mar_2024_day2_t1
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t1
* Goals:
	* Task 1: UpgradeOfficer

## QL_7DAYS_MAR_2024_DAY3_T1
### qe_7days_mar_2024_day3_a_t1:
* Name: Day 3: Raw Materials
* Description: Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.
* QuestLine: ql_7days_mar_2024_day3_t1
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t1
* Goals:
	* Task 1: GainItem

### qe_7days_mar_2024_day3_b_t1:
* Name: Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.
* Description: Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.
* QuestLine: ql_7days_mar_2024_day3_t1
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t1
* Goals:
	* Task 1: Craft

### qe_7days_mar_2024_day3_c_t1:
* Name: Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.
* Description: Small items such as strike craft, modules and parts can be built in the fabricator. Larger items such as escort ships and flagships must be constructed at shipyards provided at larger stations.
* QuestLine: ql_7days_mar_2024_day3_t1
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t1
* Goals:
	* Task 1: Craft

### qe_7days_mar_2024_day3_d_t1:
* Name: Items and resources can be sold for credits in the market at stations.
* Description: Items and resources can be sold for credits in the market at stations.
* QuestLine: ql_7days_mar_2024_day3_t1
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t1
* Goals:
	* Task 1: GainItem

## QL_7DAYS_MAR_2024_DAY4_T1
### qe_7days_mar_2024_day4_a_t1:
* Name: Day 4: Hypothesis
* Description: Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
* QuestLine: ql_7days_mar_2024_day4_t1
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t1
* Goals:
	* Task 1: Complete 3 side missions

### qe_7days_mar_2024_day4_b_t1:
* Name: Progenitor relics can be found in relic signature signals. Relics can be sold on the market for credits, though some liaison offices may be interested in relics as well.
* Description: Progenitor relics can be found in relic signature signals. Relics can be sold on the market for credits, though some liaison offices may be interested in relics as well.
* QuestLine: ql_7days_mar_2024_day4_t1
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t1
* Goals:
	* Task 1: GainItem

### qe_7days_mar_2024_day4_c_t1:
* Name: Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.
* Description: Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.
* QuestLine: ql_7days_mar_2024_day4_t1
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t1
* Goals:
	* Task 1: 7 ShipsDestroyedProgenitorT1_ShipsDestroyedProgenitorT2_ShipsDestroyedProgenitorT3_ShipsDestroyedProgenitorT4

### qe_7days_mar_2024_day4_d_t1:
* Name: Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.
* Description: Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.
* QuestLine: ql_7days_mar_2024_day4_t1
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t1
* Goals:
	* Task 1: Complete side mission

## QL_7DAYS_MAR_2024_DAY5_T1
### qe_7days_mar_2024_day5_a_t1:
* Name: Day 5: Lessons
* Description: Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
* QuestLine: ql_7days_mar_2024_day5_t1
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t1
* Goals:
	* Task 1: Complete 3 side missions

### qe_7days_mar_2024_day5_b_t1:
* Name: Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.
* Description: Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.
* QuestLine: ql_7days_mar_2024_day5_t1
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t1
* Goals:
	* Task 1: GainItem

### qe_7days_mar_2024_day5_c_t1:
* Name: Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* Description: Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* QuestLine: ql_7days_mar_2024_day5_t1
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t1
* Goals:
	* Task 1: UpgradeOfficer

### qe_7days_mar_2024_day5_d_t1:
* Name: Discharging officers grants credits and insignias, which can be used to level up other officers.
* Description: Discharging officers grants credits and insignias, which can be used to level up other officers.
* QuestLine: ql_7days_mar_2024_day5_t1
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t1
* Goals:
	* Task 1: GainItem

## QL_7DAYS_MAR_2024_DAY6_T1
### qe_7days_mar_2024_day6_a_t1:
* Name: Day 6: Stockpile
* Description: Rare earths are an occasional by-product of refining. They are required for upgrading modules.
* QuestLine: ql_7days_mar_2024_day6_t1
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t1
* Goals:
	* Task 1: GainItem

### qe_7days_mar_2024_day6_b_t1:
* Name: The strength of modules can be increased through upgrades, which cost rare earths.
* Description: Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* QuestLine: ql_7days_mar_2024_day6_t1
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t1
* Goals:
	* Task 1: UpgradeOfficer

### qe_7days_mar_2024_day6_c_t1:
* Name: The strength of modules can be increased through upgrades, which cost rare earths.
* Description: Small items such as strike craft, modules and parts can be built in the fabricator. Larger items such as escort ships and flagships must be constructed at shipyards provided at larger stations.
* QuestLine: ql_7days_mar_2024_day6_t1
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t1
* Goals:
	* Task 1: Craft

### qe_7days_mar_2024_day6_d_t1:
* Name: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Description: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* QuestLine: ql_7days_mar_2024_day6_t1
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t1
* Goals:
	* Task 1: 15 ShipsDestroyedT1_ShipsDestroyedT2_ShipsDestroyedT3_ShipsDestroyedT4

## QL_7DAYS_MAR_2024_DAY7_T1
### qe_7days_mar_2024_day7_a_t1:
* Name: Day 7: Enemy Contact
* Description: Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
* QuestLine: ql_7days_mar_2024_day7_t1
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t1
* Goals:
	* Task 1: Complete 3 side missions

### qe_7days_mar_2024_day7_b_t1:
* Name: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Description: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* QuestLine: ql_7days_mar_2024_day7_t1
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t1
* Goals:
	* Task 1: 15 ShipsDestroyedT1_ShipsDestroyedT2_ShipsDestroyedT3_ShipsDestroyedT4

### qe_7days_mar_2024_day7_c_t1:
* Name: When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.
* Description: When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.
* QuestLine: ql_7days_mar_2024_day7_t1
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t1
* Goals:
	* Task 1: GainItem

### qe_7days_mar_2024_day7_d_t1:
* Name: Strikes are difficult missions that require a strong fleet from several commanders to beat. Completing a strike rewards code fragments, which can be turned in for special blueprints.
* Description: Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
* QuestLine: ql_7days_mar_2024_day7_t1
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t1
* Goals:
	* Task 1: Complete 3 side missions

## QL_7DAYS_MAR_2024_DAY1_T2
### qe_7days_mar_2024_day1_a_t2:
* Name: Day 1: Lay of the Land
* Description: Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.
* QuestLine: ql_7days_mar_2024_day1_t2
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t2
* Goals:
	* Task 1: Scan

### qe_7days_mar_2024_day1_b_t2:
* Name: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Description: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* QuestLine: ql_7days_mar_2024_day1_t2
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t2
* Goals:
	* Task 1: 15 ShipsDestroyedT2_ShipsDestroyedT3_ShipsDestroyedT4

### qe_7days_mar_2024_day1_c_t2:
* Name: Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.
* Description: Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.
* QuestLine: ql_7days_mar_2024_day1_t2
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t2
* Goals:
	* Task 1: GainItem

### qe_7days_mar_2024_day1_d_t2:
* Name: Rare earths are an occasional by-product of refining. They are required for upgrading modules.
* Description: Rare earths are an occasional by-product of refining. They are required for upgrading modules.
* QuestLine: ql_7days_mar_2024_day1_t2
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t2
* Goals:
	* Task 1: GainItem

## QL_7DAYS_MAR_2024_DAY2_T2
### qe_7days_mar_2024_day2_a_t2:
* Name: Day 2: Meet & Greet
* Description: Completing liaison assignments for a faction increases your reputation level for that faction. Higher reputation levels unlock additional items in that faction's liaison requisitions office.
* QuestLine: ql_7days_mar_2024_day2_t2
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t2
* Goals:
	* Task 1: 5 Faction_T2up

### qe_7days_mar_2024_day2_b_t2:
* Name: Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.
* Description: Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.
* QuestLine: ql_7days_mar_2024_day2_t2
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t2
* Goals:
	* Task 1: Complete 3 side missions

### qe_7days_mar_2024_day2_c_t2:
* Name: Complete liaison assignments to gain reputation for that faction. A higher reputation unlocks more items in that faction's liaison requisitions office.
* Description: Complete liaison assignments to gain reputation for that faction. A higher reputation unlocks more items in that faction's liaison requisitions office.
* QuestLine: ql_7days_mar_2024_day2_t2
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t2
* Goals:
	* Task 1: 135 RepTr1_RepTanoch_RepYaot_RepAmassari

### qe_7days_mar_2024_day2_d_t2:
* Name: Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* Description: Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* QuestLine: ql_7days_mar_2024_day2_t2
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t2
* Goals:
	* Task 1: UpgradeOfficer

## QL_7DAYS_MAR_2024_DAY3_T2
### qe_7days_mar_2024_day3_a_t2:
* Name: Day 3: Raw Materials
* Description: Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.
* QuestLine: ql_7days_mar_2024_day3_t2
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t2
* Goals:
	* Task 1: GainItem

### qe_7days_mar_2024_day3_b_t2:
* Name: Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.
* Description: Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.
* QuestLine: ql_7days_mar_2024_day3_t2
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t2
* Goals:
	* Task 1: Craft

### qe_7days_mar_2024_day3_c_t2:
* Name: Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.
* Description: Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.
* QuestLine: ql_7days_mar_2024_day3_t2
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t2
* Goals:
	* Task 1: Craft

### qe_7days_mar_2024_day3_d_t2:
* Name: Items and resources can be sold for credits in the market at stations.
* Description: Items and resources can be sold for credits in the market at stations.
* QuestLine: ql_7days_mar_2024_day3_t2
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t2
* Goals:
	* Task 1: GainItem

## QL_7DAYS_MAR_2024_DAY4_T2
### qe_7days_mar_2024_day4_a_t2:
* Name: Day 4: Hypothesis
* Description: Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.
* QuestLine: ql_7days_mar_2024_day4_t2
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t2
* Goals:
	* Task 1: GainItem

### qe_7days_mar_2024_day4_b_t2:
* Name: Progenitor relics can be found in relic signature signals. Relics can be sold on the market for credits, though some liaison offices may be interested in relics as well.
* Description: Progenitor relics can be found in relic signature signals. Relics can be sold on the market for credits, though some liaison offices may be interested in relics as well.
* QuestLine: ql_7days_mar_2024_day4_t2
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t2
* Goals:
	* Task 1: GainItem

### qe_7days_mar_2024_day4_c_t2:
* Name: Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.
* Description: Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.
* QuestLine: ql_7days_mar_2024_day4_t2
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t2
* Goals:
	* Task 1: 7 ShipsDestroyedProgenitorT2_ShipsDestroyedProgenitorT3_ShipsDestroyedProgenitorT4

### qe_7days_mar_2024_day4_d_t2:
* Name: Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.
* Description: Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.
* QuestLine: ql_7days_mar_2024_day4_t2
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t2
* Goals:
	* Task 1: Complete side mission

## QL_7DAYS_MAR_2024_DAY5_T2
### qe_7days_mar_2024_day5_a_t2:
* Name: Day 5: Lessons
* Description: Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
* QuestLine: ql_7days_mar_2024_day5_t2
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t2
* Goals:
	* Task 1: Complete 3 side missions

### qe_7days_mar_2024_day5_b_t2:
* Name: Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.
* Description: Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.
* QuestLine: ql_7days_mar_2024_day5_t2
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t2
* Goals:
	* Task 1: GainItem

### qe_7days_mar_2024_day5_c_t2:
* Name: Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* Description: Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* QuestLine: ql_7days_mar_2024_day5_t2
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t2
* Goals:
	* Task 1: UpgradeOfficer

### qe_7days_mar_2024_day5_d_t2:
* Name: Discharging officers grants credits and insignias, which can be used to level up other officers.
* Description: Discharging officers grants credits and insignias, which can be used to level up other officers.
* QuestLine: ql_7days_mar_2024_day5_t2
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t2
* Goals:
	* Task 1: GainItem

## QL_7DAYS_MAR_2024_DAY6_T2
### qe_7days_mar_2024_day6_a_t2:
* Name: Day 6: Stockpile
* Description: Rare earths are an occasional by-product of refining. They are required for upgrading modules.
* QuestLine: ql_7days_mar_2024_day6_t2
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t2
* Goals:
	* Task 1: GainItem

### qe_7days_mar_2024_day6_b_t2:
* Name: The strength of modules can be increased through upgrades, which cost rare earths.
* Description: The strength of modules can be increased through upgrades, which cost rare earths.
* QuestLine: ql_7days_mar_2024_day6_t2
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t2
* Goals:
	* Task 1: Craft

### qe_7days_mar_2024_day6_c_t2:
* Name: The strength of modules can be increased through upgrades, which cost rare earths.
* Description: Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.
* QuestLine: ql_7days_mar_2024_day6_t2
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t2
* Goals:
	* Task 1: Craft

### qe_7days_mar_2024_day6_d_t2:
* Name: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Description: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* QuestLine: ql_7days_mar_2024_day6_t2
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t2
* Goals:
	* Task 1: 15 ShipsDestroyedT2_ShipsDestroyedT3_ShipsDestroyedT4

## QL_7DAYS_MAR_2024_DAY7_T2
### qe_7days_mar_2024_day7_a_t2:
* Name: Day 7: Enemy Contact
* Description: Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
* QuestLine: ql_7days_mar_2024_day7_t2
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t2
* Goals:
	* Task 1: Complete 3 side missions

### qe_7days_mar_2024_day7_b_t2:
* Name: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Description: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* QuestLine: ql_7days_mar_2024_day7_t2
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t2
* Goals:
	* Task 1: 15 ShipsDestroyedT2_ShipsDestroyedT3_ShipsDestroyedT4

### qe_7days_mar_2024_day7_c_t2:
* Name: When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.
* Description: When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.
* QuestLine: ql_7days_mar_2024_day7_t2
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t2
* Goals:
	* Task 1: GainItem

### qe_7days_mar_2024_day7_d_t2:
* Name: Strikes are difficult missions that require a strong fleet from several commanders to beat. Completing a strike rewards code fragments, which can be turned in for special blueprints.
* Description: Strikes are difficult missions that require a strong fleet from several commanders to beat. Completing a strike rewards code fragments, which can be turned in for special blueprints.
* QuestLine: ql_7days_mar_2024_day7_t2
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t2
* Goals:
	* Task 1: Complete side mission

## QL_7DAYS_MAR_2024_DAY1_T3
### qe_7days_mar_2024_day1_a_t3:
* Name: Day 1: Lay of the Land
* Description: Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.
* QuestLine: ql_7days_mar_2024_day1_t3
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t3
* Goals:
	* Task 1: Scan

### qe_7days_mar_2024_day1_b_t3:
* Name: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Description: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* QuestLine: ql_7days_mar_2024_day1_t3
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t3
* Goals:
	* Task 1: 15 ShipsDestroyedT3_ShipsDestroyedT4

### qe_7days_mar_2024_day1_c_t3:
* Name: Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.
* Description: Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.
* QuestLine: ql_7days_mar_2024_day1_t3
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t3
* Goals:
	* Task 1: GainItem

### qe_7days_mar_2024_day1_d_t3:
* Name: Rare earths are an occasional by-product of refining. They are required for upgrading modules.
* Description: Rare earths are an occasional by-product of refining. They are required for upgrading modules.
* QuestLine: ql_7days_mar_2024_day1_t3
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t3
* Goals:
	* Task 1: GainItem

## QL_7DAYS_MAR_2024_DAY2_T3
### qe_7days_mar_2024_day2_a_t3:
* Name: Day 2: Meet & Greet
* Description: Completing liaison assignments for a faction increases your reputation level for that faction. Higher reputation levels unlock additional items in that faction's liaison requisitions office.
* QuestLine: ql_7days_mar_2024_day2_t3
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t3
* Goals:
	* Task 1: 5 Faction_T3up

### qe_7days_mar_2024_day2_b_t3:
* Name: Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.
* Description: Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.
* QuestLine: ql_7days_mar_2024_day2_t3
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t3
* Goals:
	* Task 1: Complete 3 side missions

### qe_7days_mar_2024_day2_c_t3:
* Name: Complete liaison assignments to gain reputation for that faction. A higher reputation unlocks more items in that faction's liaison requisitions office.
* Description: Complete liaison assignments to gain reputation for that faction. A higher reputation unlocks more items in that faction's liaison requisitions office.
* QuestLine: ql_7days_mar_2024_day2_t3
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t3
* Goals:
	* Task 1: 180 RepTr1_RepTanoch_RepYaot_RepAmassari

### qe_7days_mar_2024_day2_d_t3:
* Name: Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* Description: Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* QuestLine: ql_7days_mar_2024_day2_t3
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t3
* Goals:
	* Task 1: UpgradeOfficer

## QL_7DAYS_MAR_2024_DAY3_T3
### qe_7days_mar_2024_day3_a_t3:
* Name: Day 3: Raw Materials
* Description: Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.
* QuestLine: ql_7days_mar_2024_day3_t3
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t3
* Goals:
	* Task 1: GainItem

### qe_7days_mar_2024_day3_b_t3:
* Name: Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.
* Description: Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.
* QuestLine: ql_7days_mar_2024_day3_t3
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t3
* Goals:
	* Task 1: Craft

### qe_7days_mar_2024_day3_c_t3:
* Name: Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.
* Description: Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.
* QuestLine: ql_7days_mar_2024_day3_t3
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t3
* Goals:
	* Task 1: Craft

### qe_7days_mar_2024_day3_d_t3:
* Name: Items and resources can be sold for credits in the market at stations.
* Description: Items and resources can be sold for credits in the market at stations.
* QuestLine: ql_7days_mar_2024_day3_t3
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t3
* Goals:
	* Task 1: GainItem

## QL_7DAYS_MAR_2024_DAY4_T3
### qe_7days_mar_2024_day4_a_t3:
* Name: Day 4: Hypothesis
* Description: Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.
* QuestLine: ql_7days_mar_2024_day4_t3
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t3
* Goals:
	* Task 1: GainItem

### qe_7days_mar_2024_day4_b_t3:
* Name: Progenitor relics can be found in relic signature signals. Relics can be sold on the market for credits, though some liaison offices may be interested in relics as well.
* Description: Progenitor relics can be found in relic signature signals. Relics can be sold on the market for credits, though some liaison offices may be interested in relics as well.
* QuestLine: ql_7days_mar_2024_day4_t3
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t3
* Goals:
	* Task 1: GainItem

### qe_7days_mar_2024_day4_c_t3:
* Name: Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.
* Description: Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.
* QuestLine: ql_7days_mar_2024_day4_t3
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t3
* Goals:
	* Task 1: 7 ShipsDestroyedProgenitorT3_ShipsDestroyedProgenitorT4

### qe_7days_mar_2024_day4_d_t3:
* Name: Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.
* Description: Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.
* QuestLine: ql_7days_mar_2024_day4_t3
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t3
* Goals:
	* Task 1: Complete side mission

## QL_7DAYS_MAR_2024_DAY5_T3
### qe_7days_mar_2024_day5_a_t3:
* Name: Day 5: Lessons
* Description: Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
* QuestLine: ql_7days_mar_2024_day5_t3
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t3
* Goals:
	* Task 1: Complete 3 side missions

### qe_7days_mar_2024_day5_b_t3:
* Name: Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.
* Description: Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.
* QuestLine: ql_7days_mar_2024_day5_t3
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t3
* Goals:
	* Task 1: GainItem

### qe_7days_mar_2024_day5_c_t3:
* Name: Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* Description: Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* QuestLine: ql_7days_mar_2024_day5_t3
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t3
* Goals:
	* Task 1: UpgradeOfficer

### qe_7days_mar_2024_day5_d_t3:
* Name: Discharging officers grants credits and insignias, which can be used to level up other officers.
* Description: Discharging officers grants credits and insignias, which can be used to level up other officers.
* QuestLine: ql_7days_mar_2024_day5_t3
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t3
* Goals:
	* Task 1: GainItem

## QL_7DAYS_MAR_2024_DAY6_T3
### qe_7days_mar_2024_day6_a_t3:
* Name: Day 6: Stockpile
* Description: Rare earths are an occasional by-product of refining. They are required for upgrading modules.
* QuestLine: ql_7days_mar_2024_day6_t3
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t3
* Goals:
	* Task 1: GainItem

### qe_7days_mar_2024_day6_b_t3:
* Name: The strength of modules can be increased through upgrades, which cost rare earths.
* Description: The strength of modules can be increased through upgrades, which cost rare earths.
* QuestLine: ql_7days_mar_2024_day6_t3
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t3
* Goals:
	* Task 1: Craft

### qe_7days_mar_2024_day6_c_t3:
* Name: The strength of modules can be increased through upgrades, which cost rare earths.
* Description: The strength of modules can be increased through upgrades, which cost rare earths.
* QuestLine: ql_7days_mar_2024_day6_t3
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t3
* Goals:
	* Task 1: Craft

### qe_7days_mar_2024_day6_d_t3:
* Name: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Description: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* QuestLine: ql_7days_mar_2024_day6_t3
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t3
* Goals:
	* Task 1: 15 ShipsDestroyedT3_ShipsDestroyedT4

## QL_7DAYS_MAR_2024_DAY7_T3
### qe_7days_mar_2024_day7_a_t3:
* Name: Day 7: Enemy Contact
* Description: Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
* QuestLine: ql_7days_mar_2024_day7_t3
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t3
* Goals:
	* Task 1: Complete 3 side missions

### qe_7days_mar_2024_day7_b_t3:
* Name: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Description: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* QuestLine: ql_7days_mar_2024_day7_t3
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t3
* Goals:
	* Task 1: 15 ShipsDestroyedT3_ShipsDestroyedT4

### qe_7days_mar_2024_day7_c_t3:
* Name: When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.
* Description: When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.
* QuestLine: ql_7days_mar_2024_day7_t3
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t3
* Goals:
	* Task 1: GainItem

### qe_7days_mar_2024_day7_d_t3:
* Name: Strikes are difficult missions that require a strong fleet from several commanders to beat. Completing a strike rewards code fragments, which can be turned in for special blueprints.
* Description: Strikes are difficult missions that require a strong fleet from several commanders to beat. Completing a strike rewards code fragments, which can be turned in for special blueprints.
* QuestLine: ql_7days_mar_2024_day7_t3
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t3
* Goals:
	* Task 1: Complete side mission

## QL_7DAYS_MAR_2024_DAY1_T4
### qe_7days_mar_2024_day1_a_t4:
* Name: Day 1: Lay of the Land
* Description: Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.
* QuestLine: ql_7days_mar_2024_day1_t4
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t4
* Goals:
	* Task 1: Scan

### qe_7days_mar_2024_day1_b_t4:
* Name: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Description: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* QuestLine: ql_7days_mar_2024_day1_t4
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t4
* Goals:
	* Task 1: 15 ShipsDestroyedT4

### qe_7days_mar_2024_day1_c_t4:
* Name: Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.
* Description: Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.
* QuestLine: ql_7days_mar_2024_day1_t4
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t4
* Goals:
	* Task 1: GainItem

### qe_7days_mar_2024_day1_d_t4:
* Name: Rare earths are an occasional by-product of refining. They are required for upgrading modules.
* Description: Rare earths are an occasional by-product of refining. They are required for upgrading modules.
* QuestLine: ql_7days_mar_2024_day1_t4
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t4
* Goals:
	* Task 1: GainItem

## QL_7DAYS_MAR_2024_DAY2_T4
### qe_7days_mar_2024_day2_a_t4:
* Name: Day 2: Meet & Greet
* Description: Completing liaison assignments for a faction increases your reputation level for that faction. Higher reputation levels unlock additional items in that faction's liaison requisitions office.
* QuestLine: ql_7days_mar_2024_day2_t4
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t4
* Goals:
	* Task 1: 5 Faction_T4up

### qe_7days_mar_2024_day2_b_t4:
* Name: Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.
* Description: Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.
* QuestLine: ql_7days_mar_2024_day2_t4
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t4
* Goals:
	* Task 1: Complete 3 side missions

### qe_7days_mar_2024_day2_c_t4:
* Name: Complete liaison assignments to gain reputation for that faction. A higher reputation unlocks more items in that faction's liaison requisitions office.
* Description: Complete liaison assignments to gain reputation for that faction. A higher reputation unlocks more items in that faction's liaison requisitions office.
* QuestLine: ql_7days_mar_2024_day2_t4
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t4
* Goals:
	* Task 1: 225 RepTr1_RepTanoch_RepYaot_RepAmassari

### qe_7days_mar_2024_day2_d_t4:
* Name: Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* Description: Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* QuestLine: ql_7days_mar_2024_day2_t4
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t4
* Goals:
	* Task 1: UpgradeOfficer

## QL_7DAYS_MAR_2024_DAY3_T4
### qe_7days_mar_2024_day3_a_t4:
* Name: Day 3: Raw Materials
* Description: Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.
* QuestLine: ql_7days_mar_2024_day3_t4
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t4
* Goals:
	* Task 1: GainItem

### qe_7days_mar_2024_day3_b_t4:
* Name: Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.
* Description: Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.
* QuestLine: ql_7days_mar_2024_day3_t4
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t4
* Goals:
	* Task 1: Craft

### qe_7days_mar_2024_day3_c_t4:
* Name: Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.
* Description: Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.
* QuestLine: ql_7days_mar_2024_day3_t4
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t4
* Goals:
	* Task 1: Craft

### qe_7days_mar_2024_day3_d_t4:
* Name: Items and resources can be sold for credits in the market at stations.
* Description: Items and resources can be sold for credits in the market at stations.
* QuestLine: ql_7days_mar_2024_day3_t4
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t4
* Goals:
	* Task 1: GainItem

## QL_7DAYS_MAR_2024_DAY4_T4
### qe_7days_mar_2024_day4_a_t4:
* Name: Day 4: Hypothesis
* Description: Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.
* QuestLine: ql_7days_mar_2024_day4_t4
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t4
* Goals:
	* Task 1: GainItem

### qe_7days_mar_2024_day4_b_t4:
* Name: Progenitor relics can be found in relic signature signals. Relics can be sold on the market for credits, though some liaison offices may be interested in relics as well.
* Description: Progenitor relics can be found in relic signature signals. Relics can be sold on the market for credits, though some liaison offices may be interested in relics as well.
* QuestLine: ql_7days_mar_2024_day4_t4
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t4
* Goals:
	* Task 1: GainItem

### qe_7days_mar_2024_day4_c_t4:
* Name: Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.
* Description: Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.
* QuestLine: ql_7days_mar_2024_day4_t4
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t4
* Goals:
	* Task 1: 7 ShipsDestroyedProgenitorT4

### qe_7days_mar_2024_day4_d_t4:
* Name: Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.
* Description: Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.
* QuestLine: ql_7days_mar_2024_day4_t4
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t4
* Goals:
	* Task 1: Complete side mission

## QL_7DAYS_MAR_2024_DAY5_T4
### qe_7days_mar_2024_day5_a_t4:
* Name: Day 5: Lessons
* Description: Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
* QuestLine: ql_7days_mar_2024_day5_t4
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t4
* Goals:
	* Task 1: Complete 3 side missions

### qe_7days_mar_2024_day5_b_t4:
* Name: Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.
* Description: Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.
* QuestLine: ql_7days_mar_2024_day5_t4
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t4
* Goals:
	* Task 1: GainItem

### qe_7days_mar_2024_day5_c_t4:
* Name: Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* Description: Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* QuestLine: ql_7days_mar_2024_day5_t4
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t4
* Goals:
	* Task 1: UpgradeOfficer

### qe_7days_mar_2024_day5_d_t4:
* Name: Discharging officers grants credits and insignias, which can be used to level up other officers.
* Description: Discharging officers grants credits and insignias, which can be used to level up other officers.
* QuestLine: ql_7days_mar_2024_day5_t4
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t4
* Goals:
	* Task 1: GainItem

## QL_7DAYS_MAR_2024_DAY6_T4
### qe_7days_mar_2024_day6_a_t4:
* Name: Day 6: Stockpile
* Description: Rare earths are an occasional by-product of refining. They are required for upgrading modules.
* QuestLine: ql_7days_mar_2024_day6_t4
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t4
* Goals:
	* Task 1: GainItem

### qe_7days_mar_2024_day6_b_t4:
* Name: The strength of modules can be increased through upgrades, which cost rare earths.
* Description: The strength of modules can be increased through upgrades, which cost rare earths.
* QuestLine: ql_7days_mar_2024_day6_t4
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t4
* Goals:
	* Task 1: Craft

### qe_7days_mar_2024_day6_c_t4:
* Name: The strength of modules can be increased through upgrades, which cost rare earths.
* Description: The strength of modules can be increased through upgrades, which cost rare earths.
* QuestLine: ql_7days_mar_2024_day6_t4
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t4
* Goals:
	* Task 1: Craft

### qe_7days_mar_2024_day6_d_t4:
* Name: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Description: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* QuestLine: ql_7days_mar_2024_day6_t4
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t4
* Goals:
	* Task 1: 15 ShipsDestroyedT4

## QL_7DAYS_MAR_2024_DAY7_T4
### qe_7days_mar_2024_day7_a_t4:
* Name: Day 7: Enemy Contact
* Description: Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
* QuestLine: ql_7days_mar_2024_day7_t4
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t4
* Goals:
	* Task 1: Complete 3 side missions

### qe_7days_mar_2024_day7_b_t4:
* Name: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Description: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* QuestLine: ql_7days_mar_2024_day7_t4
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t4
* Goals:
	* Task 1: 15 ShipsDestroyedT4

### qe_7days_mar_2024_day7_c_t4:
* Name: When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.
* Description: When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.
* QuestLine: ql_7days_mar_2024_day7_t4
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t4
* Goals:
	* Task 1: GainItem

### qe_7days_mar_2024_day7_d_t4:
* Name: Strikes are difficult missions that require a strong fleet from several commanders to beat. Completing a strike rewards code fragments, which can be turned in for special blueprints.
* Description: Strikes are difficult missions that require a strong fleet from several commanders to beat. Completing a strike rewards code fragments, which can be turned in for special blueprints.
* QuestLine: ql_7days_mar_2024_day7_t4
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t4
* Goals:
	* Task 1: Complete side mission

## QL_EVENT_YAOTSPRING_2024_T1
### qe_yaoSpr_2024_day01_t1:
* Name: There are rumors circulating in the Empty Quarter about an increase in Cangacian pirate activity. Fleet Command asks us to gather intel from our contacts with the Iyatequa traders. We should gain some favors to bargain for information.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Description: There are rumors circulating in the Empty Quarter about an increase in Cangacian pirate activity. Fleet Command asks us to gather intel from our contacts with the Iyatequa traders. We should gain some favors to bargain for information.

<color=#FBB03F>There are different types of assignments available in your assignment log.</color>
* QuestLine: ql_event_YaotSpring_2024_t1
* Type: Event
* EventId: event_yaotSpring_2024_t1
* Goals:
	* Task 1: 5 T1up

### qe_yaoSpr_2024_day02_t1:
* Name: The Iyatequa traders are involved with pirates attacking Yaot pilgrims in the Empty Quarter. We might get more information through selling equipment and arms on the open market.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
* Description: The Iyatequa traders are involved with pirates attacking Yaot pilgrims in the Empty Quarter. We might get more information through selling equipment and arms on the open market.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
* QuestLine: ql_event_YaotSpring_2024_t1
* Type: Event
* EventId: event_yaotSpring_2024_t1
* Goals:
	* Task 1: GainItem

### qe_yaoSpr_2024_day03_t1:
* Name: To learn more about the pirate raids, we should get in contact with the Yaot pilgrims. They appear to be hiding after recent attacks. We have no other option than to perform reconnaissance in the nearby systems.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
* Description: To learn more about the pirate raids, we should get in contact with the Yaot pilgrims. They appear to be hiding after recent attacks. We have no other option than to perform reconnaissance in the nearby systems.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
* QuestLine: ql_event_YaotSpring_2024_t1
* Type: Event
* EventId: event_yaotSpring_2024_t1
* Goals:
	* Task 1: Scan

### qe_yaoSpr_2024_day04_t1:
* Name: In our search for the Yaot pilgrims we have encountered intense pirate activity. We should hunt down some of their ships and see if we can gather any additional clues.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
* Description: In our search for the Yaot pilgrims we have encountered intense pirate activity. We should hunt down some of their ships and see if we can gather any additional clues.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
* QuestLine: ql_event_YaotSpring_2024_t1
* Type: Event
* EventId: event_yaotSpring_2024_t1
* Goals:
	* Task 1: GainItem

### qe_yaoSpr_2024_day05_t1:
* Name: Some Yaot survivors in our medical ward are ready to be questioned. If we manage to prove our good intentions they might help us find the Yaot pilgrimage.

<color=#FBB03F>Prestige is earned through each player level-up and by completing daily and weekly assignments.</color>
* Description: Some Yaot survivors in our medical ward are ready to be questioned. If we manage to prove our good intentions they might help us find the Yaot pilgrimage.

<color=#FBB03F>Prestige is earned through each player level-up and by completing daily and weekly assignments.</color>
* QuestLine: ql_event_YaotSpring_2024_t1
* Type: Event
* EventId: event_yaotSpring_2024_t1
* Goals:
	* Task 1: GainItem

### qe_yaoSpr_2024_day06_t1:
* Name: The Yaot have accepted our offer to support their pilgrimage. Requests have come in from ships needing spares and replacement parts for repairs. If we provide these, we might learn more about why the pirates are after these ships.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
* Description: The Yaot have accepted our offer to support their pilgrimage. Requests have come in from ships needing spares and replacement parts for repairs. If we provide these, we might learn more about why the pirates are after these ships.

<color=#FBB03F>Small items such as strike craft, modules and parts can be built in the fabricator. Larger items such as escort ships and flagships must be constructed at shipyards provided at larger stations.</color>
* QuestLine: ql_event_YaotSpring_2024_t1
* Type: Event
* EventId: event_yaotSpring_2024_t1
* Goals:
	* Task 1: Craft

### qe_yaoSpr_2024_day07_t1:
* Name: Even though pirates are still swarming the area, Chocoan and the Yaot pilgrims are adamant about continuing their travels to see the astral conjunction events. In order to deter any further attacks on the civilian ships, we should patrol and clear the systems of any significant hostile forces.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Description: Even though pirates are still swarming the area, Chocoan and the Yaot pilgrims are adamant about continuing their travels to see the astral conjunction events. In order to deter any further attacks on the civilian ships, we should patrol and clear the systems of any significant hostile forces.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* QuestLine: ql_event_YaotSpring_2024_t1
* Type: Event
* EventId: event_yaotSpring_2024_t1
* Goals:
	* Task 1: Complete side mission

### qe_yaoSpr_2024_day08_t1:
* Name: Even the Fleet of Rams are after the Yaot pilgrim's supposed treasure. If we hope to protect them, we must first convince somebody to give us more information. We should try to make friends with the pilgrims and get somebody to talk.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from dismissing officers and are earned through completing signals.</color>
* Description: Even the Fleet of Rams are after the Yaot pilgrim's supposed treasure. If we hope to protect them, we must first convince somebody to give us more information. We should try to make friends with the pilgrims and get somebody to talk.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from dismissing officers and are earned through completing signals.</color>
* QuestLine: ql_event_YaotSpring_2024_t1
* Type: Event
* EventId: event_yaotSpring_2024_t1
* Goals:
	* Task 1: GainItem

### qe_yaoSpr_2024_day09_t1:
* Name: After talking to Chocoan we suspect there is more to the Yaot pilgrimage than the religious travels to astral conjunction events. We might be able to get more information from the Yaot Federation if we do some favors.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Description: After talking to Chocoan, we suspect there is more to the Yaot pilgrimage than the religious travels to astral conjunction events. We might be able to get more information from the Yaot Federation if we do some favors.

<color=#FBB03F>There are different types of assignments available in your assignment log.</color>
* QuestLine: ql_event_YaotSpring_2024_t1
* Type: Event
* EventId: event_yaotSpring_2024_t1
* Goals:
	* Task 1: 5 T1up

### qe_yaoSpr_2024_day10_t1:
* Name: We’ve reached a dead end on collecting intelligence on the Yaot, but our source within the Tanoch Empire has offered to provide more information. We should bring an adequate gift for compensation.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
* Description: We’ve reached a dead end on collecting intelligence on the Yaot, but our source within the Tanoch Empire has offered to provide more information. We should bring an adequate gift for compensation.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
* QuestLine: ql_event_YaotSpring_2024_t1
* Type: Event
* EventId: event_yaotSpring_2024_t1
* Goals:
	* Task 1: Pay 1 None

### qe_yaoSpr_2024_day11_t1:
* Name: While we still don't know what kind of treasure the pilgrims could have aboard their vessels, Chocoan wants to move on to another astral conjunction event. He has requested our assistance in clearing out the area from any hostile threats.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Description: While we still don't know what kind of treasure the pilgrims could have aboard their vessels, Chocoan wants to move on to another astral conjunction event. He has requested our assistance in clearing out the area from any hostile threats.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* QuestLine: ql_event_YaotSpring_2024_t1
* Type: Event
* EventId: event_yaotSpring_2024_t1
* Goals:
	* Task 1: Complete side mission

### qe_yaoSpr_2024_day12_t1:
* Name: The report on the pilgrim's procedure has been fully analyzed. Usually the pilgrim's convoy moves in a tight line formation towards the optimal conjunction points where they perform their religious rituals. However, a few ships regularly diverge from the common path and move into nearby asteroid fields. We should investigate the latest conjunction site and see if we can find anything of interest.

<color=#FBB03F>Ore can be mined from asteroids in asteroid fields. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
* Description: The report on the pilgrim's procedure has been fully analyzed. Usually the pilgrim's convoy moves in a tight line formation towards the optimal conjunction points where they perform their religious rituals. However, a few ships regularly diverge from the common path and move into nearby asteroid fields. We should investigate the latest conjunction site and see if we can find anything of interest.

<color=#FBB03F>Ore can be mined from asteroids in asteroid fields. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
* QuestLine: ql_event_YaotSpring_2024_t1
* Type: Event
* EventId: event_yaotSpring_2024_t1
* Goals:
	* Task 1: GainItem

### qe_yaoSpr_2024_day13_t1:
* Name: Chocoan has informed us that the next astral conjunction site will be inside the Cangacian territories. We convinced him to take part in the operation ourselves to ensure security in this hostile area of the Empty Quarter. Maybe we will be able to both protect the pilgrims and find out more about the suspected secret agenda. We should make sure the crew is properly prepared and ready for any eventualities.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* Description: Chocoan has informed us that the next astral conjunction site will be inside the Cangacian territories. We convinced him to take part in the operation ourselves to ensure security in this hostile area of the Empty Quarter. Maybe we will be able to both protect the pilgrims and find out more about the suspected secret agenda. We should make sure the crew is properly prepared and ready for any eventualities.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* QuestLine: ql_event_YaotSpring_2024_t1
* Type: Event
* EventId: event_yaotSpring_2024_t1
* Goals:
	* Task 1: UpgradeOfficer

### qe_yaoSpr_2024_day14_t1:
* Name: Chocoan has provided the coordinates to the next astral conjunction event. Strong hostile forces are to be expected in this system. Our goal is to both protect the civilian pilgrims and find out more about the suspected secret agenda of the Yaot Elders.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Description: Chocoan has provided the coordinates to the next astral conjunction event. Strong hostile forces are to be expected in this system. Our goal is to both protect the civilian pilgrims and find out more about the suspected secret agenda of the Yaot Elders.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* QuestLine: ql_event_YaotSpring_2024_t1
* Type: Event
* EventId: event_yaotSpring_2024_t1
* Goals:
	* Task 1: Complete mission 'Conjunction T1'

## QL_EVENT_YAOTSPRING_2024_T2
### qe_yaoSpr_2024_day01_t2:
* Name: There are rumors circulating in the Empty Quarter about an increase in Cangacian pirate activity. Fleet Command asks us to gather intel from our contacts with the Iyatequa traders. We should gain some favors to bargain for information.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Description: There are rumors circulating in the Empty Quarter about an increase in Cangacian pirate activity. Fleet Command asks us to gather intel from our contacts with the Iyatequa traders. We should gain some favors to bargain for information.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* QuestLine: ql_event_YaotSpring_2024_t2
* Type: Event
* EventId: event_yaotSpring_2024_t2
* Goals:
	* Task 1: 5 Faction_Tr1_T2up

### qe_yaoSpr_2024_day02_t2:
* Name: The Iyatequa traders are involved with pirates attacking Yaot pilgrims in the Empty Quarter. We might get more information through selling equipment and arms on the open market.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
* Description: The Iyatequa traders are involved with pirates attacking Yaot pilgrims in the Empty Quarter. We might get more information through selling equipment and arms on the open market.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
* QuestLine: ql_event_YaotSpring_2024_t2
* Type: Event
* EventId: event_yaotSpring_2024_t2
* Goals:
	* Task 1: GainItem

### qe_yaoSpr_2024_day03_t2:
* Name: To learn more about the pirate raids, we should get in contact with the Yaot pilgrims. They appear to be hiding after recent attacks. We have no other option than to perform reconnaissance in the nearby systems.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
* Description: To learn more about the pirate raids, we should get in contact with the Yaot pilgrims. They appear to be hiding after recent attacks. We have no other option than to perform reconnaissance in the nearby systems.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
* QuestLine: ql_event_YaotSpring_2024_t2
* Type: Event
* EventId: event_yaotSpring_2024_t2
* Goals:
	* Task 1: Scan

### qe_yaoSpr_2024_day04_t2:
* Name: In our search for the Yaot pilgrims we have encountered intense pirate activity. We should hunt down some of their ships and see if we can gather any additional clues.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
* Description: In our search for the Yaot pilgrims we have encountered intense pirate activity. We should hunt down some of their ships and see if we can gather any additional clues.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
* QuestLine: ql_event_YaotSpring_2024_t2
* Type: Event
* EventId: event_yaotSpring_2024_t2
* Goals:
	* Task 1: GainItem

### qe_yaoSpr_2024_day05_t2:
* Name: Some Yaot survivors in our medical ward are ready to be questioned. If we manage to prove our good intentions they might help us find the Yaot pilgrimage.

<color=#FBB03F>Prestige is earned through each player level-up and by completing daily and weekly assignments.</color>
* Description: Some Yaot survivors in our medical ward are ready to be questioned. If we manage to prove our good intentions they might help us find the Yaot pilgrimage.

<color=#FBB03F>Prestige is earned through each player level-up and by completing daily and weekly assignments.</color>
* QuestLine: ql_event_YaotSpring_2024_t2
* Type: Event
* EventId: event_yaotSpring_2024_t2
* Goals:
	* Task 1: GainItem

### qe_yaoSpr_2024_day06_t2:
* Name: The Yaot have accepted our offer to support their pilgrimage. Requests have come in from ships needing spares and replacement parts for repairs. If we provide these, we might learn more about why the pirates are after these ships.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
* Description: The Yaot have accepted our offer to support their pilgrimage. Requests have come in from ships needing spares and replacement parts for repairs. If we provide these, we might learn more about why the pirates are after these ships.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
* QuestLine: ql_event_YaotSpring_2024_t2
* Type: Event
* EventId: event_yaotSpring_2024_t2
* Goals:
	* Task 1: Craft

### qe_yaoSpr_2024_day07_t2:
* Name: Even though pirates are still swarming the area, Chocoan and the Yaot pilgrims are adamant about continuing their travels to see the astral conjunction events. In order to deter any further attacks on the civilian ships, we should patrol and clear the systems of any significant hostile forces.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Description: Even though pirates are still swarming the area, Chocoan and the Yaot pilgrims are adamant about continuing their travels to see the astral conjunction events. In order to deter any further attacks on the civilian ships, we should patrol and clear the systems of any significant hostile forces.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* QuestLine: ql_event_YaotSpring_2024_t2
* Type: Event
* EventId: event_yaotSpring_2024_t2
* Goals:
	* Task 1: Complete side mission

### qe_yaoSpr_2024_day08_t2:
* Name: Even the Fleet of Rams are after the Yaot pilgrim's supposed treasure. If we hope to protect them, we must first convince somebody to give us more information. We should try to make friends with the pilgrims and get somebody to talk.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from dismissing officers and are earned through completing signals.</color>
* Description: Even the Fleet of Rams are after the Yaot pilgrim's supposed treasure. If we hope to protect them, we must first convince somebody to give us more information. We should try to make friends with the pilgrims and get somebody to talk.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from dismissing officers and are earned through completing signals.</color>
* QuestLine: ql_event_YaotSpring_2024_t2
* Type: Event
* EventId: event_yaotSpring_2024_t2
* Goals:
	* Task 1: GainItem

### qe_yaoSpr_2024_day09_t2:
* Name: After talking to Chocoan we suspect there is more to the Yaot pilgrimage than the religious travels to astral conjunction events. We might be able to get more information from the Yaot Federation if we do some favors.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Description: After talking to Chocoan we suspect there is more to the Yaot pilgrimage than the religious travels to astral conjunction events. We might be able to get more information from the Yaot Federation if we do some favors.

<color=#FBB03F>There are different types of assignments available in your assignment log.</color>
* QuestLine: ql_event_YaotSpring_2024_t2
* Type: Event
* EventId: event_yaotSpring_2024_t2
* Goals:
	* Task 1: 5 T2up

### qe_yaoSpr_2024_day10_t2:
* Name: We’ve reached a dead end on collecting intelligence on the Yaot, but our source within the Tanoch Empire has offered to provide more information. We should bring an adequate gift for compensation.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
* Description: We’ve reached a dead end on collecting intelligence on the Yaot, but our source within the Tanoch Empire has offered to provide more information. We should bring an adequate gift for compensation.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
* QuestLine: ql_event_YaotSpring_2024_t2
* Type: Event
* EventId: event_yaotSpring_2024_t2
* Goals:
	* Task 1: Pay 1 None

### qe_yaoSpr_2024_day11_t2:
* Name: While we still don't know what kind of treasure the pilgrims could have aboard their vessels, Chocoan wants to move on to another astral conjunction event. He has requested our assistance in clearing out the area from any hostile threats.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Description: While we still don't know what kind of treasure the pilgrims could have aboard their vessels, Chocoan wants to move on to another astral conjunction event. He has requested our assistance in clearing out the area from any hostile threats.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* QuestLine: ql_event_YaotSpring_2024_t2
* Type: Event
* EventId: event_yaotSpring_2024_t2
* Goals:
	* Task 1: Complete side mission

### qe_yaoSpr_2024_day12_t2:
* Name: The report on the pilgrim's procedure has been fully analyzed. Usually the pilgrim's convoy moves in a tight line formation towards the optimal conjunction points where they perform their religious rituals. However, a few ships regularly diverge from the common path and move into nearby asteroid fields. We should investigate the latest conjunction site and see if we can find anything of interest.

<color=#FBB03F>Ore can be mined from asteroids in asteroid fields. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
* Description: The report on the pilgrim's procedure has been fully analyzed. Usually the pilgrim's convoy moves in a tight line formation towards the optimal conjunction points where they perform their religious rituals. However, a few ships regularly diverge from the common path and move into nearby asteroid fields. We should investigate the latest conjunction site and see if we can find anything of interest.

<color=#FBB03F>Ore can be mined from asteroids in asteroid fields. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
* QuestLine: ql_event_YaotSpring_2024_t2
* Type: Event
* EventId: event_yaotSpring_2024_t2
* Goals:
	* Task 1: GainItem

### qe_yaoSpr_2024_day13_t2:
* Name: Chocoan has informed us that the next astral conjunction site will be inside the Cangacian territories. We convinced him to take part in the operation ourselves to ensure security in this hostile area of the Empty Quarter. Maybe we will be able to both protect the pilgrims and find out more about the suspected secret agenda. We should make sure the crew is properly prepared and ready for any eventualities.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* Description: Chocoan has informed us that the next astral conjunction site will be inside the Cangacian territories. We convinced him to take part in the operation ourselves to ensure security in this hostile area of the Empty Quarter. Maybe we will be able to both protect the pilgrims and find out more about the suspected secret agenda. We should make sure the crew is properly prepared and ready for any eventualities.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* QuestLine: ql_event_YaotSpring_2024_t2
* Type: Event
* EventId: event_yaotSpring_2024_t2
* Goals:
	* Task 1: UpgradeOfficer

### qe_yaoSpr_2024_day14_t2:
* Name: Chocoan has provided the coordinates to the next astral conjunction event. Strong hostile forces are to be expected in this system. Our goal is to both protect the civilian pilgrims and find out more about the suspected secret agenda of the Yaot Elders.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Description: Chocoan has provided the coordinates to the next astral conjunction event. Strong hostile forces are to be expected in this system. Our goal is to both protect the civilian pilgrims and find out more about the suspected secret agenda of the Yaot Elders.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* QuestLine: ql_event_YaotSpring_2024_t2
* Type: Event
* EventId: event_yaotSpring_2024_t2
* Goals:
	* Task 1: Complete mission 'Conjunction T2'

## QL_EVENT_YAOTSPRING_2024_T3
### qe_yaoSpr_2024_day01_t3:
* Name: There are rumors circulating in the Empty Quarter about an increase in Cangacian pirate activity. Fleet Command asks us to gather intel from our contacts with the Iyatequa traders. We should gain some favors to bargain for information.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Description: There are rumors circulating in the Empty Quarter about an increase in Cangacian pirate activity. Fleet Command asks us to gather intel from our contacts with the Iyatequa traders. We should gain some favors to bargain for information.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* QuestLine: ql_event_YaotSpring_2024_t3
* Type: Event
* EventId: event_yaotSpring_2024_t3
* Goals:
	* Task 1: 5 Faction_Tr1_T3up

### qe_yaoSpr_2024_day02_t3:
* Name: The Iyatequa traders are involved with pirates attacking Yaot pilgrims in the Empty Quarter. We might get more information through selling equipment and arms on the open market.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
* Description: The Iyatequa traders are involved with pirates attacking Yaot pilgrims in the Empty Quarter. We might get more information through selling equipment and arms on the open market.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
* QuestLine: ql_event_YaotSpring_2024_t3
* Type: Event
* EventId: event_yaotSpring_2024_t3
* Goals:
	* Task 1: GainItem

### qe_yaoSpr_2024_day03_t3:
* Name: To learn more about the pirate raids, we should get in contact with the Yaot pilgrims. They appear to be hiding after recent attacks. We have no other option than to perform reconnaissance in the nearby systems.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
* Description: To learn more about the pirate raids, we should get in contact with the Yaot pilgrims. They appear to be hiding after recent attacks. We have no other option than to perform reconnaissance in the nearby systems.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
* QuestLine: ql_event_YaotSpring_2024_t3
* Type: Event
* EventId: event_yaotSpring_2024_t3
* Goals:
	* Task 1: Scan

### qe_yaoSpr_2024_day04_t3:
* Name: In our search for the Yaot pilgrims we have encountered intense pirate activity. We should hunt down some of their ships and see if we can gather any additional clues.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
* Description: In our search for the Yaot pilgrims we have encountered intense pirate activity. We should hunt down some of their ships and see if we can gather any additional clues.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
* QuestLine: ql_event_YaotSpring_2024_t3
* Type: Event
* EventId: event_yaotSpring_2024_t3
* Goals:
	* Task 1: GainItem

### qe_yaoSpr_2024_day05_t3:
* Name: Some Yaot survivors in our medical ward are ready to be questioned. If we manage to prove our good intentions they might help us find the Yaot pilgrimage.

<color=#FBB03F>Prestige is earned through each player level-up and by completing daily and weekly assignments.</color>
* Description: Some Yaot survivors in our medical ward are ready to be questioned. If we manage to prove our good intentions they might help us find the Yaot pilgrimage.

<color=#FBB03F>Prestige is earned through each player level-up and by completing daily and weekly assignments.</color>
* QuestLine: ql_event_YaotSpring_2024_t3
* Type: Event
* EventId: event_yaotSpring_2024_t3
* Goals:
	* Task 1: GainItem

### qe_yaoSpr_2024_day06_t3:
* Name: The Yaot have accepted our offer to support their pilgrimage. Requests have come in from ships needing spares and replacement parts for repairs. If we provide these, we might learn more about why the pirates are after these ships.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
* Description: The Yaot have accepted our offer to support their pilgrimage. Requests have come in from ships needing spares and replacement parts for repairs. If we provide these, we might learn more about why the pirates are after these ships.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
* QuestLine: ql_event_YaotSpring_2024_t3
* Type: Event
* EventId: event_yaotSpring_2024_t3
* Goals:
	* Task 1: Craft

### qe_yaoSpr_2024_day07_t3:
* Name: Even though pirates are still swarming the area, Chocoan and the Yaot pilgrims are adamant about continuing their travels to see the astral conjunction events. In order to deter any further attacks on the civilian ships, we should patrol and clear the systems of any significant hostile forces.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Description: Even though pirates are still swarming the area, Chocoan and the Yaot pilgrims are adamant about continuing their travels to see the astral conjunction events. In order to deter any further attacks on the civilian ships, we should patrol and clear the systems of any significant hostile forces.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* QuestLine: ql_event_YaotSpring_2024_t3
* Type: Event
* EventId: event_yaotSpring_2024_t3
* Goals:
	* Task 1: Complete side mission

### qe_yaoSpr_2024_day08_t3:
* Name: Even the Fleet of Rams are after the Yaot pilgrim's supposed treasure. If we hope to protect them, we must first convince somebody to give us more information. We should try to make friends with the pilgrims and get somebody to talk.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from dismissing officers and are earned through completing signals.</color>
* Description: Even the Fleet of Rams are after the Yaot pilgrim's supposed treasure. If we hope to protect them, we must first convince somebody to give us more information. We should try to make friends with the pilgrims and get somebody to talk.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from dismissing officers and are earned through completing signals.</color>
* QuestLine: ql_event_YaotSpring_2024_t3
* Type: Event
* EventId: event_yaotSpring_2024_t3
* Goals:
	* Task 1: GainItem

### qe_yaoSpr_2024_day09_t3:
* Name: After talking to Chocoan we suspect there is more to the Yaot pilgrimage than the religious travels to astral conjunction events. We might be able to get more information from the Yaot Federation if we do some favors.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Description: After talking to Chocoan we suspect there is more to the Yaot pilgrimage than the religious travels to astral conjunction events. We might be able to get more information from the Yaot Federation if we do some favors.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* QuestLine: ql_event_YaotSpring_2024_t3
* Type: Event
* EventId: event_yaotSpring_2024_t3
* Goals:
	* Task 1: 5 Faction_Yaot_T3up

### qe_yaoSpr_2024_day10_t3:
* Name: We’ve reached a dead end on collecting intelligence on the Yaot, but our source within the Tanoch Empire has offered to provide more information. We should bring an adequate gift for compensation.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
* Description: We’ve reached a dead end on collecting intelligence on the Yaot, but our source within the Tanoch Empire has offered to provide more information. We should bring an adequate gift for compensation.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
* QuestLine: ql_event_YaotSpring_2024_t3
* Type: Event
* EventId: event_yaotSpring_2024_t3
* Goals:
	* Task 1: Pay 1 None

### qe_yaoSpr_2024_day11_t3:
* Name: While we still don't know what kind of treasure the pilgrims could have aboard their vessels, Chocoan wants to move on to another astral conjunction event. He has requested our assistance in clearing out the area from any hostile threats.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Description: While we still don't know what kind of treasure the pilgrims could have aboard their vessels, Chocoan wants to move on to another astral conjunction event. He has requested our assistance in clearing out the area from any hostile threats.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* QuestLine: ql_event_YaotSpring_2024_t3
* Type: Event
* EventId: event_yaotSpring_2024_t3
* Goals:
	* Task 1: Complete side mission

### qe_yaoSpr_2024_day12_t3:
* Name: The report on the pilgrim's procedure has been fully analyzed. Usually the pilgrim's convoy moves in a tight line formation towards the optimal conjunction points where they perform their religious rituals. However, a few ships regularly diverge from the common path and move into nearby asteroid fields. We should investigate the latest conjunction site and see if we can find anything of interest.

<color=#FBB03F>Ore can be mined from asteroids in asteroid fields. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
* Description: The report on the pilgrim's procedure has been fully analyzed. Usually the pilgrim's convoy moves in a tight line formation towards the optimal conjunction points where they perform their religious rituals. However, a few ships regularly diverge from the common path and move into nearby asteroid fields. We should investigate the latest conjunction site and see if we can find anything of interest.

<color=#FBB03F>Ore can be mined from asteroids in asteroid fields. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
* QuestLine: ql_event_YaotSpring_2024_t3
* Type: Event
* EventId: event_yaotSpring_2024_t3
* Goals:
	* Task 1: GainItem

### qe_yaoSpr_2024_day13_t3:
* Name: Chocoan has informed us that the next astral conjunction site will be inside the Cangacian territories. We convinced him to take part in the operation ourselves to ensure security in this hostile area of the Empty Quarter. Maybe we will be able to both protect the pilgrims and find out more about the suspected secret agenda. We should make sure the crew is properly prepared and ready for any eventualities.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* Description: Chocoan has informed us that the next astral conjunction site will be inside the Cangacian territories. We convinced him to take part in the operation ourselves to ensure security in this hostile area of the Empty Quarter. Maybe we will be able to both protect the pilgrims and find out more about the suspected secret agenda. We should make sure the crew is properly prepared and ready for any eventualities.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* QuestLine: ql_event_YaotSpring_2024_t3
* Type: Event
* EventId: event_yaotSpring_2024_t3
* Goals:
	* Task 1: UpgradeOfficer

### qe_yaoSpr_2024_day14_t3:
* Name: Chocoan has provided the coordinates to the next astral conjunction event. Strong hostile forces are to be expected in this system. Our goal is to both protect the civilian pilgrims and find out more about the suspected secret agenda of the Yaot Elders.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Description: Chocoan has provided the coordinates to the next astral conjunction event. Strong hostile forces are to be expected in this system. Our goal is to both protect the civilian pilgrims and find out more about the suspected secret agenda of the Yaot Elders.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* QuestLine: ql_event_YaotSpring_2024_t3
* Type: Event
* EventId: event_yaotSpring_2024_t3
* Goals:
	* Task 1: Complete mission 'Conjunction T3'

## QL_EVENT_YAOTSPRING_2024_T4
### qe_yaoSpr_2024_day01_t4:
* Name: There are rumors circulating in the Empty Quarter about an increase in Cangacian pirate activity. Fleet Command asks us to gather intel from our contacts with the Iyatequa traders. We should gain some favors to bargain for information.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Description: There are rumors circulating in the Empty Quarter about an increase in Cangacian pirate activity. Fleet Command asks us to gather intel from our contacts with the Iyatequa traders. We should gain some favors to bargain for information.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* QuestLine: ql_event_YaotSpring_2024_t4
* Type: Event
* EventId: event_yaotSpring_2024_t4
* Goals:
	* Task 1: 5 Faction_Tr1_T4up

### qe_yaoSpr_2024_day02_t4:
* Name: The Iyatequa traders are involved with pirates attacking Yaot pilgrims in the Empty Quarter. We might get more information through selling equipment and arms on the open market.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
* Description: The Iyatequa traders are involved with pirates attacking Yaot pilgrims in the Empty Quarter. We might get more information through selling equipment and arms on the open market.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
* QuestLine: ql_event_YaotSpring_2024_t4
* Type: Event
* EventId: event_yaotSpring_2024_t4
* Goals:
	* Task 1: GainItem

### qe_yaoSpr_2024_day03_t4:
* Name: To learn more about the pirate raids, we should get in contact with the Yaot pilgrims. They appear to be hiding after recent attacks. We have no other option than to perform reconnaissance in the nearby systems.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
* Description: To learn more about the pirate raids, we should get in contact with the Yaot pilgrims. They appear to be hiding after recent attacks. We have no other option than to perform reconnaissance in the nearby systems.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
* QuestLine: ql_event_YaotSpring_2024_t4
* Type: Event
* EventId: event_yaotSpring_2024_t4
* Goals:
	* Task 1: Scan

### qe_yaoSpr_2024_day04_t4:
* Name: In our search for the Yaot pilgrims we have encountered intense pirate activity. We should hunt down some of their ships and see if we can gather any additional clues.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
* Description: In our search for the Yaot pilgrims we have encountered intense pirate activity. We should hunt down some of their ships and see if we can gather any additional clues.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
* QuestLine: ql_event_YaotSpring_2024_t4
* Type: Event
* EventId: event_yaotSpring_2024_t4
* Goals:
	* Task 1: GainItem

### qe_yaoSpr_2024_day05_t4:
* Name: Some Yaot survivors in our medical ward are ready to be questioned. If we manage to prove our good intentions they might help us find the Yaot pilgrimage.

<color=#FBB03F>Prestige is earned through each player level-up and by completing daily and weekly assignments.</color>
* Description: Some Yaot survivors in our medical ward are ready to be questioned. If we manage to prove our good intentions they might help us find the Yaot pilgrimage.

<color=#FBB03F>Prestige is earned through each player level-up and by completing daily and weekly assignments.</color>
* QuestLine: ql_event_YaotSpring_2024_t4
* Type: Event
* EventId: event_yaotSpring_2024_t4
* Goals:
	* Task 1: GainItem

### qe_yaoSpr_2024_day06_t4:
* Name: The Yaot have accepted our offer to support their pilgrimage. Requests have come in from ships needing spares and replacement parts for repairs. If we provide these, we might learn more about why the pirates are after these ships.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
* Description: The Yaot have accepted our offer to support their pilgrimage. Requests have come in from ships needing spares and replacement parts for repairs. If we provide these, we might learn more about why the pirates are after these ships.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
* QuestLine: ql_event_YaotSpring_2024_t4
* Type: Event
* EventId: event_yaotSpring_2024_t4
* Goals:
	* Task 1: Craft

### qe_yaoSpr_2024_day07_t4:
* Name: Even though pirates are still swarming the area, Chocoan and the Yaot pilgrims are adamant about continuing their travels to see the astral conjunction events. In order to deter any further attacks on the civilian ships, we should patrol and clear the systems of any significant hostile forces.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Description: Even though pirates are still swarming the area, Chocoan and the Yaot pilgrims are adamant about continuing their travels to see the astral conjunction events. In order to deter any further attacks on the civilian ships, we should patrol and clear the systems of any significant hostile forces.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* QuestLine: ql_event_YaotSpring_2024_t4
* Type: Event
* EventId: event_yaotSpring_2024_t4
* Goals:
	* Task 1: Complete side mission

### qe_yaoSpr_2024_day08_t4:
* Name: Even the Fleet of Rams are after the Yaot pilgrim's supposed treasure. If we hope to protect them, we must first convince somebody to give us more information. We should try to make friends with the pilgrims and get somebody to talk.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from dismissing officers and are earned through completing signals.</color>
* Description: Even the Fleet of Rams are after the Yaot pilgrim's supposed treasure. If we hope to protect them, we must first convince somebody to give us more information. We should try to make friends with the pilgrims and get somebody to talk.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from dismissing officers and are earned through completing signals.</color>
* QuestLine: ql_event_YaotSpring_2024_t4
* Type: Event
* EventId: event_yaotSpring_2024_t4
* Goals:
	* Task 1: GainItem

### qe_yaoSpr_2024_day09_t4:
* Name: After talking to Chocoan we suspect there is more to the Yaot pilgrimage than the religious travels to astral conjunction events. We might be able to get more information from the Yaot Federation if we do some favors.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Description: After talking to Chocoan we suspect there is more to the Yaot pilgrimage than the religious travels to astral conjunction events. We might be able to get more information from the Yaot Federation if we do some favors.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* QuestLine: ql_event_YaotSpring_2024_t4
* Type: Event
* EventId: event_yaotSpring_2024_t4
* Goals:
	* Task 1: 5 Faction_Yaot_T4up

### qe_yaoSpr_2024_day10_t4:
* Name: We’ve reached a dead end on collecting intelligence on the Yaot, but our source within the Tanoch Empire has offered to provide more information. We should bring an adequate gift for compensation.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
* Description: We’ve reached a dead end on collecting intelligence on the Yaot, but our source within the Tanoch Empire has offered to provide more information. We should bring an adequate gift for compensation.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
* QuestLine: ql_event_YaotSpring_2024_t4
* Type: Event
* EventId: event_yaotSpring_2024_t4
* Goals:
	* Task 1: Pay 1 None

### qe_yaoSpr_2024_day11_t4:
* Name: While we still don't know what kind of treasure the pilgrims could have aboard their vessels, Chocoan wants to move on to another astral conjunction event. He has requested our assistance in clearing out the area from any hostile threats.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Description: While we still don't know what kind of treasure the pilgrims could have aboard their vessels, Chocoan wants to move on to another astral conjunction event. He has requested our assistance in clearing out the area from any hostile threats.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* QuestLine: ql_event_YaotSpring_2024_t4
* Type: Event
* EventId: event_yaotSpring_2024_t4
* Goals:
	* Task 1: Complete side mission

### qe_yaoSpr_2024_day12_t4:
* Name: The report on the pilgrim's procedure has been fully analyzed. Usually the pilgrim's convoy moves in a tight line formation towards the optimal conjunction points where they perform their religious rituals. However, a few ships regularly diverge from the common path and move into nearby asteroid fields. We should investigate the latest conjunction site and see if we can find anything of interest.

<color=#FBB03F>Ore can be mined from asteroids in asteroid fields. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
* Description: The report on the pilgrim's procedure has been fully analyzed. Usually the pilgrim's convoy moves in a tight line formation towards the optimal conjunction points where they perform their religious rituals. However, a few ships regularly diverge from the common path and move into nearby asteroid fields. We should investigate the latest conjunction site and see if we can find anything of interest.

<color=#FBB03F>Ore can be mined from asteroids in asteroid fields. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
* QuestLine: ql_event_YaotSpring_2024_t4
* Type: Event
* EventId: event_yaotSpring_2024_t4
* Goals:
	* Task 1: GainItem

### qe_yaoSpr_2024_day13_t4:
* Name: Chocoan has informed us that the next astral conjunction site will be inside the Cangacian territories. We convinced him to take part in the operation ourselves to ensure security in this hostile area of the Empty Quarter. Maybe we will be able to both protect the pilgrims and find out more about the suspected secret agenda. We should make sure the crew is properly prepared and ready for any eventualities.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* Description: Chocoan has informed us that the next astral conjunction site will be inside the Cangacian territories. We convinced him to take part in the operation ourselves to ensure security in this hostile area of the Empty Quarter. Maybe we will be able to both protect the pilgrims and find out more about the suspected secret agenda. We should make sure the crew is properly prepared and ready for any eventualities.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* QuestLine: ql_event_YaotSpring_2024_t4
* Type: Event
* EventId: event_yaotSpring_2024_t4
* Goals:
	* Task 1: UpgradeOfficer

### qe_yaoSpr_2024_day14_t4:
* Name: Chocoan has provided the coordinates to the next astral conjunction event. Strong hostile forces are to be expected in this system. Our goal is to both protect the civilian pilgrims and find out more about the suspected secret agenda of the Yaot Elders.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Description: Chocoan has provided the coordinates to the next astral conjunction event. Strong hostile forces are to be expected in this system. Our goal is to both protect the civilian pilgrims and find out more about the suspected secret agenda of the Yaot Elders.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* QuestLine: ql_event_YaotSpring_2024_t4
* Type: Event
* EventId: event_yaotSpring_2024_t4
* Goals:
	* Task 1: Complete mission 'Conjunction T4'

## QL_A_001
### qa_001:
* Name: No header for quest qa_001
* Description: No description for quest qa_001
* QuestLine: ql_a_001
* Type: Achievement
* Goals:
	* Task 1: 3000 Mined1A

### qa_002:
* Name: No header for quest qa_002
* Description: No description for quest qa_002
* QuestLine: ql_a_001
* Type: Achievement
* Goals:
	* Task 1: 5 Upgrade

## QL_TEST
### qt_001:
* Name: No header for quest qt_001
* Description: No description for quest qt_001
* QuestLine: ql_test
* Type: Side
* MailsOnCompletion: m_qt_001
* Goals:
	* Task 1: 
		* Pay 500 RU Type A Ore T1
		* Pay 250 RU Type B Ore T1

## QL_TEST2
### qt_002:
* Name: No header for quest qt_002
* Description: No description for quest qt_002
* QuestLine: ql_test2
* Type: Side
* Goals:
	* Task 1: Complete missions:
		* 'Wiracoda Gate'
		* 'Gulf Taln'

## QL_TEST3
### qt_003:
* Name: No header for quest qt_003
* Description: No description for quest qt_003
* QuestLine: ql_test3
* Type: Side
* Goals:
	* Task 1: GainItem

## QL_TEST4
### qt_004:
* Name: No header for quest qt_004
* Description: No description for quest qt_004
* QuestLine: ql_test4
* Type: Side
* Goals:
	* Task 1: Complete 3 side missions

## QL_TESTQUESTDIALOG
### qm_testQuestDialog:
* Name: No header for quest qm_testQuestDialog
* Description: No description for quest qm_testQuestDialog
* QuestLine: ql_testQuestDialog
* Type: Main
* Goals:
	* Task 1: Goto Medeans's system ROA TISAAD
	* Task 2: Goto Medeans's system SAARET
	* Task 3: 
		* Goto Medeans's system ROA TISAAD
		* Goto Medeans's system SAARET

## QL_TESTDISMISSOFFICERS
### qt_testDismissOfficers:
* Name: No header for quest qt_testDismissOfficers
* Description: No description for quest qt_testDismissOfficers
* QuestLine: ql_testDismissOfficers
* Type: Side
* Goals:
	* Task 1: GainItem

## QL_TEST_STRIKE_13
### qt_test_strike_13:
* Name: No header for quest qt_test_strike_13
* Description: No description for quest qt_test_strike_13
* QuestLine: ql_test_strike_13
* Type: Main
* Goals:
	* Task 1: Complete quest 'Pirate Hideout'

## QL_TEST_STRIKE_16
### qt_test_strike_16:
* Name: No header for quest qt_test_strike_16
* Description: No description for quest qt_test_strike_16
* QuestLine: ql_test_strike_16
* Type: Main
* Goals:
	* Task 1: Complete quest 'Pirate Hideout (Heroic)'

## QL_TEST_STRIKE_14
### qt_test_strike_14:
* Name: No header for quest qt_test_strike_14
* Description: No description for quest qt_test_strike_14
* QuestLine: ql_test_strike_14
* Type: Main
* Goals:
	* Task 1: Complete quest 'Station Defense'

## QL_TEST_STRIKE_17
### qt_test_strike_17:
* Name: No header for quest qt_test_strike_17
* Description: No description for quest qt_test_strike_17
* QuestLine: ql_test_strike_17
* Type: Main
* Goals:
	* Task 1: Complete quest 'Station Defense (Heroic)'

## QL_TEST_STRIKE_21
### qt_test_strike_21:
* Name: No header for quest qt_test_strike_21
* Description: No description for quest qt_test_strike_21
* QuestLine: ql_test_strike_21
* Type: Main
* Goals:
	* Task 1: Complete quest 'Station Defense (Mythic)'

## QL_TEST_STRIKE_15
### qt_test_strike_15:
* Name: No header for quest qt_test_strike_15
* Description: No description for quest qt_test_strike_15
* QuestLine: ql_test_strike_15
* Type: Main
* Goals:
	* Task 1: Complete quest 'Pahra's Rock'

## QL_TEST_STRIKE_18
### qt_test_strike_18:
* Name: No header for quest qt_test_strike_18
* Description: No description for quest qt_test_strike_18
* QuestLine: ql_test_strike_18
* Type: Main
* Goals:
	* Task 1: Complete quest 'Pahra's Rock (Heroic)'

## QL_TEST_STRIKE_22
### qt_test_strike_22:
* Name: No header for quest qt_test_strike_22
* Description: No description for quest qt_test_strike_22
* QuestLine: ql_test_strike_22
* Type: Main
* Goals:
	* Task 1: Complete quest 'Pahra's Rock (Mythic)'

## QL_TEST_STRIKE_19
### qt_test_strike_19:
* Name: No header for quest qt_test_strike_19
* Description: No description for quest qt_test_strike_19
* QuestLine: ql_test_strike_19
* Type: Main
* Goals:
	* Task 1: Complete quest 'Breach'

## QL_TEST_STRIKE_20
### qt_test_strike_20:
* Name: No header for quest qt_test_strike_20
* Description: No description for quest qt_test_strike_20
* QuestLine: ql_test_strike_20
* Type: Main
* Goals:
	* Task 1: Complete quest 'Breach (Heroic)'

## Q_TEST_YAO_SPRING
### q_test_yaoSpr_2024_day04_t4:
* Name: No header for quest q_test_yaoSpr_2024_day04_t4
* Description: No description for quest q_test_yaoSpr_2024_day04_t4
* QuestLine: q_test_yao_spring
* Type: Side
* Goals:
	* Task 1: GainItem

## QL_COMPENSATION_LVLUP
### q_compensation_lvl_10:
* Name: Fame and Honor (Lvl 10)
* Description: Player XP can be gained from completing missions and assignments and from destroying enemy units.
* QuestLine: ql_compensation_lvlup
* Type: Event
* EventId: event_levelUpCompensationQuests
* Goals:
	* Task 1: 12600 PlayerXP

### q_compensation_lvl_20:
* Name: Fame and Honor (Lvl 20)
* Description: Player XP can be gained from completing missions and assignments and from destroying enemy units.
* QuestLine: ql_compensation_lvlup
* Type: Event
* EventId: event_levelUpCompensationQuests
* Goals:
	* Task 1: 36100 PlayerXP

### q_compensation_lvl_35:
* Name: Fame and Honor (Lvl 35)
* Description: Player XP can be gained from completing missions and assignments and from destroying enemy units.
* QuestLine: ql_compensation_lvlup
* Type: Event
* EventId: event_levelUpCompensationQuests
* Goals:
	* Task 1: 90100 PlayerXP

### q_compensation_lvl_50:
* Name: Fame and Honor (Lvl 50)
* Description: Player XP can be gained from completing missions and assignments and from destroying enemy units.
* QuestLine: ql_compensation_lvlup
* Type: Event
* EventId: event_levelUpCompensationQuests
* Goals:
	* Task 1: 166600 PlayerXP

### q_compensation_lvl_75:
* Name: Fame and Honor (Lvl 75)
* Description: Player XP can be gained from completing missions and assignments and from destroying enemy units.
* QuestLine: ql_compensation_lvlup
* Type: Event
* EventId: event_levelUpCompensationQuests
* Goals:
	* Task 1: 344100 PlayerXP

### q_compensation_lvl_100:
* Name: Fame and Honor (Lvl 100)
* Description: Player XP can be gained from completing missions and assignments and from destroying enemy units.
* QuestLine: ql_compensation_lvlup
* Type: Event
* EventId: event_levelUpCompensationQuests
* Goals:
	* Task 1: 584100 PlayerXP

### q_compensation_lvl_150:
* Name: Fame and Honor (Lvl 150)
* Description: Player XP can be gained from completing missions and assignments and from destroying enemy units.
* QuestLine: ql_compensation_lvlup
* Type: Event
* EventId: event_levelUpCompensationQuests
* Goals:
	* Task 1: 1251600 PlayerXP

### q_compensation_lvl_200:
* Name: Fame and Honor (Lvl 200)
* Description: Player XP can be gained from completing missions and assignments and from destroying enemy units.
* QuestLine: ql_compensation_lvlup
* Type: Event
* EventId: event_levelUpCompensationQuests
* Goals:
	* Task 1: 2169100 PlayerXP

### q_compensation_lvl_300:
* Name: Fame and Honor (Lvl 300)
* Description: Player XP can be gained from completing missions and assignments and from destroying enemy units.
* QuestLine: ql_compensation_lvlup
* Type: Event
* EventId: event_levelUpCompensationQuests
* Goals:
	* Task 1: 4754100 PlayerXP

## QL_TEST_GGF_STORY
### qs_s2_01_sijinLighthouse:
* Name: Sijin Lighthouse
* Description: We detected a possible signal from the missing Khar-Kalaad.
* QuestLine: ql_test_ggf_story
* Type: Side
* FollowUps: ql_raid_019
* Goals:
	* Task 1: Complete mission 'Sijin Lighthouse'

### qs_s2_01_iliyinLighthouse:
* Name: Iliyin Lighthouse
* Description: We have arrived at another lighthouse in uncharted territory. Be prepared for anything.
* QuestLine: ql_test_ggf_story
* Type: Side
* Goals:
	* Task 1: Complete mission 'Iliyin Lighthouse'

### qs_s2_01_bTemple:
* Name: Bright Temple
* Description: The Amassari here may have answers about the nature of the Progenitor observer.
* QuestLine: ql_test_ggf_story
* Type: Side
* Goals:
	* Task 1: Complete mission 'Bright Temple'

### qs_s2_01_hataldan:
* Name: Hataldan
* Description: The fallen capital of the Amassari, and last known position of the Observer.
* QuestLine: ql_test_ggf_story
* Type: Side
* FollowUps: ql_raid_020
* Goals:
	* Task 1: Complete mission 'Hataldan'
