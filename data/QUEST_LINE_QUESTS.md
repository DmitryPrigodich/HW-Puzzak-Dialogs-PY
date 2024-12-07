# HWM QUESTLINES WITH QUESTS


## QL_MAIN_T0_TUTORIAL
### qm_t0_tutMissions:
* Name:	Landing
* Description:	Our arrival in this galaxy was met with tragedy.
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
### qm_t0_introStation:
* Name:	Lazarus Station
* Description:	We were given the coordinates of a local Hiigaran settlement. We should go there.
* Type:	Main
* Goals:
	* 0:
		* GoalType: Goto
			* Target: [-1822, -636]
			* TargetMode: Station

### qm_t0_introMarket:
* Name:	Local Currency
* Description:	The market can be accessed at stations and inside the flagship, though the selection of items in the flagship market is smaller. For now, we need to pick up some local currency to barter with the locals.
* Type:	Main
* FollowUps: ql_main_t0_strikeCraft
* Goals:
	* 0:
		* GoalType: Buy
			* Id: pack_market_freeHC_insta

## QL_MAIN_T0_STRIKECRAFT
### qm_t0_introFabricator:
* Name:	Fabricator
* Description:	Our fabricators are operational again. We should produce more strike craft in case we run into more hostiles.
* Type:	Main
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: Interceptor
			* Amount: 1

### qm_t0_introEquipStrikecraft:
* Name:	Strike Craft
* Description:	We need to ready our strike craft inside our hangars.
* Type:	Main
* FollowUps: ql_main_t0_v2_signals
* Goals:
	* 0:
		* GoalType: Equip
			* Type: Squad

## QL_MAIN_T0_V2_SIGNALS
### qm_t0_v2_introScanning:
* Name:	Scanning
* Description:	We have been asked to take care of a local threat to the Lazarus Station. We need to find out where it is.
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

### qm_t0_v2_introSignals:
* Name:	Signals
* Description:	We have found hostile signals in the system. We need to clear it out and return to Lazarus Station.
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
### qm_t0_introScanBelts:
* Name:	Asteroid Clusters
* Description:	We've been asked by Lazarus Station to help with resource scarcity. We'll need to find suitable mining opportunities by scanning for mineral-rich asteroids in nearby systems.
* Type:	Main
* Goals:
	* 0:
		* GoalType: Goto
			* Target: [-1747, -653]
	* 1:
		* GoalType: Statistic
			* Id: ScannedBelt
			* Total: 1

### qm_t0_introMining:
* Name:	Mining
* Description:	We found a suitable spot for mining. Use the resource collector to mine the mineral rich asteroids.
* Type:	Main
* FollowUps: ql_main_t0_support
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: Mined0A
			* Amount: 50

## QL_MAIN_T0_SUPPORT
### qm_t0_support:
* Name:	Support
* Description:	Now that we have the needed minerals, we should go back to Lazarus Station to deliver them.
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
### qm_t0_introBridge:
* Name:	Bridge
* Description:	Gideon S'jet has offered his Progenitor expertise. We should appoint him as head of science on the bridge.
* Type:	Main
* FollowUps: ql_main_t0_escorts
* Goals:
	* 0:
		* GoalType: Equip
			* Type: Officer
			* Location: Bridge

## QL_MAIN_T0_ESCORTS
### qm_t0_introShipyard:
* Name:	Shipyard
* Description:	We have clearance to use the shipyards of Lazarus Station. We should build an additional assault frigate there to bolster our fleet.
* Type:	Main
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: AssaultFrigate
			* Amount: 1

### qm_t0_introEquipEscorts:
* Name:	Escort Ships
* Description:	Our new assault frigate needs to be staffed and readied. We can do that at any station through Fleet Configuration.
* Type:	Main
* FollowUps: ql_main_t0_sideProg
* Goals:
	* 0:
		* GoalType: Equip
			* Type: Escort

## QL_MAIN_T0_SIDEPROG
### qm_t0_scientist_Baaekh_A:
* Name:	Baaekh S’jet
* Description:	Baaekh S’jet was one of the foremost scientists on Progenitor culture. According to Gideon she has data that can help us with our own research into the Progenitors.
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

### qm_t0_scientist_Baaekh_B:
* Name:	Rescue Mission
* Description:	We found Baaekh S'jet, but she can't come out of hiding until we have distracted the hostiles in the area.
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
### qm_t0_relic:
* Name:	Relic Retrieval
* Description:	With information provided by Baaekh S’jet, we now know a potential location of a Progenitor Relic in Toasiim that must be retrieved.
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
### qm_t0_scientist_Hyeaa_A:
* Name:	Hyeaa Somtaaw
* Description:	Hyeaa Somtaaw was an expert in Progenitor Materials sciences. He has established an independent lab at Nokuuna. According to Gideon, he has data that can help us with our own research into the Progenitors.
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
### qm_t0_scientist_Hyeaa_B:
* Name:	Process Investigation
* Description:	Hyeaa Somtaaw wants to investigate our fabrication processes, find a way to improve it by incorporating Progenitor technology. In return he will share his data with us.
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

### qm_t1_facHiigaran_A:
* Name:	Outposts: Rescue
* Description:	Long-range sensors located near another hyperspace gate have registered the presence of a Hiigaran fleet that emerged here. We are asked to this location and try to help any survivors as best as we can.
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

### qm_t1_facHiigaran_B:
* Name:	Outposts: Recon
* Description:	To supply the needs of the Hiigaran fleet, we've been dispatched to look for a great mining source. Intel indicates this will put us into direct conflict with the Fleet of Rams.
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

### qm_t1_facHiigaran_C:
* Name:	Outposts: Wall of Will
* Description:	One of the only planetary settlements under Hiigaran control has been scouted by the Fleet of Rams. Until the planetary defenses are strengthened, they need military equipment to supply the defense.
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

### qm_t1_facHiigaran_D:
* Name:	Outposts: Security
* Description:	Hiigaran forces are working to clear systems to set up for colonization. The system in question is of special importance. We've been asked to go there and assist in securing the area.
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

### qm_t1_facCangacian_A:
* Name:	Troubles: Defiance
* Description:	The world of Huaca is looking for help. They are opposing conscription from Supay’s Fleet of Rams, the punishment of which is brutal assault.
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

### qm_t1_facCangacian_B:
* Name:	Troubles: Seeker
* Description:	To oppose the Fleet of Rams, we were asked to undergo a mission to survey and map one of their three largest systems. We should also sabotage their efforts when the opportunity presents itself.
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

### qm_t1_facCangacian_C:
* Name:	Troubles: Stone Hearth
* Description:	We're asked to to assist the system of Acheron. They do not have a refinery set up, so we need to go there and refine metals for their construction facilities to use.
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

### qm_t1_facCangacian_D:
* Name:	Troubles: A Black Eye
* Description:	The Fleet of Rams is assembling an assault force that is aimed at a cluster of neutral systems. Intel shows that another Cangacian band plans to engage Supay’s commanding lieutenant here. We're asked to create a distraction to weaken the Fleet of Rams in the resulting battle.
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

### qm_t1_facProgenitors_A:
* Name:	Components: A Wide Exchange
* Description:	A few locals in this system have Progenitor technology they willing to hand to us if we agree to help them with their own problems regarding hostile Progenitor vessels and shortage of resources.
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

### qm_t1_facProgenitors_B:
* Name:	Components: Hunt
* Description:	Progenitor vessels in this area are equipped with M-type fuses. We need to attack and destroy a few vessels in order to gather enough of quality for use in the prototype.
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

### qm_t1_facProgenitors_C:
* Name:	Components: A Full Quiver
* Description:	Fleet command out of Lazarus frowns upon commanders that delve into Progenitor ruins without a minimum of protection. We need to bring our ship up to code and command will approve our ship for such operations in the future.
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

### qm_t1_facProgenitors_D:
* Name:	Components: Repurpose the Past
* Description:	To save time, rather than reconstruct a Particle density array, we can salvage one from advanced Progenitor craft. We need to attack enough Progenitor ships to find one that is in decent condition. The module will require rare earths in order to activate properly. We can gather them at the system as well.
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

### qm_t1_facIyatequa_A:
* Name:	Business: An Honest Job
* Description:	The Iyatequa asked us to perform a variety of simple activities and allowing them to monitor the related systems for their own research purposes.
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

### qm_t1_facIyatequa_B:
* Name:	Business: The Barrier
* Description:	We've been told to deal with an attempted trade blockade set up by pirates. We will need to get some spare resources and some module upgrades before we face the enemy.
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

### qm_t1_facIyatequa_C:
* Name:	Business: The Sheriff
* Description:	Hostiles have been gathering near Iyatequa trading routes. We've been asked to investigate and root out pirates and other undesirables.
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

### qm_t1_facIyatequa_D:
* Name:	Business: The Dealer
* Description:	A dealer supplying the Iyatequa has tried cutting corners and incured their wrath. We've been asked to apprehend him.
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

### qm_t2_facCangacian_A:
* Name:	Incursion: Reverse Engineering
* Description:	This colony was attacked by vessels incorporating non-Cangacian technology. We're asked to try to reverse engineer some of it.
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

### qm_t2_facCangacian_B:
* Name:	Incursion: Rebuilding Efforts
* Description:	This colony was hit hard. We need to clear the area of remaining pirates and help with rebuilding.
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

### qm_t2_facCangacian_C:
* Name:	Incursion: Enemy Intentions
* Description:	This colony repelled the attackers and gathered some intel. They need our help to decrypt it and find safe places for mining.
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

### qm_t2_facCangacian_D:
* Name:	Incursion: Preemptive Strike
* Description:	The most recent attack. Intel shows it was just a scouting mission. We need to help with setting up quick defenses and take out the assault fleet before they can strike.
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

### qm_t2_facHiigaran_A:
* Name:	Repairs: Mining Opportunities
* Description:	To repair Lazarus Station, new minerals are needed. We are asked to look for new places to mine and help set up the fabrication systems.
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

### qm_t2_facHiigaran_B:
* Name:	Repairs: Secure the Perimeter
* Description:	After the recent attack, we need to secure the borders of Hiigaran space.
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

### qm_t2_facHiigaran_C:
* Name:	Repairs: Motivation Boost
* Description:	We are asked to lead several high profile campaigns against enemy forces to rally more Hiigaran fleets and raise awareness to the rebuilding efforts of Lazarus Station.

(The blueprints for small Weapon and Machinery parts can be found in the market.)
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

### qm_t2_facHiigaran_D:
* Name:	Repairs: Empty the Lairs
* Description:	The attackers still have their bases of operation. We need to clear them out to prevent future attacks.
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

### qm_t2_facIyatequa_A:
* Name:	Intermediary: Delivery Run
* Description:	The Iyatequa want us to deliver some resources - from our own pockets. They said the rewards will compensate for our losses. We'll see.
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

### qm_t2_facIyatequa_B:
* Name:	Intermediary: Patrolling Trade Routes
* Description:	We're asked to patrol the Iyatequa trading routes and clear out hostiles near them.
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

### qm_t2_facIyatequa_C:
* Name:	Intermediary: The Catch
* Description:	This assignment seems simple enough. We simply have to find Cangacian fleets and destroy them.
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

### qm_t2_facIyatequa_D:
* Name:	Intermediary: Art of Escape
* Description:	The Iyatequa want us to find a master thief of legendary reputation.
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

### qm_t2_internalRefinery:
* Name:	Refinery Module
* Description:	Additional refinery and fabricator modules increase our economic power.
* Type:	Main
* Goals:
	* 0:
		* GoalType: Craft
			* Tags: Refining_Factory
	* 1:
		* GoalType: Equip
			* Type: Internal
			* Tags: Refining_Factory

### qm_t2_facTanoch_A:
* Name:	Errands: Golden Harvest
* Description:	A Tanoch planetary government is experiencing a resource shortfall, and has asked for help with procuring raw material.
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

### qm_t2_facTanoch_B:
* Name:	Errands: Safety and Security
* Description:	Pirates are attacking Tanoch systems. We've been asked to drive them back.
* Type:	Side
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: RepTanoch
			* Amount: 350
		* GoalType: Statistic
			* Id: ShipsDestroyedP1
			* Amount: 15

### qm_t2_facTanoch_C:
* Name:	Errands: Disaster Relief
* Description:	A Tanoch world is having trouble getting resources from the Empire so they’ve asked anyone for help.
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

### qm_t2_facTanoch_D:
* Name:	Errands: Hired Defenses
* Description:	The border worlds are being threatened from Yaot assaults and are desperate for defenders. They ask us to drive the Yaot back.
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

### qm_t2_facYaot_A:
* Name:	Conflict: Direct Attack
* Description:	The Tanoch want us to actively engage the Yaot fleets to disrupt their activities in Tanoch space.
* Type:	Side
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedYaot
			* Amount: 30

### qm_t2_facYaot_B:
* Name:	Conflict: Hazardous Archeology
* Description:	We are looking for evidence of a missing Progenitor hyperspace gate in the area which should be there but isn’t. According to Tanoch intelligence the Yaot are also seeking this object.
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

### qm_t2_facYaot_C:
* Name:	Conflict: Seek and Find
* Description:	A Hiigaran flagship has gone missing in Tanoch space. Preliminary evidence points towards Yaot involvement. Lazarus wants us to investigate.
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

### qm_t2_facYaot_D:
* Name:	Conflict: Opposition Research
* Description:	The Yaot are the first major antagonistic power we have encountered. We need to make sure our crew is properly trained and ready to handle the upcoming battles.
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

### qs_unlockStrikes_t1:
* Name:	Rising to the Challenge
* Description:	As we venture further into this galaxy, we will encounter greater and greater threats. We need to be prepared.
* Type:	Side
* Goals:
	* 0:
		* GoalType: Goto
			* Target: [-1535, -436]
			* MoveType: InSystem
	* 1:
		* GoalType: Scan
			* : 

### qt_daily_buy:
* Name:	Big Spender
* Description:	You can buy resources or items in the market as well as in the liaison requisitions.
* Type:	Daily
* Goals:
	* 0:
		* GoalType: Buy
			* Amount: 1

### qt_daily_mine:
* Name:	Primary Sector
* Description:	Ores can be mined in asteroid clusters, while gas is harvested from jovians.
* Type:	Daily
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: Mined
			* Amount: 1500

### qt_daily_refine:
* Name:	Metallurgy
* Description:	Refining ores is required to turn them into usable metals for the production process.
* Type:	Daily
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Refining
			* Amount: 500

### qt_daily_craft:
* Name:	Means of Production
* Description:	You can fabricate all sorts of products in your flagship's factories.
* Type:	Daily
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Amount: 10

### qt_daily_gainRP:
* Name:	Hoarding Knowledge
* Description:	Research points are passively collected in your flagship's laboratories. They are needed to conduct research.
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

### qt_daily_insignias:
* Name:	Distinction
* Description:	You can earn insignias by completing missions. They are needed to promote your officers, which increases their attributes.
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

### qt_daily_liaison:
* Name:	Adventurism
* Description:	Completing missions gives you XP to level up.
* Type:	Daily
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3

### qt_daily_destroy:
* Name:	Trophies
* Description:	Destroyed enemy vessels sometimes leave salvage behind which may contain resources.
* Type:	Daily
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyed
			* Amount: 15

### qt_daily_signals:
* Name:	New Discoveries
* Description:	Some objects require to be scanned several times to reveal them fully.
* Type:	Daily
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem
			* Amount: 5
			* Analyzed: True

### qt_daily_dailyMission:
* Name:	Bragging Rights
* Description:	A strike is a great opportunity to test your strength and train your coordination with other commanders.
* Type:	Daily
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Mode: Strike

### qt_daily_dailies:
* Name:	Periodic Activity
* Description:	Most daily and weekly assignments grant Prestige, which can be used in the prestige section of the market to acquire special blueprints and other items.
* Type:	Daily
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 8
			* Tags: Daily

### qt_weekly_dailies:
* Name:	Assiduity
* Description:	Daily assignments refresh once a day, make sure to claim your reward before that happens.
* Type:	Weekly
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 40
			* Tags: Daily

### qt_weekly_reputation:
* Name:	Connections
* Description:	Completing liaison assignments improves your standing with that particular faction, which in turn unlocks new items in their liaison requisitions.
* Type:	Weekly
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 9
			* Tags: Faction

### qt_weekly_clanQuests:
* Name:	Stronger Together
* Description:	You can only complete clan assignments while you are inside a clan. Completing these grants you clan credits as well as clan supplies for the whole clan.
* Type:	Weekly
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 10
			* Tags: Clan

### qt_weekly_levelOfficers:
* Name:	Ranks and File
* Description:	After reaching enough levels, officers will gain a new rank, which increases their abilities.
* Type:	Weekly
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 7

### qt_weekly_upgrades:
* Name:	Marvels of Engineering
* Description:	Module upgrades need rare earth materials and can only be done at a trading station.
* Type:	Weekly
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Upgrade
			* Amount: 10

### qt_weekly_missions:
* Name:	Signal Sweep
* Description:	New signals may appear through scanning after you have cleared out a few.
* Type:	Weekly
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 9
			* Mode: Generated

### qt_weekly_research:
* Name:	Scientific Method
* Description:	Research is conducted inside your flagship's laboratories.
* Type:	Weekly
* Goals:
	* 0:
		* GoalType: Craft
			* Tags: Research
			* Amount: 5

### qe_amaSum_2023_daily_A_t1:
* Name:	No header for quest qe_amaSum_2023_daily_A_t1
* Description:	No description for quest qe_amaSum_2023_daily_A_t1
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

### qe_amaSum_2023_daily_B_t1:
* Name:	No header for quest qe_amaSum_2023_daily_B_t1
* Description:	No description for quest qe_amaSum_2023_daily_B_t1
* Type:	Event
* EventId:	event_season_amaSum_2023_t1
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: T1up
			* Amount: 1

### qe_amaSum_2023_daily_C_t1:
* Name:	No header for quest qe_amaSum_2023_daily_C_t1
* Description:	No description for quest qe_amaSum_2023_daily_C_t1
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

### qe_amaSum_2023_daily_D_t1:
* Name:	No header for quest qe_amaSum_2023_daily_D_t1
* Description:	No description for quest qe_amaSum_2023_daily_D_t1
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

### qe_amaSum_2023_daily_A_t2:
* Name:	No header for quest qe_amaSum_2023_daily_A_t2
* Description:	No description for quest qe_amaSum_2023_daily_A_t2
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

### qe_amaSum_2023_daily_B_t2:
* Name:	No header for quest qe_amaSum_2023_daily_B_t2
* Description:	No description for quest qe_amaSum_2023_daily_B_t2
* Type:	Event
* EventId:	event_season_amaSum_2023_t2
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: Part_T2up
			* Amount: 25

### qe_amaSum_2023_daily_C_t2:
* Name:	No header for quest qe_amaSum_2023_daily_C_t2
* Description:	No description for quest qe_amaSum_2023_daily_C_t2
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

### qe_amaSum_2023_daily_D_t2:
* Name:	No header for quest qe_amaSum_2023_daily_D_t2
* Description:	No description for quest qe_amaSum_2023_daily_D_t2
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

### qe_amaSum_2023_daily_A_t3:
* Name:	No header for quest qe_amaSum_2023_daily_A_t3
* Description:	No description for quest qe_amaSum_2023_daily_A_t3
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

### qe_amaSum_2023_daily_B_t3:
* Name:	No header for quest qe_amaSum_2023_daily_B_t3
* Description:	No description for quest qe_amaSum_2023_daily_B_t3
* Type:	Event
* EventId:	event_season_amaSum_2023_t3
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: Part_T3up
			* Amount: 25

### qe_amaSum_2023_daily_C_t3:
* Name:	No header for quest qe_amaSum_2023_daily_C_t3
* Description:	No description for quest qe_amaSum_2023_daily_C_t3
* Type:	Event
* EventId:	event_season_amaSum_2023_t3
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedDarkHiigaranT3
				* ShipsDestroyedDarkHiigaranT4
			* Amount: 10

### qe_amaSum_2023_daily_D_t3:
* Name:	No header for quest qe_amaSum_2023_daily_D_t3
* Description:	No description for quest qe_amaSum_2023_daily_D_t3
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

### qe_amaSum_2023_daily_A_t4:
* Name:	No header for quest qe_amaSum_2023_daily_A_t4
* Description:	No description for quest qe_amaSum_2023_daily_A_t4
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

### qe_amaSum_2023_daily_B_t4:
* Name:	No header for quest qe_amaSum_2023_daily_B_t4
* Description:	No description for quest qe_amaSum_2023_daily_B_t4
* Type:	Event
* EventId:	event_season_amaSum_2023_t4
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: Part_T4up
			* Amount: 25

### qe_amaSum_2023_daily_C_t4:
* Name:	No header for quest qe_amaSum_2023_daily_C_t4
* Description:	No description for quest qe_amaSum_2023_daily_C_t4
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

### qe_amaSum_2023_daily_D_t4:
* Name:	No header for quest qe_amaSum_2023_daily_D_t4
* Description:	No description for quest qe_amaSum_2023_daily_D_t4
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

### qe_7days_mar_2024_daily_A_t1:
* Name:	Finds must be discovered through scanning. After being analyzed, they can be picked up to collect the reward inside.
* Description:	Finds must be discovered through scanning. After being analyzed, they can be picked up to collect the reward inside.
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t1
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_Container_T1up
			* Amount: 1
			* Analyzed: True

### qe_7days_mar_2024_daily_A_t2:
* Name:	Finds must be discovered through scanning. After being analyzed, they can be picked up to collect the reward inside.
* Description:	Finds must be discovered through scanning. After being analyzed, they can be picked up to collect the reward inside.
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t2
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_Container_T2up
			* Amount: 1
			* Analyzed: True

### qe_7days_mar_2024_daily_A_t3:
* Name:	Finds must be discovered through scanning. After being analyzed, they can be picked up to collect the reward inside.
* Description:	Finds must be discovered through scanning. After being analyzed, they can be picked up to collect the reward inside.
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t3
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_Container_T3up
			* Amount: 1
			* Analyzed: True

### qe_7days_mar_2024_daily_A_t4:
* Name:	Finds must be discovered through scanning. After being analyzed, they can be picked up to collect the reward inside.
* Description:	Finds must be discovered through scanning. After being analyzed, they can be picked up to collect the reward inside.
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t4
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_Container_T4up
			* Amount: 1
			* Analyzed: True

### qe_7days_mar_2024_daily_B_t1:
* Name:	Progenitor relics can be found in relic signature signals.
* Description:	Progenitor relics can be found in relic signature signals.
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t1
* Goals:
	* 0:
		* GoalType: Pay
			* Id: questItem_progenitorRelic_t1
			* Amount: 1

### qe_7days_mar_2024_daily_B_t2:
* Name:	Progenitor relics can be found in relic signature signals.
* Description:	Progenitor relics can be found in relic signature signals.
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t2
* Goals:
	* 0:
		* GoalType: Pay
			* Id: questItem_progenitorRelic_t2
			* Amount: 1

### qe_7days_mar_2024_daily_B_t3:
* Name:	Progenitor relics can be found in relic signature signals.
* Description:	Progenitor relics can be found in relic signature signals.
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t3
* Goals:
	* 0:
		* GoalType: Pay
			* Id: questItem_progenitorRelic_t3
			* Amount: 1

### qe_7days_mar_2024_daily_B_t4:
* Name:	Progenitor relics can be found in relic signature signals.
* Description:	Progenitor relics can be found in relic signature signals.
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t4
* Goals:
	* 0:
		* GoalType: Pay
			* Id: questItem_progenitorRelic_t4
			* Amount: 1

### qe_7days_mar_2024_daily_C_t1:
* Name:	Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.
* Description:	Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Rare_T1up
			* Mode: Generated

### qe_7days_mar_2024_daily_C_t2:
* Name:	Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.
* Description:	Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Epic_T2up
			* Mode: Generated

### qe_7days_mar_2024_daily_C_t3:
* Name:	Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.
* Description:	Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Epic_T3up
			* Mode: Generated

### qe_7days_mar_2024_daily_C_t4:
* Name:	Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.
* Description:	Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Epic_T4up
			* Mode: Generated

### qe_7days_mar_2024_daily_D_t1:
* Name:	Prestige is earned through each player level-up and by completing daily and weekly assignments.
* Description:	Prestige is earned through each player level-up and by completing daily and weekly assignments.
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

### qe_7days_mar_2024_daily_D_t2:
* Name:	Prestige is earned through each player level-up and by completing daily and weekly assignments.
* Description:	Prestige is earned through each player level-up and by completing daily and weekly assignments.
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

### qe_7days_mar_2024_daily_D_t3:
* Name:	Prestige is earned through each player level-up and by completing daily and weekly assignments.
* Description:	Prestige is earned through each player level-up and by completing daily and weekly assignments.
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

### qe_7days_mar_2024_daily_D_t4:
* Name:	Prestige is earned through each player level-up and by completing daily and weekly assignments.
* Description:	Prestige is earned through each player level-up and by completing daily and weekly assignments.
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

### qe_iyaFal_2023_daily_A_t1:
* Name:	No header for quest qe_iyaFal_2023_daily_A_t1
* Description:	No description for quest qe_iyaFal_2023_daily_A_t1
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

### qe_iyaFal_2023_daily_B_t1:
* Name:	No header for quest qe_iyaFal_2023_daily_B_t1
* Description:	No description for quest qe_iyaFal_2023_daily_B_t1
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

### qe_iyaFal_2023_daily_C_t1:
* Name:	No header for quest qe_iyaFal_2023_daily_C_t1
* Description:	No description for quest qe_iyaFal_2023_daily_C_t1
* Type:	Event
* EventId:	event_season_iyaFal_2023_t1
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_T1up
			* Amount: 10
			* Analyzed: True

### qe_iyaFal_2023_daily_D_t1:
* Name:	No header for quest qe_iyaFal_2023_daily_D_t1
* Description:	No description for quest qe_iyaFal_2023_daily_D_t1
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

### qe_iyaFal_2023_daily_A_t2:
* Name:	No header for quest qe_iyaFal_2023_daily_A_t2
* Description:	No description for quest qe_iyaFal_2023_daily_A_t2
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

### qe_iyaFal_2023_daily_B_t2:
* Name:	No header for quest qe_iyaFal_2023_daily_B_t2
* Description:	No description for quest qe_iyaFal_2023_daily_B_t2
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

### qe_iyaFal_2023_daily_C_t2:
* Name:	No header for quest qe_iyaFal_2023_daily_C_t2
* Description:	No description for quest qe_iyaFal_2023_daily_C_t2
* Type:	Event
* EventId:	event_season_iyaFal_2023_t2
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_T2up
			* Amount: 10
			* Analyzed: True

### qe_iyaFal_2023_daily_D_t2:
* Name:	No header for quest qe_iyaFal_2023_daily_D_t2
* Description:	No description for quest qe_iyaFal_2023_daily_D_t2
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

### qe_iyaFal_2023_daily_A_t3:
* Name:	No header for quest qe_iyaFal_2023_daily_A_t3
* Description:	No description for quest qe_iyaFal_2023_daily_A_t3
* Type:	Event
* EventId:	event_season_iyaFal_2023_t3
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedP1T3
				* ShipsDestroyedP1T4
			* Amount: 10

### qe_iyaFal_2023_daily_B_t3:
* Name:	No header for quest qe_iyaFal_2023_daily_B_t3
* Description:	No description for quest qe_iyaFal_2023_daily_B_t3
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

### qe_iyaFal_2023_daily_C_t3:
* Name:	No header for quest qe_iyaFal_2023_daily_C_t3
* Description:	No description for quest qe_iyaFal_2023_daily_C_t3
* Type:	Event
* EventId:	event_season_iyaFal_2023_t3
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_T3up
			* Amount: 10
			* Analyzed: True

### qe_iyaFal_2023_daily_D_t3:
* Name:	No header for quest qe_iyaFal_2023_daily_D_t3
* Description:	No description for quest qe_iyaFal_2023_daily_D_t3
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

### qe_iyaFal_2023_daily_A_t4:
* Name:	No header for quest qe_iyaFal_2023_daily_A_t4
* Description:	No description for quest qe_iyaFal_2023_daily_A_t4
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

### qe_iyaFal_2023_daily_B_t4:
* Name:	No header for quest qe_iyaFal_2023_daily_B_t4
* Description:	No description for quest qe_iyaFal_2023_daily_B_t4
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

### qe_iyaFal_2023_daily_C_t4:
* Name:	No header for quest qe_iyaFal_2023_daily_C_t4
* Description:	No description for quest qe_iyaFal_2023_daily_C_t4
* Type:	Event
* EventId:	event_season_iyaFal_2023_t4
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_T4up
			* Amount: 10
			* Analyzed: True

### qe_iyaFal_2023_daily_D_t4:
* Name:	No header for quest qe_iyaFal_2023_daily_D_t4
* Description:	No description for quest qe_iyaFal_2023_daily_D_t4
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

### qe_anniversary_2023_daily_A_t1:
* Name:	Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
* Description:	Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
* Type:	Event
* EventId:	event_anniversary_2023_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 5
			* Tags: T1up
			* Mode: Generated

### qe_anniversary_2023_daily_B_t1:
* Name:	Rare earths are an occasional by-product of refining. They are required for upgrading modules.
* Description:	Rare earths are an occasional by-product of refining. They are required for upgrading modules.
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

### qe_anniversary_2023_daily_A_t2:
* Name:	Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
* Description:	Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
* Type:	Event
* EventId:	event_anniversary_2023_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 5
			* Tags: T2up
			* Mode: Generated

### qe_anniversary_2023_daily_B_t2:
* Name:	Rare earths are an occasional by-product of refining. They are required for upgrading modules.
* Description:	Rare earths are an occasional by-product of refining. They are required for upgrading modules.
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

### qe_anniversary_2023_daily_A_t3:
* Name:	Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
* Description:	Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
* Type:	Event
* EventId:	event_anniversary_2023_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 5
			* Tags: T3up
			* Mode: Generated

### qe_anniversary_2023_daily_B_t3:
* Name:	Rare earths are an occasional by-product of refining. They are required for upgrading modules.
* Description:	Rare earths are an occasional by-product of refining. They are required for upgrading modules.
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

### qe_anniversary_2023_daily_A_t4:
* Name:	Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
* Description:	Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
* Type:	Event
* EventId:	event_anniversary_2023_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 5
			* Tags: T4up
			* Mode: Generated

### qe_anniversary_2023_daily_B_t4:
* Name:	Rare earths are an occasional by-product of refining. They are required for upgrading modules.
* Description:	Rare earths are an occasional by-product of refining. They are required for upgrading modules.
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

### qe_halloween_2023_daily_A_t1:
* Name:	Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
* Description:	Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
* Type:	Event
* EventId:	event_halloween_2023_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: ProgenitorInvasion_T1up
			* Mode: Generated

### qe_halloween_2023_daily_B_t1:
* Name:	Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
* Description:	Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
* Type:	Event
* EventId:	event_halloween_2023_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 2
			* Tags: ProgenitorInvasion_T1up
			* Mode: Generated

### qe_halloween_2023_daily_C_t1:
* Name:	Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
* Description:	Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
* Type:	Event
* EventId:	event_halloween_2023_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 5
			* Tags: ProgenitorInvasion_T1up
			* Mode: Generated

### qe_halloween_2023_daily_D_t1:
* Name:	Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
* Description:	Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
* Type:	Event
* EventId:	event_halloween_2023_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 10
			* Tags: ProgenitorInvasion_T1up
			* Mode: Generated

### qe_halloween_2023_daily_A_t2:
* Name:	Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
* Description:	Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
* Type:	Event
* EventId:	event_halloween_2023_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: ProgenitorInvasion_T2up
			* Mode: Generated

### qe_halloween_2023_daily_B_t2:
* Name:	Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
* Description:	Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
* Type:	Event
* EventId:	event_halloween_2023_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 2
			* Tags: ProgenitorInvasion_T2up
			* Mode: Generated

### qe_halloween_2023_daily_C_t2:
* Name:	Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
* Description:	Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
* Type:	Event
* EventId:	event_halloween_2023_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 5
			* Tags: ProgenitorInvasion_T2up
			* Mode: Generated

### qe_halloween_2023_daily_D_t2:
* Name:	Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
* Description:	Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
* Type:	Event
* EventId:	event_halloween_2023_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 10
			* Tags: ProgenitorInvasion_T2up
			* Mode: Generated

### qe_halloween_2023_daily_A_t3:
* Name:	Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
* Description:	Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
* Type:	Event
* EventId:	event_halloween_2023_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: ProgenitorInvasion_T3up
			* Mode: Generated

### qe_halloween_2023_daily_B_t3:
* Name:	Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
* Description:	Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
* Type:	Event
* EventId:	event_halloween_2023_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 2
			* Tags: ProgenitorInvasion_T3up
			* Mode: Generated

### qe_halloween_2023_daily_C_t3:
* Name:	Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
* Description:	Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
* Type:	Event
* EventId:	event_halloween_2023_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 5
			* Tags: ProgenitorInvasion_T3up
			* Mode: Generated

### qe_halloween_2023_daily_D_t3:
* Name:	Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
* Description:	Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
* Type:	Event
* EventId:	event_halloween_2023_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 10
			* Tags: ProgenitorInvasion_T3up
			* Mode: Generated

### qe_halloween_2023_daily_A_t4:
* Name:	Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
* Description:	Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
* Type:	Event
* EventId:	event_halloween_2023_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: ProgenitorInvasion_T4up
			* Mode: Generated

### qe_halloween_2023_daily_B_t4:
* Name:	Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
* Description:	Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
* Type:	Event
* EventId:	event_halloween_2023_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 2
			* Tags: ProgenitorInvasion_T4up
			* Mode: Generated

### qe_halloween_2023_daily_C_t4:
* Name:	Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
* Description:	Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
* Type:	Event
* EventId:	event_halloween_2023_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 5
			* Tags: ProgenitorInvasion_T4up
			* Mode: Generated

### qe_halloween_2023_daily_D_t4:
* Name:	Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
* Description:	Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
* Type:	Event
* EventId:	event_halloween_2023_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 10
			* Tags: ProgenitorInvasion_T4up
			* Mode: Generated

### qe_tanWin_2023_daily_A_t1:
* Name:	The Chicuat collect Progenitor relics for scientific study, rather than venerate them. Their academics would gladly acquire any such objects to advance their knowledge.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
* Description:	The Chicuat collect Progenitor relics for scientific study, rather than venerate them. Their academics would gladly acquire any such objects to advance their knowledge.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
* Type:	Event
* EventId:	event_tanochWinter_2023_t1
* Goals:
	* 0:
		* GoalType: Pay
			* Id: questItem_progenitorRelic_t1
			* Amount: 1

### qe_tanWin_2023_daily_B_t1:
* Name:	Tasks performed for the Tanoch Empire also assist the Chicuat indirectly. Gaining favor with the Empire can give them more leverage in negotiations for aid.

<color=#FBB03F>Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.</color>
* Description:	Tasks performed for the Tanoch Empire also assist the Chicuat indirectly. Gaining favor with the Empire can give the Chicuat more leverage in negotiations for aid.

<color=#FBB03F>Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.</color>
* Type:	Event
* EventId:	event_tanochWinter_2023_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 5
			* Tags: T1up
			* Mode: Generated

### qe_tanWin_2023_daily_C_t1:
* Name:	The Chicuat are always in need of supplies and equipment to bolster their economy and support their people. Any aid to them would be welcomed.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
* Description:	The Chicuat are always in need of supplies and equipment to bolster their economy and support their people. Any aid to them would be welcomed.

<color=#FBB03F>Small items such as strike craft, modules and parts can be built in the fabricator. Larger items such as escort ships and flagships must be constructed at shipyards provided at larger stations.</color>
* Type:	Event
* EventId:	event_tanochWinter_2023_t1
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: T1up
			* Amount: 1

### qe_tanWin_2023_daily_D_t1:
* Name:	The conflict between the Chicuat and ethnic Tanoch people goes back centuries. Training our crew about the details of this conflict will help us navigate the inner workings of the Tanoch Empire better.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* Description:	The conflict between the Chicuat and ethnic Tanoch people goes back centuries. Training our crew about the details of this conflict will help us navigate the inner workings of the Tanoch Empire better.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* Type:	Event
* EventId:	event_tanochWinter_2023_t1
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 1

### qe_tanWin_2023_daily_A_t2:
* Name:	The Chicuat collect Progenitor relics for scientific study, rather than venerate them. Their academics would gladly acquire any such objects to advance their knowledge.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
* Description:	The Chicuat collect Progenitor relics for scientific study, rather than venerate them. Their academics would gladly acquire any such objects to advance their knowledge.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
* Type:	Event
* EventId:	event_tanochWinter_2023_t2
* Goals:
	* 0:
		* GoalType: Pay
			* Id: questItem_progenitorRelic_t2
			* Amount: 1

### qe_tanWin_2023_daily_B_t2:
* Name:	Tasks performed for the Tanoch Empire also assist the Chicuat indirectly. Gaining favor with the Empire can give them more leverage in negotiations for aid.

<color=#FBB03F>Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.</color>
* Description:	Tasks performed for the Tanoch Empire also assist the Chicuat indirectly. Gaining favor with the Empire can give them more leverage in negotiations for aid.

<color=#FBB03F>Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.</color>
* Type:	Event
* EventId:	event_tanochWinter_2023_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 5
			* Mode: Faction
			* Tags: T2up_Tanoch

### qe_tanWin_2023_daily_C_t2:
* Name:	The Chicuat are always in need of supplies and equipment to bolster their economy and support their people. Any aid to them would be welcomed.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
* Description:	The Chicuat are always in need of supplies and equipment to bolster their economy and support their people. Any aid to them would be welcomed.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
* Type:	Event
* EventId:	event_tanochWinter_2023_t2
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: Part_T2up
			* Amount: 100

### qe_tanWin_2023_daily_D_t2:
* Name:	The conflict between the Chicuat and ethnic Tanoch people goes back centuries. Training our crew about the details of this conflict will help us navigate the inner workings of the Tanoch Empire better.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* Description:	The conflict between the Chicuat and ethnic Tanoch people goes back centuries. Training our crew about the details of this conflict will help us navigate the inner workings of the Tanoch Empire better.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* Type:	Event
* EventId:	event_tanochWinter_2023_t2
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 2

### qe_tanWin_2023_daily_A_t3:
* Name:	The Chicuat collect Progenitor relics for scientific study, rather than venerate them. Their academics would gladly acquire any such objects to advance their knowledge.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
* Description:	The Chicuat collect Progenitor relics for scientific study, rather than venerate them. Their academics would gladly acquire any such objects to advance their knowledge.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
* Type:	Event
* EventId:	event_tanochWinter_2023_t3
* Goals:
	* 0:
		* GoalType: Pay
			* Id: questItem_progenitorRelic_t3
			* Amount: 1

### qe_tanWin_2023_daily_B_t3:
* Name:	Tasks performed for the Tanoch Empire also assist the Chicuat indirectly. Gaining favor with the Empire can give them more leverage in negotiations for aid.

<color=#FBB03F>Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.</color>
* Description:	Tasks performed for the Tanoch Empire also assist the Chicuat indirectly. Gaining favor with the Empire can give them more leverage in negotiations for aid.

<color=#FBB03F>Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.</color>
* Type:	Event
* EventId:	event_tanochWinter_2023_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 5
			* Mode: Faction
			* Tags: T3up_Tanoch

### qe_tanWin_2023_daily_C_t3:
* Name:	The Chicuat are always in need of supplies and equipment to bolster their economy and support their people. Any aid to them would be welcomed.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
* Description:	The Chicuat are always in need of supplies and equipment to bolster their economy and support their people. Any aid to them would be welcomed.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
* Type:	Event
* EventId:	event_tanochWinter_2023_t3
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: Part_T3up
			* Amount: 100

### qe_tanWin_2023_daily_D_t3:
* Name:	The conflict between the Chicuat and ethnic Tanoch people goes back centuries. Training our crew about the details of this conflict will help us navigate the inner workings of the Tanoch Empire better.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* Description:	The conflict between the Chicuat and ethnic Tanoch people goes back centuries. Training our crew about the details of this conflict will help us navigate the inner workings of the Tanoch Empire better.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* Type:	Event
* EventId:	event_tanochWinter_2023_t3
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 3

### qe_tanWin_2023_daily_A_t4:
* Name:	The Chicuat collect Progenitor relics for scientific study, rather than venerate them. Their academics would gladly acquire any such objects to advance their knowledge.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
* Description:	The Chicuat collect Progenitor relics for scientific study, rather than venerate them. Their academics would gladly acquire any such objects to advance their knowledge.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
* Type:	Event
* EventId:	event_tanochWinter_2023_t4
* Goals:
	* 0:
		* GoalType: Pay
			* Id: questItem_progenitorRelic_t4
			* Amount: 1

### qe_tanWin_2023_daily_B_t4:
* Name:	Tasks performed for the Tanoch Empire also assist the Chicuat indirectly. Gaining favor with the Empire can give them more leverage in negotiations for aid.

<color=#FBB03F>Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.</color>
* Description:	Tasks performed for the Tanoch Empire also assist the Chicuat indirectly. Gaining favor with the Empire can give them more leverage in negotiations for aid.

<color=#FBB03F>Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.</color>
* Type:	Event
* EventId:	event_tanochWinter_2023_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 5
			* Mode: Faction
			* Tags: T4up_Tanoch

### qe_tanWin_2023_daily_C_t4:
* Name:	The Chicuat are always in need of supplies and equipment to bolster their economy and support their people. Any aid to them would be welcomed.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
* Description:	The Chicuat are always in need of supplies and equipment to bolster their economy and support their people. Any aid to them would be welcomed.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
* Type:	Event
* EventId:	event_tanochWinter_2023_t4
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: Part_T4up
			* Amount: 100

### qe_tanWin_2023_daily_D_t4:
* Name:	The conflict between the Chicuat and ethnic Tanoch people goes back centuries. Training our crew about the details of this conflict will help us navigate the inner workings of the Tanoch Empire better.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* Description:	The conflict between the Chicuat and ethnic Tanoch people goes back centuries. Training our crew about the details of this conflict will help us navigate the inner workings of the Tanoch Empire better.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* Type:	Event
* EventId:	event_tanochWinter_2023_t4
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 5

### qe_nimbusTreasures_2024_daily_A_t1:
* Name:	New capacitors were installed in our scanner modules during the last maintenance cycle and must be calibrated. Test them above maximum power.

<color=#FBB03F>Batteries can be used to recharge a scanner or even to overcharge it above 100%. Some rare scannable objects can only be found by overcharged scanners.</color>
* Description:	New capacitors were installed in our scanner modules during the last maintenance cycle and must be calibrated. Test them above maximum power.

<color=#FBB03F>Batteries can be used to recharge a scanner or even to overcharge it above 100%. Some rare scannable objects can only be found by overcharged scanners.</color>
* Type:	Event
* EventId:	event_nimbusTreasures_2024_t1
* Goals:
	* 0:
		* GoalType: ChargeScanner
			* NewCharge: 1.5

### qe_nimbusTreasures_2024_daily_B_t1:
* Name:	New firmware has been installed in our scanner modules. They must complete a routine calibration cycle until they pass inspection.

<color=#FBB03F>Scannable objects, such as finds, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
* Description:	New firmware has been installed in our scanner modules. They must complete a routine calibration cycle until they pass inspection.

<color=#FBB03F>Scannable objects, such as finds, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
* Type:	Event
* EventId:	event_nimbusTreasures_2024_t1
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_Container_T1up
			* Amount: 3
			* Analyzed: True

### qe_nimbusTreasures_2024_daily_C1_t1:
* Name:	To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
* Description:	To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
* Type:	Event
* EventId:	event_nimbusTreasures_2024_t1
* Goals:
	* 0:
		* GoalType: Pay
			* Id: questItem_alienProbe_t1
			* Amount: 1

### qe_nimbusTreasures_2024_daily_C2_t1:
* Name:	To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
* Description:	To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
* Type:	Event
* EventId:	event_nimbusTreasures_2024_t1
* Goals:
	* 0:
		* GoalType: Pay
			* Id: questItem_alienProbe_t1
			* Amount: 2

### qe_nimbusTreasures_2024_daily_C3_t1:
* Name:	To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
* Description:	To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
* Type:	Event
* EventId:	event_nimbusTreasures_2024_t1
* Goals:
	* 0:
		* GoalType: Pay
			* Id: questItem_alienProbe_t1
			* Amount: 3

### qe_nimbusTreasures_2024_daily_C4_t1:
* Name:	To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
* Description:	To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
* Type:	Event
* EventId:	event_nimbusTreasures_2024_t1
* Goals:
	* 0:
		* GoalType: Pay
			* Id: questItem_alienProbe_t1
			* Amount: 4

### qe_nimbusTreasures_2024_daily_A_t2:
* Name:	New capacitors were installed in our scanner modules during the last maintenance cycle and must be calibrated. Test them above maximum power.

<color=#FBB03F>Batteries can be used to recharge a scanner or even to overcharge it above 100%. Some rare scannable objects can only be found by overcharged scanners.</color>
* Description:	New capacitors were installed in our scanner modules during the last maintenance cycle and must be calibrated. Test them above maximum power.

<color=#FBB03F>Batteries can be used to recharge a scanner or even to overcharge it above 100%. Some rare scannable objects can only be found by overcharged scanners.</color>
* Type:	Event
* EventId:	event_nimbusTreasures_2024_t2
* Goals:
	* 0:
		* GoalType: ChargeScanner
			* NewCharge: 1.5

### qe_nimbusTreasures_2024_daily_B_t2:
* Name:	New firmware has been installed in our scanner modules. They must complete a routine calibration cycle until they pass inspection.

<color=#FBB03F>Scannable objects, such as finds, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
* Description:	New firmware has been installed in our scanner modules. They must complete a routine calibration cycle until they pass inspection.

<color=#FBB03F>Scannable objects, such as finds, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
* Type:	Event
* EventId:	event_nimbusTreasures_2024_t2
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_Container_T2up
			* Amount: 3
			* Analyzed: True

### qe_nimbusTreasures_2024_daily_C1_t2:
* Name:	To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
* Description:	To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
* Type:	Event
* EventId:	event_nimbusTreasures_2024_t2
* Goals:
	* 0:
		* GoalType: Pay
			* Id: questItem_alienProbe_t2
			* Amount: 1

### qe_nimbusTreasures_2024_daily_C2_t2:
* Name:	To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
* Description:	To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
* Type:	Event
* EventId:	event_nimbusTreasures_2024_t2
* Goals:
	* 0:
		* GoalType: Pay
			* Id: questItem_alienProbe_t2
			* Amount: 2

### qe_nimbusTreasures_2024_daily_C3_t2:
* Name:	To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
* Description:	To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
* Type:	Event
* EventId:	event_nimbusTreasures_2024_t2
* Goals:
	* 0:
		* GoalType: Pay
			* Id: questItem_alienProbe_t2
			* Amount: 3

### qe_nimbusTreasures_2024_daily_C4_t2:
* Name:	To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
* Description:	To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
* Type:	Event
* EventId:	event_nimbusTreasures_2024_t2
* Goals:
	* 0:
		* GoalType: Pay
			* Id: questItem_alienProbe_t2
			* Amount: 4

### qe_nimbusTreasures_2024_daily_A_t3:
* Name:	New capacitors were installed in our scanner modules during the last maintenance cycle and must be calibrated. Test them above maximum power.

<color=#FBB03F>Batteries can be used to recharge a scanner or even to overcharge it above 100%. Some rare scannable objects can only be found by overcharged scanners.</color>
* Description:	New capacitors were installed in our scanner modules during the last maintenance cycle and must be calibrated. Test them above maximum power.

<color=#FBB03F>Batteries can be used to recharge a scanner or even to overcharge it above 100%. Some rare scannable objects can only be found by overcharged scanners.</color>
* Type:	Event
* EventId:	event_nimbusTreasures_2024_t3
* Goals:
	* 0:
		* GoalType: ChargeScanner
			* NewCharge: 1.5

### qe_nimbusTreasures_2024_daily_B_t3:
* Name:	New firmware has been installed in our scanner modules. They must complete a routine calibration cycle until they pass inspection.

<color=#FBB03F>Scannable objects, such as finds, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
* Description:	New firmware has been installed in our scanner modules. They must complete a routine calibration cycle until they pass inspection.

<color=#FBB03F>Scannable objects, such as finds, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
* Type:	Event
* EventId:	event_nimbusTreasures_2024_t3
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_Container_T3up
			* Amount: 3
			* Analyzed: True

### qe_nimbusTreasures_2024_daily_C1_t3:
* Name:	To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
* Description:	To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
* Type:	Event
* EventId:	event_nimbusTreasures_2024_t3
* Goals:
	* 0:
		* GoalType: Pay
			* Id: questItem_alienProbe_t3
			* Amount: 1

### qe_nimbusTreasures_2024_daily_C2_t3:
* Name:	To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
* Description:	To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
* Type:	Event
* EventId:	event_nimbusTreasures_2024_t3
* Goals:
	* 0:
		* GoalType: Pay
			* Id: questItem_alienProbe_t3
			* Amount: 2

### qe_nimbusTreasures_2024_daily_C3_t3:
* Name:	To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
* Description:	To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
* Type:	Event
* EventId:	event_nimbusTreasures_2024_t3
* Goals:
	* 0:
		* GoalType: Pay
			* Id: questItem_alienProbe_t3
			* Amount: 3

### qe_nimbusTreasures_2024_daily_C4_t3:
* Name:	To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
* Description:	To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
* Type:	Event
* EventId:	event_nimbusTreasures_2024_t3
* Goals:
	* 0:
		* GoalType: Pay
			* Id: questItem_alienProbe_t3
			* Amount: 4

### qe_nimbusTreasures_2024_daily_A_t4:
* Name:	New capacitors were installed in our scanner modules during the last maintenance cycle and must be calibrated. Test them above maximum power.

<color=#FBB03F>Batteries can be used to recharge a scanner or even to overcharge it above 100%. Some rare scannable objects can only be found by overcharged scanners.</color>
* Description:	New capacitors were installed in our scanner modules during the last maintenance cycle and must be calibrated. Test them above maximum power.

<color=#FBB03F>Batteries can be used to recharge a scanner or even to overcharge it above 100%. Some rare scannable objects can only be found by overcharged scanners.</color>
* Type:	Event
* EventId:	event_nimbusTreasures_2024_t4
* Goals:
	* 0:
		* GoalType: ChargeScanner
			* NewCharge: 1.5

### qe_nimbusTreasures_2024_daily_B_t4:
* Name:	New firmware has been installed in our scanner modules. They must complete a routine calibration cycle until they pass inspection.

<color=#FBB03F>Scannable objects, such as finds, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
* Description:	New firmware has been installed in our scanner modules. They must complete a routine calibration cycle until they pass inspection.

<color=#FBB03F>Scannable objects, such as finds, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
* Type:	Event
* EventId:	event_nimbusTreasures_2024_t4
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_Container_T4up
			* Amount: 3
			* Analyzed: True

### qe_nimbusTreasures_2024_daily_C1_t4:
* Name:	To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
* Description:	To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
* Type:	Event
* EventId:	event_nimbusTreasures_2024_t4
* Goals:
	* 0:
		* GoalType: Pay
			* Id: questItem_alienProbe_t4
			* Amount: 1

### qe_nimbusTreasures_2024_daily_C2_t4:
* Name:	To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
* Description:	To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
* Type:	Event
* EventId:	event_nimbusTreasures_2024_t4
* Goals:
	* 0:
		* GoalType: Pay
			* Id: questItem_alienProbe_t4
			* Amount: 2

### qe_nimbusTreasures_2024_daily_C3_t4:
* Name:	To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
* Description:	To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
* Type:	Event
* EventId:	event_nimbusTreasures_2024_t4
* Goals:
	* 0:
		* GoalType: Pay
			* Id: questItem_alienProbe_t4
			* Amount: 3

### qe_nimbusTreasures_2024_daily_C4_t4:
* Name:	To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
* Description:	To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
* Type:	Event
* EventId:	event_nimbusTreasures_2024_t4
* Goals:
	* 0:
		* GoalType: Pay
			* Id: questItem_alienProbe_t4
			* Amount: 4

### qe_yaoSpr_2024_daily_A_t1:
* Name:	The Cangacian pirate bands running in this area are seeking the Yaot conjunction pilgrimage fleet. Attack them to dissuade their scouting efforts.

<color=#FBB03F>The Cangacians are pirates that harass trade routes and colonies. We may find them in signals in most areas of the galaxy. They have been sighted raiding mining fleets in asteroid clusters as well.</color>
* Description:	The Cangacian pirate bands running in this area are seeking the Yaot conjunction pilgrimage fleet. Attack them to dissuade their scouting efforts.

<color=#FBB03F>The Cangacians are pirates that harass trade routes and colonies. We may find them in signals in most areas of the galaxy. They have been sighted raiding mining fleets in asteroid clusters as well.</color>
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

### qe_yaoSpr_2024_daily_A_t2:
* Name:	The Cangacian pirate bands running in this area are seeking the Yaot conjunction pilgrimage fleet. Attack them to dissuade their scouting efforts.

<color=#FBB03F>The Cangacians are pirates that harass trade routes and colonies. We may find them in signals in most areas of the galaxy. They have been sighted raiding mining fleets in asteroid clusters as well.</color>
* Description:	The Cangacian pirate bands running in this area are seeking the Yaot conjunction pilgrimage fleet. Attack them to dissuade their scouting efforts.

<color=#FBB03F>The Cangacians are pirates that harass trade routes and colonies. We may find them in signals in most areas of the galaxy. They have been sighted raiding mining fleets in asteroid clusters as well.</color>
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

### qe_yaoSpr_2024_daily_A_t3:
* Name:	The Cangacian pirate bands running in this area are seeking the Yaot conjunction pilgrimage fleet. Attack them to dissuade their scouting efforts.

<color=#FBB03F>The Cangacians are pirates that harass trade routes and colonies. We may find them in signals in most areas of the galaxy. They have been sighted raiding mining fleets in asteroid clusters as well.</color>
* Description:	The Cangacian pirate bands running in this area are seeking the Yaot conjunction pilgrimage fleet. Attack them to dissuade their scouting efforts.

<color=#FBB03F>The Cangacians are pirates that harass trade routes and colonies. We may find them in signals in most areas of the galaxy. They have been sighted raiding mining fleets in asteroid clusters as well.</color>
* Type:	Event
* EventId:	event_yaotSpring_2024_t3
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedP1T3
				* ShipsDestroyedP1T4
			* Amount: 10

### qe_yaoSpr_2024_daily_A_t4:
* Name:	The Cangacian pirate bands running in this area are seeking the Yaot conjunction pilgrimage fleet. Attack them to dissuade their scouting efforts.

<color=#FBB03F>The Cangacians are pirates that harass trade routes and colonies. We may find them in signals in most areas of the galaxy. They have been sighted raiding mining fleets in asteroid clusters as well.</color>
* Description:	The Cangacian pirate bands running in this area are seeking the Yaot conjunction pilgrimage fleet. Attack them to dissuade their scouting efforts.

<color=#FBB03F>The Cangacians are pirates that harass trade routes and colonies. We may find them in signals in most areas of the galaxy. They have been sighted raiding mining fleets in asteroid clusters as well.</color>
* Type:	Event
* EventId:	event_yaotSpring_2024_t4
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedP1T3
				* ShipsDestroyedP1T4
			* Amount: 10

### qe_yaoSpr_2024_daily_B_t1:
* Name:	We must learn more about the situation if we're to understand why the Yaot pilgrim fleet is being targeted. Search for any remains that are left in their path of passage.

<color=#FBB03F>Finds must be discovered through scanning. After being analyzed, they can be picked up to collect the reward inside.</color>
* Description:	We must learn more about the situation if we're to understand why the Yaot pilgrim fleet is being targeted. Search for any remains that are left in their path of passage.

<color=#FBB03F>Finds must be discovered through scanning. After being analyzed, they can be picked up to collect the reward inside.</color>
* Type:	Event
* EventId:	event_yaotSpring_2024_t1
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_Container_T1up
			* Amount: 1
			* Analyzed: True

### qe_yaoSpr_2024_daily_B_t2:
* Name:	We must learn more about the situation if we're to understand why the Yaot pilgrim fleet is being targeted. Search for any remains that are left in their path of passage.

<color=#FBB03F>Finds must be discovered through scanning. After being analyzed, they can be picked up to collect the reward inside.</color>
* Description:	We must learn more about the situation if we're to understand why the Yaot pilgrim fleet is being targeted. Search for any remains that are left in their path of passage.

<color=#FBB03F>Finds must be discovered through scanning. After being analyzed, they can be picked up to collect the reward inside.</color>
* Type:	Event
* EventId:	event_yaotSpring_2024_t2
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_Container_T2up
			* Amount: 1
			* Analyzed: True

### qe_yaoSpr_2024_daily_B_t3:
* Name:	We must learn more about the situation if we're to understand why the Yaot pilgrim fleet is being targeted. Search for any remains that are left in their path of passage.

<color=#FBB03F>Finds must be discovered through scanning. After being analyzed, they can be picked up to collect the reward inside.</color>
* Description:	We must learn more about the situation if we're to understand why the Yaot pilgrim fleet is being targeted. Search for any remains that are left in their path of passage.

<color=#FBB03F>Finds must be discovered through scanning. After being analyzed, they can be picked up to collect the reward inside.</color>
* Type:	Event
* EventId:	event_yaotSpring_2024_t3
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_Container_T3up
			* Amount: 1
			* Analyzed: True

### qe_yaoSpr_2024_daily_B_t4:
* Name:	We must learn more about the situation if we're to understand why the Yaot pilgrim fleet is being targeted. Search for any remains that are left in their path of passage.

<color=#FBB03F>Finds must be discovered through scanning. After being analyzed, they can be picked up to collect the reward inside.</color>
* Description:	We must learn more about the situation if we're to understand why the Yaot pilgrim fleet is being targeted. Search for any remains that are left in their path of passage.

<color=#FBB03F>Finds must be discovered through scanning. After being analyzed, they can be picked up to collect the reward inside.</color>
* Type:	Event
* EventId:	event_yaotSpring_2024_t4
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_Container_T4up
			* Amount: 1
			* Analyzed: True

### qe_yaoSpr_2024_daily_C_t1:
* Name:	The Yaot pilgrimage is far from home and likely out of the supply network from the Yaot fleet. Any aid we can provide them would go a long way in helping them complete their journey.

<color=#FBB03F>Tokens of the eldest can be found in lost caches within Yaot territory or in Cangacian salvage.</color>
* Description:	The Yaot pilgrimage is far from home and likely out of the supply network from the Yaot fleet. Any aid we can provide them would go a long way in helping them complete their journey.

<color=#FBB03F>Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.</color>
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

### qe_yaoSpr_2024_daily_C_t2:
* Name:	The Yaot pilgrimage is far from home and likely out of the supply network from the Yaot fleet. Any aid we can provide them would go a long way in helping them complete their journey.

<color=#FBB03F>Tokens of the eldest can be found in lost caches within Yaot territory or in Cangacian salvage.</color>
* Description:	The Yaot pilgrimage is far from home and likely out of the supply network from the Yaot fleet. Any aid we can provide them would go a long way in helping them complete their journey.

<color=#FBB03F>Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.</color>
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

### qe_yaoSpr_2024_daily_C_t3:
* Name:	The Yaot pilgrimage is far from home and likely out of the supply network from the Yaot fleet. Any aid we can provide them would go a long way in helping them complete their journey.

<color=#FBB03F>Tokens of the eldest can be found in lost caches within Yaot territory or in Cangacian salvage.</color>
* Description:	The Yaot pilgrimage is far from home and likely out of the supply network from the Yaot fleet. Any aid we can provide them would go a long way in helping them complete their journey.

<color=#FBB03F>Tokens of the eldest can be found in lost caches within Yaot territory or in Cangacian salvage.</color>
* Type:	Event
* EventId:	event_yaotSpring_2024_t3
* Goals:
	* 0:
		* GoalType: Pay
			* Id: yao_collectable_u_01
			* Amount: 1

### qe_yaoSpr_2024_daily_C_t4:
* Name:	The Yaot pilgrimage is far from home and likely out of the supply network from the Yaot fleet. Any aid we can provide them would go a long way in helping them complete their journey.

<color=#FBB03F>Tokens of the eldest can be found in lost caches within Yaot territory or in Cangacian salvage.</color>
* Description:	The Yaot pilgrimage is far from home and likely out of the supply network from the Yaot fleet. Any aid we can provide them would go a long way in helping them complete their journey.

<color=#FBB03F>Tokens of the eldest can be found in lost caches within Yaot territory or in Cangacian salvage.</color>
* Type:	Event
* EventId:	event_yaotSpring_2024_t4
* Goals:
	* 0:
		* GoalType: Pay
			* Id: yao_collectable_u_01
			* Amount: 3

### qe_yaoSpr_2024_daily_D_t1:
* Name:	The Yaot likely do not know this region of space well based on how rarely they're encountered here. Examine the nearby star systems to assist the Yaot pilgrims in navigating the region.

<color=#FBB03F>Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.</color>
* Description:	The Yaot likely do not know this region of space well based on how rarely they're encountered here. Examine the nearby star systems to assist the Yaot pilgrims in navigating the region.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
* Type:	Event
* EventId:	event_yaotSpring_2024_t1
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_Generated_T1up
			* Amount: 5
			* Analyzed: True

### qe_yaoSpr_2024_daily_D_t2:
* Name:	The Yaot likely do not know this region of space well based on how rarely they're encountered here. Examine the nearby star systems to assist the Yaot pilgrims in navigating the region.

<color=#FBB03F>Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.</color>
* Description:	The Yaot likely do not know this region of space well based on how rarely they're encountered here. Examine the nearby star systems to assist the Yaot pilgrims in navigating the region.

<color=#FBB03F>Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.</color>
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

### qe_yaoSpr_2024_daily_D_t3:
* Name:	The Yaot likely do not know this region of space well based on how rarely they're encountered here. Examine the nearby star systems to assist the Yaot pilgrims in navigating the region.

<color=#FBB03F>Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.</color>
* Description:	The Yaot likely do not know this region of space well based on how rarely they're encountered here. Examine the nearby star systems to assist the Yaot pilgrims in navigating the region.

<color=#FBB03F>Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.</color>
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

### qe_yaoSpr_2024_daily_D_t4:
* Name:	The Yaot likely do not know this region of space well based on how rarely they're encountered here. Examine the nearby star systems to assist the Yaot pilgrims in navigating the region.

<color=#FBB03F>Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.</color>
* Description:	The Yaot likely do not know this region of space well based on how rarely they're encountered here. Examine the nearby star systems to assist the Yaot pilgrims in navigating the region.

<color=#FBB03F>Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.</color>
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
### qm_t0_Jolja:
* Name:	Delver
* Description:	After examining the Progenitor Relic, Gideon wants us to find a Progenitor Terminal in Iniim. If we access this, we may have some answers about what happened at Wiracoda Gate.
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
### qm_t0_pickKiith:
* Name:	Blood Ties
* Description:	The local Hiigaran survivors wish to know what Kiith we affiliate with. There are advantages for declaring for a specific Kiith.
* Type:	Main
* Goals:
	* 0:
		* Type: SelectKiith

### qm_t0_pickName:
* Name:	Declaration
* Description:	The Hiigaran survivors want to know your name, commander.
* Type:	Main
* FollowUps:
	* ql_main_t1_newOres
	* ql_main_t0_joinClan
* Goals:
	* 0:
		* Type: ChangeName

## QL_MAIN_T0_JOINCLAN
### qm_t0_joinClan:
* Name:	A Clan of Choice
* Description:	We can increase our firepower and capabilities by joining with other battle groups.
* Type:	Main
* Goals:
	* 0:
		* Type: JoinClan

## QL_MAIN_T1_NEWORES
### qm_t1_newOres:
* Name:	New Minerals
* Description:	The inner systems may have different resources. We should check out the asteroids for mining spots.
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

### qm_t1_introRefining:
* Name:	Refinery
* Description:	The new ores require refining to be usable for construction purposes. Luckily we have refining facilities on board.
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
### qm_t1_facHiigaran:
* Name:	Hiigaran Outposts
* Description:	Lazarus station asked us to help some Hiigaran outposts on the frontier.
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
### qm_t1_strikeCraft:
* Name:	New Strike Craft
* Description:	We have found a way to incorporate the new materials into our ship design.
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
### qm_t1_RColEquip:
* Name:	New Resource Collector
* Description:	The new ores are more difficult to mine. We should build resource collectors that are equipped to deal with these denser metals.
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

### qm_t1_RColMine:
* Name:	Mining Spree
* Description:	We should put our new resource collectors to the test and stockpile some ores.
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
### qm_t1_advCombat_01:
* Name:	Combat Trials
* Description:	Our Hiigaran allies have prepared a combat area to test our improved strike craft.
* Type:	Main
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: story_B01_CombatTrials

### qm_t1_killEnemyShips:
* Name:	Hostiles
* Description:	These inner systems are crawling with enemies. We should thin their numbers. Enemies are found in asteroid clusters and signals.
* Type:	Main
* FollowUps: ql_main_t1_promoteOfficer
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyed
			* Amount: 25

## QL_MAIN_T1_PROMOTEOFFICER
### qm_t1_introPromoteOfficer:
* Name:	Crew Experience
* Description:	Training our officers will increase their performance significantly. To train an officer we need to find insignias. Insignias can be gained from discharging officers and may be rewarded from completing signals.
* Type:	Main
* FollowUps: ql_main_t1_escorts
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 1

### qm_t1_rankUpOfficer:
* Name:	Crew Promotion
* Description:	We should promote our most experienced officers to further improve their performance. Promoting an officer increase their special ability or may even grant them a second.
* Type:	Side
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 1
			* MinLevel: 10

## QL_MAIN_T1_ESCORTS
### qm_t1_escort:
* Name:	New Escorts
* Description:	We should bolster our fleet with frigates made from the new metals.
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
### qm_t1_advCombat_02:
* Name:	Meropis Defense
* Description:	We received a message that Meropis, a Iyatequa communications station, is asking for support in an expected Cangacian attack.
* Type:	Main
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: story_B02_MeropisDefense

### qm_t1_doSignals:
* Name:	Signal Tracking
* Description:	The Cangacians have been repelled, but we should disrupt their activities by hunting down hostile signals in the area.
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
### qm_t1_facCangacian:
* Name:	Cangacian Troubles
* Description:	Cangacians are attacking colonies. We should help them in whatever way we can.
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
### qm_t1_introCraftFlagship:
* Name:	Flagship Construction
* Description:	We have an Explorer-class flagship blueprint utilizing the new minerals found in this region.
* Type:	Main
* FollowUps: ql_main_t1_killCangacians
* Goals:
	* 0:
		* GoalType: StartCraft
			* Category: Crafting
			* Tags: Flagship_Ship
			* Amount: 1

### qm_t1_introEquipFlagship:
* Name:	New Flagship
* Description:	Once the flagship construction has finished, we should move over to the new flagship, including our ships and officers. This is done via the fleet configuration.
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
### qm_t1_killCangacians:
* Name:	Pest Control
* Description:	While we wait for the flagship construction to finish, we might as well make this galaxy a safer place.
* Type:	Side
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedP1
			* Amount: 20

## QL_MAIN_T1_ADVCOMBAT_03
### qm_t1_advCombat_03:
* Name:	The Pool
* Description:	The Iyatequa have flagged a location for suspicious hostile activity. They've asked us to investigate on their behalf.
* Type:	Main
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: story_B03_ThePool

### qm_t1_killProgenitors:
* Name:	Hostile History
* Description:	The Progenitor remnants present a danger to the people living in this galaxy. We should thin their numbers.
* Type:	Main
* FollowUps: ql_main_t1_turrets
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedProgenitor
			* Amount: 10

## QL_MAIN_T1_TURRETS
### qm_t1_craftTurret:
* Name:	Weapon Turrets
* Description:	The new flagship follows modular design principles, allowing us to outfit it with turrets as we choose. First we should build a weapon turret.
* Type:	Main
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: Weapon_Module_T1
			* Amount: 1

### qm_t1_mountTurret:
* Name:	Mounting Turrets
* Description:	Now that we have a turret module, we should mount it on our flagship. Turrets can be managed in the external module view of our flagship.
* Type:	Main
* FollowUps: ql_main_t1_upgrades
* Goals:
	* 0:
		* GoalType: Equip
			* Type: Weapon

## QL_MAIN_T1_UPGRADES
### qm_t1_rareEarths:
* Name:	Rare Elements
* Description:	When refining ores in the refinery there is a chance for rare earths to appear in addition to the refined metals.
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

### qm_t1_upgradeTurret:
* Name:	Turret Upgrades
* Description:	The rare minerals we have extracted can be used to improve our modules.
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

### qm_t1_upgradeTurret_3:
* Name:	Turret Upgrades Level 3
* Description:	A module can be upgraded multiple times, vastly increasing its power.
* Type:	Side
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Upgrade
			* Tags: Weapon_Module
			* Amount: 1
			* MinLevel: 3

### qm_t1_upgradeTurret_4:
* Name:	Turret Upgrades Level 4
* Description:	A module can be upgraded multiple times, vastly increasing its power.
* Type:	Side
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Upgrade
			* Tags: Weapon_Module
			* Amount: 1
			* MinLevel: 4

### qm_t1_upgradeTurret_5:
* Name:	Turret Upgrades Level 5
* Description:	A module can be upgraded multiple times, vastly increasing its power.
* Type:	Side
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Upgrade
			* Tags: Weapon_Module
			* Amount: 1
			* MinLevel: 5

### qm_t1_upgradeTurret_6:
* Name:	Turret Upgrades Level 6
* Description:	A module can be upgraded multiple times, vastly increasing its power.
* Type:	Side
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Upgrade
			* Tags: Weapon_Module
			* Amount: 1
			* MinLevel: 6

### qm_t1_upgradeTurret_7:
* Name:	Turret Upgrades Level 7
* Description:	A module can be upgraded multiple times, vastly increasing its power.
* Type:	Side
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Upgrade
			* Tags: Weapon_Module
			* Amount: 1
			* MinLevel: 7

### qm_t1_upgradeTurret_8:
* Name:	Turret Upgrades Level 8
* Description:	A module can be upgraded multiple times, vastly increasing its power.
* Type:	Side
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Upgrade
			* Tags: Weapon_Module
			* Amount: 1
			* MinLevel: 8

### qm_t1_upgradeTurretMax:
* Name:	Final Turret Upgrades
* Description:	Once a module has been upgraded to level 9, it is at its maximum level and cannot be upgraded further.
* Type:	Side
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Upgrade
			* Tags: Weapon_Module
			* Amount: 1
			* MinLevel: 9

## QL_MAIN_T1_SIDEPROG
### qm_t1_facProgenitors:
* Name:	Progenitor Components
* Description:	To improve our scanner, we should gather data on Progenitor vessels. Once we have enough data, we can create a new scanner blueprint.
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
### qm_t1_scannerModule:
* Name:	New Scanner
* Description:	Based on the data from the Progenitor fragments, our engineers have created a new scanner blueprint.
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
### qm_t1_scannerOvercharge:
* Name:	Rare Find
* Description:	Some objects are too hidden to find them with our scanner under regular circumstances. Luckily, we can use special batteries to overcharge the scanner beyond its normal abilities to be able to find those.
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
### qm_t2_findPirateHideout:
* Name:	Hidden in the Dark
* Description:	We need to find the system from where the recent Cangacian activity originates. Reports indicate the system might be near Saraal. We should go there and use our long range scanners.
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

### qm_t2_strikePirateHideout:
* Name:	Cangacian Hideout
* Description:	We have located the pirate hideout. Now is the time to strike.
* Type:	Main
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Ids:
				* qm_t1_facProgenitors_A
				* qm_t1_facProgenitors_B
				* qm_t1_facProgenitors_C
				* qm_t1_facProgenitors_D
			* Amount: 1

## QL_MAIN_T1_UPGRADEEXTERNALS
### qm_t1_upgradeModules:
* Name:	Exploration Upgrades
* Description:	In order to move deeper into the galaxy we should upgrade our scanner and drives core.
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
### qm_t1_introLiaison:
* Name:	Reaching Out
* Description:	The Iyatequa are interested in doing business with us. Completing liaison assignments for them will allow us to increase our reputation, which allows us to buy special items and blueprints in their liaison requisitions office.
* Type:	Side
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 3
			* Tags: Faction

## QL_MAIN_T1_INTROINTERNALS
### qm_t1_introInternals:
* Name:	Internal Modules
* Description:	Our flagship has a configurable interior, which we can use to boost our exploration, production or combat abilities using internal modules.
* Type:	Main
* Goals:
	* 0:
		* GoalType: Craft
			* Tags: Crafting_Factory
	* 1:
		* GoalType: Equip
			* Type: Internal
			* Tags: Crafting_Factory

### qm_t1_upgradeInternals:
* Name:	Internal Module Upgrades
* Description:	Just like with weapon turrets, we can improve our internal module's performance through upgrades.
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
### qm_t1_facIyatequa:
* Name:	Iyatequa Business
* Description:	The Iyatequa have heard of our plan to meet the Tanoch and agreed to help us set up our science facilities to research better drives. For a price, of course.
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
### qm_t2_introRP:
* Name:	Laboratories
* Description:	Our scientists have brought our on-ship laboratories online. We can collect the data of their findings there.
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

### qm_t2_introResearch:
* Name:	Research Center
* Description:	Lazarus Base has given us access to a workshop module attached to the station. We can perform further research there and develop new technologies.
* Type:	Main
* FollowUps: ql_main_t2_newResources
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Research
			* Id: rp_catExpl_hyperCap_t2_c
			* Tags: T2

## QL_MAIN_T2_NEWRESOURCES
### qm_t2_newResources:
* Name:	New Resources T2
* Description:	It seems the deeper we move into the galaxy the more minerals we find.
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
### qm_t2_facCangacian:
* Name:	Cangacian Incursion
* Description:	Several Hiigaran colonies are under attack by Cangacians. Lazarus command has asked us to help as much as we can.
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
### qm_t2_startResearchT2Intc:
* Name:	Interceptor T2
* Description:	We can research better ship blueprints using the new materials found in this region.
* Type:	Main
* FollowUps: ql_main_t2_strikeCraftCraft
* Goals:
	* 0:
		* GoalType: StartCraft
			* Category: Research
			* Id: rp_catStrCraft_bp_sf_intc_t2_c

### qm_t2_finResearchT2Intc:
* Name:	Interceptor Schematics
* Description:	Schematics research unlock new blueprints for the fabricators and shipyard.
* Type:	Main
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Research
			* Id: rp_catStrCraft_bp_sf_intc_t2_c

## QL_MAIN_T2_STRIKECRAFTCRAFT
### qm_t2_introParts:
* Name:	Ship Parts Assembly
* Description:	The new constructions will require the use of specially fabricated parts.

The blueprints for small Hull, Weapon and Machinery parts can be found in the market.
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

### qm_t2_strikeCraft:
* Name:	Strike Craft T2
* Description:	Now that we have finished the research and crafted the necessary parts, we can craft an interceptor squadron.
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
### qm_t2_facHiigaran:
* Name:	Lazarus Repairs
* Description:	Lazarus Station was recently attacked. Command asked us to help with rebuilding efforts.
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
### qm_t2_craftRCol:
* Name:	Resource Collector T2
* Description:	Mining the new ores can be done faster with special resource collectors equipped with better mining gear.
* Type:	Side
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: RCol_T2
			* Amount: 1

### qm_t2_RColMining:
* Name:	Ore Deal
* Description:	With our new resource collectors, we can mine ores much faster than before.
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
### qm_t2_craftRCon:
* Name:	Resource Controller
* Description:	We acquired a blueprint for the Resource Controller, an escort ship we can send on independent mining missions. Like other escort ships, it must be built in the shipyard.
* Type:	Side
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: RCon
			* Amount: 1

### qm_t2_introIdleMine:
* Name:	Remote Mining
* Description:	Resource Controllers can be sent away to mine ores without our supervision. To do that, it must be assigned to an escort slot in fleet configuration.
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
### qm_t2_startResearchT2Frig:
* Name:	Assault Frigate T2
* Description:	We can research a better assault frigate blueprint using the new minerals.
* Type:	Main
* FollowUps: ql_main_t2_oreD
* Goals:
	* 0:
		* GoalType: StartCraft
			* Category: Research
			* Id: rp_catEscorts_bp_cf_assa_t2_c

### qm_t2_finResearchT2Frig:
* Name:	Assault Frigate Schematics
* Description:	Our scientists are at work developing new schematics for the assault frigate.
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
### qm_t2_introOreD:
* Name:	Gold Rush
* Description:	Some asteroids in this region contain a rare ore we can use for advanced constructions.
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

### qm_t2_craftUncShip:
* Name:	Elite Ships
* Description:	We acquired a blueprint for an advanced ship design. It requires the rare ore to be built.
* Type:	Side
* Goals:
	* 0:
		* GoalType: Craft
			* Id: hgn_sf_intc_01_u_t2

## QL_MAIN_T2_RESEARCHPULSARCORVETTE
### qm_t2_researchPulsarCorvette:
* Name:	Pulsar Corvette Schematics
* Description:	Uncommon, rare and epic researches are not part of the central research path and must be found in order to be researched.

The Pulsar Corvette Schematics can be found in the code fragment market.
* Type:	Side
* FollowUps: ql_main_t2_pulsarCorvette
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Research
			* Id: rp_catStrCraft_bp_sc_puls_t2_c
			* MinLevel: 1

## QL_MAIN_T2_PULSARCORVETTE
### qm_t2_pulsarCorvette:
* Name:	Pulsar Corvette
* Description:	Pulsar Corvettes are effective against other corvettes and small escort ships.
* Type:	Side
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: PulsarCorvette_T2
			* Amount: 1

## QL_MAIN_T2_CRAFTESCORT
### qm_t2_largeHullParts:
* Name:	Large Hull Parts Assembly
* Description:	The frigate blueprint requires a large version of the hull parts.

The blueprint for large hull parts can be found in the market.
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

### qm_t2_escort:
* Name:	Escort Ships T2
* Description:	With the large hull parts we can finally construct the frigate.
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
### qm_t2_introLiaison:
* Name:	Liaison Office
* Description:	Doing assignments for the liaison office will allow us to requisition better blueprints and better equipment.
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
### qm_t2_facIyatequa:
* Name:	Iyatequa Intermediary
* Description:	The Iyatequa have offered to liaison between us and the Tanoch if we agree to run some errands for them.
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
### qm_t2_strikeStationDefense:
* Name:	Station Defense
* Description:	A large Tanoch station is under attack by a large fleet of pirates. We should band together with other fleets to repel the attackers.
* Type:	Side
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Ids:
				* qm_t2_facIyatequa_A
				* qm_t2_facIyatequa_B
				* qm_t2_facIyatequa_C
				* qm_t2_facIyatequa_D
			* Amount: 1

## QL_MAIN_T2_LARGEWPNPARTS
### qm_t2_liaisonTanoch:
* Name:	Tanoch Relations
* Description:	The Tanoch liaison office will offer better items the higher our reputation is.
* Type:	Main
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 10
			* Tags: Faction_Tanoch_T2up

### qm_t2_largeWeaponParts:
* Name:	Large Weapon Parts Assembly
* Description:	Large weapon parts are required for building flagships and weapon modules.

The blueprint for large weapon parts can be found in the Tanoch liaison requisitions office.
* Type:	Main
* FollowUps: ql_main_t2_flagship
* Goals:
	* 0:
		* GoalType: Craft
			* Tags: Part_Weapon_L_T2
			* Amount: 100
			* Category: Crafting

## QL_MAIN_T2_LARGEMCHPARTS
### qm_t2_liaisonIyatequa:
* Name:	Iyatequa Relations
* Description:	The Iyatequa liaison office will offer better items the higher our reputation is.
* Type:	Main
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 10
			* Tags: Faction_Tr1_T2up

### qm_t2_largeMachineParts:
* Name:	Large Machinery Parts Assembly
* Description:	Large machinery parts are required for building flagships and non-weapon modules.

The blueprint for large machinery parts can be found in the Iyatequa liaison requisitions office.
* Type:	Main
* FollowUps: ql_main_t2_flagship
* Goals:
	* 0:
		* GoalType: Craft
			* Tags: Part_Module_L_T2
			* Amount: 100
			* Category: Crafting

## QL_MAIN_T2_FLAGSHIP
### qm_t2_startCraftFlagship:
* Name:	Flagship Construction T2
* Description:	Now that we have the necessary resources, we can start building our new flagship. Its larger drive core will allow us to enter Tanoch territory. Flagship blueprints are available in the market.
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

### qm_t2_finCraftFlagship:
* Name:	Flagship T2
* Description:	The construction of our new flagship is under way. Once it's finished, we can switch over and move our squadrons and officers as well as modules to the new flagship.
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
### qm_t2_strikePahrasRock:
* Name:	Pahra's Rock
* Description:	Pirate's major Asteroid Base in the area has been threatening the Hiigaran settlements. Hiigaran Flagships have been gathered to strike on this Base.​
* Type:	Side
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Ids:
				* qm_t2_largeWeaponParts
				* qm_t2_largeMachineParts
			* Amount: 1

## QL_MAIN_T2_TURRETS
### qm_t2_turrets:
* Name:	Weapon Turrets T2
* Description:	We should stay up to date on weapon technology. Researching new weapon schematics will unlock better modules.
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
### qm_t2_tanochet:
* Name:	Tanochet
* Description:	We can finally reach the Tanoch capital. It is time to meet the emperor.
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
### qm_t2_internalFabricator:
* Name:	Fabricator Module
* Description:	Our new flagship offers the ability to reconfigure its internal layout.
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
### qm_t2_epicSignals:
* Name:	High Risk High Reward
* Description:	Occasionally we come across high energy signals. It might be worth checking out, but it could also be a potential danger. We should proceed with caution.
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
### qm_t2_facTanoch:
* Name:	Tanoch Errands
* Description:	The Tanoch have asked us to run some errands for them. This could be a chance for us to gain their trust.
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
### qm_t2_upgradeInternals:
* Name:	Internal Module Upgrades
* Description:	Just like with weapon turrets, we can improve our internal module's performance through upgrades.
* Type:	Main
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Upgrade
			* Tags: Factory
			* Amount: 2
			* MinLevel: 5

### qm_t2_otherInternals:
* Name:	Compartments
* Description:	Our flagship is sectioned into three compartments. We can install different modules in different compartments.
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
### qm_t2_compartments:
* Name:	Compartments
* Description:	Our flagship is sectioned into three compartments. We can install different modules in different compartments.
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
### qm_t2_facYaot:
* Name:	Yaot Conflict
* Description:	We have received assignments from both Tanochetlan and Lazarus station. They asked us to investigate the Yaot threat.
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
### qm_t2_templeTonaati:
* Name:	Temple Tonaati
* Description:	We are following Vaygr fleet to find out their hidden plan.
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
### qm_t3_researchJumpCap:
* Name:	Expanding the Horizon
* Description:	Our scientists have come up with new theories on how to increase the power of our engines. With the new technology we should be able to enter space that was previously inaccessible to us.
* Type:	Main
* FollowUps: ql_main_t3_intro
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Research
			* Id: rp_catExpl_hyperCap_t3_c
			* MinLevel: 1

## QL_MAIN_T3_INTRO
### qm_t3_scouting:
* Name:	New Frontiers
* Description:	With our improved hyperjump technology, we should upgrade our engines and sensors to explore the new areas.
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

### qm_t3_scouting_scanBelts:
* Name:	Resource Scouting
* Description:	Fleet command wants accurate maps of nearby asteroid clusters in order to chart resources and hazards. Contribute to this effort by scanning asteroid clusters.
* Type:	Main
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ScannedBelt
			* Total: 55

### qm_t3_scouting_scanJovian:
* Name:	Gas Giant Scan
* Description:	New scanning protocols for scanning gas giants are being tested. Contribute to this test by fully scanning a gas giant.
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
### qm_t3_gasMining:
* Name:	A New Resource
* Description:	We found a new type of resource that warrants a closer look. We should take some samples for study. To harvest gas, simply send a Gas Collector into the atmosphere of a gas planet. Be careful. Deeper layers will deal more damage to your ships! The blueprint for the Gas Collector can be found in the Market.
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
### qm_t3_yaotLiaison:
* Name:	Yaot Relations
* Description:	The Yaot have opened their liaison office to us.
* Type:	Side
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: RepYaot
			* Total: 1000

## QL_MAIN_T3_SIDEYAOT
### qm_t3_facYaot:
* Name:	Uneasy Allies
* Description:	The Yaot are interested in opening relations with us and wish to begin a dialogue.
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
### qm_t3_sideYaot_A_1:
* Name:	Truce: Loadstones I
* Description:	The Yaot present a simple request to map and gather resources in order to test our capabilities and their trust in us.
* Type:	Side
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ScannedBelt
			* Total: 65
		* GoalType: Pay
			* Id: 3O
			* Amount: 50

### qm_t3_sideYaot_A_2:
* Name:	Truce: Loadstones II
* Description:	The Yaot have asked us to collect further resources and clear the mining areas of hostiles.
* Type:	Side
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: Mined3C
			* Amount: 2500
		* GoalType: Statistic
			* Id: ShipsDestroyed
			* Amount: 30

### qm_t3_sideYaot_A_3:
* Name:	Truce: Loadstones III
* Description:	The Yaot are interested in learning our capacity for materials refining. We'll be compensated well.
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
### qm_t3_sideYaot_B_1:
* Name:	Truce: The Privateer I
* Description:	The Yaot have a supply line they want protected, and are willing to hire us to clear it of hostiles.
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

### qm_t3_sideYaot_B_2:
* Name:	Truce: The Privateer II
* Description:	The Yaot wish to commission us to guard this patrol route until their own patrols can relieve us.
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

### qm_t3_sideYaot_B_3:
* Name:	Truce: The Privateer III
* Description:	The Yaot are impressed with our combat capabilities and want to see how we fare against stronger enemies.
* Type:	Side
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T2up
			* Mode: Strike

## QL_MAIN_T3_SIDEYAOT_C
### qm_t3_sideYaot_C_1:
* Name:	Truce: Exchange of Ideas I
* Description:	The Yaot have made more contracts available to us on a trial basis. We should engage them.
* Type:	Side
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: Faction_Yaot_T3up

### qm_t3_sideYaot_C_2:
* Name:	Truce: Exchange of Ideas II
* Description:	The Yaot are becoming more comfortable with employing us. More work for them will go a long way to improving relations.
* Type:	Side
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: RepYaot
			* Amount: 250
		* GoalType: Statistic
			* Id: ShipsDestroyed
			* Amount: 30

### qm_t3_sideYaot_C_3:
* Name:	Truce: Exchange of Ideas III
* Description:	The Yaot trust us enough to employ our services on a contract basis. More work is available.
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
### qm_t3_facTanoch:
* Name:	Inside the Empire
* Description:	We have been contacted by the Chicuat people within the Tanoch empire. They have been denied Imperial services and are asking us for help.
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
### qm_t3_sideTanoch_A_1:
* Name:	Chicuat: Dry Well I
* Description:	Next to no Imperial resources are reaching the Chicuat worlds. They are asking us to provide what we spare.
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

### qm_t3_sideTanoch_A_2:
* Name:	Chicuat: Dry Well II
* Description:	The Chicuat refineries are busy with the ores we have provided. Meanwhile, an agricultural colony providing most of the food in the sector is running on systems that are barely holding together. They have asked us for spare parts.
* Type:	Side
* Goals:
	* 0:
		* GoalType: Pay
			* Id: intmed_module_large_t2
			* Amount: 15

### qm_t3_sideTanoch_A_3:
* Name:	Chicuat: Dry Well III
* Description:	The economic system has been stabilized, but without proper defenses, raiders will undo everything we've done. We should provide them with some fighters of their own and give their militia some training.
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
### qm_t3_sideTanoch_B_1:
* Name:	Chicuat: Exposed I
* Description:	Without Imperial patrols, Chicuat space is vulnerable against raiders. They have asked us to make a sweep across their space to clear the sector of hostiles.
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

### qm_t3_sideTanoch_B_2:
* Name:	Chicuat: Exposed II
* Description:	Most hostiles have been chased off, but some bold bands of the Fleet of Rams have refused to be intimidated. It is time to make a statement.
* Type:	Side
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 7
		* GoalType: Statistic
			* Id: ShipsDestroyedP1
			* Amount: 25

### qm_t3_sideTanoch_B_3:
* Name:	Chicuat: Exposed III
* Description:	The Chicuat officials have seen our results and several of them want to see us in action. They hope to learn from us how to organize their defenses better.
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
### qm_t3_sideTanoch_C_1:
* Name:	Chicuat: Favors I
* Description:	Our contact has suggested running some errands for the Tanoch in the name of the Chicuat people. Doing so would hopefully increase the Chicuat's standing within the Empire.
* Type:	Side
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: RepTanoch
			* Amount: 500

### qm_t3_sideTanoch_C_2:
* Name:	Chicuat: Favors II
* Description:	The Empire is reacting to our support of the Chicuat people. While we wait to learn more about the outcome, the Chicuat have asked if their officers can cross-train with ours.
* Type:	Side
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 15
		* GoalType: CompleteQuest
			* Amount: 7
			* Tags: Faction_Tanoch_T2up

### qm_t3_sideTanoch_C_3:
* Name:	Chicuat: Favors III
* Description:	After lengthy negotiations with the Chicuat, the Empire reluctantly has agreed to a relief operation, sending resources to worlds in need. Naturally they ask us for support instead of sending their own materials...
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
### qm_t3_starTotek:
* Name:	Star Totek
* Description:	We are closing in on possible Vaygr transmissions close to the star.
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
### qm_t3_strikeBreach:
* Name:	Breach
* Description:	We found an enemy base that is heavily fortified. Breaching its defenses will not be easy.
* Type:	Side
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Ids:
				* Refining3N
				* Refining3O
				* Refining3P
				* Refining3Q
			* Amount: 1

## QL_MAIN_T3_SIDEHIIG
### qm_t3_facHiigaran:
* Name:	Planting the Flag
* Description:	Lazarus Base calls us back to the Hiigaran colonies to establish a presence there and keep the peace.
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
### qm_t3_sideHiigaran_A_1:
* Name:	Colonies: Brick Making I
* Description:	Hiigaran resource efforts are very short handed, so we’ll be going to assist gas collection in deep space.
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

### qm_t3_sideHiigaran_A_2:
* Name:	Colonies: Brick Making II
* Description:	Our assistance has been helpful so far, but we are asked to provide and analyze some ore samples from the deeper regions of the galaxy.
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

### qm_t3_sideHiigaran_A_3:
* Name:	Colonies: Brick Making III
* Description:	The logistics have been set up for the most part, but we are asked to help with some deliveries.
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
### qm_t3_sideHiigaran_B_1:
* Name:	Colonies: Security Blanket I
* Description:	Lazarus base has established a quota for all commanders hunting loose pirates in Hiigaran space.
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

### qm_t3_sideHiigaran_B_2:
* Name:	Colonies: Security Blanket II
* Description:	Most pirates have gone into hiding, but we are asked to make sweeps of local space, to flush out the remaining hostiles.
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

### qm_t3_sideHiigaran_B_3:
* Name:	Colonies: Security Blanket III
* Description:	The hostile presence has been reduced to a manageable level, but Progenitor craft threaten research vessels. We need to get rid of them and analyze some of the debris.
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
### qm_t3_sideHiigaran_C_1:
* Name:	Colonies: The Next Generation I
* Description:	Lazarus has sent us some trainees to get some practical experience on our ship.
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

### qm_t3_sideHiigaran_C_2:
* Name:	Colonies: The Next Generation II
* Description:	Many of the trainees are going to become pilots and navigators, but have so far trained in controlled or virtual flight simulators. They need some real experience.
* Type:	Side
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: Ship_Unit_T3up
			* Amount: 5
		* GoalType: UpgradeOfficer
			* Amount: 20

### qm_t3_sideHiigaran_C_3:
* Name:	Colonies: The Next Generation III
* Description:	The final course is the graduation level for the trainees, who must see actual combat. You are to take the crew into battle and complete the course. Once finished, they return to Lazarus to finish up their coursework.
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
### qm_t3_facIyatequa:
* Name:	Blue Collar Work
* Description:	Ekekko informed us about exclusive work needed by the Iyatequa, and the traders will pay well for this assistance. This is below the table work on various jobs they don’t widely advertise for. They do not say what the ultimate purpose of this work is, though.
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
### qm_t3_sideIyatequa_A_1:
* Name:	Contracts: The Empty Quarter I
* Description:	A small world in the Empty Quarter is looking for trustworthy connections. They offer an assortment of various tasks.
* Type:	Side
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 7
			* Tags: Faction_Tr1_T3up
		* GoalType: Statistic
			* Id: PlayerXP
			* Amount: 2250

### qm_t3_sideIyatequa_A_2:
* Name:	Contracts: The Empty Quarter II
* Description:	A wealthy socialite has heard of our accomplishments and wants some things done. Discreetly, of course.
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

### qm_t3_sideIyatequa_A_3:
* Name:	Contracts: The Empty Quarter III
* Description:	Our contact in the Empty Quarter is looking for new opportunities and has been pleased with our work so far. They want us to scout out new areas of space in order to expand their influence.
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
### qm_t3_sideIyatequa_B_1:
* Name:	Contracts: Territory Claim I
* Description:	The Iyatequa plan to set up new trading routes in space currently riddled by pirates. They asked us to clean up the area.
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

### qm_t3_sideIyatequa_B_2:
* Name:	Contracts: Territory Claim II
* Description:	Some pirates apparently didn't get the hint yet. We should show them the Iyatequa mean business.
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

### qm_t3_sideIyatequa_B_3:
* Name:	Contracts: Territory Claim III
* Description:	Most pirates have dispersed, but just to make sure they do not come back we should increase our reputation so future raiders will think twice before setting up nests here.
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
### qm_t3_sideIyatequa_C_1:
* Name:	Contracts: Supplies I
* Description:	A local world wants help building and supplying a space station. We are asked to test possible mining sites and clear them of hostiles.
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

### qm_t3_sideIyatequa_C_2:
* Name:	Contracts: Supplies II
* Description:	Mining ships have departed for the asteroids we have charted, but the internal systems require special gases. We are asked to sample the gases at promising jovians.
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

### qm_t3_sideIyatequa_C_3:
* Name:	Contracts: Supplies III
* Description:	The mining sites have been prepared, but the Iyatequa asked us with further assistance through supplies and mining craft.
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
### qm_t3_facCangacian:
* Name:	Roadblocks
* Description:	Reports at the Tanoch border are coming in stating that the Fleet of Rams, Supay’s army, is on the move at last.
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
### qm_t3_sideCangacian_A_1:
* Name:	Defense: Intercept I
* Description:	We are asked to intercept as many Cangacian fleets as we can.
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

### qm_t3_sideCangacian_A_2:
* Name:	Defense: Intercept II
* Description:	The Cangacians continue to probe the Tanoch defenses. We should look for suspicious activity.
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

### qm_t3_sideCangacian_A_3:
* Name:	Defense: Intercept III
* Description:	Supay's fleets may have holdouts in systems we have not been looking yet. We should find those and flush them out.
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
### qm_t3_sideCangacian_B_1:
* Name:	Defense: Assist I
* Description:	To counter these attacks our crew must be well trained.
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

### qm_t3_sideCangacian_B_2:
* Name:	Defense: Assist II
* Description:	Our crew is analyzing the attack patterns to find ways to predict where the Fleet of Rams may strike next.
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

### qm_t3_sideCangacian_B_3:
* Name:	Defense: Assist III
* Description:	Several smaller worlds on the border have sent us some of their recruits, in hopes they could get some practical experience from our battles with the Cangacians.
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
### qm_t3_sideCangacian_C_1:
* Name:	Defense: Barricade I
* Description:	Several mining fleets of the border systems have taken losses and are asking us to provide them with safe locations to find resources.
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

### qm_t3_sideCangacian_C_2:
* Name:	Defense: Barricade II
* Description:	The remaining mining fleets are flocking to the new mining spots, but they require gases for advanced weaponry.
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

### qm_t3_sideCangacian_C_3:
* Name:	Defense: Barricade III
* Description:	The border worlds' new mining lanes are buzzing with activity, but they need supplies to build up defenses against future raids.
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
### qm_t3_sijinLighthouse:
* Name:	Sijin Lighthouse
* Description:	We detected a possible signal from the missing Khar-Kalaad.
* Type:	Main
* CinematicIds:	40
* FollowUps: ql_main_t4_intro
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: story_D01_SijinLighthouse

## QL_MAIN_T4_INTRO
### qm_t4_researchJumpCap:
* Name:	Mind the Gap
* Description:	Crossing the Nightmare Gulf requires an upgrade to our hyperjump technology. After some scans of the gate at Sijin Lighthouse, our scientists think they are able to make the leap possible.
* Type:	Main
* FollowUps: ql_main_t4_iliyinLighthouse
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Research
			* Id: rp_catExpl_hyperCap_t4_c
			* MinLevel: 1

## QL_MAIN_T4_ILIYINLIGHTHOUSE
### qm_t4_iliyinLighthouse:
* Name:	Iliyin Lighthouse
* Description:	We have arrived at another lighthouse in uncharted territory. Be prepared for anything.
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
### qm_t4_amassariLiaison:
* Name:	Amassari Relations
* Description:	The Amassari have opened their liaison office to us.
* Type:	Side
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: RepAmassari
			* Total: 1000

## QL_MAIN_T4_MOONRESOURCES
### qm_t4_moonResources:
* Name:	Crystals
* Description:	Crystals are a new type of resource that can be combined with refined metals into a composite material needed for advanced constructions. So far we have only been able to find them by chance in <color=#FBB03F>signals and liaison missions</color>.
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
### qm_t4_brightTemple:
* Name:	Bright Temple
* Description:	The Amassari here may contain answers about the nature of the Progenitor observer.
* Type:	Main
* FollowUps: ql_main_t4_postBrightTemple
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: story_D03_BrightTemple

## QL_MAIN_T4_POSTBRIGHTTEMPLE
### qm_t4_postBrightTemple_1:
* Name:	Among the People
* Description:	We should take this time to become better acquainted with the Amassari and their culture. Performing tasks for the assorted groups will accomplish this.
* Type:	Main
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: RepAmassari
			* Amount: 1000

### qm_t4_postBrightTemple_2:
* Name:	Fabrication Methods
* Description:	A new technique for refining was discovered from the Amassari. Test this process by refining rare earths.
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

### qm_t4_postBrightTemple_3:
* Name:	Experience and Knowledge
* Description:	Our crews need a new round of training to become familiar with Amassari practices and tactics.
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
### qm_t4_hataldan:
* Name:	Hataldan
* Description:	The fallen capital of the Amassari, and last known position of the Observer.
* Type:	Main
* FollowUps: ql_main_t4_postHataldan
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: story_D04_Hataldan

## QL_MAIN_T4_POSTHATALDAN
### qm_t4_postHataldan_1:
* Name:	The Hunt Begins
* Description:	The search begins for Kidara and the stolen Observer. We must examine any objects we can find scattered around for clues about her whereabouts.
* Type:	Main
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_Container_T4up
			* Amount: 10
			* Analyzed: True

### qm_t4_postHataldan_2:
* Name:	Forcible Interrogation
* Description:	Destroying Kiithless ships and scavenging their databanks could fill some gaps in our intelligence about the Kiithless. The hunt continues!
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

### qm_t4_postHataldan_3:
* Name:	Pieces of the Puzzle
* Description:	A cryptic clue that emerged from harvesting Kiithless vessels may have a solution if we can piece together a saga from the Hagthar Empire. Collect relics from these ancient people.
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
### qm_t4_nightmareGulf:
* Name:	Nightmare Gulf
* Description:	The Hagthar knew of pockets and safe regions close to this massive interstellar storm. We now know the way to Kidara's hideout in The Nightmare Gulf. It's time to end this.
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
### qm_t4_strikeNightmareGulf:
* Name:	Strike at Nightmare Gulf
* Description:	The Hagthar knew of pockets and safe regions close to this massive interstellar storm. We now know the way to Kidara's hideout in The Nightmare Gulf. It's time to end this.
* Type:	Side
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Ids:
				* SellItem
				* BuyItem
				* MoveToUser
				* RemoveFromInventory
				* MoveToStash
				* RetrieveFromStash
			* Amount: 1

## QL_MAIN_T4_TANWIN
### qm_t4_tanWin_DefendBase:
* Name:	Gesture of Aid
* Description:	We received emergency communication from the Chicuat Elders. They anticipate a raid on one of their remote trading stations. Toci asks us to take on the defense in order to relieve the weakened and overextended Chicuat forces.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Type:	Main
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_tanWin2023_DefendBase_t4

### qm_t4_tanWin_AttackBase:
* Name:	In the Shadows
* Description:	Intelligence from the Chicuat points to a Tecuban base operating around an uninhabited planet. We must go there and eliminate this base to stop the raids.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Type:	Main
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_tanWin2023_AttackBase_t4

### qm_t4_tanWin_Relic:
* Name:	Attack the Vaygr
* Description:	In our search for the Vaygr involved with the Tecuban, we aquired one of their communication frequencies. If we contact the Vaygr now, we should be able to trace their signal and hyper jump to their exact location.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Type:	Main
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_tanWin2023_Relic_t4

### qm_t4_tanWin_Academy:
* Name:	Showdown at the Academy
* Description:	We finally learned Jochik Kaan's intentions. He sparked the flames of war to weaken the Chicuat defenses and steal the Baetyl from Tlapallan Academy, one of their key centers of learning. We must travel there at once, before it is too late.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Type:	Main
* FollowUps: ql_main_t4_yaoSpr
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_tanWin2023_Academy_t4

## QL_MAIN_T4_YAOSPR
### qm_t4_yaoSpr_Conjunction:
* Name:	The Promised Place
* Description:	Chocoan has provided the coordinates to the next astral conjunction event. Strong hostile forces are to be expected in this system. Our goal is to both protect the civilian pilgrims and find out more about the suspected secret agenda of the Yaot Elders.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Type:	Main
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_yaoSpr2024_Conjunction_t4

## QL_ORB_T3_INTRO
### qm_orb_t3_components:
* Name:	Starbase Components
* Description:	<color=#FBB03F>The blueprints for starbase components can be found in the liaison requisitions offices.</color>

Our engineers have come up with a plan to build a starbase, which will serve as our base of operations. Before we can do that, however, we need to construct the necessary components.
* Type:	Side
* Goals:
	* 0:
		* GoalType: Craft
			* Id: playerOrb_comp_stabilizer_t3
		* GoalType: Craft
			* Id: playerOrb_comp_frame_t3
		* GoalType: Craft
			* Id: playerOrb_comp_lifeSupport_t3

### qm_orb_t3_orbital:
* Name:	Starbase
* Description:	<color=#FBB03F>The blueprint for the starbase can be found in the regular market.</color>

Now that we have the components, we can build the starbase proper. Once the pieces have been constructed, it can be quickly assembled in orbit around celestial objects.
* Type:	Side
* Goals:
	* 0:
		* GoalType: Craft
			* Id: hgn_co_orbi_01_t1

### qm_orb_t3_placeOrbital:
* Name:	Starbase Placement
* Description:	<color=#FBB03F>Place or relocate your starbase by selecting a celestial object in the target list inside the star system view.</color>

Our finished starbase is ready and can be placed in orbit of a planet or moon.
* Type:	Side
* Goals:
	* 0:
		* GoalType: PlaceOrbital
			* NoParameter: None

### qm_orb_t3_modules:
* Name:	Starbase Modules
* Description:	<color=#FBB03F>The regular fabricator and refinery module can be mounted on the starbase, but there are specialized starbase modules. Blueprints for some of those can be found in the liaison requisitions offices.</color>

Now that our starbase is finished, we can start filling it up with modules.
* Type:	Side
* Goals:
	* 0:
		* GoalType: Equip
			* Type: Internal
			* Tags: Orbital
			* Target: hgn_co_orbi_01_t1

## QL_SIDE_EXPLORATION
### qs_exploration_01:
* Name:	Exploration I
* Description:	We should explore this galaxy further. Who knows what we could find.
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

### qs_exploration_02:
* Name:	Exploration II
* Description:	We have made discoveries that will keep our scientists busy for months.
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

### qs_exploration_03:
* Name:	Exploration III
* Description:	This galaxy is full of danger and opportunity. We should analyze and prepare.
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
### qs_economy_01:
* Name:	Production I
* Description:	Building up a fleet requires a constant supply of materials.
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

### qs_economy_02:
* Name:	Production II
* Description:	We should not let our fabrication modules go idle.
* Type:	Side
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Amount: 50

### qs_economy_03:
* Name:	Production III
* Description:	Building bigger and greater ships will require bigger and greater materials.
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
### qs_battle_01:
* Name:	Combat I
* Description:	Space is full of danger. We need to be prepared.
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

### qs_battle_02:
* Name:	Combat II
* Description:	We need allies if we are to survive in this galaxy.
* Type:	Side
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 25
			* Tags: Faction_T2up

### qs_battle_03:
* Name:	Combat III
* Description:	Only great challenges yield great rewards.
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
### qs_unlockStrikes_t2:
* Name:	Rising to the Challenge
* Description:	As we venture further into this galaxy, we will encounter greater and greater threats. We need to be prepared.
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
### qs_unlockStrikes_t3:
* Name:	Rising to the Challenge
* Description:	As we venture further into this galaxy, we will encounter greater and greater threats. We need to be prepared.
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
### qs_Keid_01:
* Name:	The Siege of Keid
* Description:	Keid is struggling under the weight of enemy attacks and depleted resources. Help them take back control of the system.
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

### qs_Keid_02:
* Name:	Rebuilding Keid
* Description:	The people of Keid suffer from a lack of resources. Support them by collecting and refining resources.
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

### qs_Keid_03:
* Name:	The Future of Keid
* Description:	Donate your hard-earned resources and credits so that the people of Keid may fight on.
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
### qs_Exile_01:
* Name:	A Test of Might
* Description:	Destroy pirates and complete strikes to prove your strength.
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

### qs_Exile_02:
* Name:	The Nomad's Walk
* Description:	Gather resources and craft units to demonstrate your independence and self-reliance.
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

### qs_Exile_03:
* Name:	The Cartographer's Promise
* Description:	Travel across the galaxy and discover new locations to help chart the unknown.
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
### qs_Ytep_01:
* Name:	Ytep Under Fire
* Description:	Help the people of Ytep take back control of the system by pushing back enemies.
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

### qs_Ytep_02:
* Name:	Supplying the War Effort
* Description:	Collect enough parts and ships to support the war effort in Ytep.
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

### qs_Ytep_03:
* Name:	To Strengthen Ytep
* Description:	Donate T2 parts and ships to help the people of Ytep fight after you are gone.
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
### qs_killPirate1_pre01:
* Name:	Cangacian Raider Fleets I
* Description:	Pirates known as the Cangacians are harassing trade fleets of the Iyatequa.
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedP1
			* Total: 10

### qs_killPirate1_00:
* Name:	Cangacian Raider Fleets II
* Description:	More Cangacian activity is being reported.
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedP1
			* Total: 25

### qs_killPirate1_01:
* Name:	Cangacian Raider Fleets III
* Description:	Give the pirates a bloody nose. Show them you're no pushover.
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedP1
			* Total: 50

### qs_killPirate1_02:
* Name:	Cangacian Raider Fleets IV
* Description:	Hunt down pirate ships to suppress their activities in the area.
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedP1
			* Total: 100

### qs_killPirate1_03:
* Name:	Cangacian Raider Fleets V
* Description:	Beat back the local pirates by eliminating most of their forces.
* Type:	Achievement
* FollowUps: ql_esca_killYaot
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedP1
			* Total: 200

### qs_killPirate1_04:
* Name:	Cangacian Raider Fleets VI
* Description:	An organized pirate force has moved into the area. Show them they are not welcome.
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedP1
			* Total: 400

### qs_killPirate1_05:
* Name:	Cangacian Raider Fleets VII
* Description:	The Fleet of Rams has increased their presence. Meet them with equal enmity.
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedP1
			* Total: 800

### qs_killPirate1_06:
* Name:	Cangacian Raider Fleets VIII
* Description:	The Fleet of Rams is hunting the local defenders. Oppose them with force!
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedP1
			* Total: 1600

### qs_killPirate1_07:
* Name:	Cangacian Raider Fleets IX
* Description:	Supay himself has routed one of his fleets to the area. Engage them at will!
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedP1
			* Total: 3200

### qs_killPirate1_08:
* Name:	Cangacian Raider Fleets X
* Description:	Send a message to Supay, warlord of the Fleet of Rams. Destroy one of his fleets.
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedP1
			* Total: 6400

## QL_ESCA_KILLTANOCH
### qs_killTanoch_pre01:
* Name:	Tanoch Renegade Fleets I
* Description:	Renegades of the Tanoch nation are disrupting the peace of the empire.
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedTanoch
			* Total: 10

### qs_killTanoch_00:
* Name:	Tanoch Renegade Fleets II
* Description:	More renegade fleets are being reported.
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedTanoch
			* Total: 25

### qs_killTanoch_01:
* Name:	Tanoch Renegade Fleets III
* Description:	Poach Tanoch patrols to weaken their activities in the area. Hostile Tanoch signals have been located in T2 systems and higher.
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedTanoch
			* Total: 50

### qs_killTanoch_02:
* Name:	Tanoch Renegade Fleets IV
* Description:	Continue to attack Tanoch patrols to weaken their local status. Hostile Tanoch signals have been located in T2 systems and higher.
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedTanoch
			* Total: 100

### qs_killTanoch_03:
* Name:	Tanoch Renegade Fleets V
* Description:	Tanoch freighter crews fear your arrival. Continue the attacks! Hostile Tanoch signals have been located in T2 systems and higher.
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedTanoch
			* Total: 200

### qs_killTanoch_04:
* Name:	Tanoch Renegade Fleets VI
* Description:	Tanoch freighters request action against you. Continue the attacks! Hostile Tanoch signals have been located in T2 systems and higher.
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedTanoch
			* Total: 400

### qs_killTanoch_05:
* Name:	Tanoch Renegade Fleets VII
* Description:	The Tanoch patrol force recognizes you on sight. Continue the attacks! Hostile Tanoch signals have been located in T2 systems and higher.
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedTanoch
			* Total: 800

### qs_killTanoch_06:
* Name:	Tanoch Renegade Fleets VIII
* Description:	Tanoch warning stations alert the Empire to your presence. Continue your attacks! Hostile Tanoch signals have been located in T2 systems and higher.
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedTanoch
			* Total: 1600

### qs_killTanoch_07:
* Name:	Tanoch Renegade Fleets IX
* Description:	The Tanoch regard you as a fleet-level threat. Continue your assaults against them! Hostile Tanoch signals have been located in T2 systems and higher.
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedTanoch
			* Total: 3200

### qs_killTanoch_08:
* Name:	Tanoch Renegade Fleets X
* Description:	The Emperor will know your name. Hostile Tanoch signals have been located in T2 systems and higher.
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedTanoch
			* Total: 6400

## QL_ESCA_KILLYAOT
### qs_killYaot_pre01:
* Name:	Yaot Rebel Fleets I
* Description:	Some Yaot that are dissatisfied with the government have begun causing chaos in regional space.
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedYaot
			* Total: 10

### qs_killYaot_00:
* Name:	Yaot Rebel Fleets II
* Description:	More Yaot rebels have been reported.
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedYaot
			* Total: 25

### qs_killYaot_01:
* Name:	Yaot Rebel Fleets III
* Description:	Attack the Yaot patrols to drive them from this area.
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedYaot
			* Total: 50

### qs_killYaot_02:
* Name:	Yaot Rebel Fleets IV
* Description:	Continue attacking the Yaot to drive them from the region.
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedYaot
			* Total: 100

### qs_killYaot_03:
* Name:	Yaot Rebel Fleets V
* Description:	Yaot Fleet captains recognize your silhouette. Continue the attack.
* Type:	Achievement
* FollowUps: ql_esca_killTanoch
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedYaot
			* Total: 200

### qs_killYaot_04:
* Name:	Yaot Rebel Fleets VI
* Description:	Yaot sensors are alerted to your presence. Continue the attack!
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedYaot
			* Total: 400

### qs_killYaot_05:
* Name:	Yaot Rebel Fleets VII
* Description:	Yaot Fleet commanders are watching out for you. Continue your assaults against them!
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedYaot
			* Total: 800

### qs_killYaot_06:
* Name:	Yaot Rebel Fleets VIII
* Description:	Your name is mentioned between Yaot Fleet commanders. Continue your attacks!
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedYaot
			* Total: 1600

### qs_killYaot_07:
* Name:	Yaot Rebel Fleets IX
* Description:	You are impacting Yaot fleet operations in this area. Continue your attack!
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedYaot
			* Total: 3200

### qs_killYaot_08:
* Name:	Yaot Rebel Fleets X
* Description:	Your threat level among the Yaot is higher than most Tanoch fleets. Continue the attack!
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedYaot
			* Total: 6400

## QL_ESCA_MINET1
### qs_mineT1ABC_pre01:
* Name:	Mining Procedures I
* Description:	We need to test our mining equipment.
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

### qs_mineT1ABC_00:
* Name:	Mining Procedures II
* Description:	We should check our mining procedures and see if we could streamline the process.
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

### qs_mineT1ABC_01:
* Name:	Mining Procedures III
* Description:	Start collecting asteroids to calibrate our resource refinery methods.
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

### qs_mineT1ABC_02:
* Name:	Mining Procedures IV
* Description:	More materials are necessary to establish our baseline. Harvest more asteroids.
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

### qs_mineT1ABC_03:
* Name:	Mining Procedures V
* Description:	Our refineries have been calibrated to local nimbus materials. Begin our first production haul.
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

### qs_mineT1ABC_04:
* Name:	Mining Procedures VI
* Description:	Begin our second production haul for processing.
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

### qs_mineT1ABC_05:
* Name:	Mining Procedures VII
* Description:	Begin our third production haul for processing.
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

### qs_mineT1ABC_06:
* Name:	Mining Procedures VIII
* Description:	Begin our fourth production haul for processing.
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

### qs_mineT1ABC_07:
* Name:	Mining Procedures IX
* Description:	One final haul is needed to certify the refinery for full operations.
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

### qs_mineT1ABC_08:
* Name:	Mining Procedures X
* Description:	One last production haul is needed to certify the refinery for Grade 1 Procesing.
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
### qs_mineT2ABC_pre01:
* Name:	New Mining Procedures I
* Description:	We need to test our mining equipment on these new types of minerals.
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

### qs_mineT2ABC_00:
* Name:	New Mining Procedures II
* Description:	We should check our mining procedures on these new types of minerals.
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

### qs_mineT2ABC_01:
* Name:	New Mining Procedures III
* Description:	Engineering has proposed minor upgrades to the refinery process. Harvest larger asteroids for testing.
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

### qs_mineT2ABC_02:
* Name:	New Mining Procedures IV
* Description:	Engineering is ready to implement these minor changes. Continue supplying larger resources.
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

### qs_mineT2ABC_03:
* Name:	New Mining Procedures V
* Description:	Engineering wants to test further refits to the refinery. Supply additional resources for testing.
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

### qs_mineT2ABC_04:
* Name:	New Mining Procedures VI
* Description:	Continue refinery trials. Provide larger resources.
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

### qs_mineT2ABC_05:
* Name:	New Mining Procedures VII
* Description:	Continue refinery trials. Provide larger resources.
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

### qs_mineT2ABC_06:
* Name:	New Mining Procedures VIII
* Description:	Continue refinery trials. Provide larger resources.
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

### qs_mineT2ABC_07:
* Name:	New Mining Procedures IX
* Description:	Continue refinery trials. Provide larger resources.
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

### qs_mineT2ABC_08:
* Name:	New Mining Procedures X
* Description:	One final load is necessary to approve the new refit to the refinery.
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
### qs_mineT3ABC_pre01:
* Name:	Advanced Mining Procedures I
* Description:	We need to test our mining equipment on these new types of minerals.
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

### qs_mineT3ABC_00:
* Name:	Advanced Mining Procedures II
* Description:	We should check our mining procedures on these new types of minerals.
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

### qs_mineT3ABC_01:
* Name:	Advanced Mining Procedures III
* Description:	Refinery teams propose a new chemical process for resource extraction.
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

### qs_mineT3ABC_02:
* Name:	Advanced Mining Procedures IV
* Description:	Supply reduced manpower tests by harvesting further resources.
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

### qs_mineT3ABC_03:
* Name:	Advanced Mining Procedures V
* Description:	Conducting reduced manpower stress test on refinery complex.
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

### qs_mineT3ABC_04:
* Name:	Advanced Mining Procedures VI
* Description:	Conducting reduced manpower stress test on refinery complex.
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

### qs_mineT3ABC_05:
* Name:	Advanced Mining Procedures VII
* Description:	Conducting reduced manpower stress test on refinery complex.
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

### qs_mineT3ABC_06:
* Name:	Advanced Mining Procedures VIII
* Description:	Conducting reduced manpower stress test on refinery complex.
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

### qs_mineT3ABC_07:
* Name:	Advanced Mining Procedures IX
* Description:	Final test of reduced crew capacity through new refinery process. Procure resources.
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

### qs_mineT3ABC_08:
* Name:	Advanced Mining Procedures X
* Description:	Final certification of refinery postprocessing procedure. Supply resources for this test.
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
### qs_scan_pre01:
* Name:	System Charts I
* Description:	We should explore the star systems in this new galaxy.
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: Scanned
			* Total: 50

### qs_scan_00:
* Name:	System Charts II
* Description:	We need to fill our system charts with actual data.
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: Scanned
			* Total: 150

### qs_scan_01:
* Name:	System Charts III
* Description:	The new sensor suite needs raw data to begin configuring the array. Begin scanning.
* Type:	Achievement
* FollowUps: ql_esca_generated
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: Scanned
			* Total: 300

### qs_scan_02:
* Name:	System Charts IV
* Description:	The array is ready to begin trials. Begin scanning targets.
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: Scanned
			* Total: 600

### qs_scan_03:
* Name:	System Charts V
* Description:	Begin testing short range detection sensors. Begin scanning targets.
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: Scanned
			* Total: 1200

### qs_scan_04:
* Name:	System Charts VI
* Description:	Conduct scans. Calibration will focus on short range performance.
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: Scanned
			* Total: 2500

### qs_scan_05:
* Name:	System Charts VII
* Description:	Conduct scans. Calibration will focus on long range performance.
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: Scanned
			* Total: 5000

### qs_scan_06:
* Name:	System Charts VIII
* Description:	Conduct Scans. Calibration will focus on hyperspace oddities.
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: Scanned
			* Total: 10000

### qs_scan_07:
* Name:	System Charts IX
* Description:	Conduct scans. Calibration will focus on signals moving at distance.
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: Scanned
			* Total: 20000

### qs_scan_08:
* Name:	System Charts X
* Description:	Final comprehensive test of all sensor systems.
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: Scanned
			* Total: 40000

## QL_ESCA_GENERATED
### qs_finishGenerated_pre01:
* Name:	Signal Search I
* Description:	We should look out for possible signals in deep space. They could represent opportunities for us.
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: MissionsDoneGenerated
			* Total: 2

### qs_finishGenerated_00:
* Name:	Signal Search II
* Description:	We should actively search for signals in deep space.
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: MissionsDoneGenerated
			* Total: 5

### qs_finishGenerated_01:
* Name:	Signal Search III
* Description:	Signals investigation for pathfinding and reconnaissance.
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: MissionsDoneGenerated
			* Total: 10

### qs_finishGenerated_02:
* Name:	Signal Search IV
* Description:	Further investigate mysterious signals for pathfinding and reconnaissance.
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: MissionsDoneGenerated
			* Total: 20

### qs_finishGenerated_03:
* Name:	Signal Search V
* Description:	Hunt for anomalous signals to unlock further discoveries and rewards.
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: MissionsDoneGenerated
			* Total: 40

### qs_finishGenerated_04:
* Name:	Signal Search VI
* Description:	Establish signal gain and investigation methods.
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: MissionsDoneGenerated
			* Total: 80

### qs_finishGenerated_05:
* Name:	Signal Search VII
* Description:	Routine investigation of anomalous signals.
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: MissionsDoneGenerated
			* Total: 160

### qs_finishGenerated_06:
* Name:	Signal Search VIII
* Description:	Special teams designated for signal investigations response.
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: MissionsDoneGenerated
			* Total: 320

### qs_finishGenerated_07:
* Name:	Signal Search IX
* Description:	Catalogue of anomalous activities established.
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: MissionsDoneGenerated
			* Total: 640

### qs_finishGenerated_08:
* Name:	Signal Search X
* Description:	Investigative mastery.
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: MissionsDoneGenerated
			* Total: 1300

## QL_RAID_013
### qr_013:
* Name:	Pirate Hideout
* Description:	A lot of pirate activity has been reported in this region. The local pirate faction must have a major base here. Our task is to find the base, and destroy any pirate vessel and structure in this sector.
* Type:	Strike
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: strike_01_PirateHideout

## QL_RAID_016
### qr_016:
* Name:	Pirate Hideout (Heroic)
* Description:	A lot of pirate activity has been reported in this region. The local pirate faction must have a major base here. Our task is to find the base, and destroy any pirate vessel and structure in this sector.
* Type:	Strike
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: strike_01_PirateHideout_heroic

## QL_RAID_014
### qr_014:
* Name:	Station Defense
* Description:	We have received intel that enemy forces are planning to attack a local trading station. In order to defend the station, we must immediately move our fleet into defensive position.
* Type:	Strike
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: strike_02_StationDefense

## QL_RAID_017
### qr_017:
* Name:	Station Defense (Heroic)
* Description:	We have received intel that enemy forces are planning to attack a local trading station. In order to defend the station, we must immediately move our fleet into defensive position.
* Type:	Strike
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: strike_02_StationDefense_heroic

## QL_RAID_021
### qr_021:
* Name:	Station Defense (Mythic)
* Description:	We have received intel that enemy forces are planning to attack a local trading station. In order to defend the station, we must immediately move our fleet into defensive position.
* Type:	Strike
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: strike_02_StationDefense_mythic

## QL_RAID_015
### qr_015:
* Name:	Pahra's Rock
* Description:	The presence of a large Cangacian asteroid base in this area has been threatening the Hiigaran settlements. Our task is to perform an attack on this base, destroy it and any Cangacian fleet nearby.
* Type:	Strike
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: strike_03_PahrasRock

## QL_RAID_018
### qr_018:
* Name:	Pahra's Rock (Heroic)
* Description:	The presence of a large Cangacian asteroid base in this area has been threatening the Hiigaran settlements. Our task is to perform an attack on this base, destroy it and any Cangacian fleet nearby.
* Type:	Strike
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: strike_03_PahrasRock_heroic

## QL_RAID_022
### qr_022:
* Name:	Pahra's Rock (Mythic)
* Description:	The presence of a large Cangacian asteroid base in this area has been threatening the Hiigaran settlements. Our task is to perform an attack on this base, destroy it and any Cangacian fleet nearby.
* Type:	Strike
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: strike_03_PahrasRock_mythic

## QL_RAID_019
### qr_019:
* Name:	Breach
* Description:	Sitting in a safe pocket inside an electromagnetic asteroid field, this station is a crucial base of operation. As it is heavily defended, we came up with the cunning plan to fill an old freighter with explosives and escort it to the base.
* Type:	Strike
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: strike_04_Breach

## QL_RAID_020
### qr_020:
* Name:	Breach (Heroic)
* Description:	Sitting in a safe pocket inside an electromagnetic asteroid field, this station is a crucial base of operation. As it is heavily defended, we came up with the cunning plan to fill an old freighter with explosives and escort it to the base.
* Type:	Strike
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: strike_04_Breach_heroic

## QL_RAID_023
### qr_023:
* Name:	Nightmare Gulf
* Description:	A base used by Kiithless raiders has been located in this area of the nightmare gulf. A large attack force will be needed to destroy it and free the Progenitor assets held at this location.
* Type:	Strike
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: strike_05_NightmareGulf

## QL_EVENT_TEST_1
### qe_test_eventtestquest_1:
* Name:	No header for quest qe_test_eventtestquest_1
* Description:	No description for quest qe_test_eventtestquest_1
* Type:	Event
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Amount: 10

## QL_EVENT_TEST_2
### qe_test_eventtestquest_2:
* Name:	No header for quest qe_test_eventtestquest_2
* Description:	No description for quest qe_test_eventtestquest_2
* Type:	Event
* Goals:
	* 0:
		* GoalType: Pay
			* Id: CR
			* Amount: 10

## QL_EVENT_TEST_3
### qe_test_eventtestquest_3:
* Name:	No header for quest qe_test_eventtestquest_3
* Description:	No description for quest qe_test_eventtestquest_3
* Type:	Event
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1

## QL_YAOT_SPRING_2023_DAILY_A_T2
### qe_yaot_spring_2023_daily_A_t2:
* Name:	No header for quest qe_yaot_spring_2023_daily_A_t2
* Description:	No description for quest qe_yaot_spring_2023_daily_A_t2
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
### qe_yaot_spring_2023_daily_B_t2:
* Name:	No header for quest qe_yaot_spring_2023_daily_B_t2
* Description:	No description for quest qe_yaot_spring_2023_daily_B_t2
* Type:	Event
* EventId:	event_season_yaoSpr_2023
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedTanoch
			* Amount: 10

## QL_YAOT_SPRING_2023_DAILY_C_T3
### qe_yaot_spring_2023_daily_C_t3:
* Name:	No header for quest qe_yaot_spring_2023_daily_C_t3
* Description:	No description for quest qe_yaot_spring_2023_daily_C_t3
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
### qe_yaot_spring_2023_daily_D_t3:
* Name:	No header for quest qe_yaot_spring_2023_daily_D_t3
* Description:	No description for quest qe_yaot_spring_2023_daily_D_t3
* Type:	Event
* EventId:	event_season_yaoSpr_2023
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: Faction_Yaot

## QL_EVENT_YAOT_SPRING_2023
### qe_yaot_spring_2023_day1:
* Name:	No header for quest qe_yaot_spring_2023_day1
* Description:	No description for quest qe_yaot_spring_2023_day1
* Type:	Event
* EventId:	event_season_yaoSpr_2023
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: Mined
			* Amount: 750

### qe_yaot_spring_2023_day2:
* Name:	No header for quest qe_yaot_spring_2023_day2
* Description:	No description for quest qe_yaot_spring_2023_day2
* Type:	Event
* EventId:	event_season_yaoSpr_2023
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Mode: Generated

### qe_yaot_spring_2023_day3:
* Name:	No header for quest qe_yaot_spring_2023_day3
* Description:	No description for quest qe_yaot_spring_2023_day3
* Type:	Event
* EventId:	event_season_yaoSpr_2023
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Refining
			* Amount: 500

### qe_yaot_spring_2023_day4:
* Name:	No header for quest qe_yaot_spring_2023_day4
* Description:	No description for quest qe_yaot_spring_2023_day4
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

### qe_yaot_spring_2023_day5:
* Name:	No header for quest qe_yaot_spring_2023_day5
* Description:	No description for quest qe_yaot_spring_2023_day5
* Type:	Event
* EventId:	event_season_yaoSpr_2023
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 3

### qe_yaot_spring_2023_day6:
* Name:	No header for quest qe_yaot_spring_2023_day6
* Description:	No description for quest qe_yaot_spring_2023_day6
* Type:	Event
* EventId:	event_season_yaoSpr_2023
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Mode: Generated

### qe_yaot_spring_2023_day7:
* Name:	No header for quest qe_yaot_spring_2023_day7
* Description:	No description for quest qe_yaot_spring_2023_day7
* Type:	Event
* EventId:	event_season_yaoSpr_2023
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: Mined
			* Amount: 750

### qe_yaot_spring_2023_day8:
* Name:	No header for quest qe_yaot_spring_2023_day8
* Description:	No description for quest qe_yaot_spring_2023_day8
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

### qe_yaot_spring_2023_day9:
* Name:	No header for quest qe_yaot_spring_2023_day9
* Description:	No description for quest qe_yaot_spring_2023_day9
* Type:	Event
* EventId:	event_season_yaoSpr_2023
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Refining
			* Amount: 500

### qe_yaot_spring_2023_day10:
* Name:	No header for quest qe_yaot_spring_2023_day10
* Description:	No description for quest qe_yaot_spring_2023_day10
* Type:	Event
* EventId:	event_season_yaoSpr_2023
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Mode: Generated

### qe_yaot_spring_2023_day11:
* Name:	No header for quest qe_yaot_spring_2023_day11
* Description:	No description for quest qe_yaot_spring_2023_day11
* Type:	Event
* EventId:	event_season_yaoSpr_2023
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: Mined
			* Amount: 750

### qe_yaot_spring_2023_day12:
* Name:	No header for quest qe_yaot_spring_2023_day12
* Description:	No description for quest qe_yaot_spring_2023_day12
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

### qe_yaot_spring_2023_day13:
* Name:	No header for quest qe_yaot_spring_2023_day13
* Description:	No description for quest qe_yaot_spring_2023_day13
* Type:	Event
* EventId:	event_season_yaoSpr_2023
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 3

### qe_yaot_spring_2023_day14:
* Name:	No header for quest qe_yaot_spring_2023_day14
* Description:	No description for quest qe_yaot_spring_2023_day14
* Type:	Event
* EventId:	event_season_yaoSpr_2023
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: story_C01_Tanochet_event_heroic

## QL_EVENT_AMASUM_2023_T1
### qe_amaSum_2023_day1_t1:
* Name:	No header for quest qe_amaSum_2023_day1_t1
* Description:	No description for quest qe_amaSum_2023_day1_t1
* Type:	Event
* EventId:	event_season_amaSum_2023_t1
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Refining
			* Tags: Asteroid_Refined_T1up
			* Amount: 350

### qe_amaSum_2023_day2_t1:
* Name:	No header for quest qe_amaSum_2023_day2_t1
* Description:	No description for quest qe_amaSum_2023_day2_t1
* Type:	Event
* EventId:	event_season_amaSum_2023_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T1up
			* Mode: Generated

### qe_amaSum_2023_day3_t1:
* Name:	No header for quest qe_amaSum_2023_day3_t1
* Description:	No description for quest qe_amaSum_2023_day3_t1
* Type:	Event
* EventId:	event_season_amaSum_2023_t1
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 3

### qe_amaSum_2023_day4_t1:
* Name:	No header for quest qe_amaSum_2023_day4_t1
* Description:	No description for quest qe_amaSum_2023_day4_t1
* Type:	Event
* EventId:	event_season_amaSum_2023_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T1up
			* Mode: Generated

### qe_amaSum_2023_day5_t1:
* Name:	No header for quest qe_amaSum_2023_day5_t1
* Description:	No description for quest qe_amaSum_2023_day5_t1
* Type:	Event
* EventId:	event_season_amaSum_2023_t1
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Refining
			* Tags: Asteroid_Refined_T1up
			* Amount: 350

### qe_amaSum_2023_day6_t1:
* Name:	No header for quest qe_amaSum_2023_day6_t1
* Description:	No description for quest qe_amaSum_2023_day6_t1
* Type:	Event
* EventId:	event_season_amaSum_2023_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T1up
			* Mode: Generated

### qe_amaSum_2023_day7_t1:
* Name:	No header for quest qe_amaSum_2023_day7_t1
* Description:	No description for quest qe_amaSum_2023_day7_t1
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

### qe_amaSum_2023_day8_t1:
* Name:	No header for quest qe_amaSum_2023_day8_t1
* Description:	No description for quest qe_amaSum_2023_day8_t1
* Type:	Event
* EventId:	event_season_amaSum_2023_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T1up
			* Mode: Generated

### qe_amaSum_2023_day9_t1:
* Name:	No header for quest qe_amaSum_2023_day9_t1
* Description:	No description for quest qe_amaSum_2023_day9_t1
* Type:	Event
* EventId:	event_season_amaSum_2023_t1
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Refining
			* Tags: Asteroid_Refined_T1up
			* Amount: 350

### qe_amaSum_2023_day10_t1:
* Name:	No header for quest qe_amaSum_2023_day10_t1
* Description:	No description for quest qe_amaSum_2023_day10_t1
* Type:	Event
* EventId:	event_season_amaSum_2023_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T1up
			* Mode: Generated

### qe_amaSum_2023_day11_t1:
* Name:	No header for quest qe_amaSum_2023_day11_t1
* Description:	No description for quest qe_amaSum_2023_day11_t1
* Type:	Event
* EventId:	event_season_amaSum_2023_t1
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 3

### qe_amaSum_2023_day12_t1:
* Name:	No header for quest qe_amaSum_2023_day12_t1
* Description:	No description for quest qe_amaSum_2023_day12_t1
* Type:	Event
* EventId:	event_season_amaSum_2023_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T1up
			* Mode: Generated

### qe_amaSum_2023_day13_t1:
* Name:	No header for quest qe_amaSum_2023_day13_t1
* Description:	No description for quest qe_amaSum_2023_day13_t1
* Type:	Event
* EventId:	event_season_amaSum_2023_t1
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Refining
			* Tags: Asteroid_Refined_T1up
			* Amount: 350

### qe_amaSum_2023_day14_t1:
* Name:	No header for quest qe_amaSum_2023_day14_t1
* Description:	No description for quest qe_amaSum_2023_day14_t1
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

### qe_amaSum_2023_day15_t1:
* Name:	No header for quest qe_amaSum_2023_day15_t1
* Description:	No description for quest qe_amaSum_2023_day15_t1
* Type:	Event
* EventId:	event_season_amaSum_2023_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_01_StationDefense

## QL_EVENT_AMASUM_2023_T2
### qe_amaSum_2023_day1_t2:
* Name:	No header for quest qe_amaSum_2023_day1_t2
* Description:	No description for quest qe_amaSum_2023_day1_t2
* Type:	Event
* EventId:	event_season_amaSum_2023_t2
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Refining
			* Tags: Asteroid_Refined_T2up
			* Amount: 400

### qe_amaSum_2023_day2_t2:
* Name:	No header for quest qe_amaSum_2023_day2_t2
* Description:	No description for quest qe_amaSum_2023_day2_t2
* Type:	Event
* EventId:	event_season_amaSum_2023_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T2up
			* Mode: Generated

### qe_amaSum_2023_day3_t2:
* Name:	No header for quest qe_amaSum_2023_day3_t2
* Description:	No description for quest qe_amaSum_2023_day3_t2
* Type:	Event
* EventId:	event_season_amaSum_2023_t2
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 3

### qe_amaSum_2023_day4_t2:
* Name:	No header for quest qe_amaSum_2023_day4_t2
* Description:	No description for quest qe_amaSum_2023_day4_t2
* Type:	Event
* EventId:	event_season_amaSum_2023_t2
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: Faction_T2up

### qe_amaSum_2023_day5_t2:
* Name:	No header for quest qe_amaSum_2023_day5_t2
* Description:	No description for quest qe_amaSum_2023_day5_t2
* Type:	Event
* EventId:	event_season_amaSum_2023_t2
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Refining
			* Tags: Asteroid_Refined_T2up
			* Amount: 400

### qe_amaSum_2023_day6_t2:
* Name:	No header for quest qe_amaSum_2023_day6_t2
* Description:	No description for quest qe_amaSum_2023_day6_t2
* Type:	Event
* EventId:	event_season_amaSum_2023_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T2up
			* Mode: Generated

### qe_amaSum_2023_day7_t2:
* Name:	No header for quest qe_amaSum_2023_day7_t2
* Description:	No description for quest qe_amaSum_2023_day7_t2
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

### qe_amaSum_2023_day8_t2:
* Name:	No header for quest qe_amaSum_2023_day8_t2
* Description:	No description for quest qe_amaSum_2023_day8_t2
* Type:	Event
* EventId:	event_season_amaSum_2023_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Mode: Strike
			* Tags: T1up

### qe_amaSum_2023_day9_t2:
* Name:	No header for quest qe_amaSum_2023_day9_t2
* Description:	No description for quest qe_amaSum_2023_day9_t2
* Type:	Event
* EventId:	event_season_amaSum_2023_t2
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Refining
			* Tags: Asteroid_Refined_T2up
			* Amount: 400

### qe_amaSum_2023_day10_t2:
* Name:	No header for quest qe_amaSum_2023_day10_t2
* Description:	No description for quest qe_amaSum_2023_day10_t2
* Type:	Event
* EventId:	event_season_amaSum_2023_t2
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: Faction_T2up

### qe_amaSum_2023_day11_t2:
* Name:	No header for quest qe_amaSum_2023_day11_t2
* Description:	No description for quest qe_amaSum_2023_day11_t2
* Type:	Event
* EventId:	event_season_amaSum_2023_t2
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 3

### qe_amaSum_2023_day12_t2:
* Name:	No header for quest qe_amaSum_2023_day12_t2
* Description:	No description for quest qe_amaSum_2023_day12_t2
* Type:	Event
* EventId:	event_season_amaSum_2023_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Mode: Strike
			* Tags: T1up

### qe_amaSum_2023_day13_t2:
* Name:	No header for quest qe_amaSum_2023_day13_t2
* Description:	No description for quest qe_amaSum_2023_day13_t2
* Type:	Event
* EventId:	event_season_amaSum_2023_t2
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Refining
			* Tags: Asteroid_Refined_T2up
			* Amount: 400

### qe_amaSum_2023_day14_t2:
* Name:	No header for quest qe_amaSum_2023_day14_t2
* Description:	No description for quest qe_amaSum_2023_day14_t2
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

### qe_amaSum_2023_day15_t2:
* Name:	No header for quest qe_amaSum_2023_day15_t2
* Description:	No description for quest qe_amaSum_2023_day15_t2
* Type:	Event
* EventId:	event_season_amaSum_2023_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_02_StationDefense

## QL_EVENT_AMASUM_2023_T3
### qe_amaSum_2023_day1_t3:
* Name:	No header for quest qe_amaSum_2023_day1_t3
* Description:	No description for quest qe_amaSum_2023_day1_t3
* Type:	Event
* EventId:	event_season_amaSum_2023_t3
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Refining
			* Tags: Asteroid_Refined_T3up
			* Amount: 450

### qe_amaSum_2023_day2_t3:
* Name:	No header for quest qe_amaSum_2023_day2_t3
* Description:	No description for quest qe_amaSum_2023_day2_t3
* Type:	Event
* EventId:	event_season_amaSum_2023_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T3up
			* Mode: Generated

### qe_amaSum_2023_day3_t3:
* Name:	No header for quest qe_amaSum_2023_day3_t3
* Description:	No description for quest qe_amaSum_2023_day3_t3
* Type:	Event
* EventId:	event_season_amaSum_2023_t3
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 3

### qe_amaSum_2023_day4_t3:
* Name:	No header for quest qe_amaSum_2023_day4_t3
* Description:	No description for quest qe_amaSum_2023_day4_t3
* Type:	Event
* EventId:	event_season_amaSum_2023_t3
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: Faction_T3up

### qe_amaSum_2023_day5_t3:
* Name:	No header for quest qe_amaSum_2023_day5_t3
* Description:	No description for quest qe_amaSum_2023_day5_t3
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

### qe_amaSum_2023_day6_t3:
* Name:	No header for quest qe_amaSum_2023_day6_t3
* Description:	No description for quest qe_amaSum_2023_day6_t3
* Type:	Event
* EventId:	event_season_amaSum_2023_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T3up
			* Mode: Generated

### qe_amaSum_2023_day7_t3:
* Name:	No header for quest qe_amaSum_2023_day7_t3
* Description:	No description for quest qe_amaSum_2023_day7_t3
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

### qe_amaSum_2023_day8_t3:
* Name:	No header for quest qe_amaSum_2023_day8_t3
* Description:	No description for quest qe_amaSum_2023_day8_t3
* Type:	Event
* EventId:	event_season_amaSum_2023_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Mode: Strike
			* Tags: T2up

### qe_amaSum_2023_day9_t3:
* Name:	No header for quest qe_amaSum_2023_day9_t3
* Description:	No description for quest qe_amaSum_2023_day9_t3
* Type:	Event
* EventId:	event_season_amaSum_2023_t3
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Refining
			* Tags: Asteroid_Refined_T3up
			* Amount: 450

### qe_amaSum_2023_day10_t3:
* Name:	No header for quest qe_amaSum_2023_day10_t3
* Description:	No description for quest qe_amaSum_2023_day10_t3
* Type:	Event
* EventId:	event_season_amaSum_2023_t3
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: Faction_T3up

### qe_amaSum_2023_day11_t3:
* Name:	No header for quest qe_amaSum_2023_day11_t3
* Description:	No description for quest qe_amaSum_2023_day11_t3
* Type:	Event
* EventId:	event_season_amaSum_2023_t3
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 3

### qe_amaSum_2023_day12_t3:
* Name:	No header for quest qe_amaSum_2023_day12_t3
* Description:	No description for quest qe_amaSum_2023_day12_t3
* Type:	Event
* EventId:	event_season_amaSum_2023_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Mode: Strike
			* Tags: T2up

### qe_amaSum_2023_day13_t3:
* Name:	No header for quest qe_amaSum_2023_day13_t3
* Description:	No description for quest qe_amaSum_2023_day13_t3
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

### qe_amaSum_2023_day14_t3:
* Name:	No header for quest qe_amaSum_2023_day14_t3
* Description:	No description for quest qe_amaSum_2023_day14_t3
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

### qe_amaSum_2023_day15_t3:
* Name:	No header for quest qe_amaSum_2023_day15_t3
* Description:	No description for quest qe_amaSum_2023_day15_t3
* Type:	Event
* EventId:	event_season_amaSum_2023_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_03_StationDefense

## QL_EVENT_AMASUM_2023_T4
### qe_amaSum_2023_day1_t4:
* Name:	No header for quest qe_amaSum_2023_day1_t4
* Description:	No description for quest qe_amaSum_2023_day1_t4
* Type:	Event
* EventId:	event_season_amaSum_2023_t4
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Refining
			* Tags: Asteroid_Refined_T4up
			* Amount: 500

### qe_amaSum_2023_day2_t4:
* Name:	No header for quest qe_amaSum_2023_day2_t4
* Description:	No description for quest qe_amaSum_2023_day2_t4
* Type:	Event
* EventId:	event_season_amaSum_2023_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T4up
			* Mode: Generated

### qe_amaSum_2023_day3_t4:
* Name:	No header for quest qe_amaSum_2023_day3_t4
* Description:	No description for quest qe_amaSum_2023_day3_t4
* Type:	Event
* EventId:	event_season_amaSum_2023_t4
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 3

### qe_amaSum_2023_day4_t4:
* Name:	No header for quest qe_amaSum_2023_day4_t4
* Description:	No description for quest qe_amaSum_2023_day4_t4
* Type:	Event
* EventId:	event_season_amaSum_2023_t4
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: Faction_Amassari_T4up

### qe_amaSum_2023_day5_t4:
* Name:	No header for quest qe_amaSum_2023_day5_t4
* Description:	No description for quest qe_amaSum_2023_day5_t4
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

### qe_amaSum_2023_day6_t4:
* Name:	No header for quest qe_amaSum_2023_day6_t4
* Description:	No description for quest qe_amaSum_2023_day6_t4
* Type:	Event
* EventId:	event_season_amaSum_2023_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T4up
			* Mode: Generated

### qe_amaSum_2023_day7_t4:
* Name:	No header for quest qe_amaSum_2023_day7_t4
* Description:	No description for quest qe_amaSum_2023_day7_t4
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

### qe_amaSum_2023_day8_t4:
* Name:	No header for quest qe_amaSum_2023_day8_t4
* Description:	No description for quest qe_amaSum_2023_day8_t4
* Type:	Event
* EventId:	event_season_amaSum_2023_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 5
			* Mode: Strike
			* Tags: T3up

### qe_amaSum_2023_day9_t4:
* Name:	No header for quest qe_amaSum_2023_day9_t4
* Description:	No description for quest qe_amaSum_2023_day9_t4
* Type:	Event
* EventId:	event_season_amaSum_2023_t4
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Refining
			* Tags: Asteroid_Refined_T4up
			* Amount: 500

### qe_amaSum_2023_day10_t4:
* Name:	No header for quest qe_amaSum_2023_day10_t4
* Description:	No description for quest qe_amaSum_2023_day10_t4
* Type:	Event
* EventId:	event_season_amaSum_2023_t4
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: Faction_Amassari_T4up

### qe_amaSum_2023_day11_t4:
* Name:	No header for quest qe_amaSum_2023_day11_t4
* Description:	No description for quest qe_amaSum_2023_day11_t4
* Type:	Event
* EventId:	event_season_amaSum_2023_t4
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 3

### qe_amaSum_2023_day12_t4:
* Name:	No header for quest qe_amaSum_2023_day12_t4
* Description:	No description for quest qe_amaSum_2023_day12_t4
* Type:	Event
* EventId:	event_season_amaSum_2023_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 5
			* Mode: Strike
			* Tags: T3up

### qe_amaSum_2023_day13_t4:
* Name:	No header for quest qe_amaSum_2023_day13_t4
* Description:	No description for quest qe_amaSum_2023_day13_t4
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

### qe_amaSum_2023_day14_t4:
* Name:	No header for quest qe_amaSum_2023_day14_t4
* Description:	No description for quest qe_amaSum_2023_day14_t4
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

### qe_amaSum_2023_day15_t4:
* Name:	No header for quest qe_amaSum_2023_day15_t4
* Description:	No description for quest qe_amaSum_2023_day15_t4
* Type:	Event
* EventId:	event_season_amaSum_2023_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_04_StationDefense

## QL_7DAYS_MAR_2024_DAY1_T1
### qe_7days_mar_2024_day1_a_t1:
* Name:	Day 1: Lay of the Land
* Description:	Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t1
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_T1up
			* Amount: 10
			* Analyzed: True

### qe_7days_mar_2024_day1_b_t1:
* Name:	The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Description:	The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
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

### qe_7days_mar_2024_day1_c_t1:
* Name:	Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.
* Description:	Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.
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

### qe_7days_mar_2024_day1_d_t1:
* Name:	Rare earths are an occasional by-product of refining. They are required for upgrading modules.
* Description:	Rare earths are an occasional by-product of refining. They are required for upgrading modules.
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
### qe_7days_mar_2024_day1_a_t2:
* Name:	Day 1: Lay of the Land
* Description:	Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t2
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_T2up
			* Amount: 10
			* Analyzed: True

### qe_7days_mar_2024_day1_b_t2:
* Name:	The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Description:	The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
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

### qe_7days_mar_2024_day1_c_t2:
* Name:	Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.
* Description:	Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.
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

### qe_7days_mar_2024_day1_d_t2:
* Name:	Rare earths are an occasional by-product of refining. They are required for upgrading modules.
* Description:	Rare earths are an occasional by-product of refining. They are required for upgrading modules.
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
### qe_7days_mar_2024_day1_a_t3:
* Name:	Day 1: Lay of the Land
* Description:	Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t3
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_T3up
			* Amount: 10
			* Analyzed: True

### qe_7days_mar_2024_day1_b_t3:
* Name:	The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Description:	The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t3
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedT3
				* ShipsDestroyedT4
			* Amount: 15

### qe_7days_mar_2024_day1_c_t3:
* Name:	Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.
* Description:	Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.
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

### qe_7days_mar_2024_day1_d_t3:
* Name:	Rare earths are an occasional by-product of refining. They are required for upgrading modules.
* Description:	Rare earths are an occasional by-product of refining. They are required for upgrading modules.
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
### qe_7days_mar_2024_day1_a_t4:
* Name:	Day 1: Lay of the Land
* Description:	Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t4
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_T4up
			* Amount: 10
			* Analyzed: True

### qe_7days_mar_2024_day1_b_t4:
* Name:	The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Description:	The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t4
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedT4
			* Amount: 15

### qe_7days_mar_2024_day1_c_t4:
* Name:	Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.
* Description:	Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.
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

### qe_7days_mar_2024_day1_d_t4:
* Name:	Rare earths are an occasional by-product of refining. They are required for upgrading modules.
* Description:	Rare earths are an occasional by-product of refining. They are required for upgrading modules.
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
### qe_7days_mar_2024_day2_a_t1:
* Name:	Day 2: Meet & Greet
* Description:	There are different types of assignments available in your assignment log.
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t1
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: T1up

### qe_7days_mar_2024_day2_b_t1:
* Name:	Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.
* Description:	During missions you will usually fight against enemy ships. They can be part of an assignment, or they can be found as signals through scanning.
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T1up

### qe_7days_mar_2024_day2_c_t1:
* Name:	Complete liaison assignments to gain reputation for that faction. A higher reputation unlocks more items in that faction's liaison requisitions office.
* Description:	Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.
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

### qe_7days_mar_2024_day2_d_t1:
* Name:	Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* Description:	Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t1
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 1

## QL_7DAYS_MAR_2024_DAY2_T2
### qe_7days_mar_2024_day2_a_t2:
* Name:	Day 2: Meet & Greet
* Description:	Completing liaison assignments for a faction increases your reputation level for that faction. Higher reputation levels unlock additional items in that faction's liaison requisitions office.
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t2
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: Faction_T2up

### qe_7days_mar_2024_day2_b_t2:
* Name:	Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.
* Description:	Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Mode: Faction
			* Tags: T2up

### qe_7days_mar_2024_day2_c_t2:
* Name:	Complete liaison assignments to gain reputation for that faction. A higher reputation unlocks more items in that faction's liaison requisitions office.
* Description:	Complete liaison assignments to gain reputation for that faction. A higher reputation unlocks more items in that faction's liaison requisitions office.
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

### qe_7days_mar_2024_day2_d_t2:
* Name:	Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* Description:	Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t2
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 2

## QL_7DAYS_MAR_2024_DAY2_T3
### qe_7days_mar_2024_day2_a_t3:
* Name:	Day 2: Meet & Greet
* Description:	Completing liaison assignments for a faction increases your reputation level for that faction. Higher reputation levels unlock additional items in that faction's liaison requisitions office.
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t3
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: Faction_T3up

### qe_7days_mar_2024_day2_b_t3:
* Name:	Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.
* Description:	Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Mode: Faction
			* Tags: T3up

### qe_7days_mar_2024_day2_c_t3:
* Name:	Complete liaison assignments to gain reputation for that faction. A higher reputation unlocks more items in that faction's liaison requisitions office.
* Description:	Complete liaison assignments to gain reputation for that faction. A higher reputation unlocks more items in that faction's liaison requisitions office.
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

### qe_7days_mar_2024_day2_d_t3:
* Name:	Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* Description:	Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t3
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 3

## QL_7DAYS_MAR_2024_DAY2_T4
### qe_7days_mar_2024_day2_a_t4:
* Name:	Day 2: Meet & Greet
* Description:	Completing liaison assignments for a faction increases your reputation level for that faction. Higher reputation levels unlock additional items in that faction's liaison requisitions office.
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t4
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: Faction_T4up

### qe_7days_mar_2024_day2_b_t4:
* Name:	Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.
* Description:	Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Mode: Faction
			* Tags: T4up

### qe_7days_mar_2024_day2_c_t4:
* Name:	Complete liaison assignments to gain reputation for that faction. A higher reputation unlocks more items in that faction's liaison requisitions office.
* Description:	Complete liaison assignments to gain reputation for that faction. A higher reputation unlocks more items in that faction's liaison requisitions office.
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

### qe_7days_mar_2024_day2_d_t4:
* Name:	Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* Description:	Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t4
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 5

## QL_7DAYS_MAR_2024_DAY3_T1
### qe_7days_mar_2024_day3_a_t1:
* Name:	Day 3: Raw Materials
* Description:	Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.
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

### qe_7days_mar_2024_day3_b_t1:
* Name:	Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.
* Description:	Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t1
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Refining
			* Tags: Asteroid_Refined_T1up
			* Amount: 500

### qe_7days_mar_2024_day3_c_t1:
* Name:	Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.
* Description:	Small items such as strike craft, modules and parts can be built in the fabricator. Larger items such as escort ships and flagships must be constructed at shipyards provided at larger stations.
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t1
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: T1up
			* Amount: 1

### qe_7days_mar_2024_day3_d_t1:
* Name:	Items and resources can be sold for credits in the market at stations.
* Description:	Items and resources can be sold for credits in the market at stations.
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
### qe_7days_mar_2024_day3_a_t2:
* Name:	Day 3: Raw Materials
* Description:	Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.
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

### qe_7days_mar_2024_day3_b_t2:
* Name:	Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.
* Description:	Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t2
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Refining
			* Tags: Asteroid_Refined_T2up
			* Amount: 500

### qe_7days_mar_2024_day3_c_t2:
* Name:	Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.
* Description:	Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t2
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: Part_T2up
			* Amount: 25

### qe_7days_mar_2024_day3_d_t2:
* Name:	Items and resources can be sold for credits in the market at stations.
* Description:	Items and resources can be sold for credits in the market at stations.
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
### qe_7days_mar_2024_day3_a_t3:
* Name:	Day 3: Raw Materials
* Description:	Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.
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

### qe_7days_mar_2024_day3_b_t3:
* Name:	Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.
* Description:	Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t3
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Refining
			* Tags: Asteroid_Refined_T3up
			* Amount: 500

### qe_7days_mar_2024_day3_c_t3:
* Name:	Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.
* Description:	Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t3
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: Part_T3up
			* Amount: 25

### qe_7days_mar_2024_day3_d_t3:
* Name:	Items and resources can be sold for credits in the market at stations.
* Description:	Items and resources can be sold for credits in the market at stations.
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
### qe_7days_mar_2024_day3_a_t4:
* Name:	Day 3: Raw Materials
* Description:	Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.
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

### qe_7days_mar_2024_day3_b_t4:
* Name:	Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.
* Description:	Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t4
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Refining
			* Tags: Asteroid_Refined_T4up
			* Amount: 500

### qe_7days_mar_2024_day3_c_t4:
* Name:	Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.
* Description:	Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t4
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: Part_T4up
			* Amount: 25

### qe_7days_mar_2024_day3_d_t4:
* Name:	Items and resources can be sold for credits in the market at stations.
* Description:	Items and resources can be sold for credits in the market at stations.
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
### qe_7days_mar_2024_day4_a_t1:
* Name:	Day 4: Hypothesis
* Description:	Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T1up
			* Mode: Generated

### qe_7days_mar_2024_day4_b_t1:
* Name:	Progenitor relics can be found in relic signature signals. Relics can be sold on the market for credits, though some liaison offices may be interested in relics as well.
* Description:	Progenitor relics can be found in relic signature signals. Relics can be sold on the market for credits, though some liaison offices may be interested in relics as well.
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

### qe_7days_mar_2024_day4_c_t1:
* Name:	Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.
* Description:	Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.
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

### qe_7days_mar_2024_day4_d_t1:
* Name:	Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.
* Description:	Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Rare_T1up
			* Mode: Generated

## QL_7DAYS_MAR_2024_DAY4_T2
### qe_7days_mar_2024_day4_a_t2:
* Name:	Day 4: Hypothesis
* Description:	Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.
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

### qe_7days_mar_2024_day4_b_t2:
* Name:	Progenitor relics can be found in relic signature signals. Relics can be sold on the market for credits, though some liaison offices may be interested in relics as well.
* Description:	Progenitor relics can be found in relic signature signals. Relics can be sold on the market for credits, though some liaison offices may be interested in relics as well.
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

### qe_7days_mar_2024_day4_c_t2:
* Name:	Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.
* Description:	Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.
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

### qe_7days_mar_2024_day4_d_t2:
* Name:	Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.
* Description:	Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Epic_T2up
			* Mode: Generated

## QL_7DAYS_MAR_2024_DAY4_T3
### qe_7days_mar_2024_day4_a_t3:
* Name:	Day 4: Hypothesis
* Description:	Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.
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

### qe_7days_mar_2024_day4_b_t3:
* Name:	Progenitor relics can be found in relic signature signals. Relics can be sold on the market for credits, though some liaison offices may be interested in relics as well.
* Description:	Progenitor relics can be found in relic signature signals. Relics can be sold on the market for credits, though some liaison offices may be interested in relics as well.
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

### qe_7days_mar_2024_day4_c_t3:
* Name:	Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.
* Description:	Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t3
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedProgenitorT3
				* ShipsDestroyedProgenitorT4
			* Amount: 7

### qe_7days_mar_2024_day4_d_t3:
* Name:	Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.
* Description:	Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Epic_T3up
			* Mode: Generated

## QL_7DAYS_MAR_2024_DAY4_T4
### qe_7days_mar_2024_day4_a_t4:
* Name:	Day 4: Hypothesis
* Description:	Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.
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

### qe_7days_mar_2024_day4_b_t4:
* Name:	Progenitor relics can be found in relic signature signals. Relics can be sold on the market for credits, though some liaison offices may be interested in relics as well.
* Description:	Progenitor relics can be found in relic signature signals. Relics can be sold on the market for credits, though some liaison offices may be interested in relics as well.
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

### qe_7days_mar_2024_day4_c_t4:
* Name:	Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.
* Description:	Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.
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

### qe_7days_mar_2024_day4_d_t4:
* Name:	Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.
* Description:	Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Epic_T4up
			* Mode: Generated

## QL_7DAYS_MAR_2024_DAY5_T1
### qe_7days_mar_2024_day5_a_t1:
* Name:	Day 5: Lessons
* Description:	Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T1up
			* Mode: Generated

### qe_7days_mar_2024_day5_b_t1:
* Name:	Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.
* Description:	Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.
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

### qe_7days_mar_2024_day5_c_t1:
* Name:	Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* Description:	Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t1
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 1

### qe_7days_mar_2024_day5_d_t1:
* Name:	Discharging officers grants credits and insignias, which can be used to level up other officers.
* Description:	Discharging officers grants credits and insignias, which can be used to level up other officers.
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
### qe_7days_mar_2024_day5_a_t2:
* Name:	Day 5: Lessons
* Description:	Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T2up
			* Mode: Generated

### qe_7days_mar_2024_day5_b_t2:
* Name:	Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.
* Description:	Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.
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

### qe_7days_mar_2024_day5_c_t2:
* Name:	Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* Description:	Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t2
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 2

### qe_7days_mar_2024_day5_d_t2:
* Name:	Discharging officers grants credits and insignias, which can be used to level up other officers.
* Description:	Discharging officers grants credits and insignias, which can be used to level up other officers.
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
### qe_7days_mar_2024_day5_a_t3:
* Name:	Day 5: Lessons
* Description:	Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T3up
			* Mode: Generated

### qe_7days_mar_2024_day5_b_t3:
* Name:	Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.
* Description:	Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.
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

### qe_7days_mar_2024_day5_c_t3:
* Name:	Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* Description:	Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t3
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 3

### qe_7days_mar_2024_day5_d_t3:
* Name:	Discharging officers grants credits and insignias, which can be used to level up other officers.
* Description:	Discharging officers grants credits and insignias, which can be used to level up other officers.
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
### qe_7days_mar_2024_day5_a_t4:
* Name:	Day 5: Lessons
* Description:	Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T4up
			* Mode: Generated

### qe_7days_mar_2024_day5_b_t4:
* Name:	Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.
* Description:	Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.
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

### qe_7days_mar_2024_day5_c_t4:
* Name:	Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* Description:	Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t4
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 5

### qe_7days_mar_2024_day5_d_t4:
* Name:	Discharging officers grants credits and insignias, which can be used to level up other officers.
* Description:	Discharging officers grants credits and insignias, which can be used to level up other officers.
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
### qe_7days_mar_2024_day6_a_t1:
* Name:	Day 6: Stockpile
* Description:	Rare earths are an occasional by-product of refining. They are required for upgrading modules.
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

### qe_7days_mar_2024_day6_b_t1:
* Name:	The strength of modules can be increased through upgrades, which cost rare earths.
* Description:	Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t1
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 1

### qe_7days_mar_2024_day6_c_t1:
* Name:	The strength of modules can be increased through upgrades, which cost rare earths.
* Description:	Small items such as strike craft, modules and parts can be built in the fabricator. Larger items such as escort ships and flagships must be constructed at shipyards provided at larger stations.
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t1
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: T1up
			* Amount: 1

### qe_7days_mar_2024_day6_d_t1:
* Name:	The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Description:	The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
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
### qe_7days_mar_2024_day6_a_t2:
* Name:	Day 6: Stockpile
* Description:	Rare earths are an occasional by-product of refining. They are required for upgrading modules.
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

### qe_7days_mar_2024_day6_b_t2:
* Name:	The strength of modules can be increased through upgrades, which cost rare earths.
* Description:	The strength of modules can be increased through upgrades, which cost rare earths.
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t2
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Upgrade
			* Tags: External_Module_T1up
			* Amount: 1

### qe_7days_mar_2024_day6_c_t2:
* Name:	The strength of modules can be increased through upgrades, which cost rare earths.
* Description:	Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t2
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: Part_T2up
			* Amount: 25

### qe_7days_mar_2024_day6_d_t2:
* Name:	The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Description:	The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
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
### qe_7days_mar_2024_day6_a_t3:
* Name:	Day 6: Stockpile
* Description:	Rare earths are an occasional by-product of refining. They are required for upgrading modules.
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

### qe_7days_mar_2024_day6_b_t3:
* Name:	The strength of modules can be increased through upgrades, which cost rare earths.
* Description:	The strength of modules can be increased through upgrades, which cost rare earths.
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t3
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Upgrade
			* Tags: External_Module_T2up
			* Amount: 1

### qe_7days_mar_2024_day6_c_t3:
* Name:	The strength of modules can be increased through upgrades, which cost rare earths.
* Description:	The strength of modules can be increased through upgrades, which cost rare earths.
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t3
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Upgrade
			* Tags: Internal_Module_T2up
			* Amount: 1

### qe_7days_mar_2024_day6_d_t3:
* Name:	The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Description:	The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
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
### qe_7days_mar_2024_day6_a_t4:
* Name:	Day 6: Stockpile
* Description:	Rare earths are an occasional by-product of refining. They are required for upgrading modules.
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

### qe_7days_mar_2024_day6_b_t4:
* Name:	The strength of modules can be increased through upgrades, which cost rare earths.
* Description:	The strength of modules can be increased through upgrades, which cost rare earths.
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t4
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Upgrade
			* Tags: External_Module_T3up
			* Amount: 1

### qe_7days_mar_2024_day6_c_t4:
* Name:	The strength of modules can be increased through upgrades, which cost rare earths.
* Description:	The strength of modules can be increased through upgrades, which cost rare earths.
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t4
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Upgrade
			* Tags: Internal_Module_T3up
			* Amount: 1

### qe_7days_mar_2024_day6_d_t4:
* Name:	The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Description:	The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t4
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedT4
			* Amount: 15

## QL_7DAYS_MAR_2024_DAY7_T1
### qe_7days_mar_2024_day7_a_t1:
* Name:	Day 7: Enemy Contact
* Description:	Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T1up
			* Mode: Generated

### qe_7days_mar_2024_day7_b_t1:
* Name:	The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Description:	The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
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

### qe_7days_mar_2024_day7_c_t1:
* Name:	When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.
* Description:	When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.
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

### qe_7days_mar_2024_day7_d_t1:
* Name:	Strikes are difficult missions that require a strong fleet from several commanders to beat. Completing a strike rewards code fragments, which can be turned in for special blueprints.
* Description:	Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T1up
			* Mode: Generated

## QL_7DAYS_MAR_2024_DAY7_T2
### qe_7days_mar_2024_day7_a_t2:
* Name:	Day 7: Enemy Contact
* Description:	Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T2up
			* Mode: Generated

### qe_7days_mar_2024_day7_b_t2:
* Name:	The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Description:	The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
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

### qe_7days_mar_2024_day7_c_t2:
* Name:	When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.
* Description:	When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.
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

### qe_7days_mar_2024_day7_d_t2:
* Name:	Strikes are difficult missions that require a strong fleet from several commanders to beat. Completing a strike rewards code fragments, which can be turned in for special blueprints.
* Description:	Strikes are difficult missions that require a strong fleet from several commanders to beat. Completing a strike rewards code fragments, which can be turned in for special blueprints.
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Mode: Strike
			* Tags: T1up

## QL_7DAYS_MAR_2024_DAY7_T3
### qe_7days_mar_2024_day7_a_t3:
* Name:	Day 7: Enemy Contact
* Description:	Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T3up
			* Mode: Generated

### qe_7days_mar_2024_day7_b_t3:
* Name:	The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Description:	The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t3
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedT3
				* ShipsDestroyedT4
			* Amount: 15

### qe_7days_mar_2024_day7_c_t3:
* Name:	When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.
* Description:	When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.
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

### qe_7days_mar_2024_day7_d_t3:
* Name:	Strikes are difficult missions that require a strong fleet from several commanders to beat. Completing a strike rewards code fragments, which can be turned in for special blueprints.
* Description:	Strikes are difficult missions that require a strong fleet from several commanders to beat. Completing a strike rewards code fragments, which can be turned in for special blueprints.
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Mode: Strike
			* Tags: T2up

## QL_7DAYS_MAR_2024_DAY7_T4
### qe_7days_mar_2024_day7_a_t4:
* Name:	Day 7: Enemy Contact
* Description:	Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T4up
			* Mode: Generated

### qe_7days_mar_2024_day7_b_t4:
* Name:	The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Description:	The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t4
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedT4
			* Amount: 15

### qe_7days_mar_2024_day7_c_t4:
* Name:	When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.
* Description:	When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.
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

### qe_7days_mar_2024_day7_d_t4:
* Name:	Strikes are difficult missions that require a strong fleet from several commanders to beat. Completing a strike rewards code fragments, which can be turned in for special blueprints.
* Description:	Strikes are difficult missions that require a strong fleet from several commanders to beat. Completing a strike rewards code fragments, which can be turned in for special blueprints.
* Type:	Event
* EventId:	event_monthlyEvent_2024_03_01_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Mode: Strike
			* Tags: T3up

## QL_7DAYS_2023_08_DAY1_T1
### qe_7days_2023_08_day1_a_t1:
* Name:	Day 1: Lay of the Land
* Description:	Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.
* Type:	Event
* EventId:	event_7days_2023_08_21_t1
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_T1up
			* Amount: 10
			* Analyzed: True

### qe_7days_2023_08_day1_b_t1:
* Name:	The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Description:	The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
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

### qe_7days_2023_08_day1_c_t1:
* Name:	Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.
* Description:	Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.
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

### qe_7days_2023_08_day1_d_t1:
* Name:	Rare earths are an occasional by-product of refining. They are required for upgrading modules.
* Description:	Rare earths are an occasional by-product of refining. They are required for upgrading modules.
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
### qe_7days_2023_08_day1_a_t2:
* Name:	Day 1: Lay of the Land
* Description:	Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.
* Type:	Event
* EventId:	event_7days_2023_08_21_t2
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_T2up
			* Amount: 10
			* Analyzed: True

### qe_7days_2023_08_day1_b_t2:
* Name:	The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Description:	The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
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

### qe_7days_2023_08_day1_c_t2:
* Name:	Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.
* Description:	Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.
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

### qe_7days_2023_08_day1_d_t2:
* Name:	Rare earths are an occasional by-product of refining. They are required for upgrading modules.
* Description:	Rare earths are an occasional by-product of refining. They are required for upgrading modules.
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
### qe_7days_2023_08_day1_a_t3:
* Name:	Day 1: Lay of the Land
* Description:	Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.
* Type:	Event
* EventId:	event_7days_2023_08_21_t3
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_T3up
			* Amount: 10
			* Analyzed: True

### qe_7days_2023_08_day1_b_t3:
* Name:	The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Description:	The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Type:	Event
* EventId:	event_7days_2023_08_21_t3
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedT3
				* ShipsDestroyedT4
			* Amount: 15

### qe_7days_2023_08_day1_c_t3:
* Name:	Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.
* Description:	Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.
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

### qe_7days_2023_08_day1_d_t3:
* Name:	Rare earths are an occasional by-product of refining. They are required for upgrading modules.
* Description:	Rare earths are an occasional by-product of refining. They are required for upgrading modules.
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
### qe_7days_2023_08_day1_a_t4:
* Name:	Day 1: Lay of the Land
* Description:	Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.
* Type:	Event
* EventId:	event_7days_2023_08_21_t4
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_T4up
			* Amount: 10
			* Analyzed: True

### qe_7days_2023_08_day1_b_t4:
* Name:	The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Description:	The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Type:	Event
* EventId:	event_7days_2023_08_21_t4
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedT4
			* Amount: 15

### qe_7days_2023_08_day1_c_t4:
* Name:	Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.
* Description:	Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.
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

### qe_7days_2023_08_day1_d_t4:
* Name:	Rare earths are an occasional by-product of refining. They are required for upgrading modules.
* Description:	Rare earths are an occasional by-product of refining. They are required for upgrading modules.
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
### qe_7days_2023_08_day2_a_t1:
* Name:	Day 2: Meet & Greet
* Description:	There are different types of assignments available in your assignment log.
* Type:	Event
* EventId:	event_7days_2023_08_21_t1
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: T1up

### qe_7days_2023_08_day2_b_t1:
* Name:	Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.
* Description:	During missions you will usually fight against enemy ships. They can be part of an assignment, or they can be found as signals through scanning.
* Type:	Event
* EventId:	event_7days_2023_08_21_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T1up

### qe_7days_2023_08_day2_c_t1:
* Name:	Complete liaison assignments to gain reputation for that faction. A higher reputation unlocks more items in that faction's liaison requisitions office.
* Description:	Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.
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

### qe_7days_2023_08_day2_d_t1:
* Name:	Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* Description:	Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* Type:	Event
* EventId:	event_7days_2023_08_21_t1
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 1

## QL_7DAYS_2023_08_DAY2_T2
### qe_7days_2023_08_day2_a_t2:
* Name:	Day 2: Meet & Greet
* Description:	Completing liaison assignments for a faction increases your reputation level for that faction. Higher reputation levels unlock additional items in that faction's liaison requisitions office.
* Type:	Event
* EventId:	event_7days_2023_08_21_t2
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: Faction_T2up

### qe_7days_2023_08_day2_b_t2:
* Name:	Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.
* Description:	Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.
* Type:	Event
* EventId:	event_7days_2023_08_21_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Mode: Faction
			* Tags: T2up

### qe_7days_2023_08_day2_c_t2:
* Name:	Complete liaison assignments to gain reputation for that faction. A higher reputation unlocks more items in that faction's liaison requisitions office.
* Description:	Complete liaison assignments to gain reputation for that faction. A higher reputation unlocks more items in that faction's liaison requisitions office.
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

### qe_7days_2023_08_day2_d_t2:
* Name:	Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* Description:	Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* Type:	Event
* EventId:	event_7days_2023_08_21_t2
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 2

## QL_7DAYS_2023_08_DAY2_T3
### qe_7days_2023_08_day2_a_t3:
* Name:	Day 2: Meet & Greet
* Description:	Completing liaison assignments for a faction increases your reputation level for that faction. Higher reputation levels unlock additional items in that faction's liaison requisitions office.
* Type:	Event
* EventId:	event_7days_2023_08_21_t3
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: Faction_T3up

### qe_7days_2023_08_day2_b_t3:
* Name:	Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.
* Description:	Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.
* Type:	Event
* EventId:	event_7days_2023_08_21_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Mode: Faction
			* Tags: T3up

### qe_7days_2023_08_day2_c_t3:
* Name:	Complete liaison assignments to gain reputation for that faction. A higher reputation unlocks more items in that faction's liaison requisitions office.
* Description:	Complete liaison assignments to gain reputation for that faction. A higher reputation unlocks more items in that faction's liaison requisitions office.
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

### qe_7days_2023_08_day2_d_t3:
* Name:	Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* Description:	Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* Type:	Event
* EventId:	event_7days_2023_08_21_t3
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 3

## QL_7DAYS_2023_08_DAY2_T4
### qe_7days_2023_08_day2_a_t4:
* Name:	Day 2: Meet & Greet
* Description:	Completing liaison assignments for a faction increases your reputation level for that faction. Higher reputation levels unlock additional items in that faction's liaison requisitions office.
* Type:	Event
* EventId:	event_7days_2023_08_21_t4
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: Faction_T4up

### qe_7days_2023_08_day2_b_t4:
* Name:	Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.
* Description:	Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.
* Type:	Event
* EventId:	event_7days_2023_08_21_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Mode: Faction
			* Tags: T4up

### qe_7days_2023_08_day2_c_t4:
* Name:	Complete liaison assignments to gain reputation for that faction. A higher reputation unlocks more items in that faction's liaison requisitions office.
* Description:	Complete liaison assignments to gain reputation for that faction. A higher reputation unlocks more items in that faction's liaison requisitions office.
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

### qe_7days_2023_08_day2_d_t4:
* Name:	Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* Description:	Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* Type:	Event
* EventId:	event_7days_2023_08_21_t4
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 5

## QL_7DAYS_2023_08_DAY3_T1
### qe_7days_2023_08_day3_a_t1:
* Name:	Day 3: Raw Materials
* Description:	Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.
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

### qe_7days_2023_08_day3_b_t1:
* Name:	Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.
* Description:	Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.
* Type:	Event
* EventId:	event_7days_2023_08_21_t1
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Refining
			* Tags: Asteroid_Refined_T1up
			* Amount: 500

### qe_7days_2023_08_day3_c_t1:
* Name:	Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.
* Description:	Small items such as strike craft, modules and parts can be built in the fabricator. Larger items such as escort ships and flagships must be constructed at shipyards provided at larger stations.
* Type:	Event
* EventId:	event_7days_2023_08_21_t1
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: T1up
			* Amount: 1

### qe_7days_2023_08_day3_d_t1:
* Name:	Items and resources can be sold for credits in the market at stations.
* Description:	Items and resources can be sold for credits in the market at stations.
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
### qe_7days_2023_08_day3_a_t2:
* Name:	Day 3: Raw Materials
* Description:	Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.
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

### qe_7days_2023_08_day3_b_t2:
* Name:	Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.
* Description:	Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.
* Type:	Event
* EventId:	event_7days_2023_08_21_t2
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Refining
			* Tags: Asteroid_Refined_T2up
			* Amount: 500

### qe_7days_2023_08_day3_c_t2:
* Name:	Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.
* Description:	Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.
* Type:	Event
* EventId:	event_7days_2023_08_21_t2
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: Part_T2up
			* Amount: 25

### qe_7days_2023_08_day3_d_t2:
* Name:	Items and resources can be sold for credits in the market at stations.
* Description:	Items and resources can be sold for credits in the market at stations.
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
### qe_7days_2023_08_day3_a_t3:
* Name:	Day 3: Raw Materials
* Description:	Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.
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

### qe_7days_2023_08_day3_b_t3:
* Name:	Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.
* Description:	Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.
* Type:	Event
* EventId:	event_7days_2023_08_21_t3
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Refining
			* Tags: Asteroid_Refined_T3up
			* Amount: 500

### qe_7days_2023_08_day3_c_t3:
* Name:	Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.
* Description:	Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.
* Type:	Event
* EventId:	event_7days_2023_08_21_t3
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: Part_T3up
			* Amount: 25

### qe_7days_2023_08_day3_d_t3:
* Name:	Items and resources can be sold for credits in the market at stations.
* Description:	Items and resources can be sold for credits in the market at stations.
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
### qe_7days_2023_08_day3_a_t4:
* Name:	Day 3: Raw Materials
* Description:	Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.
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

### qe_7days_2023_08_day3_b_t4:
* Name:	Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.
* Description:	Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.
* Type:	Event
* EventId:	event_7days_2023_08_21_t4
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Refining
			* Tags: Asteroid_Refined_T4up
			* Amount: 500

### qe_7days_2023_08_day3_c_t4:
* Name:	Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.
* Description:	Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.
* Type:	Event
* EventId:	event_7days_2023_08_21_t4
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: Part_T4up
			* Amount: 25

### qe_7days_2023_08_day3_d_t4:
* Name:	Items and resources can be sold for credits in the market at stations.
* Description:	Items and resources can be sold for credits in the market at stations.
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
### qe_7days_2023_08_day4_a_t1:
* Name:	Day 4: Hypothesis
* Description:	Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
* Type:	Event
* EventId:	event_7days_2023_08_21_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T1up
			* Mode: Generated

### qe_7days_2023_08_day4_b_t1:
* Name:	Progenitor relics can be found in relic signature signals. Relics can be sold on the market for credits, though some liaison offices may be interested in relics as well.
* Description:	Progenitor relics can be found in relic signature signals. Relics can be sold on the market for credits, though some liaison offices may be interested in relics as well.
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

### qe_7days_2023_08_day4_c_t1:
* Name:	Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.
* Description:	Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.
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

### qe_7days_2023_08_day4_d_t1:
* Name:	Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.
* Description:	Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.
* Type:	Event
* EventId:	event_7days_2023_08_21_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Rare_T1up
			* Mode: Generated

## QL_7DAYS_2023_08_DAY4_T2
### qe_7days_2023_08_day4_a_t2:
* Name:	Day 4: Hypothesis
* Description:	Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.
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

### qe_7days_2023_08_day4_b_t2:
* Name:	Progenitor relics can be found in relic signature signals. Relics can be sold on the market for credits, though some liaison offices may be interested in relics as well.
* Description:	Progenitor relics can be found in relic signature signals. Relics can be sold on the market for credits, though some liaison offices may be interested in relics as well.
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

### qe_7days_2023_08_day4_c_t2:
* Name:	Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.
* Description:	Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.
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

### qe_7days_2023_08_day4_d_t2:
* Name:	Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.
* Description:	Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.
* Type:	Event
* EventId:	event_7days_2023_08_21_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Epic_T2up
			* Mode: Generated

## QL_7DAYS_2023_08_DAY4_T3
### qe_7days_2023_08_day4_a_t3:
* Name:	Day 4: Hypothesis
* Description:	Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.
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

### qe_7days_2023_08_day4_b_t3:
* Name:	Progenitor relics can be found in relic signature signals. Relics can be sold on the market for credits, though some liaison offices may be interested in relics as well.
* Description:	Progenitor relics can be found in relic signature signals. Relics can be sold on the market for credits, though some liaison offices may be interested in relics as well.
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

### qe_7days_2023_08_day4_c_t3:
* Name:	Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.
* Description:	Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.
* Type:	Event
* EventId:	event_7days_2023_08_21_t3
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedProgenitorT3
				* ShipsDestroyedProgenitorT4
			* Amount: 7

### qe_7days_2023_08_day4_d_t3:
* Name:	Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.
* Description:	Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.
* Type:	Event
* EventId:	event_7days_2023_08_21_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Epic_T3up
			* Mode: Generated

## QL_7DAYS_2023_08_DAY4_T4
### qe_7days_2023_08_day4_a_t4:
* Name:	Day 4: Hypothesis
* Description:	Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.
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

### qe_7days_2023_08_day4_b_t4:
* Name:	Progenitor relics can be found in relic signature signals. Relics can be sold on the market for credits, though some liaison offices may be interested in relics as well.
* Description:	Progenitor relics can be found in relic signature signals. Relics can be sold on the market for credits, though some liaison offices may be interested in relics as well.
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

### qe_7days_2023_08_day4_c_t4:
* Name:	Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.
* Description:	Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.
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

### qe_7days_2023_08_day4_d_t4:
* Name:	Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.
* Description:	Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.
* Type:	Event
* EventId:	event_7days_2023_08_21_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Epic_T4up
			* Mode: Generated

## QL_7DAYS_2023_08_DAY5_T1
### qe_7days_2023_08_day5_a_t1:
* Name:	Day 5: Lessons
* Description:	Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
* Type:	Event
* EventId:	event_7days_2023_08_21_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T1up
			* Mode: Generated

### qe_7days_2023_08_day5_b_t1:
* Name:	Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.
* Description:	Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.
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

### qe_7days_2023_08_day5_c_t1:
* Name:	Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* Description:	Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* Type:	Event
* EventId:	event_7days_2023_08_21_t1
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 1

### qe_7days_2023_08_day5_d_t1:
* Name:	Discharging officers grants credits and insignias, which can be used to level up other officers.
* Description:	Discharging officers grants credits and insignias, which can be used to level up other officers.
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
### qe_7days_2023_08_day5_a_t2:
* Name:	Day 5: Lessons
* Description:	Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
* Type:	Event
* EventId:	event_7days_2023_08_21_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T2up
			* Mode: Generated

### qe_7days_2023_08_day5_b_t2:
* Name:	Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.
* Description:	Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.
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

### qe_7days_2023_08_day5_c_t2:
* Name:	Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* Description:	Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* Type:	Event
* EventId:	event_7days_2023_08_21_t2
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 2

### qe_7days_2023_08_day5_d_t2:
* Name:	Discharging officers grants credits and insignias, which can be used to level up other officers.
* Description:	Discharging officers grants credits and insignias, which can be used to level up other officers.
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
### qe_7days_2023_08_day5_a_t3:
* Name:	Day 5: Lessons
* Description:	Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
* Type:	Event
* EventId:	event_7days_2023_08_21_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T3up
			* Mode: Generated

### qe_7days_2023_08_day5_b_t3:
* Name:	Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.
* Description:	Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.
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

### qe_7days_2023_08_day5_c_t3:
* Name:	Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* Description:	Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* Type:	Event
* EventId:	event_7days_2023_08_21_t3
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 3

### qe_7days_2023_08_day5_d_t3:
* Name:	Discharging officers grants credits and insignias, which can be used to level up other officers.
* Description:	Discharging officers grants credits and insignias, which can be used to level up other officers.
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
### qe_7days_2023_08_day5_a_t4:
* Name:	Day 5: Lessons
* Description:	Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
* Type:	Event
* EventId:	event_7days_2023_08_21_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T4up
			* Mode: Generated

### qe_7days_2023_08_day5_b_t4:
* Name:	Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.
* Description:	Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.
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

### qe_7days_2023_08_day5_c_t4:
* Name:	Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* Description:	Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* Type:	Event
* EventId:	event_7days_2023_08_21_t4
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 5

### qe_7days_2023_08_day5_d_t4:
* Name:	Discharging officers grants credits and insignias, which can be used to level up other officers.
* Description:	Discharging officers grants credits and insignias, which can be used to level up other officers.
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
### qe_7days_2023_08_day6_a_t1:
* Name:	Day 6: Stockpile
* Description:	Rare earths are an occasional by-product of refining. They are required for upgrading modules.
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

### qe_7days_2023_08_day6_b_t1:
* Name:	The strength of modules can be increased through upgrades, which cost rare earths.
* Description:	Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* Type:	Event
* EventId:	event_7days_2023_08_21_t1
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 1

### qe_7days_2023_08_day6_c_t1:
* Name:	The strength of modules can be increased through upgrades, which cost rare earths.
* Description:	Small items such as strike craft, modules and parts can be built in the fabricator. Larger items such as escort ships and flagships must be constructed at shipyards provided at larger stations.
* Type:	Event
* EventId:	event_7days_2023_08_21_t1
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: T1up
			* Amount: 1

### qe_7days_2023_08_day6_d_t1:
* Name:	The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Description:	The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
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
### qe_7days_2023_08_day6_a_t2:
* Name:	Day 6: Stockpile
* Description:	Rare earths are an occasional by-product of refining. They are required for upgrading modules.
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

### qe_7days_2023_08_day6_b_t2:
* Name:	The strength of modules can be increased through upgrades, which cost rare earths.
* Description:	The strength of modules can be increased through upgrades, which cost rare earths.
* Type:	Event
* EventId:	event_7days_2023_08_21_t2
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Upgrade
			* Tags: External_Module_T1up
			* Amount: 1

### qe_7days_2023_08_day6_c_t2:
* Name:	The strength of modules can be increased through upgrades, which cost rare earths.
* Description:	Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.
* Type:	Event
* EventId:	event_7days_2023_08_21_t2
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: Part_T2up
			* Amount: 25

### qe_7days_2023_08_day6_d_t2:
* Name:	The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Description:	The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
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
### qe_7days_2023_08_day6_a_t3:
* Name:	Day 6: Stockpile
* Description:	Rare earths are an occasional by-product of refining. They are required for upgrading modules.
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

### qe_7days_2023_08_day6_b_t3:
* Name:	The strength of modules can be increased through upgrades, which cost rare earths.
* Description:	The strength of modules can be increased through upgrades, which cost rare earths.
* Type:	Event
* EventId:	event_7days_2023_08_21_t3
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Upgrade
			* Tags: External_Module_T2up
			* Amount: 1

### qe_7days_2023_08_day6_c_t3:
* Name:	The strength of modules can be increased through upgrades, which cost rare earths.
* Description:	The strength of modules can be increased through upgrades, which cost rare earths.
* Type:	Event
* EventId:	event_7days_2023_08_21_t3
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Upgrade
			* Tags: Internal_Module_T2up
			* Amount: 1

### qe_7days_2023_08_day6_d_t3:
* Name:	The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Description:	The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
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
### qe_7days_2023_08_day6_a_t4:
* Name:	Day 6: Stockpile
* Description:	Rare earths are an occasional by-product of refining. They are required for upgrading modules.
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

### qe_7days_2023_08_day6_b_t4:
* Name:	The strength of modules can be increased through upgrades, which cost rare earths.
* Description:	The strength of modules can be increased through upgrades, which cost rare earths.
* Type:	Event
* EventId:	event_7days_2023_08_21_t4
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Upgrade
			* Tags: External_Module_T3up
			* Amount: 1

### qe_7days_2023_08_day6_c_t4:
* Name:	The strength of modules can be increased through upgrades, which cost rare earths.
* Description:	The strength of modules can be increased through upgrades, which cost rare earths.
* Type:	Event
* EventId:	event_7days_2023_08_21_t4
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Upgrade
			* Tags: Internal_Module_T3up
			* Amount: 1

### qe_7days_2023_08_day6_d_t4:
* Name:	The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Description:	The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Type:	Event
* EventId:	event_7days_2023_08_21_t4
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedT4
			* Amount: 15

## QL_7DAYS_2023_08_DAY7_T1
### qe_7days_2023_08_day7_a_t1:
* Name:	Day 7: Enemy Contact
* Description:	Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
* Type:	Event
* EventId:	event_7days_2023_08_21_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T1up
			* Mode: Generated

### qe_7days_2023_08_day7_b_t1:
* Name:	The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Description:	The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
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

### qe_7days_2023_08_day7_c_t1:
* Name:	When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.
* Description:	When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.
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

### qe_7days_2023_08_day7_d_t1:
* Name:	Strikes are difficult missions that require a strong fleet from several commanders to beat. Completing a strike rewards code fragments, which can be turned in for special blueprints.
* Description:	Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
* Type:	Event
* EventId:	event_7days_2023_08_21_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T1up
			* Mode: Generated

## QL_7DAYS_2023_08_DAY7_T2
### qe_7days_2023_08_day7_a_t2:
* Name:	Day 7: Enemy Contact
* Description:	Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
* Type:	Event
* EventId:	event_7days_2023_08_21_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T2up
			* Mode: Generated

### qe_7days_2023_08_day7_b_t2:
* Name:	The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Description:	The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
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

### qe_7days_2023_08_day7_c_t2:
* Name:	When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.
* Description:	When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.
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

### qe_7days_2023_08_day7_d_t2:
* Name:	Strikes are difficult missions that require a strong fleet from several commanders to beat. Completing a strike rewards code fragments, which can be turned in for special blueprints.
* Description:	Strikes are difficult missions that require a strong fleet from several commanders to beat. Completing a strike rewards code fragments, which can be turned in for special blueprints.
* Type:	Event
* EventId:	event_7days_2023_08_21_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Mode: Strike
			* Tags: T1up

## QL_7DAYS_2023_08_DAY7_T3
### qe_7days_2023_08_day7_a_t3:
* Name:	Day 7: Enemy Contact
* Description:	Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
* Type:	Event
* EventId:	event_7days_2023_08_21_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T3up
			* Mode: Generated

### qe_7days_2023_08_day7_b_t3:
* Name:	The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Description:	The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Type:	Event
* EventId:	event_7days_2023_08_21_t3
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedT3
				* ShipsDestroyedT4
			* Amount: 15

### qe_7days_2023_08_day7_c_t3:
* Name:	When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.
* Description:	When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.
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

### qe_7days_2023_08_day7_d_t3:
* Name:	Strikes are difficult missions that require a strong fleet from several commanders to beat. Completing a strike rewards code fragments, which can be turned in for special blueprints.
* Description:	Strikes are difficult missions that require a strong fleet from several commanders to beat. Completing a strike rewards code fragments, which can be turned in for special blueprints.
* Type:	Event
* EventId:	event_7days_2023_08_21_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Mode: Strike
			* Tags: T2up

## QL_7DAYS_2023_08_DAY7_T4
### qe_7days_2023_08_day7_a_t4:
* Name:	Day 7: Enemy Contact
* Description:	Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
* Type:	Event
* EventId:	event_7days_2023_08_21_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T4up
			* Mode: Generated

### qe_7days_2023_08_day7_b_t4:
* Name:	The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Description:	The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Type:	Event
* EventId:	event_7days_2023_08_21_t4
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: ShipsDestroyedT4
			* Amount: 15

### qe_7days_2023_08_day7_c_t4:
* Name:	When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.
* Description:	When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.
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

### qe_7days_2023_08_day7_d_t4:
* Name:	Strikes are difficult missions that require a strong fleet from several commanders to beat. Completing a strike rewards code fragments, which can be turned in for special blueprints.
* Description:	Strikes are difficult missions that require a strong fleet from several commanders to beat. Completing a strike rewards code fragments, which can be turned in for special blueprints.
* Type:	Event
* EventId:	event_7days_2023_08_21_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Mode: Strike
			* Tags: T3up

## QL_EVENT_IYAFAL_2023_T1
### qe_iyaFal_2023_day01_t1:
* Name:	No header for quest qe_iyaFal_2023_day01_t1
* Description:	No description for quest qe_iyaFal_2023_day01_t1
* Type:	Event
* EventId:	event_season_iyaFal_2023_t1
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: T1up

### qe_iyaFal_2023_day02_t1:
* Name:	No header for quest qe_iyaFal_2023_day02_t1
* Description:	No description for quest qe_iyaFal_2023_day02_t1
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

### qe_iyaFal_2023_day03_t1:
* Name:	No header for quest qe_iyaFal_2023_day03_t1
* Description:	No description for quest qe_iyaFal_2023_day03_t1
* Type:	Event
* EventId:	event_season_iyaFal_2023_t1
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: T1up
			* Amount: 5

### qe_iyaFal_2023_day04_t1:
* Name:	No header for quest qe_iyaFal_2023_day04_t1
* Description:	No description for quest qe_iyaFal_2023_day04_t1
* Type:	Event
* EventId:	event_season_iyaFal_2023_t1
* MailsOnCompletion:	m_iyaFal_day4_log
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T1up
			* Mode: Generated

### qe_iyaFal_2023_day05_t1:
* Name:	No header for quest qe_iyaFal_2023_day05_t1
* Description:	No description for quest qe_iyaFal_2023_day05_t1
* Type:	Event
* EventId:	event_season_iyaFal_2023_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T1up

### qe_iyaFal_2023_day06_t1:
* Name:	No header for quest qe_iyaFal_2023_day06_t1
* Description:	No description for quest qe_iyaFal_2023_day06_t1
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

### qe_iyaFal_2023_day07_t1:
* Name:	No header for quest qe_iyaFal_2023_day07_t1
* Description:	No description for quest qe_iyaFal_2023_day07_t1
* Type:	Event
* EventId:	event_season_iyaFal_2023_t1
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 1

### qe_iyaFal_2023_day08_t1:
* Name:	No header for quest qe_iyaFal_2023_day08_t1
* Description:	No description for quest qe_iyaFal_2023_day08_t1
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

### qe_iyaFal_2023_day09_t1:
* Name:	No header for quest qe_iyaFal_2023_day09_t1
* Description:	No description for quest qe_iyaFal_2023_day09_t1
* Type:	Event
* EventId:	event_season_iyaFal_2023_t1
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: T1up

### qe_iyaFal_2023_day10_t1:
* Name:	No header for quest qe_iyaFal_2023_day10_t1
* Description:	No description for quest qe_iyaFal_2023_day10_t1
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

### qe_iyaFal_2023_day11_t1:
* Name:	No header for quest qe_iyaFal_2023_day11_t1
* Description:	No description for quest qe_iyaFal_2023_day11_t1
* Type:	Event
* EventId:	event_season_iyaFal_2023_t1
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: T1up
			* Amount: 5

### qe_iyaFal_2023_day12_t1:
* Name:	No header for quest qe_iyaFal_2023_day12_t1
* Description:	No description for quest qe_iyaFal_2023_day12_t1
* Type:	Event
* EventId:	event_season_iyaFal_2023_t1
* MailsOnCompletion:	m_iyaFal_day12_log
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Rare_T1up
			* Mode: Generated

### qe_iyaFal_2023_day13_t1:
* Name:	No header for quest qe_iyaFal_2023_day13_t1
* Description:	No description for quest qe_iyaFal_2023_day13_t1
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

### qe_iyaFal_2023_day14_t1:
* Name:	No header for quest qe_iyaFal_2023_day14_t1
* Description:	No description for quest qe_iyaFal_2023_day14_t1
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

### qe_iyaFal_2023_day15_t1:
* Name:	No header for quest qe_iyaFal_2023_day15_t1
* Description:	No description for quest qe_iyaFal_2023_day15_t1
* Type:	Event
* EventId:	event_season_iyaFal_2023_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_iyaFal2023_Escort_t1

## QL_EVENT_IYAFAL_2023_EPILOG_T1
### qe_iyaFal_2023_epi01_t1:
* Name:	No header for quest qe_iyaFal_2023_epi01_t1
* Description:	No description for quest qe_iyaFal_2023_epi01_t1
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

### qe_iyaFal_2023_epi02_t1:
* Name:	No header for quest qe_iyaFal_2023_epi02_t1
* Description:	No description for quest qe_iyaFal_2023_epi02_t1
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

### qe_iyaFal_2023_epi03_t1:
* Name:	No header for quest qe_iyaFal_2023_epi03_t1
* Description:	No description for quest qe_iyaFal_2023_epi03_t1
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

### qe_iyaFal_2023_epi04_t1:
* Name:	No header for quest qe_iyaFal_2023_epi04_t1
* Description:	No description for quest qe_iyaFal_2023_epi04_t1
* Type:	Event
* EventId:	event_season_iyaFal_2023_t1
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 1

### qe_iyaFal_2023_epi05_t1:
* Name:	No header for quest qe_iyaFal_2023_epi05_t1
* Description:	No description for quest qe_iyaFal_2023_epi05_t1
* Type:	Event
* EventId:	event_season_iyaFal_2023_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Rare_T1up
			* Mode: Generated

## QL_EVENT_IYAFAL_2023_T2
### qe_iyaFal_2023_day01_t2:
* Name:	No header for quest qe_iyaFal_2023_day01_t2
* Description:	No description for quest qe_iyaFal_2023_day01_t2
* Type:	Event
* EventId:	event_season_iyaFal_2023_t2
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: Faction_Tr1_T2up

### qe_iyaFal_2023_day02_t2:
* Name:	No header for quest qe_iyaFal_2023_day02_t2
* Description:	No description for quest qe_iyaFal_2023_day02_t2
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

### qe_iyaFal_2023_day03_t2:
* Name:	No header for quest qe_iyaFal_2023_day03_t2
* Description:	No description for quest qe_iyaFal_2023_day03_t2
* Type:	Event
* EventId:	event_season_iyaFal_2023_t2
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: Part_T2up
			* Amount: 100

### qe_iyaFal_2023_day04_t2:
* Name:	No header for quest qe_iyaFal_2023_day04_t2
* Description:	No description for quest qe_iyaFal_2023_day04_t2
* Type:	Event
* EventId:	event_season_iyaFal_2023_t2
* MailsOnCompletion:	m_iyaFal_day4_log
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T2up
			* Mode: Generated

### qe_iyaFal_2023_day05_t2:
* Name:	No header for quest qe_iyaFal_2023_day05_t2
* Description:	No description for quest qe_iyaFal_2023_day05_t2
* Type:	Event
* EventId:	event_season_iyaFal_2023_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Mode: Faction
			* Tags: T2up

### qe_iyaFal_2023_day06_t2:
* Name:	No header for quest qe_iyaFal_2023_day06_t2
* Description:	No description for quest qe_iyaFal_2023_day06_t2
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

### qe_iyaFal_2023_day07_t2:
* Name:	No header for quest qe_iyaFal_2023_day07_t2
* Description:	No description for quest qe_iyaFal_2023_day07_t2
* Type:	Event
* EventId:	event_season_iyaFal_2023_t2
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 2

### qe_iyaFal_2023_day08_t2:
* Name:	No header for quest qe_iyaFal_2023_day08_t2
* Description:	No description for quest qe_iyaFal_2023_day08_t2
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

### qe_iyaFal_2023_day09_t2:
* Name:	No header for quest qe_iyaFal_2023_day09_t2
* Description:	No description for quest qe_iyaFal_2023_day09_t2
* Type:	Event
* EventId:	event_season_iyaFal_2023_t2
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: Faction_Tr1_T2up

### qe_iyaFal_2023_day10_t2:
* Name:	No header for quest qe_iyaFal_2023_day10_t2
* Description:	No description for quest qe_iyaFal_2023_day10_t2
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

### qe_iyaFal_2023_day11_t2:
* Name:	No header for quest qe_iyaFal_2023_day11_t2
* Description:	No description for quest qe_iyaFal_2023_day11_t2
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

### qe_iyaFal_2023_day12_t2:
* Name:	No header for quest qe_iyaFal_2023_day12_t2
* Description:	No description for quest qe_iyaFal_2023_day12_t2
* Type:	Event
* EventId:	event_season_iyaFal_2023_t2
* MailsOnCompletion:	m_iyaFal_day12_log
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Epic_T2up
			* Mode: Generated

### qe_iyaFal_2023_day13_t2:
* Name:	No header for quest qe_iyaFal_2023_day13_t2
* Description:	No description for quest qe_iyaFal_2023_day13_t2
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

### qe_iyaFal_2023_day14_t2:
* Name:	No header for quest qe_iyaFal_2023_day14_t2
* Description:	No description for quest qe_iyaFal_2023_day14_t2
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

### qe_iyaFal_2023_day15_t2:
* Name:	No header for quest qe_iyaFal_2023_day15_t2
* Description:	No description for quest qe_iyaFal_2023_day15_t2
* Type:	Event
* EventId:	event_season_iyaFal_2023_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_iyaFal2023_Escort_t2

## QL_EVENT_IYAFAL_2023_EPILOG_T2
### qe_iyaFal_2023_epi01_t2:
* Name:	No header for quest qe_iyaFal_2023_epi01_t2
* Description:	No description for quest qe_iyaFal_2023_epi01_t2
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

### qe_iyaFal_2023_epi02_t2:
* Name:	No header for quest qe_iyaFal_2023_epi02_t2
* Description:	No description for quest qe_iyaFal_2023_epi02_t2
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

### qe_iyaFal_2023_epi03_t2:
* Name:	No header for quest qe_iyaFal_2023_epi03_t2
* Description:	No description for quest qe_iyaFal_2023_epi03_t2
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

### qe_iyaFal_2023_epi04_t2:
* Name:	No header for quest qe_iyaFal_2023_epi04_t2
* Description:	No description for quest qe_iyaFal_2023_epi04_t2
* Type:	Event
* EventId:	event_season_iyaFal_2023_t2
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 2

### qe_iyaFal_2023_epi05_t2:
* Name:	No header for quest qe_iyaFal_2023_epi05_t2
* Description:	No description for quest qe_iyaFal_2023_epi05_t2
* Type:	Event
* EventId:	event_season_iyaFal_2023_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Mode: Strike
			* Tags: T1up

## QL_EVENT_IYAFAL_2023_T3
### qe_iyaFal_2023_day01_t3:
* Name:	No header for quest qe_iyaFal_2023_day01_t3
* Description:	No description for quest qe_iyaFal_2023_day01_t3
* Type:	Event
* EventId:	event_season_iyaFal_2023_t3
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: Faction_Tr1_T3up

### qe_iyaFal_2023_day02_t3:
* Name:	No header for quest qe_iyaFal_2023_day02_t3
* Description:	No description for quest qe_iyaFal_2023_day02_t3
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

### qe_iyaFal_2023_day03_t3:
* Name:	No header for quest qe_iyaFal_2023_day03_t3
* Description:	No description for quest qe_iyaFal_2023_day03_t3
* Type:	Event
* EventId:	event_season_iyaFal_2023_t3
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: Part_T3up
			* Amount: 100

### qe_iyaFal_2023_day04_t3:
* Name:	No header for quest qe_iyaFal_2023_day04_t3
* Description:	No description for quest qe_iyaFal_2023_day04_t3
* Type:	Event
* EventId:	event_season_iyaFal_2023_t3
* MailsOnCompletion:	m_iyaFal_day4_log
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T3up
			* Mode: Generated

### qe_iyaFal_2023_day05_t3:
* Name:	No header for quest qe_iyaFal_2023_day05_t3
* Description:	No description for quest qe_iyaFal_2023_day05_t3
* Type:	Event
* EventId:	event_season_iyaFal_2023_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Mode: Faction
			* Tags: T3up

### qe_iyaFal_2023_day06_t3:
* Name:	No header for quest qe_iyaFal_2023_day06_t3
* Description:	No description for quest qe_iyaFal_2023_day06_t3
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

### qe_iyaFal_2023_day07_t3:
* Name:	No header for quest qe_iyaFal_2023_day07_t3
* Description:	No description for quest qe_iyaFal_2023_day07_t3
* Type:	Event
* EventId:	event_season_iyaFal_2023_t3
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 3

### qe_iyaFal_2023_day08_t3:
* Name:	No header for quest qe_iyaFal_2023_day08_t3
* Description:	No description for quest qe_iyaFal_2023_day08_t3
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

### qe_iyaFal_2023_day09_t3:
* Name:	No header for quest qe_iyaFal_2023_day09_t3
* Description:	No description for quest qe_iyaFal_2023_day09_t3
* Type:	Event
* EventId:	event_season_iyaFal_2023_t3
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: Faction_Tr1_T3up

### qe_iyaFal_2023_day10_t3:
* Name:	No header for quest qe_iyaFal_2023_day10_t3
* Description:	No description for quest qe_iyaFal_2023_day10_t3
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

### qe_iyaFal_2023_day11_t3:
* Name:	No header for quest qe_iyaFal_2023_day11_t3
* Description:	No description for quest qe_iyaFal_2023_day11_t3
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

### qe_iyaFal_2023_day12_t3:
* Name:	No header for quest qe_iyaFal_2023_day12_t3
* Description:	No description for quest qe_iyaFal_2023_day12_t3
* Type:	Event
* EventId:	event_season_iyaFal_2023_t3
* MailsOnCompletion:	m_iyaFal_day12_log
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Epic_T3up
			* Mode: Generated

### qe_iyaFal_2023_day13_t3:
* Name:	No header for quest qe_iyaFal_2023_day13_t3
* Description:	No description for quest qe_iyaFal_2023_day13_t3
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

### qe_iyaFal_2023_day14_t3:
* Name:	No header for quest qe_iyaFal_2023_day14_t3
* Description:	No description for quest qe_iyaFal_2023_day14_t3
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

### qe_iyaFal_2023_day15_t3:
* Name:	No header for quest qe_iyaFal_2023_day15_t3
* Description:	No description for quest qe_iyaFal_2023_day15_t3
* Type:	Event
* EventId:	event_season_iyaFal_2023_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_iyaFal2023_Escort_t3

## QL_EVENT_IYAFAL_2023_EPILOG_T3
### qe_iyaFal_2023_epi01_t3:
* Name:	No header for quest qe_iyaFal_2023_epi01_t3
* Description:	No description for quest qe_iyaFal_2023_epi01_t3
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

### qe_iyaFal_2023_epi02_t3:
* Name:	No header for quest qe_iyaFal_2023_epi02_t3
* Description:	No description for quest qe_iyaFal_2023_epi02_t3
* Type:	Event
* EventId:	event_season_iyaFal_2023_t3
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedProgenitorT3
				* ShipsDestroyedProgenitorT4
			* Amount: 10

### qe_iyaFal_2023_epi03_t3:
* Name:	No header for quest qe_iyaFal_2023_epi03_t3
* Description:	No description for quest qe_iyaFal_2023_epi03_t3
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

### qe_iyaFal_2023_epi04_t3:
* Name:	No header for quest qe_iyaFal_2023_epi04_t3
* Description:	No description for quest qe_iyaFal_2023_epi04_t3
* Type:	Event
* EventId:	event_season_iyaFal_2023_t3
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 3

### qe_iyaFal_2023_epi05_t3:
* Name:	No header for quest qe_iyaFal_2023_epi05_t3
* Description:	No description for quest qe_iyaFal_2023_epi05_t3
* Type:	Event
* EventId:	event_season_iyaFal_2023_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Mode: Strike
			* Tags: T2up

## QL_EVENT_IYAFAL_2023_T4
### qe_iyaFal_2023_day01_t4:
* Name:	No header for quest qe_iyaFal_2023_day01_t4
* Description:	No description for quest qe_iyaFal_2023_day01_t4
* Type:	Event
* EventId:	event_season_iyaFal_2023_t4
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: Faction_T4up

### qe_iyaFal_2023_day02_t4:
* Name:	No header for quest qe_iyaFal_2023_day02_t4
* Description:	No description for quest qe_iyaFal_2023_day02_t4
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

### qe_iyaFal_2023_day03_t4:
* Name:	No header for quest qe_iyaFal_2023_day03_t4
* Description:	No description for quest qe_iyaFal_2023_day03_t4
* Type:	Event
* EventId:	event_season_iyaFal_2023_t4
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: Part_T4up
			* Amount: 100

### qe_iyaFal_2023_day04_t4:
* Name:	No header for quest qe_iyaFal_2023_day04_t4
* Description:	No description for quest qe_iyaFal_2023_day04_t4
* Type:	Event
* EventId:	event_season_iyaFal_2023_t4
* MailsOnCompletion:	m_iyaFal_day4_log
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Tags: T4up
			* Mode: Generated

### qe_iyaFal_2023_day05_t4:
* Name:	No header for quest qe_iyaFal_2023_day05_t4
* Description:	No description for quest qe_iyaFal_2023_day05_t4
* Type:	Event
* EventId:	event_season_iyaFal_2023_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Mode: Faction
			* Tags: T4up

### qe_iyaFal_2023_day06_t4:
* Name:	No header for quest qe_iyaFal_2023_day06_t4
* Description:	No description for quest qe_iyaFal_2023_day06_t4
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

### qe_iyaFal_2023_day07_t4:
* Name:	No header for quest qe_iyaFal_2023_day07_t4
* Description:	No description for quest qe_iyaFal_2023_day07_t4
* Type:	Event
* EventId:	event_season_iyaFal_2023_t4
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 5

### qe_iyaFal_2023_day08_t4:
* Name:	No header for quest qe_iyaFal_2023_day08_t4
* Description:	No description for quest qe_iyaFal_2023_day08_t4
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

### qe_iyaFal_2023_day09_t4:
* Name:	No header for quest qe_iyaFal_2023_day09_t4
* Description:	No description for quest qe_iyaFal_2023_day09_t4
* Type:	Event
* EventId:	event_season_iyaFal_2023_t4
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: Faction_T4up

### qe_iyaFal_2023_day10_t4:
* Name:	No header for quest qe_iyaFal_2023_day10_t4
* Description:	No description for quest qe_iyaFal_2023_day10_t4
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

### qe_iyaFal_2023_day11_t4:
* Name:	No header for quest qe_iyaFal_2023_day11_t4
* Description:	No description for quest qe_iyaFal_2023_day11_t4
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

### qe_iyaFal_2023_day12_t4:
* Name:	No header for quest qe_iyaFal_2023_day12_t4
* Description:	No description for quest qe_iyaFal_2023_day12_t4
* Type:	Event
* EventId:	event_season_iyaFal_2023_t4
* MailsOnCompletion:	m_iyaFal_day12_log
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Epic_T4up
			* Mode: Generated

### qe_iyaFal_2023_day13_t4:
* Name:	No header for quest qe_iyaFal_2023_day13_t4
* Description:	No description for quest qe_iyaFal_2023_day13_t4
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

### qe_iyaFal_2023_day14_t4:
* Name:	No header for quest qe_iyaFal_2023_day14_t4
* Description:	No description for quest qe_iyaFal_2023_day14_t4
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

### qe_iyaFal_2023_day15_t4:
* Name:	No header for quest qe_iyaFal_2023_day15_t4
* Description:	No description for quest qe_iyaFal_2023_day15_t4
* Type:	Event
* EventId:	event_season_iyaFal_2023_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_iyaFal2023_Escort_t4

## QL_EVENT_IYAFAL_2023_EPILOG_T4
### qe_iyaFal_2023_epi01_t4:
* Name:	No header for quest qe_iyaFal_2023_epi01_t4
* Description:	No description for quest qe_iyaFal_2023_epi01_t4
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

### qe_iyaFal_2023_epi02_t4:
* Name:	No header for quest qe_iyaFal_2023_epi02_t4
* Description:	No description for quest qe_iyaFal_2023_epi02_t4
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

### qe_iyaFal_2023_epi03_t4:
* Name:	No header for quest qe_iyaFal_2023_epi03_t4
* Description:	No description for quest qe_iyaFal_2023_epi03_t4
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

### qe_iyaFal_2023_epi04_t4:
* Name:	No header for quest qe_iyaFal_2023_epi04_t4
* Description:	No description for quest qe_iyaFal_2023_epi04_t4
* Type:	Event
* EventId:	event_season_iyaFal_2023_t4
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 5

### qe_iyaFal_2023_epi05_t4:
* Name:	No header for quest qe_iyaFal_2023_epi05_t4
* Description:	No description for quest qe_iyaFal_2023_epi05_t4
* Type:	Event
* EventId:	event_season_iyaFal_2023_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 5
			* Mode: Strike
			* Tags: T3up

## QL_EVENT_ANNIVERSARY_2023_T1
### qe_anniversary_2023_day01_A_t1:
* Name:	Day 1: Research Directive
* Description:	We received priority communication from Lazarus Base concerning Gideon S'jet. The transmission is encrypted with a specific vibration that can only be found on Hiigaran fabricators. We need to construct any item to match the encryption.

<color=#FBB03F>Small items such as strike craft, modules and parts can be built in the fabricator. Larger items such as escort ships and flagships must be constructed at shipyards provided at larger stations.</color>
* Type:	Event
* EventId:	event_anniversary_2023_t1
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: T1up
			* Amount: 1

### qe_anniversary_2023_day01_B_t1:
* Name:	The list given to us by Gideon includes many components found only in Progenitor ships. The easiest way to collect them is to harvest them from downed Progenitor units.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
* Description:	The list given to us by Gideon includes many components found only in Progenitor ships. The easiest way to collect them is to harvest them from downed Progenitor units.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
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

### qe_anniversary_2023_day01_C_t1:
* Name:	Progenitor Cognition Nodes are a fragile component often found floating in free space near ancient wreckages.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
* Description:	Progenitor Cognition Nodes are a fragile component often found floating in free space near ancient wreckages.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
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

### qe_anniversary_2023_day02_A_t1:
* Name:	Day 2: Cash Money
* Description:	Ekekko can bring us in contact with traders specialized in Progenitor technology. But knowing the Iyatequa, everything has a price. We should mine minerals to recuperate the losses we'll have to pay.

<color=#FBB03F>Ore can be mined from asteroids in asteroid fields. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
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

### qe_anniversary_2023_day02_B_t1:
* Name:	To impress the Iyatequa traders and procure the Progenitor components for Gideon, we will have to work on our reputation among a certain clientele.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Description:	To impress the Iyatequa traders and buy the Progenitor components for Gideon, we will have to work on our reputation.

<color=#FBB03F>You can earn insignias by completing missions.</color>
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

### qe_anniversary_2023_day02_C_t1:
* Name:	In order to raise funds to acquire the needed Progenitor components for Gideon, we must sell some of our stored items on the local market.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
* Description:	In order to raise funds to acquire the needed Progenitor components for Gideon, we must sell some of our stored items on the local market.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
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

### qe_anniversary_2023_day03_A_t1:
* Name:	Day 3: Stop Scouting
* Description:	We need to search for recent communications data in this sector to pick up a lead on Guahai's Yaot fleet. We should find what we are looking for on recently destroyed ships.

<color=#FBB03F>The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.</color>
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

### qe_anniversary_2023_day03_B_t1:
* Name:	We are in search of the missing data disk Guahai mentioned in his transmission. We might be able to find it in salvage crates from local outlaws.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
* Description:	We are in search of the missing data disk Guahai mentioned in his transmission. We might be able to find it in salvage crates from local outlaws.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
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

### qe_anniversary_2023_day03_C_t1:
* Name:	The reconnaissance disk gave us a lead on the Progenitor component the Yaot call the Stambha. Enemy activity is high in the target location.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* Description:	The data disk gave us a lead on the Progenitor component the Yaot call the Stambah. It seems to be located inside a sector with strong enemy activity.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Type:	Event
* EventId:	event_anniversary_2023_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Rare_T1up
			* Mode: Generated

### qe_anniversary_2023_day04_A_t1:
* Name:	Day 4: Lost and Found
* Description:	Gideon has emerged from his laboratory. He talks of the possibility to build a device that could change the fortunes of Hiigarans in Nimbus. However, we must search for a final component.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
* Type:	Event
* EventId:	event_anniversary_2023_t1
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_T1up
			* Amount: 5
			* Analyzed: True

### qe_anniversary_2023_day04_B_t1:
* Name:	Gideon is in need of raw materials to construct a secret device. We should look for a jovian planet to collect some gas.

<color=#FBB03F>Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.</color>
* Description:	Gideon is in need of raw materials to construct his secret device. We have to mine some minerals for him.

<color=#FBB03F>Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
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

### qe_anniversary_2023_day04_C_t1:
* Name:	According to Ekekko, the last component on Gideon's list might be in the hands of a powerful enemy. The search for additional information is sending us into the most dangerous areas of this sector.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Description:	According to Ekekko, the last component on Gideon's list might be in the hands of a powerful enemy. The search for additional information is sending us into the most dangerous areas of this sector.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Type:	Event
* EventId:	event_anniversary_2023_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Rare_T1up
			* Mode: Generated

### qe_anniversary_2023_day05_A_t1:
* Name:	Day 5: Help Wanted
* Description:	We want to make contact with Tepin Papan, commander of the Tanoch Empire. To open up a communication channel, we should do some hired work for the local authorities.

<color=#FBB03F>There are different types of assignments available in your assignment log.</color>
* Type:	Event
* EventId:	event_anniversary_2023_t1
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: T1up

### qe_anniversary_2023_day05_B_t1:
* Name:	Tepin Papan has offered to provide information on Gideon's last component if we help him with a security issue he currently faces.

<color=#FBB03F>Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.</color>
* Description:	Tepin Papan has offered to provide information on Gideon's last component if we help him with a security issue he currently faces.

<color=#FBB03F>The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.</color>
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

### qe_anniversary_2023_day05_C_t1:
* Name:	According to Tepin Papan, some of the Tanoch sectors require assistance. We should seek out their liaison offices and complete assignments.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Description:	Tepin Papan wants us to retrieve some stolen goods. We should begin salvaging crates in the areas indicated by Tanoch data.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
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

### qe_anniversary_2023_day06_A_t1:
* Name:	Day 6: Training Day
* Description:	While Lazarus Base is processing the reports on the stolen Progenitor component, Gideon wants us to train a crew to handle the device he's constructing.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.</color>
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

### qe_anniversary_2023_day06_B_t1:
* Name:	With Gideon's new program, we should start training the crew that will man his enigmatic device.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* Description:	With Gideon's new program, we should start training the crew that will man his enigmatic device.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* Type:	Event
* EventId:	event_anniversary_2023_t1
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 1

### qe_anniversary_2023_day06_C_t1:
* Name:	It is time to put our newly trained crew to the test. We received a task from Lazarus Base to engage a hostile fleet nearby.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* Description:	It is time to put our newly trained crew to the test. We received a task from Lazarus Base to engage a hostile fleet nearby.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Type:	Event
* EventId:	event_anniversary_2023_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Rare_T1up
			* Mode: Generated

### qe_anniversary_2023_day07_A_t1:
* Name:	Day 7: Simple Collection
* Description:	Guhai is a high ranking Yaot official and Lazarus Base has advised us to follow his instructions for now. His first transmitted task needs us to mine resources.

<color=#FBB03F>Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
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

### qe_anniversary_2023_day07_B_t1:
* Name:	We continue to follow Guahai’s orders. His next task for us is to produce refined material.

<color=#FBB03F>Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.</color>
* Description:	We continue to follow Guahai’s orders. His next task for us is to produce refined material.

<color=#FBB03F>Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.</color>
* Type:	Event
* EventId:	event_anniversary_2023_t1
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Refining
			* Tags: Asteroid_Refined_T1up
			* Amount: 500

### qe_anniversary_2023_day07_C_t1:
* Name:	Guahai requires us to build specific items for his fleet, as repayment for stealing their cultural item.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
* Description:	Guahai requires us to build specific items for his fleet, as repayment for stealing their cultural item.

<color=#FBB03F>Small items such as strike craft, modules and parts can be built in the fabricator. Larger items such as escort ships and flagships must be constructed at shipyards provided at larger stations.</color>
* Type:	Event
* EventId:	event_anniversary_2023_t1
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: T1up
			* Amount: 1

### qe_anniversary_2023_day08_A_t1:
* Name:	Day 8: Cangacian Patrol
* Description:	Lazarus Base has informed us that the Tanoch reports on the stolen Progenitor component point towards an infamous pirate group called The Fleet of Rams. We should hunt down Cangacian vessels for more information.

<color=#FBB03F>The Cangacians are pirates that harass trade routes and colonies. We may find them in signals in most areas of the galaxy. They have been sighted raiding mining fleets in asteroid clusters as well.</color>
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

### qe_anniversary_2023_day08_B_t1:
* Name:	The last item Gideon needs to build his device is in the possession of Catequil, Lieutenant of the Fleet of Rams. We have to find communications data from hostile ships to locate his position.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
* Description:	The last item Gideon needs to build his device is in the possession of Catequil, Lieutenant of the Fleet of Rams. We have to find communications data from hostile ships to locate his position.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
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

### qe_anniversary_2023_day08_C_t1:
* Name:	Our engineers were able to triangulate Catequil's transmission. We must chase him down to attain the last Progenitor component for Gideon.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* Description:	Our engineers were able to triangulate Catequil's transmission. We must chase him down to attain the last Progenitor component for Gideon.

<color=#FBB03F>The Cangacians are pirates that harass trade routes and colonies. We may find them in signals in most areas of the galaxy. They have been sighted raiding mining fleets in asteroid clusters as well.</color>
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

### qe_anniversary_2023_day09_A_t1:
* Name:	Day 9: Special Instructions
* Description:	While Gideon is finalizing the construction of the Progenitor Negotiator, one of our officers must be trained to utilize it in action.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* Type:	Event
* EventId:	event_anniversary_2023_t1
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 1

### qe_anniversary_2023_day09_B_t1:
* Name:	Before we embark on Gideon's special operation, we should further increase our fleet's power to ensure we are ready for any eventuality.

<color=#FBB03F>Internal Modules can be upgraded in the Internal Module screen which increases their attributes. Upgrading one level costs credits and RE.</color>
* Description:	We have to fabricate several items to modify a common freighter for Gideon's special operation.

<color=#FBB03F>Small items such as strike craft, modules and parts can be built in the fabricator. Larger items such as escort ships and flagships must be constructed at shipyards provided at larger stations.</color>
* Type:	Event
* EventId:	event_anniversary_2023_t1
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: T1up
			* Amount: 1

### qe_anniversary_2023_day09_C_t1:
* Name:	We are instructed to perform one final operations readiness test. All forces must be fully prepared for whatever Gideon is planning.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* Description:	We are instructed to perform one final operations readiness test. All forces must be fully prepared for whatever Gideon is planning.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Type:	Event
* EventId:	event_anniversary_2023_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Rare_T1up
			* Mode: Generated

### qe_anniversary_2023_day10_A_t1:
* Name:	Day 10: The Special Operation
* Description:	Gideon has finally revealed his plan. From the Progenitor components we collected he constructed a communication device to retake control of Wiracoda Gate. We are trying to go home.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Type:	Event
* EventId:	event_anniversary_2023_t1
* MailsOnCompletion:	m_anniversary_enoch_log
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_anniversary2023_Wiracoda_t1

## QL_EVENT_ANNIVERSARY_2023_T2
### qe_anniversary_2023_day01_A_t2:
* Name:	We received priority communication from Hiigaran Command of Lazarus Base concerning Gideon S'jet. We need to decrypt it in our laboratory first before we can read it.

<color=#FBB03F>Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.</color>
* Description:	We received priority communication from Hiigaran Command of Lazarus Base concerning Gideon S'jet. We need to decrypt it in our laboratory first before we can read it.

<color=#FBB03F>Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.</color>
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

### qe_anniversary_2023_day01_B_t2:
* Name:	The list given to us by Gideon includes many components found only in Progenitor ships. The easiest way to collect them is to harvest them from downed Progenitor units.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
* Description:	The list given to us by Gideon includes many components found only in Progenitor ships. The easiest way to collect them is to harvest them from downed Progenitor units.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
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

### qe_anniversary_2023_day01_C_t2:
* Name:	Progenitor Cognition Nodes are a fragile component often found floating in free space near ancient wreckages.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
* Description:	Progenitor Cognition Nodes are a fragile component often found floating in free space near ancient wreckages.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
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

### qe_anniversary_2023_day02_A_t2:
* Name:	Ekekko can bring us in contact with traders specialized in Progenitor technology. But knowing the Iyatequa, everything has a price. We should mine minerals to recuperate the losses we'll have to pay.

<color=#FBB03F>Type D ore is not abundant enough to form asteroid clusters on its own. Instead, asteroids with D type ore can be found within clusters rich with other types of ore.</color>
* Description:	Ekekko can bring us in contact with traders specialized in Progenitor technology. But knowing the Iyatequa, everything has a price. We should mine minerals to recuperate the losses we'll have to pay.

<color=#FBB03F>Type D ore is not abundant enough to form asteroid clusters on its own. Instead, asteroids with D type ore can be found within clusters rich with other types of ore.</color>
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

### qe_anniversary_2023_day02_B_t2:
* Name:	To impress the Iyatequa traders and procure the Progenitor components for Gideon, we will have to work on our reputation among a certain clientele.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Description:	To impress the Iyatequa traders and procure the Progenitor components for Gideon, we will have to work on our reputation among a certain clientele.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
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

### qe_anniversary_2023_day02_C_t2:
* Name:	In order to raise funds to acquire the needed Progenitor components for Gideon, we must sell some of our stored items on the local market.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
* Description:	In order to raise funds to acquire the needed Progenitor components for Gideon, we must sell some of our stored items on the local market.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
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

### qe_anniversary_2023_day03_A_t2:
* Name:	We need to search for recent communications data in this sector to pick up a lead on Guahai's Yaot fleet. We should find what we are looking for on recently destroyed ships.

<color=#FBB03F>The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.</color>
* Description:	We need to search for recent communications data in this sector to pick up a lead on Guahai's Yaot fleet. We should find what we are looking for on recently destroyed ships.

<color=#FBB03F>The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.</color>
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

### qe_anniversary_2023_day03_B_t2:
* Name:	We are in search of the missing data disk Guahai mentioned in his transmission. We might be able to find it in salvage crates from local outlaws.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
* Description:	We are in search of the missing data disk Guahai mentioned in his transmission. We might be able to find it in salvage crates from local outlaws.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
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

### qe_anniversary_2023_day03_C_t2:
* Name:	The reconnaissance disk gave us a lead on the Progenitor component the Yaot call the Stambha. Enemy activity is high in the target location.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* Description:	The reconnaissance disk gave us a lead on the Progenitor component the Yaot call the Stambha. Enemy activity is high in the target location.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* Type:	Event
* EventId:	event_anniversary_2023_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Mode: Strike
			* Tags: T1up

### qe_anniversary_2023_day04_A_t2:
* Name:	Gideon has emerged from his laboratory. He talks of the possibility to build a device that could change the fortunes of Hiigarans in Nimbus. However, we must search for a final component.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
* Description:	Gideon has emerged from his laboratory. He talks of the possibility to build a device that could change the fortunes of Hiigarans in Nimbus. However, we must search for a final component.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
* Type:	Event
* EventId:	event_anniversary_2023_t2
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_T2up
			* Amount: 5
			* Analyzed: True

### qe_anniversary_2023_day04_B_t2:
* Name:	Gideon is in need of raw materials to construct a secret device. We should look for a jovian planet to collect some gas.

<color=#FBB03F>Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.</color>
* Description:	Gideon is in need of raw materials to construct his secret device. We have to mine some minerals for him.

<color=#FBB03F>Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
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

### qe_anniversary_2023_day04_C_t2:
* Name:	According to Ekekko, the last component on Gideon's list might be in the hands of a powerful enemy. The search for additional information is sending us into the most dangerous areas of this sector.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Description:	According to Ekekko, the last component on Gideon's list might be in the hands of a powerful enemy. The search for additional information is sending us into the most dangerous areas of this sector.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Type:	Event
* EventId:	event_anniversary_2023_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Epic_T2up
			* Mode: Generated

### qe_anniversary_2023_day05_A_t2:
* Name:	We want to make contact with Tepin Papan, commander of the Tanoch Empire. To find a communication channel, we should do some hired work for the local authorities.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Description:	We want to make contact with Tepin Papan, commander of the Tanoch Empire. To find a communication channel, we should do some hired work for the local authorities.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Type:	Event
* EventId:	event_anniversary_2023_t2
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: Faction_T2up

### qe_anniversary_2023_day05_B_t2:
* Name:	Tepin Papan has offered to provide information on Gideon's last component if we help him with a security issue he currently faces.

<color=#FBB03F>Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.</color>
* Description:	Tepin Papan has offered to provide information on Gideon's last component if we help him with a security issue he currently faces.

<color=#FBB03F>Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.</color>
* Type:	Event
* EventId:	event_anniversary_2023_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Mode: Faction
			* Tags: T2up_Tanoch

### qe_anniversary_2023_day05_C_t2:
* Name:	According to Tepin Papan, some of the Tanoch sectors require assistance. We should seek out their liaison offices and complete assignments.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Description:	According to Tepin Papan, some of the Tanoch sectors require assistance. We should seek out their liaison offices and complete assignments.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Type:	Event
* EventId:	event_anniversary_2023_t2
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: RepTanoch
			* Amount: 135

### qe_anniversary_2023_day06_A_t2:
* Name:	While Lazarus Base is processing the reports on the stolen Progenitor component, Gideon wants us to train a crew to handle the device he's constructing.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.</color>
* Description:	While Lazarus Base is processing the reports on the stolen Progenitor component, Gideon wants us to train a crew to handle the device he's constructing.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.</color>
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

### qe_anniversary_2023_day06_B_t2:
* Name:	With Gideon's new program, we should start training the crew that will man his enigmatic device.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* Description:	With Gideon's new program, we should start training the crew that will man his enigmatic device.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* Type:	Event
* EventId:	event_anniversary_2023_t2
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 2

### qe_anniversary_2023_day06_C_t2:
* Name:	It is time to put our newly trained crew to the test. We received a task from Lazarus Base to engage a hostile fleet nearby.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* Description:	It is time to put our newly trained crew to the test. We received a task from Lazarus Base to engage a hostile fleet nearby.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* Type:	Event
* EventId:	event_anniversary_2023_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Mode: Strike
			* Tags: T1up

### qe_anniversary_2023_day07_A_t2:
* Name:	Guhai is a high ranking Yaot official and Lazarus Base has advised us to follow his instructions for now. His first transmitted task needs us to mine resources.

<color=#FBB03F>Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
* Description:	Guhai is a high ranking Yaot official and Lazarus Base has advised us to follow his instructions for now. His first transmitted task needs us to mine resources.

<color=#FBB03F>Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
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

### qe_anniversary_2023_day07_B_t2:
* Name:	We continue to follow Guahai’s orders. His next task for us is to produce refined material.

<color=#FBB03F>Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.</color>
* Description:	We continue to follow Guahai’s orders. His next task for us is to produce refined material.

<color=#FBB03F>Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.</color>
* Type:	Event
* EventId:	event_anniversary_2023_t2
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Refining
			* Tags: Asteroid_Refined_T2up
			* Amount: 500

### qe_anniversary_2023_day07_C_t2:
* Name:	Guahai requires us to build specific items for his fleet, as repayment for stealing their cultural item.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
* Description:	Guahai requires us to build specific items for his fleet, as repayment for stealing their cultural item.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
* Type:	Event
* EventId:	event_anniversary_2023_t2
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: Part_T2up
			* Amount: 50

### qe_anniversary_2023_day08_A_t2:
* Name:	Lazarus Base has informed us that the Tanoch reports on the stolen Progenitor component point towards an infamous pirate group called The Fleet of Rams. We should hunt down Cangacian vessels for more information.

<color=#FBB03F>The Cangacians are pirates that harass trade routes and colonies. We may find them in signals in most areas of the galaxy. They have been sighted raiding mining fleets in asteroid clusters as well.</color>
* Description:	Lazarus Base has informed us that the Tanoch reports on the stolen Progenitor component point towards an infamous pirate group called The Fleet of Rams. We should hunt down Cangacian vessels for more information.

<color=#FBB03F>The Cangacians are pirates that harass trade routes and colonies. We may find them in signals in most areas of the galaxy. They have been sighted raiding mining fleets in asteroid clusters as well.</color>
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

### qe_anniversary_2023_day08_B_t2:
* Name:	The last item Gideon needs to build his device is in the possession of Catequil, Lieutenant of the Fleet of Rams. We have to find communications data from hostile ships to locate his position.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
* Description:	The last item Gideon needs to build his device is in the possession of Catequil, Lieutenant of the Fleet of Rams. We have to find communications data from hostile ships to locate his position.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
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

### qe_anniversary_2023_day08_C_t2:
* Name:	Our engineers were able to triangulate Catequil's transmission. We must chase him down to attain the last Progenitor component for Gideon.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* Description:	Our engineers were able to triangulate Catequil's transmission. We must chase him down to attain the last Progenitor component for Gideon.

<color=#FBB03F>The Cangacians are pirates that harass trade routes and colonies. We may find them in signals in most areas of the galaxy. They have been sighted raiding mining fleets in asteroid clusters as well.</color>
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

### qe_anniversary_2023_day09_A_t2:
* Name:	While Gideon is finalizing the construction of the Progenitor Negotiator, we should increase our fleet's power to protect it in action.

<color=#FBB03F>External modules, such as turrets or sensors, can be upgraded in the External Module screen which will increase their power. Upgrading one level costs credits and RE.</color>
* Description:	While Gideon is finalizing the construction of the Progenitor Negotiator, we should increase our fleet's power to protect it in action.

<color=#FBB03F>External modules, such as turrets or sensors, can be upgraded in the External Module screen which will increase their power. Upgrading one level costs credits and RE.</color>
* Type:	Event
* EventId:	event_anniversary_2023_t2
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Upgrade
			* Tags: External_Module_T1up
			* Amount: 1

### qe_anniversary_2023_day09_B_t2:
* Name:	Before we embark on Gideon's special operation, we should further increase our fleet's power to ensure we are ready for any eventuality.

<color=#FBB03F>Internal Modules can be upgraded in the Internal Module screen which increases their attributes. Upgrading one level costs credits and RE.</color>
* Description:	We have to fabricate several items to modify a common freighter for Gideon's special operation.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
* Type:	Event
* EventId:	event_anniversary_2023_t2
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: Part_T2up
			* Amount: 50

### qe_anniversary_2023_day09_C_t2:
* Name:	We are instructed to perform one final operations readiness test. All forces must be fully prepared for whatever Gideon is planning.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* Description:	We are instructed to perform one final operations readiness test. All forces must be fully prepared for whatever Gideon is planning.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* Type:	Event
* EventId:	event_anniversary_2023_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Mode: Strike
			* Tags: T1up

### qe_anniversary_2023_day10_A_t2:
* Name:	Gideon has finally revealed his plan. From the Progenitor components we collected he constructed a communication device to retake control of Wiracoda Gate. We are trying to go home.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Description:	Gideon has finally revealed his plan. From the Progenitor components we collected he constructed a communication device to retake control of Wiracoda Gate. We are trying to go home.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Type:	Event
* EventId:	event_anniversary_2023_t2
* MailsOnCompletion:	m_anniversary_enoch_log
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_anniversary2023_Wiracoda_t2

## QL_EVENT_ANNIVERSARY_2023_T3
### qe_anniversary_2023_day01_A_t3:
* Name:	We received priority communication from Hiigaran Command of Lazarus Base concerning Gideon S'jet. We need to decrypt it in our laboratory first before we can read it.

<color=#FBB03F>Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.</color>
* Description:	We received priority communication from Hiigaran Command of Lazarus Base concerning Gideon S'jet. We need to decrypt it in our laboratory first before we can read it.

<color=#FBB03F>Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.</color>
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

### qe_anniversary_2023_day01_B_t3:
* Name:	The list given to us by Gideon includes many components found only in Progenitor ships. The easiest way to collect them is to harvest them from downed Progenitor units.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
* Description:	The list given to us by Gideon includes many components found only in Progenitor ships. The easiest way to collect them is to harvest them from downed Progenitor units.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
* Type:	Event
* EventId:	event_anniversary_2023_t3
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedProgenitorT3
				* ShipsDestroyedProgenitorT4
			* Amount: 7

### qe_anniversary_2023_day01_C_t3:
* Name:	Progenitor Cognition Nodes are a fragile component often found floating in free space near ancient wreckages.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
* Description:	Progenitor Cognition Nodes are a fragile component often found floating in free space near ancient wreckages.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
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

### qe_anniversary_2023_day02_A_t3:
* Name:	Ekekko can bring us in contact with traders specialized in Progenitor technology. But knowing the Iyatequa, everything has a price. We should mine minerals to recuperate the losses we'll have to pay.

<color=#FBB03F>Type D ore is not abundant enough to form asteroid clusters on its own. Instead, asteroids with D type ore can be found within clusters rich with other types of ore.</color>
* Description:	Ekekko can bring us in contact with traders specialized in Progenitor technology. But knowing the Iyatequa, everything has a price. We should mine minerals to recuperate the losses we'll have to pay.

<color=#FBB03F>Type D ore is not abundant enough to form asteroid clusters on its own. Instead, asteroids with D type ore can be found within clusters rich with other types of ore.</color>
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

### qe_anniversary_2023_day02_B_t3:
* Name:	To impress the Iyatequa traders and procure the Progenitor components for Gideon, we will have to work on our reputation among a certain clientele.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Description:	To impress the Iyatequa traders and procure the Progenitor components for Gideon, we will have to work on our reputation among a certain clientele.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
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

### qe_anniversary_2023_day02_C_t3:
* Name:	In order to raise funds to acquire the needed Progenitor components for Gideon, we must sell some of our stored items on the local market.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
* Description:	In order to raise funds to acquire the needed Progenitor components for Gideon, we must sell some of our stored items on the local market.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
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

### qe_anniversary_2023_day03_A_t3:
* Name:	We need to search for recent communications data in this sector to pick up a lead on Guahai's Yaot fleet. We should find what we are looking for on recently destroyed ships.

<color=#FBB03F>The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.</color>
* Description:	We need to search for recent communications data in this sector to pick up a lead on Guahai's Yaot fleet. We should find what we are looking for on recently destroyed ships.

<color=#FBB03F>The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.</color>
* Type:	Event
* EventId:	event_anniversary_2023_t3
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedT3
				* ShipsDestroyedT4
			* Amount: 15

### qe_anniversary_2023_day03_B_t3:
* Name:	We are in search of the missing data disk Guahai mentioned in his transmission. We might be able to find it in salvage crates from local outlaws.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
* Description:	We are in search of the missing data disk Guahai mentioned in his transmission. We might be able to find it in salvage crates from local outlaws.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
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

### qe_anniversary_2023_day03_C_t3:
* Name:	The reconnaissance disk gave us a lead on the Progenitor component the Yaot call the Stambha. Enemy activity is high in the target location.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* Description:	The reconnaissance disk gave us a lead on the Progenitor component the Yaot call the Stambha. Enemy activity is high in the target location.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* Type:	Event
* EventId:	event_anniversary_2023_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Mode: Strike
			* Tags: T2up

### qe_anniversary_2023_day04_A_t3:
* Name:	Gideon has emerged from his laboratory. He talks of the possibility to build a device that could change the fortunes of Hiigarans in Nimbus. However, we must search for a final component.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
* Description:	Gideon has emerged from his laboratory. He talks of the possibility to build a device that could change the fortunes of Hiigarans in Nimbus. However, we must search for a final component.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
* Type:	Event
* EventId:	event_anniversary_2023_t3
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_T3up
			* Amount: 5
			* Analyzed: True

### qe_anniversary_2023_day04_B_t3:
* Name:	Gideon is in need of raw materials to construct a secret device. We should look for a jovian planet to collect some gas.

<color=#FBB03F>Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.</color>
* Description:	Gideon is in need of raw materials to construct a secret device. We should look for a jovian planet to collect some gas.

<color=#FBB03F>Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.</color>
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

### qe_anniversary_2023_day04_C_t3:
* Name:	According to Ekekko, the last component on Gideon's list might be in the hands of a powerful enemy. The search for additional information is sending us into the most dangerous areas of this sector.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Description:	According to Ekekko, the last component on Gideon's list might be in the hands of a powerful enemy. The search for additional information is sending us into the most dangerous areas of this sector.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Type:	Event
* EventId:	event_anniversary_2023_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Epic_T3up
			* Mode: Generated

### qe_anniversary_2023_day05_A_t3:
* Name:	We want to make contact with Tepin Papan, commander of the Tanoch Empire. To find a communication channel, we should do some hired work for the local authorities.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Description:	We want to make contact with Tepin Papan, commander of the Tanoch Empire. To find a communication channel, we should do some hired work for the local authorities.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Type:	Event
* EventId:	event_anniversary_2023_t3
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: Faction_T3up

### qe_anniversary_2023_day05_B_t3:
* Name:	Tepin Papan has offered to provide information on Gideon's last component if we help him with a security issue he currently faces.

<color=#FBB03F>Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.</color>
* Description:	Tepin Papan has offered to provide information on Gideon's last component if we help him with a security issue he currently faces.

<color=#FBB03F>Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.</color>
* Type:	Event
* EventId:	event_anniversary_2023_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Mode: Faction
			* Tags: T3up_Tanoch

### qe_anniversary_2023_day05_C_t3:
* Name:	According to Tepin Papan, some of the Tanoch sectors require assistance. We should seek out their liaison offices and complete assignments.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Description:	According to Tepin Papan, some of the Tanoch sectors require assistance. We should seek out their liaison offices and complete assignments.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Type:	Event
* EventId:	event_anniversary_2023_t3
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: RepTanoch
			* Amount: 180

### qe_anniversary_2023_day06_A_t3:
* Name:	While Lazarus Base is processing the reports on the stolen Progenitor component, Gideon wants us to train a crew to handle the device he's constructing.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.</color>
* Description:	While Lazarus Base is processing the reports on the stolen Progenitor component, Gideon wants us to train a crew to handle the device he's constructing.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.</color>
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

### qe_anniversary_2023_day06_B_t3:
* Name:	With Gideon's new program, we should start training the crew that will man his enigmatic device.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* Description:	With Gideon's new program, we should start training the crew that will man his enigmatic device.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* Type:	Event
* EventId:	event_anniversary_2023_t3
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 3

### qe_anniversary_2023_day06_C_t3:
* Name:	It is time to put our newly trained crew to the test. We received a task from Lazarus Base to engage a hostile fleet nearby.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* Description:	It is time to put our newly trained crew to the test. We received a task from Lazarus Base to engage a hostile fleet nearby.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* Type:	Event
* EventId:	event_anniversary_2023_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Mode: Strike
			* Tags: T2up

### qe_anniversary_2023_day07_A_t3:
* Name:	Guhai is a high ranking Yaot official and Lazarus Base has advised us to follow his instructions for now. His first transmitted task needs us to mine resources.

<color=#FBB03F>Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
* Description:	Guhai is a high ranking Yaot official and Lazarus Base has advised us to follow his instructions for now. His first transmitted task needs us to mine resources.

<color=#FBB03F>Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
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

### qe_anniversary_2023_day07_B_t3:
* Name:	We continue to follow Guahai’s orders. His next task for us is to produce refined material.

<color=#FBB03F>Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.</color>
* Description:	We continue to follow Guahai’s orders. His next task for us is to produce refined material.

<color=#FBB03F>Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.</color>
* Type:	Event
* EventId:	event_anniversary_2023_t3
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Refining
			* Tags: Asteroid_Refined_T3up
			* Amount: 500

### qe_anniversary_2023_day07_C_t3:
* Name:	Guahai requires us to build specific items for his fleet, as repayment for stealing their cultural item.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
* Description:	Guahai requires us to build specific items for his fleet, as repayment for stealing their cultural item.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
* Type:	Event
* EventId:	event_anniversary_2023_t3
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: Part_T3up
			* Amount: 50

### qe_anniversary_2023_day08_A_t3:
* Name:	Lazarus Base has informed us that the Tanoch reports on the stolen Progenitor component point towards an infamous pirate group called The Fleet of Rams. We should hunt down Cangacian vessels for more information.

<color=#FBB03F>The Cangacians are pirates that harass trade routes and colonies. We may find them in signals in most areas of the galaxy. They have been sighted raiding mining fleets in asteroid clusters as well.</color>
* Description:	Lazarus Base has informed us that the Tanoch reports on the stolen Progenitor component point towards an infamous pirate group called The Fleet of Rams. We should hunt down Cangacian vessels for more information.

<color=#FBB03F>The Cangacians are pirates that harass trade routes and colonies. We may find them in signals in most areas of the galaxy. They have been sighted raiding mining fleets in asteroid clusters as well.</color>
* Type:	Event
* EventId:	event_anniversary_2023_t3
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedP1T3
				* ShipsDestroyedP1T4
			* Amount: 10

### qe_anniversary_2023_day08_B_t3:
* Name:	The last item Gideon needs to build his device is in the possession of Catequil, Lieutenant of the Fleet of Rams. We have to find communications data from hostile ships to locate his position.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
* Description:	The last item Gideon needs to build his device is in the possession of Catequil, Lieutenant of the Fleet of Rams. We have to find communications data from hostile ships to locate his position.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
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

### qe_anniversary_2023_day08_C_t3:
* Name:	Our engineers were able to triangulate Catequil's transmission. We must chase him down to attain the last Progenitor component for Gideon.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* Description:	Our engineers were able to triangulate Catequil's transmission. We must chase him down to attain the last Progenitor component for Gideon.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* Type:	Event
* EventId:	event_anniversary_2023_t3
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Id: qr_015

### qe_anniversary_2023_day09_A_t3:
* Name:	While Gideon is finalizing the construction of the Progenitor Negotiator, we should increase our fleet's power to protect it in action.

<color=#FBB03F>External modules, such as turrets or sensors, can be upgraded in the External Module screen which will increase their power. Upgrading one level costs credits and RE.</color>
* Description:	While Gideon is finalizing the construction of the Progenitor Negotiator, we should increase our fleet's power to protect it in action.

<color=#FBB03F>External modules, such as turrets or sensors, can be upgraded in the External Module screen which will increase their power. Upgrading one level costs credits and RE.</color>
* Type:	Event
* EventId:	event_anniversary_2023_t3
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Upgrade
			* Tags: External_Module_T2up
			* Amount: 1

### qe_anniversary_2023_day09_B_t3:
* Name:	Before we embark on Gideon's special operation, we should further increase our fleet's power to ensure we are ready for any eventuality.

<color=#FBB03F>Internal Modules can be upgraded in the Internal Module screen which increases their attributes. Upgrading one level costs credits and RE.</color>
* Description:	Before we embark on Gideon's special operation, we should further increase our fleet's power to ensure we are ready for any eventuality.

<color=#FBB03F>Internal Modules can be upgraded in the Internal Module screen which increases their attributes. Upgrading one level costs credits and RE.</color>
* Type:	Event
* EventId:	event_anniversary_2023_t3
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Upgrade
			* Tags: Internal_Module_T2up
			* Amount: 1

### qe_anniversary_2023_day09_C_t3:
* Name:	We are instructed to perform one final operations readiness test. All forces must be fully prepared for whatever Gideon is planning.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* Description:	We are instructed to perform one final operations readiness test. All forces must be fully prepared for whatever Gideon is planning.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* Type:	Event
* EventId:	event_anniversary_2023_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Mode: Strike
			* Tags: T2up

### qe_anniversary_2023_day10_A_t3:
* Name:	Gideon has finally revealed his plan. From the Progenitor components we collected he constructed a communication device to retake control of Wiracoda Gate. We are trying to go home.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Description:	Gideon has finally revealed his plan. From the Progenitor components we collected he constructed a communication device to retake control of Wiracoda Gate. We are trying to go home.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Type:	Event
* EventId:	event_anniversary_2023_t3
* MailsOnCompletion:	m_anniversary_enoch_log
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_anniversary2023_Wiracoda_t3

## QL_EVENT_ANNIVERSARY_2023_T4
### qe_anniversary_2023_day01_A_t4:
* Name:	We received priority communication from Hiigaran Command of Lazarus Base concerning Gideon S'jet. We need to decrypt it in our laboratory first before we can read it.

<color=#FBB03F>Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.</color>
* Description:	We received priority communication from Hiigaran Command of Lazarus Base concerning Gideon S'jet. We need to decrypt it in our laboratory first before we can read it.

<color=#FBB03F>Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.</color>
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

### qe_anniversary_2023_day01_B_t4:
* Name:	The list given to us by Gideon includes many components found only in Progenitor ships. The easiest way to collect them is to harvest them from downed Progenitor units.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
* Description:	The list given to us by Gideon includes many components found only in Progenitor ships. The easiest way to collect them is to harvest them from downed Progenitor units.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
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

### qe_anniversary_2023_day01_C_t4:
* Name:	Progenitor Cognition Nodes are a fragile component often found floating in free space near ancient wreckages.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
* Description:	Progenitor Cognition Nodes are a fragile component often found floating in free space near ancient wreckages.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
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

### qe_anniversary_2023_day02_A_t4:
* Name:	Ekekko can bring us in contact with traders specialized in Progenitor technology. But knowing the Iyatequa, everything has a price. We should mine minerals to recuperate the losses we'll have to pay.

<color=#FBB03F>Type D ore is not abundant enough to form asteroid clusters on its own. Instead, asteroids with D type ore can be found within clusters rich with other types of ore.</color>
* Description:	Ekekko can bring us in contact with traders specialized in Progenitor technology. But knowing the Iyatequa, everything has a price. We should mine minerals to recuperate the losses we'll have to pay.

<color=#FBB03F>Type D ore is not abundant enough to form asteroid clusters on its own. Instead, asteroids with D type ore can be found within clusters rich with other types of ore.</color>
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

### qe_anniversary_2023_day02_B_t4:
* Name:	To impress the Iyatequa traders and procure the Progenitor components for Gideon, we will have to work on our reputation among a certain clientele.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Description:	To impress the Iyatequa traders and procure the Progenitor components for Gideon, we will have to work on our reputation among a certain clientele.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
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

### qe_anniversary_2023_day02_C_t4:
* Name:	In order to raise funds to acquire the needed Progenitor components for Gideon, we must sell some of our stored items on the local market.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
* Description:	In order to raise funds to acquire the needed Progenitor components for Gideon, we must sell some of our stored items on the local market.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
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

### qe_anniversary_2023_day03_A_t4:
* Name:	We need to search for recent communications data in this sector to pick up a lead on Guahai's Yaot fleet. We should find what we are looking for on recently destroyed ships.

<color=#FBB03F>The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.</color>
* Description:	We need to search for recent communications data in this sector to pick up a lead on Guahai's Yaot fleet. We should find what we are looking for on recently destroyed ships.

<color=#FBB03F>The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.</color>
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

### qe_anniversary_2023_day03_B_t4:
* Name:	We are in search of the missing data disk Guahai mentioned in his transmission. We might be able to find it in salvage crates from local outlaws.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
* Description:	We are in search of the missing data disk Guahai mentioned in his transmission. We might be able to find it in salvage crates from local outlaws.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
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

### qe_anniversary_2023_day03_C_t4:
* Name:	The reconnaissance disk gave us a lead on the Progenitor component the Yaot call the Stambha. Enemy activity is high in the target location.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* Description:	The reconnaissance disk gave us a lead on the Progenitor component the Yaot call the Stambha. Enemy activity is high in the target location.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* Type:	Event
* EventId:	event_anniversary_2023_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Mode: Strike
			* Tags: T3up

### qe_anniversary_2023_day04_A_t4:
* Name:	Gideon has emerged from his laboratory. He talks of the possibility to build a device that could change the fortunes of Hiigarans in Nimbus. However, we must search for a final component.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
* Description:	Gideon has emerged from his laboratory. He talks of the possibility to build a device that could change the fortunes of Hiigarans in Nimbus. However, we must search for a final component.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
* Type:	Event
* EventId:	event_anniversary_2023_t4
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_T4up
			* Amount: 5
			* Analyzed: True

### qe_anniversary_2023_day04_B_t4:
* Name:	Gideon is in need of raw materials to construct a secret device. We should look for a jovian planet to collect some gas.

<color=#FBB03F>Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.</color>
* Description:	Gideon is in need of raw materials to construct a secret device. We should look for a jovian planet to collect some gas.

<color=#FBB03F>Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.</color>
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

### qe_anniversary_2023_day04_C_t4:
* Name:	According to Ekekko, the last component on Gideon's list might be in the hands of a powerful enemy. The search for additional information is sending us into the most dangerous areas of this sector.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Description:	According to Ekekko, the last component on Gideon's list might be in the hands of a powerful enemy. The search for additional information is sending us into the most dangerous areas of this sector.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Type:	Event
* EventId:	event_anniversary_2023_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Epic_T4up
			* Mode: Generated

### qe_anniversary_2023_day05_A_t4:
* Name:	We want to make contact with Tepin Papan, commander of the Tanoch Empire. To find a communication channel, we should do some hired work for the local authorities.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Description:	We want to make contact with Tepin Papan, commander of the Tanoch Empire. To find a communication channel, we should do some hired work for the local authorities.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Type:	Event
* EventId:	event_anniversary_2023_t4
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: Faction_T4up

### qe_anniversary_2023_day05_B_t4:
* Name:	Tepin Papan has offered to provide information on Gideon's last component if we help him with a security issue he currently faces.

<color=#FBB03F>Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.</color>
* Description:	Tepin Papan has offered to provide information on Gideon's last component if we help him with a security issue he currently faces.

<color=#FBB03F>Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.</color>
* Type:	Event
* EventId:	event_anniversary_2023_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Mode: Faction
			* Tags: T4up_Tanoch

### qe_anniversary_2023_day05_C_t4:
* Name:	According to Tepin Papan, some of the Tanoch sectors require assistance. We should seek out their liaison offices and complete assignments.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Description:	According to Tepin Papan, some of the Tanoch sectors require assistance. We should seek out their liaison offices and complete assignments.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Type:	Event
* EventId:	event_anniversary_2023_t4
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: RepTanoch
			* Amount: 225

### qe_anniversary_2023_day06_A_t4:
* Name:	While Lazarus Base is processing the reports on the stolen Progenitor component, Gideon wants us to train a crew to handle the device he's constructing.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.</color>
* Description:	While Lazarus Base is processing the reports on the stolen Progenitor component, Gideon wants us to train a crew to handle the device he's constructing.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.</color>
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

### qe_anniversary_2023_day06_B_t4:
* Name:	With Gideon's new program, we should start training the crew that will man his enigmatic device.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* Description:	With Gideon's new program, we should start training the crew that will man his enigmatic device.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* Type:	Event
* EventId:	event_anniversary_2023_t4
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 5

### qe_anniversary_2023_day06_C_t4:
* Name:	It is time to put our newly trained crew to the test. We received a task from Lazarus Base to engage a hostile fleet nearby.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* Description:	It is time to put our newly trained crew to the test. We received a task from Lazarus Base to engage a hostile fleet nearby.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* Type:	Event
* EventId:	event_anniversary_2023_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Mode: Strike
			* Tags: T3up

### qe_anniversary_2023_day07_A_t4:
* Name:	Guhai is a high ranking Yaot official and Lazarus Base has advised us to follow his instructions for now. His first transmitted task needs us to mine resources.

<color=#FBB03F>Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
* Description:	Guhai is a high ranking Yaot official and Lazarus Base has advised us to follow his instructions for now. His first transmitted task needs us to mine resources.

<color=#FBB03F>Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
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

### qe_anniversary_2023_day07_B_t4:
* Name:	We continue to follow Guahai’s orders. His next task for us is to produce refined material.

<color=#FBB03F>Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.</color>
* Description:	We continue to follow Guahai’s orders. His next task for us is to produce refined material.

<color=#FBB03F>Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.</color>
* Type:	Event
* EventId:	event_anniversary_2023_t4
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Refining
			* Tags: Asteroid_Refined_T4up
			* Amount: 500

### qe_anniversary_2023_day07_C_t4:
* Name:	Guahai requires us to build specific items for his fleet, as repayment for stealing their cultural item.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
* Description:	Guahai requires us to build specific items for his fleet, as repayment for stealing their cultural item.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
* Type:	Event
* EventId:	event_anniversary_2023_t4
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: Part_T4up
			* Amount: 50

### qe_anniversary_2023_day08_A_t4:
* Name:	Lazarus Base has informed us that the Tanoch reports on the stolen Progenitor component point towards an infamous pirate group called The Fleet of Rams. We should hunt down Cangacian vessels for more information.

<color=#FBB03F>The Cangacians are pirates that harass trade routes and colonies. We may find them in signals in most areas of the galaxy. They have been sighted raiding mining fleets in asteroid clusters as well.</color>
* Description:	Lazarus Base has informed us that the Tanoch reports on the stolen Progenitor component point towards an infamous pirate group called The Fleet of Rams. We should hunt down Cangacian vessels for more information.

<color=#FBB03F>The Cangacians are pirates that harass trade routes and colonies. We may find them in signals in most areas of the galaxy. They have been sighted raiding mining fleets in asteroid clusters as well.</color>
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

### qe_anniversary_2023_day08_B_t4:
* Name:	The last item Gideon needs to build his device is in the possession of Catequil, Lieutenant of the Fleet of Rams. We have to find communications data from hostile ships to locate his position.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
* Description:	The last item Gideon needs to build his device is in the possession of Catequil, Lieutenant of the Fleet of Rams. We have to find communications data from hostile ships to locate his position.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
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

### qe_anniversary_2023_day08_C_t4:
* Name:	Our engineers were able to triangulate Catequil's transmission. We must chase him down to attain the last Progenitor component for Gideon.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* Description:	Our engineers were able to triangulate Catequil's transmission. We must chase him down to attain the last Progenitor component for Gideon.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* Type:	Event
* EventId:	event_anniversary_2023_t4
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Id: qr_018

### qe_anniversary_2023_day09_A_t4:
* Name:	While Gideon is finalizing the construction of the Progenitor Negotiator, we should increase our fleet's power to protect it in action.

<color=#FBB03F>External modules, such as turrets or sensors, can be upgraded in the External Module screen which will increase their power. Upgrading one level costs credits and RE.</color>
* Description:	While Gideon is finalizing the construction of the Progenitor Negotiator, we should increase our fleet's power to protect it in action.

<color=#FBB03F>External modules, such as turrets or sensors, can be upgraded in the External Module screen which will increase their power. Upgrading one level costs credits and RE.</color>
* Type:	Event
* EventId:	event_anniversary_2023_t4
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Upgrade
			* Tags: External_Module_T3up
			* Amount: 1

### qe_anniversary_2023_day09_B_t4:
* Name:	Before we embark on Gideon's special operation, we should further increase our fleet's power to ensure we are ready for any eventuality.

<color=#FBB03F>Internal Modules can be upgraded in the Internal Module screen which increases their attributes. Upgrading one level costs credits and RE.</color>
* Description:	Before we embark on Gideon's special operation, we should further increase our fleet's power to ensure we are ready for any eventuality.

<color=#FBB03F>Internal Modules can be upgraded in the Internal Module screen which increases their attributes. Upgrading one level costs credits and RE.</color>
* Type:	Event
* EventId:	event_anniversary_2023_t4
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Upgrade
			* Tags: Internal_Module_T3up
			* Amount: 1

### qe_anniversary_2023_day09_C_t4:
* Name:	We are instructed to perform one final operations readiness test. All forces must be fully prepared for whatever Gideon is planning.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* Description:	We are instructed to perform one final operations readiness test. All forces must be fully prepared for whatever Gideon is planning.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* Type:	Event
* EventId:	event_anniversary_2023_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Mode: Strike
			* Tags: T3up

### qe_anniversary_2023_day10_A_t4:
* Name:	Gideon has finally revealed his plan. From the Progenitor components we collected he constructed a communication device to retake control of Wiracoda Gate. We are trying to go home.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Description:	Gideon has finally revealed his plan. From the Progenitor components we collected he constructed a communication device to retake control of Wiracoda Gate. We are trying to go home.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Type:	Event
* EventId:	event_anniversary_2023_t4
* MailsOnCompletion:	m_anniversary_enoch_log
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_anniversary2023_Wiracoda_t4

## QL_EVENT_HALLOWEEN_2023_T1
### qe_halloween_2023_day01_t1:
* Name:	Day 1: Sentinel Duty
* Description:	We are receiving disturbing reports from all over the galaxy. The disaster at Wiracoda Gate has sent the Progenitors into a frenzy! We must assist the defensive efforts wherever we can until we understand what is happening.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
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

### qe_halloween_2023_day02_t1:
* Name:	Day 2: Prospector
* Description:	Refineries are being targeted by the Progenitors in many sectors of Nimbus. Stocks need to be replenished if the defenders are to hold off this calamity.

<color=#FBB03F>Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
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

### qe_halloween_2023_day03_t1:
* Name:	Day 3: Deep Space Recovery
* Description:	Gideon wants to collect any evidence which points to the Progenitor’s current activity. We should collect data from ships that were in combat with the abnormal Progenitor vessels.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
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

### qe_halloween_2023_day04_t1:
* Name:	Day 4: Smelt and Refine
* Description:	Many planets are still in desperate need of resources to hold off the Progenitors. Especially rare resources have been in high demand to increase defensive capabilities.

<color=#FBB03F>Rare earths are an occasional by-product of refining. They are required for upgrading modules.</color>
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

### qe_halloween_2023_day05_t1:
* Name:	Day 5: The Guidepost
* Description:	Gideon has identified a specific Progenitor component we must find in order to decrypt the errant Keeper's command frequency.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
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

### qe_halloween_2023_day06_t1:
* Name:	Day 6: Replacement Parts
* Description:	Many sectors have suffered heavy damages from the ongoing Progenitor attacks. More parts are needed to replenish the defending fleets.

<color=#FBB03F>Small items such as strike craft, modules and parts can be built in the fabricator. Larger items such as escort ships and flagships must be constructed at shipyards provided at larger stations.</color>
* Type:	Event
* EventId:	event_halloween_2023_t1
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: T1up
			* Amount: 5

### qe_halloween_2023_day07_t1:
* Name:	Day 7: Triangulation
* Description:	In order for Gideon to triangulate the location of the errant Keeper we need to hunt down Progenitor vessels receiving its command signal.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
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

### qe_halloween_2023_day08_t1:
* Name:	Day 8: Officer Training
* Description:	We are unsure what awaits us when we'll face the corrupted Keeper once again. Gideon has advised us to train our officers in Progenitor communication theory to effectively analyze the situation in the field.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* Type:	Event
* EventId:	event_halloween_2023_t1
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 1

### qe_halloween_2023_day09_t1:
* Name:	Day 9: Military Exercise
* Description:	In order to be fully prepared for the confrontation with the corrupted Keeper, we need to perform a fleet wide ready-check for all systems. We can engage enemies that have been preying on the local area lately due to the diminished security situation.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Type:	Event
* EventId:	event_halloween_2023_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Rare_T1up
			* Mode: Generated

### qe_halloween_2023_day10_t1:
* Name:	Day 10: Safe Passage
* Description:	The Iyatequa promised to negotiate a deal for safe passage into Cangacian space. However, even though the galaxy is at stake, the traders still insist on receiving a hefty price.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
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

### qe_halloween_2023_day11_t1:
* Name:	Day 11: Confrontation
* Description:	We must confront the corrupted Keeper Malik and end the Progenitor incursion.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Type:	Event
* EventId:	event_halloween_2023_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_halloween2023_Rashidun_t1

## QL_EVENT_HALLOWEEN_2023_T2
### qe_halloween_2023_day01_t2:
* Name:	We are receiving disturbing reports from all over the galaxy. The disaster at Wiracoda Gate has sent the Progenitors into a frenzy! We must assist the defensive efforts wherever we can until we understand what is happening.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
* Description:	We are receiving disturbing reports from all over the galaxy. The disaster at Wiracoda Gate has sent the Progenitors into a frenzy! We must assist the defensive efforts wherever we can until we understand what is happening.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
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

### qe_halloween_2023_day02_t2:
* Name:	Gas refineries are being targeted by the Progenitors in many sectors of Nimbus. Stocks need to be replenished if the defenders are to hold off this calamity.

<color=#FBB03F>Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.</color>
* Description:	Refineries are being targeted by the Progenitors in many sectors of Nimbus. Stocks need to be replenished if the defenders are to hold off this calamity.

<color=#FBB03F>Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
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

### qe_halloween_2023_day03_t2:
* Name:	Gideon wants to collect any evidence which points to the Progenitor’s current activity. We should collect data from ships that were in combat with the abnormal Progenitor vessels.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
* Description:	Gideon wants to collect any evidence which points to the Progenitor’s current activity. We should collect data from ships that were in combat with the abnormal Progenitor vessels.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
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

### qe_halloween_2023_day04_t2:
* Name:	Many planets are still in desperate need of resources to hold off the Progenitors. Especially rare resources have been in high demand to increase defensive capabilities.

<color=#FBB03F>Rare earths are an occasional by-product of refining. They are required for upgrading modules.</color>
* Description:	Many planets are still in desperate need of resources to hold off the Progenitors. Especially rare resources have been in high demand to increase defensive capabilities.

<color=#FBB03F>Rare earths are an occasional by-product of refining. They are required for upgrading modules.</color>
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

### qe_halloween_2023_day05_t2:
* Name:	Gideon has identified a specific Progenitor component we must find in order to decrypt the errant Keeper's command frequency.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
* Description:	Gideon has identified a specific Progenitor component we must find in order to decrypt the errant Keeper's command frequency.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
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

### qe_halloween_2023_day06_t2:
* Name:	Many sectors have suffered heavy damages from the ongoing Progenitor attacks. More parts are needed to replenish the defending fleets.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
* Description:	Many sectors have suffered heavy damages from the ongoing Progenitor attacks. More parts are needed to replenish the defending fleets.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
* Type:	Event
* EventId:	event_halloween_2023_t2
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: Part_T2up
			* Amount: 100

### qe_halloween_2023_day07_t2:
* Name:	In order for Gideon to triangulate the location of the errant Keeper we need to hunt down Progenitor vessels receiving its command signal.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
* Description:	In order for Gideon to triangulate the location of the errant Keeper we need to hunt down Progenitor vessels receiving its command signal.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
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

### qe_halloween_2023_day08_t2:
* Name:	We are unsure what awaits us when we'll face the corrupted Keeper once again. Gideon has advised us to train our officers in Progenitor communication theory to effectively analyze the situation in the field.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* Description:	We are unsure what awaits us when we'll face the corrupted Keeper once again. Gideon has advised us to train our officers in Progenitor communication theory to effectively analyze the situation in the field.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* Type:	Event
* EventId:	event_halloween_2023_t2
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 2

### qe_halloween_2023_day09_t2:
* Name:	In order to be fully prepared for the confrontation with the corrupted Keeper, we need to perform a fleet wide ready-check for all systems. We can engage enemies that have been preying on the local area lately due to the diminished security situation.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* Description:	In order to be fully prepared for the confrontation with the corrupted Keeper, we need to perform a fleet wide ready-check for all systems. We can engage enemies that have been preying on the local area lately due to the diminished security situation.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* Type:	Event
* EventId:	event_halloween_2023_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Mode: Strike
			* Tags: T1up

### qe_halloween_2023_day10_t2:
* Name:	The Iyatequa promised to negotiate a deal for safe passage into Cangacian space. However, even though the galaxy is at stake, the traders still insist on receiving a hefty price.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
* Description:	The Iyatequa promised to negotiate a deal for safe passage into Cangacian space. However, even though the galaxy is at stake, the traders still insist on receiving a hefty price.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
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

### qe_halloween_2023_day11_t2:
* Name:	We must confront the corrupted Keeper Malik and end the Progenitor incursion.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Description:	We must confront the corrupted Keeper Malik and end the Progenitor incursion.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Type:	Event
* EventId:	event_halloween_2023_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_halloween2023_Rashidun_t2

## QL_EVENT_HALLOWEEN_2023_T3
### qe_halloween_2023_day01_t3:
* Name:	We are receiving disturbing reports from all over the galaxy. The disaster at Wiracoda Gate has sent the Progenitors into a frenzy! We must assist the defensive efforts wherever we can until we understand what is happening.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
* Description:	We are receiving disturbing reports from all over the galaxy. The disaster at Wiracoda Gate has sent the Progenitors into a frenzy! We must assist the defensive efforts wherever we can until we understand what is happening.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
* Type:	Event
* EventId:	event_halloween_2023_t3
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedProgenitorT3
				* ShipsDestroyedProgenitorT4
			* Amount: 10

### qe_halloween_2023_day02_t3:
* Name:	Gas refineries are being targeted by the Progenitors in many sectors of Nimbus. Stocks need to be replenished if the defenders are to hold off this calamity.

<color=#FBB03F>Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.</color>
* Description:	Gas refineries are being targeted by the Progenitors in many sectors of Nimbus. Stocks need to be replenished if the defenders are to hold off this calamity.

<color=#FBB03F>Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.</color>
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

### qe_halloween_2023_day03_t3:
* Name:	Gideon wants to collect any evidence which points to the Progenitor’s current activity. We should collect data from ships that were in combat with the abnormal Progenitor vessels.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
* Description:	Gideon wants to collect any evidence which points to the Progenitor’s current activity. We should collect data from ships that were in combat with the abnormal Progenitor vessels.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
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

### qe_halloween_2023_day04_t3:
* Name:	Many planets are still in desperate need of resources to hold off the Progenitors. Especially rare resources have been in high demand to increase defensive capabilities.

<color=#FBB03F>Rare earths are an occasional by-product of refining. They are required for upgrading modules.</color>
* Description:	Many planets are still in desperate need of resources to hold off the Progenitors. Especially rare resources have been in high demand to increase defensive capabilities.

<color=#FBB03F>Rare earths are an occasional by-product of refining. They are required for upgrading modules.</color>
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

### qe_halloween_2023_day05_t3:
* Name:	Gideon has identified a specific Progenitor component we must find in order to decrypt the errant Keeper's command frequency.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
* Description:	Gideon has identified a specific Progenitor component we must find in order to decrypt the errant Keeper's command frequency.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
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

### qe_halloween_2023_day06_t3:
* Name:	Many sectors have suffered heavy damages from the ongoing Progenitor attacks. More parts are needed to replenish the defending fleets.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
* Description:	Many sectors have suffered heavy damages from the ongoing Progenitor attacks. More parts are needed to replenish the defending fleets.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
* Type:	Event
* EventId:	event_halloween_2023_t3
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: Part_T3up
			* Amount: 100

### qe_halloween_2023_day07_t3:
* Name:	In order for Gideon to triangulate the location of the errant Keeper we need to hunt down Progenitor vessels receiving its command signal.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
* Description:	In order for Gideon to triangulate the location of the errant Keeper we need to hunt down Progenitor vessels receiving its command signal.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
* Type:	Event
* EventId:	event_halloween_2023_t3
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedProgenitorT3
				* ShipsDestroyedProgenitorT4
			* Amount: 10

### qe_halloween_2023_day08_t3:
* Name:	We are unsure what awaits us when we'll face the corrupted Keeper once again. Gideon has advised us to train our officers in Progenitor communication theory to effectively analyze the situation in the field.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* Description:	We are unsure what awaits us when we'll face the corrupted Keeper once again. Gideon has advised us to train our officers in Progenitor communication theory to effectively analyze the situation in the field.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* Type:	Event
* EventId:	event_halloween_2023_t3
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 3

### qe_halloween_2023_day09_t3:
* Name:	In order to be fully prepared for the confrontation with the corrupted Keeper, we need to perform a fleet wide ready-check for all systems. We can engage enemies that have been preying on the local area lately due to the diminished security situation.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* Description:	In order to be fully prepared for the confrontation with the corrupted Keeper, we need to perform a fleet wide ready-check for all systems. We can engage enemies that have been preying on the local area lately due to the diminished security situation.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* Type:	Event
* EventId:	event_halloween_2023_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Mode: Strike
			* Tags: T2up

### qe_halloween_2023_day10_t3:
* Name:	The Iyatequa promised to negotiate a deal for safe passage into Cangacian space. However, even though the galaxy is at stake, the traders still insist on receiving a hefty price.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
* Description:	The Iyatequa promised to negotiate a deal for safe passage into Cangacian space. However, even though the galaxy is at stake, the traders still insist on receiving a hefty price.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
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

### qe_halloween_2023_day11_t3:
* Name:	We must confront the corrupted Keeper Malik and end the Progenitor incursion.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Description:	We must confront the corrupted Keeper Malik and end the Progenitor incursion.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Type:	Event
* EventId:	event_halloween_2023_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_halloween2023_Rashidun_t3

## QL_EVENT_HALLOWEEN_2023_T4
### qe_halloween_2023_day01_t4:
* Name:	We are receiving disturbing reports from all over the galaxy. The disaster at Wiracoda Gate has sent the Progenitors into a frenzy! We must assist the defensive efforts wherever we can until we understand what is happening.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
* Description:	We are receiving disturbing reports from all over the galaxy. The disaster at Wiracoda Gate has sent the Progenitors into a frenzy! We must assist the defensive efforts wherever we can until we understand what is happening.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
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

### qe_halloween_2023_day02_t4:
* Name:	Gas refineries are being targeted by the Progenitors in many sectors of Nimbus. Stocks need to be replenished if the defenders are to hold off this calamity.

<color=#FBB03F>Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.</color>
* Description:	Gas refineries are being targeted by the Progenitors in many sectors of Nimbus. Stocks need to be replenished if the defenders are to hold off this calamity.

<color=#FBB03F>Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.</color>
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

### qe_halloween_2023_day03_t4:
* Name:	Gideon wants to collect any evidence which points to the Progenitor’s current activity. We should collect data from ships that were in combat with the abnormal Progenitor vessels.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
* Description:	Gideon wants to collect any evidence which points to the Progenitor’s current activity. We should collect data from ships that were in combat with the abnormal Progenitor vessels.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
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

### qe_halloween_2023_day04_t4:
* Name:	Many planets are still in desperate need of resources to hold off the Progenitors. Especially rare resources have been in high demand to increase defensive capabilities.

<color=#FBB03F>Rare earths are an occasional by-product of refining. They are required for upgrading modules.</color>
* Description:	Many planets are still in desperate need of resources to hold off the Progenitors. Especially rare resources have been in high demand to increase defensive capabilities.

<color=#FBB03F>Rare earths are an occasional by-product of refining. They are required for upgrading modules.</color>
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

### qe_halloween_2023_day05_t4:
* Name:	Gideon has identified a specific Progenitor component we must find in order to decrypt the errant Keeper's command frequency.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
* Description:	Gideon has identified a specific Progenitor component we must find in order to decrypt the errant Keeper's command frequency.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
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

### qe_halloween_2023_day06_t4:
* Name:	Many sectors have suffered heavy damages from the ongoing Progenitor attacks. More parts are needed to replenish the defending fleets.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
* Description:	Many sectors have suffered heavy damages from the ongoing Progenitor attacks. More parts are needed to replenish the defending fleets.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
* Type:	Event
* EventId:	event_halloween_2023_t4
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: Part_T4up
			* Amount: 100

### qe_halloween_2023_day07_t4:
* Name:	In order for Gideon to triangulate the location of the errant Keeper we need to hunt down Progenitor vessels receiving its command signal.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
* Description:	In order for Gideon to triangulate the location of the errant Keeper we need to hunt down Progenitor vessels receiving its command signal.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
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

### qe_halloween_2023_day08_t4:
* Name:	We are unsure what awaits us when we'll face the corrupted Keeper once again. Gideon has advised us to train our officers in Progenitor communication theory to effectively analyze the situation in the field.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* Description:	We are unsure what awaits us when we'll face the corrupted Keeper once again. Gideon has advised us to train our officers in Progenitor communication theory to effectively analyze the situation in the field.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* Type:	Event
* EventId:	event_halloween_2023_t4
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 5

### qe_halloween_2023_day09_t4:
* Name:	In order to be fully prepared for the confrontation with the corrupted Keeper, we need to perform a fleet wide ready-check for all systems. We can engage enemies that have been preying on the local area lately due to the diminished security situation.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* Description:	In order to be fully prepared for the confrontation with the corrupted Keeper, we need to perform a fleet wide ready-check for all systems. We can engage enemies that have been preying on the local area lately due to the diminished security situation.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* Type:	Event
* EventId:	event_halloween_2023_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 5
			* Mode: Strike
			* Tags: T3up

### qe_halloween_2023_day10_t4:
* Name:	The Iyatequa promised to negotiate a deal for safe passage into Cangacian space. However, even though the galaxy is at stake, the traders still insist on receiving a hefty price.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
* Description:	The Iyatequa promised to negotiate a deal for safe passage into Cangacian space. However, even though the galaxy is at stake, the traders still insist on receiving a hefty price.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
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

### qe_halloween_2023_day11_t4:
* Name:	We must confront the corrupted Keeper Malik and end the Progenitor incursion.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Description:	We must confront the corrupted Keeper Malik and end the Progenitor incursion.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Type:	Event
* EventId:	event_halloween_2023_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_halloween2023_Rashidun_t4

## QL_EVENT_TANOCHWINTER_2023_T1
### qe_tanWin_2023_day01_t1:
* Name:	Day 1: Resource Relief
* Description:	We received priority communication from Lazarus Base. A subfaction of the Tanoch, the Chicuat, have made contact with Hiigaran representatives and requested aid. Fleet Command wants us to support the Chicuat and establish friendly ties. Our first task is to provide basic resources.

<color=#FBB03F>Ore can be mined from asteroids in asteroid fields. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
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

### qe_tanWin_2023_day02_t1:
* Name:	Day 2: Processor Surrogate
* Description:	The Chicuat infrastructure is badly degraded with age and suffered heavy damage in recent attacks. We're asked to refine materials to support their restoration efforts.

<color=#FBB03F>Rare earths are an occasional by-product of refining. They are required for upgrading modules.</color>
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

### qe_tanWin_2023_day03_t1:
* Name:	Day 3: Wayward Cargo
* Description:	The Chicuat have informed us several critical supply convoys have gone missing. We should try to retrieve any goods by hunting down local bandits.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
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

### qe_tanWin_2023_day04_t1:
* Name:	Day 4: Relief Package
* Description:	Ekekko, our Iyatequa liaison, has suggested to negotiate a trade deal with his contacts to support the Chicuat's need for basic supplies. We should sell some of our own items to get the traders interested.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
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

### qe_tanWin_2023_day05_t1:
* Name:	Day 5: Gesture of Aid
* Description:	We received emergency communication from the Chicuat Elders. They anticipate a raid on one of their remote trading stations. Toci asks us to take on the defense in order to relieve the weakened and overextended Chicuat forces.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Type:	Event
* EventId:	event_tanochWinter_2023_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_tanWin2023_DefendBase_t1

### qe_tanWin_2023_day06_t1:
* Name:	Day 6: Imperial Appeal
* Description:	We must find out whether the Tecuban really are behind the recent attacks on the Chicuat. Our contact in the Tanoch Empire might be able to provide information. We should do some assignments to show good faith.

<color=#FBB03F>There are different types of assignments available in your assignment log.</color>
* Type:	Event
* EventId:	event_tanochWinter_2023_t1
* MailsOnCompletion:	m_tanWin_2023_d06_log
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: T1up

### qe_tanWin_2023_day07_t1:
* Name:	Day 7: Black Eye
* Description:	Lazarus Base has processed Tepin Papan's information. There are reports about the rising influence of an ambitous leader named Heyoka. He is promoting expansionist ideas and has a particular disdain for the Chicuat. We should find out if the name is familiar in the criminal underworld here.

<color=#FBB03F>The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.</color>
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

### qe_tanWin_2023_day08_t1:
* Name:	Day 8: Catch and Kill
* Description:	Our investigations produced evidence for contact between the Tecuban leader Heyoka and high profile criminals. We must hunt down these outlaws to learn more.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Type:	Event
* EventId:	event_tanochWinter_2023_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Rare_T1up
			* Mode: Generated

### qe_tanWin_2023_day09_t1:
* Name:	Day 9: Raise the Stakes
* Description:	The Chicuat Elders have asked us to wait for their intelligence report on possible Tecuban forces within Acatla. In the meanwhile we should strengthen our forces to prepare for battle.

<color=#FBB03F>Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.</color>
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

### qe_tanWin_2023_day10_t1:
* Name:	Day 10: In the Shadows
* Description:	Intelligence from the Chicuat points to a Tecuban base operating around an uninhabited planet. We must go there and eliminate this base to stop the raids.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Type:	Event
* EventId:	event_tanochWinter_2023_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_tanWin2023_AttackBase_t1

### qe_tanWin_2023_day11_t1:
* Name:	Day 11: Imperial Rumors
* Description:	In order to gather information about the Vaygr's activity we must contact Tepin Papan once more. We should do some assignments to compensate him for his assistance.

<color=#FBB03F>There are different types of assignments available in your assignment log.</color>
* Type:	Event
* EventId:	event_tanochWinter_2023_t1
* MailsOnCompletion:	m_tanWin_2023_d11_log
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: T1up

### qe_tanWin_2023_day12_t1:
* Name:	Day 12: Seek and Recover
* Description:	While Tepin Papan is trying to gather information about the Vaygr's involvement with the Tecuban, we should scan some systems and see if we can find any clues about their whereabouts.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
* Type:	Event
* EventId:	event_tanochWinter_2023_t1
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_T1up
			* Amount: 10
			* Analyzed: True

### qe_tanWin_2023_day13_t1:
* Name:	Day 13: Among the People
* Description:	We hope to learn more about the Vaygr's activity from the local people. We should do some good deeds around here to gain their trust.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.</color>
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

### qe_tanWin_2023_day14_t1:
* Name:	Day 14: Active Search
* Description:	Some local folks have agreed to provide information that could lead to the Vaygr. However, before they hand it over, they want us help them with a particularly challenging mission.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Type:	Event
* EventId:	event_tanochWinter_2023_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Rare_T1up
			* Mode: Generated

### qe_tanWin_2023_day15_t1:
* Name:	Day 15: Hunting Party
* Description:	We must hunt down a group of thugs that is suspected to be working for the Vaygr.

<color=#FBB03F>The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.</color>
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

### qe_tanWin_2023_day16_t1:
* Name:	Day 16: Attack the Vaygr
* Description:	In our search for the Vaygr involved with the Tecuban, we aquired one of their communication frequencies. If we contact the Vaygr now, we should be able to trace their signal and hyper jump to their exact location.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Type:	Event
* EventId:	event_tanochWinter_2023_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_tanWin2023_Relic_t1

### qe_tanWin_2023_day17_t1:
* Name:	Day 17: Polite Inquiries
* Description:	There is still no answer from Tepin Papan since we last spoke with him. We should do some more assignments to gain his attention and see if he was able to gather any information about the Vaygr's intentions.

<color=#FBB03F>There are different types of assignments available in your assignment log.</color>
* Type:	Event
* EventId:	event_tanochWinter_2023_t1
* MailsOnCompletion:	m_tanWin_2023_d17_log
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: T1up

### qe_tanWin_2023_day18_t1:
* Name:	Day 18: Purchased Whispers
* Description:	Ekekko wants us to trade on the local markets and see if we find someone who's willing to sell information on Jochik Kaan's motives.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
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

### qe_tanWin_2023_day19_t1:
* Name:	Day 19: Getting There First
* Description:	We contacted the Chicuat Elders and told them about Jochik Kaan's possible intention to obtain a particular Progenitor object. They have given us intel about a criminal organization that deals with Progenitor objects within the Tanoch Empire. We should investigate.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Type:	Event
* EventId:	event_tanochWinter_2023_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Rare_T1up
			* Mode: Generated

### qe_tanWin_2023_day20_t1:
* Name:	Day 20: Providing Protection
* Description:	While Gideon S'jet is researching the data set of Progenitor objects, the Chicuat Elders have informed us of a resurgance of Tecuban activity within their territory. We should support the defensive efforts.

<color=#FBB03F>The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.</color>
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

### qe_tanWin_2023_day21_t1:
* Name:	Day 21: Hunt for Knowledge
* Description:	Gideon S'jet's research into the data set of Progenitor objects turned out more difficult than expected. He asked us to support him to accelerate the process.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
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

### qe_tanWin_2023_day22_t1:
* Name:	Day 22: Showdown at the Academy
* Description:	We finally learned Jochik Kaan's intentions. He sparked the flames of war to weaken the Chicuat defenses and steal the Baetyl from Tlapallan Academy, one of their key centers of learning. We must travel there at once, before it is too late.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Type:	Event
* EventId:	event_tanochWinter_2023_t1
* MailsOnCompletion:	m_tanWin_2023_d22_log
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_tanWin2023_Academy_t1

## QL_EVENT_TANOCHWINTER_2023_T2
### qe_tanWin_2023_day01_t2:
* Name:	We received priority communication from Lazarus Base. A subfaction of the Tanoch, the Chicuat, have made contact with Hiigaran representatives and requested aid. Fleet Command wants us to support the Chicuat and establish friendly ties. Our first task is to provide basic resources.

<color=#FBB03F>Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.</color>
* Description:	We received priority communication from Lazarus Base. A subfaction of the Tanoch, the Chicuat, have made contact with Hiigaran representatives and requested aid. Fleet Command wants us to support the Chicuat and establish friendly ties. Our first task is to provide basic resources.

<color=#FBB03F>Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.</color>
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

### qe_tanWin_2023_day02_t2:
* Name:	The Chicuat infrastructure is badly degraded with age and suffered heavy damage in recent attacks. We're asked to refine materials to support their restoration efforts.

<color=#FBB03F>Rare earths are an occasional by-product of refining. They are required for upgrading modules.</color>
* Description:	The Chicuat infrastructure is badly degraded with age and suffered heavy damage in recent attacks. We're asked to refine materials to support their restoration efforts.

<color=#FBB03F>Rare earths are an occasional by-product of refining. They are required for upgrading modules.</color>
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

### qe_tanWin_2023_day03_t2:
* Name:	The Chicuat have informed us several critical supply convoys have gone missing. We should try to retrieve any goods by hunting down local bandits.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
* Description:	The Chicuat have informed us several critical supply convoys have gone missing. We should try to retrieve any goods by hunting down local bandits.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
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

### qe_tanWin_2023_day04_t2:
* Name:	Ekekko, our Iyatequa liaison, has suggested to negotiate a trade deal with his contacts to support the Chicuat's need for basic supplies. We should sell some of our own items to get the traders interested.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
* Description:	Ekekko, our Iyatequa liaison, has suggested to negotiate a trade deal with his contacts to support the Chicuat's need for basic supplies. We should sell some of our own items to get the traders interested.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
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

### qe_tanWin_2023_day05_t2:
* Name:	We received emergency communication from the Chicuat Elders. They anticipate a raid on one of their remote trading stations. Toci asks us to take on the defense in order to relieve the weakened and overextended Chicuat forces.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Description:	We received emergency communication from the Chicuat Elders. They anticipate a raid on one of their remote trading stations. Toci asks us to take on the defense in order to relieve the weakened and overextended Chicuat forces.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Type:	Event
* EventId:	event_tanochWinter_2023_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_tanWin2023_DefendBase_t2

### qe_tanWin_2023_day06_t2:
* Name:	We must find out whether the Tecuban really are behind the recent attacks on the Chicuat. Our contact in the Tanoch Empire might be able to provide information. We should do some assignments to show good faith.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Description:	We must find out whether the Tecuban really are behind the recent attacks on the Chicuat. Our contact in the Tanoch Empire might be able to provide information. We should do some assignments to show good faith.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Type:	Event
* EventId:	event_tanochWinter_2023_t2
* MailsOnCompletion:	m_tanWin_2023_d06_log
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: Faction_Tanoch_T2up

### qe_tanWin_2023_day07_t2:
* Name:	Lazarus Base has processed Tepin Papan's information. There are reports about the rising influence of an ambitous leader named Heyoka. He is promoting expansionist ideas and has a particular disdain for the Chicuat. We should find out if the name is familiar in the criminal underworld here.

<color=#FBB03F>Some Tanoch fleets have broken away from the Tanoch empire to pursue their own agenda. These renegades can be found in signals, prowling Yaot space to continue ancient feuds.</color>
* Description:	Lazarus Base has processed Tepin Papan's information. There are reports about the rising influence of an ambitous leader named Heyoka. He is promoting expansionist ideas and has a particular disdain for the Chicuat. We should find out if the name is familiar in the criminal underworld here.

<color=#FBB03F>Some Tanoch fleets have broken away from the Tanoch empire to pursue their own agenda. These renegades can be found in signals, prowling Yaot space to continue ancient feuds.</color>
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

### qe_tanWin_2023_day08_t2:
* Name:	Our investigations produced evidence for contact between the Tecuban leader Heyoka and high profile criminals. We must hunt down these outlaws to learn more.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Description:	Our investigations produced evidence for contact between the Tecuban leader Heyoka and high profile criminals. We must hunt down these outlaws to learn more.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Type:	Event
* EventId:	event_tanochWinter_2023_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Epic_T2up
			* Mode: Generated

### qe_tanWin_2023_day09_t2:
* Name:	The Chicuat Elders have asked us to wait for their intelligence report on possible Tecuban forces within Acatla. In the meanwhile we should strengthen our forces to prepare for battle.

<color=#FBB03F>External modules, such as turrets or sensors, can be upgraded in the External Module screen which will increase their power. Upgrading one level costs credits and RE.</color>
* Description:	The Chicuat Elders have asked us to wait for their intelligence report on possible Tecuban forces within Acatla. In the meanwhile we should strengthen our forces to prepare for battle.

<color=#FBB03F>External modules, such as turrets or sensors, can be upgraded in the External Module screen which will increase their power. Upgrading one level costs credits and RE.</color>
* Type:	Event
* EventId:	event_tanochWinter_2023_t2
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Upgrade
			* Tags: External_Module_T1up
			* Amount: 1

### qe_tanWin_2023_day10_t2:
* Name:	Intelligence from the Chicuat points to a Tecuban base operating around an uninhabited planet. We must go there and eliminate this base to stop the raids.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Description:	Intelligence from the Chicuat points to a Tecuban base operating around an uninhabited planet. We must go there and eliminate this base to stop the raids.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Type:	Event
* EventId:	event_tanochWinter_2023_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_tanWin2023_AttackBase_t2

### qe_tanWin_2023_day11_t2:
* Name:	In order to gather information about the Vaygr's activity we must contact Tepin Papan once more. We should do some assignments to compensate him for his assistance.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Description:	In order to gather information about the Vaygr's activity we must contact Tepin Papan once more. We should do some assignments to compensate him for his assistance.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Type:	Event
* EventId:	event_tanochWinter_2023_t2
* MailsOnCompletion:	m_tanWin_2023_d11_log
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: RepTanoch
			* Amount: 135

### qe_tanWin_2023_day12_t2:
* Name:	While Tepin Papan is trying to gather information about the Vaygr's involvement with the Tecuban, we should scan some systems and see if we can find any clues about their whereabouts.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
* Description:	While Tepin Papan is trying to gather information about the Vaygr's involvement with the Tecuban, we should scan some systems and see if we can find any clues about their whereabouts.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
* Type:	Event
* EventId:	event_tanochWinter_2023_t2
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_T2up
			* Amount: 10
			* Analyzed: True

### qe_tanWin_2023_day13_t2:
* Name:	We hope to learn more about the Vaygr's activity from the local people. We should do some good deeds around here to gain their trust.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.</color>
* Description:	We hope to learn more about the Vaygr's activity from the local people. We should do some good deeds around here to gain their trust.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.</color>
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

### qe_tanWin_2023_day14_t2:
* Name:	Some local folks have agreed to provide information that could lead to the Vaygr. However, before they hand it over, they want us help them with a particularly challenging mission.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Description:	Some local folks have agreed to provide information that could lead to the Vaygr. However, before they hand it over, they want us help them with a particularly challenging mission.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Type:	Event
* EventId:	event_tanochWinter_2023_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Epic_T2up
			* Mode: Generated

### qe_tanWin_2023_day15_t2:
* Name:	We must hunt down a group of thugs that is suspected to be working for the Vaygr.

<color=#FBB03F>Some Tanoch fleets have broken away from the Tanoch empire to pursue their own agenda. These renegades can be found in signals, prowling Yaot space to continue ancient feuds.</color>
* Description:	We must hunt down a group of thugs that is suspected to be working for the Vaygr.

<color=#FBB03F>Some Tanoch fleets have broken away from the Tanoch empire to pursue their own agenda. These renegades can be found in signals, prowling Yaot space to continue ancient feuds.</color>
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

### qe_tanWin_2023_day16_t2:
* Name:	In our search for the Vaygr involved with the Tecuban, we aquired one of their communication frequencies. If we contact the Vaygr now, we should be able to trace their signal and hyper jump to their exact location.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Description:	In our search for the Vaygr involved with the Tecuban, we aquired one of their communication frequencies. If we contact the Vaygr now, we should be able to trace their signal and hyper jump to their exact location.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Type:	Event
* EventId:	event_tanochWinter_2023_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_tanWin2023_Relic_t2

### qe_tanWin_2023_day17_t2:
* Name:	There is still no answer from Tepin Papan since we last spoke with him. We should do some more assignments to gain his attention and see if he was able to gather any information about the Vaygr's intentions.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Description:	There is still no answer from Tepin Papan since we last spoke with him. We should do some more assignments to gain his attention and see if he was able to gather any information about the Vaygr's intentions.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Type:	Event
* EventId:	event_tanochWinter_2023_t2
* MailsOnCompletion:	m_tanWin_2023_d17_log
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: Faction_Tanoch_T2up

### qe_tanWin_2023_day18_t2:
* Name:	Ekekko wants us to trade on the local markets and see if we find someone who's willing to sell information on Jochik Kaan's motives.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
* Description:	Ekekko wants us to trade on the local markets and see if we find someone who's willing to sell information on Jochik Kaan's motives.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
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

### qe_tanWin_2023_day19_t2:
* Name:	We contacted the Chicuat Elders and told them about Jochik Kaan's possible intention to obtain a particular Progenitor object. They have given us intel about a criminal organization that deals with Progenitor objects within the Tanoch Empire. We should investigate.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Description:	We contacted the Chicuat Elders and told them about Jochik Kaan's possible intention to obtain a particular Progenitor object. They have given us intel about a criminal organization that deals with Progenitor objects within the Tanoch Empire. We should investigate.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Type:	Event
* EventId:	event_tanochWinter_2023_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Epic_T2up
			* Mode: Generated

### qe_tanWin_2023_day20_t2:
* Name:	While Gideon S'jet is researching the data set of Progenitor objects, the Chicuat Elders have informed us of a resurgance of Tecuban activity within their territory. We should support the defensive efforts.

<color=#FBB03F>Some Tanoch fleets have broken away from the Tanoch empire to pursue their own agenda. These renegades can be found in signals, prowling Yaot space to continue ancient feuds.</color>
* Description:	While Gideon S'jet is researching the data set of Progenitor objects, the Chicuat Elders have informed us of a resurgance of Tecuban activity within their territory. We should support the defensive efforts.

<color=#FBB03F>Some Tanoch fleets have broken away from the Tanoch empire to pursue their own agenda. These renegades can be found in signals, prowling Yaot space to continue ancient feuds.</color>
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

### qe_tanWin_2023_day21_t2:
* Name:	Gideon S'jet's research into the data set of Progenitor objects turned out more difficult than expected. He asked us to support him to accelerate the process.

<color=#FBB03F>Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.</color>
* Description:	Gideon S'jet's research into the data set of Progenitor objects turned out more difficult than expected. He asked us to support him to accelerate the process.

<color=#FBB03F>Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.</color>
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

### qe_tanWin_2023_day22_t2:
* Name:	We finally learned Jochik Kaan's intentions. He sparked the flames of war to weaken the Chicuat defenses and steal the Baetyl from Tlapallan Academy, one of their key centers of learning. We must travel there at once, before it is too late.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Description:	We finally learned Jochik Kaan's intentions. He sparked the flames of war to weaken the Chicuat defenses and steal the Baetyl from Tlapallan Academy, one of their key centers of learning. We must travel there at once, before it is too late.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Type:	Event
* EventId:	event_tanochWinter_2023_t2
* MailsOnCompletion:	m_tanWin_2023_d22_log
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_tanWin2023_Academy_t2

## QL_EVENT_TANOCHWINTER_2023_T3
### qe_tanWin_2023_day01_t3:
* Name:	We received priority communication from Lazarus Base. A subfaction of the Tanoch, the Chicuat, have made contact with Hiigaran representatives and requested aid. Fleet Command wants us to support the Chicuat and establish friendly ties. Our first task is to provide basic resources.

<color=#FBB03F>Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.</color>
* Description:	We received priority communication from Lazarus Base. A subfaction of the Tanoch, the Chicuat, have made contact with Hiigaran representatives and requested aid. Fleet Command wants us to support the Chicuat and establish friendly ties. Our first task is to provide basic resources.

<color=#FBB03F>Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.</color>
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

### qe_tanWin_2023_day02_t3:
* Name:	The Chicuat infrastructure is badly degraded with age and suffered heavy damage in recent attacks. We're asked to refine materials to support their restoration efforts.

<color=#FBB03F>Rare earths are an occasional by-product of refining. They are required for upgrading modules.</color>
* Description:	The Chicuat infrastructure is badly degraded with age and suffered heavy damage in recent attacks. We're asked to refine materials to support their restoration efforts.

<color=#FBB03F>Rare earths are an occasional by-product of refining. They are required for upgrading modules.</color>
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

### qe_tanWin_2023_day03_t3:
* Name:	The Chicuat have informed us several critical supply convoys have gone missing. We should try to retrieve any goods by hunting down local bandits.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
* Description:	The Chicuat have informed us several critical supply convoys have gone missing. We should try to retrieve any goods by hunting down local bandits.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
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

### qe_tanWin_2023_day04_t3:
* Name:	Ekekko, our Iyatequa liaison, has suggested to negotiate a trade deal with his contacts to support the Chicuat's need for basic supplies. We should sell some of our own items to get the traders interested.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
* Description:	Ekekko, our Iyatequa liaison, has suggested to negotiate a trade deal with his contacts to support the Chicuat's need for basic supplies. We should sell some of our own items to get the traders interested.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
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

### qe_tanWin_2023_day05_t3:
* Name:	We received emergency communication from the Chicuat Elders. They anticipate a raid on one of their remote trading stations. Toci asks us to take on the defense in order to relieve the weakened and overextended Chicuat forces.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Description:	We received emergency communication from the Chicuat Elders. They anticipate a raid on one of their remote trading stations. Toci asks us to take on the defense in order to relieve the weakened and overextended Chicuat forces.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Type:	Event
* EventId:	event_tanochWinter_2023_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_tanWin2023_DefendBase_t3

### qe_tanWin_2023_day06_t3:
* Name:	We must find out whether the Tecuban really are behind the recent attacks on the Chicuat. Our contact in the Tanoch Empire might be able to provide information. We should do some assignments to show good faith.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Description:	We must find out whether the Tecuban really are behind the recent attacks on the Chicuat. Our contact in the Tanoch Empire might be able to provide information. We should do some assignments to show good faith.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Type:	Event
* EventId:	event_tanochWinter_2023_t3
* MailsOnCompletion:	m_tanWin_2023_d06_log
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: Faction_Tanoch_T3up

### qe_tanWin_2023_day07_t3:
* Name:	Lazarus Base has processed Tepin Papan's information. There are reports about the rising influence of an ambitous leader named Heyoka. He is promoting expansionist ideas and has a particular disdain for the Chicuat. We should find out if the name is familiar in the criminal underworld here.

<color=#FBB03F>Some Tanoch fleets have broken away from the Tanoch empire to pursue their own agenda. These renegades can be found in signals, prowling Yaot space to continue ancient feuds.</color>
* Description:	Lazarus Base has processed Tepin Papan's information. There are reports about the rising influence of an ambitous leader named Heyoka. He is promoting expansionist ideas and has a particular disdain for the Chicuat. We should find out if the name is familiar in the criminal underworld here.

<color=#FBB03F>Some Tanoch fleets have broken away from the Tanoch empire to pursue their own agenda. These renegades can be found in signals, prowling Yaot space to continue ancient feuds.</color>
* Type:	Event
* EventId:	event_tanochWinter_2023_t3
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedTanochT3
				* ShipsDestroyedTanochT4
			* Amount: 10

### qe_tanWin_2023_day08_t3:
* Name:	Our investigations produced evidence for contact between the Tecuban leader Heyoka and high profile criminals. We must hunt down these outlaws to learn more.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Description:	Our investigations produced evidence for contact between the Tecuban leader Heyoka and high profile criminals. We must hunt down these outlaws to learn more.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Type:	Event
* EventId:	event_tanochWinter_2023_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Epic_T3up
			* Mode: Generated

### qe_tanWin_2023_day09_t3:
* Name:	The Chicuat Elders have asked us to wait for their intelligence report on possible Tecuban forces within Acatla. In the meanwhile we should strengthen our forces to prepare for battle.

<color=#FBB03F>External modules, such as turrets or sensors, can be upgraded in the External Module screen which will increase their power. Upgrading one level costs credits and RE.</color>
* Description:	The Chicuat Elders have asked us to wait for their intelligence report on possible Tecuban forces within Acatla. In the meanwhile we should strengthen our forces to prepare for battle.

<color=#FBB03F>External modules, such as turrets or sensors, can be upgraded in the External Module screen which will increase their power. Upgrading one level costs credits and RE.</color>
* Type:	Event
* EventId:	event_tanochWinter_2023_t3
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Upgrade
			* Tags: External_Module_T2up
			* Amount: 1

### qe_tanWin_2023_day10_t3:
* Name:	Intelligence from the Chicuat points to a Tecuban base operating around an uninhabited planet. We must go there and eliminate this base to stop the raids.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Description:	Intelligence from the Chicuat points to a Tecuban base operating around an uninhabited planet. We must go there and eliminate this base to stop the raids.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Type:	Event
* EventId:	event_tanochWinter_2023_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_tanWin2023_AttackBase_t3

### qe_tanWin_2023_day11_t3:
* Name:	In order to gather information about the Vaygr's activity we must contact Tepin Papan once more. We should do some assignments to compensate him for his assistance.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Description:	In order to gather information about the Vaygr's activity we must contact Tepin Papan once more. We should do some assignments to compensate him for his assistance.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Type:	Event
* EventId:	event_tanochWinter_2023_t3
* MailsOnCompletion:	m_tanWin_2023_d11_log
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: RepTanoch
			* Amount: 180

### qe_tanWin_2023_day12_t3:
* Name:	While Tepin Papan is trying to gather information about the Vaygr's involvement with the Tecuban, we should scan some systems and see if we can find any clues about their whereabouts.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
* Description:	While Tepin Papan is trying to gather information about the Vaygr's involvement with the Tecuban, we should scan some systems and see if we can find any clues about their whereabouts.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
* Type:	Event
* EventId:	event_tanochWinter_2023_t3
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_T3up
			* Amount: 10
			* Analyzed: True

### qe_tanWin_2023_day13_t3:
* Name:	We hope to learn more about the Vaygr's activity from the local people. We should do some good deeds around here to gain their trust.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.</color>
* Description:	We hope to learn more about the Vaygr's activity from the local people. We should do some good deeds around here to gain their trust.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.</color>
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

### qe_tanWin_2023_day14_t3:
* Name:	Some local folks have agreed to provide information that could lead to the Vaygr. However, before they hand it over, they want us help them with a particularly challenging mission.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Description:	Some local folks have agreed to provide information that could lead to the Vaygr. However, before they hand it over, they want us help them with a particularly challenging mission.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Type:	Event
* EventId:	event_tanochWinter_2023_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Epic_T3up
			* Mode: Generated

### qe_tanWin_2023_day15_t3:
* Name:	We must hunt down a group of thugs that is suspected to be working for the Vaygr.

<color=#FBB03F>Some Tanoch fleets have broken away from the Tanoch empire to pursue their own agenda. These renegades can be found in signals, prowling Yaot space to continue ancient feuds.</color>
* Description:	We must hunt down a group of thugs that is suspected to be working for the Vaygr.

<color=#FBB03F>Some Tanoch fleets have broken away from the Tanoch empire to pursue their own agenda. These renegades can be found in signals, prowling Yaot space to continue ancient feuds.</color>
* Type:	Event
* EventId:	event_tanochWinter_2023_t3
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedTanochT3
				* ShipsDestroyedTanochT4
			* Amount: 10

### qe_tanWin_2023_day16_t3:
* Name:	In our search for the Vaygr involved with the Tecuban, we aquired one of their communication frequencies. If we contact the Vaygr now, we should be able to trace their signal and hyper jump to their exact location.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Description:	In our search for the Vaygr involved with the Tecuban, we aquired one of their communication frequencies. If we contact the Vaygr now, we should be able to trace their signal and hyper jump to their exact location.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Type:	Event
* EventId:	event_tanochWinter_2023_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_tanWin2023_Relic_t3

### qe_tanWin_2023_day17_t3:
* Name:	There is still no answer from Tepin Papan since we last spoke with him. We should do some more assignments to gain his attention and see if he was able to gather any information about the Vaygr's intentions.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Description:	There is still no answer from Tepin Papan since we last spoke with him. We should do some more assignments to gain his attention and see if he was able to gather any information about the Vaygr's intentions.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Type:	Event
* EventId:	event_tanochWinter_2023_t3
* MailsOnCompletion:	m_tanWin_2023_d17_log
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: Faction_Tanoch_T3up

### qe_tanWin_2023_day18_t3:
* Name:	Ekekko wants us to trade on the local markets and see if we find someone who's willing to sell information on Jochik Kaan's motives.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
* Description:	Ekekko wants us to trade on the local markets and see if we find someone who's willing to sell information on Jochik Kaan's motives.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
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

### qe_tanWin_2023_day19_t3:
* Name:	We contacted the Chicuat Elders and told them about Jochik Kaan's possible intention to obtain a particular Progenitor object. They have given us intel about a criminal organization that deals with Progenitor objects within the Tanoch Empire. We should investigate.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Description:	We contacted the Chicuat Elders and told them about Jochik Kaan's possible intention to obtain a particular Progenitor object. They have given us intel about a criminal organization that deals with Progenitor objects within the Tanoch Empire. We should investigate.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Type:	Event
* EventId:	event_tanochWinter_2023_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Epic_T3up
			* Mode: Generated

### qe_tanWin_2023_day20_t3:
* Name:	While Gideon S'jet is researching the data set of Progenitor objects, the Chicuat Elders have informed us of a resurgance of Tecuban activity within their territory. We should support the defensive efforts.

<color=#FBB03F>Some Tanoch fleets have broken away from the Tanoch empire to pursue their own agenda. These renegades can be found in signals, prowling Yaot space to continue ancient feuds.</color>
* Description:	While Gideon S'jet is researching the data set of Progenitor objects, the Chicuat Elders have informed us of a resurgance of Tecuban activity within their territory. We should support the defensive efforts.

<color=#FBB03F>Some Tanoch fleets have broken away from the Tanoch empire to pursue their own agenda. These renegades can be found in signals, prowling Yaot space to continue ancient feuds.</color>
* Type:	Event
* EventId:	event_tanochWinter_2023_t3
* Goals:
	* 0:
		* GoalType: Statistic
			* Ids:
				* ShipsDestroyedTanochT3
				* ShipsDestroyedTanochT4
			* Amount: 10

### qe_tanWin_2023_day21_t3:
* Name:	Gideon S'jet's research into the data set of Progenitor objects turned out more difficult than expected. He asked us to support him to accelerate the process.

<color=#FBB03F>Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.</color>
* Description:	Gideon S'jet's research into the data set of Progenitor objects turned out more difficult than expected. He asked us to support him to accelerate the process.

<color=#FBB03F>Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.</color>
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

### qe_tanWin_2023_day22_t3:
* Name:	We finally learned Jochik Kaan's intentions. He sparked the flames of war to weaken the Chicuat defenses and steal the Baetyl from Tlapallan Academy, one of their key centers of learning. We must travel there at once, before it is too late.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Description:	We finally learned Jochik Kaan's intentions. He sparked the flames of war to weaken the Chicuat defenses and steal the Baetyl from Tlapallan Academy, one of their key centers of learning. We must travel there at once, before it is too late.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Type:	Event
* EventId:	event_tanochWinter_2023_t3
* MailsOnCompletion:	m_tanWin_2023_d22_log
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_tanWin2023_Academy_t3

## QL_EVENT_TANOCHWINTER_2023_T4
### qe_tanWin_2023_day01_t4:
* Name:	We received priority communication from Lazarus Base. A subfaction of the Tanoch, the Chicuat, have made contact with Hiigaran representatives and requested aid. Fleet Command wants us to support the Chicuat and establish friendly ties. Our first task is to provide basic resources.

<color=#FBB03F>Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.</color>
* Description:	We received priority communication from Lazarus Base. A subfaction of the Tanoch, the Chicuat, have made contact with Hiigaran representatives and requested aid. Fleet Command wants us to support the Chicuat and establish friendly ties. Our first task is to provide basic resources.

<color=#FBB03F>Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.</color>
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

### qe_tanWin_2023_day02_t4:
* Name:	The Chicuat infrastructure is badly degraded with age and suffered heavy damage in recent attacks. We're asked to refine materials to support their restoration efforts.

<color=#FBB03F>Rare earths are an occasional by-product of refining. They are required for upgrading modules.</color>
* Description:	The Chicuat infrastructure is badly degraded with age and suffered heavy damage in recent attacks. We're asked to refine materials to support their restoration efforts.

<color=#FBB03F>Rare earths are an occasional by-product of refining. They are required for upgrading modules.</color>
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

### qe_tanWin_2023_day03_t4:
* Name:	The Chicuat have informed us several critical supply convoys have gone missing. We should try to retrieve any goods by hunting down local bandits.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
* Description:	The Chicuat have informed us several critical supply convoys have gone missing. We should try to retrieve any goods by hunting down local bandits.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
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

### qe_tanWin_2023_day04_t4:
* Name:	Ekekko, our Iyatequa liaison, has suggested to negotiate a trade deal with his contacts to support the Chicuat's need for basic supplies. We should sell some of our own items to get the traders interested.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
* Description:	Ekekko, our Iyatequa liaison, has suggested to negotiate a trade deal with his contacts to support the Chicuat's need for basic supplies. We should sell some of our own items to get the traders interested.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
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

### qe_tanWin_2023_day05_t4:
* Name:	We received emergency communication from the Chicuat Elders. They anticipate a raid on one of their remote trading stations. Toci asks us to take on the defense in order to relieve the weakened and overextended Chicuat forces.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Description:	We received emergency communication from the Chicuat Elders. They anticipate a raid on one of their remote trading stations. Toci asks us to take on the defense in order to relieve the weakened and overextended Chicuat forces.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Type:	Event
* EventId:	event_tanochWinter_2023_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_tanWin2023_DefendBase_t4

### qe_tanWin_2023_day06_t4:
* Name:	We must find out whether the Tecuban really are behind the recent attacks on the Chicuat. Our contact in the Tanoch Empire might be able to provide information. We should do some assignments to show good faith.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Description:	We must find out whether the Tecuban really are behind the recent attacks on the Chicuat. Our contact in the Tanoch Empire might be able to provide information. We should do some assignments to show good faith.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Type:	Event
* EventId:	event_tanochWinter_2023_t4
* MailsOnCompletion:	m_tanWin_2023_d06_log
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: Faction_Tanoch_T4up

### qe_tanWin_2023_day07_t4:
* Name:	Lazarus Base has processed Tepin Papan's information. There are reports about the rising influence of an ambitous leader named Heyoka. He is promoting expansionist ideas and has a particular disdain for the Chicuat. We should find out if the name is familiar in the criminal underworld here.

<color=#FBB03F>Some Tanoch fleets have broken away from the Tanoch empire to pursue their own agenda. These renegades can be found in signals, prowling Yaot space to continue ancient feuds.</color>
* Description:	Lazarus Base has processed Tepin Papan's information. There are reports about the rising influence of an ambitous leader named Heyoka. He is promoting expansionist ideas and has a particular disdain for the Chicuat. We should find out if the name is familiar in the criminal underworld here.

<color=#FBB03F>Some Tanoch fleets have broken away from the Tanoch empire to pursue their own agenda. These renegades can be found in signals, prowling Yaot space to continue ancient feuds.</color>
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

### qe_tanWin_2023_day08_t4:
* Name:	Our investigations produced evidence for contact between the Tecuban leader Heyoka and high profile criminals. We must hunt down these outlaws to learn more.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Description:	Our investigations produced evidence for contact between the Tecuban leader Heyoka and high profile criminals. We must hunt down these outlaws to learn more.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Type:	Event
* EventId:	event_tanochWinter_2023_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Epic_T4up
			* Mode: Generated

### qe_tanWin_2023_day09_t4:
* Name:	The Chicuat Elders have asked us to wait for their intelligence report on possible Tecuban forces within Acatla. In the meanwhile we should strengthen our forces to prepare for battle.

<color=#FBB03F>External modules, such as turrets or sensors, can be upgraded in the External Module screen which will increase their power. Upgrading one level costs credits and RE.</color>
* Description:	The Chicuat Elders have asked us to wait for their intelligence report on possible Tecuban forces within Acatla. In the meanwhile we should strengthen our forces to prepare for battle.

<color=#FBB03F>External modules, such as turrets or sensors, can be upgraded in the External Module screen which will increase their power. Upgrading one level costs credits and RE.</color>
* Type:	Event
* EventId:	event_tanochWinter_2023_t4
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Upgrade
			* Tags: External_Module_T3up
			* Amount: 1

### qe_tanWin_2023_day10_t4:
* Name:	Intelligence from the Chicuat points to a Tecuban base operating around an uninhabited planet. We must go there and eliminate this base to stop the raids.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Description:	Intelligence from the Chicuat points to a Tecuban base operating around an uninhabited planet. We must go there and eliminate this base to stop the raids.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Type:	Event
* EventId:	event_tanochWinter_2023_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_tanWin2023_AttackBase_t4

### qe_tanWin_2023_day11_t4:
* Name:	In order to gather information about the Vaygr's activity we must contact Tepin Papan once more. We should do some assignments to compensate him for his assistance.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Description:	In order to gather information about the Vaygr's activity we must contact Tepin Papan once more. We should do some assignments to compensate him for his assistance.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Type:	Event
* EventId:	event_tanochWinter_2023_t4
* MailsOnCompletion:	m_tanWin_2023_d11_log
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: RepTanoch
			* Amount: 225

### qe_tanWin_2023_day12_t4:
* Name:	While Tepin Papan is trying to gather information about the Vaygr's involvement with the Tecuban, we should scan some systems and see if we can find any clues about their whereabouts.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
* Description:	While Tepin Papan is trying to gather information about the Vaygr's involvement with the Tecuban, we should scan some systems and see if we can find any clues about their whereabouts.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
* Type:	Event
* EventId:	event_tanochWinter_2023_t4
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_T4up
			* Amount: 10
			* Analyzed: True

### qe_tanWin_2023_day13_t4:
* Name:	We hope to learn more about the Vaygr's activity from the local people. We should do some good deeds around here to gain their trust.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.</color>
* Description:	We hope to learn more about the Vaygr's activity from the local people. We should do some good deeds around here to gain their trust.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.</color>
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

### qe_tanWin_2023_day14_t4:
* Name:	Some local folks have agreed to provide information that could lead to the Vaygr. However, before they hand it over, they want us help them with a particularly challenging mission.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Description:	Some local folks have agreed to provide information that could lead to the Vaygr. However, before they hand it over, they want us help them with a particularly challenging mission.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Type:	Event
* EventId:	event_tanochWinter_2023_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Epic_T4up
			* Mode: Generated

### qe_tanWin_2023_day15_t4:
* Name:	We must hunt down a group of thugs that is suspected to be working for the Vaygr.

<color=#FBB03F>Some Tanoch fleets have broken away from the Tanoch empire to pursue their own agenda. These renegades can be found in signals, prowling Yaot space to continue ancient feuds.</color>
* Description:	We must hunt down a group of thugs that is suspected to be working for the Vaygr.

<color=#FBB03F>Some Tanoch fleets have broken away from the Tanoch empire to pursue their own agenda. These renegades can be found in signals, prowling Yaot space to continue ancient feuds.</color>
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

### qe_tanWin_2023_day16_t4:
* Name:	In our search for the Vaygr involved with the Tecuban, we aquired one of their communication frequencies. If we contact the Vaygr now, we should be able to trace their signal and hyper jump to their exact location.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Description:	In our search for the Vaygr involved with the Tecuban, we aquired one of their communication frequencies. If we contact the Vaygr now, we should be able to trace their signal and hyper jump to their exact location.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Type:	Event
* EventId:	event_tanochWinter_2023_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_tanWin2023_Relic_t4

### qe_tanWin_2023_day17_t4:
* Name:	There is still no answer from Tepin Papan since we last spoke with him. We should do some more assignments to gain his attention and see if he was able to gather any information about the Vaygr's intentions.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Description:	There is still no answer from Tepin Papan since we last spoke with him. We should do some more assignments to gain his attention and see if he was able to gather any information about the Vaygr's intentions.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Type:	Event
* EventId:	event_tanochWinter_2023_t4
* MailsOnCompletion:	m_tanWin_2023_d17_log
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: Faction_Tanoch_T4up

### qe_tanWin_2023_day18_t4:
* Name:	Ekekko wants us to trade on the local markets and see if we find someone who's willing to sell information on Jochik Kaan's motives.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
* Description:	Ekekko wants us to trade on the local markets and see if we find someone who's willing to sell information on Jochik Kaan's motives.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
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

### qe_tanWin_2023_day19_t4:
* Name:	We contacted the Chicuat Elders and told them about Jochik Kaan's possible intention to obtain a particular Progenitor object. They have given us intel about a criminal organization that deals with Progenitor objects within the Tanoch Empire. We should investigate.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Description:	We contacted the Chicuat Elders and told them about Jochik Kaan's possible intention to obtain a particular Progenitor object. They have given us intel about a criminal organization that deals with Progenitor objects within the Tanoch Empire. We should investigate.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Type:	Event
* EventId:	event_tanochWinter_2023_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Epic_T4up
			* Mode: Generated

### qe_tanWin_2023_day20_t4:
* Name:	While Gideon S'jet is researching the data set of Progenitor objects, the Chicuat Elders have informed us of a resurgance of Tecuban activity within their territory. We should support the defensive efforts.

<color=#FBB03F>Some Tanoch fleets have broken away from the Tanoch empire to pursue their own agenda. These renegades can be found in signals, prowling Yaot space to continue ancient feuds.</color>
* Description:	While Gideon S'jet is researching the data set of Progenitor objects, the Chicuat Elders have informed us of a resurgance of Tecuban activity within their territory. We should support the defensive efforts.

<color=#FBB03F>Some Tanoch fleets have broken away from the Tanoch empire to pursue their own agenda. These renegades can be found in signals, prowling Yaot space to continue ancient feuds.</color>
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

### qe_tanWin_2023_day21_t4:
* Name:	Gideon S'jet's research into the data set of Progenitor objects turned out more difficult than expected. He asked us to support him to accelerate the process.

<color=#FBB03F>Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.</color>
* Description:	Gideon S'jet's research into the data set of Progenitor objects turned out more difficult than expected. He asked us to support him to accelerate the process.

<color=#FBB03F>Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.</color>
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

### qe_tanWin_2023_day22_t4:
* Name:	We finally learned Jochik Kaan's intentions. He sparked the flames of war to weaken the Chicuat defenses and steal the Baetyl from Tlapallan Academy, one of their key centers of learning. We must travel there at once, before it is too late.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Description:	We finally learned Jochik Kaan's intentions. He sparked the flames of war to weaken the Chicuat defenses and steal the Baetyl from Tlapallan Academy, one of their key centers of learning. We must travel there at once, before it is too late.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Type:	Event
* EventId:	event_tanochWinter_2023_t4
* MailsOnCompletion:	m_tanWin_2023_d22_log
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_tanWin2023_Academy_t4

## QL_EVENT_YAOTSPRING_2024_T1
### qe_yaoSpr_2024_day01_t1:
* Name:	There are rumors circulating in the Empty Quarter about an increase in Cangacian pirate activity. Fleet Command asks us to gather intel from our contacts with the Iyatequa traders. We should gain some favors to bargain for information.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Description:	There are rumors circulating in the Empty Quarter about an increase in Cangacian pirate activity. Fleet Command asks us to gather intel from our contacts with the Iyatequa traders. We should gain some favors to bargain for information.

<color=#FBB03F>There are different types of assignments available in your assignment log.</color>
* Type:	Event
* EventId:	event_yaotSpring_2024_t1
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: T1up

### qe_yaoSpr_2024_day02_t1:
* Name:	The Iyatequa traders are involved with pirates attacking Yaot pilgrims in the Empty Quarter. We might get more information through selling equipment and arms on the open market.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
* Description:	The Iyatequa traders are involved with pirates attacking Yaot pilgrims in the Empty Quarter. We might get more information through selling equipment and arms on the open market.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
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

### qe_yaoSpr_2024_day03_t1:
* Name:	To learn more about the pirate raids, we should get in contact with the Yaot pilgrims. They appear to be hiding after recent attacks. We have no other option than to perform reconnaissance in the nearby systems.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
* Description:	To learn more about the pirate raids, we should get in contact with the Yaot pilgrims. They appear to be hiding after recent attacks. We have no other option than to perform reconnaissance in the nearby systems.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
* Type:	Event
* EventId:	event_yaotSpring_2024_t1
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_T1up
			* Amount: 5
			* Analyzed: True

### qe_yaoSpr_2024_day04_t1:
* Name:	In our search for the Yaot pilgrims we have encountered intense pirate activity. We should hunt down some of their ships and see if we can gather any additional clues.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
* Description:	In our search for the Yaot pilgrims we have encountered intense pirate activity. We should hunt down some of their ships and see if we can gather any additional clues.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
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

### qe_yaoSpr_2024_day05_t1:
* Name:	Some Yaot survivors in our medical ward are ready to be questioned. If we manage to prove our good intentions they might help us find the Yaot pilgrimage.

<color=#FBB03F>Prestige is earned through each player level-up and by completing daily and weekly assignments.</color>
* Description:	Some Yaot survivors in our medical ward are ready to be questioned. If we manage to prove our good intentions they might help us find the Yaot pilgrimage.

<color=#FBB03F>Prestige is earned through each player level-up and by completing daily and weekly assignments.</color>
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

### qe_yaoSpr_2024_day06_t1:
* Name:	The Yaot have accepted our offer to support their pilgrimage. Requests have come in from ships needing spares and replacement parts for repairs. If we provide these, we might learn more about why the pirates are after these ships.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
* Description:	The Yaot have accepted our offer to support their pilgrimage. Requests have come in from ships needing spares and replacement parts for repairs. If we provide these, we might learn more about why the pirates are after these ships.

<color=#FBB03F>Small items such as strike craft, modules and parts can be built in the fabricator. Larger items such as escort ships and flagships must be constructed at shipyards provided at larger stations.</color>
* Type:	Event
* EventId:	event_yaotSpring_2024_t1
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: T1up
			* Amount: 1

### qe_yaoSpr_2024_day07_t1:
* Name:	Even though pirates are still swarming the area, Chocoan and the Yaot pilgrims are adamant about continuing their travels to see the astral conjunction events. In order to deter any further attacks on the civilian ships, we should patrol and clear the systems of any significant hostile forces.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Description:	Even though pirates are still swarming the area, Chocoan and the Yaot pilgrims are adamant about continuing their travels to see the astral conjunction events. In order to deter any further attacks on the civilian ships, we should patrol and clear the systems of any significant hostile forces.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Type:	Event
* EventId:	event_yaotSpring_2024_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Rare_T1up
			* Mode: Generated

### qe_yaoSpr_2024_day08_t1:
* Name:	Even the Fleet of Rams are after the Yaot pilgrim's supposed treasure. If we hope to protect them, we must first convince somebody to give us more information. We should try to make friends with the pilgrims and get somebody to talk.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from dismissing officers and are earned through completing signals.</color>
* Description:	Even the Fleet of Rams are after the Yaot pilgrim's supposed treasure. If we hope to protect them, we must first convince somebody to give us more information. We should try to make friends with the pilgrims and get somebody to talk.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from dismissing officers and are earned through completing signals.</color>
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

### qe_yaoSpr_2024_day09_t1:
* Name:	After talking to Chocoan we suspect there is more to the Yaot pilgrimage than the religious travels to astral conjunction events. We might be able to get more information from the Yaot Federation if we do some favors.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Description:	After talking to Chocoan, we suspect there is more to the Yaot pilgrimage than the religious travels to astral conjunction events. We might be able to get more information from the Yaot Federation if we do some favors.

<color=#FBB03F>There are different types of assignments available in your assignment log.</color>
* Type:	Event
* EventId:	event_yaotSpring_2024_t1
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: T1up

### qe_yaoSpr_2024_day10_t1:
* Name:	We’ve reached a dead end on collecting intelligence on the Yaot, but our source within the Tanoch Empire has offered to provide more information. We should bring an adequate gift for compensation.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
* Description:	We’ve reached a dead end on collecting intelligence on the Yaot, but our source within the Tanoch Empire has offered to provide more information. We should bring an adequate gift for compensation.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
* Type:	Event
* EventId:	event_yaotSpring_2024_t1
* Goals:
	* 0:
		* GoalType: Pay
			* Id: questItem_progenitorRelic_t1
			* Amount: 1

### qe_yaoSpr_2024_day11_t1:
* Name:	While we still don't know what kind of treasure the pilgrims could have aboard their vessels, Chocoan wants to move on to another astral conjunction event. He has requested our assistance in clearing out the area from any hostile threats.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Description:	While we still don't know what kind of treasure the pilgrims could have aboard their vessels, Chocoan wants to move on to another astral conjunction event. He has requested our assistance in clearing out the area from any hostile threats.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Type:	Event
* EventId:	event_yaotSpring_2024_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Rare_T1up
			* Mode: Generated

### qe_yaoSpr_2024_day12_t1:
* Name:	The report on the pilgrim's procedure has been fully analyzed. Usually the pilgrim's convoy moves in a tight line formation towards the optimal conjunction points where they perform their religious rituals. However, a few ships regularly diverge from the common path and move into nearby asteroid fields. We should investigate the latest conjunction site and see if we can find anything of interest.

<color=#FBB03F>Ore can be mined from asteroids in asteroid fields. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
* Description:	The report on the pilgrim's procedure has been fully analyzed. Usually the pilgrim's convoy moves in a tight line formation towards the optimal conjunction points where they perform their religious rituals. However, a few ships regularly diverge from the common path and move into nearby asteroid fields. We should investigate the latest conjunction site and see if we can find anything of interest.

<color=#FBB03F>Ore can be mined from asteroids in asteroid fields. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
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

### qe_yaoSpr_2024_day13_t1:
* Name:	Chocoan has informed us that the next astral conjunction site will be inside the Cangacian territories. We convinced him to take part in the operation ourselves to ensure security in this hostile area of the Empty Quarter. Maybe we will be able to both protect the pilgrims and find out more about the suspected secret agenda. We should make sure the crew is properly prepared and ready for any eventualities.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* Description:	Chocoan has informed us that the next astral conjunction site will be inside the Cangacian territories. We convinced him to take part in the operation ourselves to ensure security in this hostile area of the Empty Quarter. Maybe we will be able to both protect the pilgrims and find out more about the suspected secret agenda. We should make sure the crew is properly prepared and ready for any eventualities.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* Type:	Event
* EventId:	event_yaotSpring_2024_t1
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 1

### qe_yaoSpr_2024_day14_t1:
* Name:	Chocoan has provided the coordinates to the next astral conjunction event. Strong hostile forces are to be expected in this system. Our goal is to both protect the civilian pilgrims and find out more about the suspected secret agenda of the Yaot Elders.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Description:	Chocoan has provided the coordinates to the next astral conjunction event. Strong hostile forces are to be expected in this system. Our goal is to both protect the civilian pilgrims and find out more about the suspected secret agenda of the Yaot Elders.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Type:	Event
* EventId:	event_yaotSpring_2024_t1
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_yaoSpr2024_Conjunction_t1

## QL_EVENT_YAOTSPRING_2024_T2
### qe_yaoSpr_2024_day01_t2:
* Name:	There are rumors circulating in the Empty Quarter about an increase in Cangacian pirate activity. Fleet Command asks us to gather intel from our contacts with the Iyatequa traders. We should gain some favors to bargain for information.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Description:	There are rumors circulating in the Empty Quarter about an increase in Cangacian pirate activity. Fleet Command asks us to gather intel from our contacts with the Iyatequa traders. We should gain some favors to bargain for information.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Type:	Event
* EventId:	event_yaotSpring_2024_t2
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: Faction_Tr1_T2up

### qe_yaoSpr_2024_day02_t2:
* Name:	The Iyatequa traders are involved with pirates attacking Yaot pilgrims in the Empty Quarter. We might get more information through selling equipment and arms on the open market.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
* Description:	The Iyatequa traders are involved with pirates attacking Yaot pilgrims in the Empty Quarter. We might get more information through selling equipment and arms on the open market.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
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

### qe_yaoSpr_2024_day03_t2:
* Name:	To learn more about the pirate raids, we should get in contact with the Yaot pilgrims. They appear to be hiding after recent attacks. We have no other option than to perform reconnaissance in the nearby systems.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
* Description:	To learn more about the pirate raids, we should get in contact with the Yaot pilgrims. They appear to be hiding after recent attacks. We have no other option than to perform reconnaissance in the nearby systems.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
* Type:	Event
* EventId:	event_yaotSpring_2024_t2
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_T2up
			* Amount: 5
			* Analyzed: True

### qe_yaoSpr_2024_day04_t2:
* Name:	In our search for the Yaot pilgrims we have encountered intense pirate activity. We should hunt down some of their ships and see if we can gather any additional clues.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
* Description:	In our search for the Yaot pilgrims we have encountered intense pirate activity. We should hunt down some of their ships and see if we can gather any additional clues.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
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

### qe_yaoSpr_2024_day05_t2:
* Name:	Some Yaot survivors in our medical ward are ready to be questioned. If we manage to prove our good intentions they might help us find the Yaot pilgrimage.

<color=#FBB03F>Prestige is earned through each player level-up and by completing daily and weekly assignments.</color>
* Description:	Some Yaot survivors in our medical ward are ready to be questioned. If we manage to prove our good intentions they might help us find the Yaot pilgrimage.

<color=#FBB03F>Prestige is earned through each player level-up and by completing daily and weekly assignments.</color>
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

### qe_yaoSpr_2024_day06_t2:
* Name:	The Yaot have accepted our offer to support their pilgrimage. Requests have come in from ships needing spares and replacement parts for repairs. If we provide these, we might learn more about why the pirates are after these ships.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
* Description:	The Yaot have accepted our offer to support their pilgrimage. Requests have come in from ships needing spares and replacement parts for repairs. If we provide these, we might learn more about why the pirates are after these ships.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
* Type:	Event
* EventId:	event_yaotSpring_2024_t2
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: Part_T2up
			* Amount: 100

### qe_yaoSpr_2024_day07_t2:
* Name:	Even though pirates are still swarming the area, Chocoan and the Yaot pilgrims are adamant about continuing their travels to see the astral conjunction events. In order to deter any further attacks on the civilian ships, we should patrol and clear the systems of any significant hostile forces.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Description:	Even though pirates are still swarming the area, Chocoan and the Yaot pilgrims are adamant about continuing their travels to see the astral conjunction events. In order to deter any further attacks on the civilian ships, we should patrol and clear the systems of any significant hostile forces.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Type:	Event
* EventId:	event_yaotSpring_2024_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Epic_T2up
			* Mode: Generated

### qe_yaoSpr_2024_day08_t2:
* Name:	Even the Fleet of Rams are after the Yaot pilgrim's supposed treasure. If we hope to protect them, we must first convince somebody to give us more information. We should try to make friends with the pilgrims and get somebody to talk.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from dismissing officers and are earned through completing signals.</color>
* Description:	Even the Fleet of Rams are after the Yaot pilgrim's supposed treasure. If we hope to protect them, we must first convince somebody to give us more information. We should try to make friends with the pilgrims and get somebody to talk.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from dismissing officers and are earned through completing signals.</color>
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

### qe_yaoSpr_2024_day09_t2:
* Name:	After talking to Chocoan we suspect there is more to the Yaot pilgrimage than the religious travels to astral conjunction events. We might be able to get more information from the Yaot Federation if we do some favors.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Description:	After talking to Chocoan we suspect there is more to the Yaot pilgrimage than the religious travels to astral conjunction events. We might be able to get more information from the Yaot Federation if we do some favors.

<color=#FBB03F>There are different types of assignments available in your assignment log.</color>
* Type:	Event
* EventId:	event_yaotSpring_2024_t2
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: T2up

### qe_yaoSpr_2024_day10_t2:
* Name:	We’ve reached a dead end on collecting intelligence on the Yaot, but our source within the Tanoch Empire has offered to provide more information. We should bring an adequate gift for compensation.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
* Description:	We’ve reached a dead end on collecting intelligence on the Yaot, but our source within the Tanoch Empire has offered to provide more information. We should bring an adequate gift for compensation.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
* Type:	Event
* EventId:	event_yaotSpring_2024_t2
* Goals:
	* 0:
		* GoalType: Pay
			* Id: questItem_progenitorRelic_t2
			* Amount: 1

### qe_yaoSpr_2024_day11_t2:
* Name:	While we still don't know what kind of treasure the pilgrims could have aboard their vessels, Chocoan wants to move on to another astral conjunction event. He has requested our assistance in clearing out the area from any hostile threats.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Description:	While we still don't know what kind of treasure the pilgrims could have aboard their vessels, Chocoan wants to move on to another astral conjunction event. He has requested our assistance in clearing out the area from any hostile threats.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Type:	Event
* EventId:	event_yaotSpring_2024_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Epic_T2up
			* Mode: Generated

### qe_yaoSpr_2024_day12_t2:
* Name:	The report on the pilgrim's procedure has been fully analyzed. Usually the pilgrim's convoy moves in a tight line formation towards the optimal conjunction points where they perform their religious rituals. However, a few ships regularly diverge from the common path and move into nearby asteroid fields. We should investigate the latest conjunction site and see if we can find anything of interest.

<color=#FBB03F>Ore can be mined from asteroids in asteroid fields. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
* Description:	The report on the pilgrim's procedure has been fully analyzed. Usually the pilgrim's convoy moves in a tight line formation towards the optimal conjunction points where they perform their religious rituals. However, a few ships regularly diverge from the common path and move into nearby asteroid fields. We should investigate the latest conjunction site and see if we can find anything of interest.

<color=#FBB03F>Ore can be mined from asteroids in asteroid fields. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
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

### qe_yaoSpr_2024_day13_t2:
* Name:	Chocoan has informed us that the next astral conjunction site will be inside the Cangacian territories. We convinced him to take part in the operation ourselves to ensure security in this hostile area of the Empty Quarter. Maybe we will be able to both protect the pilgrims and find out more about the suspected secret agenda. We should make sure the crew is properly prepared and ready for any eventualities.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* Description:	Chocoan has informed us that the next astral conjunction site will be inside the Cangacian territories. We convinced him to take part in the operation ourselves to ensure security in this hostile area of the Empty Quarter. Maybe we will be able to both protect the pilgrims and find out more about the suspected secret agenda. We should make sure the crew is properly prepared and ready for any eventualities.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* Type:	Event
* EventId:	event_yaotSpring_2024_t2
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 2

### qe_yaoSpr_2024_day14_t2:
* Name:	Chocoan has provided the coordinates to the next astral conjunction event. Strong hostile forces are to be expected in this system. Our goal is to both protect the civilian pilgrims and find out more about the suspected secret agenda of the Yaot Elders.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Description:	Chocoan has provided the coordinates to the next astral conjunction event. Strong hostile forces are to be expected in this system. Our goal is to both protect the civilian pilgrims and find out more about the suspected secret agenda of the Yaot Elders.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Type:	Event
* EventId:	event_yaotSpring_2024_t2
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_yaoSpr2024_Conjunction_t2

## QL_EVENT_YAOTSPRING_2024_T3
### qe_yaoSpr_2024_day01_t3:
* Name:	There are rumors circulating in the Empty Quarter about an increase in Cangacian pirate activity. Fleet Command asks us to gather intel from our contacts with the Iyatequa traders. We should gain some favors to bargain for information.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Description:	There are rumors circulating in the Empty Quarter about an increase in Cangacian pirate activity. Fleet Command asks us to gather intel from our contacts with the Iyatequa traders. We should gain some favors to bargain for information.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Type:	Event
* EventId:	event_yaotSpring_2024_t3
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: Faction_Tr1_T3up

### qe_yaoSpr_2024_day02_t3:
* Name:	The Iyatequa traders are involved with pirates attacking Yaot pilgrims in the Empty Quarter. We might get more information through selling equipment and arms on the open market.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
* Description:	The Iyatequa traders are involved with pirates attacking Yaot pilgrims in the Empty Quarter. We might get more information through selling equipment and arms on the open market.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
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

### qe_yaoSpr_2024_day03_t3:
* Name:	To learn more about the pirate raids, we should get in contact with the Yaot pilgrims. They appear to be hiding after recent attacks. We have no other option than to perform reconnaissance in the nearby systems.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
* Description:	To learn more about the pirate raids, we should get in contact with the Yaot pilgrims. They appear to be hiding after recent attacks. We have no other option than to perform reconnaissance in the nearby systems.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
* Type:	Event
* EventId:	event_yaotSpring_2024_t3
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_T3up
			* Amount: 5
			* Analyzed: True

### qe_yaoSpr_2024_day04_t3:
* Name:	In our search for the Yaot pilgrims we have encountered intense pirate activity. We should hunt down some of their ships and see if we can gather any additional clues.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
* Description:	In our search for the Yaot pilgrims we have encountered intense pirate activity. We should hunt down some of their ships and see if we can gather any additional clues.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
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

### qe_yaoSpr_2024_day05_t3:
* Name:	Some Yaot survivors in our medical ward are ready to be questioned. If we manage to prove our good intentions they might help us find the Yaot pilgrimage.

<color=#FBB03F>Prestige is earned through each player level-up and by completing daily and weekly assignments.</color>
* Description:	Some Yaot survivors in our medical ward are ready to be questioned. If we manage to prove our good intentions they might help us find the Yaot pilgrimage.

<color=#FBB03F>Prestige is earned through each player level-up and by completing daily and weekly assignments.</color>
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

### qe_yaoSpr_2024_day06_t3:
* Name:	The Yaot have accepted our offer to support their pilgrimage. Requests have come in from ships needing spares and replacement parts for repairs. If we provide these, we might learn more about why the pirates are after these ships.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
* Description:	The Yaot have accepted our offer to support their pilgrimage. Requests have come in from ships needing spares and replacement parts for repairs. If we provide these, we might learn more about why the pirates are after these ships.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
* Type:	Event
* EventId:	event_yaotSpring_2024_t3
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: Part_T3up
			* Amount: 100

### qe_yaoSpr_2024_day07_t3:
* Name:	Even though pirates are still swarming the area, Chocoan and the Yaot pilgrims are adamant about continuing their travels to see the astral conjunction events. In order to deter any further attacks on the civilian ships, we should patrol and clear the systems of any significant hostile forces.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Description:	Even though pirates are still swarming the area, Chocoan and the Yaot pilgrims are adamant about continuing their travels to see the astral conjunction events. In order to deter any further attacks on the civilian ships, we should patrol and clear the systems of any significant hostile forces.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Type:	Event
* EventId:	event_yaotSpring_2024_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Epic_T3up
			* Mode: Generated

### qe_yaoSpr_2024_day08_t3:
* Name:	Even the Fleet of Rams are after the Yaot pilgrim's supposed treasure. If we hope to protect them, we must first convince somebody to give us more information. We should try to make friends with the pilgrims and get somebody to talk.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from dismissing officers and are earned through completing signals.</color>
* Description:	Even the Fleet of Rams are after the Yaot pilgrim's supposed treasure. If we hope to protect them, we must first convince somebody to give us more information. We should try to make friends with the pilgrims and get somebody to talk.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from dismissing officers and are earned through completing signals.</color>
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

### qe_yaoSpr_2024_day09_t3:
* Name:	After talking to Chocoan we suspect there is more to the Yaot pilgrimage than the religious travels to astral conjunction events. We might be able to get more information from the Yaot Federation if we do some favors.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Description:	After talking to Chocoan we suspect there is more to the Yaot pilgrimage than the religious travels to astral conjunction events. We might be able to get more information from the Yaot Federation if we do some favors.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Type:	Event
* EventId:	event_yaotSpring_2024_t3
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: Faction_Yaot_T3up

### qe_yaoSpr_2024_day10_t3:
* Name:	We’ve reached a dead end on collecting intelligence on the Yaot, but our source within the Tanoch Empire has offered to provide more information. We should bring an adequate gift for compensation.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
* Description:	We’ve reached a dead end on collecting intelligence on the Yaot, but our source within the Tanoch Empire has offered to provide more information. We should bring an adequate gift for compensation.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
* Type:	Event
* EventId:	event_yaotSpring_2024_t3
* Goals:
	* 0:
		* GoalType: Pay
			* Id: questItem_progenitorRelic_t3
			* Amount: 1

### qe_yaoSpr_2024_day11_t3:
* Name:	While we still don't know what kind of treasure the pilgrims could have aboard their vessels, Chocoan wants to move on to another astral conjunction event. He has requested our assistance in clearing out the area from any hostile threats.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Description:	While we still don't know what kind of treasure the pilgrims could have aboard their vessels, Chocoan wants to move on to another astral conjunction event. He has requested our assistance in clearing out the area from any hostile threats.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Type:	Event
* EventId:	event_yaotSpring_2024_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Epic_T3up
			* Mode: Generated

### qe_yaoSpr_2024_day12_t3:
* Name:	The report on the pilgrim's procedure has been fully analyzed. Usually the pilgrim's convoy moves in a tight line formation towards the optimal conjunction points where they perform their religious rituals. However, a few ships regularly diverge from the common path and move into nearby asteroid fields. We should investigate the latest conjunction site and see if we can find anything of interest.

<color=#FBB03F>Ore can be mined from asteroids in asteroid fields. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
* Description:	The report on the pilgrim's procedure has been fully analyzed. Usually the pilgrim's convoy moves in a tight line formation towards the optimal conjunction points where they perform their religious rituals. However, a few ships regularly diverge from the common path and move into nearby asteroid fields. We should investigate the latest conjunction site and see if we can find anything of interest.

<color=#FBB03F>Ore can be mined from asteroids in asteroid fields. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
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

### qe_yaoSpr_2024_day13_t3:
* Name:	Chocoan has informed us that the next astral conjunction site will be inside the Cangacian territories. We convinced him to take part in the operation ourselves to ensure security in this hostile area of the Empty Quarter. Maybe we will be able to both protect the pilgrims and find out more about the suspected secret agenda. We should make sure the crew is properly prepared and ready for any eventualities.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* Description:	Chocoan has informed us that the next astral conjunction site will be inside the Cangacian territories. We convinced him to take part in the operation ourselves to ensure security in this hostile area of the Empty Quarter. Maybe we will be able to both protect the pilgrims and find out more about the suspected secret agenda. We should make sure the crew is properly prepared and ready for any eventualities.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* Type:	Event
* EventId:	event_yaotSpring_2024_t3
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 3

### qe_yaoSpr_2024_day14_t3:
* Name:	Chocoan has provided the coordinates to the next astral conjunction event. Strong hostile forces are to be expected in this system. Our goal is to both protect the civilian pilgrims and find out more about the suspected secret agenda of the Yaot Elders.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Description:	Chocoan has provided the coordinates to the next astral conjunction event. Strong hostile forces are to be expected in this system. Our goal is to both protect the civilian pilgrims and find out more about the suspected secret agenda of the Yaot Elders.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Type:	Event
* EventId:	event_yaotSpring_2024_t3
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_yaoSpr2024_Conjunction_t3

## QL_EVENT_YAOTSPRING_2024_T4
### qe_yaoSpr_2024_day01_t4:
* Name:	There are rumors circulating in the Empty Quarter about an increase in Cangacian pirate activity. Fleet Command asks us to gather intel from our contacts with the Iyatequa traders. We should gain some favors to bargain for information.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Description:	There are rumors circulating in the Empty Quarter about an increase in Cangacian pirate activity. Fleet Command asks us to gather intel from our contacts with the Iyatequa traders. We should gain some favors to bargain for information.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Type:	Event
* EventId:	event_yaotSpring_2024_t4
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: Faction_Tr1_T4up

### qe_yaoSpr_2024_day02_t4:
* Name:	The Iyatequa traders are involved with pirates attacking Yaot pilgrims in the Empty Quarter. We might get more information through selling equipment and arms on the open market.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
* Description:	The Iyatequa traders are involved with pirates attacking Yaot pilgrims in the Empty Quarter. We might get more information through selling equipment and arms on the open market.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
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

### qe_yaoSpr_2024_day03_t4:
* Name:	To learn more about the pirate raids, we should get in contact with the Yaot pilgrims. They appear to be hiding after recent attacks. We have no other option than to perform reconnaissance in the nearby systems.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
* Description:	To learn more about the pirate raids, we should get in contact with the Yaot pilgrims. They appear to be hiding after recent attacks. We have no other option than to perform reconnaissance in the nearby systems.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
* Type:	Event
* EventId:	event_yaotSpring_2024_t4
* Goals:
	* 0:
		* GoalType: Scan
			* Tags: InSystem_T4up
			* Amount: 5
			* Analyzed: True

### qe_yaoSpr_2024_day04_t4:
* Name:	In our search for the Yaot pilgrims we have encountered intense pirate activity. We should hunt down some of their ships and see if we can gather any additional clues.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
* Description:	In our search for the Yaot pilgrims we have encountered intense pirate activity. We should hunt down some of their ships and see if we can gather any additional clues.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
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

### qe_yaoSpr_2024_day05_t4:
* Name:	Some Yaot survivors in our medical ward are ready to be questioned. If we manage to prove our good intentions they might help us find the Yaot pilgrimage.

<color=#FBB03F>Prestige is earned through each player level-up and by completing daily and weekly assignments.</color>
* Description:	Some Yaot survivors in our medical ward are ready to be questioned. If we manage to prove our good intentions they might help us find the Yaot pilgrimage.

<color=#FBB03F>Prestige is earned through each player level-up and by completing daily and weekly assignments.</color>
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

### qe_yaoSpr_2024_day06_t4:
* Name:	The Yaot have accepted our offer to support their pilgrimage. Requests have come in from ships needing spares and replacement parts for repairs. If we provide these, we might learn more about why the pirates are after these ships.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
* Description:	The Yaot have accepted our offer to support their pilgrimage. Requests have come in from ships needing spares and replacement parts for repairs. If we provide these, we might learn more about why the pirates are after these ships.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
* Type:	Event
* EventId:	event_yaotSpring_2024_t4
* Goals:
	* 0:
		* GoalType: Craft
			* Category: Crafting
			* Tags: Part_T4up
			* Amount: 100

### qe_yaoSpr_2024_day07_t4:
* Name:	Even though pirates are still swarming the area, Chocoan and the Yaot pilgrims are adamant about continuing their travels to see the astral conjunction events. In order to deter any further attacks on the civilian ships, we should patrol and clear the systems of any significant hostile forces.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Description:	Even though pirates are still swarming the area, Chocoan and the Yaot pilgrims are adamant about continuing their travels to see the astral conjunction events. In order to deter any further attacks on the civilian ships, we should patrol and clear the systems of any significant hostile forces.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Type:	Event
* EventId:	event_yaotSpring_2024_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Epic_T4up
			* Mode: Generated

### qe_yaoSpr_2024_day08_t4:
* Name:	Even the Fleet of Rams are after the Yaot pilgrim's supposed treasure. If we hope to protect them, we must first convince somebody to give us more information. We should try to make friends with the pilgrims and get somebody to talk.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from dismissing officers and are earned through completing signals.</color>
* Description:	Even the Fleet of Rams are after the Yaot pilgrim's supposed treasure. If we hope to protect them, we must first convince somebody to give us more information. We should try to make friends with the pilgrims and get somebody to talk.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from dismissing officers and are earned through completing signals.</color>
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

### qe_yaoSpr_2024_day09_t4:
* Name:	After talking to Chocoan we suspect there is more to the Yaot pilgrimage than the religious travels to astral conjunction events. We might be able to get more information from the Yaot Federation if we do some favors.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Description:	After talking to Chocoan we suspect there is more to the Yaot pilgrimage than the religious travels to astral conjunction events. We might be able to get more information from the Yaot Federation if we do some favors.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Type:	Event
* EventId:	event_yaotSpring_2024_t4
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Amount: 5
			* Tags: Faction_Yaot_T4up

### qe_yaoSpr_2024_day10_t4:
* Name:	We’ve reached a dead end on collecting intelligence on the Yaot, but our source within the Tanoch Empire has offered to provide more information. We should bring an adequate gift for compensation.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
* Description:	We’ve reached a dead end on collecting intelligence on the Yaot, but our source within the Tanoch Empire has offered to provide more information. We should bring an adequate gift for compensation.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
* Type:	Event
* EventId:	event_yaotSpring_2024_t4
* Goals:
	* 0:
		* GoalType: Pay
			* Id: questItem_progenitorRelic_t4
			* Amount: 1

### qe_yaoSpr_2024_day11_t4:
* Name:	While we still don't know what kind of treasure the pilgrims could have aboard their vessels, Chocoan wants to move on to another astral conjunction event. He has requested our assistance in clearing out the area from any hostile threats.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Description:	While we still don't know what kind of treasure the pilgrims could have aboard their vessels, Chocoan wants to move on to another astral conjunction event. He has requested our assistance in clearing out the area from any hostile threats.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Type:	Event
* EventId:	event_yaotSpring_2024_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 1
			* Tags: Epic_T4up
			* Mode: Generated

### qe_yaoSpr_2024_day12_t4:
* Name:	The report on the pilgrim's procedure has been fully analyzed. Usually the pilgrim's convoy moves in a tight line formation towards the optimal conjunction points where they perform their religious rituals. However, a few ships regularly diverge from the common path and move into nearby asteroid fields. We should investigate the latest conjunction site and see if we can find anything of interest.

<color=#FBB03F>Ore can be mined from asteroids in asteroid fields. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
* Description:	The report on the pilgrim's procedure has been fully analyzed. Usually the pilgrim's convoy moves in a tight line formation towards the optimal conjunction points where they perform their religious rituals. However, a few ships regularly diverge from the common path and move into nearby asteroid fields. We should investigate the latest conjunction site and see if we can find anything of interest.

<color=#FBB03F>Ore can be mined from asteroids in asteroid fields. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
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

### qe_yaoSpr_2024_day13_t4:
* Name:	Chocoan has informed us that the next astral conjunction site will be inside the Cangacian territories. We convinced him to take part in the operation ourselves to ensure security in this hostile area of the Empty Quarter. Maybe we will be able to both protect the pilgrims and find out more about the suspected secret agenda. We should make sure the crew is properly prepared and ready for any eventualities.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* Description:	Chocoan has informed us that the next astral conjunction site will be inside the Cangacian territories. We convinced him to take part in the operation ourselves to ensure security in this hostile area of the Empty Quarter. Maybe we will be able to both protect the pilgrims and find out more about the suspected secret agenda. We should make sure the crew is properly prepared and ready for any eventualities.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* Type:	Event
* EventId:	event_yaotSpring_2024_t4
* Goals:
	* 0:
		* GoalType: UpgradeOfficer
			* Amount: 5

### qe_yaoSpr_2024_day14_t4:
* Name:	Chocoan has provided the coordinates to the next astral conjunction event. Strong hostile forces are to be expected in this system. Our goal is to both protect the civilian pilgrims and find out more about the suspected secret agenda of the Yaot Elders.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Description:	Chocoan has provided the coordinates to the next astral conjunction event. Strong hostile forces are to be expected in this system. Our goal is to both protect the civilian pilgrims and find out more about the suspected secret agenda of the Yaot Elders.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Type:	Event
* EventId:	event_yaotSpring_2024_t4
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: event_yaoSpr2024_Conjunction_t4

## QL_TEST
### qt_001:
* Name:	No header for quest qt_001
* Description:	No description for quest qt_001
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
### qt_002:
* Name:	No header for quest qt_002
* Description:	No description for quest qt_002
* Type:	Side
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Ids:
				* story_A02_WiracodaGate
				* story_A03_GulfTaln

## QL_TEST3
### qt_003:
* Name:	No header for quest qt_003
* Description:	No description for quest qt_003
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
### qt_004:
* Name:	No header for quest qt_004
* Description:	No description for quest qt_004
* Type:	Side
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Amount: 3
			* Mode: Faction
			* Tags: Tanoch_T3up

## QL_TESTQUESTDIALOG
### qm_testQuestDialog:
* Name:	No header for quest qm_testQuestDialog
* Description:	No description for quest qm_testQuestDialog
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
### qt_testDismissOfficers:
* Name:	No header for quest qt_testDismissOfficers
* Description:	No description for quest qt_testDismissOfficers
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
### qt_test_strike_13:
* Name:	No header for quest qt_test_strike_13
* Description:	No description for quest qt_test_strike_13
* Type:	Main
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Ids:
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

## QL_TEST_STRIKE_16
### qt_test_strike_16:
* Name:	No header for quest qt_test_strike_16
* Description:	No description for quest qt_test_strike_16
* Type:	Main
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Ids:
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

## QL_TEST_STRIKE_14
### qt_test_strike_14:
* Name:	No header for quest qt_test_strike_14
* Description:	No description for quest qt_test_strike_14
* Type:	Main
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Ids:
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

## QL_TEST_STRIKE_17
### qt_test_strike_17:
* Name:	No header for quest qt_test_strike_17
* Description:	No description for quest qt_test_strike_17
* Type:	Main
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Ids:
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

## QL_TEST_STRIKE_21
### qt_test_strike_21:
* Name:	No header for quest qt_test_strike_21
* Description:	No description for quest qt_test_strike_21
* Type:	Main
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Ids:
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

## QL_TEST_STRIKE_15
### qt_test_strike_15:
* Name:	No header for quest qt_test_strike_15
* Description:	No description for quest qt_test_strike_15
* Type:	Main
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Ids:
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

## QL_TEST_STRIKE_18
### qt_test_strike_18:
* Name:	No header for quest qt_test_strike_18
* Description:	No description for quest qt_test_strike_18
* Type:	Main
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Ids:
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

## QL_TEST_STRIKE_22
### qt_test_strike_22:
* Name:	No header for quest qt_test_strike_22
* Description:	No description for quest qt_test_strike_22
* Type:	Main
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Ids:
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

## QL_TEST_STRIKE_19
### qt_test_strike_19:
* Name:	No header for quest qt_test_strike_19
* Description:	No description for quest qt_test_strike_19
* Type:	Main
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Ids:
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

## QL_TEST_STRIKE_20
### qt_test_strike_20:
* Name:	No header for quest qt_test_strike_20
* Description:	No description for quest qt_test_strike_20
* Type:	Main
* Goals:
	* 0:
		* GoalType: CompleteQuest
			* Ids:
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

## QL_A_001
### qa_001:
* Name:	No header for quest qa_001
* Description:	No description for quest qa_001
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: Mined1A
			* Total: 3000

### qa_002:
* Name:	No header for quest qa_002
* Description:	No description for quest qa_002
* Type:	Achievement
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: Upgrade
			* Amount: 5

## QL_TEST_GGF_STORY
### qs_s2_01_sijinLighthouse:
* Name:	Sijin Lighthouse
* Description:	We detected a possible signal from the missing Khar-Kalaad.
* Type:	Side
* FollowUps: ql_raid_019
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: story_D01_SijinLighthouse

### qs_s2_01_iliyinLighthouse:
* Name:	Iliyin Lighthouse
* Description:	We have arrived at another lighthouse in uncharted territory. Be prepared for anything.
* Type:	Side
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: story_D02_IliyinLighthouse

### qs_s2_01_bTemple:
* Name:	Bright Temple
* Description:	The Amassari here may have answers about the nature of the Progenitor observer.
* Type:	Side
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: story_D03_BrightTemple

### qs_s2_01_hataldan:
* Name:	Hataldan
* Description:	The fallen capital of the Amassari, and last known position of the Observer.
* Type:	Side
* FollowUps: ql_raid_020
* Goals:
	* 0:
		* GoalType: CompleteMission
			* Id: story_D04_Hataldan

## QL_COMPENSATION_LVLUP
### q_compensation_lvl_10:
* Name:	Fame and Honor (Lvl 10)
* Description:	Player XP can be gained from completing missions and assignments and from destroying enemy units.
* Type:	Event
* EventId:	event_levelUpCompensationQuests
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: PlayerXP
			* Total: 12600

### q_compensation_lvl_20:
* Name:	Fame and Honor (Lvl 20)
* Description:	Player XP can be gained from completing missions and assignments and from destroying enemy units.
* Type:	Event
* EventId:	event_levelUpCompensationQuests
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: PlayerXP
			* Total: 36100

### q_compensation_lvl_35:
* Name:	Fame and Honor (Lvl 35)
* Description:	Player XP can be gained from completing missions and assignments and from destroying enemy units.
* Type:	Event
* EventId:	event_levelUpCompensationQuests
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: PlayerXP
			* Total: 90100

### q_compensation_lvl_50:
* Name:	Fame and Honor (Lvl 50)
* Description:	Player XP can be gained from completing missions and assignments and from destroying enemy units.
* Type:	Event
* EventId:	event_levelUpCompensationQuests
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: PlayerXP
			* Total: 166600

### q_compensation_lvl_75:
* Name:	Fame and Honor (Lvl 75)
* Description:	Player XP can be gained from completing missions and assignments and from destroying enemy units.
* Type:	Event
* EventId:	event_levelUpCompensationQuests
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: PlayerXP
			* Total: 344100

### q_compensation_lvl_100:
* Name:	Fame and Honor (Lvl 100)
* Description:	Player XP can be gained from completing missions and assignments and from destroying enemy units.
* Type:	Event
* EventId:	event_levelUpCompensationQuests
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: PlayerXP
			* Total: 584100

### q_compensation_lvl_150:
* Name:	Fame and Honor (Lvl 150)
* Description:	Player XP can be gained from completing missions and assignments and from destroying enemy units.
* Type:	Event
* EventId:	event_levelUpCompensationQuests
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: PlayerXP
			* Total: 1251600

### q_compensation_lvl_200:
* Name:	Fame and Honor (Lvl 200)
* Description:	Player XP can be gained from completing missions and assignments and from destroying enemy units.
* Type:	Event
* EventId:	event_levelUpCompensationQuests
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: PlayerXP
			* Total: 2169100

### q_compensation_lvl_300:
* Name:	Fame and Honor (Lvl 300)
* Description:	Player XP can be gained from completing missions and assignments and from destroying enemy units.
* Type:	Event
* EventId:	event_levelUpCompensationQuests
* Goals:
	* 0:
		* GoalType: Statistic
			* Id: PlayerXP
			* Total: 4754100

## Q_TEST_YAO_SPRING
### q_test_yaoSpr_2024_day04_t4:
* Name:	No header for quest q_test_yaoSpr_2024_day04_t4
* Description:	No description for quest q_test_yaoSpr_2024_day04_t4
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
