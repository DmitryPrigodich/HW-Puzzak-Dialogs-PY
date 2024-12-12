# HWM QUESTS

## QM_T0_TUTMISSIONS
* Name: Landing
* Description: Our arrival in this galaxy was met with tragedy.
* Type: Main
* CinematicIds: 20:10:25
* FollowUps: ql_main_t0_station
* Goals:
	* Task 1: Complete missions:
		* 'Duzumi Gate'
		* 'Duzumi Gate'
	* Task 2: Complete mission 'Wiracoda Gate'
	* Task 3: Complete mission 'Gulf Taln'

## QM_T0_INTROSTATION
* Name: Lazarus Station
* Description: We were given the coordinates of a local Hiigaran settlement. We should go there.
* Type: Main
* Goals:
	* Task 1: Goto LAZARUS system of Hiigaran Medea's territories

## QM_T0_INTROMARKET
* Name: Local Currency
* Description: The market can be accessed at stations and inside the flagship, though the selection of items in the flagship market is smaller. For now, we need to pick up some local currency to barter with the locals.
* Type: Main
* FollowUps: ql_main_t0_strikeCraft
* Goals:
	* Task 1: Buy: pack_market_freeHC_insta

## QM_T0_INTROFABRICATOR
* Name: Fabricator
* Description: Our fabricators are operational again. We should produce more strike craft in case we run into more hostiles.
* Type: Main
* Goals:
	* Task 1: Craft

## QM_T0_INTROEQUIPSTRIKECRAFT
* Name: Strike Craft
* Description: We need to ready our strike craft inside our hangars.
* Type: Main
* FollowUps: ql_main_t0_v2_signals
* Goals:
	* Task 1: Equip Squad

## QM_T0_V2_INTROSCANNING
* Name: Scanning
* Description: We have been asked to take care of a local threat to the Lazarus Station. We need to find out where it is.
* Type: Main
* Goals:
	* Task 1: Scan
	* Task 2: Scan

## QM_T0_V2_INTROSIGNALS
* Name: Signals
* Description: We have found hostile signals in the system. We need to clear it out and return to Lazarus Station.
* Type: Main
* FollowUps: ql_main_t0_mining
* Goals:
	* Task 1: Complete side mission
	* Task 2: Goto LAZARUS system of Hiigaran Medea's territories

## QM_T0_INTROSCANBELTS
* Name: Asteroid Clusters
* Description: We've been asked by Lazarus Station to help with resource scarcity. We'll need to find suitable mining opportunities by scanning for mineral-rich asteroids in nearby systems.
* Type: Main
* Goals:
	* Task 1: Goto JONALLI system of Hiigaran Medea's territories
	* Task 2: 1 ScannedBelt

## QM_T0_INTROMINING
* Name: Mining
* Description: We found a suitable spot for mining. Use the resource collector to mine the mineral rich asteroids.
* Type: Main
* FollowUps: ql_main_t0_support
* Goals:
	* Task 1: 50 Mined0A

## QM_T0_SUPPORT
* Name: Support
* Description: Now that we have the needed minerals, we should go back to Lazarus Station to deliver them.
* Type: Main
* FollowUps: ql_main_t0_officer
* Goals:
	* Task 1: Pay 25 RU Type M Ore in LAZARUS system of Hiigaran Medea's territories

## QM_T0_INTROBRIDGE
* Name: Bridge
* Description: Gideon S'jet has offered his Progenitor expertise. We should appoint him as head of science on the bridge.
* Type: Main
* FollowUps: ql_main_t0_escorts
* Goals:
	* Task 1: Equip Officer

## QM_T0_INTROSHIPYARD
* Name: Shipyard
* Description: We have clearance to use the shipyards of Lazarus Station. We should build an additional assault frigate there to bolster our fleet.
* Type: Main
* Goals:
	* Task 1: Craft

## QM_T0_INTROEQUIPESCORTS
* Name: Escort Ships
* Description: Our new assault frigate needs to be staffed and readied. We can do that at any station through Fleet Configuration.
* Type: Main
* FollowUps: ql_main_t0_sideProg
* Goals:
	* Task 1: Equip Escort

## QM_T0_SCIENTIST_BAAEKH_A
* Name: Baaekh S’jet
* Description: Baaekh S’jet was one of the foremost scientists on Progenitor culture. According to Gideon she has data that can help us with our own research into the Progenitors.
* Type: Main
* Goals:
	* Task 1: Goto ROA TISAAD system of Hiigaran Medea's territories
	* Task 2: Goto SAARET system of Hiigaran Medea's territories
	* Task 3: 
		* 4 ScannedBelt
		* 1 ScannedGenerated

## QM_T0_SCIENTIST_BAAEKH_B
* Name: Rescue Mission
* Description: We found Baaekh S'jet, but she can't come out of hiding until we have distracted the hostiles in the area.
* Type: Main
* FollowUps: ql_main_t0_relic
* Goals:
	* Task 1: Complete side mission
	* Task 2: Goto ROA TISAAD system of Hiigaran Medea's territories

## QM_T0_RELIC
* Name: Relic Retrieval
* Description: With information provided by Baaekh S’jet, we now know a potential location of a Progenitor Relic in Toasiim that must be retrieved.
* Type: Main
* FollowUps: ql_main_t0_moreMining
* Goals:
	* Task 1: Goto TOASIIM system of Hiigaran Medea's territories
	* Task 2: Scan
	* Task 3: Complete mission 'Relic Signature'

## QM_T0_SCIENTIST_HYEAA_A
* Name: Hyeaa Somtaaw
* Description: Hyeaa Somtaaw was an expert in Progenitor Materials sciences. He has established an independent lab at Nokuuna. According to Gideon, he has data that can help us with our own research into the Progenitors.
* Type: Main
* FollowUps: ql_main_t0_jolja
* Goals:
	* Task 1: Goto NOKUUNA system of Hiigaran Medea's territories
	* Task 2: Craft
	* Task 3: Equip Squad
	* Task 4: 225 Mined0A

## QM_T0_SCIENTIST_HYEAA_B
* Name: Process Investigation
* Description: Hyeaa Somtaaw wants to investigate our fabrication processes, find a way to improve it by incorporating Progenitor technology. In return he will share his data with us.
* Type: Main
* Goals:
	* Task 1: 
		* Craft
		* Craft
		* Craft
	* Task 2: Craft

## QM_T0_JOLJA
* Name: Delver
* Description: After examining the Progenitor Relic, Gideon wants us to find a Progenitor Terminal in Iniim. If we access this, we may have some answers about what happened at Wiracoda Gate.
* Type: Main
* FollowUps: ql_main_t0_setupPlayer
* Goals:
	* Task 1: Goto INIIM system of Hiigaran Medea's territories
	* Task 2: Scan
	* Task 3: Complete mission 'Jolja'
	* Task 4: Goto LAZARUS system of Hiigaran Medea's territories

## QM_T0_PICKKIITH
* Name: Blood Ties
* Description: The local Hiigaran survivors wish to know what Kiith we affiliate with. There are advantages for declaring for a specific Kiith.
* Type: Main
* Goals:
	* Task 1: SelectKiith

## QM_T0_PICKNAME
* Name: Declaration
* Description: The Hiigaran survivors want to know your name, commander.
* Type: Main
* FollowUps:
	* ql_main_t1_newOres
	* ql_main_t0_joinClan
* Goals:
	* Task 1: ChangeName

## QM_T0_JOINCLAN
* Name: A Clan of Choice
* Description: We can increase our firepower and capabilities by joining with other battle groups.
* Type: Main
* Goals:
	* Task 1: JoinClan

## QM_T1_NEWORES
* Name: New Minerals
* Description: The inner systems may have different resources. We should check out the asteroids for mining spots.
* Type: Main
* FollowUps: ql_esca_mineT1
* Goals:
	* Task 1: Goto DEVADAASI system of Iyatequa's territories
	* Task 2: 6 ScannedBelt
	* Task 3: 200 Mined1A_Mined1B_Mined1C

## QM_T1_INTROREFINING
* Name: Refinery
* Description: The new ores require refining to be usable for construction purposes. Luckily we have refining facilities on board.
* Type: Main
* FollowUps:
	* ql_main_t1_sideHiig
	* qm_t1_facHiigaran_A
	* qm_t1_facHiigaran_B
	* qm_t1_facHiigaran_C
	* qm_t1_facHiigaran_D
* Goals:
	* Task 1: 100 Refining1N_Refining1O_Refining1P
	* Task 2: Goto LAZARUS system of Hiigaran Medea's territories

## QM_T1_FACHIIGARAN
* Name: Hiigaran Outposts
* Description: Lazarus station asked us to help some Hiigaran outposts on the frontier.
* Type: Main
* FollowUps: ql_main_t1_strikeCraft
* Goals:
	* Task 1: Complete 3 of qm_t1_facHiigaran_A|qm_t1_facHiigaran_B|qm_t1_facHiigaran_C|qm_t1_facHiigaran_D
	* Task 2: Goto LAZARUS system of Hiigaran Medea's territories

## QM_T1_FACHIIGARAN_A
* Name: Outposts: Rescue
* Description: Long-range sensors located near another hyperspace gate have registered the presence of a Hiigaran fleet that emerged here. We are asked to this location and try to help any survivors as best as we can.
* Type: Side
* Goals:
	* Task 1: Goto TELA DIIM system of Iyatequa's territories
	* Task 2: 
		* 3 ScannedGenerated
		* Complete 3 side missions
	* Task 3: Pay 500 RU Type A Ore T1

## QM_T1_FACHIIGARAN_B
* Name: Outposts: Recon
* Description: To supply the needs of the Hiigaran fleet, we've been dispatched to look for a great mining source. Intel indicates this will put us into direct conflict with the Fleet of Rams.
* Type: Side
* Goals:
	* Task 1: Goto EKAAM NAR system of Iyatequa's territories
	* Task 2: 10 ScannedBelt
	* Task 3: 
		* 500 Mined1A_Mined1B_Mined1C
		* 15 ShipsDestroyed
	* Task 4: Goto EKAAM NAR system of Iyatequa's territories

## QM_T1_FACHIIGARAN_C
* Name: Outposts: Wall of Will
* Description: One of the only planetary settlements under Hiigaran control has been scouted by the Fleet of Rams. Until the planetary defenses are strengthened, they need military equipment to supply the defense.
* Type: Side
* Goals:
	* Task 1: Goto ARIITAR system of Iyatequa's territories
	* Task 2: 500 Mined1A
	* Task 3: Pay 150 RU Type A Ore T1
	* Task 4: Pay 3 Resource Collector
	* Task 5: Pay 1 Interceptor Squadron

## QM_T1_FACHIIGARAN_D
* Name: Outposts: Security
* Description: Hiigaran forces are working to clear systems to set up for colonization. The system in question is of special importance. We've been asked to go there and assist in securing the area.
* Type: Side
* Goals:
	* Task 1: Goto INAYAT system of Iyatequa's territories
	* Task 2: Scan
	* Task 3: 
		* 15 ShipsDestroyed
		* Complete 3 side missions
	* Task 4: Goto INAYAT system of Iyatequa's territories

## QM_T1_STRIKECRAFT
* Name: New Strike Craft
* Description: We have found a way to incorporate the new materials into our ship design.
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

## QM_T1_RCOLEQUIP
* Name: New Resource Collector
* Description: The new ores are more difficult to mine. We should build resource collectors that are equipped to deal with these denser metals.
* Type: Main
* Goals:
	* Task 1: Craft
	* Task 2: Equip Squad

## QM_T1_RCOLMINE
* Name: Mining Spree
* Description: We should put our new resource collectors to the test and stockpile some ores.
* Type: Main
* Goals:
	* Task 1: 4500 Mined1A_Mined1B_Mined1C

## QM_T1_ADVCOMBAT_01
* Name: Combat Trials
* Description: Our Hiigaran allies have prepared a combat area to test our improved strike craft.
* Type: Main
* Goals:
	* Task 1: Complete mission 'Combat Trials'

## QM_T1_KILLENEMYSHIPS
* Name: Hostiles
* Description: These inner systems are crawling with enemies. We should thin their numbers. Enemies are found in asteroid clusters and signals.
* Type: Main
* FollowUps: ql_main_t1_promoteOfficer
* Goals:
	* Task 1: 25 ShipsDestroyed

## QM_T1_INTROPROMOTEOFFICER
* Name: Crew Experience
* Description: Training our officers will increase their performance significantly. To train an officer we need to find insignias. Insignias can be gained from discharging officers and may be rewarded from completing signals.
* Type: Main
* FollowUps: ql_main_t1_escorts
* Goals:
	* Task 1: UpgradeOfficer

## QM_T1_RANKUPOFFICER
* Name: Crew Promotion
* Description: We should promote our most experienced officers to further improve their performance. Promoting an officer increase their special ability or may even grant them a second.
* Type: Side
* Goals:
	* Task 1: UpgradeOfficer

## QM_T1_ESCORT
* Name: New Escorts
* Description: We should bolster our fleet with frigates made from the new metals.
* Type: Main
* FollowUps: ql_main_t1_advCombat_02
* Goals:
	* Task 1: Craft
	* Task 2: Equip Escort

## QM_T1_ADVCOMBAT_02
* Name: Meropis Defense
* Description: We received a message that Meropis, a Iyatequa communications station, is asking for support in an expected Cangacian attack.
* Type: Main
* Goals:
	* Task 1: Complete mission 'Meropis Defense'

## QM_T1_DOSIGNALS
* Name: Signal Tracking
* Description: The Cangacians have been repelled, but we should disrupt their activities by hunting down hostile signals in the area.
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

## QM_T1_FACCANGACIAN
* Name: Cangacian Troubles
* Description: Cangacians are attacking colonies. We should help them in whatever way we can.
* Type: Main
* FollowUps: ql_main_t1_flagship
* Goals:
	* Task 1: Complete 3 of qm_t1_facCangacian_A|qm_t1_facCangacian_B|qm_t1_facCangacian_C|qm_t1_facCangacian_D
	* Task 2: Goto LAZARUS system of Hiigaran Medea's territories

## QM_T1_FACCANGACIAN_A
* Name: Troubles: Defiance
* Description: The world of Huaca is looking for help. They are opposing conscription from Supay’s Fleet of Rams, the punishment of which is brutal assault.
* Type: Side
* Goals:
	* Task 1: Goto NAREDRA system of Iyatequa's territories
	* Task 2: 15 ShipsDestroyedP1
	* Task 3: 
		* 1000 Mined1A_Mined1B_Mined1C
		* 500 Refining1N_Refining1O_Refining1P
	* Task 4: Goto NAREDRA system of Iyatequa's territories

## QM_T1_FACCANGACIAN_B
* Name: Troubles: Seeker
* Description: To oppose the Fleet of Rams, we were asked to undergo a mission to survey and map one of their three largest systems. We should also sabotage their efforts when the opportunity presents itself.
* Type: Side
* Goals:
	* Task 1: Goto JISHUN system of Iyatequa's territories
	* Task 2: 
		* 4 ScannedGenerated
		* Complete 4 side missions
		* 15 ShipsDestroyedP1
	* Task 3: Goto JISHUN system of Iyatequa's territories

## QM_T1_FACCANGACIAN_C
* Name: Troubles: Stone Hearth
* Description: We're asked to to assist the system of Acheron. They do not have a refinery set up, so we need to go there and refine metals for their construction facilities to use.
* Type: Side
* Goals:
	* Task 1: Goto DEVADAASI system of Iyatequa's territories
	* Task 2: 15 ScannedBelt
	* Task 3: 
		* 1000 Mined1A
		* 500 Refining1N
	* Task 4: Pay 300 RU Type A Refined T1

## QM_T1_FACCANGACIAN_D
* Name: Troubles: A Black Eye
* Description: The Fleet of Rams is assembling an assault force that is aimed at a cluster of neutral systems. Intel shows that another Cangacian band plans to engage Supay’s commanding lieutenant here. We're asked to create a distraction to weaken the Fleet of Rams in the resulting battle.
* Type: Side
* Goals:
	* Task 1: Goto ESTRAIIR system of Iyatequa's territories
	* Task 2: Scan
	* Task 3: Pay 1 Interceptor Squadron
	* Task 4: Complete 4 side missions
	* Task 5: Goto ESTRAIIR system of Iyatequa's territories

## QM_T1_INTROCRAFTFLAGSHIP
* Name: Flagship Construction
* Description: We have an Explorer-class flagship blueprint utilizing the new minerals found in this region.
* Type: Main
* FollowUps: ql_main_t1_killCangacians
* Goals:
	* Task 1: Start Crafting - Flagship_Ship

## QM_T1_INTROEQUIPFLAGSHIP
* Name: New Flagship
* Description: Once the flagship construction has finished, we should move over to the new flagship, including our ships and officers. This is done via the fleet configuration.
* Type: Main
* FollowUps: ql_main_t1_advCombat_03
* Goals:
	* Task 1: Craft
	* Task 2: Equip Flagship
	* Task 3: 
		* Equip Squad
		* Equip Escort
		* Equip Officer

## QM_T1_KILLCANGACIANS
* Name: Pest Control
* Description: While we wait for the flagship construction to finish, we might as well make this galaxy a safer place.
* Type: Side
* Goals:
	* Task 1: 20 ShipsDestroyedP1

## QM_T1_ADVCOMBAT_03
* Name: The Pool
* Description: The Iyatequa have flagged a location for suspicious hostile activity. They've asked us to investigate on their behalf.
* Type: Main
* Goals:
	* Task 1: Complete mission 'The Pool'

## QM_T1_KILLPROGENITORS
* Name: Hostile History
* Description: The Progenitor remnants present a danger to the people living in this galaxy. We should thin their numbers.
* Type: Main
* FollowUps: ql_main_t1_turrets
* Goals:
	* Task 1: 10 ShipsDestroyedProgenitor

## QM_T1_CRAFTTURRET
* Name: Weapon Turrets
* Description: The new flagship follows modular design principles, allowing us to outfit it with turrets as we choose. First we should build a weapon turret.
* Type: Main
* Goals:
	* Task 1: Craft

## QM_T1_MOUNTTURRET
* Name: Mounting Turrets
* Description: Now that we have a turret module, we should mount it on our flagship. Turrets can be managed in the external module view of our flagship.
* Type: Main
* FollowUps: ql_main_t1_upgrades
* Goals:
	* Task 1: Equip Weapon

## QM_T1_RAREEARTHS
* Name: Rare Elements
* Description: When refining ores in the refinery there is a chance for rare earths to appear in addition to the refined metals.
* Type: Main
* Goals:
	* Task 1: GainItem

## QM_T1_UPGRADETURRET
* Name: Turret Upgrades
* Description: The rare minerals we have extracted can be used to improve our modules.
* Type: Main
* FollowUps:
	* ql_main_t1_sideProg
	* qm_t1_facProgenitors_A
	* qm_t1_facProgenitors_B
	* qm_t1_facProgenitors_C
	* qm_t1_facProgenitors_D
* Goals:
	* Task 1: Craft

## QM_T1_UPGRADETURRET_3
* Name: Turret Upgrades Level 3
* Description: A module can be upgraded multiple times, vastly increasing its power.
* Type: Side
* Goals:
	* Task 1: Craft

## QM_T1_UPGRADETURRET_4
* Name: Turret Upgrades Level 4
* Description: A module can be upgraded multiple times, vastly increasing its power.
* Type: Side
* Goals:
	* Task 1: Craft

## QM_T1_UPGRADETURRET_5
* Name: Turret Upgrades Level 5
* Description: A module can be upgraded multiple times, vastly increasing its power.
* Type: Side
* Goals:
	* Task 1: Craft

## QM_T1_UPGRADETURRET_6
* Name: Turret Upgrades Level 6
* Description: A module can be upgraded multiple times, vastly increasing its power.
* Type: Side
* Goals:
	* Task 1: Craft

## QM_T1_UPGRADETURRET_7
* Name: Turret Upgrades Level 7
* Description: A module can be upgraded multiple times, vastly increasing its power.
* Type: Side
* Goals:
	* Task 1: Craft

## QM_T1_UPGRADETURRET_8
* Name: Turret Upgrades Level 8
* Description: A module can be upgraded multiple times, vastly increasing its power.
* Type: Side
* Goals:
	* Task 1: Craft

## QM_T1_UPGRADETURRETMAX
* Name: Final Turret Upgrades
* Description: Once a module has been upgraded to level 9, it is at its maximum level and cannot be upgraded further.
* Type: Side
* Goals:
	* Task 1: Craft

## QM_T1_FACPROGENITORS
* Name: Progenitor Components
* Description: To improve our scanner, we should gather data on Progenitor vessels. Once we have enough data, we can create a new scanner blueprint.
* Type: Main
* FollowUps: ql_main_t1_scanner
* Goals:
	* Task 1: Complete 3 of qm_t1_facProgenitors_A|qm_t1_facProgenitors_B|qm_t1_facProgenitors_C|qm_t1_facProgenitors_D
	* Task 2: Goto LAZARUS system of Hiigaran Medea's territories

## QM_T1_FACPROGENITORS_A
* Name: Components: A Wide Exchange
* Description: A few locals in this system have Progenitor technology they willing to hand to us if we agree to help them with their own problems regarding hostile Progenitor vessels and shortage of resources.
* Type: Side
* Goals:
	* Task 1: Goto JISHUN system of Iyatequa's territories
	* Task 2: 
		* 10 ShipsDestroyedProgenitor
		* 3000 Mined1A_Mined1B_Mined1C
		* 1500 Refining1N_Refining1O_Refining1P
	* Task 3: Goto JISHUN system of Iyatequa's territories

## QM_T1_FACPROGENITORS_B
* Name: Components: Hunt
* Description: Progenitor vessels in this area are equipped with M-type fuses. We need to attack and destroy a few vessels in order to gather enough of quality for use in the prototype.
* Type: Side
* Goals:
	* Task 1: Goto NAREDRA system of Iyatequa's territories
	* Task 2: 
		* 5 ScannedGenerated
		* Craft
		* Complete 5 side missions
	* Task 3: Goto NAREDRA system of Iyatequa's territories

## QM_T1_FACPROGENITORS_C
* Name: Components: A Full Quiver
* Description: Fleet command out of Lazarus frowns upon commanders that delve into Progenitor ruins without a minimum of protection. We need to bring our ship up to code and command will approve our ship for such operations in the future.
* Type: Side
* Goals:
	* Task 1: Goto SARAAL system of Iyatequa's territories
	* Task 2: GainItem
	* Task 3: Craft
	* Task 4: Complete 5 side missions
	* Task 5: Goto SARAAL system of Iyatequa's territories

## QM_T1_FACPROGENITORS_D
* Name: Components: Repurpose the Past
* Description: To save time, rather than reconstruct a Particle density array, we can salvage one from advanced Progenitor craft. We need to attack enough Progenitor ships to find one that is in decent condition. The module will require rare earths in order to activate properly. We can gather them at the system as well.
* Type: Side
* Goals:
	* Task 1: Goto DEVADAASI system of Iyatequa's territories
	* Task 2: 20 ScannedBelt
	* Task 3: 
		* GainItem
		* 10 ShipsDestroyedProgenitor
	* Task 4: Goto DEVADAASI system of Iyatequa's territories

## QM_T1_SCANNERMODULE
* Name: New Scanner
* Description: Based on the data from the Progenitor fragments, our engineers have created a new scanner blueprint.
* Type: Main
* FollowUps:
	* ql_main_t2_strike
	* ql_esca_scan
	* ql_main_t1_scannerCharge
* Goals:
	* Task 1: Craft
	* Task 2: Equip Sensor

## QM_T1_SCANNEROVERCHARGE
* Name: Rare Find
* Description: Some objects are too hidden to find them with our scanner under regular circumstances. Luckily, we can use special batteries to overcharge the scanner beyond its normal abilities to be able to find those.
* Type: Side
* Goals:
	* Task 1: ChargeScanner
	* Task 2: Scan

## QM_T2_FINDPIRATEHIDEOUT
* Name: Hidden in the Dark
* Description: We need to find the system from where the recent Cangacian activity originates. Reports indicate the system might be near Saraal. We should go there and use our long range scanners.
* Type: Main
* FollowUps:
	* ql_raid_013
	* ql_main_t1_upgradeExternals
	* ql_main_t1_introLiaison
* Goals:
	* Task 1: 
		* Scan
		* Goto DEVADAASI system of Iyatequa's territories

## QM_T2_STRIKEPIRATEHIDEOUT
* Name: Cangacian Hideout
* Description: We have located the pirate hideout. Now is the time to strike.
* Type: Main
* Goals:
	* Task 1: Complete 1 of qr_013

## QM_T1_UPGRADEMODULES
* Name: Exploration Upgrades
* Description: In order to move deeper into the galaxy we should upgrade our scanner and drives core.
* Type: Main
* FollowUps: ql_main_t1_introInternals
* Goals:
	* Task 1: 
		* Craft
		* Craft

## QM_T1_INTROLIAISON
* Name: Reaching Out
* Description: The Iyatequa are interested in doing business with us. Completing liaison assignments for them will allow us to increase our reputation, which allows us to buy special items and blueprints in their liaison requisitions office.
* Type: Side
* Goals:
	* Task 1: 3 Faction

## QM_T1_INTROINTERNALS
* Name: Internal Modules
* Description: Our flagship has a configurable interior, which we can use to boost our exploration, production or combat abilities using internal modules.
* Type: Main
* Goals:
	* Task 1: Craft
	* Task 2: Equip Internal

## QM_T1_UPGRADEINTERNALS
* Name: Internal Module Upgrades
* Description: Just like with weapon turrets, we can improve our internal module's performance through upgrades.
* Type: Main
* FollowUps:
	* ql_main_t1_sideIyat
	* qm_t1_facIyatequa_A
	* qm_t1_facIyatequa_B
	* qm_t1_facIyatequa_C
	* qm_t1_facIyatequa_D
* Goals:
	* Task 1: Craft

## QM_T1_FACIYATEQUA
* Name: Iyatequa Business
* Description: The Iyatequa have heard of our plan to meet the Tanoch and agreed to help us set up our science facilities to research better drives. For a price, of course.
* Type: Main
* FollowUps: ql_main_t2_research
* Goals:
	* Task 1: Complete 3 of qm_t1_facIyatequa_A|qm_t1_facIyatequa_B|qm_t1_facIyatequa_C|qm_t1_facIyatequa_D
	* Task 2: Goto LAZARUS system of Hiigaran Medea's territories

## QM_T1_FACIYATEQUA_A
* Name: Business: An Honest Job
* Description: The Iyatequa asked us to perform a variety of simple activities and allowing them to monitor the related systems for their own research purposes.
* Type: Side
* Goals:
	* Task 1: Goto NIIREA PAAS system of Iyatequa's territories
	* Task 2: 
		* 3000 Mined1A_Mined1B_Mined1C
		* GainItem
		* Craft
	* Task 3: Goto NIIREA PAAS system of Iyatequa's territories

## QM_T1_FACIYATEQUA_B
* Name: Business: The Barrier
* Description: We've been told to deal with an attempted trade blockade set up by pirates. We will need to get some spare resources and some module upgrades before we face the enemy.
* Type: Side
* Goals:
	* Task 1: Goto INAYAT system of Iyatequa's territories
	* Task 2: 
		* 1500 Refining1N_Refining1O_Refining1P
		* Craft
	* Task 3: 25 ShipsDestroyed
	* Task 4: Goto INAYAT system of Iyatequa's territories

## QM_T1_FACIYATEQUA_C
* Name: Business: The Sheriff
* Description: Hostiles have been gathering near Iyatequa trading routes. We've been asked to investigate and root out pirates and other undesirables.
* Type: Side
* Goals:
	* Task 1: Goto EKAAM NAR system of Iyatequa's territories
	* Task 2: 
		* Scan
		* Complete 5 side missions
		* 25 ShipsDestroyed
	* Task 3: Goto EKAAM NAR system of Iyatequa's territories

## QM_T1_FACIYATEQUA_D
* Name: Business: The Dealer
* Description: A dealer supplying the Iyatequa has tried cutting corners and incured their wrath. We've been asked to apprehend him.
* Type: Side
* Goals:
	* Task 1: Goto ARIITAR system of Iyatequa's territories
	* Task 2: Goto TELA DIIM system of Iyatequa's territories
	* Task 3: 
		* Scan
		* Complete 5 side missions
	* Task 4: Pay 1000 RU Type B Refined T1
	* Task 5: Goto ARIITAR system of Iyatequa's territories

## QM_T2_INTRORP
* Name: Laboratories
* Description: Our scientists have brought our on-ship laboratories online. We can collect the data of their findings there.
* Type: Main
* Goals:
	* Task 1: GainItem

## QM_T2_INTRORESEARCH
* Name: Research Center
* Description: Lazarus Base has given us access to a workshop module attached to the station. We can perform further research there and develop new technologies.
* Type: Main
* FollowUps: ql_main_t2_newResources
* Goals:
	* Task 1: Craft

## QM_T2_NEWRESOURCES
* Name: New Resources T2
* Description: It seems the deeper we move into the galaxy the more minerals we find.
* Type: Main
* FollowUps:
	* ql_main_t2_sideCang
	* qm_t2_facCangacian_A
	* qm_t2_facCangacian_B
	* qm_t2_facCangacian_C
	* qm_t2_facCangacian_D
* Goals:
	* Task 1: Goto BISHAAN TEL system of Iyatequa's territories
	* Task 2: 25 ScannedBelt
	* Task 3: 3000 Mined2A_Mined2B_Mined2C_Mined2D
	* Task 4: Craft
	* Task 5: Goto LAZARUS system of Hiigaran Medea's territories

## QM_T2_FACCANGACIAN
* Name: Cangacian Incursion
* Description: Several Hiigaran colonies are under attack by Cangacians. Lazarus command has asked us to help as much as we can.
* Type: Main
* FollowUps: ql_main_t2_strikeCraftResearch
* Goals:
	* Task 1: Complete 3 of qm_t2_facCangacian_A|qm_t2_facCangacian_B|qm_t2_facCangacian_C|qm_t2_facCangacian_D
	* Task 2: Goto LAZARUS system of Hiigaran Medea's territories

## QM_T2_FACCANGACIAN_A
* Name: Incursion: Reverse Engineering
* Description: This colony was attacked by vessels incorporating non-Cangacian technology. We're asked to try to reverse engineer some of it.
* Type: Side
* Goals:
	* Task 1: Goto BISHAAN TEL system of Iyatequa's territories
	* Task 2: 35 ShipsDestroyed
	* Task 3: GainItem
	* Task 4: Craft
	* Task 5: Goto BISHAAN TEL system of Iyatequa's territories

## QM_T2_FACCANGACIAN_B
* Name: Incursion: Rebuilding Efforts
* Description: This colony was hit hard. We need to clear the area of remaining pirates and help with rebuilding.
* Type: Side
* Goals:
	* Task 1: Goto SOBEL REM system of Iyatequa's territories
	* Task 2: Complete 10 side missions
	* Task 3: 
		* Pay 650 RU Type A Ore T2
		* Pay 650 RU Type B Ore T2
		* Pay 650 RU Type C Ore T2
	* Task 4: GainItem
	* Task 5: Goto SOBEL REM system of Iyatequa's territories

## QM_T2_FACCANGACIAN_C
* Name: Incursion: Enemy Intentions
* Description: This colony repelled the attackers and gathered some intel. They need our help to decrypt it and find safe places for mining.
* Type: Side
* Goals:
	* Task 1: Goto KEID system of Iyatequa's territories
	* Task 2: GainItem
	* Task 3: 
		* 30 ScannedBelt
		* 35 ShipsDestroyed
	* Task 4: Goto KEID system of Iyatequa's territories

## QM_T2_FACCANGACIAN_D
* Name: Incursion: Preemptive Strike
* Description: The most recent attack. Intel shows it was just a scouting mission. We need to help with setting up quick defenses and take out the assault fleet before they can strike.
* Type: Side
* Goals:
	* Task 1: Goto MITUUL system of Iyatequa's territories
	* Task 2: Pay 1000 RU Type B Refined T2
	* Task 3: 
		* 10 ScannedGenerated
		* Complete 10 side missions
	* Task 4: Goto MITUUL system of Iyatequa's territories

## QM_T2_STARTRESEARCHT2INTC
* Name: Interceptor T2
* Description: We can research better ship blueprints using the new materials found in this region.
* Type: Main
* FollowUps: ql_main_t2_strikeCraftCraft
* Goals:
	* Task 1: Start Research - rp_catStrCraft_bp_sf_intc_t2_c

## QM_T2_FINRESEARCHT2INTC
* Name: Interceptor Schematics
* Description: Schematics research unlock new blueprints for the fabricators and shipyard.
* Type: Main
* Goals:
	* Task 1: Craft

## QM_T2_INTROPARTS
* Name: Ship Parts Assembly
* Description: The new constructions will require the use of specially fabricated parts.

The blueprints for small Hull, Weapon and Machinery parts can be found in the market.
* Type: Main
* Goals:
	* Task 1: Buy: bp_intmed_ship_small_t2
	* Task 2: Craft

## QM_T2_STRIKECRAFT
* Name: Strike Craft T2
* Description: Now that we have finished the research and crafted the necessary parts, we can craft an interceptor squadron.
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

## QM_T2_FACHIIGARAN
* Name: Lazarus Repairs
* Description: Lazarus Station was recently attacked. Command asked us to help with rebuilding efforts.
* Type: Main
* FollowUps: ql_main_t2_researchEscort
* Goals:
	* Task 1: Complete 3 of qm_t2_facHiigaran_A|qm_t2_facHiigaran_B|qm_t2_facHiigaran_C|qm_t2_facHiigaran_D

## QM_T2_FACHIIGARAN_A
* Name: Repairs: Mining Opportunities
* Description: To repair Lazarus Station, new minerals are needed. We are asked to look for new places to mine and help set up the fabrication systems.
* Type: Side
* Goals:
	* Task 1: Goto KEID system of Iyatequa's territories
	* Task 2: Scan
	* Task 3: Craft
	* Task 4: Pay 1000 RU Type C Refined T2

## QM_T2_FACHIIGARAN_B
* Name: Repairs: Secure the Perimeter
* Description: After the recent attack, we need to secure the borders of Hiigaran space.
* Type: Side
* Goals:
	* Task 1: Goto KISHO RE system of Iyatequa's territories
	* Task 2: Complete 10 side missions
	* Task 3: Craft
	* Task 4: Pay 60 Small Hull Parts

## QM_T2_FACHIIGARAN_C
* Name: Repairs: Motivation Boost
* Description: We are asked to lead several high profile campaigns against enemy forces to rally more Hiigaran fleets and raise awareness to the rebuilding efforts of Lazarus Station.

(The blueprints for small Weapon and Machinery parts can be found in the market.)
* Type: Side
* Goals:
	* Task 1: Goto BISHAAN TEL system of Iyatequa's territories
	* Task 2: 
		* Complete side mission
		* 35 ShipsDestroyed
	* Task 3: Pay 60 Small Weapon Parts

## QM_T2_FACHIIGARAN_D
* Name: Repairs: Empty the Lairs
* Description: The attackers still have their bases of operation. We need to clear them out to prevent future attacks.
* Type: Side
* Goals:
	* Task 1: Goto MARAT KAN system of Iyatequa's territories
	* Task 2: 
		* 35 ScannedBelt
		* 35 ShipsDestroyed
	* Task 3: 
		* Pay 650 RU Type A Ore T2
		* Pay 650 RU Type B Ore T2
		* Pay 650 RU Type C Ore T2

## QM_T2_CRAFTRCOL
* Name: Resource Collector T2
* Description: Mining the new ores can be done faster with special resource collectors equipped with better mining gear.
* Type: Side
* Goals:
	* Task 1: Craft

## QM_T2_RCOLMINING
* Name: Ore Deal
* Description: With our new resource collectors, we can mine ores much faster than before.
* Type: Side
* FollowUps: ql_main_t2_RCon
* Goals:
	* Task 1: 9000 Mined2A_Mined2B_Mined2C_Mined2D

## QM_T2_CRAFTRCON
* Name: Resource Controller
* Description: We acquired a blueprint for the Resource Controller, an escort ship we can send on independent mining missions. Like other escort ships, it must be built in the shipyard.
* Type: Side
* Goals:
	* Task 1: Craft

## QM_T2_INTROIDLEMINE
* Name: Remote Mining
* Description: Resource Controllers can be sent away to mine ores without our supervision. To do that, it must be assigned to an escort slot in fleet configuration.
* Type: Side
* Goals:
	* Task 1: 5000 IdleMined

## QM_T2_STARTRESEARCHT2FRIG
* Name: Assault Frigate T2
* Description: We can research a better assault frigate blueprint using the new minerals.
* Type: Main
* FollowUps: ql_main_t2_oreD
* Goals:
	* Task 1: Start Research - rp_catEscorts_bp_cf_assa_t2_c

## QM_T2_FINRESEARCHT2FRIG
* Name: Assault Frigate Schematics
* Description: Our scientists are at work developing new schematics for the assault frigate.
* Type: Main
* FollowUps:
	* ql_main_t2_craftEscort
	* ql_main_t2_researchPulsarCorvette
* Goals:
	* Task 1: Craft

## QM_T2_INTROORED
* Name: Gold Rush
* Description: Some asteroids in this region contain a rare ore we can use for advanced constructions.
* Type: Side
* Goals:
	* Task 1: 3500 Mined2D
	* Task 2: Craft

## QM_T2_CRAFTUNCSHIP
* Name: Elite Ships
* Description: We acquired a blueprint for an advanced ship design. It requires the rare ore to be built.
* Type: Side
* Goals:
	* Task 1: Craft

## QM_T2_RESEARCHPULSARCORVETTE
* Name: Pulsar Corvette Schematics
* Description: Uncommon, rare and epic researches are not part of the central research path and must be found in order to be researched.

The Pulsar Corvette Schematics can be found in the code fragment market.
* Type: Side
* FollowUps: ql_main_t2_pulsarCorvette
* Goals:
	* Task 1: Craft

## QM_T2_PULSARCORVETTE
* Name: Pulsar Corvette
* Description: Pulsar Corvettes are effective against other corvettes and small escort ships.
* Type: Side
* Goals:
	* Task 1: Craft

## QM_T2_LARGEHULLPARTS
* Name: Large Hull Parts Assembly
* Description: The frigate blueprint requires a large version of the hull parts.

The blueprint for large hull parts can be found in the market.
* Type: Main
* Goals:
	* Task 1: Buy: bp_intmed_ship_large_t2
	* Task 2: Craft

## QM_T2_ESCORT
* Name: Escort Ships T2
* Description: With the large hull parts we can finally construct the frigate.
* Type: Main
* FollowUps:
	* ql_main_t2_introLiaison
	* ql_main_t2_strikeStationDefense
	* ql_raid_014
* Goals:
	* Task 1: Craft

## QM_T2_INTROLIAISON
* Name: Liaison Office
* Description: Doing assignments for the liaison office will allow us to requisition better blueprints and better equipment.
* Type: Main
* FollowUps:
	* ql_main_t2_sideIyat
	* qm_t2_facIyatequa_A
	* qm_t2_facIyatequa_B
	* qm_t2_facIyatequa_C
	* qm_t2_facIyatequa_D
* Goals:
	* Task 1: 3 Faction

## QM_T2_FACIYATEQUA
* Name: Iyatequa Intermediary
* Description: The Iyatequa have offered to liaison between us and the Tanoch if we agree to run some errands for them.
* Type: Main
* FollowUps:
	* ql_main_t2_largeWpnParts
	* ql_main_t2_largeMchParts
* Goals:
	* Task 1: Complete 3 of qm_t2_facIyatequa_A|qm_t2_facIyatequa_B|qm_t2_facIyatequa_C|qm_t2_facIyatequa_D
	* Task 2: Goto LAZARUS system of Hiigaran Medea's territories

## QM_T2_FACIYATEQUA_A
* Name: Intermediary: Delivery Run
* Description: The Iyatequa want us to deliver some resources - from our own pockets. They said the rewards will compensate for our losses. We'll see.
* Type: Side
* Goals:
	* Task 1: Goto SOBEL REM system of Iyatequa's territories
	* Task 2: 
		* Pay 1000 RU Type B Refined T2
		* Pay 1000 RU Type C Refined T2
		* Pay 20 Large Hull Parts
	* Task 3: 7 Faction_Tr1_T2up
	* Task 4: Goto SOBEL REM system of Iyatequa's territories

## QM_T2_FACIYATEQUA_B
* Name: Intermediary: Patrolling Trade Routes
* Description: We're asked to patrol the Iyatequa trading routes and clear out hostiles near them.
* Type: Side
* Goals:
	* Task 1: Goto KISHO RE system of Iyatequa's territories
	* Task 2: 15 ShipsDestroyedProgenitor
	* Task 3: 15 Faction_Tr1_T2up
	* Task 4: Goto KISHO RE system of Iyatequa's territories

## QM_T2_FACIYATEQUA_C
* Name: Intermediary: The Catch
* Description: This assignment seems simple enough. We simply have to find Cangacian fleets and destroy them.
* Type: Side
* Goals:
	* Task 1: Goto MARAT KAN system of Iyatequa's territories
	* Task 2: 30 ShipsDestroyedP1
	* Task 3: 
		* 30 ShipsDestroyed
		* 7 Faction_Tr1_T2up
	* Task 4: Goto MARAT KAN system of Iyatequa's territories

## QM_T2_FACIYATEQUA_D
* Name: Intermediary: Art of Escape
* Description: The Iyatequa want us to find a master thief of legendary reputation.
* Type: Side
* Goals:
	* Task 1: Goto MITUUL system of Iyatequa's territories
	* Task 2: Scan
	* Task 3: GainItem
	* Task 4: 
		* Pay 1 Resource Collector
		* Pay 500 RU Type D Ore T2
	* Task 5: Goto MITUUL system of Iyatequa's territories

## QM_T2_STRIKESTATIONDEFENSE
* Name: Station Defense
* Description: A large Tanoch station is under attack by a large fleet of pirates. We should band together with other fleets to repel the attackers.
* Type: Side
* Goals:
	* Task 1: Complete 1 of qr_014

## QM_T2_LIAISONTANOCH
* Name: Tanoch Relations
* Description: The Tanoch liaison office will offer better items the higher our reputation is.
* Type: Main
* Goals:
	* Task 1: 10 Faction_Tanoch_T2up

## QM_T2_LARGEWEAPONPARTS
* Name: Large Weapon Parts Assembly
* Description: Large weapon parts are required for building flagships and weapon modules.

The blueprint for large weapon parts can be found in the Tanoch liaison requisitions office.
* Type: Main
* FollowUps: ql_main_t2_flagship
* Goals:
	* Task 1: Craft

## QM_T2_LIAISONIYATEQUA
* Name: Iyatequa Relations
* Description: The Iyatequa liaison office will offer better items the higher our reputation is.
* Type: Main
* Goals:
	* Task 1: 10 Faction_Tr1_T2up

## QM_T2_LARGEMACHINEPARTS
* Name: Large Machinery Parts Assembly
* Description: Large machinery parts are required for building flagships and non-weapon modules.

The blueprint for large machinery parts can be found in the Iyatequa liaison requisitions office.
* Type: Main
* FollowUps: ql_main_t2_flagship
* Goals:
	* Task 1: Craft

## QM_T2_STARTCRAFTFLAGSHIP
* Name: Flagship Construction T2
* Description: Now that we have the necessary resources, we can start building our new flagship. Its larger drive core will allow us to enter Tanoch territory. Flagship blueprints are available in the market.
* Type: Main
* FollowUps:
	* ql_Keid
	* ql_main_t2_strikePahrasRock
	* ql_raid_015
* Goals:
	* Task 1: Complete 2 of qm_t2_largeWeaponParts|qm_t2_largeMachineParts
	* Task 2: Start Crafting - Flagship_Ship_T2

## QM_T2_FINCRAFTFLAGSHIP
* Name: Flagship T2
* Description: The construction of our new flagship is under way. Once it's finished, we can switch over and move our squadrons and officers as well as modules to the new flagship.
* Type: Main
* FollowUps:
	* ql_main_t2_tanochet
	* ql_main_t2_turrets
* Goals:
	* Task 1: Craft

## QM_T2_STRIKEPAHRASROCK
* Name: Pahra's Rock
* Description: Pirate's major Asteroid Base in the area has been threatening the Hiigaran settlements. Hiigaran Flagships have been gathered to strike on this Base.​
* Type: Side
* Goals:
	* Task 1: Complete 1 of qr_015

## QM_T2_TURRETS
* Name: Weapon Turrets T2
* Description: We should stay up to date on weapon technology. Researching new weapon schematics will unlock better modules.
* Type: Side
* Goals:
	* Task 1: Craft
	* Task 2: Craft
	* Task 3: Equip Weapon

## QM_T2_TANOCHET
* Name: Tanochet
* Description: We can finally reach the Tanoch capital. It is time to meet the emperor.
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

## QM_T2_INTERNALFABRICATOR
* Name: Fabricator Module
* Description: Our new flagship offers the ability to reconfigure its internal layout.
* Type: Main
* Goals:
	* Task 1: Craft
	* Task 2: Equip Internal

## QM_T2_INTERNALREFINERY
* Name: Refinery Module
* Description: Additional refinery and fabricator modules increase our economic power.
* Type: Main
* Goals:
	* Task 1: Craft
	* Task 2: Equip Internal

## QM_T2_EPICSIGNALS
* Name: High Risk High Reward
* Description: Occasionally we come across high energy signals. It might be worth checking out, but it could also be a potential danger. We should proceed with caution.
* Type: Side
* Goals:
	* Task 1: 
		* Scan
		* Complete side mission

## QM_T2_FACTANOCH
* Name: Tanoch Errands
* Description: The Tanoch have asked us to run some errands for them. This could be a chance for us to gain their trust.
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
	* Task 2: Goto TANOCHETLAN system of Tanoch's territories

## QM_T2_FACTANOCH_A
* Name: Errands: Golden Harvest
* Description: A Tanoch planetary government is experiencing a resource shortfall, and has asked for help with procuring raw material.
* Type: Side
* Goals:
	* Task 1: 40 ScannedBelt
	* Task 2: 
		* Pay 350 RU Type A Refined T2
		* Pay 350 RU Type B Refined T2
		* Pay 350 RU Type C Refined T2

## QM_T2_FACTANOCH_B
* Name: Errands: Safety and Security
* Description: Pirates are attacking Tanoch systems. We've been asked to drive them back.
* Type: Side
* Goals:
	* Task 1: 
		* 350 RepTanoch
		* 15 ShipsDestroyedP1

## QM_T2_FACTANOCH_C
* Name: Errands: Disaster Relief
* Description: A Tanoch world is having trouble getting resources from the Empire so they’ve asked anyone for help.
* Type: Side
* Goals:
	* Task 1: 
		* Craft
		* Craft
	* Task 2: 
		* Pay 350 RU Type B Refined T2
		* Pay 50 Small Machinery Parts
		* Pay 1 Resource Collector

## QM_T2_FACTANOCH_D
* Name: Errands: Hired Defenses
* Description: The border worlds are being threatened from Yaot assaults and are desperate for defenders. They ask us to drive the Yaot back.
* Type: Side
* Goals:
	* Task 1: 
		* Scan
		* 15 ShipsDestroyedYaot

## QM_T2_UPGRADEINTERNALS
* Name: Internal Module Upgrades
* Description: Just like with weapon turrets, we can improve our internal module's performance through upgrades.
* Type: Main
* Goals:
	* Task 1: Craft

## QM_T2_OTHERINTERNALS
* Name: Compartments
* Description: Our flagship is sectioned into three compartments. We can install different modules in different compartments.
* Type: Side
* Goals:
	* Task 1: 
		* Equip Internal
		* Equip Internal

## QM_T2_COMPARTMENTS
* Name: Compartments
* Description: Our flagship is sectioned into three compartments. We can install different modules in different compartments.
* Type: Side
* Goals:
	* Task 1: 
		* Equip Internal
		* Equip Internal

## QM_T2_FACYAOT
* Name: Yaot Conflict
* Description: We have received assignments from both Tanochetlan and Lazarus station. They asked us to investigate the Yaot threat.
* Type: Main
* FollowUps: ql_main_t2_templeTonaati
* Goals:
	* Task 1: Complete 3 of qm_t2_facYaot_A|qm_t2_facYaot_B|qm_t2_facYaot_C|qm_t2_facYaot_D
	* Task 2: Goto TANOCHETLAN system of Tanoch's territories

## QM_T2_FACYAOT_A
* Name: Conflict: Direct Attack
* Description: The Tanoch want us to actively engage the Yaot fleets to disrupt their activities in Tanoch space.
* Type: Side
* Goals:
	* Task 1: 30 ShipsDestroyedYaot

## QM_T2_FACYAOT_B
* Name: Conflict: Hazardous Archeology
* Description: We are looking for evidence of a missing Progenitor hyperspace gate in the area which should be there but isn’t. According to Tanoch intelligence the Yaot are also seeking this object.
* Type: Side
* Goals:
	* Task 1: 
		* 45 ScannedBelt
		* 1800 Mined2A_Mined2B_Mined2C_Mined2D

## QM_T2_FACYAOT_C
* Name: Conflict: Seek and Find
* Description: A Hiigaran flagship has gone missing in Tanoch space. Preliminary evidence points towards Yaot involvement. Lazarus wants us to investigate.
* Type: Side
* Goals:
	* Task 1: 
		* Scan
		* Complete 10 side missions
		* Scan

## QM_T2_FACYAOT_D
* Name: Conflict: Opposition Research
* Description: The Yaot are the first major antagonistic power we have encountered. We need to make sure our crew is properly trained and ready to handle the upcoming battles.
* Type: Side
* Goals:
	* Task 1: 
		* GainItem
		* UpgradeOfficer

## QM_T2_TEMPLETONAATI
* Name: Temple Tonaati
* Description: We are following Vaygr fleet to find out their hidden plan.
* Type: Main
* FollowUps:
	* ql_Exile
	* ql_side_exploration
	* ql_main_t3_jumpCap
* Goals:
	* Task 1: Complete mission 'Temple Tonaati'

## QM_T3_RESEARCHJUMPCAP
* Name: Expanding the Horizon
* Description: Our scientists have come up with new theories on how to increase the power of our engines. With the new technology we should be able to enter space that was previously inaccessible to us.
* Type: Main
* FollowUps: ql_main_t3_intro
* Goals:
	* Task 1: Craft

## QM_T3_SCOUTING
* Name: New Frontiers
* Description: With our improved hyperjump technology, we should upgrade our engines and sensors to explore the new areas.
* Type: Main
* Goals:
	* Task 1: 
		* Craft
		* Craft

## QM_T3_SCOUTING_SCANBELTS
* Name: Resource Scouting
* Description: Fleet command wants accurate maps of nearby asteroid clusters in order to chart resources and hazards. Contribute to this effort by scanning asteroid clusters.
* Type: Main
* Goals:
	* Task 1: 55 ScannedBelt

## QM_T3_SCOUTING_SCANJOVIAN
* Name: Gas Giant Scan
* Description: New scanning protocols for scanning gas giants are being tested. Contribute to this test by fully scanning a gas giant.
* Type: Main
* FollowUps:
	* ql_main_t3_gasMining
	* ql_main_t3_yaotLiaison
* Goals:
	* Task 1: 1 ScannedJovian

## QM_T3_GASMINING
* Name: A New Resource
* Description: We found a new type of resource that warrants a closer look. We should take some samples for study. To harvest gas, simply send a Gas Collector into the atmosphere of a gas planet. Be careful. Deeper layers will deal more damage to your ships! The blueprint for the Gas Collector can be found in the Market.
* Type: Main
* FollowUps:
	* ql_main_t3_sideYaot
	* ql_main_t3_sideYaot_A
	* ql_main_t3_sideYaot_B
	* ql_main_t3_sideYaot_C
* Goals:
	* Task 1: Craft
	* Task 2: 1000 Mined3E_Mined3F_Mined3G_Mined3H

## QM_T3_YAOTLIAISON
* Name: Yaot Relations
* Description: The Yaot have opened their liaison office to us.
* Type: Side
* Goals:
	* Task 1: 1000 RepYaot

## QM_T3_FACYAOT
* Name: Uneasy Allies
* Description: The Yaot are interested in opening relations with us and wish to begin a dialogue.
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
	* Task 2: Goto YAOTL system of Yaot's territories

## QM_T3_SIDEYAOT_A_1
* Name: Truce: Loadstones I
* Description: The Yaot present a simple request to map and gather resources in order to test our capabilities and their trust in us.
* Type: Side
* Goals:
	* Task 1: 
		* 65 ScannedBelt
		* Pay 50 RU Type B Refined T3

## QM_T3_SIDEYAOT_A_2
* Name: Truce: Loadstones II
* Description: The Yaot have asked us to collect further resources and clear the mining areas of hostiles.
* Type: Side
* Goals:
	* Task 1: 
		* 2500 Mined3C
		* 30 ShipsDestroyed

## QM_T3_SIDEYAOT_A_3
* Name: Truce: Loadstones III
* Description: The Yaot are interested in learning our capacity for materials refining. We'll be compensated well.
* Type: Side
* Goals:
	* Task 1: 
		* 300 Refining3N
		* Pay 100 RU Type A Refined T3

## QM_T3_SIDEYAOT_B_1
* Name: Truce: The Privateer I
* Description: The Yaot have a supply line they want protected, and are willing to hire us to clear it of hostiles.
* Type: Side
* Goals:
	* Task 1: 
		* Scan
		* Complete 6 side missions

## QM_T3_SIDEYAOT_B_2
* Name: Truce: The Privateer II
* Description: The Yaot wish to commission us to guard this patrol route until their own patrols can relieve us.
* Type: Side
* Goals:
	* Task 1: 
		* 30 ShipsDestroyed
		* GainItem

## QM_T3_SIDEYAOT_B_3
* Name: Truce: The Privateer III
* Description: The Yaot are impressed with our combat capabilities and want to see how we fare against stronger enemies.
* Type: Side
* Goals:
	* Task 1: Complete 3 side missions

## QM_T3_SIDEYAOT_C_1
* Name: Truce: Exchange of Ideas I
* Description: The Yaot have made more contracts available to us on a trial basis. We should engage them.
* Type: Side
* Goals:
	* Task 1: 5 Faction_Yaot_T3up

## QM_T3_SIDEYAOT_C_2
* Name: Truce: Exchange of Ideas II
* Description: The Yaot are becoming more comfortable with employing us. More work for them will go a long way to improving relations.
* Type: Side
* Goals:
	* Task 1: 
		* 250 RepYaot
		* 30 ShipsDestroyed

## QM_T3_SIDEYAOT_C_3
* Name: Truce: Exchange of Ideas III
* Description: The Yaot trust us enough to employ our services on a contract basis. More work is available.
* Type: Side
* Goals:
	* Task 1: 
		* GainItem
		* 4050 RepYaot

## QM_T3_FACTANOCH
* Name: Inside the Empire
* Description: We have been contacted by the Chicuat people within the Tanoch empire. They have been denied Imperial services and are asking us for help.
* Type: Main
* FollowUps:
	* ql_raid_018
	* ql_main_t3_starTotek
* Goals:
	* Task 1: Complete 2 of qm_t3_sideTanoch_A_3|qm_t3_sideTanoch_B_3|qm_t3_sideTanoch_C_3
	* Task 2: Goto TANOCHETLAN system of Tanoch's territories

## QM_T3_SIDETANOCH_A_1
* Name: Chicuat: Dry Well I
* Description: Next to no Imperial resources are reaching the Chicuat worlds. They are asking us to provide what we spare.
* Type: Side
* Goals:
	* Task 1: 
		* Pay 400 RU Type A Ore T3
		* Pay 200 RU Type B Ore T3
		* Pay 1400 RU Type C Ore T3

## QM_T3_SIDETANOCH_A_2
* Name: Chicuat: Dry Well II
* Description: The Chicuat refineries are busy with the ores we have provided. Meanwhile, an agricultural colony providing most of the food in the sector is running on systems that are barely holding together. They have asked us for spare parts.
* Type: Side
* Goals:
	* Task 1: Pay 15 Large Machinery Parts

## QM_T3_SIDETANOCH_A_3
* Name: Chicuat: Dry Well III
* Description: The economic system has been stabilized, but without proper defenses, raiders will undo everything we've done. We should provide them with some fighters of their own and give their militia some training.
* Type: Side
* Goals:
	* Task 1: 
		* Pay 50 Small Hull Parts
		* Pay 50 Small Weapon Parts
	* Task 2: Complete 5 side missions

## QM_T3_SIDETANOCH_B_1
* Name: Chicuat: Exposed I
* Description: Without Imperial patrols, Chicuat space is vulnerable against raiders. They have asked us to make a sweep across their space to clear the sector of hostiles.
* Type: Side
* Goals:
	* Task 1: 
		* Scan
		* 35 ShipsDestroyed

## QM_T3_SIDETANOCH_B_2
* Name: Chicuat: Exposed II
* Description: Most hostiles have been chased off, but some bold bands of the Fleet of Rams have refused to be intimidated. It is time to make a statement.
* Type: Side
* Goals:
	* Task 1: 
		* Complete 7 side missions
		* 25 ShipsDestroyedP1

## QM_T3_SIDETANOCH_B_3
* Name: Chicuat: Exposed III
* Description: The Chicuat officials have seen our results and several of them want to see us in action. They hope to learn from us how to organize their defenses better.
* Type: Side
* Goals:
	* Task 1: 
		* Complete 3 side missions
		* GainItem

## QM_T3_SIDETANOCH_C_1
* Name: Chicuat: Favors I
* Description: Our contact has suggested running some errands for the Tanoch in the name of the Chicuat people. Doing so would hopefully increase the Chicuat's standing within the Empire.
* Type: Side
* Goals:
	* Task 1: 500 RepTanoch

## QM_T3_SIDETANOCH_C_2
* Name: Chicuat: Favors II
* Description: The Empire is reacting to our support of the Chicuat people. While we wait to learn more about the outcome, the Chicuat have asked if their officers can cross-train with ours.
* Type: Side
* Goals:
	* Task 1: 
		* UpgradeOfficer
		* 7 Faction_Tanoch_T2up

## QM_T3_SIDETANOCH_C_3
* Name: Chicuat: Favors III
* Description: After lengthy negotiations with the Chicuat, the Empire reluctantly has agreed to a relief operation, sending resources to worlds in need. Naturally they ask us for support instead of sending their own materials...
* Type: Side
* Goals:
	* Task 1: 
		* 8500 RepTanoch
		* 600 Refining3N_Refining3O_Refining3P_Refining3Q

## QM_T3_STARTOTEK
* Name: Star Totek
* Description: We are closing in on possible Vaygr transmissions close to the star.
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

## QM_T3_STRIKEBREACH
* Name: Breach
* Description: We found an enemy base that is heavily fortified. Breaching its defenses will not be easy.
* Type: Side
* Goals:
	* Task 1: Complete 1 of qr_019

## QM_T3_FACHIIGARAN
* Name: Planting the Flag
* Description: Lazarus Base calls us back to the Hiigaran colonies to establish a presence there and keep the peace.
* Type: Main
* FollowUps:
	* ql_main_t3_sideIyat
	* ql_main_t3_sideIyat_A
	* ql_main_t3_sideIyat_B
	* ql_main_t3_sideIyat_C
* Goals:
	* Task 1: Complete 2 of qm_t3_sideHiigaran_A_3|qm_t3_sideHiigaran_B_3|qm_t3_sideHiigaran_C_3
	* Task 2: Goto LAZARUS system of Hiigaran Medea's territories

## QM_T3_SIDEHIIGARAN_A_1
* Name: Colonies: Brick Making I
* Description: Hiigaran resource efforts are very short handed, so we’ll be going to assist gas collection in deep space.
* Type: Side
* Goals:
	* Task 1: 
		* 20 ScannedJovian
		* 600 Mined3E_Mined3F_Mined3G_Mined3H

## QM_T3_SIDEHIIGARAN_A_2
* Name: Colonies: Brick Making II
* Description: Our assistance has been helpful so far, but we are asked to provide and analyze some ore samples from the deeper regions of the galaxy.
* Type: Side
* Goals:
	* Task 1: 
		* 5000 Mined3A_Mined3B_Mined3C_Mined3D
		* GainItem

## QM_T3_SIDEHIIGARAN_A_3
* Name: Colonies: Brick Making III
* Description: The logistics have been set up for the most part, but we are asked to help with some deliveries.
* Type: Side
* Goals:
	* Task 1: 
		* Pay 100 GU Type G Gas T3
		* Pay 200 RU Type B Refined T3
		* Pay 40 Small Hull Parts

## QM_T3_SIDEHIIGARAN_B_1
* Name: Colonies: Security Blanket I
* Description: Lazarus base has established a quota for all commanders hunting loose pirates in Hiigaran space.
* Type: Side
* Goals:
	* Task 1: 
		* 30 ShipsDestroyedP1
		* GainItem

## QM_T3_SIDEHIIGARAN_B_2
* Name: Colonies: Security Blanket II
* Description: Most pirates have gone into hiding, but we are asked to make sweeps of local space, to flush out the remaining hostiles.
* Type: Side
* Goals:
	* Task 1: 
		* Scan
		* Complete 5 side missions

## QM_T3_SIDEHIIGARAN_B_3
* Name: Colonies: Security Blanket III
* Description: The hostile presence has been reduced to a manageable level, but Progenitor craft threaten research vessels. We need to get rid of them and analyze some of the debris.
* Type: Side
* Goals:
	* Task 1: 
		* 15 ShipsDestroyedProgenitor
		* GainItem

## QM_T3_SIDEHIIGARAN_C_1
* Name: Colonies: The Next Generation I
* Description: Lazarus has sent us some trainees to get some practical experience on our ship.
* Type: Side
* Goals:
	* Task 1: 
		* GainItem
		* 2000 PlayerXP

## QM_T3_SIDEHIIGARAN_C_2
* Name: Colonies: The Next Generation II
* Description: Many of the trainees are going to become pilots and navigators, but have so far trained in controlled or virtual flight simulators. They need some real experience.
* Type: Side
* Goals:
	* Task 1: 
		* Craft
		* UpgradeOfficer

## QM_T3_SIDEHIIGARAN_C_3
* Name: Colonies: The Next Generation III
* Description: The final course is the graduation level for the trainees, who must see actual combat. You are to take the crew into battle and complete the course. Once finished, they return to Lazarus to finish up their coursework.
* Type: Side
* Goals:
	* Task 1: Complete 10 side missions
	* Task 2: UpgradeOfficer

## QM_T3_FACIYATEQUA
* Name: Blue Collar Work
* Description: Ekekko informed us about exclusive work needed by the Iyatequa, and the traders will pay well for this assistance. This is below the table work on various jobs they don’t widely advertise for. They do not say what the ultimate purpose of this work is, though.
* Type: Main
* FollowUps:
	* ql_main_t3_Cang
	* ql_main_t3_Cang_A
	* ql_main_t3_Cang_B
	* ql_main_t3_Cang_C
* Goals:
	* Task 1: Complete 2 of qm_t3_sideIyatequa_A_3|qm_t3_sideIyatequa_B_3|qm_t3_sideIyatequa_C_3
	* Task 2: Goto SARAAL system of Iyatequa's territories

## QM_T3_SIDEIYATEQUA_A_1
* Name: Contracts: The Empty Quarter I
* Description: A small world in the Empty Quarter is looking for trustworthy connections. They offer an assortment of various tasks.
* Type: Side
* Goals:
	* Task 1: 
		* 7 Faction_Tr1_T3up
		* 2250 PlayerXP

## QM_T3_SIDEIYATEQUA_A_2
* Name: Contracts: The Empty Quarter II
* Description: A wealthy socialite has heard of our accomplishments and wants some things done. Discreetly, of course.
* Type: Side
* Goals:
	* Task 1: 
		* 500 RepTr1
		* 1000 Refining3N_Refining3O_Refining3P_Refining3Q

## QM_T3_SIDEIYATEQUA_A_3
* Name: Contracts: The Empty Quarter III
* Description: Our contact in the Empty Quarter is looking for new opportunities and has been pleased with our work so far. They want us to scout out new areas of space in order to expand their influence.
* Type: Side
* Goals:
	* Task 1: 
		* 8500 RepTr1
		* Scan

## QM_T3_SIDEIYATEQUA_B_1
* Name: Contracts: Territory Claim I
* Description: The Iyatequa plan to set up new trading routes in space currently riddled by pirates. They asked us to clean up the area.
* Type: Side
* Goals:
	* Task 1: 
		* Scan
		* 35 ShipsDestroyedP1

## QM_T3_SIDEIYATEQUA_B_2
* Name: Contracts: Territory Claim II
* Description: Some pirates apparently didn't get the hint yet. We should show them the Iyatequa mean business.
* Type: Side
* Goals:
	* Task 1: 
		* Complete 8 side missions
		* GainItem

## QM_T3_SIDEIYATEQUA_B_3
* Name: Contracts: Territory Claim III
* Description: Most pirates have dispersed, but just to make sure they do not come back we should increase our reputation so future raiders will think twice before setting up nests here.
* Type: Side
* Goals:
	* Task 1: 
		* Complete 5 side missions
		* Complete 2 side missions

## QM_T3_SIDEIYATEQUA_C_1
* Name: Contracts: Supplies I
* Description: A local world wants help building and supplying a space station. We are asked to test possible mining sites and clear them of hostiles.
* Type: Side
* Goals:
	* Task 1: 
		* 6000 Mined3A_Mined3B_Mined3C_Mined3D
		* 55 ShipsDestroyed

## QM_T3_SIDEIYATEQUA_C_2
* Name: Contracts: Supplies II
* Description: Mining ships have departed for the asteroids we have charted, but the internal systems require special gases. We are asked to sample the gases at promising jovians.
* Type: Side
* Goals:
	* Task 1: 
		* 600 Mined3E_Mined3F_Mined3G_Mined3H
		* 100 Mined3H

## QM_T3_SIDEIYATEQUA_C_3
* Name: Contracts: Supplies III
* Description: The mining sites have been prepared, but the Iyatequa asked us with further assistance through supplies and mining craft.
* Type: Side
* Goals:
	* Task 1: 
		* Pay 150 GU Type G Gas T3
		* Pay 300 RU Type B Refined T3
		* Pay 50 Small Hull Parts

## QM_T3_FACCANGACIAN
* Name: Roadblocks
* Description: Reports at the Tanoch border are coming in stating that the Fleet of Rams, Supay’s army, is on the move at last.
* Type: Main
* FollowUps: ql_main_t3_sijinLighthouse
* Goals:
	* Task 1: Complete 2 of qm_t3_sideCangacian_A_3|qm_t3_sideCangacian_B_3|qm_t3_sideCangacian_C_3

## QM_T3_SIDECANGACIAN_A_1
* Name: Defense: Intercept I
* Description: We are asked to intercept as many Cangacian fleets as we can.
* Type: Side
* Goals:
	* Task 1: 
		* 40 ShipsDestroyedP1
		* GainItem

## QM_T3_SIDECANGACIAN_A_2
* Name: Defense: Intercept II
* Description: The Cangacians continue to probe the Tanoch defenses. We should look for suspicious activity.
* Type: Side
* Goals:
	* Task 1: 
		* Scan
		* Complete 9 side missions

## QM_T3_SIDECANGACIAN_A_3
* Name: Defense: Intercept III
* Description: Supay's fleets may have holdouts in systems we have not been looking yet. We should find those and flush them out.
* Type: Side
* Goals:
	* Task 1: 
		* Complete 4 side missions
		* Scan

## QM_T3_SIDECANGACIAN_B_1
* Name: Defense: Assist I
* Description: To counter these attacks our crew must be well trained.
* Type: Side
* Goals:
	* Task 1: 
		* GainItem
		* UpgradeOfficer

## QM_T3_SIDECANGACIAN_B_2
* Name: Defense: Assist II
* Description: Our crew is analyzing the attack patterns to find ways to predict where the Fleet of Rams may strike next.
* Type: Side
* Goals:
	* Task 1: 
		* GainItem
		* 2500 PlayerXP

## QM_T3_SIDECANGACIAN_B_3
* Name: Defense: Assist III
* Description: Several smaller worlds on the border have sent us some of their recruits, in hopes they could get some practical experience from our battles with the Cangacians.
* Type: Side
* Goals:
	* Task 1: Complete 10 side missions
	* Task 2: UpgradeOfficer

## QM_T3_SIDECANGACIAN_C_1
* Name: Defense: Barricade I
* Description: Several mining fleets of the border systems have taken losses and are asking us to provide them with safe locations to find resources.
* Type: Side
* Goals:
	* Task 1: 
		* 80 ScannedBelt
		* 1500 Refining3N_Refining3O_Refining3P_Refining3Q

## QM_T3_SIDECANGACIAN_C_2
* Name: Defense: Barricade II
* Description: The remaining mining fleets are flocking to the new mining spots, but they require gases for advanced weaponry.
* Type: Side
* Goals:
	* Task 1: 
		* 40 ScannedJovian
		* 750 Mined3E_Mined3F_Mined3G_Mined3H

## QM_T3_SIDECANGACIAN_C_3
* Name: Defense: Barricade III
* Description: The border worlds' new mining lanes are buzzing with activity, but they need supplies to build up defenses against future raids.
* Type: Side
* Goals:
	* Task 1: 
		* Pay 20 Small Hull Parts
		* Pay 20 Small Weapon Parts
		* Pay 20 Small Machinery Parts

## QM_T3_SIJINLIGHTHOUSE
* Name: Sijin Lighthouse
* Description: We detected a possible signal from the missing Khar-Kalaad.
* Type: Main
* CinematicIds: 40
* FollowUps: ql_main_t4_intro
* Goals:
	* Task 1: Complete mission 'Sijin Lighthouse'

## QM_T4_RESEARCHJUMPCAP
* Name: Mind the Gap
* Description: Crossing the Nightmare Gulf requires an upgrade to our hyperjump technology. After some scans of the gate at Sijin Lighthouse, our scientists think they are able to make the leap possible.
* Type: Main
* FollowUps: ql_main_t4_iliyinLighthouse
* Goals:
	* Task 1: Craft

## QM_T4_ILIYINLIGHTHOUSE
* Name: Iliyin Lighthouse
* Description: We have arrived at another lighthouse in uncharted territory. Be prepared for anything.
* Type: Main
* FollowUps:
	* ql_raid_020
	* ql_raid_021
	* ql_raid_022
	* ql_main_t4_amassariLiaison
	* ql_main_t4_moonResources
* Goals:
	* Task 1: Complete mission 'Iliyin Lighthouse'

## QM_T4_AMASSARILIAISON
* Name: Amassari Relations
* Description: The Amassari have opened their liaison office to us.
* Type: Side
* Goals:
	* Task 1: 1000 RepAmassari

## QM_T4_MOONRESOURCES
* Name: Crystals
* Description: Crystals are a new type of resource that can be combined with refined metals into a composite material needed for advanced constructions. So far we have only been able to find them by chance in <color=#FBB03F>signals and liaison missions</color>.
* Type: Main
* FollowUps: ql_main_t4_brightTemple
* Goals:
	* Task 1: GainItem
	* Task 2: 100 Refining4V_Refining4W_Refining4X_Refining4Y

## QM_T4_BRIGHTTEMPLE
* Name: Bright Temple
* Description: The Amassari here may contain answers about the nature of the Progenitor observer.
* Type: Main
* FollowUps: ql_main_t4_postBrightTemple
* Goals:
	* Task 1: Complete mission 'Bright Temple'

## QM_T4_POSTBRIGHTTEMPLE_1
* Name: Among the People
* Description: We should take this time to become better acquainted with the Amassari and their culture. Performing tasks for the assorted groups will accomplish this.
* Type: Main
* Goals:
	* Task 1: 1000 RepAmassari

## QM_T4_POSTBRIGHTTEMPLE_2
* Name: Fabrication Methods
* Description: A new technique for refining was discovered from the Amassari. Test this process by refining rare earths.
* Type: Main
* Goals:
	* Task 1: GainItem

## QM_T4_POSTBRIGHTTEMPLE_3
* Name: Experience and Knowledge
* Description: Our crews need a new round of training to become familiar with Amassari practices and tactics.
* Type: Main
* FollowUps: ql_main_t4_hataldan
* Goals:
	* Task 1: GainItem

## QM_T4_HATALDAN
* Name: Hataldan
* Description: The fallen capital of the Amassari, and last known position of the Observer.
* Type: Main
* FollowUps: ql_main_t4_postHataldan
* Goals:
	* Task 1: Complete mission 'Hataldan'

## QM_T4_POSTHATALDAN_1
* Name: The Hunt Begins
* Description: The search begins for Kidara and the stolen Observer. We must examine any objects we can find scattered around for clues about her whereabouts.
* Type: Main
* Goals:
	* Task 1: Scan

## QM_T4_POSTHATALDAN_2
* Name: Forcible Interrogation
* Description: Destroying Kiithless ships and scavenging their databanks could fill some gaps in our intelligence about the Kiithless. The hunt continues!
* Type: Main
* Goals:
	* Task 1: 50 ShipsDestroyedDarkHiigaranT4

## QM_T4_POSTHATALDAN_3
* Name: Pieces of the Puzzle
* Description: A cryptic clue that emerged from harvesting Kiithless vessels may have a solution if we can piece together a saga from the Hagthar Empire. Collect relics from these ancient people.
* Type: Main
* FollowUps: ql_main_t4_nightmareGulf
* Goals:
	* Task 1: GainItem

## QM_T4_NIGHTMAREGULF
* Name: Nightmare Gulf
* Description: The Hagthar knew of pockets and safe regions close to this massive interstellar storm. We now know the way to Kidara's hideout in The Nightmare Gulf. It's time to end this.
* Type: Main
* FollowUps:
	* ql_raid_023
	* ql_main_t4_strikeNightmareGulf
	* ql_main_t4_tanWin
* Goals:
	* Task 1: Complete mission 'Nightmare Gulf'

## QM_T4_STRIKENIGHTMAREGULF
* Name: Strike at Nightmare Gulf
* Description: The Hagthar knew of pockets and safe regions close to this massive interstellar storm. We now know the way to Kidara's hideout in The Nightmare Gulf. It's time to end this.
* Type: Side
* Goals:
	* Task 1: Complete 1 of qr_023

## QM_T4_TANWIN_DEFENDBASE
* Name: Gesture of Aid
* Description: We received emergency communication from the Chicuat Elders. They anticipate a raid on one of their remote trading stations. Toci asks us to take on the defense in order to relieve the weakened and overextended Chicuat forces.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Type: Main
* Goals:
	* Task 1: Complete mission 'Repulse Raid T4'

## QM_T4_TANWIN_ATTACKBASE
* Name: In the Shadows
* Description: Intelligence from the Chicuat points to a Tecuban base operating around an uninhabited planet. We must go there and eliminate this base to stop the raids.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Type: Main
* Goals:
	* Task 1: Complete mission 'Base Busting T4'

## QM_T4_TANWIN_RELIC
* Name: Attack the Vaygr
* Description: In our search for the Vaygr involved with the Tecuban, we aquired one of their communication frequencies. If we contact the Vaygr now, we should be able to trace their signal and hyper jump to their exact location.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Type: Main
* Goals:
	* Task 1: Complete mission 'Destination T4'

## QM_T4_TANWIN_ACADEMY
* Name: Showdown at the Academy
* Description: We finally learned Jochik Kaan's intentions. He sparked the flames of war to weaken the Chicuat defenses and steal the Baetyl from Tlapallan Academy, one of their key centers of learning. We must travel there at once, before it is too late.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Type: Main
* FollowUps: ql_main_t4_yaoSpr
* Goals:
	* Task 1: Complete mission 'Tlapallan Academy T4'

## QM_T4_YAOSPR_CONJUNCTION
* Name: The Promised Place
* Description: Chocoan has provided the coordinates to the next astral conjunction event. Strong hostile forces are to be expected in this system. Our goal is to both protect the civilian pilgrims and find out more about the suspected secret agenda of the Yaot Elders.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Type: Main
* Goals:
	* Task 1: Complete mission 'Conjunction T4'

## QM_ORB_T3_COMPONENTS
* Name: Starbase Components
* Description: <color=#FBB03F>The blueprints for starbase components can be found in the liaison requisitions offices.</color>

Our engineers have come up with a plan to build a starbase, which will serve as our base of operations. Before we can do that, however, we need to construct the necessary components.
* Type: Side
* Goals:
	* Task 1: 
		* Craft
		* Craft
		* Craft

## QM_ORB_T3_ORBITAL
* Name: Starbase
* Description: <color=#FBB03F>The blueprint for the starbase can be found in the regular market.</color>

Now that we have the components, we can build the starbase proper. Once the pieces have been constructed, it can be quickly assembled in orbit around celestial objects.
* Type: Side
* Goals:
	* Task 1: Craft

## QM_ORB_T3_PLACEORBITAL
* Name: Starbase Placement
* Description: <color=#FBB03F>Place or relocate your starbase by selecting a celestial object in the target list inside the star system view.</color>

Our finished starbase is ready and can be placed in orbit of a planet or moon.
* Type: Side
* Goals:
	* Task 1: PlaceOrbital

## QM_ORB_T3_MODULES
* Name: Starbase Modules
* Description: <color=#FBB03F>The regular fabricator and refinery module can be mounted on the starbase, but there are specialized starbase modules. Blueprints for some of those can be found in the liaison requisitions offices.</color>

Now that our starbase is finished, we can start filling it up with modules.
* Type: Side
* Goals:
	* Task 1: Equip Internal

## QS_EXPLORATION_01
* Name: Exploration I
* Description: We should explore this galaxy further. Who knows what we could find.
* Type: Side
* FollowUps: ql_side_001
* Goals:
	* Task 1: 
		* Scan
		* Complete 10 side missions

## QS_EXPLORATION_02
* Name: Exploration II
* Description: We have made discoveries that will keep our scientists busy for months.
* Type: Side
* FollowUps: ql_side_002
* Goals:
	* Task 1: GainItem

## QS_EXPLORATION_03
* Name: Exploration III
* Description: This galaxy is full of danger and opportunity. We should analyze and prepare.
* Type: Side
* FollowUps: ql_Ytep
* Goals:
	* Task 1: Scan
	* Task 2: Pay 5000 RU Type C Refined T2

## QS_ECONOMY_01
* Name: Production I
* Description: Building up a fleet requires a constant supply of materials.
* Type: Side
* Goals:
	* Task 1: 
		* Craft
		* Complete 5 side missions

## QS_ECONOMY_02
* Name: Production II
* Description: We should not let our fabrication modules go idle.
* Type: Side
* Goals:
	* Task 1: Craft

## QS_ECONOMY_03
* Name: Production III
* Description: Building bigger and greater ships will require bigger and greater materials.
* Type: Side
* Goals:
	* Task 1: Craft
	* Task 2: Pay 5000 RU Type A Refined T2

## QS_BATTLE_01
* Name: Combat I
* Description: Space is full of danger. We need to be prepared.
* Type: Side
* Goals:
	* Task 1: 
		* Craft
		* Complete 15 side missions

## QS_BATTLE_02
* Name: Combat II
* Description: We need allies if we are to survive in this galaxy.
* Type: Side
* Goals:
	* Task 1: 25 Faction_T2up

## QS_BATTLE_03
* Name: Combat III
* Description: Only great challenges yield great rewards.
* Type: Side
* Goals:
	* Task 1: Complete side mission
	* Task 2: Pay 5000 RU Type B Refined T2

## QS_UNLOCKSTRIKES_T1
* Name: Rising to the Challenge
* Description: As we venture further into this galaxy, we will encounter greater and greater threats. We need to be prepared.
* Type: Side
* Goals:
	* Task 1: Goto TOCHTEPE system of Tanoch's territories
	* Task 2: Scan

## QS_UNLOCKSTRIKES_T2
* Name: Rising to the Challenge
* Description: As we venture further into this galaxy, we will encounter greater and greater threats. We need to be prepared.
* Type: Side
* FollowUps:
	* ql_raid_014
	* ql_raid_015
	* ql_raid_016
* Goals:
	* Task 1: Equip Flagship

## QS_UNLOCKSTRIKES_T3
* Name: Rising to the Challenge
* Description: As we venture further into this galaxy, we will encounter greater and greater threats. We need to be prepared.
* Type: Side
* FollowUps:
	* ql_raid_017
	* ql_raid_018
* Goals:
	* Task 1: Equip Flagship

## QS_KEID_01
* Name: The Siege of Keid
* Description: Keid is struggling under the weight of enemy attacks and depleted resources. Help them take back control of the system.
* Type: Side
* Goals:
	* Task 1: Goto KEID system of Iyatequa's territories
	* Task 2: 
		* Scan
		* Complete 10 side missions
		* 50 ShipsDestroyedT2

## QS_KEID_02
* Name: Rebuilding Keid
* Description: The people of Keid suffer from a lack of resources. Support them by collecting and refining resources.
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

## QS_KEID_03
* Name: The Future of Keid
* Description: Donate your hard-earned resources and credits so that the people of Keid may fight on.
* Type: Side
* Goals:
	* Task 1: 
		* Pay 1000 RU Type A Refined T2 in KEID system of Iyatequa's territories
		* Pay 1000 RU Type B Refined T2 in KEID system of Iyatequa's territories
		* Pay 1000 RU Type C Refined T2 in KEID system of Iyatequa's territories
	* Task 2: 
		* Pay 700 RU Type D Refined T2 in KEID system of Iyatequa's territories
		* Pay 10000 Credits in KEID system of Iyatequa's territories

## QS_EXILE_01
* Name: A Test of Might
* Description: Destroy pirates and complete strikes to prove your strength.
* Type: Side
* Goals:
	* Task 1: 
		* Complete 10 side missions
		* 150 ShipsDestroyedP1

## QS_EXILE_02
* Name: The Nomad's Walk
* Description: Gather resources and craft units to demonstrate your independence and self-reliance.
* Type: Side
* Goals:
	* Task 1: 
		* 15000 Mined2A
		* 15000 Mined2B
		* 15000 Mined2C
	* Task 2: Craft

## QS_EXILE_03
* Name: The Cartographer's Promise
* Description: Travel across the galaxy and discover new locations to help chart the unknown.
* Type: Side
* Goals:
	* Task 1: 
		* Goto ESTRAIIR system of Iyatequa's territories
		* Goto TUNDA MIRAAN system of Yaot's territories
		* Goto AXOCOTIL system of Tanoch's territories
	* Task 2: Scan

## QS_YTEP_01
* Name: Ytep Under Fire
* Description: Help the people of Ytep take back control of the system by pushing back enemies.
* Type: Side
* Goals:
	* Task 1: Goto YTEP system of Yaot's territories
	* Task 2: 
		* Scan
		* Complete 10 side missions
		* 75 ShipsDestroyedT3

## QS_YTEP_02
* Name: Supplying the War Effort
* Description: Collect enough parts and ships to support the war effort in Ytep.
* Type: Side
* Goals:
	* Task 1: 
		* Craft
		* Craft
		* Craft
	* Task 2: 
		* Craft
		* Craft

## QS_YTEP_03
* Name: To Strengthen Ytep
* Description: Donate T2 parts and ships to help the people of Ytep fight after you are gone.
* Type: Side
* Goals:
	* Task 1: 
		* Pay 20 Small Hull Parts in YTEP system of Yaot's territories
		* Pay 800 Small Weapon Parts in YTEP system of Yaot's territories
		* Pay 800 Small Machinery Parts in YTEP system of Yaot's territories
	* Task 2: 
		* Pay 1 Interceptor Squadron in YTEP system of Yaot's territories
		* Pay 1 Assault Corvette Squadron in YTEP system of Yaot's territories

## QS_KILLPIRATE1_PRE01
* Name: Cangacian Raider Fleets I
* Description: Pirates known as the Cangacians are harassing trade fleets of the Iyatequa.
* Type: Achievement
* Goals:
	* Task 1: 10 ShipsDestroyedP1

## QS_KILLPIRATE1_00
* Name: Cangacian Raider Fleets II
* Description: More Cangacian activity is being reported.
* Type: Achievement
* Goals:
	* Task 1: 25 ShipsDestroyedP1

## QS_KILLPIRATE1_01
* Name: Cangacian Raider Fleets III
* Description: Give the pirates a bloody nose. Show them you're no pushover.
* Type: Achievement
* Goals:
	* Task 1: 50 ShipsDestroyedP1

## QS_KILLPIRATE1_02
* Name: Cangacian Raider Fleets IV
* Description: Hunt down pirate ships to suppress their activities in the area.
* Type: Achievement
* Goals:
	* Task 1: 100 ShipsDestroyedP1

## QS_KILLPIRATE1_03
* Name: Cangacian Raider Fleets V
* Description: Beat back the local pirates by eliminating most of their forces.
* Type: Achievement
* FollowUps: ql_esca_killYaot
* Goals:
	* Task 1: 200 ShipsDestroyedP1

## QS_KILLPIRATE1_04
* Name: Cangacian Raider Fleets VI
* Description: An organized pirate force has moved into the area. Show them they are not welcome.
* Type: Achievement
* Goals:
	* Task 1: 400 ShipsDestroyedP1

## QS_KILLPIRATE1_05
* Name: Cangacian Raider Fleets VII
* Description: The Fleet of Rams has increased their presence. Meet them with equal enmity.
* Type: Achievement
* Goals:
	* Task 1: 800 ShipsDestroyedP1

## QS_KILLPIRATE1_06
* Name: Cangacian Raider Fleets VIII
* Description: The Fleet of Rams is hunting the local defenders. Oppose them with force!
* Type: Achievement
* Goals:
	* Task 1: 1600 ShipsDestroyedP1

## QS_KILLPIRATE1_07
* Name: Cangacian Raider Fleets IX
* Description: Supay himself has routed one of his fleets to the area. Engage them at will!
* Type: Achievement
* Goals:
	* Task 1: 3200 ShipsDestroyedP1

## QS_KILLPIRATE1_08
* Name: Cangacian Raider Fleets X
* Description: Send a message to Supay, warlord of the Fleet of Rams. Destroy one of his fleets.
* Type: Achievement
* Goals:
	* Task 1: 6400 ShipsDestroyedP1

## QS_KILLTANOCH_PRE01
* Name: Tanoch Renegade Fleets I
* Description: Renegades of the Tanoch nation are disrupting the peace of the empire.
* Type: Achievement
* Goals:
	* Task 1: 10 ShipsDestroyedTanoch

## QS_KILLTANOCH_00
* Name: Tanoch Renegade Fleets II
* Description: More renegade fleets are being reported.
* Type: Achievement
* Goals:
	* Task 1: 25 ShipsDestroyedTanoch

## QS_KILLTANOCH_01
* Name: Tanoch Renegade Fleets III
* Description: Poach Tanoch patrols to weaken their activities in the area. Hostile Tanoch signals have been located in T2 systems and higher.
* Type: Achievement
* Goals:
	* Task 1: 50 ShipsDestroyedTanoch

## QS_KILLTANOCH_02
* Name: Tanoch Renegade Fleets IV
* Description: Continue to attack Tanoch patrols to weaken their local status. Hostile Tanoch signals have been located in T2 systems and higher.
* Type: Achievement
* Goals:
	* Task 1: 100 ShipsDestroyedTanoch

## QS_KILLTANOCH_03
* Name: Tanoch Renegade Fleets V
* Description: Tanoch freighter crews fear your arrival. Continue the attacks! Hostile Tanoch signals have been located in T2 systems and higher.
* Type: Achievement
* Goals:
	* Task 1: 200 ShipsDestroyedTanoch

## QS_KILLTANOCH_04
* Name: Tanoch Renegade Fleets VI
* Description: Tanoch freighters request action against you. Continue the attacks! Hostile Tanoch signals have been located in T2 systems and higher.
* Type: Achievement
* Goals:
	* Task 1: 400 ShipsDestroyedTanoch

## QS_KILLTANOCH_05
* Name: Tanoch Renegade Fleets VII
* Description: The Tanoch patrol force recognizes you on sight. Continue the attacks! Hostile Tanoch signals have been located in T2 systems and higher.
* Type: Achievement
* Goals:
	* Task 1: 800 ShipsDestroyedTanoch

## QS_KILLTANOCH_06
* Name: Tanoch Renegade Fleets VIII
* Description: Tanoch warning stations alert the Empire to your presence. Continue your attacks! Hostile Tanoch signals have been located in T2 systems and higher.
* Type: Achievement
* Goals:
	* Task 1: 1600 ShipsDestroyedTanoch

## QS_KILLTANOCH_07
* Name: Tanoch Renegade Fleets IX
* Description: The Tanoch regard you as a fleet-level threat. Continue your assaults against them! Hostile Tanoch signals have been located in T2 systems and higher.
* Type: Achievement
* Goals:
	* Task 1: 3200 ShipsDestroyedTanoch

## QS_KILLTANOCH_08
* Name: Tanoch Renegade Fleets X
* Description: The Emperor will know your name. Hostile Tanoch signals have been located in T2 systems and higher.
* Type: Achievement
* Goals:
	* Task 1: 6400 ShipsDestroyedTanoch

## QS_KILLYAOT_PRE01
* Name: Yaot Rebel Fleets I
* Description: Some Yaot that are dissatisfied with the government have begun causing chaos in regional space.
* Type: Achievement
* Goals:
	* Task 1: 10 ShipsDestroyedYaot

## QS_KILLYAOT_00
* Name: Yaot Rebel Fleets II
* Description: More Yaot rebels have been reported.
* Type: Achievement
* Goals:
	* Task 1: 25 ShipsDestroyedYaot

## QS_KILLYAOT_01
* Name: Yaot Rebel Fleets III
* Description: Attack the Yaot patrols to drive them from this area.
* Type: Achievement
* Goals:
	* Task 1: 50 ShipsDestroyedYaot

## QS_KILLYAOT_02
* Name: Yaot Rebel Fleets IV
* Description: Continue attacking the Yaot to drive them from the region.
* Type: Achievement
* Goals:
	* Task 1: 100 ShipsDestroyedYaot

## QS_KILLYAOT_03
* Name: Yaot Rebel Fleets V
* Description: Yaot Fleet captains recognize your silhouette. Continue the attack.
* Type: Achievement
* FollowUps: ql_esca_killTanoch
* Goals:
	* Task 1: 200 ShipsDestroyedYaot

## QS_KILLYAOT_04
* Name: Yaot Rebel Fleets VI
* Description: Yaot sensors are alerted to your presence. Continue the attack!
* Type: Achievement
* Goals:
	* Task 1: 400 ShipsDestroyedYaot

## QS_KILLYAOT_05
* Name: Yaot Rebel Fleets VII
* Description: Yaot Fleet commanders are watching out for you. Continue your assaults against them!
* Type: Achievement
* Goals:
	* Task 1: 800 ShipsDestroyedYaot

## QS_KILLYAOT_06
* Name: Yaot Rebel Fleets VIII
* Description: Your name is mentioned between Yaot Fleet commanders. Continue your attacks!
* Type: Achievement
* Goals:
	* Task 1: 1600 ShipsDestroyedYaot

## QS_KILLYAOT_07
* Name: Yaot Rebel Fleets IX
* Description: You are impacting Yaot fleet operations in this area. Continue your attack!
* Type: Achievement
* Goals:
	* Task 1: 3200 ShipsDestroyedYaot

## QS_KILLYAOT_08
* Name: Yaot Rebel Fleets X
* Description: Your threat level among the Yaot is higher than most Tanoch fleets. Continue the attack!
* Type: Achievement
* Goals:
	* Task 1: 6400 ShipsDestroyedYaot

## QS_MINET1ABC_PRE01
* Name: Mining Procedures I
* Description: We need to test our mining equipment.
* Type: Achievement
* Goals:
	* Task 1: 
		* 1000 Mined1A
		* 1000 Mined1B
		* 1000 Mined1C

## QS_MINET1ABC_00
* Name: Mining Procedures II
* Description: We should check our mining procedures and see if we could streamline the process.
* Type: Achievement
* Goals:
	* Task 1: 
		* 3000 Mined1A
		* 3000 Mined1B
		* 3000 Mined1C

## QS_MINET1ABC_01
* Name: Mining Procedures III
* Description: Start collecting asteroids to calibrate our resource refinery methods.
* Type: Achievement
* Goals:
	* Task 1: 
		* 6000 Mined1A
		* 6000 Mined1B
		* 6000 Mined1C

## QS_MINET1ABC_02
* Name: Mining Procedures IV
* Description: More materials are necessary to establish our baseline. Harvest more asteroids.
* Type: Achievement
* Goals:
	* Task 1: 
		* 12000 Mined1A
		* 12000 Mined1B
		* 12000 Mined1C

## QS_MINET1ABC_03
* Name: Mining Procedures V
* Description: Our refineries have been calibrated to local nimbus materials. Begin our first production haul.
* Type: Achievement
* FollowUps: ql_esca_mineT2
* Goals:
	* Task 1: 
		* 24000 Mined1A
		* 24000 Mined1B
		* 24000 Mined1C

## QS_MINET1ABC_04
* Name: Mining Procedures VI
* Description: Begin our second production haul for processing.
* Type: Achievement
* Goals:
	* Task 1: 
		* 48000 Mined1A
		* 48000 Mined1B
		* 48000 Mined1C

## QS_MINET1ABC_05
* Name: Mining Procedures VII
* Description: Begin our third production haul for processing.
* Type: Achievement
* Goals:
	* Task 1: 
		* 96000 Mined1A
		* 96000 Mined1B
		* 96000 Mined1C

## QS_MINET1ABC_06
* Name: Mining Procedures VIII
* Description: Begin our fourth production haul for processing.
* Type: Achievement
* Goals:
	* Task 1: 
		* 192000 Mined1A
		* 192000 Mined1B
		* 192000 Mined1C

## QS_MINET1ABC_07
* Name: Mining Procedures IX
* Description: One final haul is needed to certify the refinery for full operations.
* Type: Achievement
* Goals:
	* Task 1: 
		* 384000 Mined1A
		* 384000 Mined1B
		* 384000 Mined1C

## QS_MINET1ABC_08
* Name: Mining Procedures X
* Description: One last production haul is needed to certify the refinery for Grade 1 Procesing.
* Type: Achievement
* Goals:
	* Task 1: 
		* 768000 Mined1A
		* 768000 Mined1B
		* 768000 Mined1C

## QS_MINET2ABC_PRE01
* Name: New Mining Procedures I
* Description: We need to test our mining equipment on these new types of minerals.
* Type: Achievement
* Goals:
	* Task 1: 
		* 1000 Mined2A
		* 1000 Mined2B
		* 1000 Mined2C

## QS_MINET2ABC_00
* Name: New Mining Procedures II
* Description: We should check our mining procedures on these new types of minerals.
* Type: Achievement
* Goals:
	* Task 1: 
		* 3000 Mined2A
		* 3000 Mined2B
		* 3000 Mined2C

## QS_MINET2ABC_01
* Name: New Mining Procedures III
* Description: Engineering has proposed minor upgrades to the refinery process. Harvest larger asteroids for testing.
* Type: Achievement
* Goals:
	* Task 1: 
		* 6000 Mined2A
		* 6000 Mined2B
		* 6000 Mined2C

## QS_MINET2ABC_02
* Name: New Mining Procedures IV
* Description: Engineering is ready to implement these minor changes. Continue supplying larger resources.
* Type: Achievement
* Goals:
	* Task 1: 
		* 12000 Mined2A
		* 12000 Mined2B
		* 12000 Mined2C

## QS_MINET2ABC_03
* Name: New Mining Procedures V
* Description: Engineering wants to test further refits to the refinery. Supply additional resources for testing.
* Type: Achievement
* FollowUps: ql_esca_mineT3
* Goals:
	* Task 1: 
		* 24000 Mined2A
		* 24000 Mined2B
		* 24000 Mined2C

## QS_MINET2ABC_04
* Name: New Mining Procedures VI
* Description: Continue refinery trials. Provide larger resources.
* Type: Achievement
* Goals:
	* Task 1: 
		* 48000 Mined2A
		* 48000 Mined2B
		* 48000 Mined2C

## QS_MINET2ABC_05
* Name: New Mining Procedures VII
* Description: Continue refinery trials. Provide larger resources.
* Type: Achievement
* Goals:
	* Task 1: 
		* 96000 Mined2A
		* 96000 Mined2B
		* 96000 Mined2C

## QS_MINET2ABC_06
* Name: New Mining Procedures VIII
* Description: Continue refinery trials. Provide larger resources.
* Type: Achievement
* Goals:
	* Task 1: 
		* 192000 Mined2A
		* 192000 Mined2B
		* 192000 Mined2C

## QS_MINET2ABC_07
* Name: New Mining Procedures IX
* Description: Continue refinery trials. Provide larger resources.
* Type: Achievement
* Goals:
	* Task 1: 
		* 384000 Mined2A
		* 384000 Mined2B
		* 384000 Mined2C

## QS_MINET2ABC_08
* Name: New Mining Procedures X
* Description: One final load is necessary to approve the new refit to the refinery.
* Type: Achievement
* Goals:
	* Task 1: 
		* 768000 Mined2A
		* 768000 Mined2B
		* 768000 Mined2C

## QS_MINET3ABC_PRE01
* Name: Advanced Mining Procedures I
* Description: We need to test our mining equipment on these new types of minerals.
* Type: Achievement
* Goals:
	* Task 1: 
		* 1000 Mined3A
		* 1000 Mined3B
		* 1000 Mined3C

## QS_MINET3ABC_00
* Name: Advanced Mining Procedures II
* Description: We should check our mining procedures on these new types of minerals.
* Type: Achievement
* Goals:
	* Task 1: 
		* 3000 Mined3A
		* 3000 Mined3B
		* 3000 Mined3C

## QS_MINET3ABC_01
* Name: Advanced Mining Procedures III
* Description: Refinery teams propose a new chemical process for resource extraction.
* Type: Achievement
* Goals:
	* Task 1: 
		* 6000 Mined3A
		* 6000 Mined3B
		* 6000 Mined3C

## QS_MINET3ABC_02
* Name: Advanced Mining Procedures IV
* Description: Supply reduced manpower tests by harvesting further resources.
* Type: Achievement
* Goals:
	* Task 1: 
		* 12000 Mined3A
		* 12000 Mined3B
		* 12000 Mined3C

## QS_MINET3ABC_03
* Name: Advanced Mining Procedures V
* Description: Conducting reduced manpower stress test on refinery complex.
* Type: Achievement
* Goals:
	* Task 1: 
		* 24000 Mined3A
		* 24000 Mined3B
		* 24000 Mined3C

## QS_MINET3ABC_04
* Name: Advanced Mining Procedures VI
* Description: Conducting reduced manpower stress test on refinery complex.
* Type: Achievement
* Goals:
	* Task 1: 
		* 48000 Mined3A
		* 48000 Mined3B
		* 48000 Mined3C

## QS_MINET3ABC_05
* Name: Advanced Mining Procedures VII
* Description: Conducting reduced manpower stress test on refinery complex.
* Type: Achievement
* Goals:
	* Task 1: 
		* 96000 Mined3A
		* 96000 Mined3B
		* 96000 Mined3C

## QS_MINET3ABC_06
* Name: Advanced Mining Procedures VIII
* Description: Conducting reduced manpower stress test on refinery complex.
* Type: Achievement
* Goals:
	* Task 1: 
		* 192000 Mined3A
		* 192000 Mined3B
		* 192000 Mined3C

## QS_MINET3ABC_07
* Name: Advanced Mining Procedures IX
* Description: Final test of reduced crew capacity through new refinery process. Procure resources.
* Type: Achievement
* Goals:
	* Task 1: 
		* 384000 Mined3A
		* 384000 Mined3B
		* 384000 Mined3C

## QS_MINET3ABC_08
* Name: Advanced Mining Procedures X
* Description: Final certification of refinery postprocessing procedure. Supply resources for this test.
* Type: Achievement
* Goals:
	* Task 1: 
		* 768000 Mined3A
		* 768000 Mined3B
		* 768000 Mined3C

## QS_SCAN_PRE01
* Name: System Charts I
* Description: We should explore the star systems in this new galaxy.
* Type: Achievement
* Goals:
	* Task 1: 50 Scanned

## QS_SCAN_00
* Name: System Charts II
* Description: We need to fill our system charts with actual data.
* Type: Achievement
* Goals:
	* Task 1: 150 Scanned

## QS_SCAN_01
* Name: System Charts III
* Description: The new sensor suite needs raw data to begin configuring the array. Begin scanning.
* Type: Achievement
* FollowUps: ql_esca_generated
* Goals:
	* Task 1: 300 Scanned

## QS_SCAN_02
* Name: System Charts IV
* Description: The array is ready to begin trials. Begin scanning targets.
* Type: Achievement
* Goals:
	* Task 1: 600 Scanned

## QS_SCAN_03
* Name: System Charts V
* Description: Begin testing short range detection sensors. Begin scanning targets.
* Type: Achievement
* Goals:
	* Task 1: 1200 Scanned

## QS_SCAN_04
* Name: System Charts VI
* Description: Conduct scans. Calibration will focus on short range performance.
* Type: Achievement
* Goals:
	* Task 1: 2500 Scanned

## QS_SCAN_05
* Name: System Charts VII
* Description: Conduct scans. Calibration will focus on long range performance.
* Type: Achievement
* Goals:
	* Task 1: 5000 Scanned

## QS_SCAN_06
* Name: System Charts VIII
* Description: Conduct Scans. Calibration will focus on hyperspace oddities.
* Type: Achievement
* Goals:
	* Task 1: 10000 Scanned

## QS_SCAN_07
* Name: System Charts IX
* Description: Conduct scans. Calibration will focus on signals moving at distance.
* Type: Achievement
* Goals:
	* Task 1: 20000 Scanned

## QS_SCAN_08
* Name: System Charts X
* Description: Final comprehensive test of all sensor systems.
* Type: Achievement
* Goals:
	* Task 1: 40000 Scanned

## QS_FINISHGENERATED_PRE01
* Name: Signal Search I
* Description: We should look out for possible signals in deep space. They could represent opportunities for us.
* Type: Achievement
* Goals:
	* Task 1: 2 MissionsDoneGenerated

## QS_FINISHGENERATED_00
* Name: Signal Search II
* Description: We should actively search for signals in deep space.
* Type: Achievement
* Goals:
	* Task 1: 5 MissionsDoneGenerated

## QS_FINISHGENERATED_01
* Name: Signal Search III
* Description: Signals investigation for pathfinding and reconnaissance.
* Type: Achievement
* Goals:
	* Task 1: 10 MissionsDoneGenerated

## QS_FINISHGENERATED_02
* Name: Signal Search IV
* Description: Further investigate mysterious signals for pathfinding and reconnaissance.
* Type: Achievement
* Goals:
	* Task 1: 20 MissionsDoneGenerated

## QS_FINISHGENERATED_03
* Name: Signal Search V
* Description: Hunt for anomalous signals to unlock further discoveries and rewards.
* Type: Achievement
* Goals:
	* Task 1: 40 MissionsDoneGenerated

## QS_FINISHGENERATED_04
* Name: Signal Search VI
* Description: Establish signal gain and investigation methods.
* Type: Achievement
* Goals:
	* Task 1: 80 MissionsDoneGenerated

## QS_FINISHGENERATED_05
* Name: Signal Search VII
* Description: Routine investigation of anomalous signals.
* Type: Achievement
* Goals:
	* Task 1: 160 MissionsDoneGenerated

## QS_FINISHGENERATED_06
* Name: Signal Search VIII
* Description: Special teams designated for signal investigations response.
* Type: Achievement
* Goals:
	* Task 1: 320 MissionsDoneGenerated

## QS_FINISHGENERATED_07
* Name: Signal Search IX
* Description: Catalogue of anomalous activities established.
* Type: Achievement
* Goals:
	* Task 1: 640 MissionsDoneGenerated

## QS_FINISHGENERATED_08
* Name: Signal Search X
* Description: Investigative mastery.
* Type: Achievement
* Goals:
	* Task 1: 1300 MissionsDoneGenerated

## QR_013
* Name: Pirate Hideout
* Description: A lot of pirate activity has been reported in this region. The local pirate faction must have a major base here. Our task is to find the base, and destroy any pirate vessel and structure in this sector.
* Type: Strike
* Goals:
	* Task 1: Complete mission 'Pirate Hideout'

## QR_016
* Name: Pirate Hideout (Heroic)
* Description: A lot of pirate activity has been reported in this region. The local pirate faction must have a major base here. Our task is to find the base, and destroy any pirate vessel and structure in this sector.
* Type: Strike
* Goals:
	* Task 1: Complete mission 'Pirate Hideout (Heroic)'

## QR_014
* Name: Station Defense
* Description: We have received intel that enemy forces are planning to attack a local trading station. In order to defend the station, we must immediately move our fleet into defensive position.
* Type: Strike
* Goals:
	* Task 1: Complete mission 'Station Defense'

## QR_017
* Name: Station Defense (Heroic)
* Description: We have received intel that enemy forces are planning to attack a local trading station. In order to defend the station, we must immediately move our fleet into defensive position.
* Type: Strike
* Goals:
	* Task 1: Complete mission 'Station Defense (Heroic)'

## QR_021
* Name: Station Defense (Mythic)
* Description: We have received intel that enemy forces are planning to attack a local trading station. In order to defend the station, we must immediately move our fleet into defensive position.
* Type: Strike
* Goals:
	* Task 1: Complete mission 'Station Defense (Mythic)'

## QR_015
* Name: Pahra's Rock
* Description: The presence of a large Cangacian asteroid base in this area has been threatening the Hiigaran settlements. Our task is to perform an attack on this base, destroy it and any Cangacian fleet nearby.
* Type: Strike
* Goals:
	* Task 1: Complete mission 'Pahra's Rock'

## QR_018
* Name: Pahra's Rock (Heroic)
* Description: The presence of a large Cangacian asteroid base in this area has been threatening the Hiigaran settlements. Our task is to perform an attack on this base, destroy it and any Cangacian fleet nearby.
* Type: Strike
* Goals:
	* Task 1: Complete mission 'Pahra's Rock (Heroic)'

## QR_022
* Name: Pahra's Rock (Mythic)
* Description: The presence of a large Cangacian asteroid base in this area has been threatening the Hiigaran settlements. Our task is to perform an attack on this base, destroy it and any Cangacian fleet nearby.
* Type: Strike
* Goals:
	* Task 1: Complete mission 'Pahra's Rock (Mythic)'

## QR_019
* Name: Breach
* Description: Sitting in a safe pocket inside an electromagnetic asteroid field, this station is a crucial base of operation. As it is heavily defended, we came up with the cunning plan to fill an old freighter with explosives and escort it to the base.
* Type: Strike
* Goals:
	* Task 1: Complete mission 'Breach'

## QR_020
* Name: Breach (Heroic)
* Description: Sitting in a safe pocket inside an electromagnetic asteroid field, this station is a crucial base of operation. As it is heavily defended, we came up with the cunning plan to fill an old freighter with explosives and escort it to the base.
* Type: Strike
* Goals:
	* Task 1: Complete mission 'Breach (Heroic)'

## QR_023
* Name: Nightmare Gulf
* Description: A base used by Kiithless raiders has been located in this area of the nightmare gulf. A large attack force will be needed to destroy it and free the Progenitor assets held at this location.
* Type: Strike
* Goals:
	* Task 1: Complete mission 'Nightmare Gulf'

## QT_DAILY_BUY
* Name: Big Spender
* Description: You can buy resources or items in the market as well as in the liaison requisitions.
* Type: Daily
* Goals:
	* Task 1: 
## QT_DAILY_MINE
* Name: Primary Sector
* Description: Ores can be mined in asteroid clusters, while gas is harvested from jovians.
* Type: Daily
* Goals:
	* Task 1: 1500 Mined

## QT_DAILY_REFINE
* Name: Metallurgy
* Description: Refining ores is required to turn them into usable metals for the production process.
* Type: Daily
* Goals:
	* Task 1: Craft

## QT_DAILY_CRAFT
* Name: Means of Production
* Description: You can fabricate all sorts of products in your flagship's factories.
* Type: Daily
* Goals:
	* Task 1: Craft

## QT_DAILY_GAINRP
* Name: Hoarding Knowledge
* Description: Research points are passively collected in your flagship's laboratories. They are needed to conduct research.
* Type: Daily
* Goals:
	* Task 1: GainItem

## QT_DAILY_INSIGNIAS
* Name: Distinction
* Description: You can earn insignias by completing missions. They are needed to promote your officers, which increases their attributes.
* Type: Daily
* Goals:
	* Task 1: GainItem

## QT_DAILY_LIAISON
* Name: Adventurism
* Description: Completing missions gives you XP to level up.
* Type: Daily
* Goals:
	* Task 1: Complete 3 side missions

## QT_DAILY_DESTROY
* Name: Trophies
* Description: Destroyed enemy vessels sometimes leave salvage behind which may contain resources.
* Type: Daily
* Goals:
	* Task 1: 15 ShipsDestroyed

## QT_DAILY_SIGNALS
* Name: New Discoveries
* Description: Some objects require to be scanned several times to reveal them fully.
* Type: Daily
* Goals:
	* Task 1: Scan

## QT_DAILY_DAILYMISSION
* Name: Bragging Rights
* Description: A strike is a great opportunity to test your strength and train your coordination with other commanders.
* Type: Daily
* Goals:
	* Task 1: Complete side mission

## QT_DAILY_DAILIES
* Name: Periodic Activity
* Description: Most daily and weekly assignments grant Prestige, which can be used in the prestige section of the market to acquire special blueprints and other items.
* Type: Daily
* Goals:
	* Task 1: 8 Daily

## QT_WEEKLY_DAILIES
* Name: Assiduity
* Description: Daily assignments refresh once a day, make sure to claim your reward before that happens.
* Type: Weekly
* Goals:
	* Task 1: 40 Daily

## QT_WEEKLY_REPUTATION
* Name: Connections
* Description: Completing liaison assignments improves your standing with that particular faction, which in turn unlocks new items in their liaison requisitions.
* Type: Weekly
* Goals:
	* Task 1: 9 Faction

## QT_WEEKLY_CLANQUESTS
* Name: Stronger Together
* Description: You can only complete clan assignments while you are inside a clan. Completing these grants you clan credits as well as clan supplies for the whole clan.
* Type: Weekly
* Goals:
	* Task 1: 10 Clan

## QT_WEEKLY_LEVELOFFICERS
* Name: Ranks and File
* Description: After reaching enough levels, officers will gain a new rank, which increases their abilities.
* Type: Weekly
* Goals:
	* Task 1: UpgradeOfficer

## QT_WEEKLY_UPGRADES
* Name: Marvels of Engineering
* Description: Module upgrades need rare earth materials and can only be done at a trading station.
* Type: Weekly
* Goals:
	* Task 1: Craft

## QT_WEEKLY_MISSIONS
* Name: Signal Sweep
* Description: New signals may appear through scanning after you have cleared out a few.
* Type: Weekly
* Goals:
	* Task 1: Complete 9 side missions

## QT_WEEKLY_RESEARCH
* Name: Scientific Method
* Description: Research is conducted inside your flagship's laboratories.
* Type: Weekly
* Goals:
	* Task 1: Craft

## QE_TEST_EVENTTESTQUEST_1
* Name: No header for quest qe_test_eventtestquest_1
* Description: No description for quest qe_test_eventtestquest_1

* Type: Event
* Goals:
	* Task 1: Craft

## QE_TEST_EVENTTESTQUEST_2
* Name: No header for quest qe_test_eventtestquest_2
* Description: No description for quest qe_test_eventtestquest_2

* Type: Event
* Goals:
	* Task 1: Pay 10 Credits

## QE_TEST_EVENTTESTQUEST_3
* Name: No header for quest qe_test_eventtestquest_3
* Description: No description for quest qe_test_eventtestquest_3

* Type: Event
* Goals:
	* Task 1: Complete side mission

## QE_YAOT_SPRING_2023_DAILY_A_T2
* Name: No header for quest qe_yaot_spring_2023_daily_A_t2
* Description: No description for quest qe_yaot_spring_2023_daily_A_t2

* Type: Event
* EventId: event_season_yaoSpr_2023
* Goals:
	* Task 1: GainItem

## QE_YAOT_SPRING_2023_DAILY_B_T2
* Name: No header for quest qe_yaot_spring_2023_daily_B_t2
* Description: No description for quest qe_yaot_spring_2023_daily_B_t2

* Type: Event
* EventId: event_season_yaoSpr_2023
* Goals:
	* Task 1: 10 ShipsDestroyedTanoch

## QE_YAOT_SPRING_2023_DAILY_C_T3
* Name: No header for quest qe_yaot_spring_2023_daily_C_t3
* Description: No description for quest qe_yaot_spring_2023_daily_C_t3

* Type: Event
* EventId: event_season_yaoSpr_2023
* Goals:
	* Task 1: 100 Mined3E_Mined3F_Mined3G_Mined3H_Mined4E_Mined4F_Mined4G_Mined4H

## QE_YAOT_SPRING_2023_DAILY_D_T3
* Name: No header for quest qe_yaot_spring_2023_daily_D_t3
* Description: No description for quest qe_yaot_spring_2023_daily_D_t3

* Type: Event
* EventId: event_season_yaoSpr_2023
* Goals:
	* Task 1: 5 Faction_Yaot

## QE_YAOT_SPRING_2023_DAY1
* Name: No header for quest qe_yaot_spring_2023_day1
* Description: No description for quest qe_yaot_spring_2023_day1

* Type: Event
* EventId: event_season_yaoSpr_2023
* Goals:
	* Task 1: 750 Mined

## QE_YAOT_SPRING_2023_DAY2
* Name: No header for quest qe_yaot_spring_2023_day2
* Description: No description for quest qe_yaot_spring_2023_day2

* Type: Event
* EventId: event_season_yaoSpr_2023
* Goals:
	* Task 1: Complete 3 side missions

## QE_YAOT_SPRING_2023_DAY3
* Name: No header for quest qe_yaot_spring_2023_day3
* Description: No description for quest qe_yaot_spring_2023_day3

* Type: Event
* EventId: event_season_yaoSpr_2023
* Goals:
	* Task 1: Craft

## QE_YAOT_SPRING_2023_DAY4
* Name: No header for quest qe_yaot_spring_2023_day4
* Description: No description for quest qe_yaot_spring_2023_day4

* Type: Event
* EventId: event_season_yaoSpr_2023
* Goals:
	* Task 1: GainItem

## QE_YAOT_SPRING_2023_DAY5
* Name: No header for quest qe_yaot_spring_2023_day5
* Description: No description for quest qe_yaot_spring_2023_day5

* Type: Event
* EventId: event_season_yaoSpr_2023
* Goals:
	* Task 1: UpgradeOfficer

## QE_YAOT_SPRING_2023_DAY6
* Name: No header for quest qe_yaot_spring_2023_day6
* Description: No description for quest qe_yaot_spring_2023_day6

* Type: Event
* EventId: event_season_yaoSpr_2023
* Goals:
	* Task 1: Complete 3 side missions

## QE_YAOT_SPRING_2023_DAY7
* Name: No header for quest qe_yaot_spring_2023_day7
* Description: No description for quest qe_yaot_spring_2023_day7

* Type: Event
* EventId: event_season_yaoSpr_2023
* Goals:
	* Task 1: 750 Mined

## QE_YAOT_SPRING_2023_DAY8
* Name: No header for quest qe_yaot_spring_2023_day8
* Description: No description for quest qe_yaot_spring_2023_day8

* Type: Event
* EventId: event_season_yaoSpr_2023
* Goals:
	* Task 1: GainItem

## QE_YAOT_SPRING_2023_DAY9
* Name: No header for quest qe_yaot_spring_2023_day9
* Description: No description for quest qe_yaot_spring_2023_day9

* Type: Event
* EventId: event_season_yaoSpr_2023
* Goals:
	* Task 1: Craft

## QE_YAOT_SPRING_2023_DAY10
* Name: No header for quest qe_yaot_spring_2023_day10
* Description: No description for quest qe_yaot_spring_2023_day10

* Type: Event
* EventId: event_season_yaoSpr_2023
* Goals:
	* Task 1: Complete 3 side missions

## QE_YAOT_SPRING_2023_DAY11
* Name: No header for quest qe_yaot_spring_2023_day11
* Description: No description for quest qe_yaot_spring_2023_day11

* Type: Event
* EventId: event_season_yaoSpr_2023
* Goals:
	* Task 1: 750 Mined

## QE_YAOT_SPRING_2023_DAY12
* Name: No header for quest qe_yaot_spring_2023_day12
* Description: No description for quest qe_yaot_spring_2023_day12

* Type: Event
* EventId: event_season_yaoSpr_2023
* Goals:
	* Task 1: GainItem

## QE_YAOT_SPRING_2023_DAY13
* Name: No header for quest qe_yaot_spring_2023_day13
* Description: No description for quest qe_yaot_spring_2023_day13

* Type: Event
* EventId: event_season_yaoSpr_2023
* Goals:
	* Task 1: UpgradeOfficer

## QE_YAOT_SPRING_2023_DAY14
* Name: No header for quest qe_yaot_spring_2023_day14
* Description: No description for quest qe_yaot_spring_2023_day14

* Type: Event
* EventId: event_season_yaoSpr_2023
* Goals:
	* Task 1: Complete mission 'Tanochet (Event)'

## QE_AMASUM_2023_DAILY_A_T1
* Name: Gather for Many
* Description: To continue operations in Amassari space, we need to replenish our strategic reserves. Collect resources to build up this stockpile.

<color=#FBB03F>Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
* Type: Event
* EventId: event_season_amaSum_2023_t1
* Goals:
	* Task 1: GainItem

## QE_AMASUM_2023_DAILY_B_T1
* Name: Make into Plenty
* Description: The quartermaster is concerned about our stockpile of spare parts. Begin construction of spares to replenish supplies.

<color=#FBB03F>Small items such as strike craft, modules and parts can be built in the fabricator. Larger items such as escort ships and flagships must be constructed at shipyards provided at larger stations.</color>
* Type: Event
* EventId: event_season_amaSum_2023_t1
* Goals:
	* Task 1: Craft

## QE_AMASUM_2023_DAILY_C_T1
* Name: Protect the Weak
* Description: Combat channels are rife with activity from Kiithless Hiigarans. It's our responsibility to put a stop to these raids and restore the peace.

<color=#FBB03F>While normally raiding Amassari space, Kidara's Kiithless have recently begun aggressive incursions into the rest of the galaxy. Find their fleets in signals and asteroid clusters and destroy them.</color>
* Type: Event
* EventId: event_season_amaSum_2023_t1
* Goals:
	* Task 1: 10 ShipsDestroyedDarkHiigaranT1_ShipsDestroyedDarkHiigaranT2_ShipsDestroyedDarkHiigaranT3_ShipsDestroyedDarkHiigaranT4

## QE_AMASUM_2023_DAILY_D_T1
* Name: Find the Lost
* Description: Monitoring Kiithless channels reveals a Progenitor Relic is nearby. We need to secure it before they do.

<color=#FBB03F>Progenitor relics can be found in relic signature signals. Relics can be sold on the market for credits, though some liaison offices may be interested in relics as well.</color>
* Type: Event
* EventId: event_season_amaSum_2023_t1
* Goals:
	* Task 1: GainItem

## QE_AMASUM_2023_DAY1_T1
* Name: Day 1: Provide Parts
* Description: The Amassari have very little in the way of developed industry, and would appreciate any refined parts we can provide. Craft some to provide a supply.

<color=#FBB03F>Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.</color>
* Type: Event
* EventId: event_season_amaSum_2023_t1
* Goals:
	* Task 1: Craft

## QE_AMASUM_2023_DAY2_T1
* Name: Day 2: Find Treasures
* Description: Sensors have detected possible ruins of interest in the vicinity. Investigate to see if there's anything of interest found here.

<color=#FBB03F>Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.</color>
* Type: Event
* EventId: event_season_amaSum_2023_t1
* Goals:
	* Task 1: Complete 3 side missions

## QE_AMASUM_2023_DAY3_T1
* Name: Day 3: Learn our Ways
* Description: Very little is known about the Hagthar Empire, the ancestors of the Amassari. In order to continue operations here, we need to educate our officers about what we know.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* Type: Event
* EventId: event_season_amaSum_2023_t1
* Goals:
	* Task 1: UpgradeOfficer

## QE_AMASUM_2023_DAY4_T1
* Name: Day 4: Ally and Friend
* Description: Our guide is willing to connect us with several Amassari officials in the vicinity that need help. We could benefit from this cooperation.

<color=#FBB03F>Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.</color>
* Type: Event
* EventId: event_season_amaSum_2023_t1
* Goals:
	* Task 1: Complete 3 side missions

## QE_AMASUM_2023_DAY5_T1
* Name: Day 5: Race for Gold
* Description: Jothru has revealed there may be more information to find among the Hagthar ruins if we can find the pieces. We must prepare for this venture.

<color=#FBB03F>Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.</color>
* Type: Event
* EventId: event_season_amaSum_2023_t1
* Goals:
	* Task 1: Craft

## QE_AMASUM_2023_DAY6_T1
* Name: Day 6: Hunting high and low
* Description: Jothru can provide the whereabouts, but not the exact location, of key pieces belonging to significant parts of Hagthar history. Perhaps we can learn what the Kiithless are seeking.

<color=#FBB03F>Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.</color>
* Type: Event
* EventId: event_season_amaSum_2023_t1
* Goals:
	* Task 1: Complete 3 side missions

## QE_AMASUM_2023_DAY7_T1
* Name: Day 7: Ways of the Enemy
* Description: Kiithless strikes have been increasing against the Amassari. We need to calibrate our training to match their new battle techniques in order to stop them.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from dismissing officers and are earned through completing signals.</color>
* Type: Event
* EventId: event_season_amaSum_2023_t1
* Goals:
	* Task 1: GainItem

## QE_AMASUM_2023_DAY8_T1
* Name: Day 8: Hand against Foe
* Description: Our training was timely. Jothru has handed us some leads on potential Kiithless activity in the region. We must investigate.

<color=#FBB03F>Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.</color>
* Type: Event
* EventId: event_season_amaSum_2023_t1
* Goals:
	* Task 1: Complete 3 side missions

## QE_AMASUM_2023_DAY9_T1
* Name: Day 9: Distant Gems
* Description: During our battles we took some hits to ship's stores. It's advised to rebuild our stockpiles with refined ores.

<color=#FBB03F>Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.</color>
* Type: Event
* EventId: event_season_amaSum_2023_t1
* Goals:
	* Task 1: Craft

## QE_AMASUM_2023_DAY10_T1
* Name: Day 10: Path of the Reclaimer
* Description: More Amassari have reached out to Jothru and us with more jobs. There's an unspoken offer as well to assist with our strikes against the Kiithless.

<color=#FBB03F>Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.</color>
* Type: Event
* EventId: event_season_amaSum_2023_t1
* Goals:
	* Task 1: Complete 3 side missions

## QE_AMASUM_2023_DAY11_T1
* Name: Day 11: Knowledge and Defense
* Description: Assisting the Amassari has paid off, we're intercepting communications traffic suggesting they're being disrupted. We need to brief all officers on this stage of the operation against them.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* Type: Event
* EventId: event_season_amaSum_2023_t1
* Goals:
	* Task 1: UpgradeOfficer

## QE_AMASUM_2023_DAY12_T1
* Name: Day 12: Star Hunter
* Description: Fleet Intelligence has deduced several available targets belonging to the Kiithless. If we hit them, it will further disrupt their supplies to the point of dissolving their operations here.

<color=#FBB03F>Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.</color>
* Type: Event
* EventId: event_season_amaSum_2023_t1
* Goals:
	* Task 1: Complete 3 side missions

## QE_AMASUM_2023_DAY13_T1
* Name: Day 13: Crown of Stones
* Description: We need to stockpile resources to prepare for a final battle against the Kiithless in the Hather Plains.

<color=#FBB03F>Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.</color>
* Type: Event
* EventId: event_season_amaSum_2023_t1
* Goals:
	* Task 1: Craft

## QE_AMASUM_2023_DAY14_T1
* Name: Day 14: Lord of the Dust
* Description: All officers need to be briefed on the potential dangers posed by the remaining Kiithless fleet.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from dismissing officers and are earned through completing signals.</color>
* Type: Event
* EventId: event_season_amaSum_2023_t1
* Goals:
	* Task 1: GainItem

## QE_AMASUM_2023_DAY15_T1
* Name: Day 15: Kin of the Amassari
* Description: The Kiithless are targeting Ambadda waystation. Thassin's Needle, an artifact, is housed here. They must be stopped from raiding this station!

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it.</color>

<color=#FBB03F>To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Type: Event
* EventId: event_season_amaSum_2023_t1
* Goals:
	* Task 1: Complete mission 'event_01_StationDefense'

## QE_AMASUM_2023_DAILY_A_T2
* Name: Gather for Many
* Description: To continue operations in Amassari space, we need to replenish our strategic reserves. Collect resources to build up this stockpile.

<color=#FBB03F>Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
* Type: Event
* EventId: event_season_amaSum_2023_t2
* Goals:
	* Task 1: GainItem

## QE_AMASUM_2023_DAILY_B_T2
* Name: Make into Plenty
* Description: The quartermaster is concerned about our stockpile of spare parts. Begin construction of spares to replenish supplies.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
* Type: Event
* EventId: event_season_amaSum_2023_t2
* Goals:
	* Task 1: Craft

## QE_AMASUM_2023_DAILY_C_T2
* Name: Protect the Weak
* Description: Combat channels are rife with activity from Kiithless Hiigarans. It's our responsibility to put a stop to these raids and restore the peace.

<color=#FBB03F>While normally raiding Amassari space, Kidara's Kiithless have recently begun aggressive incursions into the rest of the galaxy. Find their fleets in signals and asteroid clusters and destroy them.</color>
* Type: Event
* EventId: event_season_amaSum_2023_t2
* Goals:
	* Task 1: 10 ShipsDestroyedDarkHiigaranT2_ShipsDestroyedDarkHiigaranT3_ShipsDestroyedDarkHiigaranT4

## QE_AMASUM_2023_DAILY_D_T2
* Name: Find the Lost
* Description: Monitoring Kiithless channels reveals a Progenitor Relic is nearby. We need to secure it before they do.

<color=#FBB03F>Progenitor relics can be found in relic signature signals. Relics can be sold on the market for credits, though some liaison offices may be interested in relics as well.</color>
* Type: Event
* EventId: event_season_amaSum_2023_t2
* Goals:
	* Task 1: GainItem

## QE_AMASUM_2023_DAY1_T2
* Name: Day 1: Provide Parts
* Description: The Amassari have very little in the way of developed industry, and would appreciate any refined parts we can provide. Craft some to provide a supply.

<color=#FBB03F>Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.</color>
* Type: Event
* EventId: event_season_amaSum_2023_t2
* Goals:
	* Task 1: Craft

## QE_AMASUM_2023_DAY2_T2
* Name: Day 2: Find Treasures
* Description: Sensors have detected possible ruins of interest in the vicinity. Investigate to see if there's anything of interest found here.

<color=#FBB03F>Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.</color>
* Type: Event
* EventId: event_season_amaSum_2023_t2
* Goals:
	* Task 1: Complete 3 side missions

## QE_AMASUM_2023_DAY3_T2
* Name: Day 3: Learn our Ways
* Description: Very little is known about the Hagthar Empire, the ancestors of the Amassari. In order to continue operations here, we need to educate our officers about what we know.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* Type: Event
* EventId: event_season_amaSum_2023_t2
* Goals:
	* Task 1: UpgradeOfficer

## QE_AMASUM_2023_DAY4_T2
* Name: Day 4: Ally and Friend
* Description: Our guide is willing to connect us with several Amassari officials in the vicinity that need help. We could benefit from this cooperation.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Higher reputation levels unlock additional items in that faction's liaison requisitions office.</color>
* Type: Event
* EventId: event_season_amaSum_2023_t2
* Goals:
	* Task 1: 5 Faction_T2up

## QE_AMASUM_2023_DAY5_T2
* Name: Day 5: Race for Gold
* Description: Jothru has revealed there may be more information to find among the Hagthar ruins if we can find the pieces. We must prepare for this venture.

<color=#FBB03F>Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.</color>
* Type: Event
* EventId: event_season_amaSum_2023_t2
* Goals:
	* Task 1: Craft

## QE_AMASUM_2023_DAY6_T2
* Name: Day 6: Hunting high and low
* Description: Jothru can provide the whereabouts, but not the exact location, of key pieces belonging to significant parts of Hagthar history. Perhaps we can learn what the Kiithless are seeking.

<color=#FBB03F>Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.</color>
* Type: Event
* EventId: event_season_amaSum_2023_t2
* Goals:
	* Task 1: Complete 3 side missions

## QE_AMASUM_2023_DAY7_T2
* Name: Day 7: Ways of the Enemy
* Description: Kiithless strikes have been increasing against the Amassari. We need to calibrate our training to match their new battle techniques in order to stop them.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from dismissing officers and are earned through completing signals.</color>
* Type: Event
* EventId: event_season_amaSum_2023_t2
* Goals:
	* Task 1: GainItem

## QE_AMASUM_2023_DAY8_T2
* Name: Day 8: Hand against Foe
* Description: Our training was timely. Jothru has handed us some leads on potential Kiithless activity in the region. We must investigate.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat. Completing a strike rewards code fragments, which can be turned in for special blueprints.</color>
* Type: Event
* EventId: event_season_amaSum_2023_t2
* Goals:
	* Task 1: Complete side mission

## QE_AMASUM_2023_DAY9_T2
* Name: Day 9: Distant Gems
* Description: During our battles we took some hits to ship's stores. It's advised to rebuild our stockpiles with refined ores.

<color=#FBB03F>Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.</color>
* Type: Event
* EventId: event_season_amaSum_2023_t2
* Goals:
	* Task 1: Craft

## QE_AMASUM_2023_DAY10_T2
* Name: Day 10: Path of the Reclaimer
* Description: More Amassari have reached out to Jothru and us with more jobs. There's an unspoken offer as well to assist with our strikes against the Kiithless.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Higher reputation levels unlock additional items in that faction's liaison requisitions office.</color>
* Type: Event
* EventId: event_season_amaSum_2023_t2
* Goals:
	* Task 1: 5 Faction_T2up

## QE_AMASUM_2023_DAY11_T2
* Name: Day 11: Knowledge and Defense
* Description: Assisting the Amassari has paid off, we're intercepting communications traffic suggesting they're being disrupted. We need to brief all officers on this stage of the operation against them.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* Type: Event
* EventId: event_season_amaSum_2023_t2
* Goals:
	* Task 1: UpgradeOfficer

## QE_AMASUM_2023_DAY12_T2
* Name: Day 12: Star Hunter
* Description: Fleet Intelligence has deduced several available targets belonging to the Kiithless. If we hit them, it will further disrupt their supplies to the point of dissolving their operations here.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat. Completing a strike rewards code fragments, which can be turned in for special blueprints.</color>
* Type: Event
* EventId: event_season_amaSum_2023_t2
* Goals:
	* Task 1: Complete side mission

## QE_AMASUM_2023_DAY13_T2
* Name: Day 13: Crown of Stones
* Description: We need to stockpile resources to prepare for a final battle against the Kiithless in the Hather Plains.

<color=#FBB03F>Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.</color>
* Type: Event
* EventId: event_season_amaSum_2023_t2
* Goals:
	* Task 1: Craft

## QE_AMASUM_2023_DAY14_T2
* Name: Day 14: Lord of the Dust
* Description: All officers need to be briefed on the potential dangers posed by the remaining Kiithless fleet.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from dismissing officers and are earned through completing signals.</color>
* Type: Event
* EventId: event_season_amaSum_2023_t2
* Goals:
	* Task 1: GainItem

## QE_AMASUM_2023_DAY15_T2
* Name: Day 15: Kin of the Amassari
* Description: The Kiithless are targeting Ambadda waystation. Thassin's Needle, an artifact, is housed here. They must be stopped from raiding this station!

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it.</color>

<color=#FBB03F>To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Type: Event
* EventId: event_season_amaSum_2023_t2
* Goals:
	* Task 1: Complete mission 'event_02_StationDefense'

## QE_AMASUM_2023_DAILY_A_T3
* Name: Gather for Many
* Description: To continue operations in Amassari space, we need to replenish our strategic reserves. Collect resources to build up this stockpile.

<color=#FBB03F>Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
* Type: Event
* EventId: event_season_amaSum_2023_t3
* Goals:
	* Task 1: GainItem

## QE_AMASUM_2023_DAILY_B_T3
* Name: Make into Plenty
* Description: The quartermaster is concerned about our stockpile of spare parts. Begin construction of spares to replenish supplies.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
* Type: Event
* EventId: event_season_amaSum_2023_t3
* Goals:
	* Task 1: Craft

## QE_AMASUM_2023_DAILY_C_T3
* Name: Protect the Weak
* Description: Combat channels are rife with activity from Kiithless Hiigarans. It's our responsibility to put a stop to these raids and restore the peace.

<color=#FBB03F>While normally raiding Amassari space, Kidara's Kiithless have recently begun aggressive incursions into the rest of the galaxy. Find their fleets in signals and asteroid clusters and destroy them.</color>
* Type: Event
* EventId: event_season_amaSum_2023_t3
* Goals:
	* Task 1: 10 ShipsDestroyedDarkHiigaranT3_ShipsDestroyedDarkHiigaranT4

## QE_AMASUM_2023_DAILY_D_T3
* Name: Find the Lost
* Description: Monitoring Kiithless channels reveals a Progenitor Relic is nearby. We need to secure it before they do.

<color=#FBB03F>Progenitor relics can be found in relic signature signals. Relics can be sold on the market for credits, though some liaison offices may be interested in relics as well.</color>
* Type: Event
* EventId: event_season_amaSum_2023_t3
* Goals:
	* Task 1: GainItem

## QE_AMASUM_2023_DAY1_T3
* Name: Day 1: Provide Parts
* Description: The Amassari have very little in the way of developed industry, and would appreciate any refined parts we can provide. Craft some to provide a supply.

<color=#FBB03F>Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.</color>
* Type: Event
* EventId: event_season_amaSum_2023_t3
* Goals:
	* Task 1: Craft

## QE_AMASUM_2023_DAY2_T3
* Name: Day 2: Find Treasures
* Description: Sensors have detected possible ruins of interest in the vicinity. Investigate to see if there's anything of interest found here.

<color=#FBB03F>Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.</color>
* Type: Event
* EventId: event_season_amaSum_2023_t3
* Goals:
	* Task 1: Complete 3 side missions

## QE_AMASUM_2023_DAY3_T3
* Name: Day 3: Learn our Ways
* Description: Very little is known about the Hagthar Empire, the ancestors of the Amassari. In order to continue operations here, we need to educate our officers about what we know.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* Type: Event
* EventId: event_season_amaSum_2023_t3
* Goals:
	* Task 1: UpgradeOfficer

## QE_AMASUM_2023_DAY4_T3
* Name: Day 4: Ally and Friend
* Description: Our guide is willing to connect us with several Amassari officials in the vicinity that need help. We could benefit from this cooperation.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Higher reputation levels unlock additional items in that faction's liaison requisitions office.</color>
* Type: Event
* EventId: event_season_amaSum_2023_t3
* Goals:
	* Task 1: 5 Faction_T3up

## QE_AMASUM_2023_DAY5_T3
* Name: Day 5: Race for Gold
* Description: Jothru has revealed there may be more information to find among the Hagthar ruins if we can find the pieces. We must prepare for this venture.

<color=#FBB03F>Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.</color>
* Type: Event
* EventId: event_season_amaSum_2023_t3
* Goals:
	* Task 1: GainItem

## QE_AMASUM_2023_DAY6_T3
* Name: Day 6: Hunting high and low
* Description: Jothru can provide the whereabouts, but not the exact location, of key pieces belonging to significant parts of Hagthar history. Perhaps we can learn what the Kiithless are seeking.

<color=#FBB03F>Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.</color>
* Type: Event
* EventId: event_season_amaSum_2023_t3
* Goals:
	* Task 1: Complete 3 side missions

## QE_AMASUM_2023_DAY7_T3
* Name: Day 7: Ways of the Enemy
* Description: Kiithless strikes have been increasing against the Amassari. We need to calibrate our training to match their new battle techniques in order to stop them.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from dismissing officers and are earned through completing signals.</color>
* Type: Event
* EventId: event_season_amaSum_2023_t3
* Goals:
	* Task 1: GainItem

## QE_AMASUM_2023_DAY8_T3
* Name: Day 8: Hand against Foe
* Description: Our training was timely. Jothru has handed us some leads on potential Kiithless activity in the region. We must investigate.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat. Completing a strike rewards code fragments, which can be turned in for special blueprints.</color>
* Type: Event
* EventId: event_season_amaSum_2023_t3
* Goals:
	* Task 1: Complete 3 side missions

## QE_AMASUM_2023_DAY9_T3
* Name: Day 9: Distant Gems
* Description: During our battles we took some hits to ship's stores. It's advised to rebuild our stockpiles with refined ores.

<color=#FBB03F>Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.</color>
* Type: Event
* EventId: event_season_amaSum_2023_t3
* Goals:
	* Task 1: Craft

## QE_AMASUM_2023_DAY10_T3
* Name: Day 10: Path of the Reclaimer
* Description: More Amassari have reached out to Jothru and us with more jobs. There's an unspoken offer as well to assist with our strikes against the Kiithless.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Higher reputation levels unlock additional items in that faction's liaison requisitions office.</color>
* Type: Event
* EventId: event_season_amaSum_2023_t3
* Goals:
	* Task 1: 5 Faction_T3up

## QE_AMASUM_2023_DAY11_T3
* Name: Day 11: Knowledge and Defense
* Description: Assisting the Amassari has paid off, we're intercepting communications traffic suggesting they're being disrupted. We need to brief all officers on this stage of the operation against them.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* Type: Event
* EventId: event_season_amaSum_2023_t3
* Goals:
	* Task 1: UpgradeOfficer

## QE_AMASUM_2023_DAY12_T3
* Name: Day 12: Star Hunter
* Description: Fleet Intelligence has deduced several available targets belonging to the Kiithless. If we hit them, it will further disrupt their supplies to the point of dissolving their operations here.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat. Completing a strike rewards code fragments, which can be turned in for special blueprints.</color>
* Type: Event
* EventId: event_season_amaSum_2023_t3
* Goals:
	* Task 1: Complete 3 side missions

## QE_AMASUM_2023_DAY13_T3
* Name: Day 13: Crown of Stones
* Description: We need to stockpile resources to prepare for a final battle against the Kiithless in the Hather Plains.

<color=#FBB03F>Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.</color>
* Type: Event
* EventId: event_season_amaSum_2023_t3
* Goals:
	* Task 1: GainItem

## QE_AMASUM_2023_DAY14_T3
* Name: Day 14: Lord of the Dust
* Description: All officers need to be briefed on the potential dangers posed by the remaining Kiithless fleet.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from dismissing officers and are earned through completing signals.</color>
* Type: Event
* EventId: event_season_amaSum_2023_t3
* Goals:
	* Task 1: GainItem

## QE_AMASUM_2023_DAY15_T3
* Name: Day 15: Kin of the Amassari
* Description: The Kiithless are targeting Ambadda waystation. Thassin's Needle, an artifact, is housed here. They must be stopped from raiding this station!

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it.</color>

<color=#FBB03F>To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Type: Event
* EventId: event_season_amaSum_2023_t3
* Goals:
	* Task 1: Complete mission 'event_03_StationDefense'

## QE_AMASUM_2023_DAILY_A_T4
* Name: Gather for Many
* Description: To continue operations in Amassari space, we need to replenish our strategic reserves. Collect resources to build up this stockpile.

<color=#FBB03F>Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
* Type: Event
* EventId: event_season_amaSum_2023_t4
* Goals:
	* Task 1: GainItem

## QE_AMASUM_2023_DAILY_B_T4
* Name: Make into Plenty
* Description: The quartermaster is concerned about our stockpile of spare parts. Begin construction of spares to replenish supplies.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
* Type: Event
* EventId: event_season_amaSum_2023_t4
* Goals:
	* Task 1: Craft

## QE_AMASUM_2023_DAILY_C_T4
* Name: Protect the Weak
* Description: Combat channels are rife with activity from Kiithless Hiigarans. It's our responsibility to put a stop to these raids and restore the peace.

<color=#FBB03F>While normally raiding Amassari space, Kidara's Kiithless have recently begun aggressive incursions into the rest of the galaxy. Find their fleets in signals and asteroid clusters and destroy them.</color>
* Type: Event
* EventId: event_season_amaSum_2023_t4
* Goals:
	* Task 1: 10 ShipsDestroyedDarkHiigaranT4

## QE_AMASUM_2023_DAILY_D_T4
* Name: Find the Lost
* Description: Monitoring Kiithless channels reveals a Progenitor Relic is nearby. We need to secure it before they do.

<color=#FBB03F>Progenitor relics can be found in relic signature signals. Relics can be sold on the market for credits, though some liaison offices may be interested in relics as well.</color>
* Type: Event
* EventId: event_season_amaSum_2023_t4
* Goals:
	* Task 1: GainItem

## QE_AMASUM_2023_DAY1_T4
* Name: Day 1: Provide Parts
* Description: The Amassari have very little in the way of developed industry, and would appreciate any refined parts we can provide. Craft some to provide a supply.

<color=#FBB03F>Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.</color>
* Type: Event
* EventId: event_season_amaSum_2023_t4
* Goals:
	* Task 1: Craft

## QE_AMASUM_2023_DAY2_T4
* Name: Day 2: Find Treasures
* Description: Sensors have detected possible ruins of interest in the vicinity. Investigate to see if there's anything of interest found here.

<color=#FBB03F>Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.</color>
* Type: Event
* EventId: event_season_amaSum_2023_t4
* Goals:
	* Task 1: Complete 3 side missions

## QE_AMASUM_2023_DAY3_T4
* Name: Day 3: Learn our Ways
* Description: Very little is known about the Hagthar Empire, the ancestors of the Amassari. In order to continue operations here, we need to educate our officers about what we know.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* Type: Event
* EventId: event_season_amaSum_2023_t4
* Goals:
	* Task 1: UpgradeOfficer

## QE_AMASUM_2023_DAY4_T4
* Name: Day 4: Ally and Friend
* Description: Our guide is willing to connect us with several Amassari officials in the vicinity that need help. We could benefit from this cooperation.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Higher reputation levels unlock additional items in that faction's liaison requisitions office.</color>
* Type: Event
* EventId: event_season_amaSum_2023_t4
* Goals:
	* Task 1: 5 Faction_Amassari_T4up

## QE_AMASUM_2023_DAY5_T4
* Name: Day 5: Race for Gold
* Description: Jothru has revealed there may be more information to find among the Hagthar ruins if we can find the pieces. We must prepare for this venture.

<color=#FBB03F>Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.</color>
* Type: Event
* EventId: event_season_amaSum_2023_t4
* Goals:
	* Task 1: GainItem

## QE_AMASUM_2023_DAY6_T4
* Name: Day 6: Hunting high and low
* Description: Jothru can provide the whereabouts, but not the exact location, of key pieces belonging to significant parts of Hagthar history. Perhaps we can learn what the Kiithless are seeking.

<color=#FBB03F>Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.</color>
* Type: Event
* EventId: event_season_amaSum_2023_t4
* Goals:
	* Task 1: Complete 3 side missions

## QE_AMASUM_2023_DAY7_T4
* Name: Day 7: Ways of the Enemy
* Description: Kiithless strikes have been increasing against the Amassari. We need to calibrate our training to match their new battle techniques in order to stop them.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from dismissing officers and are earned through completing signals.</color>
* Type: Event
* EventId: event_season_amaSum_2023_t4
* Goals:
	* Task 1: GainItem

## QE_AMASUM_2023_DAY8_T4
* Name: Day 8: Hand against Foe
* Description: Our training was timely. Jothru has handed us some leads on potential Kiithless activity in the region. We must investigate.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat. Completing a strike rewards code fragments, which can be turned in for special blueprints.</color>
* Type: Event
* EventId: event_season_amaSum_2023_t4
* Goals:
	* Task 1: Complete 5 side missions

## QE_AMASUM_2023_DAY9_T4
* Name: Day 9: Distant Gems
* Description: During our battles we took some hits to ship's stores. It's advised to rebuild our stockpiles with refined ores.

<color=#FBB03F>Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.</color>
* Type: Event
* EventId: event_season_amaSum_2023_t4
* Goals:
	* Task 1: Craft

## QE_AMASUM_2023_DAY10_T4
* Name: Day 10: Path of the Reclaimer
* Description: More Amassari have reached out to Jothru and us with more jobs. There's an unspoken offer as well to assist with our strikes against the Kiithless.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Higher reputation levels unlock additional items in that faction's liaison requisitions office.</color>
* Type: Event
* EventId: event_season_amaSum_2023_t4
* Goals:
	* Task 1: 5 Faction_Amassari_T4up

## QE_AMASUM_2023_DAY11_T4
* Name: Day 11: Knowledge and Defense
* Description: Assisting the Amassari has paid off, we're intercepting communications traffic suggesting they're being disrupted. We need to brief all officers on this stage of the operation against them.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* Type: Event
* EventId: event_season_amaSum_2023_t4
* Goals:
	* Task 1: UpgradeOfficer

## QE_AMASUM_2023_DAY12_T4
* Name: Day 12: Star Hunter
* Description: Fleet Intelligence has deduced several available targets belonging to the Kiithless. If we hit them, it will further disrupt their supplies to the point of dissolving their operations here.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat. Completing a strike rewards code fragments, which can be turned in for special blueprints.</color>
* Type: Event
* EventId: event_season_amaSum_2023_t4
* Goals:
	* Task 1: Complete 5 side missions

## QE_AMASUM_2023_DAY13_T4
* Name: Day 13: Crown of Stones
* Description: We need to stockpile resources to prepare for a final battle against the Kiithless in the Hather Plains.

<color=#FBB03F>Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.</color>
* Type: Event
* EventId: event_season_amaSum_2023_t4
* Goals:
	* Task 1: GainItem

## QE_AMASUM_2023_DAY14_T4
* Name: Day 14: Lord of the Dust
* Description: All officers need to be briefed on the potential dangers posed by the remaining Kiithless fleet.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from dismissing officers and are earned through completing signals.</color>
* Type: Event
* EventId: event_season_amaSum_2023_t4
* Goals:
	* Task 1: GainItem

## QE_AMASUM_2023_DAY15_T4
* Name: Day 15: Kin of the Amassari
* Description: The Kiithless are targeting Ambadda waystation. Thassin's Needle, an artifact, is housed here. They must be stopped from raiding this station!

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it.</color>

<color=#FBB03F>To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Type: Event
* EventId: event_season_amaSum_2023_t4
* Goals:
	* Task 1: Complete mission 'event_04_StationDefense'

## QE_7DAYS_MAR_2024_DAILY_A_T1
* Name: Routine Scan Test
* Description: Finds must be discovered through scanning. After being analyzed, they can be picked up to collect the reward inside.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t1
* Goals:
	* Task 1: Scan

## QE_7DAYS_MAR_2024_DAILY_A_T2
* Name: Routine Scan Test
* Description: Finds must be discovered through scanning. After being analyzed, they can be picked up to collect the reward inside.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t2
* Goals:
	* Task 1: Scan

## QE_7DAYS_MAR_2024_DAILY_A_T3
* Name: Routine Scan Test
* Description: Finds must be discovered through scanning. After being analyzed, they can be picked up to collect the reward inside.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t3
* Goals:
	* Task 1: Scan

## QE_7DAYS_MAR_2024_DAILY_A_T4
* Name: Routine Scan Test
* Description: Finds must be discovered through scanning. After being analyzed, they can be picked up to collect the reward inside.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t4
* Goals:
	* Task 1: Scan

## QE_7DAYS_MAR_2024_DAILY_B_T1
* Name: Archeological Charity
* Description: Progenitor relics can be found in relic signature signals.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t1
* Goals:
	* Task 1: Pay 1 None

## QE_7DAYS_MAR_2024_DAILY_B_T2
* Name: Archeological Charity
* Description: Progenitor relics can be found in relic signature signals.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t2
* Goals:
	* Task 1: Pay 1 None

## QE_7DAYS_MAR_2024_DAILY_B_T3
* Name: Archeological Charity
* Description: Progenitor relics can be found in relic signature signals.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t3
* Goals:
	* Task 1: Pay 1 None

## QE_7DAYS_MAR_2024_DAILY_B_T4
* Name: Archeological Charity
* Description: Progenitor relics can be found in relic signature signals.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t4
* Goals:
	* Task 1: Pay 1 None

## QE_7DAYS_MAR_2024_DAILY_C_T1
* Name: Combat Drill
* Description: Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t1
* Goals:
	* Task 1: Complete side mission

## QE_7DAYS_MAR_2024_DAILY_C_T2
* Name: Combat Drill
* Description: Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t2
* Goals:
	* Task 1: Complete side mission

## QE_7DAYS_MAR_2024_DAILY_C_T3
* Name: Combat Drill
* Description: Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t3
* Goals:
	* Task 1: Complete side mission

## QE_7DAYS_MAR_2024_DAILY_C_T4
* Name: Combat Drill
* Description: Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t4
* Goals:
	* Task 1: Complete side mission

## QE_7DAYS_MAR_2024_DAILY_D_T1
* Name: Road to Promotion
* Description: Prestige is earned through each player level-up and by completing daily and weekly assignments.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t1
* Goals:
	* Task 1: GainItem

## QE_7DAYS_MAR_2024_DAILY_D_T2
* Name: Road to Promotion
* Description: Prestige is earned through each player level-up and by completing daily and weekly assignments.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t2
* Goals:
	* Task 1: GainItem

## QE_7DAYS_MAR_2024_DAILY_D_T3
* Name: Road to Promotion
* Description: Prestige is earned through each player level-up and by completing daily and weekly assignments.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t3
* Goals:
	* Task 1: GainItem

## QE_7DAYS_MAR_2024_DAILY_D_T4
* Name: Road to Promotion
* Description: Prestige is earned through each player level-up and by completing daily and weekly assignments.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t4
* Goals:
	* Task 1: GainItem

## QE_7DAYS_MAR_2024_DAY1_A_T1
* Name: Day 1: Lay of the Land
* Description: Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t1
* Goals:
	* Task 1: Scan

## QE_7DAYS_MAR_2024_DAY1_A_T2
* Name: Day 1: Lay of the Land
* Description: Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t2
* Goals:
	* Task 1: Scan

## QE_7DAYS_MAR_2024_DAY1_A_T3
* Name: Day 1: Lay of the Land
* Description: Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t3
* Goals:
	* Task 1: Scan

## QE_7DAYS_MAR_2024_DAY1_A_T4
* Name: Day 1: Lay of the Land
* Description: Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t4
* Goals:
	* Task 1: Scan

## QE_7DAYS_MAR_2024_DAY1_B_T1
* Name: Day 1: Staking a Claim
* Description: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t1
* Goals:
	* Task 1: 15 ShipsDestroyedT1_ShipsDestroyedT2_ShipsDestroyedT3_ShipsDestroyedT4

## QE_7DAYS_MAR_2024_DAY1_B_T2
* Name: Day 1: Staking a Claim
* Description: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t2
* Goals:
	* Task 1: 15 ShipsDestroyedT2_ShipsDestroyedT3_ShipsDestroyedT4

## QE_7DAYS_MAR_2024_DAY1_B_T3
* Name: Day 1: Staking a Claim
* Description: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t3
* Goals:
	* Task 1: 15 ShipsDestroyedT3_ShipsDestroyedT4

## QE_7DAYS_MAR_2024_DAY1_B_T4
* Name: Day 1: Staking a Claim
* Description: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t4
* Goals:
	* Task 1: 15 ShipsDestroyedT4

## QE_7DAYS_MAR_2024_DAY1_C_T1
* Name: Day 1: Gathering
* Description: Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t1
* Goals:
	* Task 1: GainItem

## QE_7DAYS_MAR_2024_DAY1_C_T2
* Name: Day 1: Gathering
* Description: Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t2
* Goals:
	* Task 1: GainItem

## QE_7DAYS_MAR_2024_DAY1_C_T3
* Name: Day 1: Gathering
* Description: Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t3
* Goals:
	* Task 1: GainItem

## QE_7DAYS_MAR_2024_DAY1_C_T4
* Name: Day 1: Gathering
* Description: Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t4
* Goals:
	* Task 1: GainItem

## QE_7DAYS_MAR_2024_DAY1_D_T1
* Name: Day 1: Processing
* Description: Rare earths are an occasional by-product of refining. They are required for upgrading modules.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t1
* Goals:
	* Task 1: GainItem

## QE_7DAYS_MAR_2024_DAY1_D_T2
* Name: Day 1: Processing
* Description: Rare earths are an occasional by-product of refining. They are required for upgrading modules.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t2
* Goals:
	* Task 1: GainItem

## QE_7DAYS_MAR_2024_DAY1_D_T3
* Name: Day 1: Processing
* Description: Rare earths are an occasional by-product of refining. They are required for upgrading modules.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t3
* Goals:
	* Task 1: GainItem

## QE_7DAYS_MAR_2024_DAY1_D_T4
* Name: Day 1: Processing
* Description: Rare earths are an occasional by-product of refining. They are required for upgrading modules.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t4
* Goals:
	* Task 1: GainItem

## QE_7DAYS_MAR_2024_DAY2_A_T1
* Name: Day 2: Meet & Greet
* Description: There are different types of assignments available in your assignment log.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t1
* Goals:
	* Task 1: 5 T1up

## QE_7DAYS_MAR_2024_DAY2_A_T2
* Name: Day 2: Meet & Greet
* Description: Completing liaison assignments for a faction increases your reputation level for that faction. Higher reputation levels unlock additional items in that faction's liaison requisitions office.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t2
* Goals:
	* Task 1: 5 Faction_T2up

## QE_7DAYS_MAR_2024_DAY2_A_T3
* Name: Day 2: Meet & Greet
* Description: Completing liaison assignments for a faction increases your reputation level for that faction. Higher reputation levels unlock additional items in that faction's liaison requisitions office.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t3
* Goals:
	* Task 1: 5 Faction_T3up

## QE_7DAYS_MAR_2024_DAY2_A_T4
* Name: Day 2: Meet & Greet
* Description: Completing liaison assignments for a faction increases your reputation level for that faction. Higher reputation levels unlock additional items in that faction's liaison requisitions office.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t4
* Goals:
	* Task 1: 5 Faction_T4up

## QE_7DAYS_MAR_2024_DAY2_B_T1
* Name: Day 2: Cooperation
* Description: During missions you will usually fight against enemy ships. They can be part of an assignment, or they can be found as signals through scanning.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t1
* Goals:
	* Task 1: Complete 3 side missions

## QE_7DAYS_MAR_2024_DAY2_B_T2
* Name: Day 2: Cooperation
* Description: Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t2
* Goals:
	* Task 1: Complete 3 side missions

## QE_7DAYS_MAR_2024_DAY2_B_T3
* Name: Day 2: Cooperation
* Description: Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t3
* Goals:
	* Task 1: Complete 3 side missions

## QE_7DAYS_MAR_2024_DAY2_B_T4
* Name: Day 2: Cooperation
* Description: Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t4
* Goals:
	* Task 1: Complete 3 side missions

## QE_7DAYS_MAR_2024_DAY2_C_T1
* Name: Day 2: Cultural Exchange
* Description: Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t1
* Goals:
	* Task 1: GainItem

## QE_7DAYS_MAR_2024_DAY2_C_T2
* Name: Day 2: Cultural Exchange
* Description: Complete liaison assignments to gain reputation for that faction. A higher reputation unlocks more items in that faction's liaison requisitions office.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t2
* Goals:
	* Task 1: 135 RepTr1_RepTanoch_RepYaot_RepAmassari

## QE_7DAYS_MAR_2024_DAY2_C_T3
* Name: Day 2: Cultural Exchange
* Description: Complete liaison assignments to gain reputation for that faction. A higher reputation unlocks more items in that faction's liaison requisitions office.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t3
* Goals:
	* Task 1: 180 RepTr1_RepTanoch_RepYaot_RepAmassari

## QE_7DAYS_MAR_2024_DAY2_C_T4
* Name: Day 2: Cultural Exchange
* Description: Complete liaison assignments to gain reputation for that faction. A higher reputation unlocks more items in that faction's liaison requisitions office.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t4
* Goals:
	* Task 1: 225 RepTr1_RepTanoch_RepYaot_RepAmassari

## QE_7DAYS_MAR_2024_DAY2_D_T1
* Name: Day 2: Exchange Officers
* Description: Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t1
* Goals:
	* Task 1: UpgradeOfficer

## QE_7DAYS_MAR_2024_DAY2_D_T2
* Name: Day 2: Exchange Officers
* Description: Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t2
* Goals:
	* Task 1: UpgradeOfficer

## QE_7DAYS_MAR_2024_DAY2_D_T3
* Name: Day 2: Exchange Officers
* Description: Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t3
* Goals:
	* Task 1: UpgradeOfficer

## QE_7DAYS_MAR_2024_DAY2_D_T4
* Name: Day 2: Exchange Officers
* Description: Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t4
* Goals:
	* Task 1: UpgradeOfficer

## QE_7DAYS_MAR_2024_DAY3_A_T1
* Name: Day 3: Raw Materials
* Description: Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t1
* Goals:
	* Task 1: GainItem

## QE_7DAYS_MAR_2024_DAY3_A_T2
* Name: Day 3: Raw Materials
* Description: Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t2
* Goals:
	* Task 1: GainItem

## QE_7DAYS_MAR_2024_DAY3_A_T3
* Name: Day 3: Raw Materials
* Description: Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t3
* Goals:
	* Task 1: GainItem

## QE_7DAYS_MAR_2024_DAY3_A_T4
* Name: Day 3: Raw Materials
* Description: Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t4
* Goals:
	* Task 1: GainItem

## QE_7DAYS_MAR_2024_DAY3_B_T1
* Name: Day 3: Industry
* Description: Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t1
* Goals:
	* Task 1: Craft

## QE_7DAYS_MAR_2024_DAY3_B_T2
* Name: Day 3: Industry
* Description: Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t2
* Goals:
	* Task 1: Craft

## QE_7DAYS_MAR_2024_DAY3_B_T3
* Name: Day 3: Industry
* Description: Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t3
* Goals:
	* Task 1: Craft

## QE_7DAYS_MAR_2024_DAY3_B_T4
* Name: Day 3: Industry
* Description: Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t4
* Goals:
	* Task 1: Craft

## QE_7DAYS_MAR_2024_DAY3_C_T1
* Name: Day 3: Construction
* Description: Small items such as strike craft, modules and parts can be built in the fabricator. Larger items such as escort ships and flagships must be constructed at shipyards provided at larger stations.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t1
* Goals:
	* Task 1: Craft

## QE_7DAYS_MAR_2024_DAY3_C_T2
* Name: Day 3: Construction
* Description: Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t2
* Goals:
	* Task 1: Craft

## QE_7DAYS_MAR_2024_DAY3_C_T3
* Name: Day 3: Construction
* Description: Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t3
* Goals:
	* Task 1: Craft

## QE_7DAYS_MAR_2024_DAY3_C_T4
* Name: Day 3: Construction
* Description: Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t4
* Goals:
	* Task 1: Craft

## QE_7DAYS_MAR_2024_DAY3_D_T1
* Name: Day 3: Return on Investments
* Description: Items and resources can be sold for credits in the market at stations.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t1
* Goals:
	* Task 1: GainItem

## QE_7DAYS_MAR_2024_DAY3_D_T2
* Name: Day 3: Return on Investments
* Description: Items and resources can be sold for credits in the market at stations.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t2
* Goals:
	* Task 1: GainItem

## QE_7DAYS_MAR_2024_DAY3_D_T3
* Name: Day 3: Return on Investments
* Description: Items and resources can be sold for credits in the market at stations.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t3
* Goals:
	* Task 1: GainItem

## QE_7DAYS_MAR_2024_DAY3_D_T4
* Name: Day 3: Return on Investments
* Description: Items and resources can be sold for credits in the market at stations.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t4
* Goals:
	* Task 1: GainItem

## QE_7DAYS_MAR_2024_DAY4_A_T1
* Name: Day 4: Hypothesis
* Description: Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t1
* Goals:
	* Task 1: Complete 3 side missions

## QE_7DAYS_MAR_2024_DAY4_A_T2
* Name: Day 4: Hypothesis
* Description: Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t2
* Goals:
	* Task 1: GainItem

## QE_7DAYS_MAR_2024_DAY4_A_T3
* Name: Day 4: Hypothesis
* Description: Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t3
* Goals:
	* Task 1: GainItem

## QE_7DAYS_MAR_2024_DAY4_A_T4
* Name: Day 4: Hypothesis
* Description: Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t4
* Goals:
	* Task 1: GainItem

## QE_7DAYS_MAR_2024_DAY4_B_T1
* Name: Day 4: Validation
* Description: Progenitor relics can be found in relic signature signals. Relics can be sold on the market for credits, though some liaison offices may be interested in relics as well.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t1
* Goals:
	* Task 1: GainItem

## QE_7DAYS_MAR_2024_DAY4_B_T2
* Name: Day 4: Validation
* Description: Progenitor relics can be found in relic signature signals. Relics can be sold on the market for credits, though some liaison offices may be interested in relics as well.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t2
* Goals:
	* Task 1: GainItem

## QE_7DAYS_MAR_2024_DAY4_B_T3
* Name: Day 4: Validation
* Description: Progenitor relics can be found in relic signature signals. Relics can be sold on the market for credits, though some liaison offices may be interested in relics as well.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t3
* Goals:
	* Task 1: GainItem

## QE_7DAYS_MAR_2024_DAY4_B_T4
* Name: Day 4: Validation
* Description: Progenitor relics can be found in relic signature signals. Relics can be sold on the market for credits, though some liaison offices may be interested in relics as well.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t4
* Goals:
	* Task 1: GainItem

## QE_7DAYS_MAR_2024_DAY4_C_T1
* Name: Day 4: Practical Application
* Description: Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t1
* Goals:
	* Task 1: 7 ShipsDestroyedProgenitorT1_ShipsDestroyedProgenitorT2_ShipsDestroyedProgenitorT3_ShipsDestroyedProgenitorT4

## QE_7DAYS_MAR_2024_DAY4_C_T2
* Name: Day 4: Practical Application
* Description: Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t2
* Goals:
	* Task 1: 7 ShipsDestroyedProgenitorT2_ShipsDestroyedProgenitorT3_ShipsDestroyedProgenitorT4

## QE_7DAYS_MAR_2024_DAY4_C_T3
* Name: Day 4: Practical Application
* Description: Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t3
* Goals:
	* Task 1: 7 ShipsDestroyedProgenitorT3_ShipsDestroyedProgenitorT4

## QE_7DAYS_MAR_2024_DAY4_C_T4
* Name: Day 4: Practical Application
* Description: Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t4
* Goals:
	* Task 1: 7 ShipsDestroyedProgenitorT4

## QE_7DAYS_MAR_2024_DAY4_D_T1
* Name: Day 4: Results
* Description: Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t1
* Goals:
	* Task 1: Complete side mission

## QE_7DAYS_MAR_2024_DAY4_D_T2
* Name: Day 4: Results
* Description: Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t2
* Goals:
	* Task 1: Complete side mission

## QE_7DAYS_MAR_2024_DAY4_D_T3
* Name: Day 4: Results
* Description: Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t3
* Goals:
	* Task 1: Complete side mission

## QE_7DAYS_MAR_2024_DAY4_D_T4
* Name: Day 4: Results
* Description: Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t4
* Goals:
	* Task 1: Complete side mission

## QE_7DAYS_MAR_2024_DAY5_A_T1
* Name: Day 5: Lessons
* Description: Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t1
* Goals:
	* Task 1: Complete 3 side missions

## QE_7DAYS_MAR_2024_DAY5_A_T2
* Name: Day 5: Lessons
* Description: Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t2
* Goals:
	* Task 1: Complete 3 side missions

## QE_7DAYS_MAR_2024_DAY5_A_T3
* Name: Day 5: Lessons
* Description: Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t3
* Goals:
	* Task 1: Complete 3 side missions

## QE_7DAYS_MAR_2024_DAY5_A_T4
* Name: Day 5: Lessons
* Description: Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t4
* Goals:
	* Task 1: Complete 3 side missions

## QE_7DAYS_MAR_2024_DAY5_B_T1
* Name: Day 5: Training
* Description: Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t1
* Goals:
	* Task 1: GainItem

## QE_7DAYS_MAR_2024_DAY5_B_T2
* Name: Day 5: Training
* Description: Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t2
* Goals:
	* Task 1: GainItem

## QE_7DAYS_MAR_2024_DAY5_B_T3
* Name: Day 5: Training
* Description: Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t3
* Goals:
	* Task 1: GainItem

## QE_7DAYS_MAR_2024_DAY5_B_T4
* Name: Day 5: Training
* Description: Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t4
* Goals:
	* Task 1: GainItem

## QE_7DAYS_MAR_2024_DAY5_C_T1
* Name: Day 5: Promotion
* Description: Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t1
* Goals:
	* Task 1: UpgradeOfficer

## QE_7DAYS_MAR_2024_DAY5_C_T2
* Name: Day 5: Promotion
* Description: Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t2
* Goals:
	* Task 1: UpgradeOfficer

## QE_7DAYS_MAR_2024_DAY5_C_T3
* Name: Day 5: Promotion
* Description: Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t3
* Goals:
	* Task 1: UpgradeOfficer

## QE_7DAYS_MAR_2024_DAY5_C_T4
* Name: Day 5: Promotion
* Description: Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t4
* Goals:
	* Task 1: UpgradeOfficer

## QE_7DAYS_MAR_2024_DAY5_D_T1
* Name: Day 5: Graduation
* Description: Discharging officers grants credits and insignias, which can be used to level up other officers.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t1
* Goals:
	* Task 1: GainItem

## QE_7DAYS_MAR_2024_DAY5_D_T2
* Name: Day 5: Graduation
* Description: Discharging officers grants credits and insignias, which can be used to level up other officers.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t2
* Goals:
	* Task 1: GainItem

## QE_7DAYS_MAR_2024_DAY5_D_T3
* Name: Day 5: Graduation
* Description: Discharging officers grants credits and insignias, which can be used to level up other officers.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t3
* Goals:
	* Task 1: GainItem

## QE_7DAYS_MAR_2024_DAY5_D_T4
* Name: Day 5: Graduation
* Description: Discharging officers grants credits and insignias, which can be used to level up other officers.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t4
* Goals:
	* Task 1: GainItem

## QE_7DAYS_MAR_2024_DAY6_A_T1
* Name: Day 6: Stockpile
* Description: Rare earths are an occasional by-product of refining. They are required for upgrading modules.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t1
* Goals:
	* Task 1: GainItem

## QE_7DAYS_MAR_2024_DAY6_A_T2
* Name: Day 6: Stockpile
* Description: Rare earths are an occasional by-product of refining. They are required for upgrading modules.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t2
* Goals:
	* Task 1: GainItem

## QE_7DAYS_MAR_2024_DAY6_A_T3
* Name: Day 6: Stockpile
* Description: Rare earths are an occasional by-product of refining. They are required for upgrading modules.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t3
* Goals:
	* Task 1: GainItem

## QE_7DAYS_MAR_2024_DAY6_A_T4
* Name: Day 6: Stockpile
* Description: Rare earths are an occasional by-product of refining. They are required for upgrading modules.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t4
* Goals:
	* Task 1: GainItem

## QE_7DAYS_MAR_2024_DAY6_B_T1
* Name: Day 6: Reinforcements
* Description: Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t1
* Goals:
	* Task 1: UpgradeOfficer

## QE_7DAYS_MAR_2024_DAY6_B_T2
* Name: Day 6: Reinforcements
* Description: The strength of modules can be increased through upgrades, which cost rare earths.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t2
* Goals:
	* Task 1: Craft

## QE_7DAYS_MAR_2024_DAY6_B_T3
* Name: Day 6: Reinforcements
* Description: The strength of modules can be increased through upgrades, which cost rare earths.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t3
* Goals:
	* Task 1: Craft

## QE_7DAYS_MAR_2024_DAY6_B_T4
* Name: Day 6: Reinforcements
* Description: The strength of modules can be increased through upgrades, which cost rare earths.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t4
* Goals:
	* Task 1: Craft

## QE_7DAYS_MAR_2024_DAY6_C_T1
* Name: Day 6: Improvements
* Description: Small items such as strike craft, modules and parts can be built in the fabricator. Larger items such as escort ships and flagships must be constructed at shipyards provided at larger stations.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t1
* Goals:
	* Task 1: Craft

## QE_7DAYS_MAR_2024_DAY6_C_T2
* Name: Day 6: Improvements
* Description: Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t2
* Goals:
	* Task 1: Craft

## QE_7DAYS_MAR_2024_DAY6_C_T3
* Name: Day 6: Improvements
* Description: The strength of modules can be increased through upgrades, which cost rare earths.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t3
* Goals:
	* Task 1: Craft

## QE_7DAYS_MAR_2024_DAY6_C_T4
* Name: Day 6: Improvements
* Description: The strength of modules can be increased through upgrades, which cost rare earths.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t4
* Goals:
	* Task 1: Craft

## QE_7DAYS_MAR_2024_DAY6_D_T1
* Name: Day 6: Trial Run
* Description: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t1
* Goals:
	* Task 1: 15 ShipsDestroyedT1_ShipsDestroyedT2_ShipsDestroyedT3_ShipsDestroyedT4

## QE_7DAYS_MAR_2024_DAY6_D_T2
* Name: Day 6: Trial Run
* Description: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t2
* Goals:
	* Task 1: 15 ShipsDestroyedT2_ShipsDestroyedT3_ShipsDestroyedT4

## QE_7DAYS_MAR_2024_DAY6_D_T3
* Name: Day 6: Trial Run
* Description: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t3
* Goals:
	* Task 1: 15 ShipsDestroyedT3_ShipsDestroyedT4

## QE_7DAYS_MAR_2024_DAY6_D_T4
* Name: Day 6: Trial Run
* Description: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t4
* Goals:
	* Task 1: 15 ShipsDestroyedT4

## QE_7DAYS_MAR_2024_DAY7_A_T1
* Name: Day 7: Enemy Contact
* Description: Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t1
* Goals:
	* Task 1: Complete 3 side missions

## QE_7DAYS_MAR_2024_DAY7_A_T2
* Name: Day 7: Enemy Contact
* Description: Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t2
* Goals:
	* Task 1: Complete 3 side missions

## QE_7DAYS_MAR_2024_DAY7_A_T3
* Name: Day 7: Enemy Contact
* Description: Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t3
* Goals:
	* Task 1: Complete 3 side missions

## QE_7DAYS_MAR_2024_DAY7_A_T4
* Name: Day 7: Enemy Contact
* Description: Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t4
* Goals:
	* Task 1: Complete 3 side missions

## QE_7DAYS_MAR_2024_DAY7_B_T1
* Name: Day 7: Rules of Engagement
* Description: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t1
* Goals:
	* Task 1: 15 ShipsDestroyedT1_ShipsDestroyedT2_ShipsDestroyedT3_ShipsDestroyedT4

## QE_7DAYS_MAR_2024_DAY7_B_T2
* Name: Day 7: Rules of Engagement
* Description: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t2
* Goals:
	* Task 1: 15 ShipsDestroyedT2_ShipsDestroyedT3_ShipsDestroyedT4

## QE_7DAYS_MAR_2024_DAY7_B_T3
* Name: Day 7: Rules of Engagement
* Description: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t3
* Goals:
	* Task 1: 15 ShipsDestroyedT3_ShipsDestroyedT4

## QE_7DAYS_MAR_2024_DAY7_B_T4
* Name: Day 7: Rules of Engagement
* Description: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t4
* Goals:
	* Task 1: 15 ShipsDestroyedT4

## QE_7DAYS_MAR_2024_DAY7_C_T1
* Name: Day 7: Conflict
* Description: When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t1
* Goals:
	* Task 1: GainItem

## QE_7DAYS_MAR_2024_DAY7_C_T2
* Name: Day 7: Conflict
* Description: When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t2
* Goals:
	* Task 1: GainItem

## QE_7DAYS_MAR_2024_DAY7_C_T3
* Name: Day 7: Conflict
* Description: When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t3
* Goals:
	* Task 1: GainItem

## QE_7DAYS_MAR_2024_DAY7_C_T4
* Name: Day 7: Conflict
* Description: When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t4
* Goals:
	* Task 1: GainItem

## QE_7DAYS_MAR_2024_DAY7_D_T1
* Name: Day 7: Triumph
* Description: Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t1
* Goals:
	* Task 1: Complete 3 side missions

## QE_7DAYS_MAR_2024_DAY7_D_T2
* Name: Day 7: Triumph
* Description: Strikes are difficult missions that require a strong fleet from several commanders to beat. Completing a strike rewards code fragments, which can be turned in for special blueprints.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t2
* Goals:
	* Task 1: Complete side mission

## QE_7DAYS_MAR_2024_DAY7_D_T3
* Name: Day 7: Triumph
* Description: Strikes are difficult missions that require a strong fleet from several commanders to beat. Completing a strike rewards code fragments, which can be turned in for special blueprints.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t3
* Goals:
	* Task 1: Complete side mission

## QE_7DAYS_MAR_2024_DAY7_D_T4
* Name: Day 7: Triumph
* Description: Strikes are difficult missions that require a strong fleet from several commanders to beat. Completing a strike rewards code fragments, which can be turned in for special blueprints.
* Type: Event
* EventId: event_monthlyEvent_2024_03_01_t4
* Goals:
	* Task 1: Complete side mission

## QE_7DAYS_2023_08_DAY1_A_T1
* Name: Day 1: Lay of the Land
* Description: Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.
* Type: Event
* EventId: event_7days_2023_08_21_t1
* Goals:
	* Task 1: Scan

## QE_7DAYS_2023_08_DAY1_A_T2
* Name: Day 1: Lay of the Land
* Description: Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.
* Type: Event
* EventId: event_7days_2023_08_21_t2
* Goals:
	* Task 1: Scan

## QE_7DAYS_2023_08_DAY1_A_T3
* Name: Day 1: Lay of the Land
* Description: Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.
* Type: Event
* EventId: event_7days_2023_08_21_t3
* Goals:
	* Task 1: Scan

## QE_7DAYS_2023_08_DAY1_A_T4
* Name: Day 1: Lay of the Land
* Description: Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.
* Type: Event
* EventId: event_7days_2023_08_21_t4
* Goals:
	* Task 1: Scan

## QE_7DAYS_2023_08_DAY1_B_T1
* Name: Day 1: Staking a Claim
* Description: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Type: Event
* EventId: event_7days_2023_08_21_t1
* Goals:
	* Task 1: 15 ShipsDestroyedT1_ShipsDestroyedT2_ShipsDestroyedT3_ShipsDestroyedT4

## QE_7DAYS_2023_08_DAY1_B_T2
* Name: Day 1: Staking a Claim
* Description: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Type: Event
* EventId: event_7days_2023_08_21_t2
* Goals:
	* Task 1: 15 ShipsDestroyedT2_ShipsDestroyedT3_ShipsDestroyedT4

## QE_7DAYS_2023_08_DAY1_B_T3
* Name: Day 1: Staking a Claim
* Description: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Type: Event
* EventId: event_7days_2023_08_21_t3
* Goals:
	* Task 1: 15 ShipsDestroyedT3_ShipsDestroyedT4

## QE_7DAYS_2023_08_DAY1_B_T4
* Name: Day 1: Staking a Claim
* Description: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Type: Event
* EventId: event_7days_2023_08_21_t4
* Goals:
	* Task 1: 15 ShipsDestroyedT4

## QE_7DAYS_2023_08_DAY1_C_T1
* Name: Day 1: Gathering
* Description: Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.
* Type: Event
* EventId: event_7days_2023_08_21_t1
* Goals:
	* Task 1: GainItem

## QE_7DAYS_2023_08_DAY1_C_T2
* Name: Day 1: Gathering
* Description: Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.
* Type: Event
* EventId: event_7days_2023_08_21_t2
* Goals:
	* Task 1: GainItem

## QE_7DAYS_2023_08_DAY1_C_T3
* Name: Day 1: Gathering
* Description: Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.
* Type: Event
* EventId: event_7days_2023_08_21_t3
* Goals:
	* Task 1: GainItem

## QE_7DAYS_2023_08_DAY1_C_T4
* Name: Day 1: Gathering
* Description: Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.
* Type: Event
* EventId: event_7days_2023_08_21_t4
* Goals:
	* Task 1: GainItem

## QE_7DAYS_2023_08_DAY1_D_T1
* Name: Day 1: Processing
* Description: Rare earths are an occasional by-product of refining. They are required for upgrading modules.
* Type: Event
* EventId: event_7days_2023_08_21_t1
* Goals:
	* Task 1: GainItem

## QE_7DAYS_2023_08_DAY1_D_T2
* Name: Day 1: Processing
* Description: Rare earths are an occasional by-product of refining. They are required for upgrading modules.
* Type: Event
* EventId: event_7days_2023_08_21_t2
* Goals:
	* Task 1: GainItem

## QE_7DAYS_2023_08_DAY1_D_T3
* Name: Day 1: Processing
* Description: Rare earths are an occasional by-product of refining. They are required for upgrading modules.
* Type: Event
* EventId: event_7days_2023_08_21_t3
* Goals:
	* Task 1: GainItem

## QE_7DAYS_2023_08_DAY1_D_T4
* Name: Day 1: Processing
* Description: Rare earths are an occasional by-product of refining. They are required for upgrading modules.
* Type: Event
* EventId: event_7days_2023_08_21_t4
* Goals:
	* Task 1: GainItem

## QE_7DAYS_2023_08_DAY2_A_T1
* Name: Day 2: Meet & Greet
* Description: There are different types of assignments available in your assignment log.
* Type: Event
* EventId: event_7days_2023_08_21_t1
* Goals:
	* Task 1: 5 T1up

## QE_7DAYS_2023_08_DAY2_A_T2
* Name: Day 2: Meet & Greet
* Description: Completing liaison assignments for a faction increases your reputation level for that faction. Higher reputation levels unlock additional items in that faction's liaison requisitions office.
* Type: Event
* EventId: event_7days_2023_08_21_t2
* Goals:
	* Task 1: 5 Faction_T2up

## QE_7DAYS_2023_08_DAY2_A_T3
* Name: Day 2: Meet & Greet
* Description: Completing liaison assignments for a faction increases your reputation level for that faction. Higher reputation levels unlock additional items in that faction's liaison requisitions office.
* Type: Event
* EventId: event_7days_2023_08_21_t3
* Goals:
	* Task 1: 5 Faction_T3up

## QE_7DAYS_2023_08_DAY2_A_T4
* Name: Day 2: Meet & Greet
* Description: Completing liaison assignments for a faction increases your reputation level for that faction. Higher reputation levels unlock additional items in that faction's liaison requisitions office.
* Type: Event
* EventId: event_7days_2023_08_21_t4
* Goals:
	* Task 1: 5 Faction_T4up

## QE_7DAYS_2023_08_DAY2_B_T1
* Name: Day 2: Cooperation
* Description: During missions you will usually fight against enemy ships. They can be part of an assignment, or they can be found as signals through scanning.
* Type: Event
* EventId: event_7days_2023_08_21_t1
* Goals:
	* Task 1: Complete 3 side missions

## QE_7DAYS_2023_08_DAY2_B_T2
* Name: Day 2: Cooperation
* Description: Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.
* Type: Event
* EventId: event_7days_2023_08_21_t2
* Goals:
	* Task 1: Complete 3 side missions

## QE_7DAYS_2023_08_DAY2_B_T3
* Name: Day 2: Cooperation
* Description: Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.
* Type: Event
* EventId: event_7days_2023_08_21_t3
* Goals:
	* Task 1: Complete 3 side missions

## QE_7DAYS_2023_08_DAY2_B_T4
* Name: Day 2: Cooperation
* Description: Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.
* Type: Event
* EventId: event_7days_2023_08_21_t4
* Goals:
	* Task 1: Complete 3 side missions

## QE_7DAYS_2023_08_DAY2_C_T1
* Name: Day 2: Cultural Exchange
* Description: Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.
* Type: Event
* EventId: event_7days_2023_08_21_t1
* Goals:
	* Task 1: GainItem

## QE_7DAYS_2023_08_DAY2_C_T2
* Name: Day 2: Cultural Exchange
* Description: Complete liaison assignments to gain reputation for that faction. A higher reputation unlocks more items in that faction's liaison requisitions office.
* Type: Event
* EventId: event_7days_2023_08_21_t2
* Goals:
	* Task 1: 135 RepTr1_RepTanoch_RepYaot_RepAmassari

## QE_7DAYS_2023_08_DAY2_C_T3
* Name: Day 2: Cultural Exchange
* Description: Complete liaison assignments to gain reputation for that faction. A higher reputation unlocks more items in that faction's liaison requisitions office.
* Type: Event
* EventId: event_7days_2023_08_21_t3
* Goals:
	* Task 1: 180 RepTr1_RepTanoch_RepYaot_RepAmassari

## QE_7DAYS_2023_08_DAY2_C_T4
* Name: Day 2: Cultural Exchange
* Description: Complete liaison assignments to gain reputation for that faction. A higher reputation unlocks more items in that faction's liaison requisitions office.
* Type: Event
* EventId: event_7days_2023_08_21_t4
* Goals:
	* Task 1: 225 RepTr1_RepTanoch_RepYaot_RepAmassari

## QE_7DAYS_2023_08_DAY2_D_T1
* Name: Day 2: Exchange Officers
* Description: Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* Type: Event
* EventId: event_7days_2023_08_21_t1
* Goals:
	* Task 1: UpgradeOfficer

## QE_7DAYS_2023_08_DAY2_D_T2
* Name: Day 2: Exchange Officers
* Description: Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* Type: Event
* EventId: event_7days_2023_08_21_t2
* Goals:
	* Task 1: UpgradeOfficer

## QE_7DAYS_2023_08_DAY2_D_T3
* Name: Day 2: Exchange Officers
* Description: Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* Type: Event
* EventId: event_7days_2023_08_21_t3
* Goals:
	* Task 1: UpgradeOfficer

## QE_7DAYS_2023_08_DAY2_D_T4
* Name: Day 2: Exchange Officers
* Description: Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* Type: Event
* EventId: event_7days_2023_08_21_t4
* Goals:
	* Task 1: UpgradeOfficer

## QE_7DAYS_2023_08_DAY3_A_T1
* Name: Day 3: Raw Materials
* Description: Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.
* Type: Event
* EventId: event_7days_2023_08_21_t1
* Goals:
	* Task 1: GainItem

## QE_7DAYS_2023_08_DAY3_A_T2
* Name: Day 3: Raw Materials
* Description: Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.
* Type: Event
* EventId: event_7days_2023_08_21_t2
* Goals:
	* Task 1: GainItem

## QE_7DAYS_2023_08_DAY3_A_T3
* Name: Day 3: Raw Materials
* Description: Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.
* Type: Event
* EventId: event_7days_2023_08_21_t3
* Goals:
	* Task 1: GainItem

## QE_7DAYS_2023_08_DAY3_A_T4
* Name: Day 3: Raw Materials
* Description: Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.
* Type: Event
* EventId: event_7days_2023_08_21_t4
* Goals:
	* Task 1: GainItem

## QE_7DAYS_2023_08_DAY3_B_T1
* Name: Day 3: Industry
* Description: Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.
* Type: Event
* EventId: event_7days_2023_08_21_t1
* Goals:
	* Task 1: Craft

## QE_7DAYS_2023_08_DAY3_B_T2
* Name: Day 3: Industry
* Description: Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.
* Type: Event
* EventId: event_7days_2023_08_21_t2
* Goals:
	* Task 1: Craft

## QE_7DAYS_2023_08_DAY3_B_T3
* Name: Day 3: Industry
* Description: Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.
* Type: Event
* EventId: event_7days_2023_08_21_t3
* Goals:
	* Task 1: Craft

## QE_7DAYS_2023_08_DAY3_B_T4
* Name: Day 3: Industry
* Description: Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.
* Type: Event
* EventId: event_7days_2023_08_21_t4
* Goals:
	* Task 1: Craft

## QE_7DAYS_2023_08_DAY3_C_T1
* Name: Day 3: Construction
* Description: Small items such as strike craft, modules and parts can be built in the fabricator. Larger items such as escort ships and flagships must be constructed at shipyards provided at larger stations.
* Type: Event
* EventId: event_7days_2023_08_21_t1
* Goals:
	* Task 1: Craft

## QE_7DAYS_2023_08_DAY3_C_T2
* Name: Day 3: Construction
* Description: Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.
* Type: Event
* EventId: event_7days_2023_08_21_t2
* Goals:
	* Task 1: Craft

## QE_7DAYS_2023_08_DAY3_C_T3
* Name: Day 3: Construction
* Description: Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.
* Type: Event
* EventId: event_7days_2023_08_21_t3
* Goals:
	* Task 1: Craft

## QE_7DAYS_2023_08_DAY3_C_T4
* Name: Day 3: Construction
* Description: Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.
* Type: Event
* EventId: event_7days_2023_08_21_t4
* Goals:
	* Task 1: Craft

## QE_7DAYS_2023_08_DAY3_D_T1
* Name: Day 3: Return on Investments
* Description: Items and resources can be sold for credits in the market at stations.
* Type: Event
* EventId: event_7days_2023_08_21_t1
* Goals:
	* Task 1: GainItem

## QE_7DAYS_2023_08_DAY3_D_T2
* Name: Day 3: Return on Investments
* Description: Items and resources can be sold for credits in the market at stations.
* Type: Event
* EventId: event_7days_2023_08_21_t2
* Goals:
	* Task 1: GainItem

## QE_7DAYS_2023_08_DAY3_D_T3
* Name: Day 3: Return on Investments
* Description: Items and resources can be sold for credits in the market at stations.
* Type: Event
* EventId: event_7days_2023_08_21_t3
* Goals:
	* Task 1: GainItem

## QE_7DAYS_2023_08_DAY3_D_T4
* Name: Day 3: Return on Investments
* Description: Items and resources can be sold for credits in the market at stations.
* Type: Event
* EventId: event_7days_2023_08_21_t4
* Goals:
	* Task 1: GainItem

## QE_7DAYS_2023_08_DAY4_A_T1
* Name: Day 4: Hypothesis
* Description: Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
* Type: Event
* EventId: event_7days_2023_08_21_t1
* Goals:
	* Task 1: Complete 3 side missions

## QE_7DAYS_2023_08_DAY4_A_T2
* Name: Day 4: Hypothesis
* Description: Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.
* Type: Event
* EventId: event_7days_2023_08_21_t2
* Goals:
	* Task 1: GainItem

## QE_7DAYS_2023_08_DAY4_A_T3
* Name: Day 4: Hypothesis
* Description: Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.
* Type: Event
* EventId: event_7days_2023_08_21_t3
* Goals:
	* Task 1: GainItem

## QE_7DAYS_2023_08_DAY4_A_T4
* Name: Day 4: Hypothesis
* Description: Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.
* Type: Event
* EventId: event_7days_2023_08_21_t4
* Goals:
	* Task 1: GainItem

## QE_7DAYS_2023_08_DAY4_B_T1
* Name: Day 4: Validation
* Description: Progenitor relics can be found in relic signature signals. Relics can be sold on the market for credits, though some liaison offices may be interested in relics as well.
* Type: Event
* EventId: event_7days_2023_08_21_t1
* Goals:
	* Task 1: GainItem

## QE_7DAYS_2023_08_DAY4_B_T2
* Name: Day 4: Validation
* Description: Progenitor relics can be found in relic signature signals. Relics can be sold on the market for credits, though some liaison offices may be interested in relics as well.
* Type: Event
* EventId: event_7days_2023_08_21_t2
* Goals:
	* Task 1: GainItem

## QE_7DAYS_2023_08_DAY4_B_T3
* Name: Day 4: Validation
* Description: Progenitor relics can be found in relic signature signals. Relics can be sold on the market for credits, though some liaison offices may be interested in relics as well.
* Type: Event
* EventId: event_7days_2023_08_21_t3
* Goals:
	* Task 1: GainItem

## QE_7DAYS_2023_08_DAY4_B_T4
* Name: Day 4: Validation
* Description: Progenitor relics can be found in relic signature signals. Relics can be sold on the market for credits, though some liaison offices may be interested in relics as well.
* Type: Event
* EventId: event_7days_2023_08_21_t4
* Goals:
	* Task 1: GainItem

## QE_7DAYS_2023_08_DAY4_C_T1
* Name: Day 4: Practical Application
* Description: Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.
* Type: Event
* EventId: event_7days_2023_08_21_t1
* Goals:
	* Task 1: 7 ShipsDestroyedProgenitorT1_ShipsDestroyedProgenitorT2_ShipsDestroyedProgenitorT3_ShipsDestroyedProgenitorT4

## QE_7DAYS_2023_08_DAY4_C_T2
* Name: Day 4: Practical Application
* Description: Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.
* Type: Event
* EventId: event_7days_2023_08_21_t2
* Goals:
	* Task 1: 7 ShipsDestroyedProgenitorT2_ShipsDestroyedProgenitorT3_ShipsDestroyedProgenitorT4

## QE_7DAYS_2023_08_DAY4_C_T3
* Name: Day 4: Practical Application
* Description: Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.
* Type: Event
* EventId: event_7days_2023_08_21_t3
* Goals:
	* Task 1: 7 ShipsDestroyedProgenitorT3_ShipsDestroyedProgenitorT4

## QE_7DAYS_2023_08_DAY4_C_T4
* Name: Day 4: Practical Application
* Description: Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.
* Type: Event
* EventId: event_7days_2023_08_21_t4
* Goals:
	* Task 1: 7 ShipsDestroyedProgenitorT4

## QE_7DAYS_2023_08_DAY4_D_T1
* Name: Day 4: Results
* Description: Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.
* Type: Event
* EventId: event_7days_2023_08_21_t1
* Goals:
	* Task 1: Complete side mission

## QE_7DAYS_2023_08_DAY4_D_T2
* Name: Day 4: Results
* Description: Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.
* Type: Event
* EventId: event_7days_2023_08_21_t2
* Goals:
	* Task 1: Complete side mission

## QE_7DAYS_2023_08_DAY4_D_T3
* Name: Day 4: Results
* Description: Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.
* Type: Event
* EventId: event_7days_2023_08_21_t3
* Goals:
	* Task 1: Complete side mission

## QE_7DAYS_2023_08_DAY4_D_T4
* Name: Day 4: Results
* Description: Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.
* Type: Event
* EventId: event_7days_2023_08_21_t4
* Goals:
	* Task 1: Complete side mission

## QE_7DAYS_2023_08_DAY5_A_T1
* Name: Day 5: Lessons
* Description: Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
* Type: Event
* EventId: event_7days_2023_08_21_t1
* Goals:
	* Task 1: Complete 3 side missions

## QE_7DAYS_2023_08_DAY5_A_T2
* Name: Day 5: Lessons
* Description: Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
* Type: Event
* EventId: event_7days_2023_08_21_t2
* Goals:
	* Task 1: Complete 3 side missions

## QE_7DAYS_2023_08_DAY5_A_T3
* Name: Day 5: Lessons
* Description: Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
* Type: Event
* EventId: event_7days_2023_08_21_t3
* Goals:
	* Task 1: Complete 3 side missions

## QE_7DAYS_2023_08_DAY5_A_T4
* Name: Day 5: Lessons
* Description: Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
* Type: Event
* EventId: event_7days_2023_08_21_t4
* Goals:
	* Task 1: Complete 3 side missions

## QE_7DAYS_2023_08_DAY5_B_T1
* Name: Day 5: Training
* Description: Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.
* Type: Event
* EventId: event_7days_2023_08_21_t1
* Goals:
	* Task 1: GainItem

## QE_7DAYS_2023_08_DAY5_B_T2
* Name: Day 5: Training
* Description: Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.
* Type: Event
* EventId: event_7days_2023_08_21_t2
* Goals:
	* Task 1: GainItem

## QE_7DAYS_2023_08_DAY5_B_T3
* Name: Day 5: Training
* Description: Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.
* Type: Event
* EventId: event_7days_2023_08_21_t3
* Goals:
	* Task 1: GainItem

## QE_7DAYS_2023_08_DAY5_B_T4
* Name: Day 5: Training
* Description: Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.
* Type: Event
* EventId: event_7days_2023_08_21_t4
* Goals:
	* Task 1: GainItem

## QE_7DAYS_2023_08_DAY5_C_T1
* Name: Day 5: Promotion
* Description: Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* Type: Event
* EventId: event_7days_2023_08_21_t1
* Goals:
	* Task 1: UpgradeOfficer

## QE_7DAYS_2023_08_DAY5_C_T2
* Name: Day 5: Promotion
* Description: Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* Type: Event
* EventId: event_7days_2023_08_21_t2
* Goals:
	* Task 1: UpgradeOfficer

## QE_7DAYS_2023_08_DAY5_C_T3
* Name: Day 5: Promotion
* Description: Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* Type: Event
* EventId: event_7days_2023_08_21_t3
* Goals:
	* Task 1: UpgradeOfficer

## QE_7DAYS_2023_08_DAY5_C_T4
* Name: Day 5: Promotion
* Description: Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* Type: Event
* EventId: event_7days_2023_08_21_t4
* Goals:
	* Task 1: UpgradeOfficer

## QE_7DAYS_2023_08_DAY5_D_T1
* Name: Day 5: Graduation
* Description: Discharging officers grants credits and insignias, which can be used to level up other officers.
* Type: Event
* EventId: event_7days_2023_08_21_t1
* Goals:
	* Task 1: GainItem

## QE_7DAYS_2023_08_DAY5_D_T2
* Name: Day 5: Graduation
* Description: Discharging officers grants credits and insignias, which can be used to level up other officers.
* Type: Event
* EventId: event_7days_2023_08_21_t2
* Goals:
	* Task 1: GainItem

## QE_7DAYS_2023_08_DAY5_D_T3
* Name: Day 5: Graduation
* Description: Discharging officers grants credits and insignias, which can be used to level up other officers.
* Type: Event
* EventId: event_7days_2023_08_21_t3
* Goals:
	* Task 1: GainItem

## QE_7DAYS_2023_08_DAY5_D_T4
* Name: Day 5: Graduation
* Description: Discharging officers grants credits and insignias, which can be used to level up other officers.
* Type: Event
* EventId: event_7days_2023_08_21_t4
* Goals:
	* Task 1: GainItem

## QE_7DAYS_2023_08_DAY6_A_T1
* Name: Day 6: Stockpile
* Description: Rare earths are an occasional by-product of refining. They are required for upgrading modules.
* Type: Event
* EventId: event_7days_2023_08_21_t1
* Goals:
	* Task 1: GainItem

## QE_7DAYS_2023_08_DAY6_A_T2
* Name: Day 6: Stockpile
* Description: Rare earths are an occasional by-product of refining. They are required for upgrading modules.
* Type: Event
* EventId: event_7days_2023_08_21_t2
* Goals:
	* Task 1: GainItem

## QE_7DAYS_2023_08_DAY6_A_T3
* Name: Day 6: Stockpile
* Description: Rare earths are an occasional by-product of refining. They are required for upgrading modules.
* Type: Event
* EventId: event_7days_2023_08_21_t3
* Goals:
	* Task 1: GainItem

## QE_7DAYS_2023_08_DAY6_A_T4
* Name: Day 6: Stockpile
* Description: Rare earths are an occasional by-product of refining. They are required for upgrading modules.
* Type: Event
* EventId: event_7days_2023_08_21_t4
* Goals:
	* Task 1: GainItem

## QE_7DAYS_2023_08_DAY6_B_T1
* Name: Day 6: Reinforcements
* Description: Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
* Type: Event
* EventId: event_7days_2023_08_21_t1
* Goals:
	* Task 1: UpgradeOfficer

## QE_7DAYS_2023_08_DAY6_B_T2
* Name: Day 6: Reinforcements
* Description: The strength of modules can be increased through upgrades, which cost rare earths.
* Type: Event
* EventId: event_7days_2023_08_21_t2
* Goals:
	* Task 1: Craft

## QE_7DAYS_2023_08_DAY6_B_T3
* Name: Day 6: Reinforcements
* Description: The strength of modules can be increased through upgrades, which cost rare earths.
* Type: Event
* EventId: event_7days_2023_08_21_t3
* Goals:
	* Task 1: Craft

## QE_7DAYS_2023_08_DAY6_B_T4
* Name: Day 6: Reinforcements
* Description: The strength of modules can be increased through upgrades, which cost rare earths.
* Type: Event
* EventId: event_7days_2023_08_21_t4
* Goals:
	* Task 1: Craft

## QE_7DAYS_2023_08_DAY6_C_T1
* Name: Day 6: Improvements
* Description: Small items such as strike craft, modules and parts can be built in the fabricator. Larger items such as escort ships and flagships must be constructed at shipyards provided at larger stations.
* Type: Event
* EventId: event_7days_2023_08_21_t1
* Goals:
	* Task 1: Craft

## QE_7DAYS_2023_08_DAY6_C_T2
* Name: Day 6: Improvements
* Description: Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.
* Type: Event
* EventId: event_7days_2023_08_21_t2
* Goals:
	* Task 1: Craft

## QE_7DAYS_2023_08_DAY6_C_T3
* Name: Day 6: Improvements
* Description: The strength of modules can be increased through upgrades, which cost rare earths.
* Type: Event
* EventId: event_7days_2023_08_21_t3
* Goals:
	* Task 1: Craft

## QE_7DAYS_2023_08_DAY6_C_T4
* Name: Day 6: Improvements
* Description: The strength of modules can be increased through upgrades, which cost rare earths.
* Type: Event
* EventId: event_7days_2023_08_21_t4
* Goals:
	* Task 1: Craft

## QE_7DAYS_2023_08_DAY6_D_T1
* Name: Day 6: Trial Run
* Description: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Type: Event
* EventId: event_7days_2023_08_21_t1
* Goals:
	* Task 1: 15 ShipsDestroyedT1_ShipsDestroyedT2_ShipsDestroyedT3_ShipsDestroyedT4

## QE_7DAYS_2023_08_DAY6_D_T2
* Name: Day 6: Trial Run
* Description: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Type: Event
* EventId: event_7days_2023_08_21_t2
* Goals:
	* Task 1: 15 ShipsDestroyedT2_ShipsDestroyedT3_ShipsDestroyedT4

## QE_7DAYS_2023_08_DAY6_D_T3
* Name: Day 6: Trial Run
* Description: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Type: Event
* EventId: event_7days_2023_08_21_t3
* Goals:
	* Task 1: 15 ShipsDestroyedT3_ShipsDestroyedT4

## QE_7DAYS_2023_08_DAY6_D_T4
* Name: Day 6: Trial Run
* Description: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Type: Event
* EventId: event_7days_2023_08_21_t4
* Goals:
	* Task 1: 15 ShipsDestroyedT4

## QE_7DAYS_2023_08_DAY7_A_T1
* Name: Day 7: Enemy Contact
* Description: Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
* Type: Event
* EventId: event_7days_2023_08_21_t1
* Goals:
	* Task 1: Complete 3 side missions

## QE_7DAYS_2023_08_DAY7_A_T2
* Name: Day 7: Enemy Contact
* Description: Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
* Type: Event
* EventId: event_7days_2023_08_21_t2
* Goals:
	* Task 1: Complete 3 side missions

## QE_7DAYS_2023_08_DAY7_A_T3
* Name: Day 7: Enemy Contact
* Description: Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
* Type: Event
* EventId: event_7days_2023_08_21_t3
* Goals:
	* Task 1: Complete 3 side missions

## QE_7DAYS_2023_08_DAY7_A_T4
* Name: Day 7: Enemy Contact
* Description: Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
* Type: Event
* EventId: event_7days_2023_08_21_t4
* Goals:
	* Task 1: Complete 3 side missions

## QE_7DAYS_2023_08_DAY7_B_T1
* Name: Day 7: Rules of Engagement
* Description: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Type: Event
* EventId: event_7days_2023_08_21_t1
* Goals:
	* Task 1: 15 ShipsDestroyedT1_ShipsDestroyedT2_ShipsDestroyedT3_ShipsDestroyedT4

## QE_7DAYS_2023_08_DAY7_B_T2
* Name: Day 7: Rules of Engagement
* Description: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Type: Event
* EventId: event_7days_2023_08_21_t2
* Goals:
	* Task 1: 15 ShipsDestroyedT2_ShipsDestroyedT3_ShipsDestroyedT4

## QE_7DAYS_2023_08_DAY7_B_T3
* Name: Day 7: Rules of Engagement
* Description: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Type: Event
* EventId: event_7days_2023_08_21_t3
* Goals:
	* Task 1: 15 ShipsDestroyedT3_ShipsDestroyedT4

## QE_7DAYS_2023_08_DAY7_B_T4
* Name: Day 7: Rules of Engagement
* Description: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
* Type: Event
* EventId: event_7days_2023_08_21_t4
* Goals:
	* Task 1: 15 ShipsDestroyedT4

## QE_7DAYS_2023_08_DAY7_C_T1
* Name: Day 7: Conflict
* Description: When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.
* Type: Event
* EventId: event_7days_2023_08_21_t1
* Goals:
	* Task 1: GainItem

## QE_7DAYS_2023_08_DAY7_C_T2
* Name: Day 7: Conflict
* Description: When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.
* Type: Event
* EventId: event_7days_2023_08_21_t2
* Goals:
	* Task 1: GainItem

## QE_7DAYS_2023_08_DAY7_C_T3
* Name: Day 7: Conflict
* Description: When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.
* Type: Event
* EventId: event_7days_2023_08_21_t3
* Goals:
	* Task 1: GainItem

## QE_7DAYS_2023_08_DAY7_C_T4
* Name: Day 7: Conflict
* Description: When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.
* Type: Event
* EventId: event_7days_2023_08_21_t4
* Goals:
	* Task 1: GainItem

## QE_7DAYS_2023_08_DAY7_D_T1
* Name: Day 7: Triumph
* Description: Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
* Type: Event
* EventId: event_7days_2023_08_21_t1
* Goals:
	* Task 1: Complete 3 side missions

## QE_7DAYS_2023_08_DAY7_D_T2
* Name: Day 7: Triumph
* Description: Strikes are difficult missions that require a strong fleet from several commanders to beat. Completing a strike rewards code fragments, which can be turned in for special blueprints.
* Type: Event
* EventId: event_7days_2023_08_21_t2
* Goals:
	* Task 1: Complete side mission

## QE_7DAYS_2023_08_DAY7_D_T3
* Name: Day 7: Triumph
* Description: Strikes are difficult missions that require a strong fleet from several commanders to beat. Completing a strike rewards code fragments, which can be turned in for special blueprints.
* Type: Event
* EventId: event_7days_2023_08_21_t3
* Goals:
	* Task 1: Complete side mission

## QE_7DAYS_2023_08_DAY7_D_T4
* Name: Day 7: Triumph
* Description: Strikes are difficult missions that require a strong fleet from several commanders to beat. Completing a strike rewards code fragments, which can be turned in for special blueprints.
* Type: Event
* EventId: event_7days_2023_08_21_t4
* Goals:
	* Task 1: Complete side mission

## QE_IYAFAL_2023_DAILY_A_T1
* Name: No header for quest qe_iyaFal_2023_daily_A_t1
* Description: No description for quest qe_iyaFal_2023_daily_A_t1

* Type: Event
* EventId: event_season_iyaFal_2023_t1
* Goals:
	* Task 1: 10 ShipsDestroyedP1T1_ShipsDestroyedP1T2_ShipsDestroyedP1T3_ShipsDestroyedP1T4

## QE_IYAFAL_2023_DAILY_B_T1
* Name: No header for quest qe_iyaFal_2023_daily_B_t1
* Description: No description for quest qe_iyaFal_2023_daily_B_t1

* Type: Event
* EventId: event_season_iyaFal_2023_t1
* Goals:
	* Task 1: GainItem

## QE_IYAFAL_2023_DAILY_C_T1
* Name: No header for quest qe_iyaFal_2023_daily_C_t1
* Description: No description for quest qe_iyaFal_2023_daily_C_t1

* Type: Event
* EventId: event_season_iyaFal_2023_t1
* Goals:
	* Task 1: Scan

## QE_IYAFAL_2023_DAILY_D_T1
* Name: No header for quest qe_iyaFal_2023_daily_D_t1
* Description: No description for quest qe_iyaFal_2023_daily_D_t1

* Type: Event
* EventId: event_season_iyaFal_2023_t1
* Goals:
	* Task 1: GainItem

## QE_IYAFAL_2023_DAY01_T1
* Name: No header for quest qe_iyaFal_2023_day01_t1
* Description: No description for quest qe_iyaFal_2023_day01_t1

* Type: Event
* EventId: event_season_iyaFal_2023_t1
* Goals:
	* Task 1: 5 T1up

## QE_IYAFAL_2023_DAY02_T1
* Name: No header for quest qe_iyaFal_2023_day02_t1
* Description: No description for quest qe_iyaFal_2023_day02_t1

* Type: Event
* EventId: event_season_iyaFal_2023_t1
* Goals:
	* Task 1: GainItem

## QE_IYAFAL_2023_DAY03_T1
* Name: No header for quest qe_iyaFal_2023_day03_t1
* Description: No description for quest qe_iyaFal_2023_day03_t1

* Type: Event
* EventId: event_season_iyaFal_2023_t1
* Goals:
	* Task 1: Craft

## QE_IYAFAL_2023_DAY04_T1
* Name: No header for quest qe_iyaFal_2023_day04_t1
* Description: No description for quest qe_iyaFal_2023_day04_t1

* Type: Event
* EventId: event_season_iyaFal_2023_t1
* MailsOnCompletion: m_iyaFal_day4_log
* Goals:
	* Task 1: Complete 3 side missions

## QE_IYAFAL_2023_DAY05_T1
* Name: No header for quest qe_iyaFal_2023_day05_t1
* Description: No description for quest qe_iyaFal_2023_day05_t1

* Type: Event
* EventId: event_season_iyaFal_2023_t1
* Goals:
	* Task 1: Complete 3 side missions

## QE_IYAFAL_2023_DAY06_T1
* Name: No header for quest qe_iyaFal_2023_day06_t1
* Description: No description for quest qe_iyaFal_2023_day06_t1

* Type: Event
* EventId: event_season_iyaFal_2023_t1
* Goals:
	* Task 1: GainItem

## QE_IYAFAL_2023_DAY07_T1
* Name: No header for quest qe_iyaFal_2023_day07_t1
* Description: No description for quest qe_iyaFal_2023_day07_t1

* Type: Event
* EventId: event_season_iyaFal_2023_t1
* Goals:
	* Task 1: UpgradeOfficer

## QE_IYAFAL_2023_DAY08_T1
* Name: No header for quest qe_iyaFal_2023_day08_t1
* Description: No description for quest qe_iyaFal_2023_day08_t1

* Type: Event
* EventId: event_season_iyaFal_2023_t1
* MailsOnCompletion: m_iyaFal_day8_log
* Goals:
	* Task 1: GainItem

## QE_IYAFAL_2023_DAY09_T1
* Name: No header for quest qe_iyaFal_2023_day09_t1
* Description: No description for quest qe_iyaFal_2023_day09_t1

* Type: Event
* EventId: event_season_iyaFal_2023_t1
* Goals:
	* Task 1: 5 T1up

## QE_IYAFAL_2023_DAY10_T1
* Name: No header for quest qe_iyaFal_2023_day10_t1
* Description: No description for quest qe_iyaFal_2023_day10_t1

* Type: Event
* EventId: event_season_iyaFal_2023_t1
* Goals:
	* Task 1: GainItem

## QE_IYAFAL_2023_DAY11_T1
* Name: No header for quest qe_iyaFal_2023_day11_t1
* Description: No description for quest qe_iyaFal_2023_day11_t1

* Type: Event
* EventId: event_season_iyaFal_2023_t1
* Goals:
	* Task 1: Craft

## QE_IYAFAL_2023_DAY12_T1
* Name: No header for quest qe_iyaFal_2023_day12_t1
* Description: No description for quest qe_iyaFal_2023_day12_t1

* Type: Event
* EventId: event_season_iyaFal_2023_t1
* MailsOnCompletion: m_iyaFal_day12_log
* Goals:
	* Task 1: Complete side mission

## QE_IYAFAL_2023_DAY13_T1
* Name: No header for quest qe_iyaFal_2023_day13_t1
* Description: No description for quest qe_iyaFal_2023_day13_t1

* Type: Event
* EventId: event_season_iyaFal_2023_t1
* Goals:
	* Task 1: GainItem

## QE_IYAFAL_2023_DAY14_T1
* Name: No header for quest qe_iyaFal_2023_day14_t1
* Description: No description for quest qe_iyaFal_2023_day14_t1

* Type: Event
* EventId: event_season_iyaFal_2023_t1
* Goals:
	* Task 1: GainItem

## QE_IYAFAL_2023_DAY15_T1
* Name: No header for quest qe_iyaFal_2023_day15_t1
* Description: No description for quest qe_iyaFal_2023_day15_t1

* Type: Event
* EventId: event_season_iyaFal_2023_t1
* Goals:
	* Task 1: Complete mission 'Trader's Bargain T1'

## QE_IYAFAL_2023_EPI01_T1
* Name: No header for quest qe_iyaFal_2023_epi01_t1
* Description: No description for quest qe_iyaFal_2023_epi01_t1

* Type: Event
* EventId: event_season_iyaFal_2023_t1
* Goals:
	* Task 1: GainItem

## QE_IYAFAL_2023_EPI02_T1
* Name: No header for quest qe_iyaFal_2023_epi02_t1
* Description: No description for quest qe_iyaFal_2023_epi02_t1

* Type: Event
* EventId: event_season_iyaFal_2023_t1
* Goals:
	* Task 1: 10 ShipsDestroyedProgenitorT1_ShipsDestroyedProgenitorT2_ShipsDestroyedProgenitorT3_ShipsDestroyedProgenitorT4

## QE_IYAFAL_2023_EPI03_T1
* Name: No header for quest qe_iyaFal_2023_epi03_t1
* Description: No description for quest qe_iyaFal_2023_epi03_t1

* Type: Event
* EventId: event_season_iyaFal_2023_t1
* Goals:
	* Task 1: GainItem

## QE_IYAFAL_2023_EPI04_T1
* Name: No header for quest qe_iyaFal_2023_epi04_t1
* Description: No description for quest qe_iyaFal_2023_epi04_t1

* Type: Event
* EventId: event_season_iyaFal_2023_t1
* Goals:
	* Task 1: UpgradeOfficer

## QE_IYAFAL_2023_EPI05_T1
* Name: No header for quest qe_iyaFal_2023_epi05_t1
* Description: No description for quest qe_iyaFal_2023_epi05_t1

* Type: Event
* EventId: event_season_iyaFal_2023_t1
* Goals:
	* Task 1: Complete side mission

## QE_IYAFAL_2023_DAILY_A_T2
* Name: No header for quest qe_iyaFal_2023_daily_A_t2
* Description: No description for quest qe_iyaFal_2023_daily_A_t2

* Type: Event
* EventId: event_season_iyaFal_2023_t2
* Goals:
	* Task 1: 10 ShipsDestroyedP1T2_ShipsDestroyedP1T3_ShipsDestroyedP1T4

## QE_IYAFAL_2023_DAILY_B_T2
* Name: No header for quest qe_iyaFal_2023_daily_B_t2
* Description: No description for quest qe_iyaFal_2023_daily_B_t2

* Type: Event
* EventId: event_season_iyaFal_2023_t2
* Goals:
	* Task 1: GainItem

## QE_IYAFAL_2023_DAILY_C_T2
* Name: No header for quest qe_iyaFal_2023_daily_C_t2
* Description: No description for quest qe_iyaFal_2023_daily_C_t2

* Type: Event
* EventId: event_season_iyaFal_2023_t2
* Goals:
	* Task 1: Scan

## QE_IYAFAL_2023_DAILY_D_T2
* Name: No header for quest qe_iyaFal_2023_daily_D_t2
* Description: No description for quest qe_iyaFal_2023_daily_D_t2

* Type: Event
* EventId: event_season_iyaFal_2023_t2
* Goals:
	* Task 1: GainItem

## QE_IYAFAL_2023_DAY01_T2
* Name: No header for quest qe_iyaFal_2023_day01_t2
* Description: No description for quest qe_iyaFal_2023_day01_t2

* Type: Event
* EventId: event_season_iyaFal_2023_t2
* Goals:
	* Task 1: 5 Faction_Tr1_T2up

## QE_IYAFAL_2023_DAY02_T2
* Name: No header for quest qe_iyaFal_2023_day02_t2
* Description: No description for quest qe_iyaFal_2023_day02_t2

* Type: Event
* EventId: event_season_iyaFal_2023_t2
* Goals:
	* Task 1: GainItem

## QE_IYAFAL_2023_DAY03_T2
* Name: No header for quest qe_iyaFal_2023_day03_t2
* Description: No description for quest qe_iyaFal_2023_day03_t2

* Type: Event
* EventId: event_season_iyaFal_2023_t2
* Goals:
	* Task 1: Craft

## QE_IYAFAL_2023_DAY04_T2
* Name: No header for quest qe_iyaFal_2023_day04_t2
* Description: No description for quest qe_iyaFal_2023_day04_t2

* Type: Event
* EventId: event_season_iyaFal_2023_t2
* MailsOnCompletion: m_iyaFal_day4_log
* Goals:
	* Task 1: Complete 3 side missions

## QE_IYAFAL_2023_DAY05_T2
* Name: No header for quest qe_iyaFal_2023_day05_t2
* Description: No description for quest qe_iyaFal_2023_day05_t2

* Type: Event
* EventId: event_season_iyaFal_2023_t2
* Goals:
	* Task 1: Complete 3 side missions

## QE_IYAFAL_2023_DAY06_T2
* Name: No header for quest qe_iyaFal_2023_day06_t2
* Description: No description for quest qe_iyaFal_2023_day06_t2

* Type: Event
* EventId: event_season_iyaFal_2023_t2
* Goals:
	* Task 1: GainItem

## QE_IYAFAL_2023_DAY07_T2
* Name: No header for quest qe_iyaFal_2023_day07_t2
* Description: No description for quest qe_iyaFal_2023_day07_t2

* Type: Event
* EventId: event_season_iyaFal_2023_t2
* Goals:
	* Task 1: UpgradeOfficer

## QE_IYAFAL_2023_DAY08_T2
* Name: No header for quest qe_iyaFal_2023_day08_t2
* Description: No description for quest qe_iyaFal_2023_day08_t2

* Type: Event
* EventId: event_season_iyaFal_2023_t2
* MailsOnCompletion: m_iyaFal_day8_log
* Goals:
	* Task 1: GainItem

## QE_IYAFAL_2023_DAY09_T2
* Name: No header for quest qe_iyaFal_2023_day09_t2
* Description: No description for quest qe_iyaFal_2023_day09_t2

* Type: Event
* EventId: event_season_iyaFal_2023_t2
* Goals:
	* Task 1: 5 Faction_Tr1_T2up

## QE_IYAFAL_2023_DAY10_T2
* Name: No header for quest qe_iyaFal_2023_day10_t2
* Description: No description for quest qe_iyaFal_2023_day10_t2

* Type: Event
* EventId: event_season_iyaFal_2023_t2
* Goals:
	* Task 1: GainItem

## QE_IYAFAL_2023_DAY11_T2
* Name: No header for quest qe_iyaFal_2023_day11_t2
* Description: No description for quest qe_iyaFal_2023_day11_t2

* Type: Event
* EventId: event_season_iyaFal_2023_t2
* Goals:
	* Task 1: GainItem

## QE_IYAFAL_2023_DAY12_T2
* Name: No header for quest qe_iyaFal_2023_day12_t2
* Description: No description for quest qe_iyaFal_2023_day12_t2

* Type: Event
* EventId: event_season_iyaFal_2023_t2
* MailsOnCompletion: m_iyaFal_day12_log
* Goals:
	* Task 1: Complete side mission

## QE_IYAFAL_2023_DAY13_T2
* Name: No header for quest qe_iyaFal_2023_day13_t2
* Description: No description for quest qe_iyaFal_2023_day13_t2

* Type: Event
* EventId: event_season_iyaFal_2023_t2
* Goals:
	* Task 1: 135 RepTr1

## QE_IYAFAL_2023_DAY14_T2
* Name: No header for quest qe_iyaFal_2023_day14_t2
* Description: No description for quest qe_iyaFal_2023_day14_t2

* Type: Event
* EventId: event_season_iyaFal_2023_t2
* Goals:
	* Task 1: GainItem

## QE_IYAFAL_2023_DAY15_T2
* Name: No header for quest qe_iyaFal_2023_day15_t2
* Description: No description for quest qe_iyaFal_2023_day15_t2

* Type: Event
* EventId: event_season_iyaFal_2023_t2
* Goals:
	* Task 1: Complete mission 'Trader's Bargain T2'

## QE_IYAFAL_2023_EPI01_T2
* Name: No header for quest qe_iyaFal_2023_epi01_t2
* Description: No description for quest qe_iyaFal_2023_epi01_t2

* Type: Event
* EventId: event_season_iyaFal_2023_t2
* Goals:
	* Task 1: GainItem

## QE_IYAFAL_2023_EPI02_T2
* Name: No header for quest qe_iyaFal_2023_epi02_t2
* Description: No description for quest qe_iyaFal_2023_epi02_t2

* Type: Event
* EventId: event_season_iyaFal_2023_t2
* Goals:
	* Task 1: 10 ShipsDestroyedProgenitorT2_ShipsDestroyedProgenitorT3_ShipsDestroyedProgenitorT4

## QE_IYAFAL_2023_EPI03_T2
* Name: No header for quest qe_iyaFal_2023_epi03_t2
* Description: No description for quest qe_iyaFal_2023_epi03_t2

* Type: Event
* EventId: event_season_iyaFal_2023_t2
* Goals:
	* Task 1: GainItem

## QE_IYAFAL_2023_EPI04_T2
* Name: No header for quest qe_iyaFal_2023_epi04_t2
* Description: No description for quest qe_iyaFal_2023_epi04_t2

* Type: Event
* EventId: event_season_iyaFal_2023_t2
* Goals:
	* Task 1: UpgradeOfficer

## QE_IYAFAL_2023_EPI05_T2
* Name: No header for quest qe_iyaFal_2023_epi05_t2
* Description: No description for quest qe_iyaFal_2023_epi05_t2

* Type: Event
* EventId: event_season_iyaFal_2023_t2
* Goals:
	* Task 1: Complete side mission

## QE_IYAFAL_2023_DAILY_A_T3
* Name: No header for quest qe_iyaFal_2023_daily_A_t3
* Description: No description for quest qe_iyaFal_2023_daily_A_t3

* Type: Event
* EventId: event_season_iyaFal_2023_t3
* Goals:
	* Task 1: 10 ShipsDestroyedP1T3_ShipsDestroyedP1T4

## QE_IYAFAL_2023_DAILY_B_T3
* Name: No header for quest qe_iyaFal_2023_daily_B_t3
* Description: No description for quest qe_iyaFal_2023_daily_B_t3

* Type: Event
* EventId: event_season_iyaFal_2023_t3
* Goals:
	* Task 1: GainItem

## QE_IYAFAL_2023_DAILY_C_T3
* Name: No header for quest qe_iyaFal_2023_daily_C_t3
* Description: No description for quest qe_iyaFal_2023_daily_C_t3

* Type: Event
* EventId: event_season_iyaFal_2023_t3
* Goals:
	* Task 1: Scan

## QE_IYAFAL_2023_DAILY_D_T3
* Name: No header for quest qe_iyaFal_2023_daily_D_t3
* Description: No description for quest qe_iyaFal_2023_daily_D_t3

* Type: Event
* EventId: event_season_iyaFal_2023_t3
* Goals:
	* Task 1: GainItem

## QE_IYAFAL_2023_DAY01_T3
* Name: No header for quest qe_iyaFal_2023_day01_t3
* Description: No description for quest qe_iyaFal_2023_day01_t3

* Type: Event
* EventId: event_season_iyaFal_2023_t3
* Goals:
	* Task 1: 5 Faction_Tr1_T3up

## QE_IYAFAL_2023_DAY02_T3
* Name: No header for quest qe_iyaFal_2023_day02_t3
* Description: No description for quest qe_iyaFal_2023_day02_t3

* Type: Event
* EventId: event_season_iyaFal_2023_t3
* Goals:
	* Task 1: GainItem

## QE_IYAFAL_2023_DAY03_T3
* Name: No header for quest qe_iyaFal_2023_day03_t3
* Description: No description for quest qe_iyaFal_2023_day03_t3

* Type: Event
* EventId: event_season_iyaFal_2023_t3
* Goals:
	* Task 1: Craft

## QE_IYAFAL_2023_DAY04_T3
* Name: No header for quest qe_iyaFal_2023_day04_t3
* Description: No description for quest qe_iyaFal_2023_day04_t3

* Type: Event
* EventId: event_season_iyaFal_2023_t3
* MailsOnCompletion: m_iyaFal_day4_log
* Goals:
	* Task 1: Complete 3 side missions

## QE_IYAFAL_2023_DAY05_T3
* Name: No header for quest qe_iyaFal_2023_day05_t3
* Description: No description for quest qe_iyaFal_2023_day05_t3

* Type: Event
* EventId: event_season_iyaFal_2023_t3
* Goals:
	* Task 1: Complete 3 side missions

## QE_IYAFAL_2023_DAY06_T3
* Name: No header for quest qe_iyaFal_2023_day06_t3
* Description: No description for quest qe_iyaFal_2023_day06_t3

* Type: Event
* EventId: event_season_iyaFal_2023_t3
* Goals:
	* Task 1: GainItem

## QE_IYAFAL_2023_DAY07_T3
* Name: No header for quest qe_iyaFal_2023_day07_t3
* Description: No description for quest qe_iyaFal_2023_day07_t3

* Type: Event
* EventId: event_season_iyaFal_2023_t3
* Goals:
	* Task 1: UpgradeOfficer

## QE_IYAFAL_2023_DAY08_T3
* Name: No header for quest qe_iyaFal_2023_day08_t3
* Description: No description for quest qe_iyaFal_2023_day08_t3

* Type: Event
* EventId: event_season_iyaFal_2023_t3
* MailsOnCompletion: m_iyaFal_day8_log
* Goals:
	* Task 1: GainItem

## QE_IYAFAL_2023_DAY09_T3
* Name: No header for quest qe_iyaFal_2023_day09_t3
* Description: No description for quest qe_iyaFal_2023_day09_t3

* Type: Event
* EventId: event_season_iyaFal_2023_t3
* Goals:
	* Task 1: 5 Faction_Tr1_T3up

## QE_IYAFAL_2023_DAY10_T3
* Name: No header for quest qe_iyaFal_2023_day10_t3
* Description: No description for quest qe_iyaFal_2023_day10_t3

* Type: Event
* EventId: event_season_iyaFal_2023_t3
* Goals:
	* Task 1: GainItem

## QE_IYAFAL_2023_DAY11_T3
* Name: No header for quest qe_iyaFal_2023_day11_t3
* Description: No description for quest qe_iyaFal_2023_day11_t3

* Type: Event
* EventId: event_season_iyaFal_2023_t3
* Goals:
	* Task 1: GainItem

## QE_IYAFAL_2023_DAY12_T3
* Name: No header for quest qe_iyaFal_2023_day12_t3
* Description: No description for quest qe_iyaFal_2023_day12_t3

* Type: Event
* EventId: event_season_iyaFal_2023_t3
* MailsOnCompletion: m_iyaFal_day12_log
* Goals:
	* Task 1: Complete side mission

## QE_IYAFAL_2023_DAY13_T3
* Name: No header for quest qe_iyaFal_2023_day13_t3
* Description: No description for quest qe_iyaFal_2023_day13_t3

* Type: Event
* EventId: event_season_iyaFal_2023_t3
* Goals:
	* Task 1: 180 RepTr1

## QE_IYAFAL_2023_DAY14_T3
* Name: No header for quest qe_iyaFal_2023_day14_t3
* Description: No description for quest qe_iyaFal_2023_day14_t3

* Type: Event
* EventId: event_season_iyaFal_2023_t3
* Goals:
	* Task 1: GainItem

## QE_IYAFAL_2023_DAY15_T3
* Name: No header for quest qe_iyaFal_2023_day15_t3
* Description: No description for quest qe_iyaFal_2023_day15_t3

* Type: Event
* EventId: event_season_iyaFal_2023_t3
* Goals:
	* Task 1: Complete mission 'Trader's Bargain T3'

## QE_IYAFAL_2023_EPI01_T3
* Name: No header for quest qe_iyaFal_2023_epi01_t3
* Description: No description for quest qe_iyaFal_2023_epi01_t3

* Type: Event
* EventId: event_season_iyaFal_2023_t3
* Goals:
	* Task 1: GainItem

## QE_IYAFAL_2023_EPI02_T3
* Name: No header for quest qe_iyaFal_2023_epi02_t3
* Description: No description for quest qe_iyaFal_2023_epi02_t3

* Type: Event
* EventId: event_season_iyaFal_2023_t3
* Goals:
	* Task 1: 10 ShipsDestroyedProgenitorT3_ShipsDestroyedProgenitorT4

## QE_IYAFAL_2023_EPI03_T3
* Name: No header for quest qe_iyaFal_2023_epi03_t3
* Description: No description for quest qe_iyaFal_2023_epi03_t3

* Type: Event
* EventId: event_season_iyaFal_2023_t3
* Goals:
	* Task 1: GainItem

## QE_IYAFAL_2023_EPI04_T3
* Name: No header for quest qe_iyaFal_2023_epi04_t3
* Description: No description for quest qe_iyaFal_2023_epi04_t3

* Type: Event
* EventId: event_season_iyaFal_2023_t3
* Goals:
	* Task 1: UpgradeOfficer

## QE_IYAFAL_2023_EPI05_T3
* Name: No header for quest qe_iyaFal_2023_epi05_t3
* Description: No description for quest qe_iyaFal_2023_epi05_t3

* Type: Event
* EventId: event_season_iyaFal_2023_t3
* Goals:
	* Task 1: Complete 3 side missions

## QE_IYAFAL_2023_DAILY_A_T4
* Name: No header for quest qe_iyaFal_2023_daily_A_t4
* Description: No description for quest qe_iyaFal_2023_daily_A_t4

* Type: Event
* EventId: event_season_iyaFal_2023_t4
* Goals:
	* Task 1: 10 ShipsDestroyedP1T4

## QE_IYAFAL_2023_DAILY_B_T4
* Name: No header for quest qe_iyaFal_2023_daily_B_t4
* Description: No description for quest qe_iyaFal_2023_daily_B_t4

* Type: Event
* EventId: event_season_iyaFal_2023_t4
* Goals:
	* Task 1: GainItem

## QE_IYAFAL_2023_DAILY_C_T4
* Name: No header for quest qe_iyaFal_2023_daily_C_t4
* Description: No description for quest qe_iyaFal_2023_daily_C_t4

* Type: Event
* EventId: event_season_iyaFal_2023_t4
* Goals:
	* Task 1: Scan

## QE_IYAFAL_2023_DAILY_D_T4
* Name: No header for quest qe_iyaFal_2023_daily_D_t4
* Description: No description for quest qe_iyaFal_2023_daily_D_t4

* Type: Event
* EventId: event_season_iyaFal_2023_t4
* Goals:
	* Task 1: GainItem

## QE_IYAFAL_2023_DAY01_T4
* Name: No header for quest qe_iyaFal_2023_day01_t4
* Description: No description for quest qe_iyaFal_2023_day01_t4

* Type: Event
* EventId: event_season_iyaFal_2023_t4
* Goals:
	* Task 1: 5 Faction_T4up

## QE_IYAFAL_2023_DAY02_T4
* Name: No header for quest qe_iyaFal_2023_day02_t4
* Description: No description for quest qe_iyaFal_2023_day02_t4

* Type: Event
* EventId: event_season_iyaFal_2023_t4
* Goals:
	* Task 1: GainItem

## QE_IYAFAL_2023_DAY03_T4
* Name: No header for quest qe_iyaFal_2023_day03_t4
* Description: No description for quest qe_iyaFal_2023_day03_t4

* Type: Event
* EventId: event_season_iyaFal_2023_t4
* Goals:
	* Task 1: Craft

## QE_IYAFAL_2023_DAY04_T4
* Name: No header for quest qe_iyaFal_2023_day04_t4
* Description: No description for quest qe_iyaFal_2023_day04_t4

* Type: Event
* EventId: event_season_iyaFal_2023_t4
* MailsOnCompletion: m_iyaFal_day4_log
* Goals:
	* Task 1: Complete 3 side missions

## QE_IYAFAL_2023_DAY05_T4
* Name: No header for quest qe_iyaFal_2023_day05_t4
* Description: No description for quest qe_iyaFal_2023_day05_t4

* Type: Event
* EventId: event_season_iyaFal_2023_t4
* Goals:
	* Task 1: Complete 3 side missions

## QE_IYAFAL_2023_DAY06_T4
* Name: No header for quest qe_iyaFal_2023_day06_t4
* Description: No description for quest qe_iyaFal_2023_day06_t4

* Type: Event
* EventId: event_season_iyaFal_2023_t4
* Goals:
	* Task 1: GainItem

## QE_IYAFAL_2023_DAY07_T4
* Name: No header for quest qe_iyaFal_2023_day07_t4
* Description: No description for quest qe_iyaFal_2023_day07_t4

* Type: Event
* EventId: event_season_iyaFal_2023_t4
* Goals:
	* Task 1: UpgradeOfficer

## QE_IYAFAL_2023_DAY08_T4
* Name: No header for quest qe_iyaFal_2023_day08_t4
* Description: No description for quest qe_iyaFal_2023_day08_t4

* Type: Event
* EventId: event_season_iyaFal_2023_t4
* MailsOnCompletion: m_iyaFal_day8_log
* Goals:
	* Task 1: GainItem

## QE_IYAFAL_2023_DAY09_T4
* Name: No header for quest qe_iyaFal_2023_day09_t4
* Description: No description for quest qe_iyaFal_2023_day09_t4

* Type: Event
* EventId: event_season_iyaFal_2023_t4
* Goals:
	* Task 1: 5 Faction_T4up

## QE_IYAFAL_2023_DAY10_T4
* Name: No header for quest qe_iyaFal_2023_day10_t4
* Description: No description for quest qe_iyaFal_2023_day10_t4

* Type: Event
* EventId: event_season_iyaFal_2023_t4
* Goals:
	* Task 1: GainItem

## QE_IYAFAL_2023_DAY11_T4
* Name: No header for quest qe_iyaFal_2023_day11_t4
* Description: No description for quest qe_iyaFal_2023_day11_t4

* Type: Event
* EventId: event_season_iyaFal_2023_t4
* Goals:
	* Task 1: GainItem

## QE_IYAFAL_2023_DAY12_T4
* Name: No header for quest qe_iyaFal_2023_day12_t4
* Description: No description for quest qe_iyaFal_2023_day12_t4

* Type: Event
* EventId: event_season_iyaFal_2023_t4
* MailsOnCompletion: m_iyaFal_day12_log
* Goals:
	* Task 1: Complete side mission

## QE_IYAFAL_2023_DAY13_T4
* Name: No header for quest qe_iyaFal_2023_day13_t4
* Description: No description for quest qe_iyaFal_2023_day13_t4

* Type: Event
* EventId: event_season_iyaFal_2023_t4
* Goals:
	* Task 1: 225 RepTr1

## QE_IYAFAL_2023_DAY14_T4
* Name: No header for quest qe_iyaFal_2023_day14_t4
* Description: No description for quest qe_iyaFal_2023_day14_t4

* Type: Event
* EventId: event_season_iyaFal_2023_t4
* Goals:
	* Task 1: GainItem

## QE_IYAFAL_2023_DAY15_T4
* Name: No header for quest qe_iyaFal_2023_day15_t4
* Description: No description for quest qe_iyaFal_2023_day15_t4

* Type: Event
* EventId: event_season_iyaFal_2023_t4
* Goals:
	* Task 1: Complete mission 'Trader's Bargain T4'

## QE_IYAFAL_2023_EPI01_T4
* Name: No header for quest qe_iyaFal_2023_epi01_t4
* Description: No description for quest qe_iyaFal_2023_epi01_t4

* Type: Event
* EventId: event_season_iyaFal_2023_t4
* Goals:
	* Task 1: GainItem

## QE_IYAFAL_2023_EPI02_T4
* Name: No header for quest qe_iyaFal_2023_epi02_t4
* Description: No description for quest qe_iyaFal_2023_epi02_t4

* Type: Event
* EventId: event_season_iyaFal_2023_t4
* Goals:
	* Task 1: 10 ShipsDestroyedProgenitorT4

## QE_IYAFAL_2023_EPI03_T4
* Name: No header for quest qe_iyaFal_2023_epi03_t4
* Description: No description for quest qe_iyaFal_2023_epi03_t4

* Type: Event
* EventId: event_season_iyaFal_2023_t4
* Goals:
	* Task 1: GainItem

## QE_IYAFAL_2023_EPI04_T4
* Name: No header for quest qe_iyaFal_2023_epi04_t4
* Description: No description for quest qe_iyaFal_2023_epi04_t4

* Type: Event
* EventId: event_season_iyaFal_2023_t4
* Goals:
	* Task 1: UpgradeOfficer

## QE_IYAFAL_2023_EPI05_T4
* Name: No header for quest qe_iyaFal_2023_epi05_t4
* Description: No description for quest qe_iyaFal_2023_epi05_t4

* Type: Event
* EventId: event_season_iyaFal_2023_t4
* Goals:
	* Task 1: Complete 5 side missions

## QE_ANNIVERSARY_2023_DAILY_A_T1
* Name: Active Monitoring
* Description: Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
* Type: Event
* EventId: event_anniversary_2023_t1
* Goals:
	* Task 1: Complete 5 side missions

## QE_ANNIVERSARY_2023_DAILY_B_T1
* Name: Refining Results
* Description: Rare earths are an occasional by-product of refining. They are required for upgrading modules.
* Type: Event
* EventId: event_anniversary_2023_t1
* Goals:
	* Task 1: GainItem

## QE_ANNIVERSARY_2023_DAY01_A_T1
* Name: Day 1: Research Directive
* Description: We received priority communication from Lazarus Base concerning Gideon S'jet. The transmission is encrypted with a specific vibration that can only be found on Hiigaran fabricators. We need to construct any item to match the encryption.

<color=#FBB03F>Small items such as strike craft, modules and parts can be built in the fabricator. Larger items such as escort ships and flagships must be constructed at shipyards provided at larger stations.</color>
* Type: Event
* EventId: event_anniversary_2023_t1
* Goals:
	* Task 1: Craft

## QE_ANNIVERSARY_2023_DAY01_B_T1
* Name: Day 1: Seek and Find
* Description: The list given to us by Gideon includes many components found only in Progenitor ships. The easiest way to collect them is to harvest them from downed Progenitor units.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
* Type: Event
* EventId: event_anniversary_2023_t1
* Goals:
	* Task 1: 7 ShipsDestroyedProgenitorT1_ShipsDestroyedProgenitorT2_ShipsDestroyedProgenitorT3_ShipsDestroyedProgenitorT4

## QE_ANNIVERSARY_2023_DAY01_C_T1
* Name: Day 1: The Capstone
* Description: Progenitor Cognition Nodes are a fragile component often found floating in free space near ancient wreckages.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
* Type: Event
* EventId: event_anniversary_2023_t1
* Goals:
	* Task 1: GainItem

## QE_ANNIVERSARY_2023_DAY02_A_T1
* Name: Day 2: Cash Money
* Description: Ekekko can bring us in contact with traders specialized in Progenitor technology. But knowing the Iyatequa, everything has a price. We should mine minerals to recuperate the losses we'll have to pay.

<color=#FBB03F>Ore can be mined from asteroids in asteroid fields. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
* Type: Event
* EventId: event_anniversary_2023_t1
* Goals:
	* Task 1: GainItem

## QE_ANNIVERSARY_2023_DAY02_B_T1
* Name: Day 2: Songs and Tales
* Description: To impress the Iyatequa traders and buy the Progenitor components for Gideon, we will have to work on our reputation.

<color=#FBB03F>You can earn insignias by completing missions.</color>
* Type: Event
* EventId: event_anniversary_2023_t1
* Goals:
	* Task 1: GainItem

## QE_ANNIVERSARY_2023_DAY02_C_T1
* Name: Day 2: Merchant Supreme
* Description: In order to raise funds to acquire the needed Progenitor components for Gideon, we must sell some of our stored items on the local market.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
* Type: Event
* EventId: event_anniversary_2023_t1
* Goals:
	* Task 1: GainItem

## QE_ANNIVERSARY_2023_DAY03_A_T1
* Name: Day 3: Stop Scouting
* Description: We need to search for recent communications data in this sector to pick up a lead on Guahai's Yaot fleet. We should find what we are looking for on recently destroyed ships.

<color=#FBB03F>The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.</color>
* Type: Event
* EventId: event_anniversary_2023_t1
* Goals:
	* Task 1: 15 ShipsDestroyedT1_ShipsDestroyedT2_ShipsDestroyedT3_ShipsDestroyedT4

## QE_ANNIVERSARY_2023_DAY03_B_T1
* Name: Day 3: Sifting for Gold
* Description: We are in search of the missing data disk Guahai mentioned in his transmission. We might be able to find it in salvage crates from local outlaws.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
* Type: Event
* EventId: event_anniversary_2023_t1
* Goals:
	* Task 1: GainItem

## QE_ANNIVERSARY_2023_DAY03_C_T1
* Name: Day 3: Concluding Battle
* Description: The data disk gave us a lead on the Progenitor component the Yaot call the Stambah. It seems to be located inside a sector with strong enemy activity.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Type: Event
* EventId: event_anniversary_2023_t1
* Goals:
	* Task 1: Complete side mission

## QE_ANNIVERSARY_2023_DAY04_A_T1
* Name: Day 4: Lost and Found
* Description: Gideon has emerged from his laboratory. He talks of the possibility to build a device that could change the fortunes of Hiigarans in Nimbus. However, we must search for a final component.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
* Type: Event
* EventId: event_anniversary_2023_t1
* Goals:
	* Task 1: Scan

## QE_ANNIVERSARY_2023_DAY04_B_T1
* Name: Day 4: Raw Materials
* Description: Gideon is in need of raw materials to construct his secret device. We have to mine some minerals for him.

<color=#FBB03F>Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
* Type: Event
* EventId: event_anniversary_2023_t1
* Goals:
	* Task 1: GainItem

## QE_ANNIVERSARY_2023_DAY04_C_T1
* Name: Day 4: Patrol Conclusion
* Description: According to Ekekko, the last component on Gideon's list might be in the hands of a powerful enemy. The search for additional information is sending us into the most dangerous areas of this sector.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Type: Event
* EventId: event_anniversary_2023_t1
* Goals:
	* Task 1: Complete side mission

## QE_ANNIVERSARY_2023_DAY05_A_T1
* Name: Day 5: Help Wanted
* Description: We want to make contact with Tepin Papan, commander of the Tanoch Empire. To open up a communication channel, we should do some hired work for the local authorities.

<color=#FBB03F>There are different types of assignments available in your assignment log.</color>
* Type: Event
* EventId: event_anniversary_2023_t1
* Goals:
	* Task 1: 5 T1up

## QE_ANNIVERSARY_2023_DAY05_B_T1
* Name: Day 5: See the Universe
* Description: Tepin Papan has offered to provide information on Gideon's last component if we help him with a security issue he currently faces.

<color=#FBB03F>The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.</color>
* Type: Event
* EventId: event_anniversary_2023_t1
* Goals:
	* Task 1: 15 ShipsDestroyedT1_ShipsDestroyedT2_ShipsDestroyedT3_ShipsDestroyedT4

## QE_ANNIVERSARY_2023_DAY05_C_T1
* Name: Day 5: Enlist Today
* Description: Tepin Papan wants us to retrieve some stolen goods. We should begin salvaging crates in the areas indicated by Tanoch data.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
* Type: Event
* EventId: event_anniversary_2023_t1
* Goals:
	* Task 1: GainItem

## QE_ANNIVERSARY_2023_DAY06_A_T1
* Name: Day 6: Training Day
* Description: While Lazarus Base is processing the reports on the stolen Progenitor component, Gideon wants us to train a crew to handle the device he's constructing.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.</color>
* Type: Event
* EventId: event_anniversary_2023_t1
* Goals:
	* Task 1: GainItem

## QE_ANNIVERSARY_2023_DAY06_B_T1
* Name: Day 6: Technical Proficiency
* Description: With Gideon's new program, we should start training the crew that will man his enigmatic device.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* Type: Event
* EventId: event_anniversary_2023_t1
* Goals:
	* Task 1: UpgradeOfficer

## QE_ANNIVERSARY_2023_DAY06_C_T1
* Name: Day 6: Crash Course
* Description: It is time to put our newly trained crew to the test. We received a task from Lazarus Base to engage a hostile fleet nearby.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Type: Event
* EventId: event_anniversary_2023_t1
* Goals:
	* Task 1: Complete side mission

## QE_ANNIVERSARY_2023_DAY07_A_T1
* Name: Day 7: Simple Collection
* Description: Guhai is a high ranking Yaot official and Lazarus Base has advised us to follow his instructions for now. His first transmitted task needs us to mine resources.

<color=#FBB03F>Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
* Type: Event
* EventId: event_anniversary_2023_t1
* Goals:
	* Task 1: GainItem

## QE_ANNIVERSARY_2023_DAY07_B_T1
* Name: Day 7: Smelting Task
* Description: We continue to follow Guahai’s orders. His next task for us is to produce refined material.

<color=#FBB03F>Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.</color>
* Type: Event
* EventId: event_anniversary_2023_t1
* Goals:
	* Task 1: Craft

## QE_ANNIVERSARY_2023_DAY07_C_T1
* Name: Day 7: Custom Craftsmanship
* Description: Guahai requires us to build specific items for his fleet, as repayment for stealing their cultural item.

<color=#FBB03F>Small items such as strike craft, modules and parts can be built in the fabricator. Larger items such as escort ships and flagships must be constructed at shipyards provided at larger stations.</color>
* Type: Event
* EventId: event_anniversary_2023_t1
* Goals:
	* Task 1: Craft

## QE_ANNIVERSARY_2023_DAY08_A_T1
* Name: Day 8: Cangacian Patrol
* Description: Lazarus Base has informed us that the Tanoch reports on the stolen Progenitor component point towards an infamous pirate group called The Fleet of Rams. We should hunt down Cangacian vessels for more information.

<color=#FBB03F>The Cangacians are pirates that harass trade routes and colonies. We may find them in signals in most areas of the galaxy. They have been sighted raiding mining fleets in asteroid clusters as well.</color>
* Type: Event
* EventId: event_anniversary_2023_t1
* Goals:
	* Task 1: 10 ShipsDestroyedP1T1_ShipsDestroyedP1T2_ShipsDestroyedP1T3_ShipsDestroyedP1T4

## QE_ANNIVERSARY_2023_DAY08_B_T1
* Name: Day 8: Postal Investigation
* Description: The last item Gideon needs to build his device is in the possession of Catequil, Lieutenant of the Fleet of Rams. We have to find communications data from hostile ships to locate his position.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
* Type: Event
* EventId: event_anniversary_2023_t1
* Goals:
	* Task 1: GainItem

## QE_ANNIVERSARY_2023_DAY08_C_T1
* Name: Day 8: Black Flag
* Description: Our engineers were able to triangulate Catequil's transmission. We must chase him down to attain the last Progenitor component for Gideon.

<color=#FBB03F>The Cangacians are pirates that harass trade routes and colonies. We may find them in signals in most areas of the galaxy. They have been sighted raiding mining fleets in asteroid clusters as well.</color>
* Type: Event
* EventId: event_anniversary_2023_t1
* Goals:
	* Task 1: 20 ShipsDestroyedP1T1_ShipsDestroyedP1T2_ShipsDestroyedP1T3_ShipsDestroyedP1T4

## QE_ANNIVERSARY_2023_DAY09_A_T1
* Name: Day 9: Special Instructions
* Description: While Gideon is finalizing the construction of the Progenitor Negotiator, one of our officers must be trained to utilize it in action.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* Type: Event
* EventId: event_anniversary_2023_t1
* Goals:
	* Task 1: UpgradeOfficer

## QE_ANNIVERSARY_2023_DAY09_B_T1
* Name: Day 9: The Chariot
* Description: We have to fabricate several items to modify a common freighter for Gideon's special operation.

<color=#FBB03F>Small items such as strike craft, modules and parts can be built in the fabricator. Larger items such as escort ships and flagships must be constructed at shipyards provided at larger stations.</color>
* Type: Event
* EventId: event_anniversary_2023_t1
* Goals:
	* Task 1: Craft

## QE_ANNIVERSARY_2023_DAY09_C_T1
* Name: Day 9: Trial Runs
* Description: We are instructed to perform one final operations readiness test. All forces must be fully prepared for whatever Gideon is planning.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Type: Event
* EventId: event_anniversary_2023_t1
* Goals:
	* Task 1: Complete side mission

## QE_ANNIVERSARY_2023_DAY10_A_T1
* Name: Day 10: The Special Operation
* Description: Gideon has finally revealed his plan. From the Progenitor components we collected he constructed a communication device to retake control of Wiracoda Gate. We are trying to go home.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Type: Event
* EventId: event_anniversary_2023_t1
* MailsOnCompletion: m_anniversary_enoch_log
* Goals:
	* Task 1: Complete mission 'Return to Wiracoda Gate T1'

## QE_ANNIVERSARY_2023_DAILY_A_T2
* Name: Active Monitoring
* Description: Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
* Type: Event
* EventId: event_anniversary_2023_t2
* Goals:
	* Task 1: Complete 5 side missions

## QE_ANNIVERSARY_2023_DAILY_B_T2
* Name: Refining Results
* Description: Rare earths are an occasional by-product of refining. They are required for upgrading modules.
* Type: Event
* EventId: event_anniversary_2023_t2
* Goals:
	* Task 1: GainItem

## QE_ANNIVERSARY_2023_DAY01_A_T2
* Name: Day 1: Research Directive
* Description: We received priority communication from Hiigaran Command of Lazarus Base concerning Gideon S'jet. We need to decrypt it in our laboratory first before we can read it.

<color=#FBB03F>Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.</color>
* Type: Event
* EventId: event_anniversary_2023_t2
* Goals:
	* Task 1: GainItem

## QE_ANNIVERSARY_2023_DAY01_B_T2
* Name: Day 1: Seek and Find
* Description: The list given to us by Gideon includes many components found only in Progenitor ships. The easiest way to collect them is to harvest them from downed Progenitor units.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
* Type: Event
* EventId: event_anniversary_2023_t2
* Goals:
	* Task 1: 7 ShipsDestroyedProgenitorT2_ShipsDestroyedProgenitorT3_ShipsDestroyedProgenitorT4

## QE_ANNIVERSARY_2023_DAY01_C_T2
* Name: Day 1: The Capstone
* Description: Progenitor Cognition Nodes are a fragile component often found floating in free space near ancient wreckages.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
* Type: Event
* EventId: event_anniversary_2023_t2
* Goals:
	* Task 1: GainItem

## QE_ANNIVERSARY_2023_DAY02_A_T2
* Name: Day 2: Cash Money
* Description: Ekekko can bring us in contact with traders specialized in Progenitor technology. But knowing the Iyatequa, everything has a price. We should mine minerals to recuperate the losses we'll have to pay.

<color=#FBB03F>Type D ore is not abundant enough to form asteroid clusters on its own. Instead, asteroids with D type ore can be found within clusters rich with other types of ore.</color>
* Type: Event
* EventId: event_anniversary_2023_t2
* Goals:
	* Task 1: GainItem

## QE_ANNIVERSARY_2023_DAY02_B_T2
* Name: Day 2: Songs and Tales
* Description: To impress the Iyatequa traders and procure the Progenitor components for Gideon, we will have to work on our reputation among a certain clientele.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Type: Event
* EventId: event_anniversary_2023_t2
* Goals:
	* Task 1: 135 RepTr1

## QE_ANNIVERSARY_2023_DAY02_C_T2
* Name: Day 2: Merchant Supreme
* Description: In order to raise funds to acquire the needed Progenitor components for Gideon, we must sell some of our stored items on the local market.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
* Type: Event
* EventId: event_anniversary_2023_t2
* Goals:
	* Task 1: GainItem

## QE_ANNIVERSARY_2023_DAY03_A_T2
* Name: Day 3: Stop Scouting
* Description: We need to search for recent communications data in this sector to pick up a lead on Guahai's Yaot fleet. We should find what we are looking for on recently destroyed ships.

<color=#FBB03F>The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.</color>
* Type: Event
* EventId: event_anniversary_2023_t2
* Goals:
	* Task 1: 15 ShipsDestroyedT2_ShipsDestroyedT3_ShipsDestroyedT4

## QE_ANNIVERSARY_2023_DAY03_B_T2
* Name: Day 3: Sifting for Gold
* Description: We are in search of the missing data disk Guahai mentioned in his transmission. We might be able to find it in salvage crates from local outlaws.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
* Type: Event
* EventId: event_anniversary_2023_t2
* Goals:
	* Task 1: GainItem

## QE_ANNIVERSARY_2023_DAY03_C_T2
* Name: Day 3: Concluding Battle
* Description: The reconnaissance disk gave us a lead on the Progenitor component the Yaot call the Stambha. Enemy activity is high in the target location.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* Type: Event
* EventId: event_anniversary_2023_t2
* Goals:
	* Task 1: Complete side mission

## QE_ANNIVERSARY_2023_DAY04_A_T2
* Name: Day 4: Lost and Found
* Description: Gideon has emerged from his laboratory. He talks of the possibility to build a device that could change the fortunes of Hiigarans in Nimbus. However, we must search for a final component.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
* Type: Event
* EventId: event_anniversary_2023_t2
* Goals:
	* Task 1: Scan

## QE_ANNIVERSARY_2023_DAY04_B_T2
* Name: Day 4: Raw Materials
* Description: Gideon is in need of raw materials to construct his secret device. We have to mine some minerals for him.

<color=#FBB03F>Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
* Type: Event
* EventId: event_anniversary_2023_t2
* Goals:
	* Task 1: GainItem

## QE_ANNIVERSARY_2023_DAY04_C_T2
* Name: Day 4: Patrol Conclusion
* Description: According to Ekekko, the last component on Gideon's list might be in the hands of a powerful enemy. The search for additional information is sending us into the most dangerous areas of this sector.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Type: Event
* EventId: event_anniversary_2023_t2
* Goals:
	* Task 1: Complete side mission

## QE_ANNIVERSARY_2023_DAY05_A_T2
* Name: Day 5: Help Wanted
* Description: We want to make contact with Tepin Papan, commander of the Tanoch Empire. To find a communication channel, we should do some hired work for the local authorities.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Type: Event
* EventId: event_anniversary_2023_t2
* Goals:
	* Task 1: 5 Faction_T2up

## QE_ANNIVERSARY_2023_DAY05_B_T2
* Name: Day 5: See the Universe
* Description: Tepin Papan has offered to provide information on Gideon's last component if we help him with a security issue he currently faces.

<color=#FBB03F>Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.</color>
* Type: Event
* EventId: event_anniversary_2023_t2
* Goals:
	* Task 1: Complete 3 side missions

## QE_ANNIVERSARY_2023_DAY05_C_T2
* Name: Day 5: Enlist Today
* Description: According to Tepin Papan, some of the Tanoch sectors require assistance. We should seek out their liaison offices and complete assignments.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Type: Event
* EventId: event_anniversary_2023_t2
* Goals:
	* Task 1: 135 RepTanoch

## QE_ANNIVERSARY_2023_DAY06_A_T2
* Name: Day 6: Training Day
* Description: While Lazarus Base is processing the reports on the stolen Progenitor component, Gideon wants us to train a crew to handle the device he's constructing.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.</color>
* Type: Event
* EventId: event_anniversary_2023_t2
* Goals:
	* Task 1: GainItem

## QE_ANNIVERSARY_2023_DAY06_B_T2
* Name: Day 6: Technical Proficiency
* Description: With Gideon's new program, we should start training the crew that will man his enigmatic device.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* Type: Event
* EventId: event_anniversary_2023_t2
* Goals:
	* Task 1: UpgradeOfficer

## QE_ANNIVERSARY_2023_DAY06_C_T2
* Name: Day 6: Crash Course
* Description: It is time to put our newly trained crew to the test. We received a task from Lazarus Base to engage a hostile fleet nearby.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* Type: Event
* EventId: event_anniversary_2023_t2
* Goals:
	* Task 1: Complete side mission

## QE_ANNIVERSARY_2023_DAY07_A_T2
* Name: Day 7: Simple Collection
* Description: Guhai is a high ranking Yaot official and Lazarus Base has advised us to follow his instructions for now. His first transmitted task needs us to mine resources.

<color=#FBB03F>Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
* Type: Event
* EventId: event_anniversary_2023_t2
* Goals:
	* Task 1: GainItem

## QE_ANNIVERSARY_2023_DAY07_B_T2
* Name: Day 7: Smelting Task
* Description: We continue to follow Guahai’s orders. His next task for us is to produce refined material.

<color=#FBB03F>Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.</color>
* Type: Event
* EventId: event_anniversary_2023_t2
* Goals:
	* Task 1: Craft

## QE_ANNIVERSARY_2023_DAY07_C_T2
* Name: Day 7: Custom Craftsmanship
* Description: Guahai requires us to build specific items for his fleet, as repayment for stealing their cultural item.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
* Type: Event
* EventId: event_anniversary_2023_t2
* Goals:
	* Task 1: Craft

## QE_ANNIVERSARY_2023_DAY08_A_T2
* Name: Day 8: Cangacian Patrol
* Description: Lazarus Base has informed us that the Tanoch reports on the stolen Progenitor component point towards an infamous pirate group called The Fleet of Rams. We should hunt down Cangacian vessels for more information.

<color=#FBB03F>The Cangacians are pirates that harass trade routes and colonies. We may find them in signals in most areas of the galaxy. They have been sighted raiding mining fleets in asteroid clusters as well.</color>
* Type: Event
* EventId: event_anniversary_2023_t2
* Goals:
	* Task 1: 10 ShipsDestroyedP1T2_ShipsDestroyedP1T3_ShipsDestroyedP1T4

## QE_ANNIVERSARY_2023_DAY08_B_T2
* Name: Day 8: Postal Investigation
* Description: The last item Gideon needs to build his device is in the possession of Catequil, Lieutenant of the Fleet of Rams. We have to find communications data from hostile ships to locate his position.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
* Type: Event
* EventId: event_anniversary_2023_t2
* Goals:
	* Task 1: GainItem

## QE_ANNIVERSARY_2023_DAY08_C_T2
* Name: Day 8: Black Flag
* Description: Our engineers were able to triangulate Catequil's transmission. We must chase him down to attain the last Progenitor component for Gideon.

<color=#FBB03F>The Cangacians are pirates that harass trade routes and colonies. We may find them in signals in most areas of the galaxy. They have been sighted raiding mining fleets in asteroid clusters as well.</color>
* Type: Event
* EventId: event_anniversary_2023_t2
* Goals:
	* Task 1: 20 ShipsDestroyedP1T2_ShipsDestroyedP1T3_ShipsDestroyedP1T4

## QE_ANNIVERSARY_2023_DAY09_A_T2
* Name: Day 9: Special Instructions
* Description: While Gideon is finalizing the construction of the Progenitor Negotiator, we should increase our fleet's power to protect it in action.

<color=#FBB03F>External modules, such as turrets or sensors, can be upgraded in the External Module screen which will increase their power. Upgrading one level costs credits and RE.</color>
* Type: Event
* EventId: event_anniversary_2023_t2
* Goals:
	* Task 1: Craft

## QE_ANNIVERSARY_2023_DAY09_B_T2
* Name: Day 9: The Chariot
* Description: We have to fabricate several items to modify a common freighter for Gideon's special operation.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
* Type: Event
* EventId: event_anniversary_2023_t2
* Goals:
	* Task 1: Craft

## QE_ANNIVERSARY_2023_DAY09_C_T2
* Name: Day 9: Trial Runs
* Description: We are instructed to perform one final operations readiness test. All forces must be fully prepared for whatever Gideon is planning.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* Type: Event
* EventId: event_anniversary_2023_t2
* Goals:
	* Task 1: Complete side mission

## QE_ANNIVERSARY_2023_DAY10_A_T2
* Name: Day 10: The Special Operation
* Description: Gideon has finally revealed his plan. From the Progenitor components we collected he constructed a communication device to retake control of Wiracoda Gate. We are trying to go home.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Type: Event
* EventId: event_anniversary_2023_t2
* MailsOnCompletion: m_anniversary_enoch_log
* Goals:
	* Task 1: Complete mission 'Return to Wiracoda Gate T2'

## QE_ANNIVERSARY_2023_DAILY_A_T3
* Name: Active Monitoring
* Description: Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
* Type: Event
* EventId: event_anniversary_2023_t3
* Goals:
	* Task 1: Complete 5 side missions

## QE_ANNIVERSARY_2023_DAILY_B_T3
* Name: Refining Results
* Description: Rare earths are an occasional by-product of refining. They are required for upgrading modules.
* Type: Event
* EventId: event_anniversary_2023_t3
* Goals:
	* Task 1: GainItem

## QE_ANNIVERSARY_2023_DAY01_A_T3
* Name: Day 1: Research Directive
* Description: We received priority communication from Hiigaran Command of Lazarus Base concerning Gideon S'jet. We need to decrypt it in our laboratory first before we can read it.

<color=#FBB03F>Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.</color>
* Type: Event
* EventId: event_anniversary_2023_t3
* Goals:
	* Task 1: GainItem

## QE_ANNIVERSARY_2023_DAY01_B_T3
* Name: Day 1: Seek and Find
* Description: The list given to us by Gideon includes many components found only in Progenitor ships. The easiest way to collect them is to harvest them from downed Progenitor units.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
* Type: Event
* EventId: event_anniversary_2023_t3
* Goals:
	* Task 1: 7 ShipsDestroyedProgenitorT3_ShipsDestroyedProgenitorT4

## QE_ANNIVERSARY_2023_DAY01_C_T3
* Name: Day 1: The Capstone
* Description: Progenitor Cognition Nodes are a fragile component often found floating in free space near ancient wreckages.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
* Type: Event
* EventId: event_anniversary_2023_t3
* Goals:
	* Task 1: GainItem

## QE_ANNIVERSARY_2023_DAY02_A_T3
* Name: Day 2: Cash Money
* Description: Ekekko can bring us in contact with traders specialized in Progenitor technology. But knowing the Iyatequa, everything has a price. We should mine minerals to recuperate the losses we'll have to pay.

<color=#FBB03F>Type D ore is not abundant enough to form asteroid clusters on its own. Instead, asteroids with D type ore can be found within clusters rich with other types of ore.</color>
* Type: Event
* EventId: event_anniversary_2023_t3
* Goals:
	* Task 1: GainItem

## QE_ANNIVERSARY_2023_DAY02_B_T3
* Name: Day 2: Songs and Tales
* Description: To impress the Iyatequa traders and procure the Progenitor components for Gideon, we will have to work on our reputation among a certain clientele.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Type: Event
* EventId: event_anniversary_2023_t3
* Goals:
	* Task 1: 180 RepTr1

## QE_ANNIVERSARY_2023_DAY02_C_T3
* Name: Day 2: Merchant Supreme
* Description: In order to raise funds to acquire the needed Progenitor components for Gideon, we must sell some of our stored items on the local market.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
* Type: Event
* EventId: event_anniversary_2023_t3
* Goals:
	* Task 1: GainItem

## QE_ANNIVERSARY_2023_DAY03_A_T3
* Name: Day 3: Stop Scouting
* Description: We need to search for recent communications data in this sector to pick up a lead on Guahai's Yaot fleet. We should find what we are looking for on recently destroyed ships.

<color=#FBB03F>The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.</color>
* Type: Event
* EventId: event_anniversary_2023_t3
* Goals:
	* Task 1: 15 ShipsDestroyedT3_ShipsDestroyedT4

## QE_ANNIVERSARY_2023_DAY03_B_T3
* Name: Day 3: Sifting for Gold
* Description: We are in search of the missing data disk Guahai mentioned in his transmission. We might be able to find it in salvage crates from local outlaws.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
* Type: Event
* EventId: event_anniversary_2023_t3
* Goals:
	* Task 1: GainItem

## QE_ANNIVERSARY_2023_DAY03_C_T3
* Name: Day 3: Concluding Battle
* Description: The reconnaissance disk gave us a lead on the Progenitor component the Yaot call the Stambha. Enemy activity is high in the target location.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* Type: Event
* EventId: event_anniversary_2023_t3
* Goals:
	* Task 1: Complete side mission

## QE_ANNIVERSARY_2023_DAY04_A_T3
* Name: Day 4: Lost and Found
* Description: Gideon has emerged from his laboratory. He talks of the possibility to build a device that could change the fortunes of Hiigarans in Nimbus. However, we must search for a final component.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
* Type: Event
* EventId: event_anniversary_2023_t3
* Goals:
	* Task 1: Scan

## QE_ANNIVERSARY_2023_DAY04_B_T3
* Name: Day 4: Raw Materials
* Description: Gideon is in need of raw materials to construct a secret device. We should look for a jovian planet to collect some gas.

<color=#FBB03F>Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.</color>
* Type: Event
* EventId: event_anniversary_2023_t3
* Goals:
	* Task 1: GainItem

## QE_ANNIVERSARY_2023_DAY04_C_T3
* Name: Day 4: Patrol Conclusion
* Description: According to Ekekko, the last component on Gideon's list might be in the hands of a powerful enemy. The search for additional information is sending us into the most dangerous areas of this sector.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Type: Event
* EventId: event_anniversary_2023_t3
* Goals:
	* Task 1: Complete side mission

## QE_ANNIVERSARY_2023_DAY05_A_T3
* Name: Day 5: Help Wanted
* Description: We want to make contact with Tepin Papan, commander of the Tanoch Empire. To find a communication channel, we should do some hired work for the local authorities.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Type: Event
* EventId: event_anniversary_2023_t3
* Goals:
	* Task 1: 5 Faction_T3up

## QE_ANNIVERSARY_2023_DAY05_B_T3
* Name: Day 5: See the Universe
* Description: Tepin Papan has offered to provide information on Gideon's last component if we help him with a security issue he currently faces.

<color=#FBB03F>Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.</color>
* Type: Event
* EventId: event_anniversary_2023_t3
* Goals:
	* Task 1: Complete 3 side missions

## QE_ANNIVERSARY_2023_DAY05_C_T3
* Name: Day 5: Enlist Today
* Description: According to Tepin Papan, some of the Tanoch sectors require assistance. We should seek out their liaison offices and complete assignments.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Type: Event
* EventId: event_anniversary_2023_t3
* Goals:
	* Task 1: 180 RepTanoch

## QE_ANNIVERSARY_2023_DAY06_A_T3
* Name: Day 6: Training Day
* Description: While Lazarus Base is processing the reports on the stolen Progenitor component, Gideon wants us to train a crew to handle the device he's constructing.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.</color>
* Type: Event
* EventId: event_anniversary_2023_t3
* Goals:
	* Task 1: GainItem

## QE_ANNIVERSARY_2023_DAY06_B_T3
* Name: Day 6: Technical Proficiency
* Description: With Gideon's new program, we should start training the crew that will man his enigmatic device.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* Type: Event
* EventId: event_anniversary_2023_t3
* Goals:
	* Task 1: UpgradeOfficer

## QE_ANNIVERSARY_2023_DAY06_C_T3
* Name: Day 6: Crash Course
* Description: It is time to put our newly trained crew to the test. We received a task from Lazarus Base to engage a hostile fleet nearby.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* Type: Event
* EventId: event_anniversary_2023_t3
* Goals:
	* Task 1: Complete side mission

## QE_ANNIVERSARY_2023_DAY07_A_T3
* Name: Day 7: Simple Collection
* Description: Guhai is a high ranking Yaot official and Lazarus Base has advised us to follow his instructions for now. His first transmitted task needs us to mine resources.

<color=#FBB03F>Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
* Type: Event
* EventId: event_anniversary_2023_t3
* Goals:
	* Task 1: GainItem

## QE_ANNIVERSARY_2023_DAY07_B_T3
* Name: Day 7: Smelting Task
* Description: We continue to follow Guahai’s orders. His next task for us is to produce refined material.

<color=#FBB03F>Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.</color>
* Type: Event
* EventId: event_anniversary_2023_t3
* Goals:
	* Task 1: Craft

## QE_ANNIVERSARY_2023_DAY07_C_T3
* Name: Day 7: Custom Craftsmanship
* Description: Guahai requires us to build specific items for his fleet, as repayment for stealing their cultural item.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
* Type: Event
* EventId: event_anniversary_2023_t3
* Goals:
	* Task 1: Craft

## QE_ANNIVERSARY_2023_DAY08_A_T3
* Name: Day 8: Cangacian Patrol
* Description: Lazarus Base has informed us that the Tanoch reports on the stolen Progenitor component point towards an infamous pirate group called The Fleet of Rams. We should hunt down Cangacian vessels for more information.

<color=#FBB03F>The Cangacians are pirates that harass trade routes and colonies. We may find them in signals in most areas of the galaxy. They have been sighted raiding mining fleets in asteroid clusters as well.</color>
* Type: Event
* EventId: event_anniversary_2023_t3
* Goals:
	* Task 1: 10 ShipsDestroyedP1T3_ShipsDestroyedP1T4

## QE_ANNIVERSARY_2023_DAY08_B_T3
* Name: Day 8: Postal Investigation
* Description: The last item Gideon needs to build his device is in the possession of Catequil, Lieutenant of the Fleet of Rams. We have to find communications data from hostile ships to locate his position.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
* Type: Event
* EventId: event_anniversary_2023_t3
* Goals:
	* Task 1: GainItem

## QE_ANNIVERSARY_2023_DAY08_C_T3
* Name: Day 8: Black Flag
* Description: Our engineers were able to triangulate Catequil's transmission. We must chase him down to attain the last Progenitor component for Gideon.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* Type: Event
* EventId: event_anniversary_2023_t3
* Goals:
	* Task 1: Complete quest 'Pahra's Rock'

## QE_ANNIVERSARY_2023_DAY09_A_T3
* Name: Day 9: Special Instructions
* Description: While Gideon is finalizing the construction of the Progenitor Negotiator, we should increase our fleet's power to protect it in action.

<color=#FBB03F>External modules, such as turrets or sensors, can be upgraded in the External Module screen which will increase their power. Upgrading one level costs credits and RE.</color>
* Type: Event
* EventId: event_anniversary_2023_t3
* Goals:
	* Task 1: Craft

## QE_ANNIVERSARY_2023_DAY09_B_T3
* Name: Day 9: The Chariot
* Description: Before we embark on Gideon's special operation, we should further increase our fleet's power to ensure we are ready for any eventuality.

<color=#FBB03F>Internal Modules can be upgraded in the Internal Module screen which increases their attributes. Upgrading one level costs credits and RE.</color>
* Type: Event
* EventId: event_anniversary_2023_t3
* Goals:
	* Task 1: Craft

## QE_ANNIVERSARY_2023_DAY09_C_T3
* Name: Day 9: Trial Runs
* Description: We are instructed to perform one final operations readiness test. All forces must be fully prepared for whatever Gideon is planning.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* Type: Event
* EventId: event_anniversary_2023_t3
* Goals:
	* Task 1: Complete side mission

## QE_ANNIVERSARY_2023_DAY10_A_T3
* Name: Day 10: The Special Operation
* Description: Gideon has finally revealed his plan. From the Progenitor components we collected he constructed a communication device to retake control of Wiracoda Gate. We are trying to go home.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Type: Event
* EventId: event_anniversary_2023_t3
* MailsOnCompletion: m_anniversary_enoch_log
* Goals:
	* Task 1: Complete mission 'Return to Wiracoda Gate T3'

## QE_ANNIVERSARY_2023_DAILY_A_T4
* Name: Active Monitoring
* Description: Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
* Type: Event
* EventId: event_anniversary_2023_t4
* Goals:
	* Task 1: Complete 5 side missions

## QE_ANNIVERSARY_2023_DAILY_B_T4
* Name: Refining Results
* Description: Rare earths are an occasional by-product of refining. They are required for upgrading modules.
* Type: Event
* EventId: event_anniversary_2023_t4
* Goals:
	* Task 1: GainItem

## QE_ANNIVERSARY_2023_DAY01_A_T4
* Name: Day 1: Research Directive
* Description: We received priority communication from Hiigaran Command of Lazarus Base concerning Gideon S'jet. We need to decrypt it in our laboratory first before we can read it.

<color=#FBB03F>Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.</color>
* Type: Event
* EventId: event_anniversary_2023_t4
* Goals:
	* Task 1: GainItem

## QE_ANNIVERSARY_2023_DAY01_B_T4
* Name: Day 1: Seek and Find
* Description: The list given to us by Gideon includes many components found only in Progenitor ships. The easiest way to collect them is to harvest them from downed Progenitor units.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
* Type: Event
* EventId: event_anniversary_2023_t4
* Goals:
	* Task 1: 7 ShipsDestroyedProgenitorT4

## QE_ANNIVERSARY_2023_DAY01_C_T4
* Name: Day 1: The Capstone
* Description: Progenitor Cognition Nodes are a fragile component often found floating in free space near ancient wreckages.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
* Type: Event
* EventId: event_anniversary_2023_t4
* Goals:
	* Task 1: GainItem

## QE_ANNIVERSARY_2023_DAY02_A_T4
* Name: Day 2: Cash Money
* Description: Ekekko can bring us in contact with traders specialized in Progenitor technology. But knowing the Iyatequa, everything has a price. We should mine minerals to recuperate the losses we'll have to pay.

<color=#FBB03F>Type D ore is not abundant enough to form asteroid clusters on its own. Instead, asteroids with D type ore can be found within clusters rich with other types of ore.</color>
* Type: Event
* EventId: event_anniversary_2023_t4
* Goals:
	* Task 1: GainItem

## QE_ANNIVERSARY_2023_DAY02_B_T4
* Name: Day 2: Songs and Tales
* Description: To impress the Iyatequa traders and procure the Progenitor components for Gideon, we will have to work on our reputation among a certain clientele.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Type: Event
* EventId: event_anniversary_2023_t4
* Goals:
	* Task 1: 225 RepTr1

## QE_ANNIVERSARY_2023_DAY02_C_T4
* Name: Day 2: Merchant Supreme
* Description: In order to raise funds to acquire the needed Progenitor components for Gideon, we must sell some of our stored items on the local market.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
* Type: Event
* EventId: event_anniversary_2023_t4
* Goals:
	* Task 1: GainItem

## QE_ANNIVERSARY_2023_DAY03_A_T4
* Name: Day 3: Stop Scouting
* Description: We need to search for recent communications data in this sector to pick up a lead on Guahai's Yaot fleet. We should find what we are looking for on recently destroyed ships.

<color=#FBB03F>The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.</color>
* Type: Event
* EventId: event_anniversary_2023_t4
* Goals:
	* Task 1: 15 ShipsDestroyedT4

## QE_ANNIVERSARY_2023_DAY03_B_T4
* Name: Day 3: Sifting for Gold
* Description: We are in search of the missing data disk Guahai mentioned in his transmission. We might be able to find it in salvage crates from local outlaws.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
* Type: Event
* EventId: event_anniversary_2023_t4
* Goals:
	* Task 1: GainItem

## QE_ANNIVERSARY_2023_DAY03_C_T4
* Name: Day 3: Concluding Battle
* Description: The reconnaissance disk gave us a lead on the Progenitor component the Yaot call the Stambha. Enemy activity is high in the target location.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* Type: Event
* EventId: event_anniversary_2023_t4
* Goals:
	* Task 1: Complete side mission

## QE_ANNIVERSARY_2023_DAY04_A_T4
* Name: Day 4: Lost and Found
* Description: Gideon has emerged from his laboratory. He talks of the possibility to build a device that could change the fortunes of Hiigarans in Nimbus. However, we must search for a final component.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
* Type: Event
* EventId: event_anniversary_2023_t4
* Goals:
	* Task 1: Scan

## QE_ANNIVERSARY_2023_DAY04_B_T4
* Name: Day 4: Raw Materials
* Description: Gideon is in need of raw materials to construct a secret device. We should look for a jovian planet to collect some gas.

<color=#FBB03F>Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.</color>
* Type: Event
* EventId: event_anniversary_2023_t4
* Goals:
	* Task 1: GainItem

## QE_ANNIVERSARY_2023_DAY04_C_T4
* Name: Day 4: Patrol Conclusion
* Description: According to Ekekko, the last component on Gideon's list might be in the hands of a powerful enemy. The search for additional information is sending us into the most dangerous areas of this sector.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Type: Event
* EventId: event_anniversary_2023_t4
* Goals:
	* Task 1: Complete side mission

## QE_ANNIVERSARY_2023_DAY05_A_T4
* Name: Day 5: Help Wanted
* Description: We want to make contact with Tepin Papan, commander of the Tanoch Empire. To find a communication channel, we should do some hired work for the local authorities.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Type: Event
* EventId: event_anniversary_2023_t4
* Goals:
	* Task 1: 5 Faction_T4up

## QE_ANNIVERSARY_2023_DAY05_B_T4
* Name: Day 5: See the Universe
* Description: Tepin Papan has offered to provide information on Gideon's last component if we help him with a security issue he currently faces.

<color=#FBB03F>Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.</color>
* Type: Event
* EventId: event_anniversary_2023_t4
* Goals:
	* Task 1: Complete 3 side missions

## QE_ANNIVERSARY_2023_DAY05_C_T4
* Name: Day 5: Enlist Today
* Description: According to Tepin Papan, some of the Tanoch sectors require assistance. We should seek out their liaison offices and complete assignments.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Type: Event
* EventId: event_anniversary_2023_t4
* Goals:
	* Task 1: 225 RepTanoch

## QE_ANNIVERSARY_2023_DAY06_A_T4
* Name: Day 6: Training Day
* Description: While Lazarus Base is processing the reports on the stolen Progenitor component, Gideon wants us to train a crew to handle the device he's constructing.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.</color>
* Type: Event
* EventId: event_anniversary_2023_t4
* Goals:
	* Task 1: GainItem

## QE_ANNIVERSARY_2023_DAY06_B_T4
* Name: Day 6: Technical Proficiency
* Description: With Gideon's new program, we should start training the crew that will man his enigmatic device.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* Type: Event
* EventId: event_anniversary_2023_t4
* Goals:
	* Task 1: UpgradeOfficer

## QE_ANNIVERSARY_2023_DAY06_C_T4
* Name: Day 6: Crash Course
* Description: It is time to put our newly trained crew to the test. We received a task from Lazarus Base to engage a hostile fleet nearby.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* Type: Event
* EventId: event_anniversary_2023_t4
* Goals:
	* Task 1: Complete side mission

## QE_ANNIVERSARY_2023_DAY07_A_T4
* Name: Day 7: Simple Collection
* Description: Guhai is a high ranking Yaot official and Lazarus Base has advised us to follow his instructions for now. His first transmitted task needs us to mine resources.

<color=#FBB03F>Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
* Type: Event
* EventId: event_anniversary_2023_t4
* Goals:
	* Task 1: GainItem

## QE_ANNIVERSARY_2023_DAY07_B_T4
* Name: Day 7: Smelting Task
* Description: We continue to follow Guahai’s orders. His next task for us is to produce refined material.

<color=#FBB03F>Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.</color>
* Type: Event
* EventId: event_anniversary_2023_t4
* Goals:
	* Task 1: Craft

## QE_ANNIVERSARY_2023_DAY07_C_T4
* Name: Day 7: Custom Craftsmanship
* Description: Guahai requires us to build specific items for his fleet, as repayment for stealing their cultural item.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
* Type: Event
* EventId: event_anniversary_2023_t4
* Goals:
	* Task 1: Craft

## QE_ANNIVERSARY_2023_DAY08_A_T4
* Name: Day 8: Cangacian Patrol
* Description: Lazarus Base has informed us that the Tanoch reports on the stolen Progenitor component point towards an infamous pirate group called The Fleet of Rams. We should hunt down Cangacian vessels for more information.

<color=#FBB03F>The Cangacians are pirates that harass trade routes and colonies. We may find them in signals in most areas of the galaxy. They have been sighted raiding mining fleets in asteroid clusters as well.</color>
* Type: Event
* EventId: event_anniversary_2023_t4
* Goals:
	* Task 1: 10 ShipsDestroyedP1T4

## QE_ANNIVERSARY_2023_DAY08_B_T4
* Name: Day 8: Postal Investigation
* Description: The last item Gideon needs to build his device is in the possession of Catequil, Lieutenant of the Fleet of Rams. We have to find communications data from hostile ships to locate his position.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
* Type: Event
* EventId: event_anniversary_2023_t4
* Goals:
	* Task 1: GainItem

## QE_ANNIVERSARY_2023_DAY08_C_T4
* Name: Day 8: Black Flag
* Description: Our engineers were able to triangulate Catequil's transmission. We must chase him down to attain the last Progenitor component for Gideon.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* Type: Event
* EventId: event_anniversary_2023_t4
* Goals:
	* Task 1: Complete quest 'Pahra's Rock (Heroic)'

## QE_ANNIVERSARY_2023_DAY09_A_T4
* Name: Day 9: Special Instructions
* Description: While Gideon is finalizing the construction of the Progenitor Negotiator, we should increase our fleet's power to protect it in action.

<color=#FBB03F>External modules, such as turrets or sensors, can be upgraded in the External Module screen which will increase their power. Upgrading one level costs credits and RE.</color>
* Type: Event
* EventId: event_anniversary_2023_t4
* Goals:
	* Task 1: Craft

## QE_ANNIVERSARY_2023_DAY09_B_T4
* Name: Day 9: The Chariot
* Description: Before we embark on Gideon's special operation, we should further increase our fleet's power to ensure we are ready for any eventuality.

<color=#FBB03F>Internal Modules can be upgraded in the Internal Module screen which increases their attributes. Upgrading one level costs credits and RE.</color>
* Type: Event
* EventId: event_anniversary_2023_t4
* Goals:
	* Task 1: Craft

## QE_ANNIVERSARY_2023_DAY09_C_T4
* Name: Day 9: Trial Runs
* Description: We are instructed to perform one final operations readiness test. All forces must be fully prepared for whatever Gideon is planning.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* Type: Event
* EventId: event_anniversary_2023_t4
* Goals:
	* Task 1: Complete side mission

## QE_ANNIVERSARY_2023_DAY10_A_T4
* Name: Day 10: The Special Operation
* Description: Gideon has finally revealed his plan. From the Progenitor components we collected he constructed a communication device to retake control of Wiracoda Gate. We are trying to go home.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Type: Event
* EventId: event_anniversary_2023_t4
* MailsOnCompletion: m_anniversary_enoch_log
* Goals:
	* Task 1: Complete mission 'Return to Wiracoda Gate T4'

## QE_HALLOWEEN_2023_DAILY_A_T1
* Name: Invasion Bystander
* Description: Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
* Type: Event
* EventId: event_halloween_2023_t1
* Goals:
	* Task 1: Complete side mission

## QE_HALLOWEEN_2023_DAILY_B_T1
* Name: Invasion Resister
* Description: Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
* Type: Event
* EventId: event_halloween_2023_t1
* Goals:
	* Task 1: Complete 2 side missions

## QE_HALLOWEEN_2023_DAILY_C_T1
* Name: Invasion Opposition
* Description: Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
* Type: Event
* EventId: event_halloween_2023_t1
* Goals:
	* Task 1: Complete 5 side missions

## QE_HALLOWEEN_2023_DAILY_D_T1
* Name: Invasion Defiant
* Description: Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
* Type: Event
* EventId: event_halloween_2023_t1
* Goals:
	* Task 1: Complete 10 side missions

## QE_HALLOWEEN_2023_DAY01_T1
* Name: Day 1: Sentinel Duty
* Description: We are receiving disturbing reports from all over the galaxy. The disaster at Wiracoda Gate has sent the Progenitors into a frenzy! We must assist the defensive efforts wherever we can until we understand what is happening.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
* Type: Event
* EventId: event_halloween_2023_t1
* Goals:
	* Task 1: 10 ShipsDestroyedProgenitorT1_ShipsDestroyedProgenitorT2_ShipsDestroyedProgenitorT3_ShipsDestroyedProgenitorT4

## QE_HALLOWEEN_2023_DAY02_T1
* Name: Day 2: Prospector
* Description: Refineries are being targeted by the Progenitors in many sectors of Nimbus. Stocks need to be replenished if the defenders are to hold off this calamity.

<color=#FBB03F>Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
* Type: Event
* EventId: event_halloween_2023_t1
* Goals:
	* Task 1: GainItem

## QE_HALLOWEEN_2023_DAY03_T1
* Name: Day 3: Deep Space Recovery
* Description: Gideon wants to collect any evidence which points to the Progenitor’s current activity. We should collect data from ships that were in combat with the abnormal Progenitor vessels.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
* Type: Event
* EventId: event_halloween_2023_t1
* Goals:
	* Task 1: GainItem

## QE_HALLOWEEN_2023_DAY04_T1
* Name: Day 4: Smelt and Refine
* Description: Many planets are still in desperate need of resources to hold off the Progenitors. Especially rare resources have been in high demand to increase defensive capabilities.

<color=#FBB03F>Rare earths are an occasional by-product of refining. They are required for upgrading modules.</color>
* Type: Event
* EventId: event_halloween_2023_t1
* Goals:
	* Task 1: GainItem

## QE_HALLOWEEN_2023_DAY05_T1
* Name: Day 5: The Guidepost
* Description: Gideon has identified a specific Progenitor component we must find in order to decrypt the errant Keeper's command frequency.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
* Type: Event
* EventId: event_halloween_2023_t1
* Goals:
	* Task 1: GainItem

## QE_HALLOWEEN_2023_DAY06_T1
* Name: Day 6: Replacement Parts
* Description: Many sectors have suffered heavy damages from the ongoing Progenitor attacks. More parts are needed to replenish the defending fleets.

<color=#FBB03F>Small items such as strike craft, modules and parts can be built in the fabricator. Larger items such as escort ships and flagships must be constructed at shipyards provided at larger stations.</color>
* Type: Event
* EventId: event_halloween_2023_t1
* Goals:
	* Task 1: Craft

## QE_HALLOWEEN_2023_DAY07_T1
* Name: Day 7: Triangulation
* Description: In order for Gideon to triangulate the location of the errant Keeper we need to hunt down Progenitor vessels receiving its command signal.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
* Type: Event
* EventId: event_halloween_2023_t1
* Goals:
	* Task 1: 10 ShipsDestroyedProgenitorT1_ShipsDestroyedProgenitorT2_ShipsDestroyedProgenitorT3_ShipsDestroyedProgenitorT4

## QE_HALLOWEEN_2023_DAY08_T1
* Name: Day 8: Officer Training
* Description: We are unsure what awaits us when we'll face the corrupted Keeper once again. Gideon has advised us to train our officers in Progenitor communication theory to effectively analyze the situation in the field.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* Type: Event
* EventId: event_halloween_2023_t1
* Goals:
	* Task 1: UpgradeOfficer

## QE_HALLOWEEN_2023_DAY09_T1
* Name: Day 9: Military Exercise
* Description: In order to be fully prepared for the confrontation with the corrupted Keeper, we need to perform a fleet wide ready-check for all systems. We can engage enemies that have been preying on the local area lately due to the diminished security situation.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Type: Event
* EventId: event_halloween_2023_t1
* Goals:
	* Task 1: Complete side mission

## QE_HALLOWEEN_2023_DAY10_T1
* Name: Day 10: Safe Passage
* Description: The Iyatequa promised to negotiate a deal for safe passage into Cangacian space. However, even though the galaxy is at stake, the traders still insist on receiving a hefty price.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
* Type: Event
* EventId: event_halloween_2023_t1
* Goals:
	* Task 1: GainItem

## QE_HALLOWEEN_2023_DAY11_T1
* Name: Day 11: Confrontation
* Description: We must confront the corrupted Keeper Malik and end the Progenitor incursion.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Type: Event
* EventId: event_halloween_2023_t1
* Goals:
	* Task 1: Complete mission 'Rashidun T1'

## QE_HALLOWEEN_2023_DAILY_A_T2
* Name: Invasion Bystander
* Description: Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
* Type: Event
* EventId: event_halloween_2023_t2
* Goals:
	* Task 1: Complete side mission

## QE_HALLOWEEN_2023_DAILY_B_T2
* Name: Invasion Resister
* Description: Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
* Type: Event
* EventId: event_halloween_2023_t2
* Goals:
	* Task 1: Complete 2 side missions

## QE_HALLOWEEN_2023_DAILY_C_T2
* Name: Invasion Opposition
* Description: Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
* Type: Event
* EventId: event_halloween_2023_t2
* Goals:
	* Task 1: Complete 5 side missions

## QE_HALLOWEEN_2023_DAILY_D_T2
* Name: Invasion Defiant
* Description: Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
* Type: Event
* EventId: event_halloween_2023_t2
* Goals:
	* Task 1: Complete 10 side missions

## QE_HALLOWEEN_2023_DAY01_T2
* Name: Day 1: Sentinel Duty
* Description: We are receiving disturbing reports from all over the galaxy. The disaster at Wiracoda Gate has sent the Progenitors into a frenzy! We must assist the defensive efforts wherever we can until we understand what is happening.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
* Type: Event
* EventId: event_halloween_2023_t2
* Goals:
	* Task 1: 10 ShipsDestroyedProgenitorT2_ShipsDestroyedProgenitorT3_ShipsDestroyedProgenitorT4

## QE_HALLOWEEN_2023_DAY02_T2
* Name: Day 2: Prospector
* Description: Refineries are being targeted by the Progenitors in many sectors of Nimbus. Stocks need to be replenished if the defenders are to hold off this calamity.

<color=#FBB03F>Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
* Type: Event
* EventId: event_halloween_2023_t2
* Goals:
	* Task 1: GainItem

## QE_HALLOWEEN_2023_DAY03_T2
* Name: Day 3: Deep Space Recovery
* Description: Gideon wants to collect any evidence which points to the Progenitor’s current activity. We should collect data from ships that were in combat with the abnormal Progenitor vessels.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
* Type: Event
* EventId: event_halloween_2023_t2
* Goals:
	* Task 1: GainItem

## QE_HALLOWEEN_2023_DAY04_T2
* Name: Day 4: Smelt and Refine
* Description: Many planets are still in desperate need of resources to hold off the Progenitors. Especially rare resources have been in high demand to increase defensive capabilities.

<color=#FBB03F>Rare earths are an occasional by-product of refining. They are required for upgrading modules.</color>
* Type: Event
* EventId: event_halloween_2023_t2
* Goals:
	* Task 1: GainItem

## QE_HALLOWEEN_2023_DAY05_T2
* Name: Day 5: The Guidepost
* Description: Gideon has identified a specific Progenitor component we must find in order to decrypt the errant Keeper's command frequency.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
* Type: Event
* EventId: event_halloween_2023_t2
* Goals:
	* Task 1: GainItem

## QE_HALLOWEEN_2023_DAY06_T2
* Name: Day 6: Replacement Parts
* Description: Many sectors have suffered heavy damages from the ongoing Progenitor attacks. More parts are needed to replenish the defending fleets.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
* Type: Event
* EventId: event_halloween_2023_t2
* Goals:
	* Task 1: Craft

## QE_HALLOWEEN_2023_DAY07_T2
* Name: Day 7: Triangulation
* Description: In order for Gideon to triangulate the location of the errant Keeper we need to hunt down Progenitor vessels receiving its command signal.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
* Type: Event
* EventId: event_halloween_2023_t2
* Goals:
	* Task 1: 10 ShipsDestroyedProgenitorT2_ShipsDestroyedProgenitorT3_ShipsDestroyedProgenitorT4

## QE_HALLOWEEN_2023_DAY08_T2
* Name: Day 8: Officer Training
* Description: We are unsure what awaits us when we'll face the corrupted Keeper once again. Gideon has advised us to train our officers in Progenitor communication theory to effectively analyze the situation in the field.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* Type: Event
* EventId: event_halloween_2023_t2
* Goals:
	* Task 1: UpgradeOfficer

## QE_HALLOWEEN_2023_DAY09_T2
* Name: Day 9: Military Exercise
* Description: In order to be fully prepared for the confrontation with the corrupted Keeper, we need to perform a fleet wide ready-check for all systems. We can engage enemies that have been preying on the local area lately due to the diminished security situation.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* Type: Event
* EventId: event_halloween_2023_t2
* Goals:
	* Task 1: Complete side mission

## QE_HALLOWEEN_2023_DAY10_T2
* Name: Day 10: Safe Passage
* Description: The Iyatequa promised to negotiate a deal for safe passage into Cangacian space. However, even though the galaxy is at stake, the traders still insist on receiving a hefty price.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
* Type: Event
* EventId: event_halloween_2023_t2
* Goals:
	* Task 1: GainItem

## QE_HALLOWEEN_2023_DAY11_T2
* Name: Day 11: Confrontation
* Description: We must confront the corrupted Keeper Malik and end the Progenitor incursion.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Type: Event
* EventId: event_halloween_2023_t2
* Goals:
	* Task 1: Complete mission 'Rashidun T2'

## QE_HALLOWEEN_2023_DAILY_A_T3
* Name: Invasion Bystander
* Description: Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
* Type: Event
* EventId: event_halloween_2023_t3
* Goals:
	* Task 1: Complete side mission

## QE_HALLOWEEN_2023_DAILY_B_T3
* Name: Invasion Resister
* Description: Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
* Type: Event
* EventId: event_halloween_2023_t3
* Goals:
	* Task 1: Complete 2 side missions

## QE_HALLOWEEN_2023_DAILY_C_T3
* Name: Invasion Opposition
* Description: Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
* Type: Event
* EventId: event_halloween_2023_t3
* Goals:
	* Task 1: Complete 5 side missions

## QE_HALLOWEEN_2023_DAILY_D_T3
* Name: Invasion Defiant
* Description: Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
* Type: Event
* EventId: event_halloween_2023_t3
* Goals:
	* Task 1: Complete 10 side missions

## QE_HALLOWEEN_2023_DAY01_T3
* Name: Day 1: Sentinel Duty
* Description: We are receiving disturbing reports from all over the galaxy. The disaster at Wiracoda Gate has sent the Progenitors into a frenzy! We must assist the defensive efforts wherever we can until we understand what is happening.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
* Type: Event
* EventId: event_halloween_2023_t3
* Goals:
	* Task 1: 10 ShipsDestroyedProgenitorT3_ShipsDestroyedProgenitorT4

## QE_HALLOWEEN_2023_DAY02_T3
* Name: Day 2: Prospector
* Description: Gas refineries are being targeted by the Progenitors in many sectors of Nimbus. Stocks need to be replenished if the defenders are to hold off this calamity.

<color=#FBB03F>Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.</color>
* Type: Event
* EventId: event_halloween_2023_t3
* Goals:
	* Task 1: GainItem

## QE_HALLOWEEN_2023_DAY03_T3
* Name: Day 3: Deep Space Recovery
* Description: Gideon wants to collect any evidence which points to the Progenitor’s current activity. We should collect data from ships that were in combat with the abnormal Progenitor vessels.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
* Type: Event
* EventId: event_halloween_2023_t3
* Goals:
	* Task 1: GainItem

## QE_HALLOWEEN_2023_DAY04_T3
* Name: Day 4: Smelt and Refine
* Description: Many planets are still in desperate need of resources to hold off the Progenitors. Especially rare resources have been in high demand to increase defensive capabilities.

<color=#FBB03F>Rare earths are an occasional by-product of refining. They are required for upgrading modules.</color>
* Type: Event
* EventId: event_halloween_2023_t3
* Goals:
	* Task 1: GainItem

## QE_HALLOWEEN_2023_DAY05_T3
* Name: Day 5: The Guidepost
* Description: Gideon has identified a specific Progenitor component we must find in order to decrypt the errant Keeper's command frequency.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
* Type: Event
* EventId: event_halloween_2023_t3
* Goals:
	* Task 1: GainItem

## QE_HALLOWEEN_2023_DAY06_T3
* Name: Day 6: Replacement Parts
* Description: Many sectors have suffered heavy damages from the ongoing Progenitor attacks. More parts are needed to replenish the defending fleets.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
* Type: Event
* EventId: event_halloween_2023_t3
* Goals:
	* Task 1: Craft

## QE_HALLOWEEN_2023_DAY07_T3
* Name: Day 7: Triangulation
* Description: In order for Gideon to triangulate the location of the errant Keeper we need to hunt down Progenitor vessels receiving its command signal.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
* Type: Event
* EventId: event_halloween_2023_t3
* Goals:
	* Task 1: 10 ShipsDestroyedProgenitorT3_ShipsDestroyedProgenitorT4

## QE_HALLOWEEN_2023_DAY08_T3
* Name: Day 8: Officer Training
* Description: We are unsure what awaits us when we'll face the corrupted Keeper once again. Gideon has advised us to train our officers in Progenitor communication theory to effectively analyze the situation in the field.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* Type: Event
* EventId: event_halloween_2023_t3
* Goals:
	* Task 1: UpgradeOfficer

## QE_HALLOWEEN_2023_DAY09_T3
* Name: Day 9: Military Exercise
* Description: In order to be fully prepared for the confrontation with the corrupted Keeper, we need to perform a fleet wide ready-check for all systems. We can engage enemies that have been preying on the local area lately due to the diminished security situation.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* Type: Event
* EventId: event_halloween_2023_t3
* Goals:
	* Task 1: Complete 3 side missions

## QE_HALLOWEEN_2023_DAY10_T3
* Name: Day 10: Safe Passage
* Description: The Iyatequa promised to negotiate a deal for safe passage into Cangacian space. However, even though the galaxy is at stake, the traders still insist on receiving a hefty price.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
* Type: Event
* EventId: event_halloween_2023_t3
* Goals:
	* Task 1: GainItem

## QE_HALLOWEEN_2023_DAY11_T3
* Name: Day 11: Confrontation
* Description: We must confront the corrupted Keeper Malik and end the Progenitor incursion.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Type: Event
* EventId: event_halloween_2023_t3
* Goals:
	* Task 1: Complete mission 'Rashidun T3'

## QE_HALLOWEEN_2023_DAILY_A_T4
* Name: Invasion Bystander
* Description: Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
* Type: Event
* EventId: event_halloween_2023_t4
* Goals:
	* Task 1: Complete side mission

## QE_HALLOWEEN_2023_DAILY_B_T4
* Name: Invasion Resister
* Description: Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
* Type: Event
* EventId: event_halloween_2023_t4
* Goals:
	* Task 1: Complete 2 side missions

## QE_HALLOWEEN_2023_DAILY_C_T4
* Name: Invasion Opposition
* Description: Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
* Type: Event
* EventId: event_halloween_2023_t4
* Goals:
	* Task 1: Complete 5 side missions

## QE_HALLOWEEN_2023_DAILY_D_T4
* Name: Invasion Defiant
* Description: Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
* Type: Event
* EventId: event_halloween_2023_t4
* Goals:
	* Task 1: Complete 10 side missions

## QE_HALLOWEEN_2023_DAY01_T4
* Name: Day 1: Sentinel Duty
* Description: We are receiving disturbing reports from all over the galaxy. The disaster at Wiracoda Gate has sent the Progenitors into a frenzy! We must assist the defensive efforts wherever we can until we understand what is happening.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
* Type: Event
* EventId: event_halloween_2023_t4
* Goals:
	* Task 1: 10 ShipsDestroyedProgenitorT4

## QE_HALLOWEEN_2023_DAY02_T4
* Name: Day 2: Prospector
* Description: Gas refineries are being targeted by the Progenitors in many sectors of Nimbus. Stocks need to be replenished if the defenders are to hold off this calamity.

<color=#FBB03F>Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.</color>
* Type: Event
* EventId: event_halloween_2023_t4
* Goals:
	* Task 1: GainItem

## QE_HALLOWEEN_2023_DAY03_T4
* Name: Day 3: Deep Space Recovery
* Description: Gideon wants to collect any evidence which points to the Progenitor’s current activity. We should collect data from ships that were in combat with the abnormal Progenitor vessels.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
* Type: Event
* EventId: event_halloween_2023_t4
* Goals:
	* Task 1: GainItem

## QE_HALLOWEEN_2023_DAY04_T4
* Name: Day 4: Smelt and Refine
* Description: Many planets are still in desperate need of resources to hold off the Progenitors. Especially rare resources have been in high demand to increase defensive capabilities.

<color=#FBB03F>Rare earths are an occasional by-product of refining. They are required for upgrading modules.</color>
* Type: Event
* EventId: event_halloween_2023_t4
* Goals:
	* Task 1: GainItem

## QE_HALLOWEEN_2023_DAY05_T4
* Name: Day 5: The Guidepost
* Description: Gideon has identified a specific Progenitor component we must find in order to decrypt the errant Keeper's command frequency.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
* Type: Event
* EventId: event_halloween_2023_t4
* Goals:
	* Task 1: GainItem

## QE_HALLOWEEN_2023_DAY06_T4
* Name: Day 6: Replacement Parts
* Description: Many sectors have suffered heavy damages from the ongoing Progenitor attacks. More parts are needed to replenish the defending fleets.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
* Type: Event
* EventId: event_halloween_2023_t4
* Goals:
	* Task 1: Craft

## QE_HALLOWEEN_2023_DAY07_T4
* Name: Day 7: Triangulation
* Description: In order for Gideon to triangulate the location of the errant Keeper we need to hunt down Progenitor vessels receiving its command signal.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
* Type: Event
* EventId: event_halloween_2023_t4
* Goals:
	* Task 1: 10 ShipsDestroyedProgenitorT4

## QE_HALLOWEEN_2023_DAY08_T4
* Name: Day 8: Officer Training
* Description: We are unsure what awaits us when we'll face the corrupted Keeper once again. Gideon has advised us to train our officers in Progenitor communication theory to effectively analyze the situation in the field.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* Type: Event
* EventId: event_halloween_2023_t4
* Goals:
	* Task 1: UpgradeOfficer

## QE_HALLOWEEN_2023_DAY09_T4
* Name: Day 9: Military Exercise
* Description: In order to be fully prepared for the confrontation with the corrupted Keeper, we need to perform a fleet wide ready-check for all systems. We can engage enemies that have been preying on the local area lately due to the diminished security situation.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
* Type: Event
* EventId: event_halloween_2023_t4
* Goals:
	* Task 1: Complete 5 side missions

## QE_HALLOWEEN_2023_DAY10_T4
* Name: Day 10: Safe Passage
* Description: The Iyatequa promised to negotiate a deal for safe passage into Cangacian space. However, even though the galaxy is at stake, the traders still insist on receiving a hefty price.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
* Type: Event
* EventId: event_halloween_2023_t4
* Goals:
	* Task 1: GainItem

## QE_HALLOWEEN_2023_DAY11_T4
* Name: Day 11: Confrontation
* Description: We must confront the corrupted Keeper Malik and end the Progenitor incursion.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Type: Event
* EventId: event_halloween_2023_t4
* Goals:
	* Task 1: Complete mission 'Rashidun T4'

## QE_TANWIN_2023_DAILY_A_T1
* Name: An Article of Hope
* Description: The Chicuat collect Progenitor relics for scientific study, rather than venerate them. Their academics would gladly acquire any such objects to advance their knowledge.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t1
* Goals:
	* Task 1: Pay 1 None

## QE_TANWIN_2023_DAILY_B_T1
* Name: A Good Samaritan
* Description: Tasks performed for the Tanoch Empire also assist the Chicuat indirectly. Gaining favor with the Empire can give the Chicuat more leverage in negotiations for aid.

<color=#FBB03F>Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t1
* Goals:
	* Task 1: Complete 5 side missions

## QE_TANWIN_2023_DAILY_C_T1
* Name: Favored Supplier
* Description: The Chicuat are always in need of supplies and equipment to bolster their economy and support their people. Any aid to them would be welcomed.

<color=#FBB03F>Small items such as strike craft, modules and parts can be built in the fabricator. Larger items such as escort ships and flagships must be constructed at shipyards provided at larger stations.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t1
* Goals:
	* Task 1: Craft

## QE_TANWIN_2023_DAILY_D_T1
* Name: Peace Officers
* Description: The conflict between the Chicuat and ethnic Tanoch people goes back centuries. Training our crew about the details of this conflict will help us navigate the inner workings of the Tanoch Empire better.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t1
* Goals:
	* Task 1: UpgradeOfficer

## QE_TANWIN_2023_DAY01_T1
* Name: Day 1: Resource Relief
* Description: We received priority communication from Lazarus Base. A subfaction of the Tanoch, the Chicuat, have made contact with Hiigaran representatives and requested aid. Fleet Command wants us to support the Chicuat and establish friendly ties. Our first task is to provide basic resources.

<color=#FBB03F>Ore can be mined from asteroids in asteroid fields. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t1
* MailsOnCompletion: m_tanWin_2023_d01_log
* Goals:
	* Task 1: GainItem

## QE_TANWIN_2023_DAY02_T1
* Name: Day 2: Processor Surrogate
* Description: The Chicuat infrastructure is badly degraded with age and suffered heavy damage in recent attacks. We're asked to refine materials to support their restoration efforts.

<color=#FBB03F>Rare earths are an occasional by-product of refining. They are required for upgrading modules.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t1
* Goals:
	* Task 1: GainItem

## QE_TANWIN_2023_DAY03_T1
* Name: Day 3: Wayward Cargo
* Description: The Chicuat have informed us several critical supply convoys have gone missing. We should try to retrieve any goods by hunting down local bandits.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t1
* Goals:
	* Task 1: GainItem

## QE_TANWIN_2023_DAY04_T1
* Name: Day 4: Relief Package
* Description: Ekekko, our Iyatequa liaison, has suggested to negotiate a trade deal with his contacts to support the Chicuat's need for basic supplies. We should sell some of our own items to get the traders interested.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t1
* Goals:
	* Task 1: GainItem

## QE_TANWIN_2023_DAY05_T1
* Name: Day 5: Gesture of Aid
* Description: We received emergency communication from the Chicuat Elders. They anticipate a raid on one of their remote trading stations. Toci asks us to take on the defense in order to relieve the weakened and overextended Chicuat forces.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t1
* Goals:
	* Task 1: Complete mission 'Repulse Raid T1'

## QE_TANWIN_2023_DAY06_T1
* Name: Day 6: Imperial Appeal
* Description: We must find out whether the Tecuban really are behind the recent attacks on the Chicuat. Our contact in the Tanoch Empire might be able to provide information. We should do some assignments to show good faith.

<color=#FBB03F>There are different types of assignments available in your assignment log.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t1
* MailsOnCompletion: m_tanWin_2023_d06_log
* Goals:
	* Task 1: 5 T1up

## QE_TANWIN_2023_DAY07_T1
* Name: Day 7: Black Eye
* Description: Lazarus Base has processed Tepin Papan's information. There are reports about the rising influence of an ambitous leader named Heyoka. He is promoting expansionist ideas and has a particular disdain for the Chicuat. We should find out if the name is familiar in the criminal underworld here.

<color=#FBB03F>The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t1
* Goals:
	* Task 1: 15 ShipsDestroyedT1_ShipsDestroyedT2_ShipsDestroyedT3_ShipsDestroyedT4

## QE_TANWIN_2023_DAY08_T1
* Name: Day 8: Catch and Kill
* Description: Our investigations produced evidence for contact between the Tecuban leader Heyoka and high profile criminals. We must hunt down these outlaws to learn more.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t1
* Goals:
	* Task 1: Complete side mission

## QE_TANWIN_2023_DAY09_T1
* Name: Day 9: Raise the Stakes
* Description: The Chicuat Elders have asked us to wait for their intelligence report on possible Tecuban forces within Acatla. In the meanwhile we should strengthen our forces to prepare for battle.

<color=#FBB03F>Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t1
* Goals:
	* Task 1: GainItem

## QE_TANWIN_2023_DAY10_T1
* Name: Day 10: In the Shadows
* Description: Intelligence from the Chicuat points to a Tecuban base operating around an uninhabited planet. We must go there and eliminate this base to stop the raids.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t1
* Goals:
	* Task 1: Complete mission 'Base Busting T1'

## QE_TANWIN_2023_DAY11_T1
* Name: Day 11: Imperial Rumors
* Description: In order to gather information about the Vaygr's activity we must contact Tepin Papan once more. We should do some assignments to compensate him for his assistance.

<color=#FBB03F>There are different types of assignments available in your assignment log.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t1
* MailsOnCompletion: m_tanWin_2023_d11_log
* Goals:
	* Task 1: 5 T1up

## QE_TANWIN_2023_DAY12_T1
* Name: Day 12: Seek and Recover
* Description: While Tepin Papan is trying to gather information about the Vaygr's involvement with the Tecuban, we should scan some systems and see if we can find any clues about their whereabouts.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t1
* Goals:
	* Task 1: Scan

## QE_TANWIN_2023_DAY13_T1
* Name: Day 13: Among the People
* Description: We hope to learn more about the Vaygr's activity from the local people. We should do some good deeds around here to gain their trust.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t1
* Goals:
	* Task 1: GainItem

## QE_TANWIN_2023_DAY14_T1
* Name: Day 14: Active Search
* Description: Some local folks have agreed to provide information that could lead to the Vaygr. However, before they hand it over, they want us help them with a particularly challenging mission.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t1
* Goals:
	* Task 1: Complete side mission

## QE_TANWIN_2023_DAY15_T1
* Name: Day 15: Hunting Party
* Description: We must hunt down a group of thugs that is suspected to be working for the Vaygr.

<color=#FBB03F>The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t1
* Goals:
	* Task 1: 15 ShipsDestroyedT1_ShipsDestroyedT2_ShipsDestroyedT3_ShipsDestroyedT4

## QE_TANWIN_2023_DAY16_T1
* Name: Day 16: Attack the Vaygr
* Description: In our search for the Vaygr involved with the Tecuban, we aquired one of their communication frequencies. If we contact the Vaygr now, we should be able to trace their signal and hyper jump to their exact location.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t1
* Goals:
	* Task 1: Complete mission 'Destination T1'

## QE_TANWIN_2023_DAY17_T1
* Name: Day 17: Polite Inquiries
* Description: There is still no answer from Tepin Papan since we last spoke with him. We should do some more assignments to gain his attention and see if he was able to gather any information about the Vaygr's intentions.

<color=#FBB03F>There are different types of assignments available in your assignment log.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t1
* MailsOnCompletion: m_tanWin_2023_d17_log
* Goals:
	* Task 1: 5 T1up

## QE_TANWIN_2023_DAY18_T1
* Name: Day 18: Purchased Whispers
* Description: Ekekko wants us to trade on the local markets and see if we find someone who's willing to sell information on Jochik Kaan's motives.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t1
* Goals:
	* Task 1: GainItem

## QE_TANWIN_2023_DAY19_T1
* Name: Day 19: Getting There First
* Description: We contacted the Chicuat Elders and told them about Jochik Kaan's possible intention to obtain a particular Progenitor object. They have given us intel about a criminal organization that deals with Progenitor objects within the Tanoch Empire. We should investigate.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t1
* Goals:
	* Task 1: Complete side mission

## QE_TANWIN_2023_DAY20_T1
* Name: Day 20: Providing Protection
* Description: While Gideon S'jet is researching the data set of Progenitor objects, the Chicuat Elders have informed us of a resurgance of Tecuban activity within their territory. We should support the defensive efforts.

<color=#FBB03F>The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t1
* Goals:
	* Task 1: 15 ShipsDestroyedT1_ShipsDestroyedT2_ShipsDestroyedT3_ShipsDestroyedT4

## QE_TANWIN_2023_DAY21_T1
* Name: Day 21: Hunt for Knowledge
* Description: Gideon S'jet's research into the data set of Progenitor objects turned out more difficult than expected. He asked us to support him to accelerate the process.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t1
* Goals:
	* Task 1: 10 ShipsDestroyedProgenitorT1_ShipsDestroyedProgenitorT2_ShipsDestroyedProgenitorT3_ShipsDestroyedProgenitorT4

## QE_TANWIN_2023_DAY22_T1
* Name: Day 22: Showdown at the Academy
* Description: We finally learned Jochik Kaan's intentions. He sparked the flames of war to weaken the Chicuat defenses and steal the Baetyl from Tlapallan Academy, one of their key centers of learning. We must travel there at once, before it is too late.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t1
* MailsOnCompletion: m_tanWin_2023_d22_log
* Goals:
	* Task 1: Complete mission 'Tlapallan Academy T1'

## QE_TANWIN_2023_DAILY_A_T2
* Name: An Article of Hope
* Description: The Chicuat collect Progenitor relics for scientific study, rather than venerate them. Their academics would gladly acquire any such objects to advance their knowledge.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t2
* Goals:
	* Task 1: Pay 1 None

## QE_TANWIN_2023_DAILY_B_T2
* Name: A Good Samaritan
* Description: Tasks performed for the Tanoch Empire also assist the Chicuat indirectly. Gaining favor with the Empire can give them more leverage in negotiations for aid.

<color=#FBB03F>Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t2
* Goals:
	* Task 1: Complete 5 side missions

## QE_TANWIN_2023_DAILY_C_T2
* Name: Favored Supplier
* Description: The Chicuat are always in need of supplies and equipment to bolster their economy and support their people. Any aid to them would be welcomed.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t2
* Goals:
	* Task 1: Craft

## QE_TANWIN_2023_DAILY_D_T2
* Name: Peace Officers
* Description: The conflict between the Chicuat and ethnic Tanoch people goes back centuries. Training our crew about the details of this conflict will help us navigate the inner workings of the Tanoch Empire better.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t2
* Goals:
	* Task 1: UpgradeOfficer

## QE_TANWIN_2023_DAY01_T2
* Name: Day 1: Resource Relief
* Description: We received priority communication from Lazarus Base. A subfaction of the Tanoch, the Chicuat, have made contact with Hiigaran representatives and requested aid. Fleet Command wants us to support the Chicuat and establish friendly ties. Our first task is to provide basic resources.

<color=#FBB03F>Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t2
* MailsOnCompletion: m_tanWin_2023_d01_log
* Goals:
	* Task 1: GainItem

## QE_TANWIN_2023_DAY02_T2
* Name: Day 2: Processor Surrogate
* Description: The Chicuat infrastructure is badly degraded with age and suffered heavy damage in recent attacks. We're asked to refine materials to support their restoration efforts.

<color=#FBB03F>Rare earths are an occasional by-product of refining. They are required for upgrading modules.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t2
* Goals:
	* Task 1: GainItem

## QE_TANWIN_2023_DAY03_T2
* Name: Day 3: Wayward Cargo
* Description: The Chicuat have informed us several critical supply convoys have gone missing. We should try to retrieve any goods by hunting down local bandits.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t2
* Goals:
	* Task 1: GainItem

## QE_TANWIN_2023_DAY04_T2
* Name: Day 4: Relief Package
* Description: Ekekko, our Iyatequa liaison, has suggested to negotiate a trade deal with his contacts to support the Chicuat's need for basic supplies. We should sell some of our own items to get the traders interested.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t2
* Goals:
	* Task 1: GainItem

## QE_TANWIN_2023_DAY05_T2
* Name: Day 5: Gesture of Aid
* Description: We received emergency communication from the Chicuat Elders. They anticipate a raid on one of their remote trading stations. Toci asks us to take on the defense in order to relieve the weakened and overextended Chicuat forces.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t2
* Goals:
	* Task 1: Complete mission 'Repulse Raid T2'

## QE_TANWIN_2023_DAY06_T2
* Name: Day 6: Imperial Appeal
* Description: We must find out whether the Tecuban really are behind the recent attacks on the Chicuat. Our contact in the Tanoch Empire might be able to provide information. We should do some assignments to show good faith.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t2
* MailsOnCompletion: m_tanWin_2023_d06_log
* Goals:
	* Task 1: 5 Faction_Tanoch_T2up

## QE_TANWIN_2023_DAY07_T2
* Name: Day 7: Black Eye
* Description: Lazarus Base has processed Tepin Papan's information. There are reports about the rising influence of an ambitous leader named Heyoka. He is promoting expansionist ideas and has a particular disdain for the Chicuat. We should find out if the name is familiar in the criminal underworld here.

<color=#FBB03F>Some Tanoch fleets have broken away from the Tanoch empire to pursue their own agenda. These renegades can be found in signals, prowling Yaot space to continue ancient feuds.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t2
* Goals:
	* Task 1: 10 ShipsDestroyedTanochT2_ShipsDestroyedTanochT3_ShipsDestroyedTanochT4

## QE_TANWIN_2023_DAY08_T2
* Name: Day 8: Catch and Kill
* Description: Our investigations produced evidence for contact between the Tecuban leader Heyoka and high profile criminals. We must hunt down these outlaws to learn more.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t2
* Goals:
	* Task 1: Complete side mission

## QE_TANWIN_2023_DAY09_T2
* Name: Day 9: Raise the Stakes
* Description: The Chicuat Elders have asked us to wait for their intelligence report on possible Tecuban forces within Acatla. In the meanwhile we should strengthen our forces to prepare for battle.

<color=#FBB03F>External modules, such as turrets or sensors, can be upgraded in the External Module screen which will increase their power. Upgrading one level costs credits and RE.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t2
* Goals:
	* Task 1: Craft

## QE_TANWIN_2023_DAY10_T2
* Name: Day 10: In the Shadows
* Description: Intelligence from the Chicuat points to a Tecuban base operating around an uninhabited planet. We must go there and eliminate this base to stop the raids.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t2
* Goals:
	* Task 1: Complete mission 'Base Busting T2'

## QE_TANWIN_2023_DAY11_T2
* Name: Day 11: Imperial Rumors
* Description: In order to gather information about the Vaygr's activity we must contact Tepin Papan once more. We should do some assignments to compensate him for his assistance.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t2
* MailsOnCompletion: m_tanWin_2023_d11_log
* Goals:
	* Task 1: 135 RepTanoch

## QE_TANWIN_2023_DAY12_T2
* Name: Day 12: Seek and Recover
* Description: While Tepin Papan is trying to gather information about the Vaygr's involvement with the Tecuban, we should scan some systems and see if we can find any clues about their whereabouts.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t2
* Goals:
	* Task 1: Scan

## QE_TANWIN_2023_DAY13_T2
* Name: Day 13: Among the People
* Description: We hope to learn more about the Vaygr's activity from the local people. We should do some good deeds around here to gain their trust.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t2
* Goals:
	* Task 1: GainItem

## QE_TANWIN_2023_DAY14_T2
* Name: Day 14: Active Search
* Description: Some local folks have agreed to provide information that could lead to the Vaygr. However, before they hand it over, they want us help them with a particularly challenging mission.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t2
* Goals:
	* Task 1: Complete side mission

## QE_TANWIN_2023_DAY15_T2
* Name: Day 15: Hunting Party
* Description: We must hunt down a group of thugs that is suspected to be working for the Vaygr.

<color=#FBB03F>Some Tanoch fleets have broken away from the Tanoch empire to pursue their own agenda. These renegades can be found in signals, prowling Yaot space to continue ancient feuds.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t2
* Goals:
	* Task 1: 10 ShipsDestroyedTanochT2_ShipsDestroyedTanochT3_ShipsDestroyedTanochT4

## QE_TANWIN_2023_DAY16_T2
* Name: Day 16: Attack the Vaygr
* Description: In our search for the Vaygr involved with the Tecuban, we aquired one of their communication frequencies. If we contact the Vaygr now, we should be able to trace their signal and hyper jump to their exact location.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t2
* Goals:
	* Task 1: Complete mission 'Destination T2'

## QE_TANWIN_2023_DAY17_T2
* Name: Day 17: Polite Inquiries
* Description: There is still no answer from Tepin Papan since we last spoke with him. We should do some more assignments to gain his attention and see if he was able to gather any information about the Vaygr's intentions.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t2
* MailsOnCompletion: m_tanWin_2023_d17_log
* Goals:
	* Task 1: 5 Faction_Tanoch_T2up

## QE_TANWIN_2023_DAY18_T2
* Name: Day 18: Purchased Whispers
* Description: Ekekko wants us to trade on the local markets and see if we find someone who's willing to sell information on Jochik Kaan's motives.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t2
* Goals:
	* Task 1: GainItem

## QE_TANWIN_2023_DAY19_T2
* Name: Day 19: Getting There First
* Description: We contacted the Chicuat Elders and told them about Jochik Kaan's possible intention to obtain a particular Progenitor object. They have given us intel about a criminal organization that deals with Progenitor objects within the Tanoch Empire. We should investigate.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t2
* Goals:
	* Task 1: Complete side mission

## QE_TANWIN_2023_DAY20_T2
* Name: Day 20: Providing Protection
* Description: While Gideon S'jet is researching the data set of Progenitor objects, the Chicuat Elders have informed us of a resurgance of Tecuban activity within their territory. We should support the defensive efforts.

<color=#FBB03F>Some Tanoch fleets have broken away from the Tanoch empire to pursue their own agenda. These renegades can be found in signals, prowling Yaot space to continue ancient feuds.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t2
* Goals:
	* Task 1: 10 ShipsDestroyedTanochT2_ShipsDestroyedTanochT3_ShipsDestroyedTanochT4

## QE_TANWIN_2023_DAY21_T2
* Name: Day 21: Hunt for Knowledge
* Description: Gideon S'jet's research into the data set of Progenitor objects turned out more difficult than expected. He asked us to support him to accelerate the process.

<color=#FBB03F>Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t2
* Goals:
	* Task 1: GainItem

## QE_TANWIN_2023_DAY22_T2
* Name: Day 22: Showdown at the Academy
* Description: We finally learned Jochik Kaan's intentions. He sparked the flames of war to weaken the Chicuat defenses and steal the Baetyl from Tlapallan Academy, one of their key centers of learning. We must travel there at once, before it is too late.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t2
* MailsOnCompletion: m_tanWin_2023_d22_log
* Goals:
	* Task 1: Complete mission 'Tlapallan Academy T2'

## QE_TANWIN_2023_DAILY_A_T3
* Name: An Article of Hope
* Description: The Chicuat collect Progenitor relics for scientific study, rather than venerate them. Their academics would gladly acquire any such objects to advance their knowledge.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t3
* Goals:
	* Task 1: Pay 1 None

## QE_TANWIN_2023_DAILY_B_T3
* Name: A Good Samaritan
* Description: Tasks performed for the Tanoch Empire also assist the Chicuat indirectly. Gaining favor with the Empire can give them more leverage in negotiations for aid.

<color=#FBB03F>Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t3
* Goals:
	* Task 1: Complete 5 side missions

## QE_TANWIN_2023_DAILY_C_T3
* Name: Favored Supplier
* Description: The Chicuat are always in need of supplies and equipment to bolster their economy and support their people. Any aid to them would be welcomed.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t3
* Goals:
	* Task 1: Craft

## QE_TANWIN_2023_DAILY_D_T3
* Name: Peace Officers
* Description: The conflict between the Chicuat and ethnic Tanoch people goes back centuries. Training our crew about the details of this conflict will help us navigate the inner workings of the Tanoch Empire better.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t3
* Goals:
	* Task 1: UpgradeOfficer

## QE_TANWIN_2023_DAY01_T3
* Name: Day 1: Resource Relief
* Description: We received priority communication from Lazarus Base. A subfaction of the Tanoch, the Chicuat, have made contact with Hiigaran representatives and requested aid. Fleet Command wants us to support the Chicuat and establish friendly ties. Our first task is to provide basic resources.

<color=#FBB03F>Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t3
* MailsOnCompletion: m_tanWin_2023_d01_log
* Goals:
	* Task 1: GainItem

## QE_TANWIN_2023_DAY02_T3
* Name: Day 2: Processor Surrogate
* Description: The Chicuat infrastructure is badly degraded with age and suffered heavy damage in recent attacks. We're asked to refine materials to support their restoration efforts.

<color=#FBB03F>Rare earths are an occasional by-product of refining. They are required for upgrading modules.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t3
* Goals:
	* Task 1: GainItem

## QE_TANWIN_2023_DAY03_T3
* Name: Day 3: Wayward Cargo
* Description: The Chicuat have informed us several critical supply convoys have gone missing. We should try to retrieve any goods by hunting down local bandits.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t3
* Goals:
	* Task 1: GainItem

## QE_TANWIN_2023_DAY04_T3
* Name: Day 4: Relief Package
* Description: Ekekko, our Iyatequa liaison, has suggested to negotiate a trade deal with his contacts to support the Chicuat's need for basic supplies. We should sell some of our own items to get the traders interested.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t3
* Goals:
	* Task 1: GainItem

## QE_TANWIN_2023_DAY05_T3
* Name: Day 5: Gesture of Aid
* Description: We received emergency communication from the Chicuat Elders. They anticipate a raid on one of their remote trading stations. Toci asks us to take on the defense in order to relieve the weakened and overextended Chicuat forces.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t3
* Goals:
	* Task 1: Complete mission 'Repulse Raid T3'

## QE_TANWIN_2023_DAY06_T3
* Name: Day 6: Imperial Appeal
* Description: We must find out whether the Tecuban really are behind the recent attacks on the Chicuat. Our contact in the Tanoch Empire might be able to provide information. We should do some assignments to show good faith.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t3
* MailsOnCompletion: m_tanWin_2023_d06_log
* Goals:
	* Task 1: 5 Faction_Tanoch_T3up

## QE_TANWIN_2023_DAY07_T3
* Name: Day 7: Black Eye
* Description: Lazarus Base has processed Tepin Papan's information. There are reports about the rising influence of an ambitous leader named Heyoka. He is promoting expansionist ideas and has a particular disdain for the Chicuat. We should find out if the name is familiar in the criminal underworld here.

<color=#FBB03F>Some Tanoch fleets have broken away from the Tanoch empire to pursue their own agenda. These renegades can be found in signals, prowling Yaot space to continue ancient feuds.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t3
* Goals:
	* Task 1: 10 ShipsDestroyedTanochT3_ShipsDestroyedTanochT4

## QE_TANWIN_2023_DAY08_T3
* Name: Day 8: Catch and Kill
* Description: Our investigations produced evidence for contact between the Tecuban leader Heyoka and high profile criminals. We must hunt down these outlaws to learn more.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t3
* Goals:
	* Task 1: Complete side mission

## QE_TANWIN_2023_DAY09_T3
* Name: Day 9: Raise the Stakes
* Description: The Chicuat Elders have asked us to wait for their intelligence report on possible Tecuban forces within Acatla. In the meanwhile we should strengthen our forces to prepare for battle.

<color=#FBB03F>External modules, such as turrets or sensors, can be upgraded in the External Module screen which will increase their power. Upgrading one level costs credits and RE.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t3
* Goals:
	* Task 1: Craft

## QE_TANWIN_2023_DAY10_T3
* Name: Day 10: In the Shadows
* Description: Intelligence from the Chicuat points to a Tecuban base operating around an uninhabited planet. We must go there and eliminate this base to stop the raids.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t3
* Goals:
	* Task 1: Complete mission 'Base Busting T3'

## QE_TANWIN_2023_DAY11_T3
* Name: Day 11: Imperial Rumors
* Description: In order to gather information about the Vaygr's activity we must contact Tepin Papan once more. We should do some assignments to compensate him for his assistance.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t3
* MailsOnCompletion: m_tanWin_2023_d11_log
* Goals:
	* Task 1: 180 RepTanoch

## QE_TANWIN_2023_DAY12_T3
* Name: Day 12: Seek and Recover
* Description: While Tepin Papan is trying to gather information about the Vaygr's involvement with the Tecuban, we should scan some systems and see if we can find any clues about their whereabouts.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t3
* Goals:
	* Task 1: Scan

## QE_TANWIN_2023_DAY13_T3
* Name: Day 13: Among the People
* Description: We hope to learn more about the Vaygr's activity from the local people. We should do some good deeds around here to gain their trust.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t3
* Goals:
	* Task 1: GainItem

## QE_TANWIN_2023_DAY14_T3
* Name: Day 14: Active Search
* Description: Some local folks have agreed to provide information that could lead to the Vaygr. However, before they hand it over, they want us help them with a particularly challenging mission.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t3
* Goals:
	* Task 1: Complete side mission

## QE_TANWIN_2023_DAY15_T3
* Name: Day 15: Hunting Party
* Description: We must hunt down a group of thugs that is suspected to be working for the Vaygr.

<color=#FBB03F>Some Tanoch fleets have broken away from the Tanoch empire to pursue their own agenda. These renegades can be found in signals, prowling Yaot space to continue ancient feuds.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t3
* Goals:
	* Task 1: 10 ShipsDestroyedTanochT3_ShipsDestroyedTanochT4

## QE_TANWIN_2023_DAY16_T3
* Name: Day 16: Attack the Vaygr
* Description: In our search for the Vaygr involved with the Tecuban, we aquired one of their communication frequencies. If we contact the Vaygr now, we should be able to trace their signal and hyper jump to their exact location.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t3
* Goals:
	* Task 1: Complete mission 'Destination T3'

## QE_TANWIN_2023_DAY17_T3
* Name: Day 17: Polite Inquiries
* Description: There is still no answer from Tepin Papan since we last spoke with him. We should do some more assignments to gain his attention and see if he was able to gather any information about the Vaygr's intentions.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t3
* MailsOnCompletion: m_tanWin_2023_d17_log
* Goals:
	* Task 1: 5 Faction_Tanoch_T3up

## QE_TANWIN_2023_DAY18_T3
* Name: Day 18: Purchased Whispers
* Description: Ekekko wants us to trade on the local markets and see if we find someone who's willing to sell information on Jochik Kaan's motives.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t3
* Goals:
	* Task 1: GainItem

## QE_TANWIN_2023_DAY19_T3
* Name: Day 19: Getting There First
* Description: We contacted the Chicuat Elders and told them about Jochik Kaan's possible intention to obtain a particular Progenitor object. They have given us intel about a criminal organization that deals with Progenitor objects within the Tanoch Empire. We should investigate.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t3
* Goals:
	* Task 1: Complete side mission

## QE_TANWIN_2023_DAY20_T3
* Name: Day 20: Providing Protection
* Description: While Gideon S'jet is researching the data set of Progenitor objects, the Chicuat Elders have informed us of a resurgance of Tecuban activity within their territory. We should support the defensive efforts.

<color=#FBB03F>Some Tanoch fleets have broken away from the Tanoch empire to pursue their own agenda. These renegades can be found in signals, prowling Yaot space to continue ancient feuds.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t3
* Goals:
	* Task 1: 10 ShipsDestroyedTanochT3_ShipsDestroyedTanochT4

## QE_TANWIN_2023_DAY21_T3
* Name: Day 21: Hunt for Knowledge
* Description: Gideon S'jet's research into the data set of Progenitor objects turned out more difficult than expected. He asked us to support him to accelerate the process.

<color=#FBB03F>Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t3
* Goals:
	* Task 1: GainItem

## QE_TANWIN_2023_DAY22_T3
* Name: Day 22: Showdown at the Academy
* Description: We finally learned Jochik Kaan's intentions. He sparked the flames of war to weaken the Chicuat defenses and steal the Baetyl from Tlapallan Academy, one of their key centers of learning. We must travel there at once, before it is too late.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t3
* MailsOnCompletion: m_tanWin_2023_d22_log
* Goals:
	* Task 1: Complete mission 'Tlapallan Academy T3'

## QE_TANWIN_2023_DAILY_A_T4
* Name: An Article of Hope
* Description: The Chicuat collect Progenitor relics for scientific study, rather than venerate them. Their academics would gladly acquire any such objects to advance their knowledge.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t4
* Goals:
	* Task 1: Pay 1 None

## QE_TANWIN_2023_DAILY_B_T4
* Name: A Good Samaritan
* Description: Tasks performed for the Tanoch Empire also assist the Chicuat indirectly. Gaining favor with the Empire can give them more leverage in negotiations for aid.

<color=#FBB03F>Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t4
* Goals:
	* Task 1: Complete 5 side missions

## QE_TANWIN_2023_DAILY_C_T4
* Name: Favored Supplier
* Description: The Chicuat are always in need of supplies and equipment to bolster their economy and support their people. Any aid to them would be welcomed.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t4
* Goals:
	* Task 1: Craft

## QE_TANWIN_2023_DAILY_D_T4
* Name: Peace Officers
* Description: The conflict between the Chicuat and ethnic Tanoch people goes back centuries. Training our crew about the details of this conflict will help us navigate the inner workings of the Tanoch Empire better.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t4
* Goals:
	* Task 1: UpgradeOfficer

## QE_TANWIN_2023_DAY01_T4
* Name: Day 1: Resource Relief
* Description: We received priority communication from Lazarus Base. A subfaction of the Tanoch, the Chicuat, have made contact with Hiigaran representatives and requested aid. Fleet Command wants us to support the Chicuat and establish friendly ties. Our first task is to provide basic resources.

<color=#FBB03F>Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t4
* MailsOnCompletion: m_tanWin_2023_d01_log
* Goals:
	* Task 1: GainItem

## QE_TANWIN_2023_DAY02_T4
* Name: Day 2: Processor Surrogate
* Description: The Chicuat infrastructure is badly degraded with age and suffered heavy damage in recent attacks. We're asked to refine materials to support their restoration efforts.

<color=#FBB03F>Rare earths are an occasional by-product of refining. They are required for upgrading modules.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t4
* Goals:
	* Task 1: GainItem

## QE_TANWIN_2023_DAY03_T4
* Name: Day 3: Wayward Cargo
* Description: The Chicuat have informed us several critical supply convoys have gone missing. We should try to retrieve any goods by hunting down local bandits.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t4
* Goals:
	* Task 1: GainItem

## QE_TANWIN_2023_DAY04_T4
* Name: Day 4: Relief Package
* Description: Ekekko, our Iyatequa liaison, has suggested to negotiate a trade deal with his contacts to support the Chicuat's need for basic supplies. We should sell some of our own items to get the traders interested.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t4
* Goals:
	* Task 1: GainItem

## QE_TANWIN_2023_DAY05_T4
* Name: Day 5: Gesture of Aid
* Description: We received emergency communication from the Chicuat Elders. They anticipate a raid on one of their remote trading stations. Toci asks us to take on the defense in order to relieve the weakened and overextended Chicuat forces.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t4
* Goals:
	* Task 1: Complete mission 'Repulse Raid T4'

## QE_TANWIN_2023_DAY06_T4
* Name: Day 6: Imperial Appeal
* Description: We must find out whether the Tecuban really are behind the recent attacks on the Chicuat. Our contact in the Tanoch Empire might be able to provide information. We should do some assignments to show good faith.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t4
* MailsOnCompletion: m_tanWin_2023_d06_log
* Goals:
	* Task 1: 5 Faction_Tanoch_T4up

## QE_TANWIN_2023_DAY07_T4
* Name: Day 7: Black Eye
* Description: Lazarus Base has processed Tepin Papan's information. There are reports about the rising influence of an ambitous leader named Heyoka. He is promoting expansionist ideas and has a particular disdain for the Chicuat. We should find out if the name is familiar in the criminal underworld here.

<color=#FBB03F>Some Tanoch fleets have broken away from the Tanoch empire to pursue their own agenda. These renegades can be found in signals, prowling Yaot space to continue ancient feuds.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t4
* Goals:
	* Task 1: 10 ShipsDestroyedTanochT4

## QE_TANWIN_2023_DAY08_T4
* Name: Day 8: Catch and Kill
* Description: Our investigations produced evidence for contact between the Tecuban leader Heyoka and high profile criminals. We must hunt down these outlaws to learn more.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t4
* Goals:
	* Task 1: Complete side mission

## QE_TANWIN_2023_DAY09_T4
* Name: Day 9: Raise the Stakes
* Description: The Chicuat Elders have asked us to wait for their intelligence report on possible Tecuban forces within Acatla. In the meanwhile we should strengthen our forces to prepare for battle.

<color=#FBB03F>External modules, such as turrets or sensors, can be upgraded in the External Module screen which will increase their power. Upgrading one level costs credits and RE.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t4
* Goals:
	* Task 1: Craft

## QE_TANWIN_2023_DAY10_T4
* Name: Day 10: In the Shadows
* Description: Intelligence from the Chicuat points to a Tecuban base operating around an uninhabited planet. We must go there and eliminate this base to stop the raids.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t4
* Goals:
	* Task 1: Complete mission 'Base Busting T4'

## QE_TANWIN_2023_DAY11_T4
* Name: Day 11: Imperial Rumors
* Description: In order to gather information about the Vaygr's activity we must contact Tepin Papan once more. We should do some assignments to compensate him for his assistance.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t4
* MailsOnCompletion: m_tanWin_2023_d11_log
* Goals:
	* Task 1: 225 RepTanoch

## QE_TANWIN_2023_DAY12_T4
* Name: Day 12: Seek and Recover
* Description: While Tepin Papan is trying to gather information about the Vaygr's involvement with the Tecuban, we should scan some systems and see if we can find any clues about their whereabouts.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t4
* Goals:
	* Task 1: Scan

## QE_TANWIN_2023_DAY13_T4
* Name: Day 13: Among the People
* Description: We hope to learn more about the Vaygr's activity from the local people. We should do some good deeds around here to gain their trust.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t4
* Goals:
	* Task 1: GainItem

## QE_TANWIN_2023_DAY14_T4
* Name: Day 14: Active Search
* Description: Some local folks have agreed to provide information that could lead to the Vaygr. However, before they hand it over, they want us help them with a particularly challenging mission.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t4
* Goals:
	* Task 1: Complete side mission

## QE_TANWIN_2023_DAY15_T4
* Name: Day 15: Hunting Party
* Description: We must hunt down a group of thugs that is suspected to be working for the Vaygr.

<color=#FBB03F>Some Tanoch fleets have broken away from the Tanoch empire to pursue their own agenda. These renegades can be found in signals, prowling Yaot space to continue ancient feuds.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t4
* Goals:
	* Task 1: 10 ShipsDestroyedTanochT4

## QE_TANWIN_2023_DAY16_T4
* Name: Day 16: Attack the Vaygr
* Description: In our search for the Vaygr involved with the Tecuban, we aquired one of their communication frequencies. If we contact the Vaygr now, we should be able to trace their signal and hyper jump to their exact location.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t4
* Goals:
	* Task 1: Complete mission 'Destination T4'

## QE_TANWIN_2023_DAY17_T4
* Name: Day 17: Polite Inquiries
* Description: There is still no answer from Tepin Papan since we last spoke with him. We should do some more assignments to gain his attention and see if he was able to gather any information about the Vaygr's intentions.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t4
* MailsOnCompletion: m_tanWin_2023_d17_log
* Goals:
	* Task 1: 5 Faction_Tanoch_T4up

## QE_TANWIN_2023_DAY18_T4
* Name: Day 18: Purchased Whispers
* Description: Ekekko wants us to trade on the local markets and see if we find someone who's willing to sell information on Jochik Kaan's motives.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t4
* Goals:
	* Task 1: GainItem

## QE_TANWIN_2023_DAY19_T4
* Name: Day 19: Getting There First
* Description: We contacted the Chicuat Elders and told them about Jochik Kaan's possible intention to obtain a particular Progenitor object. They have given us intel about a criminal organization that deals with Progenitor objects within the Tanoch Empire. We should investigate.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t4
* Goals:
	* Task 1: Complete side mission

## QE_TANWIN_2023_DAY20_T4
* Name: Day 20: Providing Protection
* Description: While Gideon S'jet is researching the data set of Progenitor objects, the Chicuat Elders have informed us of a resurgance of Tecuban activity within their territory. We should support the defensive efforts.

<color=#FBB03F>Some Tanoch fleets have broken away from the Tanoch empire to pursue their own agenda. These renegades can be found in signals, prowling Yaot space to continue ancient feuds.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t4
* Goals:
	* Task 1: 10 ShipsDestroyedTanochT4

## QE_TANWIN_2023_DAY21_T4
* Name: Day 21: Hunt for Knowledge
* Description: Gideon S'jet's research into the data set of Progenitor objects turned out more difficult than expected. He asked us to support him to accelerate the process.

<color=#FBB03F>Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t4
* Goals:
	* Task 1: GainItem

## QE_TANWIN_2023_DAY22_T4
* Name: Day 22: Showdown at the Academy
* Description: We finally learned Jochik Kaan's intentions. He sparked the flames of war to weaken the Chicuat defenses and steal the Baetyl from Tlapallan Academy, one of their key centers of learning. We must travel there at once, before it is too late.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Type: Event
* EventId: event_tanochWinter_2023_t4
* MailsOnCompletion: m_tanWin_2023_d22_log
* Goals:
	* Task 1: Complete mission 'Tlapallan Academy T4'

## QE_NIMBUSTREASURES_2024_DAILY_A_T1
* Name: Stress Test
* Description: New capacitors were installed in our scanner modules during the last maintenance cycle and must be calibrated. Test them above maximum power.

<color=#FBB03F>Batteries can be used to recharge a scanner or even to overcharge it above 100%. Some rare scannable objects can only be found by overcharged scanners.</color>
* Type: Event
* EventId: event_nimbusTreasures_2024_t1
* Goals:
	* Task 1: ChargeScanner

## QE_NIMBUSTREASURES_2024_DAILY_B_T1
* Name: Performance Test
* Description: New firmware has been installed in our scanner modules. They must complete a routine calibration cycle until they pass inspection.

<color=#FBB03F>Scannable objects, such as finds, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
* Type: Event
* EventId: event_nimbusTreasures_2024_t1
* Goals:
	* Task 1: Scan

## QE_NIMBUSTREASURES_2024_DAILY_C1_T1
* Name: Donate to the Search
* Description: To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
* Type: Event
* EventId: event_nimbusTreasures_2024_t1
* Goals:
	* Task 1: Pay 1 None

## QE_NIMBUSTREASURES_2024_DAILY_C2_T1
* Name: Increasing the Search
* Description: To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
* Type: Event
* EventId: event_nimbusTreasures_2024_t1
* Goals:
	* Task 1: Pay 2 None

## QE_NIMBUSTREASURES_2024_DAILY_C3_T1
* Name: The Search Continues
* Description: To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
* Type: Event
* EventId: event_nimbusTreasures_2024_t1
* Goals:
	* Task 1: Pay 3 None

## QE_NIMBUSTREASURES_2024_DAILY_C4_T1
* Name: Completing the Search
* Description: To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
* Type: Event
* EventId: event_nimbusTreasures_2024_t1
* Goals:
	* Task 1: Pay 4 None

## QE_NIMBUSTREASURES_2024_DAILY_A_T2
* Name: Stress Test
* Description: New capacitors were installed in our scanner modules during the last maintenance cycle and must be calibrated. Test them above maximum power.

<color=#FBB03F>Batteries can be used to recharge a scanner or even to overcharge it above 100%. Some rare scannable objects can only be found by overcharged scanners.</color>
* Type: Event
* EventId: event_nimbusTreasures_2024_t2
* Goals:
	* Task 1: ChargeScanner

## QE_NIMBUSTREASURES_2024_DAILY_B_T2
* Name: Performance Test
* Description: New firmware has been installed in our scanner modules. They must complete a routine calibration cycle until they pass inspection.

<color=#FBB03F>Scannable objects, such as finds, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
* Type: Event
* EventId: event_nimbusTreasures_2024_t2
* Goals:
	* Task 1: Scan

## QE_NIMBUSTREASURES_2024_DAILY_C1_T2
* Name: Donate to the Search
* Description: To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
* Type: Event
* EventId: event_nimbusTreasures_2024_t2
* Goals:
	* Task 1: Pay 1 None

## QE_NIMBUSTREASURES_2024_DAILY_C2_T2
* Name: Increasing the Search
* Description: To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
* Type: Event
* EventId: event_nimbusTreasures_2024_t2
* Goals:
	* Task 1: Pay 2 None

## QE_NIMBUSTREASURES_2024_DAILY_C3_T2
* Name: The Search Continues
* Description: To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
* Type: Event
* EventId: event_nimbusTreasures_2024_t2
* Goals:
	* Task 1: Pay 3 None

## QE_NIMBUSTREASURES_2024_DAILY_C4_T2
* Name: Completing the Search
* Description: To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
* Type: Event
* EventId: event_nimbusTreasures_2024_t2
* Goals:
	* Task 1: Pay 4 None

## QE_NIMBUSTREASURES_2024_DAILY_A_T3
* Name: Stress Test
* Description: New capacitors were installed in our scanner modules during the last maintenance cycle and must be calibrated. Test them above maximum power.

<color=#FBB03F>Batteries can be used to recharge a scanner or even to overcharge it above 100%. Some rare scannable objects can only be found by overcharged scanners.</color>
* Type: Event
* EventId: event_nimbusTreasures_2024_t3
* Goals:
	* Task 1: ChargeScanner

## QE_NIMBUSTREASURES_2024_DAILY_B_T3
* Name: Performance Test
* Description: New firmware has been installed in our scanner modules. They must complete a routine calibration cycle until they pass inspection.

<color=#FBB03F>Scannable objects, such as finds, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
* Type: Event
* EventId: event_nimbusTreasures_2024_t3
* Goals:
	* Task 1: Scan

## QE_NIMBUSTREASURES_2024_DAILY_C1_T3
* Name: Donate to the Search
* Description: To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
* Type: Event
* EventId: event_nimbusTreasures_2024_t3
* Goals:
	* Task 1: Pay 1 None

## QE_NIMBUSTREASURES_2024_DAILY_C2_T3
* Name: Increasing the Search
* Description: To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
* Type: Event
* EventId: event_nimbusTreasures_2024_t3
* Goals:
	* Task 1: Pay 2 None

## QE_NIMBUSTREASURES_2024_DAILY_C3_T3
* Name: The Search Continues
* Description: To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
* Type: Event
* EventId: event_nimbusTreasures_2024_t3
* Goals:
	* Task 1: Pay 3 None

## QE_NIMBUSTREASURES_2024_DAILY_C4_T3
* Name: Completing the Search
* Description: To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
* Type: Event
* EventId: event_nimbusTreasures_2024_t3
* Goals:
	* Task 1: Pay 4 None

## QE_NIMBUSTREASURES_2024_DAILY_A_T4
* Name: Stress Test
* Description: New capacitors were installed in our scanner modules during the last maintenance cycle and must be calibrated. Test them above maximum power.

<color=#FBB03F>Batteries can be used to recharge a scanner or even to overcharge it above 100%. Some rare scannable objects can only be found by overcharged scanners.</color>
* Type: Event
* EventId: event_nimbusTreasures_2024_t4
* Goals:
	* Task 1: ChargeScanner

## QE_NIMBUSTREASURES_2024_DAILY_B_T4
* Name: Performance Test
* Description: New firmware has been installed in our scanner modules. They must complete a routine calibration cycle until they pass inspection.

<color=#FBB03F>Scannable objects, such as finds, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
* Type: Event
* EventId: event_nimbusTreasures_2024_t4
* Goals:
	* Task 1: Scan

## QE_NIMBUSTREASURES_2024_DAILY_C1_T4
* Name: Donate to the Search
* Description: To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
* Type: Event
* EventId: event_nimbusTreasures_2024_t4
* Goals:
	* Task 1: Pay 1 None

## QE_NIMBUSTREASURES_2024_DAILY_C2_T4
* Name: Increasing the Search
* Description: To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
* Type: Event
* EventId: event_nimbusTreasures_2024_t4
* Goals:
	* Task 1: Pay 2 None

## QE_NIMBUSTREASURES_2024_DAILY_C3_T4
* Name: The Search Continues
* Description: To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
* Type: Event
* EventId: event_nimbusTreasures_2024_t4
* Goals:
	* Task 1: Pay 3 None

## QE_NIMBUSTREASURES_2024_DAILY_C4_T4
* Name: Completing the Search
* Description: To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
* Type: Event
* EventId: event_nimbusTreasures_2024_t4
* Goals:
	* Task 1: Pay 4 None

## QE_YAOSPR_2024_DAILY_A_T1
* Name: Running Defense
* Description: The Cangacian pirate bands running in this area are seeking the Yaot conjunction pilgrimage fleet. Attack them to dissuade their scouting efforts.

<color=#FBB03F>The Cangacians are pirates that harass trade routes and colonies. We may find them in signals in most areas of the galaxy. They have been sighted raiding mining fleets in asteroid clusters as well.</color>
* Type: Event
* EventId: event_yaotSpring_2024_t1
* Goals:
	* Task 1: 10 ShipsDestroyedP1T1_ShipsDestroyedP1T2_ShipsDestroyedP1T3_ShipsDestroyedP1T4

## QE_YAOSPR_2024_DAILY_A_T2
* Name: Running Defense
* Description: The Cangacian pirate bands running in this area are seeking the Yaot conjunction pilgrimage fleet. Attack them to dissuade their scouting efforts.

<color=#FBB03F>The Cangacians are pirates that harass trade routes and colonies. We may find them in signals in most areas of the galaxy. They have been sighted raiding mining fleets in asteroid clusters as well.</color>
* Type: Event
* EventId: event_yaotSpring_2024_t2
* Goals:
	* Task 1: 10 ShipsDestroyedP1T2_ShipsDestroyedP1T3_ShipsDestroyedP1T4

## QE_YAOSPR_2024_DAILY_A_T3
* Name: Running Defense
* Description: The Cangacian pirate bands running in this area are seeking the Yaot conjunction pilgrimage fleet. Attack them to dissuade their scouting efforts.

<color=#FBB03F>The Cangacians are pirates that harass trade routes and colonies. We may find them in signals in most areas of the galaxy. They have been sighted raiding mining fleets in asteroid clusters as well.</color>
* Type: Event
* EventId: event_yaotSpring_2024_t3
* Goals:
	* Task 1: 10 ShipsDestroyedP1T3_ShipsDestroyedP1T4

## QE_YAOSPR_2024_DAILY_A_T4
* Name: Running Defense
* Description: The Cangacian pirate bands running in this area are seeking the Yaot conjunction pilgrimage fleet. Attack them to dissuade their scouting efforts.

<color=#FBB03F>The Cangacians are pirates that harass trade routes and colonies. We may find them in signals in most areas of the galaxy. They have been sighted raiding mining fleets in asteroid clusters as well.</color>
* Type: Event
* EventId: event_yaotSpring_2024_t4
* Goals:
	* Task 1: 10 ShipsDestroyedP1T4

## QE_YAOSPR_2024_DAILY_B_T1
* Name: Footprints
* Description: We must learn more about the situation if we're to understand why the Yaot pilgrim fleet is being targeted. Search for any remains that are left in their path of passage.

<color=#FBB03F>Finds must be discovered through scanning. After being analyzed, they can be picked up to collect the reward inside.</color>
* Type: Event
* EventId: event_yaotSpring_2024_t1
* Goals:
	* Task 1: Scan

## QE_YAOSPR_2024_DAILY_B_T2
* Name: Footprints
* Description: We must learn more about the situation if we're to understand why the Yaot pilgrim fleet is being targeted. Search for any remains that are left in their path of passage.

<color=#FBB03F>Finds must be discovered through scanning. After being analyzed, they can be picked up to collect the reward inside.</color>
* Type: Event
* EventId: event_yaotSpring_2024_t2
* Goals:
	* Task 1: Scan

## QE_YAOSPR_2024_DAILY_B_T3
* Name: Footprints
* Description: We must learn more about the situation if we're to understand why the Yaot pilgrim fleet is being targeted. Search for any remains that are left in their path of passage.

<color=#FBB03F>Finds must be discovered through scanning. After being analyzed, they can be picked up to collect the reward inside.</color>
* Type: Event
* EventId: event_yaotSpring_2024_t3
* Goals:
	* Task 1: Scan

## QE_YAOSPR_2024_DAILY_B_T4
* Name: Footprints
* Description: We must learn more about the situation if we're to understand why the Yaot pilgrim fleet is being targeted. Search for any remains that are left in their path of passage.

<color=#FBB03F>Finds must be discovered through scanning. After being analyzed, they can be picked up to collect the reward inside.</color>
* Type: Event
* EventId: event_yaotSpring_2024_t4
* Goals:
	* Task 1: Scan

## QE_YAOSPR_2024_DAILY_C_T1
* Name: Alms for Pilgrims
* Description: The Yaot pilgrimage is far from home and likely out of the supply network from the Yaot fleet. Any aid we can provide them would go a long way in helping them complete their journey.

<color=#FBB03F>Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.</color>
* Type: Event
* EventId: event_yaotSpring_2024_t1
* Goals:
	* Task 1: 
		* Pay 100 RU Type A Refined T1
		* Pay 100 RU Type B Refined T1
		* Pay 100 RU Type C Refined T1

## QE_YAOSPR_2024_DAILY_C_T2
* Name: Alms for Pilgrims
* Description: The Yaot pilgrimage is far from home and likely out of the supply network from the Yaot fleet. Any aid we can provide them would go a long way in helping them complete their journey.

<color=#FBB03F>Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.</color>
* Type: Event
* EventId: event_yaotSpring_2024_t2
* Goals:
	* Task 1: 
		* Pay 100 RU Type A Refined T2
		* Pay 100 RU Type B Refined T2
		* Pay 100 RU Type C Refined T2

## QE_YAOSPR_2024_DAILY_C_T3
* Name: Alms for Pilgrims
* Description: The Yaot pilgrimage is far from home and likely out of the supply network from the Yaot fleet. Any aid we can provide them would go a long way in helping them complete their journey.

<color=#FBB03F>Tokens of the eldest can be found in lost caches within Yaot territory or in Cangacian salvage.</color>
* Type: Event
* EventId: event_yaotSpring_2024_t3
* Goals:
	* Task 1: Pay 1 Token of the Eldest

## QE_YAOSPR_2024_DAILY_C_T4
* Name: Alms for Pilgrims
* Description: The Yaot pilgrimage is far from home and likely out of the supply network from the Yaot fleet. Any aid we can provide them would go a long way in helping them complete their journey.

<color=#FBB03F>Tokens of the eldest can be found in lost caches within Yaot territory or in Cangacian salvage.</color>
* Type: Event
* EventId: event_yaotSpring_2024_t4
* Goals:
	* Task 1: Pay 3 Token of the Eldest

## QE_YAOSPR_2024_DAILY_D_T1
* Name: Eyes to the Heavens
* Description: The Yaot likely do not know this region of space well based on how rarely they're encountered here. Examine the nearby star systems to assist the Yaot pilgrims in navigating the region.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
* Type: Event
* EventId: event_yaotSpring_2024_t1
* Goals:
	* Task 1: Scan

## QE_YAOSPR_2024_DAILY_D_T2
* Name: Eyes to the Heavens
* Description: The Yaot likely do not know this region of space well based on how rarely they're encountered here. Examine the nearby star systems to assist the Yaot pilgrims in navigating the region.

<color=#FBB03F>Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.</color>
* Type: Event
* EventId: event_yaotSpring_2024_t2
* Goals:
	* Task 1: GainItem

## QE_YAOSPR_2024_DAILY_D_T3
* Name: Eyes to the Heavens
* Description: The Yaot likely do not know this region of space well based on how rarely they're encountered here. Examine the nearby star systems to assist the Yaot pilgrims in navigating the region.

<color=#FBB03F>Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.</color>
* Type: Event
* EventId: event_yaotSpring_2024_t3
* Goals:
	* Task 1: GainItem

## QE_YAOSPR_2024_DAILY_D_T4
* Name: Eyes to the Heavens
* Description: The Yaot likely do not know this region of space well based on how rarely they're encountered here. Examine the nearby star systems to assist the Yaot pilgrims in navigating the region.

<color=#FBB03F>Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.</color>
* Type: Event
* EventId: event_yaotSpring_2024_t4
* Goals:
	* Task 1: GainItem

## QE_YAOSPR_2024_DAY01_T1
* Name: Day 1: Harvesting Whispers
* Description: There are rumors circulating in the Empty Quarter about an increase in Cangacian pirate activity. Fleet Command asks us to gather intel from our contacts with the Iyatequa traders. We should gain some favors to bargain for information.

<color=#FBB03F>There are different types of assignments available in your assignment log.</color>
* Type: Event
* EventId: event_yaotSpring_2024_t1
* Goals:
	* Task 1: 5 T1up

## QE_YAOSPR_2024_DAY01_T2
* Name: Day 1: Harvesting Whispers
* Description: There are rumors circulating in the Empty Quarter about an increase in Cangacian pirate activity. Fleet Command asks us to gather intel from our contacts with the Iyatequa traders. We should gain some favors to bargain for information.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Type: Event
* EventId: event_yaotSpring_2024_t2
* Goals:
	* Task 1: 5 Faction_Tr1_T2up

## QE_YAOSPR_2024_DAY01_T3
* Name: Day 1: Harvesting Whispers
* Description: There are rumors circulating in the Empty Quarter about an increase in Cangacian pirate activity. Fleet Command asks us to gather intel from our contacts with the Iyatequa traders. We should gain some favors to bargain for information.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Type: Event
* EventId: event_yaotSpring_2024_t3
* Goals:
	* Task 1: 5 Faction_Tr1_T3up

## QE_YAOSPR_2024_DAY01_T4
* Name: Day 1: Harvesting Whispers
* Description: There are rumors circulating in the Empty Quarter about an increase in Cangacian pirate activity. Fleet Command asks us to gather intel from our contacts with the Iyatequa traders. We should gain some favors to bargain for information.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Type: Event
* EventId: event_yaotSpring_2024_t4
* Goals:
	* Task 1: 5 Faction_Tr1_T4up

## QE_YAOSPR_2024_DAY02_T1
* Name: Day 2: Buying Information
* Description: The Iyatequa traders are involved with pirates attacking Yaot pilgrims in the Empty Quarter. We might get more information through selling equipment and arms on the open market.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
* Type: Event
* EventId: event_yaotSpring_2024_t1
* Goals:
	* Task 1: GainItem

## QE_YAOSPR_2024_DAY02_T2
* Name: Day 2: Buying Information
* Description: The Iyatequa traders are involved with pirates attacking Yaot pilgrims in the Empty Quarter. We might get more information through selling equipment and arms on the open market.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
* Type: Event
* EventId: event_yaotSpring_2024_t2
* Goals:
	* Task 1: GainItem

## QE_YAOSPR_2024_DAY02_T3
* Name: Day 2: Buying Information
* Description: The Iyatequa traders are involved with pirates attacking Yaot pilgrims in the Empty Quarter. We might get more information through selling equipment and arms on the open market.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
* Type: Event
* EventId: event_yaotSpring_2024_t3
* Goals:
	* Task 1: GainItem

## QE_YAOSPR_2024_DAY02_T4
* Name: Day 2: Buying Information
* Description: The Iyatequa traders are involved with pirates attacking Yaot pilgrims in the Empty Quarter. We might get more information through selling equipment and arms on the open market.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
* Type: Event
* EventId: event_yaotSpring_2024_t4
* Goals:
	* Task 1: GainItem

## QE_YAOSPR_2024_DAY03_T1
* Name: Day 3: Remote Observation
* Description: To learn more about the pirate raids, we should get in contact with the Yaot pilgrims. They appear to be hiding after recent attacks. We have no other option than to perform reconnaissance in the nearby systems.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
* Type: Event
* EventId: event_yaotSpring_2024_t1
* Goals:
	* Task 1: Scan

## QE_YAOSPR_2024_DAY03_T2
* Name: Day 3: Remote Observation
* Description: To learn more about the pirate raids, we should get in contact with the Yaot pilgrims. They appear to be hiding after recent attacks. We have no other option than to perform reconnaissance in the nearby systems.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
* Type: Event
* EventId: event_yaotSpring_2024_t2
* Goals:
	* Task 1: Scan

## QE_YAOSPR_2024_DAY03_T3
* Name: Day 3: Remote Observation
* Description: To learn more about the pirate raids, we should get in contact with the Yaot pilgrims. They appear to be hiding after recent attacks. We have no other option than to perform reconnaissance in the nearby systems.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
* Type: Event
* EventId: event_yaotSpring_2024_t3
* Goals:
	* Task 1: Scan

## QE_YAOSPR_2024_DAY03_T4
* Name: Day 3: Remote Observation
* Description: To learn more about the pirate raids, we should get in contact with the Yaot pilgrims. They appear to be hiding after recent attacks. We have no other option than to perform reconnaissance in the nearby systems.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
* Type: Event
* EventId: event_yaotSpring_2024_t4
* Goals:
	* Task 1: Scan

## QE_YAOSPR_2024_DAY04_T1
* Name: Day 4: Hunting for Answers
* Description: In our search for the Yaot pilgrims we have encountered intense pirate activity. We should hunt down some of their ships and see if we can gather any additional clues.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
* Type: Event
* EventId: event_yaotSpring_2024_t1
* Goals:
	* Task 1: GainItem

## QE_YAOSPR_2024_DAY04_T2
* Name: Day 4: Hunting for Answers
* Description: In our search for the Yaot pilgrims we have encountered intense pirate activity. We should hunt down some of their ships and see if we can gather any additional clues.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
* Type: Event
* EventId: event_yaotSpring_2024_t2
* Goals:
	* Task 1: GainItem

## QE_YAOSPR_2024_DAY04_T3
* Name: Day 4: Hunting for Answers
* Description: In our search for the Yaot pilgrims we have encountered intense pirate activity. We should hunt down some of their ships and see if we can gather any additional clues.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
* Type: Event
* EventId: event_yaotSpring_2024_t3
* Goals:
	* Task 1: GainItem

## QE_YAOSPR_2024_DAY04_T4
* Name: Day 4: Hunting for Answers
* Description: In our search for the Yaot pilgrims we have encountered intense pirate activity. We should hunt down some of their ships and see if we can gather any additional clues.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
* Type: Event
* EventId: event_yaotSpring_2024_t4
* Goals:
	* Task 1: GainItem

## QE_YAOSPR_2024_DAY05_T1
* Name: Day 5: Lost Pilgrims
* Description: Some Yaot survivors in our medical ward are ready to be questioned. If we manage to prove our good intentions they might help us find the Yaot pilgrimage.

<color=#FBB03F>Prestige is earned through each player level-up and by completing daily and weekly assignments.</color>
* Type: Event
* EventId: event_yaotSpring_2024_t1
* Goals:
	* Task 1: GainItem

## QE_YAOSPR_2024_DAY05_T2
* Name: Day 5: Lost Pilgrims
* Description: Some Yaot survivors in our medical ward are ready to be questioned. If we manage to prove our good intentions they might help us find the Yaot pilgrimage.

<color=#FBB03F>Prestige is earned through each player level-up and by completing daily and weekly assignments.</color>
* Type: Event
* EventId: event_yaotSpring_2024_t2
* Goals:
	* Task 1: GainItem

## QE_YAOSPR_2024_DAY05_T3
* Name: Day 5: Lost Pilgrims
* Description: Some Yaot survivors in our medical ward are ready to be questioned. If we manage to prove our good intentions they might help us find the Yaot pilgrimage.

<color=#FBB03F>Prestige is earned through each player level-up and by completing daily and weekly assignments.</color>
* Type: Event
* EventId: event_yaotSpring_2024_t3
* Goals:
	* Task 1: GainItem

## QE_YAOSPR_2024_DAY05_T4
* Name: Day 5: Lost Pilgrims
* Description: Some Yaot survivors in our medical ward are ready to be questioned. If we manage to prove our good intentions they might help us find the Yaot pilgrimage.

<color=#FBB03F>Prestige is earned through each player level-up and by completing daily and weekly assignments.</color>
* Type: Event
* EventId: event_yaotSpring_2024_t4
* Goals:
	* Task 1: GainItem

## QE_YAOSPR_2024_DAY06_T1
* Name: Day 6: Parts List
* Description: The Yaot have accepted our offer to support their pilgrimage. Requests have come in from ships needing spares and replacement parts for repairs. If we provide these, we might learn more about why the pirates are after these ships.

<color=#FBB03F>Small items such as strike craft, modules and parts can be built in the fabricator. Larger items such as escort ships and flagships must be constructed at shipyards provided at larger stations.</color>
* Type: Event
* EventId: event_yaotSpring_2024_t1
* Goals:
	* Task 1: Craft

## QE_YAOSPR_2024_DAY06_T2
* Name: Day 6: Parts List
* Description: The Yaot have accepted our offer to support their pilgrimage. Requests have come in from ships needing spares and replacement parts for repairs. If we provide these, we might learn more about why the pirates are after these ships.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
* Type: Event
* EventId: event_yaotSpring_2024_t2
* Goals:
	* Task 1: Craft

## QE_YAOSPR_2024_DAY06_T3
* Name: Day 6: Parts List
* Description: The Yaot have accepted our offer to support their pilgrimage. Requests have come in from ships needing spares and replacement parts for repairs. If we provide these, we might learn more about why the pirates are after these ships.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
* Type: Event
* EventId: event_yaotSpring_2024_t3
* Goals:
	* Task 1: Craft

## QE_YAOSPR_2024_DAY06_T4
* Name: Day 6: Parts List
* Description: The Yaot have accepted our offer to support their pilgrimage. Requests have come in from ships needing spares and replacement parts for repairs. If we provide these, we might learn more about why the pirates are after these ships.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
* Type: Event
* EventId: event_yaotSpring_2024_t4
* Goals:
	* Task 1: Craft

## QE_YAOSPR_2024_DAY07_T1
* Name: Day 7: Clearing the Way
* Description: Even though pirates are still swarming the area, Chocoan and the Yaot pilgrims are adamant about continuing their travels to see the astral conjunction events. In order to deter any further attacks on the civilian ships, we should patrol and clear the systems of any significant hostile forces.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Type: Event
* EventId: event_yaotSpring_2024_t1
* Goals:
	* Task 1: Complete side mission

## QE_YAOSPR_2024_DAY07_T2
* Name: Day 7: Clearing the Way
* Description: Even though pirates are still swarming the area, Chocoan and the Yaot pilgrims are adamant about continuing their travels to see the astral conjunction events. In order to deter any further attacks on the civilian ships, we should patrol and clear the systems of any significant hostile forces.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Type: Event
* EventId: event_yaotSpring_2024_t2
* Goals:
	* Task 1: Complete side mission

## QE_YAOSPR_2024_DAY07_T3
* Name: Day 7: Clearing the Way
* Description: Even though pirates are still swarming the area, Chocoan and the Yaot pilgrims are adamant about continuing their travels to see the astral conjunction events. In order to deter any further attacks on the civilian ships, we should patrol and clear the systems of any significant hostile forces.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Type: Event
* EventId: event_yaotSpring_2024_t3
* Goals:
	* Task 1: Complete side mission

## QE_YAOSPR_2024_DAY07_T4
* Name: Day 7: Clearing the Way
* Description: Even though pirates are still swarming the area, Chocoan and the Yaot pilgrims are adamant about continuing their travels to see the astral conjunction events. In order to deter any further attacks on the civilian ships, we should patrol and clear the systems of any significant hostile forces.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Type: Event
* EventId: event_yaotSpring_2024_t4
* Goals:
	* Task 1: Complete side mission

## QE_YAOSPR_2024_DAY08_T1
* Name: Day 8: Knowledge Attained
* Description: Even the Fleet of Rams are after the Yaot pilgrim's supposed treasure. If we hope to protect them, we must first convince somebody to give us more information. We should try to make friends with the pilgrims and get somebody to talk.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from dismissing officers and are earned through completing signals.</color>
* Type: Event
* EventId: event_yaotSpring_2024_t1
* Goals:
	* Task 1: GainItem

## QE_YAOSPR_2024_DAY08_T2
* Name: Day 8: Knowledge Attained
* Description: Even the Fleet of Rams are after the Yaot pilgrim's supposed treasure. If we hope to protect them, we must first convince somebody to give us more information. We should try to make friends with the pilgrims and get somebody to talk.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from dismissing officers and are earned through completing signals.</color>
* Type: Event
* EventId: event_yaotSpring_2024_t2
* Goals:
	* Task 1: GainItem

## QE_YAOSPR_2024_DAY08_T3
* Name: Day 8: Knowledge Attained
* Description: Even the Fleet of Rams are after the Yaot pilgrim's supposed treasure. If we hope to protect them, we must first convince somebody to give us more information. We should try to make friends with the pilgrims and get somebody to talk.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from dismissing officers and are earned through completing signals.</color>
* Type: Event
* EventId: event_yaotSpring_2024_t3
* Goals:
	* Task 1: GainItem

## QE_YAOSPR_2024_DAY08_T4
* Name: Day 8: Knowledge Attained
* Description: Even the Fleet of Rams are after the Yaot pilgrim's supposed treasure. If we hope to protect them, we must first convince somebody to give us more information. We should try to make friends with the pilgrims and get somebody to talk.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from dismissing officers and are earned through completing signals.</color>
* Type: Event
* EventId: event_yaotSpring_2024_t4
* Goals:
	* Task 1: GainItem

## QE_YAOSPR_2024_DAY09_T1
* Name: Day 9: Polite Inquires
* Description: After talking to Chocoan, we suspect there is more to the Yaot pilgrimage than the religious travels to astral conjunction events. We might be able to get more information from the Yaot Federation if we do some favors.

<color=#FBB03F>There are different types of assignments available in your assignment log.</color>
* Type: Event
* EventId: event_yaotSpring_2024_t1
* Goals:
	* Task 1: 5 T1up

## QE_YAOSPR_2024_DAY09_T2
* Name: Day 9: Polite Inquires
* Description: After talking to Chocoan we suspect there is more to the Yaot pilgrimage than the religious travels to astral conjunction events. We might be able to get more information from the Yaot Federation if we do some favors.

<color=#FBB03F>There are different types of assignments available in your assignment log.</color>
* Type: Event
* EventId: event_yaotSpring_2024_t2
* Goals:
	* Task 1: 5 T2up

## QE_YAOSPR_2024_DAY09_T3
* Name: Day 9: Polite Inquires
* Description: After talking to Chocoan we suspect there is more to the Yaot pilgrimage than the religious travels to astral conjunction events. We might be able to get more information from the Yaot Federation if we do some favors.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Type: Event
* EventId: event_yaotSpring_2024_t3
* Goals:
	* Task 1: 5 Faction_Yaot_T3up

## QE_YAOSPR_2024_DAY09_T4
* Name: Day 9: Polite Inquires
* Description: After talking to Chocoan we suspect there is more to the Yaot pilgrimage than the religious travels to astral conjunction events. We might be able to get more information from the Yaot Federation if we do some favors.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
* Type: Event
* EventId: event_yaotSpring_2024_t4
* Goals:
	* Task 1: 5 Faction_Yaot_T4up

## QE_YAOSPR_2024_DAY10_T1
* Name: Day 10: Gift for Gab
* Description: We’ve reached a dead end on collecting intelligence on the Yaot, but our source within the Tanoch Empire has offered to provide more information. We should bring an adequate gift for compensation.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
* Type: Event
* EventId: event_yaotSpring_2024_t1
* Goals:
	* Task 1: Pay 1 None

## QE_YAOSPR_2024_DAY10_T2
* Name: Day 10: Gift for Gab
* Description: We’ve reached a dead end on collecting intelligence on the Yaot, but our source within the Tanoch Empire has offered to provide more information. We should bring an adequate gift for compensation.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
* Type: Event
* EventId: event_yaotSpring_2024_t2
* Goals:
	* Task 1: Pay 1 None

## QE_YAOSPR_2024_DAY10_T3
* Name: Day 10: Gift for Gab
* Description: We’ve reached a dead end on collecting intelligence on the Yaot, but our source within the Tanoch Empire has offered to provide more information. We should bring an adequate gift for compensation.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
* Type: Event
* EventId: event_yaotSpring_2024_t3
* Goals:
	* Task 1: Pay 1 None

## QE_YAOSPR_2024_DAY10_T4
* Name: Day 10: Gift for Gab
* Description: We’ve reached a dead end on collecting intelligence on the Yaot, but our source within the Tanoch Empire has offered to provide more information. We should bring an adequate gift for compensation.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
* Type: Event
* EventId: event_yaotSpring_2024_t4
* Goals:
	* Task 1: Pay 1 None

## QE_YAOSPR_2024_DAY11_T1
* Name: Day 11: Advanced Scouting
* Description: While we still don't know what kind of treasure the pilgrims could have aboard their vessels, Chocoan wants to move on to another astral conjunction event. He has requested our assistance in clearing out the area from any hostile threats.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Type: Event
* EventId: event_yaotSpring_2024_t1
* Goals:
	* Task 1: Complete side mission

## QE_YAOSPR_2024_DAY11_T2
* Name: Day 11: Advanced Scouting
* Description: While we still don't know what kind of treasure the pilgrims could have aboard their vessels, Chocoan wants to move on to another astral conjunction event. He has requested our assistance in clearing out the area from any hostile threats.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Type: Event
* EventId: event_yaotSpring_2024_t2
* Goals:
	* Task 1: Complete side mission

## QE_YAOSPR_2024_DAY11_T3
* Name: Day 11: Advanced Scouting
* Description: While we still don't know what kind of treasure the pilgrims could have aboard their vessels, Chocoan wants to move on to another astral conjunction event. He has requested our assistance in clearing out the area from any hostile threats.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Type: Event
* EventId: event_yaotSpring_2024_t3
* Goals:
	* Task 1: Complete side mission

## QE_YAOSPR_2024_DAY11_T4
* Name: Day 11: Advanced Scouting
* Description: While we still don't know what kind of treasure the pilgrims could have aboard their vessels, Chocoan wants to move on to another astral conjunction event. He has requested our assistance in clearing out the area from any hostile threats.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
* Type: Event
* EventId: event_yaotSpring_2024_t4
* Goals:
	* Task 1: Complete side mission

## QE_YAOSPR_2024_DAY12_T1
* Name: Day 12: Unearthing Secrets
* Description: The report on the pilgrim's procedure has been fully analyzed. Usually the pilgrim's convoy moves in a tight line formation towards the optimal conjunction points where they perform their religious rituals. However, a few ships regularly diverge from the common path and move into nearby asteroid fields. We should investigate the latest conjunction site and see if we can find anything of interest.

<color=#FBB03F>Ore can be mined from asteroids in asteroid fields. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
* Type: Event
* EventId: event_yaotSpring_2024_t1
* Goals:
	* Task 1: GainItem

## QE_YAOSPR_2024_DAY12_T2
* Name: Day 12: Unearthing Secrets
* Description: The report on the pilgrim's procedure has been fully analyzed. Usually the pilgrim's convoy moves in a tight line formation towards the optimal conjunction points where they perform their religious rituals. However, a few ships regularly diverge from the common path and move into nearby asteroid fields. We should investigate the latest conjunction site and see if we can find anything of interest.

<color=#FBB03F>Ore can be mined from asteroids in asteroid fields. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
* Type: Event
* EventId: event_yaotSpring_2024_t2
* Goals:
	* Task 1: GainItem

## QE_YAOSPR_2024_DAY12_T3
* Name: Day 12: Unearthing Secrets
* Description: The report on the pilgrim's procedure has been fully analyzed. Usually the pilgrim's convoy moves in a tight line formation towards the optimal conjunction points where they perform their religious rituals. However, a few ships regularly diverge from the common path and move into nearby asteroid fields. We should investigate the latest conjunction site and see if we can find anything of interest.

<color=#FBB03F>Ore can be mined from asteroids in asteroid fields. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
* Type: Event
* EventId: event_yaotSpring_2024_t3
* Goals:
	* Task 1: GainItem

## QE_YAOSPR_2024_DAY12_T4
* Name: Day 12: Unearthing Secrets
* Description: The report on the pilgrim's procedure has been fully analyzed. Usually the pilgrim's convoy moves in a tight line formation towards the optimal conjunction points where they perform their religious rituals. However, a few ships regularly diverge from the common path and move into nearby asteroid fields. We should investigate the latest conjunction site and see if we can find anything of interest.

<color=#FBB03F>Ore can be mined from asteroids in asteroid fields. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
* Type: Event
* EventId: event_yaotSpring_2024_t4
* Goals:
	* Task 1: GainItem

## QE_YAOSPR_2024_DAY13_T1
* Name: Day 13: The Precession
* Description: Chocoan has informed us that the next astral conjunction site will be inside the Cangacian territories. We convinced him to take part in the operation ourselves to ensure security in this hostile area of the Empty Quarter. Maybe we will be able to both protect the pilgrims and find out more about the suspected secret agenda. We should make sure the crew is properly prepared and ready for any eventualities.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* Type: Event
* EventId: event_yaotSpring_2024_t1
* Goals:
	* Task 1: UpgradeOfficer

## QE_YAOSPR_2024_DAY13_T2
* Name: Day 13: The Precession
* Description: Chocoan has informed us that the next astral conjunction site will be inside the Cangacian territories. We convinced him to take part in the operation ourselves to ensure security in this hostile area of the Empty Quarter. Maybe we will be able to both protect the pilgrims and find out more about the suspected secret agenda. We should make sure the crew is properly prepared and ready for any eventualities.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* Type: Event
* EventId: event_yaotSpring_2024_t2
* Goals:
	* Task 1: UpgradeOfficer

## QE_YAOSPR_2024_DAY13_T3
* Name: Day 13: The Precession
* Description: Chocoan has informed us that the next astral conjunction site will be inside the Cangacian territories. We convinced him to take part in the operation ourselves to ensure security in this hostile area of the Empty Quarter. Maybe we will be able to both protect the pilgrims and find out more about the suspected secret agenda. We should make sure the crew is properly prepared and ready for any eventualities.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* Type: Event
* EventId: event_yaotSpring_2024_t3
* Goals:
	* Task 1: UpgradeOfficer

## QE_YAOSPR_2024_DAY13_T4
* Name: Day 13: The Precession
* Description: Chocoan has informed us that the next astral conjunction site will be inside the Cangacian territories. We convinced him to take part in the operation ourselves to ensure security in this hostile area of the Empty Quarter. Maybe we will be able to both protect the pilgrims and find out more about the suspected secret agenda. We should make sure the crew is properly prepared and ready for any eventualities.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
* Type: Event
* EventId: event_yaotSpring_2024_t4
* Goals:
	* Task 1: UpgradeOfficer

## QE_YAOSPR_2024_DAY14_T1
* Name: Day 14: The Promised Place
* Description: Chocoan has provided the coordinates to the next astral conjunction event. Strong hostile forces are to be expected in this system. Our goal is to both protect the civilian pilgrims and find out more about the suspected secret agenda of the Yaot Elders.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Type: Event
* EventId: event_yaotSpring_2024_t1
* Goals:
	* Task 1: Complete mission 'Conjunction T1'

## QE_YAOSPR_2024_DAY14_T2
* Name: Day 14: The Promised Place
* Description: Chocoan has provided the coordinates to the next astral conjunction event. Strong hostile forces are to be expected in this system. Our goal is to both protect the civilian pilgrims and find out more about the suspected secret agenda of the Yaot Elders.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Type: Event
* EventId: event_yaotSpring_2024_t2
* Goals:
	* Task 1: Complete mission 'Conjunction T2'

## QE_YAOSPR_2024_DAY14_T3
* Name: Day 14: The Promised Place
* Description: Chocoan has provided the coordinates to the next astral conjunction event. Strong hostile forces are to be expected in this system. Our goal is to both protect the civilian pilgrims and find out more about the suspected secret agenda of the Yaot Elders.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Type: Event
* EventId: event_yaotSpring_2024_t3
* Goals:
	* Task 1: Complete mission 'Conjunction T3'

## QE_YAOSPR_2024_DAY14_T4
* Name: Day 14: The Promised Place
* Description: Chocoan has provided the coordinates to the next astral conjunction event. Strong hostile forces are to be expected in this system. Our goal is to both protect the civilian pilgrims and find out more about the suspected secret agenda of the Yaot Elders.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
* Type: Event
* EventId: event_yaotSpring_2024_t4
* Goals:
	* Task 1: Complete mission 'Conjunction T4'

## QT_001
* Name: No header for quest qt_001
* Description: No description for quest qt_001

* Type: Side
* MailsOnCompletion: m_qt_001
* Goals:
	* Task 1: 
		* Pay 500 RU Type A Ore T1
		* Pay 250 RU Type B Ore T1

## QT_002
* Name: No header for quest qt_002
* Description: No description for quest qt_002

* Type: Side
* Goals:
	* Task 1: Complete missions:
		* 'Wiracoda Gate'
		* 'Gulf Taln'

## QT_003
* Name: No header for quest qt_003
* Description: No description for quest qt_003

* Type: Side
* Goals:
	* Task 1: GainItem

## QT_004
* Name: No header for quest qt_004
* Description: No description for quest qt_004

* Type: Side
* Goals:
	* Task 1: Complete 3 side missions

## QM_TESTQUESTDIALOG
* Name: No header for quest qm_testQuestDialog
* Description: No description for quest qm_testQuestDialog

* Type: Main
* Goals:
	* Task 1: Goto ROA TISAAD system of Hiigaran Medea's territories
	* Task 2: Goto SAARET system of Hiigaran Medea's territories
	* Task 3: 
		* Goto ROA TISAAD system of Hiigaran Medea's territories
		* Goto SAARET system of Hiigaran Medea's territories

## QT_TESTDISMISSOFFICERS
* Name: No header for quest qt_testDismissOfficers
* Description: No description for quest qt_testDismissOfficers

* Type: Side
* Goals:
	* Task 1: GainItem

## QT_TEST_STRIKE_13
* Name: No header for quest qt_test_strike_13
* Description: No description for quest qt_test_strike_13

* Type: Main
* Goals:
	* Task 1: Complete quest 'Pirate Hideout'

## QT_TEST_STRIKE_16
* Name: No header for quest qt_test_strike_16
* Description: No description for quest qt_test_strike_16

* Type: Main
* Goals:
	* Task 1: Complete quest 'Pirate Hideout (Heroic)'

## QT_TEST_STRIKE_14
* Name: No header for quest qt_test_strike_14
* Description: No description for quest qt_test_strike_14

* Type: Main
* Goals:
	* Task 1: Complete quest 'Station Defense'

## QT_TEST_STRIKE_17
* Name: No header for quest qt_test_strike_17
* Description: No description for quest qt_test_strike_17

* Type: Main
* Goals:
	* Task 1: Complete quest 'Station Defense (Heroic)'

## QT_TEST_STRIKE_21
* Name: No header for quest qt_test_strike_21
* Description: No description for quest qt_test_strike_21

* Type: Main
* Goals:
	* Task 1: Complete quest 'Station Defense (Mythic)'

## QT_TEST_STRIKE_15
* Name: No header for quest qt_test_strike_15
* Description: No description for quest qt_test_strike_15

* Type: Main
* Goals:
	* Task 1: Complete quest 'Pahra's Rock'

## QT_TEST_STRIKE_18
* Name: No header for quest qt_test_strike_18
* Description: No description for quest qt_test_strike_18

* Type: Main
* Goals:
	* Task 1: Complete quest 'Pahra's Rock (Heroic)'

## QT_TEST_STRIKE_22
* Name: No header for quest qt_test_strike_22
* Description: No description for quest qt_test_strike_22

* Type: Main
* Goals:
	* Task 1: Complete quest 'Pahra's Rock (Mythic)'

## QT_TEST_STRIKE_19
* Name: No header for quest qt_test_strike_19
* Description: No description for quest qt_test_strike_19

* Type: Main
* Goals:
	* Task 1: Complete quest 'Breach'

## QT_TEST_STRIKE_20
* Name: No header for quest qt_test_strike_20
* Description: No description for quest qt_test_strike_20

* Type: Main
* Goals:
	* Task 1: Complete quest 'Breach (Heroic)'

## QA_001
* Name: No header for quest qa_001
* Description: No description for quest qa_001

* Type: Achievement
* Goals:
	* Task 1: 3000 Mined1A

## QA_002
* Name: No header for quest qa_002
* Description: No description for quest qa_002

* Type: Achievement
* Goals:
	* Task 1: 5 Upgrade

## QS_S2_01_SIJINLIGHTHOUSE
* Name: Sijin Lighthouse
* Description: We detected a possible signal from the missing Khar-Kalaad.
* Type: Side
* FollowUps: ql_raid_019
* Goals:
	* Task 1: Complete mission 'Sijin Lighthouse'

## QS_S2_01_ILIYINLIGHTHOUSE
* Name: Iliyin Lighthouse
* Description: We have arrived at another lighthouse in uncharted territory. Be prepared for anything.
* Type: Side
* Goals:
	* Task 1: Complete mission 'Iliyin Lighthouse'

## QS_S2_01_BTEMPLE
* Name: Bright Temple
* Description: The Amassari here may have answers about the nature of the Progenitor observer.
* Type: Side
* Goals:
	* Task 1: Complete mission 'Bright Temple'

## QS_S2_01_HATALDAN
* Name: Hataldan
* Description: The fallen capital of the Amassari, and last known position of the Observer.
* Type: Side
* FollowUps: ql_raid_020
* Goals:
	* Task 1: Complete mission 'Hataldan'

## Q_COMPENSATION_LVL_10
* Name: Fame and Honor (Lvl 10)
* Description: Player XP can be gained from completing missions and assignments and from destroying enemy units.
* Type: Event
* EventId: event_levelUpCompensationQuests
* Goals:
	* Task 1: 12600 PlayerXP

## Q_COMPENSATION_LVL_20
* Name: Fame and Honor (Lvl 20)
* Description: Player XP can be gained from completing missions and assignments and from destroying enemy units.
* Type: Event
* EventId: event_levelUpCompensationQuests
* Goals:
	* Task 1: 36100 PlayerXP

## Q_COMPENSATION_LVL_35
* Name: Fame and Honor (Lvl 35)
* Description: Player XP can be gained from completing missions and assignments and from destroying enemy units.
* Type: Event
* EventId: event_levelUpCompensationQuests
* Goals:
	* Task 1: 90100 PlayerXP

## Q_COMPENSATION_LVL_50
* Name: Fame and Honor (Lvl 50)
* Description: Player XP can be gained from completing missions and assignments and from destroying enemy units.
* Type: Event
* EventId: event_levelUpCompensationQuests
* Goals:
	* Task 1: 166600 PlayerXP

## Q_COMPENSATION_LVL_75
* Name: Fame and Honor (Lvl 75)
* Description: Player XP can be gained from completing missions and assignments and from destroying enemy units.
* Type: Event
* EventId: event_levelUpCompensationQuests
* Goals:
	* Task 1: 344100 PlayerXP

## Q_COMPENSATION_LVL_100
* Name: Fame and Honor (Lvl 100)
* Description: Player XP can be gained from completing missions and assignments and from destroying enemy units.
* Type: Event
* EventId: event_levelUpCompensationQuests
* Goals:
	* Task 1: 584100 PlayerXP

## Q_COMPENSATION_LVL_150
* Name: Fame and Honor (Lvl 150)
* Description: Player XP can be gained from completing missions and assignments and from destroying enemy units.
* Type: Event
* EventId: event_levelUpCompensationQuests
* Goals:
	* Task 1: 1251600 PlayerXP

## Q_COMPENSATION_LVL_200
* Name: Fame and Honor (Lvl 200)
* Description: Player XP can be gained from completing missions and assignments and from destroying enemy units.
* Type: Event
* EventId: event_levelUpCompensationQuests
* Goals:
	* Task 1: 2169100 PlayerXP

## Q_COMPENSATION_LVL_300
* Name: Fame and Honor (Lvl 300)
* Description: Player XP can be gained from completing missions and assignments and from destroying enemy units.
* Type: Event
* EventId: event_levelUpCompensationQuests
* Goals:
	* Task 1: 4754100 PlayerXP

## Q_TEST_YAOSPR_2024_DAY04_T4
* Name: No header for quest q_test_yaoSpr_2024_day04_t4
* Description: No description for quest q_test_yaoSpr_2024_day04_t4

* Type: Side
* Goals:
	* Task 1: GainItem
