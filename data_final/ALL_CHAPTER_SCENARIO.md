# HOMEWORLD MOBILE CHAPTERS SCRIPT
## 0. chapter_main_t0_01/Arrival

### Quest [qm_t0_tutMissions/Landing]
**DESCRIPTION**:
	Our arrival in this galaxy was met with tragedy.

**GOALS**:
	* Task 1: Complete missions:
		* 'Duzumi Gate'
		* 'Duzumi Gate'
	* Task 2: Complete mission 'Wiracoda Gate'
	* Task 3: Complete mission 'Gulf Taln'

### Mission [story_A02_WiracodaGate/Wiracoda Gate]
**LOCATION:** LAZARUS system, Hiigaran Medea territory
**FACTIONS INVOLVED:** Hiigaran Medea, Progenitor
### Mission [story_A03_GulfTaln/Gulf Taln]
**LOCATION:** LAZARUS system, Hiigaran Medea territory
**FACTIONS INVOLVED:** Cangacian, Iyatequa
**END-OF-DAY DIALOG:**
		_qm_t0_tutMissions_end_
		**Joanna**
		A hiigaran settlement? We should <color=#FBB03F>visit this Lazarus Station</color>. With luck, other missing expeditions to this galaxy made it there.

### Quest [qm_t0_introStation/Lazarus Station]
**DESCRIPTION**:
	We were given the coordinates of a local Hiigaran settlement. We should go there.

**GOALS**:
	* Task 1: Goto LAZARUS system of Hiigaran Medea's territories

**END-OF-DAY DIALOG:**
		_qm_t0_introStation_end_
		**Ekekko**
		Greetings commander, I am Ekekko, a... merchant of the Iyatequa. I would like to seek passage aboard your vessel. In exchange for this transport, I can be your bargain hunter and local guide to this region. I take up little room, and in exchange I can open doors for you that would be closed otherwise.

		**Joanna**
		Commander, the Iyatequa traders have a lot of local contacts in the vicinity. Access to what they know might be useful in the future. I’ve reviewed his proposal and it’s little effort to allow him and his cargo passage onboard. Security has already vetted his entry.

		**Ekekko**
		Well and met Commander, I am pleased to make your acquaintance and share your voyage. Please come by to visit my on-ship store to <color=#FBB03F>collect your first payment</color> now. In the future you may return any time to collect your daily fee. You are my first customer.

### Quest [qm_t0_introMarket/Local Currency]
**DESCRIPTION**:
	The market can be accessed at stations and inside the flagship, though the selection of items in the flagship market is smaller. For now, we need to pick up some local currency to barter with the locals.

**GOALS**:
	* Task 1: Buy: pack_market_freeHC_insta

**END-OF-DAY DIALOG:**
		_qm_t0_introMarket_end_
		**Fleet Command**
		Commander, welcome to Lazarus Base. Our apologies for being unable to respond to your distress signal at Wiracoda gate.

		**Fleet Command**
		We’ve had troubles from the local pirates. Your arrival has also agitated the Progenitor defenders in the region for reasons unknown.

		**Fleet Command**
		We would like to welcome you aboard to bring you up to speed about the situation here in the Nimbus galaxy, but we could use some help securing the local area.

		**Joanna**
		Acknowledged, Lazarus base. Commander, first we should re-equip our forces and <color=#FBB03F>build an interceptor squadron</color>. Our forces were thinned in the battle.


## 1. chapter_main_t0_02/Production & Signals

### Quest [qm_t0_introFabricator/Fabricator]
**DESCRIPTION**:
	Our fabricators are operational again. We should produce more strike craft in case we run into more hostiles.

**GOALS**:
	* Task 1: Craft

**END-OF-DAY DIALOG:**
		_qm_t0_introFabricator_end_
		**Joanna**
		Very good. We need to <color=#FBB03F>ready the new fighters inside our hangars</color>.

### Quest [qm_t0_introEquipStrikecraft/Strike Craft]
**DESCRIPTION**:
	We need to ready our strike craft inside our hangars.

**GOALS**:
	* Task 1: Equip Squad

**END-OF-DAY DIALOG:**
		_qm_t0_introEquipStrikecraft_end_
		**Joanna**
		Now that our interceptors are ready, we can <color=#FBB03F>scan the system</color> for hostile signals.

### Quest [qm_t0_v2_introScanning/Scanning]
**DESCRIPTION**:
	We have been asked to take care of a local threat to the Lazarus Station. We need to find out where it is.

**GOALS**:
	* Task 1: Scan
	* Task 2: Scan

**END-OF-DAY DIALOG:**
		_qm_t0_v2_introScanning_end_
		**Joanna**
		Analysis of the signature completed. The location and additional information is tracked in our computers. <color=#FBB03F>Jump to the signal</color> to engage the enemies.

### Quest [qm_t0_v2_introSignals/Signals]
**DESCRIPTION**:
	We have found hostile signals in the system. We need to clear it out and return to Lazarus Station.

**GOALS**:
	* Task 1: Complete side mission
	* Task 2: Goto LAZARUS system of Hiigaran Medea's territories

**END-OF-DAY DIALOG:**
		_qm_t0_v2_introSignals_end_
		**Fleet Command**
		Thank you for the assist, Commander. We had a raid pass through here as well and our facilities are damaged. We’re asking local commanders to gather resources and supply material for our repairs. Once we’re repaired our port facilities can reopen to you.

		**Fleet Command**
		Scouts have already identified this system as being rich in the resources we need. It would help us if you could <color=#FBB03F>mine some ores</color> here and return them to us.


## 2. chapter_main_t0_03/Materials

### Quest [qm_t0_introScanBelts/Asteroid Clusters]
**DESCRIPTION**:
	We've been asked by Lazarus Station to help with resource scarcity. We'll need to find suitable mining opportunities by scanning for mineral-rich asteroids in nearby systems.

**GOALS**:
	* Task 1: Goto JONALLI system of Hiigaran Medea's territories
	* Task 2: 1 ScannedBelt

**END-OF-DAY DIALOG:**
		_qm_t0_introScanBelts_end_
		**Joanna**
		Commander, we have located several mineral-rich asteroids. We can now <color=#FBB03F>jump to the cluster and use our resource collector to mine ores.</color>

### Quest [qm_t0_introMining/Mining]
**DESCRIPTION**:
	We found a suitable spot for mining. Use the resource collector to mine the mineral rich asteroids.

**GOALS**:
	* Task 1: 50 Mined0A

**END-OF-DAY DIALOG:**
		_qm_t0_introMining_end_
		**Joanna**
		That's it, we now should have enough ore. We should return and <color=#FBB03F>deliver the minerals to Lazarus Station</color>.

### Quest [qm_t0_support/Support]
**DESCRIPTION**:
	Now that we have the needed minerals, we should go back to Lazarus Station to deliver them.

**GOALS**:
	* Task 1: Pay 25 RU Type M Ore in LAZARUS system of Hiigaran Medea's territories

**END-OF-DAY DIALOG:**
		_qm_t0_support_end_
		**Fleet Command**
		Resources received Commander, thank you. We have aboard Gideon S’jet, renowned Progenitor Expert and survivor of the original Caral expedition. He wishes to speak with you.

		**Gideon S'jet**
		Commander, I am Gideon S’jet. I helped design the Progenitor Communicator you have aboard your vessel. I must assist your mission to explore Progenitor sites.

		**Joanna**
		Gideon was the foremost expert in Progenitor sciences after Karan when he disappeared with the Caral expedition. His knowledge would be invaluable. We should <color=#FBB03F>assign Gideon S'jet to the bridge</color>.


## 3. chapter_main_t0_04/Fleet

### Quest [qm_t0_introBridge/Bridge]
**DESCRIPTION**:
	Gideon S'jet has offered his Progenitor expertise. We should appoint him as head of science on the bridge.

**GOALS**:
	* Task 1: Equip Officer

**END-OF-DAY DIALOG:**
		_qm_t0_introBridge_end_
		**Fleet Command**
		While assigned to the bridge, Gideon grants your flagship another combat skill, which can be activated during battle.

		**Fleet Command**
		Skills require energy to activate. While it will regenerate over time, you cannot activate any skills if your energy reserves are depleted. Choose wisely when and which skills to use.

		**Gideon S'jet**
		Thank you commander. I shall relocate myself and my team to your vessel. I advise you to build up your fleet, Progenitor ruins are not to be taken lightly.

		**Joanna**
		Dangerous is an understatement. Lazarus Base has offered the use of their shipyards, we should take advantage of this and <color=#FBB03F>build an assault frigate</color>.

### Quest [qm_t0_introShipyard/Shipyard]
**DESCRIPTION**:
	We have clearance to use the shipyards of Lazarus Station. We should build an additional assault frigate there to bolster our fleet.

**GOALS**:
	* Task 1: Craft

**END-OF-DAY DIALOG:**
		_qm_t0_introShipyard_end_
		**Joanna**
		The shipyard construction has finished. We need to <color=#FBB03F>ready our new frigate using the Fleet Configuration</color>.

### Quest [qm_t0_introEquipEscorts/Escort Ships]
**DESCRIPTION**:
	Our new assault frigate needs to be staffed and readied. We can do that at any station through Fleet Configuration.

**GOALS**:
	* Task 1: Equip Escort

**END-OF-DAY DIALOG:**
		_qm_t0_introEquipEscorts_end_
		**Gideon S'jet**
		Commander, I have studied the after-action report of Wiracoda Gate. Something has changed among the Progenitor ruins in this galaxy, but I require more data before I can begin a useful analysis.

		**Gideon S'jet**
		I have colleagues in the local vicinity which may have more information than I have available. We should visit Baaekh S'jet first. I have sent the coordinates of her research lab to your navigation database.


## 4. chapter_main_t0_05/Progenitor Data

### Quest [qm_t0_scientist_Baaekh_A/Baaekh S’jet]
**DESCRIPTION**:
	Baaekh S’jet was one of the foremost scientists on Progenitor culture. According to Gideon she has data that can help us with our own research into the Progenitors.

**GOALS**:
	* Task 1: Goto ROA TISAAD system of Hiigaran Medea's territories
	* Task 2: Goto SAARET system of Hiigaran Medea's territories
	* Task 3: 
		* 4 ScannedBelt
		* 1 ScannedGenerated

**END-OF-DAY DIALOG:**
		_qm_t0_scientist_Baaekh_A_end_
		**Joanna**
		We have located the hostile forces that have Baaekh S'jet pinned down. We'll engage them at your order, Commander.

### Quest [qm_t0_scientist_Baaekh_B/Rescue Mission]
**DESCRIPTION**:
	We found Baaekh S'jet, but she can't come out of hiding until we have distracted the hostiles in the area.

**GOALS**:
	* Task 1: Complete side mission
	* Task 2: Goto ROA TISAAD system of Hiigaran Medea's territories

**END-OF-DAY DIALOG:**
		_qm_t0_scientist_Baaekh_B_end_
		**Crew Member**
		Thank you for returning me safely. Here is your data. We found coordinates to a progenitor ruin which might be useful for you.

		**Gideon S'jet**
		Thank you. Commander, I have sent the coordinates of the ruin into the navigation database.

### Quest [qm_t0_relic/Relic Retrieval]
**DESCRIPTION**:
	With information provided by Baaekh S’jet, we now know a potential location of a Progenitor Relic in Toasiim that must be retrieved.

**GOALS**:
	* Task 1: Goto TOASIIM system of Hiigaran Medea's territories
	* Task 2: Scan
	* Task 3: Complete mission 'Relic Signature'

### Mission [story_A04_RelicSignature/Relic Signature]
**LOCATION:** TOASIIM system, Hiigaran Medea territory

### Quest [qm_t0_scientist_Hyeaa_A/Hyeaa Somtaaw]
**DESCRIPTION**:
	Hyeaa Somtaaw was an expert in Progenitor Materials sciences. He has established an independent lab at Nokuuna. According to Gideon, he has data that can help us with our own research into the Progenitors.

**GOALS**:
	* Task 1: Goto NOKUUNA system of Hiigaran Medea's territories
	* Task 2: Craft
	* Task 3: Equip Squad
	* Task 4: 225 Mined0A

**END-OF-DAY DIALOG:**
		_qm_t0_scientist_Hyeaa_A_end_
		**Crew Member**
		Yes, this will do. I am transmitting my research data as we speak.

		**Gideon S'jet**
		Commander, this looks very promising. With this data I have traced a progenitor command signal back to Toasiim. We should find a Progenitor Relic generating this signal there.


## 5. chapter_main_t0_06/Ruins

### Quest [qm_t0_Jolja/Delver]
**DESCRIPTION**:
	After examining the Progenitor Relic, Gideon wants us to find a Progenitor Terminal in Iniim. If we access this, we may have some answers about what happened at Wiracoda Gate.

**GOALS**:
	* Task 1: Goto INIIM system of Hiigaran Medea's territories
	* Task 2: Scan
	* Task 3: Complete mission 'Jolja'
	* Task 4: Goto LAZARUS system of Hiigaran Medea's territories

### Mission [story_A05_Jolja/Jolja]
**LOCATION:** INIIM system, Hiigaran Medea territory
**FACTIONS INVOLVED:** Progenitor, Tanoch
**END-OF-DAY DIALOG:**
		_qm_t0_Jolja_end_
		**Fleet Command**
		Commander, your star is rising among our people, and we wish to know <color=#FBB03F>what Kiith you declare allegiance for</color>. Declaring for a Kiith will bring other survivors of that Kiith to your fleet, along with their gifts.

### Quest [qm_t0_pickKiith/Blood Ties]
**DESCRIPTION**:
	The local Hiigaran survivors wish to know what Kiith we affiliate with. There are advantages for declaring for a specific Kiith.

**GOALS**:
	* Task 1: SelectKiith

**END-OF-DAY DIALOG:**
		_qm_t0_pickKiith_end_
		**Fleet Command**
		Excellent. The old structures are still strong, but new systems are beginning to emerge. Maybe you want to join a clan as well.

		**Joanna**
		Commander, while you are listed as the ship's captain, Admiral Enoch is still considered our commanding officer, which...

		**Joanna**
		What I'm trying to say is that you should <color=#FBB03F>register your name</color> in the admiralty board computer. Then you will be officially recognized as our leading flag officer.

### Quest [qm_t0_pickName/Declaration]
**DESCRIPTION**:
	The Hiigaran survivors want to know your name, commander.

**GOALS**:
	* Task 1: ChangeName

**END-OF-DAY DIALOG:**
		_qm_t0_pickName_end_
		**Gideon S'jet**
		We have completed upgrades to the hyperspace module. With greater power we can overcome the strange gravity anomalies that litter this galaxy.

### Quest [qm_t0_joinClan/A Clan of Choice]
**DESCRIPTION**:
	We can increase our firepower and capabilities by joining with other battle groups.

**GOALS**:
	* Task 1: JoinClan


## 6. chapter_main_t1_01/New Materials

### Quest [qm_t1_newOres/New Minerals]
**DESCRIPTION**:
	The inner systems may have different resources. We should check out the asteroids for mining spots.

**GOALS**:
	* Task 1: Goto DEVADAASI system of Iyatequa's territories
	* Task 2: 6 ScannedBelt
	* Task 3: 200 Mined1A_Mined1B_Mined1C

### Quest [qm_t1_introRefining/Refinery]
**DESCRIPTION**:
	The new ores require refining to be usable for construction purposes. Luckily we have refining facilities on board.

**GOALS**:
	* Task 1: 100 Refining1N_Refining1O_Refining1P
	* Task 2: Goto LAZARUS system of Hiigaran Medea's territories


## 7. chapter_main_t1_02/Hiigaran Outposts

### Quest [qm_t1_facHiigaran/Hiigaran Outposts]
**DESCRIPTION**:
	Lazarus station asked us to help some Hiigaran outposts on the frontier.

**GOALS**:
	* Task 1: Complete 3 of qm_t1_facHiigaran_A|qm_t1_facHiigaran_B|qm_t1_facHiigaran_C|qm_t1_facHiigaran_D
	* Task 2: Goto LAZARUS system of Hiigaran Medea's territories

### Quest [qm_t1_facHiigaran_A/Outposts: Rescue]
**DESCRIPTION**:
	Long-range sensors located near another hyperspace gate have registered the presence of a Hiigaran fleet that emerged here. We are asked to this location and try to help any survivors as best as we can.

**GOALS**:
	* Task 1: Goto TELA DIIM system of Iyatequa's territories
	* Task 2: 
		* 3 ScannedGenerated
		* Complete 3 side missions
	* Task 3: Pay 500 RU Type A Ore T1

### Quest [qm_t1_facHiigaran_B/Outposts: Recon]
**DESCRIPTION**:
	To supply the needs of the Hiigaran fleet, we've been dispatched to look for a great mining source. Intel indicates this will put us into direct conflict with the Fleet of Rams.

**GOALS**:
	* Task 1: Goto EKAAM NAR system of Iyatequa's territories
	* Task 2: 10 ScannedBelt
	* Task 3: 
		* 500 Mined1A_Mined1B_Mined1C
		* 15 ShipsDestroyed
	* Task 4: Goto EKAAM NAR system of Iyatequa's territories

### Quest [qm_t1_facHiigaran_C/Outposts: Wall of Will]
**DESCRIPTION**:
	One of the only planetary settlements under Hiigaran control has been scouted by the Fleet of Rams. Until the planetary defenses are strengthened, they need military equipment to supply the defense.

**GOALS**:
	* Task 1: Goto ARIITAR system of Iyatequa's territories
	* Task 2: 500 Mined1A
	* Task 3: Pay 150 RU Type A Ore T1
	* Task 4: Pay 3 Resource Collector
	* Task 5: Pay 1 Interceptor Squadron

### Quest [qm_t1_facHiigaran_D/Outposts: Security]
**DESCRIPTION**:
	Hiigaran forces are working to clear systems to set up for colonization. The system in question is of special importance. We've been asked to go there and assist in securing the area.

**GOALS**:
	* Task 1: Goto INAYAT system of Iyatequa's territories
	* Task 2: Scan
	* Task 3: 
		* 15 ShipsDestroyed
		* Complete 3 side missions
	* Task 4: Goto INAYAT system of Iyatequa's territories

### Quest [qm_t1_strikeCraft/New Strike Craft]
**DESCRIPTION**:
	We have found a way to incorporate the new materials into our ship design.

**GOALS**:
	* Task 1: 
		* Craft
		* Craft
	* Task 2: 
		* Equip Squad
		* Equip Squad


## 8. chapter_main_t1_03/Fleet Operations

### Quest [qm_t1_advCombat_01/Combat Trials]
**DESCRIPTION**:
	Our Hiigaran allies have prepared a combat area to test our improved strike craft.

**GOALS**:
	* Task 1: Complete mission 'Combat Trials'

### Mission [story_B01_CombatTrials/Combat Trials]
**LOCATION:** TELA DIIM system, Iyatequa territory
**FACTIONS INVOLVED:** Cangacian, Hiigaran Medea
### Quest [qm_t1_killEnemyShips/Hostiles]
**DESCRIPTION**:
	These inner systems are crawling with enemies. We should thin their numbers. Enemies are found in asteroid clusters and signals.

**GOALS**:
	* Task 1: 25 ShipsDestroyed

### Quest [qm_t1_RColEquip/New Resource Collector]
**DESCRIPTION**:
	The new ores are more difficult to mine. We should build resource collectors that are equipped to deal with these denser metals.

**GOALS**:
	* Task 1: Craft
	* Task 2: Equip Squad

### Quest [qm_t1_RColMine/Mining Spree]
**DESCRIPTION**:
	We should put our new resource collectors to the test and stockpile some ores.

**GOALS**:
	* Task 1: 4500 Mined1A_Mined1B_Mined1C

### Quest [qm_t1_introPromoteOfficer/Crew Experience]
**DESCRIPTION**:
	Training our officers will increase their performance significantly. To train an officer we need to find insignias. Insignias can be gained from discharging officers and may be rewarded from completing signals.

**GOALS**:
	* Task 1: UpgradeOfficer

### Quest [qm_t1_rankUpOfficer/Crew Promotion]
**DESCRIPTION**:
	We should promote our most experienced officers to further improve their performance. Promoting an officer increase their special ability or may even grant them a second.

**GOALS**:
	* Task 1: UpgradeOfficer

### Quest [qm_t1_escort/New Escorts]
**DESCRIPTION**:
	We should bolster our fleet with frigates made from the new metals.

**GOALS**:
	* Task 1: Craft
	* Task 2: Equip Escort


## 9. chapter_main_t1_04/Cangacian Pirates

### Quest [qm_t1_advCombat_02/Meropis Defense]
**DESCRIPTION**:
	We received a message that Meropis, a Iyatequa communications station, is asking for support in an expected Cangacian attack.

**GOALS**:
	* Task 1: Complete mission 'Meropis Defense'

### Mission [story_B02_MeropisDefense/Meropis Defense]
**LOCATION:** ARIITAR system, Iyatequa territory

### Quest [qm_t1_doSignals/Signal Tracking]
**DESCRIPTION**:
	The Cangacians have been repelled, but we should disrupt their activities by hunting down hostile signals in the area.

**GOALS**:
	* Task 1: Complete side mission

### Quest [qm_t1_facCangacian/Cangacian Troubles]
**DESCRIPTION**:
	Cangacians are attacking colonies. We should help them in whatever way we can.

**GOALS**:
	* Task 1: Complete 3 of qm_t1_facCangacian_A|qm_t1_facCangacian_B|qm_t1_facCangacian_C|qm_t1_facCangacian_D
	* Task 2: Goto LAZARUS system of Hiigaran Medea's territories

### Quest [qm_t1_facCangacian_A/Troubles: Defiance]
**DESCRIPTION**:
	The world of Huaca is looking for help. They are opposing conscription from Supay’s Fleet of Rams, the punishment of which is brutal assault.

**GOALS**:
	* Task 1: Goto NAREDRA system of Iyatequa's territories
	* Task 2: 15 ShipsDestroyedP1
	* Task 3: 
		* 1000 Mined1A_Mined1B_Mined1C
		* 500 Refining1N_Refining1O_Refining1P
	* Task 4: Goto NAREDRA system of Iyatequa's territories

### Quest [qm_t1_facCangacian_B/Troubles: Seeker]
**DESCRIPTION**:
	To oppose the Fleet of Rams, we were asked to undergo a mission to survey and map one of their three largest systems. We should also sabotage their efforts when the opportunity presents itself.

**GOALS**:
	* Task 1: Goto JISHUN system of Iyatequa's territories
	* Task 2: 
		* 4 ScannedGenerated
		* Complete 4 side missions
		* 15 ShipsDestroyedP1
	* Task 3: Goto JISHUN system of Iyatequa's territories

### Quest [qm_t1_facCangacian_C/Troubles: Stone Hearth]
**DESCRIPTION**:
	We're asked to to assist the system of Acheron. They do not have a refinery set up, so we need to go there and refine metals for their construction facilities to use.

**GOALS**:
	* Task 1: Goto DEVADAASI system of Iyatequa's territories
	* Task 2: 15 ScannedBelt
	* Task 3: 
		* 1000 Mined1A
		* 500 Refining1N
	* Task 4: Pay 300 RU Type A Refined T1

### Quest [qm_t1_facCangacian_D/Troubles: A Black Eye]
**DESCRIPTION**:
	The Fleet of Rams is assembling an assault force that is aimed at a cluster of neutral systems. Intel shows that another Cangacian band plans to engage Supay’s commanding lieutenant here. We're asked to create a distraction to weaken the Fleet of Rams in the resulting battle.

**GOALS**:
	* Task 1: Goto ESTRAIIR system of Iyatequa's territories
	* Task 2: Scan
	* Task 3: Pay 1 Interceptor Squadron
	* Task 4: Complete 4 side missions
	* Task 5: Goto ESTRAIIR system of Iyatequa's territories


## 10. chapter_main_t1_05/Explorer

### Quest [qm_t1_introCraftFlagship/Flagship Construction]
**DESCRIPTION**:
	We have an Explorer-class flagship blueprint utilizing the new minerals found in this region.

**GOALS**:
	* Task 1: Start Crafting - Flagship_Ship

### Quest [qm_t1_introEquipFlagship/New Flagship]
**DESCRIPTION**:
	Once the flagship construction has finished, we should move over to the new flagship, including our ships and officers. This is done via the fleet configuration.

**GOALS**:
	* Task 1: Craft
	* Task 2: Equip Flagship
	* Task 3: 
		* Equip Squad
		* Equip Escort
		* Equip Officer

### Quest [qm_t1_killCangacians/Pest Control]
**DESCRIPTION**:
	While we wait for the flagship construction to finish, we might as well make this galaxy a safer place.

**GOALS**:
	* Task 1: 20 ShipsDestroyedP1


## 11. chapter_main_t1_06/Flagship Armaments

### Quest [qm_t1_advCombat_03/The Pool]
**DESCRIPTION**:
	The Iyatequa have flagged a location for suspicious hostile activity. They've asked us to investigate on their behalf.

**GOALS**:
	* Task 1: Complete mission 'The Pool'

### Mission [story_B03_ThePool/The Pool]
**LOCATION:** NIIREA PAAS system, Iyatequa territory
**FACTIONS INVOLVED:** Cangacian
### Quest [qm_t1_killProgenitors/Hostile History]
**DESCRIPTION**:
	The Progenitor remnants present a danger to the people living in this galaxy. We should thin their numbers.

**GOALS**:
	* Task 1: 10 ShipsDestroyedProgenitor

### Quest [qm_t1_craftTurret/Weapon Turrets]
**DESCRIPTION**:
	The new flagship follows modular design principles, allowing us to outfit it with turrets as we choose. First we should build a weapon turret.

**GOALS**:
	* Task 1: Craft

### Quest [qm_t1_mountTurret/Mounting Turrets]
**DESCRIPTION**:
	Now that we have a turret module, we should mount it on our flagship. Turrets can be managed in the external module view of our flagship.

**GOALS**:
	* Task 1: Equip Weapon

### Quest [qm_t1_rareEarths/Rare Elements]
**DESCRIPTION**:
	When refining ores in the refinery there is a chance for rare earths to appear in addition to the refined metals.

**GOALS**:
	* Task 1: GainItem

### Quest [qm_t1_upgradeTurret/Turret Upgrades]
**DESCRIPTION**:
	The rare minerals we have extracted can be used to improve our modules.

**GOALS**:
	* Task 1: Craft

### Quest [qm_t1_upgradeTurret_3/Turret Upgrades Level 3]
**DESCRIPTION**:
	A module can be upgraded multiple times, vastly increasing its power.

**GOALS**:
	* Task 1: Craft

### Quest [qm_t1_upgradeTurret_4/Turret Upgrades Level 4]
**DESCRIPTION**:
	A module can be upgraded multiple times, vastly increasing its power.

**GOALS**:
	* Task 1: Craft

### Quest [qm_t1_upgradeTurret_5/Turret Upgrades Level 5]
**DESCRIPTION**:
	A module can be upgraded multiple times, vastly increasing its power.

**GOALS**:
	* Task 1: Craft

### Quest [qm_t1_upgradeTurret_6/Turret Upgrades Level 6]
**DESCRIPTION**:
	A module can be upgraded multiple times, vastly increasing its power.

**GOALS**:
	* Task 1: Craft

### Quest [qm_t1_upgradeTurret_7/Turret Upgrades Level 7]
**DESCRIPTION**:
	A module can be upgraded multiple times, vastly increasing its power.

**GOALS**:
	* Task 1: Craft

### Quest [qm_t1_upgradeTurret_8/Turret Upgrades Level 8]
**DESCRIPTION**:
	A module can be upgraded multiple times, vastly increasing its power.

**GOALS**:
	* Task 1: Craft

### Quest [qm_t1_upgradeTurretMax/Final Turret Upgrades]
**DESCRIPTION**:
	Once a module has been upgraded to level 9, it is at its maximum level and cannot be upgraded further.

**GOALS**:
	* Task 1: Craft


## 12. chapter_main_t1_07/Progenitor Components

### Quest [qm_t1_facProgenitors/Progenitor Components]
**DESCRIPTION**:
	To improve our scanner, we should gather data on Progenitor vessels. Once we have enough data, we can create a new scanner blueprint.

**GOALS**:
	* Task 1: Complete 3 of qm_t1_facProgenitors_A|qm_t1_facProgenitors_B|qm_t1_facProgenitors_C|qm_t1_facProgenitors_D
	* Task 2: Goto LAZARUS system of Hiigaran Medea's territories

### Quest [qm_t1_facProgenitors_A/Components: A Wide Exchange]
**DESCRIPTION**:
	A few locals in this system have Progenitor technology they willing to hand to us if we agree to help them with their own problems regarding hostile Progenitor vessels and shortage of resources.

**GOALS**:
	* Task 1: Goto JISHUN system of Iyatequa's territories
	* Task 2: 
		* 10 ShipsDestroyedProgenitor
		* 3000 Mined1A_Mined1B_Mined1C
		* 1500 Refining1N_Refining1O_Refining1P
	* Task 3: Goto JISHUN system of Iyatequa's territories

### Quest [qm_t1_facProgenitors_B/Components: Hunt]
**DESCRIPTION**:
	Progenitor vessels in this area are equipped with M-type fuses. We need to attack and destroy a few vessels in order to gather enough of quality for use in the prototype.

**GOALS**:
	* Task 1: Goto NAREDRA system of Iyatequa's territories
	* Task 2: 
		* 5 ScannedGenerated
		* Craft
		* Complete 5 side missions
	* Task 3: Goto NAREDRA system of Iyatequa's territories

### Quest [qm_t1_facProgenitors_C/Components: A Full Quiver]
**DESCRIPTION**:
	Fleet command out of Lazarus frowns upon commanders that delve into Progenitor ruins without a minimum of protection. We need to bring our ship up to code and command will approve our ship for such operations in the future.

**GOALS**:
	* Task 1: Goto SARAAL system of Iyatequa's territories
	* Task 2: GainItem
	* Task 3: Craft
	* Task 4: Complete 5 side missions
	* Task 5: Goto SARAAL system of Iyatequa's territories

### Quest [qm_t1_facProgenitors_D/Components: Repurpose the Past]
**DESCRIPTION**:
	To save time, rather than reconstruct a Particle density array, we can salvage one from advanced Progenitor craft. We need to attack enough Progenitor ships to find one that is in decent condition. The module will require rare earths in order to activate properly. We can gather them at the system as well.

**GOALS**:
	* Task 1: Goto DEVADAASI system of Iyatequa's territories
	* Task 2: 20 ScannedBelt
	* Task 3: 
		* GainItem
		* 10 ShipsDestroyedProgenitor
	* Task 4: Goto DEVADAASI system of Iyatequa's territories


## 13. chapter_main_t1_08/Exploration

### Quest [qm_t1_scannerModule/New Scanner]
**DESCRIPTION**:
	Based on the data from the Progenitor fragments, our engineers have created a new scanner blueprint.

**GOALS**:
	* Task 1: Craft
	* Task 2: Equip Sensor

### Quest [qm_t1_scannerOvercharge/Rare Find]
**DESCRIPTION**:
	Some objects are too hidden to find them with our scanner under regular circumstances. Luckily, we can use special batteries to overcharge the scanner beyond its normal abilities to be able to find those.

**GOALS**:
	* Task 1: ChargeScanner
	* Task 2: Scan

### Quest [qm_t2_findPirateHideout/Hidden in the Dark]
**DESCRIPTION**:
	We need to find the system from where the recent Cangacian activity originates. Reports indicate the system might be near Saraal. We should go there and use our long range scanners.

**GOALS**:
	* Task 1: 
		* Scan
		* Goto DEVADAASI system of Iyatequa's territories

### Quest [qm_t2_strikePirateHideout/Cangacian Hideout]
**DESCRIPTION**:
	We have located the pirate hideout. Now is the time to strike.

**GOALS**:
	* Task 1: Complete 1 of qr_013

### Quest [qm_t1_upgradeModules/Exploration Upgrades]
**DESCRIPTION**:
	In order to move deeper into the galaxy we should upgrade our scanner and drives core.

**GOALS**:
	* Task 1: 
		* Craft
		* Craft

### Quest [qm_t1_introLiaison/Reaching Out]
**DESCRIPTION**:
	The Iyatequa are interested in doing business with us. Completing liaison assignments for them will allow us to increase our reputation, which allows us to buy special items and blueprints in their liaison requisitions office.

**GOALS**:
	* Task 1: 3 Faction


## 14. chapter_main_t1_09/Iyatequa Business

### Quest [qm_t1_introInternals/Internal Modules]
**DESCRIPTION**:
	Our flagship has a configurable interior, which we can use to boost our exploration, production or combat abilities using internal modules.

**GOALS**:
	* Task 1: Craft
	* Task 2: Equip Internal

### Quest [qm_t1_upgradeInternals/Internal Module Upgrades]
**DESCRIPTION**:
	Just like with weapon turrets, we can improve our internal module's performance through upgrades.

**GOALS**:
	* Task 1: Craft

### Quest [qm_t1_facIyatequa/Iyatequa Business]
**DESCRIPTION**:
	The Iyatequa have heard of our plan to meet the Tanoch and agreed to help us set up our science facilities to research better drives. For a price, of course.

**GOALS**:
	* Task 1: Complete 3 of qm_t1_facIyatequa_A|qm_t1_facIyatequa_B|qm_t1_facIyatequa_C|qm_t1_facIyatequa_D
	* Task 2: Goto LAZARUS system of Hiigaran Medea's territories

### Quest [qm_t1_facIyatequa_A/Business: An Honest Job]
**DESCRIPTION**:
	The Iyatequa asked us to perform a variety of simple activities and allowing them to monitor the related systems for their own research purposes.

**GOALS**:
	* Task 1: Goto NIIREA PAAS system of Iyatequa's territories
	* Task 2: 
		* 3000 Mined1A_Mined1B_Mined1C
		* GainItem
		* Craft
	* Task 3: Goto NIIREA PAAS system of Iyatequa's territories

### Quest [qm_t1_facIyatequa_B/Business: The Barrier]
**DESCRIPTION**:
	We've been told to deal with an attempted trade blockade set up by pirates. We will need to get some spare resources and some module upgrades before we face the enemy.

**GOALS**:
	* Task 1: Goto INAYAT system of Iyatequa's territories
	* Task 2: 
		* 1500 Refining1N_Refining1O_Refining1P
		* Craft
	* Task 3: 25 ShipsDestroyed
	* Task 4: Goto INAYAT system of Iyatequa's territories

### Quest [qm_t1_facIyatequa_C/Business: The Sheriff]
**DESCRIPTION**:
	Hostiles have been gathering near Iyatequa trading routes. We've been asked to investigate and root out pirates and other undesirables.

**GOALS**:
	* Task 1: Goto EKAAM NAR system of Iyatequa's territories
	* Task 2: 
		* Scan
		* Complete 5 side missions
		* 25 ShipsDestroyed
	* Task 3: Goto EKAAM NAR system of Iyatequa's territories

### Quest [qm_t1_facIyatequa_D/Business: The Dealer]
**DESCRIPTION**:
	A dealer supplying the Iyatequa has tried cutting corners and incured their wrath. We've been asked to apprehend him.

**GOALS**:
	* Task 1: Goto ARIITAR system of Iyatequa's territories
	* Task 2: Goto TELA DIIM system of Iyatequa's territories
	* Task 3: 
		* Scan
		* Complete 5 side missions
	* Task 4: Pay 1000 RU Type B Refined T1
	* Task 5: Goto ARIITAR system of Iyatequa's territories


## 15. chapter_main_t2_01/Research

### Quest [qm_t2_introRP/Laboratories]
**DESCRIPTION**:
	Our scientists have brought our on-ship laboratories online. We can collect the data of their findings there.

**GOALS**:
	* Task 1: GainItem

### Quest [qm_t2_introResearch/Research Center]
**DESCRIPTION**:
	Lazarus Base has given us access to a workshop module attached to the station. We can perform further research there and develop new technologies.

**GOALS**:
	* Task 1: Craft

### Quest [qm_t2_newResources/New Resources T2]
**DESCRIPTION**:
	It seems the deeper we move into the galaxy the more minerals we find.

**GOALS**:
	* Task 1: Goto BISHAAN TEL system of Iyatequa's territories
	* Task 2: 25 ScannedBelt
	* Task 3: 3000 Mined2A_Mined2B_Mined2C_Mined2D
	* Task 4: Craft
	* Task 5: Goto LAZARUS system of Hiigaran Medea's territories


## 16. chapter_main_t2_02/Cangacian Attacks

### Quest [qm_t2_facCangacian/Cangacian Incursion]
**DESCRIPTION**:
	Several Hiigaran colonies are under attack by Cangacians. Lazarus command has asked us to help as much as we can.

**GOALS**:
	* Task 1: Complete 3 of qm_t2_facCangacian_A|qm_t2_facCangacian_B|qm_t2_facCangacian_C|qm_t2_facCangacian_D
	* Task 2: Goto LAZARUS system of Hiigaran Medea's territories

### Quest [qm_t2_facCangacian_A/Incursion: Reverse Engineering]
**DESCRIPTION**:
	This colony was attacked by vessels incorporating non-Cangacian technology. We're asked to try to reverse engineer some of it.

**GOALS**:
	* Task 1: Goto BISHAAN TEL system of Iyatequa's territories
	* Task 2: 35 ShipsDestroyed
	* Task 3: GainItem
	* Task 4: Craft
	* Task 5: Goto BISHAAN TEL system of Iyatequa's territories

### Quest [qm_t2_facCangacian_B/Incursion: Rebuilding Efforts]
**DESCRIPTION**:
	This colony was hit hard. We need to clear the area of remaining pirates and help with rebuilding.

**GOALS**:
	* Task 1: Goto SOBEL REM system of Iyatequa's territories
	* Task 2: Complete 10 side missions
	* Task 3: 
		* Pay 650 RU Type A Ore T2
		* Pay 650 RU Type B Ore T2
		* Pay 650 RU Type C Ore T2
	* Task 4: GainItem
	* Task 5: Goto SOBEL REM system of Iyatequa's territories

### Quest [qm_t2_facCangacian_C/Incursion: Enemy Intentions]
**DESCRIPTION**:
	This colony repelled the attackers and gathered some intel. They need our help to decrypt it and find safe places for mining.

**GOALS**:
	* Task 1: Goto KEID system of Iyatequa's territories
	* Task 2: GainItem
	* Task 3: 
		* 30 ScannedBelt
		* 35 ShipsDestroyed
	* Task 4: Goto KEID system of Iyatequa's territories

### Quest [qm_t2_facCangacian_D/Incursion: Preemptive Strike]
**DESCRIPTION**:
	The most recent attack. Intel shows it was just a scouting mission. We need to help with setting up quick defenses and take out the assault fleet before they can strike.

**GOALS**:
	* Task 1: Goto MITUUL system of Iyatequa's territories
	* Task 2: Pay 1000 RU Type B Refined T2
	* Task 3: 
		* 10 ScannedGenerated
		* Complete 10 side missions
	* Task 4: Goto MITUUL system of Iyatequa's territories


## 17. chapter_main_t2_03/Advanced Materials

### Quest [qm_t2_startResearchT2Intc/Interceptor T2]
**DESCRIPTION**:
	We can research better ship blueprints using the new materials found in this region.

**GOALS**:
	* Task 1: Start Research - rp_catStrCraft_bp_sf_intc_t2_c

### Quest [qm_t2_finResearchT2Intc/Interceptor Schematics]
**DESCRIPTION**:
	Schematics research unlock new blueprints for the fabricators and shipyard.

**GOALS**:
	* Task 1: Craft

### Quest [qm_t2_introParts/Ship Parts Assembly]
**DESCRIPTION**:
	The new constructions will require the use of specially fabricated parts.

The blueprints for small Hull, Weapon and Machinery parts can be found in the market.

**GOALS**:
	* Task 1: Buy: bp_intmed_ship_small_t2
	* Task 2: Craft

### Quest [qm_t2_strikeCraft/Strike Craft T2]
**DESCRIPTION**:
	Now that we have finished the research and crafted the necessary parts, we can craft an interceptor squadron.

**GOALS**:
	* Task 1: Complete 1 of qm_t2_finResearchT2Intc
	* Task 2: Craft


## 18. chapter_main_t2_04/Lazarus Repairs

### Quest [qm_t2_facHiigaran/Lazarus Repairs]
**DESCRIPTION**:
	Lazarus Station was recently attacked. Command asked us to help with rebuilding efforts.

**GOALS**:
	* Task 1: Complete 3 of qm_t2_facHiigaran_A|qm_t2_facHiigaran_B|qm_t2_facHiigaran_C|qm_t2_facHiigaran_D

### Quest [qm_t2_facHiigaran_A/Repairs: Mining Opportunities]
**DESCRIPTION**:
	To repair Lazarus Station, new minerals are needed. We are asked to look for new places to mine and help set up the fabrication systems.

**GOALS**:
	* Task 1: Goto KEID system of Iyatequa's territories
	* Task 2: Scan
	* Task 3: Craft
	* Task 4: Pay 1000 RU Type C Refined T2

### Quest [qm_t2_facHiigaran_B/Repairs: Secure the Perimeter]
**DESCRIPTION**:
	After the recent attack, we need to secure the borders of Hiigaran space.

**GOALS**:
	* Task 1: Goto KISHO RE system of Iyatequa's territories
	* Task 2: Complete 10 side missions
	* Task 3: Craft
	* Task 4: Pay 60 Small Hull Parts

### Quest [qm_t2_facHiigaran_C/Repairs: Motivation Boost]
**DESCRIPTION**:
	We are asked to lead several high profile campaigns against enemy forces to rally more Hiigaran fleets and raise awareness to the rebuilding efforts of Lazarus Station.

(The blueprints for small Weapon and Machinery parts can be found in the market.)

**GOALS**:
	* Task 1: Goto BISHAAN TEL system of Iyatequa's territories
	* Task 2: 
		* Complete side mission
		* 35 ShipsDestroyed
	* Task 3: Pay 60 Small Weapon Parts

### Quest [qm_t2_facHiigaran_D/Repairs: Empty the Lairs]
**DESCRIPTION**:
	The attackers still have their bases of operation. We need to clear them out to prevent future attacks.

**GOALS**:
	* Task 1: Goto MARAT KAN system of Iyatequa's territories
	* Task 2: 
		* 35 ScannedBelt
		* 35 ShipsDestroyed
	* Task 3: 
		* Pay 650 RU Type A Ore T2
		* Pay 650 RU Type B Ore T2
		* Pay 650 RU Type C Ore T2

### Quest [qm_t2_craftRCol/Resource Collector T2]
**DESCRIPTION**:
	Mining the new ores can be done faster with special resource collectors equipped with better mining gear.

**GOALS**:
	* Task 1: Craft

### Quest [qm_t2_RColMining/Ore Deal]
**DESCRIPTION**:
	With our new resource collectors, we can mine ores much faster than before.

**GOALS**:
	* Task 1: 9000 Mined2A_Mined2B_Mined2C_Mined2D

### Quest [qm_t2_craftRCon/Resource Controller]
**DESCRIPTION**:
	We acquired a blueprint for the Resource Controller, an escort ship we can send on independent mining missions. Like other escort ships, it must be built in the shipyard.

**GOALS**:
	* Task 1: Craft

### Quest [qm_t2_introIdleMine/Remote Mining]
**DESCRIPTION**:
	Resource Controllers can be sent away to mine ores without our supervision. To do that, it must be assigned to an escort slot in fleet configuration.

**GOALS**:
	* Task 1: 5000 IdleMined


## 19. chapter_main_t2_05/Improved Fleet

### Quest [qm_t2_startResearchT2Frig/Assault Frigate T2]
**DESCRIPTION**:
	We can research a better assault frigate blueprint using the new minerals.

**GOALS**:
	* Task 1: Start Research - rp_catEscorts_bp_cf_assa_t2_c

### Quest [qm_t2_finResearchT2Frig/Assault Frigate Schematics]
**DESCRIPTION**:
	Our scientists are at work developing new schematics for the assault frigate.

**GOALS**:
	* Task 1: Craft

### Quest [qm_t2_largeHullParts/Large Hull Parts Assembly]
**DESCRIPTION**:
	The frigate blueprint requires a large version of the hull parts.

The blueprint for large hull parts can be found in the market.

**GOALS**:
	* Task 1: Buy: bp_intmed_ship_large_t2
	* Task 2: Craft

### Quest [qm_t2_escort/Escort Ships T2]
**DESCRIPTION**:
	With the large hull parts we can finally construct the frigate.

**GOALS**:
	* Task 1: Craft

### Quest [qm_t2_introOreD/Gold Rush]
**DESCRIPTION**:
	Some asteroids in this region contain a rare ore we can use for advanced constructions.

**GOALS**:
	* Task 1: 3500 Mined2D
	* Task 2: Craft

### Quest [qm_t2_craftUncShip/Elite Ships]
**DESCRIPTION**:
	We acquired a blueprint for an advanced ship design. It requires the rare ore to be built.

**GOALS**:
	* Task 1: Craft


## 20. chapter_main_t2_06/Iyatequa Intermediary

### Quest [qm_t2_introLiaison/Liaison Office]
**DESCRIPTION**:
	Doing assignments for the liaison office will allow us to requisition better blueprints and better equipment.

**GOALS**:
	* Task 1: 3 Faction

### Quest [qm_t2_strikeStationDefense/Station Defense]
**DESCRIPTION**:
	A large Tanoch station is under attack by a large fleet of pirates. We should band together with other fleets to repel the attackers.

**GOALS**:
	* Task 1: Complete 1 of qr_014

### Quest [qm_t2_researchPulsarCorvette/Pulsar Corvette Schematics]
**DESCRIPTION**:
	Uncommon, rare and epic researches are not part of the central research path and must be found in order to be researched.

The Pulsar Corvette Schematics can be found in the code fragment market.

**GOALS**:
	* Task 1: Craft

### Quest [qm_t2_pulsarCorvette/Pulsar Corvette]
**DESCRIPTION**:
	Pulsar Corvettes are effective against other corvettes and small escort ships.

**GOALS**:
	* Task 1: Craft

### Quest [qm_t2_facIyatequa/Iyatequa Intermediary]
**DESCRIPTION**:
	The Iyatequa have offered to liaison between us and the Tanoch if we agree to run some errands for them.

**GOALS**:
	* Task 1: Complete 3 of qm_t2_facIyatequa_A|qm_t2_facIyatequa_B|qm_t2_facIyatequa_C|qm_t2_facIyatequa_D
	* Task 2: Goto LAZARUS system of Hiigaran Medea's territories

### Quest [qm_t2_facIyatequa_A/Intermediary: Delivery Run]
**DESCRIPTION**:
	The Iyatequa want us to deliver some resources - from our own pockets. They said the rewards will compensate for our losses. We'll see.

**GOALS**:
	* Task 1: Goto SOBEL REM system of Iyatequa's territories
	* Task 2: 
		* Pay 1000 RU Type B Refined T2
		* Pay 1000 RU Type C Refined T2
		* Pay 20 Large Hull Parts
	* Task 3: 7 Faction_Tr1_T2up
	* Task 4: Goto SOBEL REM system of Iyatequa's territories

### Quest [qm_t2_facIyatequa_B/Intermediary: Patrolling Trade Routes]
**DESCRIPTION**:
	We're asked to patrol the Iyatequa trading routes and clear out hostiles near them.

**GOALS**:
	* Task 1: Goto KISHO RE system of Iyatequa's territories
	* Task 2: 15 ShipsDestroyedProgenitor
	* Task 3: 15 Faction_Tr1_T2up
	* Task 4: Goto KISHO RE system of Iyatequa's territories

### Quest [qm_t2_facIyatequa_C/Intermediary: The Catch]
**DESCRIPTION**:
	This assignment seems simple enough. We simply have to find Cangacian fleets and destroy them.

**GOALS**:
	* Task 1: Goto MARAT KAN system of Iyatequa's territories
	* Task 2: 30 ShipsDestroyedP1
	* Task 3: 
		* 30 ShipsDestroyed
		* 7 Faction_Tr1_T2up
	* Task 4: Goto MARAT KAN system of Iyatequa's territories

### Quest [qm_t2_facIyatequa_D/Intermediary: Art of Escape]
**DESCRIPTION**:
	The Iyatequa want us to find a master thief of legendary reputation.

**GOALS**:
	* Task 1: Goto MITUUL system of Iyatequa's territories
	* Task 2: Scan
	* Task 3: GainItem
	* Task 4: 
		* Pay 1 Resource Collector
		* Pay 500 RU Type D Ore T2
	* Task 5: Goto MITUUL system of Iyatequa's territories


## 21. chapter_main_t2_07/Improved Flagship

### Quest [qm_t2_liaisonTanoch/Tanoch Relations]
**DESCRIPTION**:
	The Tanoch liaison office will offer better items the higher our reputation is.

**GOALS**:
	* Task 1: 10 Faction_Tanoch_T2up

### Quest [qm_t2_largeWeaponParts/Large Weapon Parts Assembly]
**DESCRIPTION**:
	Large weapon parts are required for building flagships and weapon modules.

The blueprint for large weapon parts can be found in the Tanoch liaison requisitions office.

**GOALS**:
	* Task 1: Craft

### Quest [qm_t2_liaisonIyatequa/Iyatequa Relations]
**DESCRIPTION**:
	The Iyatequa liaison office will offer better items the higher our reputation is.

**GOALS**:
	* Task 1: 10 Faction_Tr1_T2up

### Quest [qm_t2_largeMachineParts/Large Machinery Parts Assembly]
**DESCRIPTION**:
	Large machinery parts are required for building flagships and non-weapon modules.

The blueprint for large machinery parts can be found in the Iyatequa liaison requisitions office.

**GOALS**:
	* Task 1: Craft

### Quest [qm_t2_startCraftFlagship/Flagship Construction T2]
**DESCRIPTION**:
	Now that we have the necessary resources, we can start building our new flagship. Its larger drive core will allow us to enter Tanoch territory. Flagship blueprints are available in the market.

**GOALS**:
	* Task 1: Complete 2 of qm_t2_largeWeaponParts|qm_t2_largeMachineParts
	* Task 2: Start Crafting - Flagship_Ship_T2

### Quest [qm_t2_finCraftFlagship/Flagship T2]
**DESCRIPTION**:
	The construction of our new flagship is under way. Once it's finished, we can switch over and move our squadrons and officers as well as modules to the new flagship.

**GOALS**:
	* Task 1: Craft

### Quest [qm_t2_strikePahrasRock/Pahra's Rock]
**DESCRIPTION**:
	Pirate's major Asteroid Base in the area has been threatening the Hiigaran settlements. Hiigaran Flagships have been gathered to strike on this Base.​

**GOALS**:
	* Task 1: Complete 1 of qr_015


## 22. chapter_main_t2_08/The Tanoch Empire

### Quest [qm_t2_turrets/Weapon Turrets T2]
**DESCRIPTION**:
	We should stay up to date on weapon technology. Researching new weapon schematics will unlock better modules.

**GOALS**:
	* Task 1: Craft
	* Task 2: Craft
	* Task 3: Equip Weapon

### Quest [qm_t2_tanochet/Tanochet]
**DESCRIPTION**:
	We can finally reach the Tanoch capital. It is time to meet the emperor.

**GOALS**:
	* Task 1: Complete mission 'Tanochet'

### Mission [story_C01_Tanochet/Tanochet]
**LOCATION:** TANOCHETLAN system, Tanoch territory
**FACTIONS INVOLVED:** Tanoch, Yaot
### Quest [qm_t2_epicSignals/High Risk High Reward]
**DESCRIPTION**:
	Occasionally we come across high energy signals. It might be worth checking out, but it could also be a potential danger. We should proceed with caution.

**GOALS**:
	* Task 1: 
		* Scan
		* Complete side mission

### Quest [qm_t2_facTanoch/Tanoch Errands]
**DESCRIPTION**:
	The Tanoch have asked us to run some errands for them. This could be a chance for us to gain their trust.

**GOALS**:
	* Task 1: Complete 3 of qm_t2_facTanoch_A|qm_t2_facTanoch_B|qm_t2_facTanoch_C|qm_t2_facTanoch_D
	* Task 2: Goto TANOCHETLAN system of Tanoch's territories

### Quest [qm_t2_facTanoch_A/Errands: Golden Harvest]
**DESCRIPTION**:
	A Tanoch planetary government is experiencing a resource shortfall, and has asked for help with procuring raw material.

**GOALS**:
	* Task 1: 40 ScannedBelt
	* Task 2: 
		* Pay 350 RU Type A Refined T2
		* Pay 350 RU Type B Refined T2
		* Pay 350 RU Type C Refined T2

### Quest [qm_t2_facTanoch_B/Errands: Safety and Security]
**DESCRIPTION**:
	Pirates are attacking Tanoch systems. We've been asked to drive them back.

**GOALS**:
	* Task 1: 
		* 350 RepTanoch
		* 15 ShipsDestroyedP1

### Quest [qm_t2_facTanoch_C/Errands: Disaster Relief]
**DESCRIPTION**:
	A Tanoch world is having trouble getting resources from the Empire so they’ve asked anyone for help.

**GOALS**:
	* Task 1: 
		* Craft
		* Craft
	* Task 2: 
		* Pay 350 RU Type B Refined T2
		* Pay 50 Small Machinery Parts
		* Pay 1 Resource Collector

### Quest [qm_t2_facTanoch_D/Errands: Hired Defenses]
**DESCRIPTION**:
	The border worlds are being threatened from Yaot assaults and are desperate for defenders. They ask us to drive the Yaot back.

**GOALS**:
	* Task 1: 
		* Scan
		* 15 ShipsDestroyedYaot


## 23. chapter_main_t2_09/Temple Tonaati

### Quest [qm_t2_compartments/Compartments]
**DESCRIPTION**:
	Our flagship is sectioned into three compartments. We can install different modules in different compartments.

**GOALS**:
	* Task 1: 
		* Equip Internal
		* Equip Internal

### Quest [qm_t2_templeTonaati/Temple Tonaati]
**DESCRIPTION**:
	We are following Vaygr fleet to find out their hidden plan.

**GOALS**:
	* Task 1: Complete mission 'Temple Tonaati'

### Mission [story_C02_TempleTonaati/Temple Tonaati]
**LOCATION:** TANOCHETLAN system, Tanoch territory
**FACTIONS INVOLVED:** Tanoch, TanochTemple, Yaot
### Quest [qm_t2_facYaot/Yaot Conflict]
**DESCRIPTION**:
	We have received assignments from both Tanochetlan and Lazarus station. They asked us to investigate the Yaot threat.

**GOALS**:
	* Task 1: Complete 3 of qm_t2_facYaot_A|qm_t2_facYaot_B|qm_t2_facYaot_C|qm_t2_facYaot_D
	* Task 2: Goto TANOCHETLAN system of Tanoch's territories

### Quest [qm_t2_facYaot_A/Conflict: Direct Attack]
**DESCRIPTION**:
	The Tanoch want us to actively engage the Yaot fleets to disrupt their activities in Tanoch space.

**GOALS**:
	* Task 1: 30 ShipsDestroyedYaot

### Quest [qm_t2_facYaot_B/Conflict: Hazardous Archeology]
**DESCRIPTION**:
	We are looking for evidence of a missing Progenitor hyperspace gate in the area which should be there but isn’t. According to Tanoch intelligence the Yaot are also seeking this object.

**GOALS**:
	* Task 1: 
		* 45 ScannedBelt
		* 1800 Mined2A_Mined2B_Mined2C_Mined2D

### Quest [qm_t2_facYaot_C/Conflict: Seek and Find]
**DESCRIPTION**:
	A Hiigaran flagship has gone missing in Tanoch space. Preliminary evidence points towards Yaot involvement. Lazarus wants us to investigate.

**GOALS**:
	* Task 1: 
		* Scan
		* Complete 10 side missions
		* Scan

### Quest [qm_t2_facYaot_D/Conflict: Opposition Research]
**DESCRIPTION**:
	The Yaot are the first major antagonistic power we have encountered. We need to make sure our crew is properly trained and ready to handle the upcoming battles.

**GOALS**:
	* Task 1: 
		* GainItem
		* UpgradeOfficer


## 24. chapter_main_t2_10/Frontiers

### Quest [qs_exploration_01/Exploration I]
**DESCRIPTION**:
	We should explore this galaxy further. Who knows what we could find.

**GOALS**:
	* Task 1: 
		* Scan
		* Complete 10 side missions

### Quest [qs_exploration_02/Exploration II]
**DESCRIPTION**:
	We have made discoveries that will keep our scientists busy for months.

**GOALS**:
	* Task 1: GainItem

### Quest [qs_exploration_03/Exploration III]
**DESCRIPTION**:
	This galaxy is full of danger and opportunity. We should analyze and prepare.

**GOALS**:
	* Task 1: Scan
	* Task 2: Pay 5000 RU Type C Refined T2

### Quest [qs_economy_01/Production I]
**DESCRIPTION**:
	Building up a fleet requires a constant supply of materials.

**GOALS**:
	* Task 1: 
		* Craft
		* Complete 5 side missions

### Quest [qs_economy_02/Production II]
**DESCRIPTION**:
	We should not let our fabrication modules go idle.

**GOALS**:
	* Task 1: Craft

### Quest [qs_economy_03/Production III]
**DESCRIPTION**:
	Building bigger and greater ships will require bigger and greater materials.

**GOALS**:
	* Task 1: Craft
	* Task 2: Pay 5000 RU Type A Refined T2

### Quest [qs_battle_01/Combat I]
**DESCRIPTION**:
	Space is full of danger. We need to be prepared.

**GOALS**:
	* Task 1: 
		* Craft
		* Complete 15 side missions

### Quest [qs_battle_02/Combat II]
**DESCRIPTION**:
	We need allies if we are to survive in this galaxy.

**GOALS**:
	* Task 1: 25 Faction_T2up

### Quest [qs_battle_03/Combat III]
**DESCRIPTION**:
	Only great challenges yield great rewards.

**GOALS**:
	* Task 1: Complete side mission
	* Task 2: Pay 5000 RU Type B Refined T2


## 25. chapter_main_t3_01/Expanding the Horizon

### Quest [qm_t3_researchJumpCap/Expanding the Horizon]
**DESCRIPTION**:
	Our scientists have come up with new theories on how to increase the power of our engines. With the new technology we should be able to enter space that was previously inaccessible to us.

**GOALS**:
	* Task 1: Craft

### Quest [qm_t3_scouting/New Frontiers]
**DESCRIPTION**:
	With our improved hyperjump technology, we should upgrade our engines and sensors to explore the new areas.

**GOALS**:
	* Task 1: 
		* Craft
		* Craft

### Quest [qm_t3_scouting_scanBelts/Resource Scouting]
**DESCRIPTION**:
	Fleet command wants accurate maps of nearby asteroid clusters in order to chart resources and hazards. Contribute to this effort by scanning asteroid clusters.

**GOALS**:
	* Task 1: 55 ScannedBelt

### Quest [qm_t3_scouting_scanJovian/Gas Giant Scan]
**DESCRIPTION**:
	New scanning protocols for scanning gas giants are being tested. Contribute to this test by fully scanning a gas giant.

**GOALS**:
	* Task 1: 1 ScannedJovian

### Quest [qm_t3_gasMining/A New Resource]
**DESCRIPTION**:
	We found a new type of resource that warrants a closer look. We should take some samples for study. To harvest gas, simply send a Gas Collector into the atmosphere of a gas planet. Be careful. Deeper layers will deal more damage to your ships! The blueprint for the Gas Collector can be found in the Market.

**GOALS**:
	* Task 1: Craft
	* Task 2: 1000 Mined3E_Mined3F_Mined3G_Mined3H

### Quest [qm_t3_yaotLiaison/Yaot Relations]
**DESCRIPTION**:
	The Yaot have opened their liaison office to us.

**GOALS**:
	* Task 1: 1000 RepYaot


## 26. chapter_main_t3_02/Uneasy Allies

### Quest [qm_t3_facYaot/Uneasy Allies]
**DESCRIPTION**:
	The Yaot are interested in opening relations with us and wish to begin a dialogue.

**GOALS**:
	* Task 1: Complete 2 of qm_t3_sideYaot_A_3|qm_t3_sideYaot_B_3|qm_t3_sideYaot_C_3
	* Task 2: Goto YAOTL system of Yaot's territories

### Quest [qm_t3_sideYaot_A_1/Truce: Loadstones I]
**DESCRIPTION**:
	The Yaot present a simple request to map and gather resources in order to test our capabilities and their trust in us.

**GOALS**:
	* Task 1: 
		* 65 ScannedBelt
		* Pay 50 RU Type B Refined T3

### Quest [qm_t3_sideYaot_A_2/Truce: Loadstones II]
**DESCRIPTION**:
	The Yaot have asked us to collect further resources and clear the mining areas of hostiles.

**GOALS**:
	* Task 1: 
		* 2500 Mined3C
		* 30 ShipsDestroyed

### Quest [qm_t3_sideYaot_A_3/Truce: Loadstones III]
**DESCRIPTION**:
	The Yaot are interested in learning our capacity for materials refining. We'll be compensated well.

**GOALS**:
	* Task 1: 
		* 300 Refining3N
		* Pay 100 RU Type A Refined T3

### Quest [qm_t3_sideYaot_B_1/Truce: The Privateer I]
**DESCRIPTION**:
	The Yaot have a supply line they want protected, and are willing to hire us to clear it of hostiles.

**GOALS**:
	* Task 1: 
		* Scan
		* Complete 6 side missions

### Quest [qm_t3_sideYaot_B_2/Truce: The Privateer II]
**DESCRIPTION**:
	The Yaot wish to commission us to guard this patrol route until their own patrols can relieve us.

**GOALS**:
	* Task 1: 
		* 30 ShipsDestroyed
		* GainItem

### Quest [qm_t3_sideYaot_B_3/Truce: The Privateer III]
**DESCRIPTION**:
	The Yaot are impressed with our combat capabilities and want to see how we fare against stronger enemies.

**GOALS**:
	* Task 1: Complete 3 side missions

### Quest [qm_t3_sideYaot_C_1/Truce: Exchange of Ideas I]
**DESCRIPTION**:
	The Yaot have made more contracts available to us on a trial basis. We should engage them.

**GOALS**:
	* Task 1: 5 Faction_Yaot_T3up

### Quest [qm_t3_sideYaot_C_2/Truce: Exchange of Ideas II]
**DESCRIPTION**:
	The Yaot are becoming more comfortable with employing us. More work for them will go a long way to improving relations.

**GOALS**:
	* Task 1: 
		* 250 RepYaot
		* 30 ShipsDestroyed

### Quest [qm_t3_sideYaot_C_3/Truce: Exchange of Ideas III]
**DESCRIPTION**:
	The Yaot trust us enough to employ our services on a contract basis. More work is available.

**GOALS**:
	* Task 1: 
		* GainItem
		* 4050 RepYaot


## 27. chapter_main_t3_03/Inside the Empire

### Quest [qm_t3_facTanoch/Inside the Empire]
**DESCRIPTION**:
	We have been contacted by the Chicuat people within the Tanoch empire. They have been denied Imperial services and are asking us for help.

**GOALS**:
	* Task 1: Complete 2 of qm_t3_sideTanoch_A_3|qm_t3_sideTanoch_B_3|qm_t3_sideTanoch_C_3
	* Task 2: Goto TANOCHETLAN system of Tanoch's territories

### Quest [qm_t3_sideTanoch_A_1/Chicuat: Dry Well I]
**DESCRIPTION**:
	Next to no Imperial resources are reaching the Chicuat worlds. They are asking us to provide what we spare.

**GOALS**:
	* Task 1: 
		* Pay 400 RU Type A Ore T3
		* Pay 200 RU Type B Ore T3
		* Pay 1400 RU Type C Ore T3

### Quest [qm_t3_sideTanoch_A_2/Chicuat: Dry Well II]
**DESCRIPTION**:
	The Chicuat refineries are busy with the ores we have provided. Meanwhile, an agricultural colony providing most of the food in the sector is running on systems that are barely holding together. They have asked us for spare parts.

**GOALS**:
	* Task 1: Pay 15 Large Machinery Parts

### Quest [qm_t3_sideTanoch_A_3/Chicuat: Dry Well III]
**DESCRIPTION**:
	The economic system has been stabilized, but without proper defenses, raiders will undo everything we've done. We should provide them with some fighters of their own and give their militia some training.

**GOALS**:
	* Task 1: 
		* Pay 50 Small Hull Parts
		* Pay 50 Small Weapon Parts
	* Task 2: Complete 5 side missions

### Quest [qm_t3_sideTanoch_B_1/Chicuat: Exposed I]
**DESCRIPTION**:
	Without Imperial patrols, Chicuat space is vulnerable against raiders. They have asked us to make a sweep across their space to clear the sector of hostiles.

**GOALS**:
	* Task 1: 
		* Scan
		* 35 ShipsDestroyed

### Quest [qm_t3_sideTanoch_B_2/Chicuat: Exposed II]
**DESCRIPTION**:
	Most hostiles have been chased off, but some bold bands of the Fleet of Rams have refused to be intimidated. It is time to make a statement.

**GOALS**:
	* Task 1: 
		* Complete 7 side missions
		* 25 ShipsDestroyedP1

### Quest [qm_t3_sideTanoch_B_3/Chicuat: Exposed III]
**DESCRIPTION**:
	The Chicuat officials have seen our results and several of them want to see us in action. They hope to learn from us how to organize their defenses better.

**GOALS**:
	* Task 1: 
		* Complete 3 side missions
		* GainItem

### Quest [qm_t3_sideTanoch_C_1/Chicuat: Favors I]
**DESCRIPTION**:
	Our contact has suggested running some errands for the Tanoch in the name of the Chicuat people. Doing so would hopefully increase the Chicuat's standing within the Empire.

**GOALS**:
	* Task 1: 500 RepTanoch

### Quest [qm_t3_sideTanoch_C_2/Chicuat: Favors II]
**DESCRIPTION**:
	The Empire is reacting to our support of the Chicuat people. While we wait to learn more about the outcome, the Chicuat have asked if their officers can cross-train with ours.

**GOALS**:
	* Task 1: 
		* UpgradeOfficer
		* 7 Faction_Tanoch_T2up

### Quest [qm_t3_sideTanoch_C_3/Chicuat: Favors III]
**DESCRIPTION**:
	After lengthy negotiations with the Chicuat, the Empire reluctantly has agreed to a relief operation, sending resources to worlds in need. Naturally they ask us for support instead of sending their own materials...

**GOALS**:
	* Task 1: 
		* 8500 RepTanoch
		* 600 Refining3N_Refining3O_Refining3P_Refining3Q


## 28. chapter_main_t3_04/Star Totek

### Quest [qm_t3_starTotek/Star Totek]
**DESCRIPTION**:
	We are closing in on possible Vaygr transmissions close to the star.

**GOALS**:
	* Task 1: Complete mission 'Star Totek'

### Mission [story_C03_StarTotek/Star Totek]
**LOCATION:** TANOCHETLAN system, Tanoch territory
**FACTIONS INVOLVED:** Progenitor, Vaygr
### Quest [qm_t3_strikeBreach/Breach]
**DESCRIPTION**:
	We found an enemy base that is heavily fortified. Breaching its defenses will not be easy.

**GOALS**:
	* Task 1: Complete 1 of qr_019

### Quest [qm_t3_facHiigaran/Planting the Flag]
**DESCRIPTION**:
	Lazarus Base calls us back to the Hiigaran colonies to establish a presence there and keep the peace.

**GOALS**:
	* Task 1: Complete 2 of qm_t3_sideHiigaran_A_3|qm_t3_sideHiigaran_B_3|qm_t3_sideHiigaran_C_3
	* Task 2: Goto LAZARUS system of Hiigaran Medea's territories

### Quest [qm_t3_sideHiigaran_A_1/Colonies: Brick Making I]
**DESCRIPTION**:
	Hiigaran resource efforts are very short handed, so we’ll be going to assist gas collection in deep space.

**GOALS**:
	* Task 1: 
		* 20 ScannedJovian
		* 600 Mined3E_Mined3F_Mined3G_Mined3H

### Quest [qm_t3_sideHiigaran_A_2/Colonies: Brick Making II]
**DESCRIPTION**:
	Our assistance has been helpful so far, but we are asked to provide and analyze some ore samples from the deeper regions of the galaxy.

**GOALS**:
	* Task 1: 
		* 5000 Mined3A_Mined3B_Mined3C_Mined3D
		* GainItem

### Quest [qm_t3_sideHiigaran_A_3/Colonies: Brick Making III]
**DESCRIPTION**:
	The logistics have been set up for the most part, but we are asked to help with some deliveries.

**GOALS**:
	* Task 1: 
		* Pay 100 GU Type G Gas T3
		* Pay 200 RU Type B Refined T3
		* Pay 40 Small Hull Parts

### Quest [qm_t3_sideHiigaran_B_1/Colonies: Security Blanket I]
**DESCRIPTION**:
	Lazarus base has established a quota for all commanders hunting loose pirates in Hiigaran space.

**GOALS**:
	* Task 1: 
		* 30 ShipsDestroyedP1
		* GainItem

### Quest [qm_t3_sideHiigaran_B_2/Colonies: Security Blanket II]
**DESCRIPTION**:
	Most pirates have gone into hiding, but we are asked to make sweeps of local space, to flush out the remaining hostiles.

**GOALS**:
	* Task 1: 
		* Scan
		* Complete 5 side missions

### Quest [qm_t3_sideHiigaran_B_3/Colonies: Security Blanket III]
**DESCRIPTION**:
	The hostile presence has been reduced to a manageable level, but Progenitor craft threaten research vessels. We need to get rid of them and analyze some of the debris.

**GOALS**:
	* Task 1: 
		* 15 ShipsDestroyedProgenitor
		* GainItem

### Quest [qm_t3_sideHiigaran_C_1/Colonies: The Next Generation I]
**DESCRIPTION**:
	Lazarus has sent us some trainees to get some practical experience on our ship.

**GOALS**:
	* Task 1: 
		* GainItem
		* 2000 PlayerXP

### Quest [qm_t3_sideHiigaran_C_2/Colonies: The Next Generation II]
**DESCRIPTION**:
	Many of the trainees are going to become pilots and navigators, but have so far trained in controlled or virtual flight simulators. They need some real experience.

**GOALS**:
	* Task 1: 
		* Craft
		* UpgradeOfficer

### Quest [qm_t3_sideHiigaran_C_3/Colonies: The Next Generation III]
**DESCRIPTION**:
	The final course is the graduation level for the trainees, who must see actual combat. You are to take the crew into battle and complete the course. Once finished, they return to Lazarus to finish up their coursework.

**GOALS**:
	* Task 1: Complete 10 side missions
	* Task 2: UpgradeOfficer


## 29. chapter_main_t3_05/Blue Collar Work

### Quest [qm_t3_facIyatequa/Blue Collar Work]
**DESCRIPTION**:
	Ekekko informed us about exclusive work needed by the Iyatequa, and the traders will pay well for this assistance. This is below the table work on various jobs they don’t widely advertise for. They do not say what the ultimate purpose of this work is, though.

**GOALS**:
	* Task 1: Complete 2 of qm_t3_sideIyatequa_A_3|qm_t3_sideIyatequa_B_3|qm_t3_sideIyatequa_C_3
	* Task 2: Goto SARAAL system of Iyatequa's territories

### Quest [qm_t3_sideIyatequa_A_1/Contracts: The Empty Quarter I]
**DESCRIPTION**:
	A small world in the Empty Quarter is looking for trustworthy connections. They offer an assortment of various tasks.

**GOALS**:
	* Task 1: 
		* 7 Faction_Tr1_T3up
		* 2250 PlayerXP

### Quest [qm_t3_sideIyatequa_A_2/Contracts: The Empty Quarter II]
**DESCRIPTION**:
	A wealthy socialite has heard of our accomplishments and wants some things done. Discreetly, of course.

**GOALS**:
	* Task 1: 
		* 500 RepTr1
		* 1000 Refining3N_Refining3O_Refining3P_Refining3Q

### Quest [qm_t3_sideIyatequa_A_3/Contracts: The Empty Quarter III]
**DESCRIPTION**:
	Our contact in the Empty Quarter is looking for new opportunities and has been pleased with our work so far. They want us to scout out new areas of space in order to expand their influence.

**GOALS**:
	* Task 1: 
		* 8500 RepTr1
		* Scan

### Quest [qm_t3_sideIyatequa_B_1/Contracts: Territory Claim I]
**DESCRIPTION**:
	The Iyatequa plan to set up new trading routes in space currently riddled by pirates. They asked us to clean up the area.

**GOALS**:
	* Task 1: 
		* Scan
		* 35 ShipsDestroyedP1

### Quest [qm_t3_sideIyatequa_B_2/Contracts: Territory Claim II]
**DESCRIPTION**:
	Some pirates apparently didn't get the hint yet. We should show them the Iyatequa mean business.

**GOALS**:
	* Task 1: 
		* Complete 8 side missions
		* GainItem

### Quest [qm_t3_sideIyatequa_B_3/Contracts: Territory Claim III]
**DESCRIPTION**:
	Most pirates have dispersed, but just to make sure they do not come back we should increase our reputation so future raiders will think twice before setting up nests here.

**GOALS**:
	* Task 1: 
		* Complete 5 side missions
		* Complete 2 side missions

### Quest [qm_t3_sideIyatequa_C_1/Contracts: Supplies I]
**DESCRIPTION**:
	A local world wants help building and supplying a space station. We are asked to test possible mining sites and clear them of hostiles.

**GOALS**:
	* Task 1: 
		* 6000 Mined3A_Mined3B_Mined3C_Mined3D
		* 55 ShipsDestroyed

### Quest [qm_t3_sideIyatequa_C_2/Contracts: Supplies II]
**DESCRIPTION**:
	Mining ships have departed for the asteroids we have charted, but the internal systems require special gases. We are asked to sample the gases at promising jovians.

**GOALS**:
	* Task 1: 
		* 600 Mined3E_Mined3F_Mined3G_Mined3H
		* 100 Mined3H

### Quest [qm_t3_sideIyatequa_C_3/Contracts: Supplies III]
**DESCRIPTION**:
	The mining sites have been prepared, but the Iyatequa asked us with further assistance through supplies and mining craft.

**GOALS**:
	* Task 1: 
		* Pay 150 GU Type G Gas T3
		* Pay 300 RU Type B Refined T3
		* Pay 50 Small Hull Parts


## 30. chapter_main_t3_06/Sijin Lighthouse

### Quest [qm_t3_facCangacian/Roadblocks]
**DESCRIPTION**:
	Reports at the Tanoch border are coming in stating that the Fleet of Rams, Supay’s army, is on the move at last.

**GOALS**:
	* Task 1: Complete 2 of qm_t3_sideCangacian_A_3|qm_t3_sideCangacian_B_3|qm_t3_sideCangacian_C_3

### Quest [qm_t3_sideCangacian_A_1/Defense: Intercept I]
**DESCRIPTION**:
	We are asked to intercept as many Cangacian fleets as we can.

**GOALS**:
	* Task 1: 
		* 40 ShipsDestroyedP1
		* GainItem

### Quest [qm_t3_sideCangacian_A_2/Defense: Intercept II]
**DESCRIPTION**:
	The Cangacians continue to probe the Tanoch defenses. We should look for suspicious activity.

**GOALS**:
	* Task 1: 
		* Scan
		* Complete 9 side missions

### Quest [qm_t3_sideCangacian_A_3/Defense: Intercept III]
**DESCRIPTION**:
	Supay's fleets may have holdouts in systems we have not been looking yet. We should find those and flush them out.

**GOALS**:
	* Task 1: 
		* Complete 4 side missions
		* Scan

### Quest [qm_t3_sideCangacian_B_1/Defense: Assist I]
**DESCRIPTION**:
	To counter these attacks our crew must be well trained.

**GOALS**:
	* Task 1: 
		* GainItem
		* UpgradeOfficer

### Quest [qm_t3_sideCangacian_B_2/Defense: Assist II]
**DESCRIPTION**:
	Our crew is analyzing the attack patterns to find ways to predict where the Fleet of Rams may strike next.

**GOALS**:
	* Task 1: 
		* GainItem
		* 2500 PlayerXP

### Quest [qm_t3_sideCangacian_B_3/Defense: Assist III]
**DESCRIPTION**:
	Several smaller worlds on the border have sent us some of their recruits, in hopes they could get some practical experience from our battles with the Cangacians.

**GOALS**:
	* Task 1: Complete 10 side missions
	* Task 2: UpgradeOfficer

### Quest [qm_t3_sideCangacian_C_1/Defense: Barricade I]
**DESCRIPTION**:
	Several mining fleets of the border systems have taken losses and are asking us to provide them with safe locations to find resources.

**GOALS**:
	* Task 1: 
		* 80 ScannedBelt
		* 1500 Refining3N_Refining3O_Refining3P_Refining3Q

### Quest [qm_t3_sideCangacian_C_2/Defense: Barricade II]
**DESCRIPTION**:
	The remaining mining fleets are flocking to the new mining spots, but they require gases for advanced weaponry.

**GOALS**:
	* Task 1: 
		* 40 ScannedJovian
		* 750 Mined3E_Mined3F_Mined3G_Mined3H

### Quest [qm_t3_sideCangacian_C_3/Defense: Barricade III]
**DESCRIPTION**:
	The border worlds' new mining lanes are buzzing with activity, but they need supplies to build up defenses against future raids.

**GOALS**:
	* Task 1: 
		* Pay 20 Small Hull Parts
		* Pay 20 Small Weapon Parts
		* Pay 20 Small Machinery Parts

### Quest [qm_t3_sijinLighthouse/Sijin Lighthouse]
**DESCRIPTION**:
	We detected a possible signal from the missing Khar-Kalaad.

**GOALS**:
	* Task 1: Complete mission 'Sijin Lighthouse'

### Mission [story_D01_SijinLighthouse/Sijin Lighthouse]
**LOCATION:** SIJIN system, Tanoch territory
**FACTIONS INVOLVED:** Hiigaran Medea, Tanoch

## 31. chapter_main_t4_01/Iliyin Lighthouse

### Quest [qm_t4_researchJumpCap/Mind the Gap]
**DESCRIPTION**:
	Crossing the Nightmare Gulf requires an upgrade to our hyperjump technology. After some scans of the gate at Sijin Lighthouse, our scientists think they are able to make the leap possible.

**GOALS**:
	* Task 1: Craft

### Quest [qm_t4_iliyinLighthouse/Iliyin Lighthouse]
**DESCRIPTION**:
	We have arrived at another lighthouse in uncharted territory. Be prepared for anything.

**GOALS**:
	* Task 1: Complete mission 'Iliyin Lighthouse'

### Mission [story_D02_IliyinLighthouse/Iliyin Lighthouse]
**LOCATION:** ILIYIN system, Amassari territory
**FACTIONS INVOLVED:** Amassari, Hiigaran Medea
### Quest [qm_t4_amassariLiaison/Amassari Relations]
**DESCRIPTION**:
	The Amassari have opened their liaison office to us.

**GOALS**:
	* Task 1: 1000 RepAmassari

### Quest [qm_t4_moonResources/Crystals]
**DESCRIPTION**:
	Crystals are a new type of resource that can be combined with refined metals into a composite material needed for advanced constructions. So far we have only been able to find them by chance in .

**GOALS**:
	* Task 1: GainItem
	* Task 2: 100 Refining4V_Refining4W_Refining4X_Refining4Y


## 32. chapter_main_t4_02/Bright Temple

### Quest [qm_t4_brightTemple/Bright Temple]
**DESCRIPTION**:
	The Amassari here may contain answers about the nature of the Progenitor observer.

**GOALS**:
	* Task 1: Complete mission 'Bright Temple'

### Mission [story_D03_BrightTemple/Bright Temple]
**LOCATION:** CANSAGA system, Amassari territory
**FACTIONS INVOLVED:** Amassari, Hiigaran Kiithless, Hiigaran Medea
### Quest [qm_t4_postBrightTemple_1/Among the People]
**DESCRIPTION**:
	We should take this time to become better acquainted with the Amassari and their culture. Performing tasks for the assorted groups will accomplish this.

**GOALS**:
	* Task 1: 1000 RepAmassari

### Quest [qm_t4_postBrightTemple_2/Fabrication Methods]
**DESCRIPTION**:
	A new technique for refining was discovered from the Amassari. Test this process by refining rare earths.

**GOALS**:
	* Task 1: GainItem

### Quest [qm_t4_postBrightTemple_3/Experience and Knowledge]
**DESCRIPTION**:
	Our crews need a new round of training to become familiar with Amassari practices and tactics.

**GOALS**:
	* Task 1: GainItem

### Quest [qm_t4_hataldan/Hataldan]
**DESCRIPTION**:
	The fallen capital of the Amassari, and last known position of the Observer.

**GOALS**:
	* Task 1: Complete mission 'Hataldan'

### Mission [story_D04_Hataldan/Hataldan]
**LOCATION:** HATALDAN system, Amassari territory
**FACTIONS INVOLVED:** Amassari, Hiigaran Kiithless, Hiigaran Medea, Progenitor

## 33. chapter_main_t4_03/Nightmare Gulf

### Quest [qm_t4_postHataldan_1/The Hunt Begins]
**DESCRIPTION**:
	The search begins for Kidara and the stolen Observer. We must examine any objects we can find scattered around for clues about her whereabouts.

**GOALS**:
	* Task 1: Scan

### Quest [qm_t4_postHataldan_2/Forcible Interrogation]
**DESCRIPTION**:
	Destroying Kiithless ships and scavenging their databanks could fill some gaps in our intelligence about the Kiithless. The hunt continues!

**GOALS**:
	* Task 1: 50 ShipsDestroyedDarkHiigaranT4

### Quest [qm_t4_postHataldan_3/Pieces of the Puzzle]
**DESCRIPTION**:
	A cryptic clue that emerged from harvesting Kiithless vessels may have a solution if we can piece together a saga from the Hagthar Empire. Collect relics from these ancient people.

**GOALS**:
	* Task 1: GainItem

### Quest [qm_t4_nightmareGulf/Nightmare Gulf]
**DESCRIPTION**:
	The Hagthar knew of pockets and safe regions close to this massive interstellar storm. We now know the way to Kidara's hideout in The Nightmare Gulf. It's time to end this.

**GOALS**:
	* Task 1: Complete mission 'Nightmare Gulf'

### Mission [story_D05_NightmareGulf/Nightmare Gulf]
**LOCATION:** VENEE system, Amassari territory
**FACTIONS INVOLVED:** Amassari, Hiigaran Kiithless, Hiigaran Medea, Progenitor
### Quest [qm_t4_strikeNightmareGulf/Strike at Nightmare Gulf]
**DESCRIPTION**:
	The Hagthar knew of pockets and safe regions close to this massive interstellar storm. We now know the way to Kidara's hideout in The Nightmare Gulf. It's time to end this.

**GOALS**:
	* Task 1: Complete 1 of qr_023


## 34. chapter_main_t4_04/The Promised Place

### Quest [qm_t4_tanWin_DefendBase/Gesture of Aid]
**DESCRIPTION**:
	We received emergency communication from the Chicuat Elders. They anticipate a raid on one of their remote trading stations. Toci asks us to take on the defense in order to relieve the weakened and overextended Chicuat forces.

**GOALS**:
	* Task 1: Complete mission 'Repulse Raid T4'

### Mission [event_tanWin2023_DefendBase_t4/Repulse Raid T4]
**DESCRIPTION**: -
**LOCATION:** TEOZACOZ system, Tanoch territory
**FACTIONS INVOLVED:** Tanoch Chicuat, Tanoch Tecuban
		_e_tanWin2023_DefendBase_intro_
		**Joanna**
		Hyperspace jump completed. There's no sign of the raiders yet, we should take defensive positions.

		**Toci Citalicue**
		We're fortunate to make it in time. Today my people will be protected and we may learn more about our attackers as well.

		_e_tanWin2023_DefendBase_firstWave_
		**Joanna**
		There they are. Hostile units are on approach vectors. Prepare for contact!

		_e_tanWin2023_DefendBase_nextWave_
		**Joanna**
		Commander, another wave is approaching!

		_e_tanWin2023_DefendBase_stationLow_
		**Toci Citalicue**
		Commander, our station can't withstand much more of this. My people are dying, do something!

		_e_tanWin2023_DefendBase_win_
		**Joanna**
		The raid has failed, we've held the line. Salvage teams are already scanning the debris for anything of interest from the attacking ships.

		**Toci Citalicue**
		Commander, these vessels belong to the Tecuban. But why would they carry out raids against us? They've never been this desperate.

		**Joanna**
		What are the Tecuban? Are they a people like the Chicuat, subjects of the Empire?

		**Toci Citalicue**
		Yes. Like us, they are a people who live within the Empire. But they have never been openly hostile to us or any other. Perhaps they are taking advantage of the recent chaos?

		**Joanna**
		Commander, we can't repel these raids forever. Like it or not, we'll need to get more involved in this internal dispute within the Empire.

		_e_tanWin2023_DefendBase_fail_
		**Joanna**
		Commander, the station just disintegrated. We've failed... we must withdraw.

### Quest [qm_t4_tanWin_AttackBase/In the Shadows]
**DESCRIPTION**:
	Intelligence from the Chicuat points to a Tecuban base operating around an uninhabited planet. We must go there and eliminate this base to stop the raids.

**GOALS**:
	* Task 1: Complete mission 'Base Busting T4'

### Mission [event_tanWin2023_AttackBase_t4/Base Busting T4]
**DESCRIPTION**: -
**LOCATION:** ACATLA system, Tanoch territory
**FACTIONS INVOLVED:** Tanoch Tecuban, Vaygr
		_e_tanWin2023_AttackBase_intro_
		**Joanna**
		We've found the base. It's active with many hostiles in the area. We're outnumbered, but if we engage carefully we can maximize the element of surprise.

		**Toci Citalicue**
		This base is larger than I expected, which is troubling. Wipe it from this system to send a message. These raids will no longer be tolerated!

		_e_tanWin2023_AttackBase_alert_
		**Joanna**
		Commander, we're being illuminated by active targeting. Hostile craft approaching.

		_e_tanWin2023_AttackBase_wave_
		**Joanna**
		More enemy craft emerging from hyperspace.

		_e_tanWin2023_AttackBase_boss_
		**Joanna**
		More enemies... strange... are that Vaygr craft? What are they doing here?

		_e_tanWin2023_AttackBase_vaygr_
		**Vaygr Commander**
		Hiigarans! Eliminate them immediately, there must be no witnesses!

		_e_tanWin2023_AttackBase_win_
		**Joanna**
		All threats neutralized. There was no sign of Heyoka, but the Vaygr appearing here raises a lot of questions.

		**Toci Citalicue**
		Who are these Vaygr? I have heard of the name, but nothing more.

		**Joanna**
		The Vaygr are enemies of ours from a war almost two decades ago. Somehow they're here in Nimbus too.

		**Toci Citalicue**
		So the Tecuban have allied with these Vaygr to pillage my people? This... this is worse than I imagined.

		**Joanna**
		You have powerful allies now as well. If the Vaygr are involved, this is our fight too. Together we'll get to the bottom of this.

### Quest [qm_t4_tanWin_Relic/Attack the Vaygr]
**DESCRIPTION**:
	In our search for the Vaygr involved with the Tecuban, we aquired one of their communication frequencies. If we contact the Vaygr now, we should be able to trace their signal and hyper jump to their exact location.

**GOALS**:
	* Task 1: Complete mission 'Destination T4'

### Mission [event_tanWin2023_Relic_t4/Destination T4]
**DESCRIPTION**: -
**LOCATION:** CUILCO system, Tanoch territory
**FACTIONS INVOLVED:** Vaygr
		_e_tanWin2023_Relic_intro_
		**Joanna**
		Commander, the Vaygr are ahead. They appear to be patrolling a Progenitor artifact.

		**Toci Citalicue**
		Why are these Vaygr interested in objects from the Makers?

		**Joanna**
		To fulfill an ancient prophecy, originally. Like us the Vaygr understand how to use these ancient devices.

		_e_tanWin2023_Relic_contact_
		**Vaygr Commander**
		Hiigarans! You are meddling in affairs that are not of your business. May death be your reward!

		_e_tanWin2023_Relic_wave_
		**Joanna**
		More Vaygr are emerging from hyperspace, Commander.

		_e_tanWin2023_Relic_boss_
		**Vaygr Commander**
		You are far from home, Hiigarans! You will die here forgotten!

		_e_tanWin2023_Relic_boss_low_
		**Vaygr Commander**
		Curse you, Hiigarans! You will never spoil the plans of Jochik Kaan, heir to the rightful Saju-ka!

		_e_tanWin2023_Relic_win_
		**Joanna**
		All hostiles defeated. So Jochik Kaan is pulling the strings in this conflict. He must have some deeper plan here for the Vaygr to be this involved.

		**Toci Citalicue**
		Yet another ruthless leader behind the attacks upon my people? It is not enough for the Tecuban to turn against us?

		**Joanna**
		We must discover what Jochik Kaan is trying to achieve here. Once we do, we'll put a stop to it.

### Quest [qm_t4_tanWin_Academy/Showdown at the Academy]
**DESCRIPTION**:
	We finally learned Jochik Kaan's intentions. He sparked the flames of war to weaken the Chicuat defenses and steal the Baetyl from Tlapallan Academy, one of their key centers of learning. We must travel there at once, before it is too late.

**GOALS**:
	* Task 1: Complete mission 'Tlapallan Academy T4'

### Mission [event_tanWin2023_Academy_t4/Tlapallan Academy T4]
**DESCRIPTION**: -
**LOCATION:** TOCHTEOP system, Tanoch territory
**FACTIONS INVOLVED:** Tanoch Chicuat, Tanoch Tecuban, Vaygr
		_e_tanWin2023_Academy_intro_
		**Joanna**
		Commander, the Vaygr are already in-system. Are we too late?

		_e_tanWin2023_Academy_heyoka_
		**Jochik Kaan**
		You've obstructed my plans for the last time, Heyoka! I have no use for disobedient fools!

		_e_tanWin2023_Academy_situation_
		**Toci Citalicue**
		The Vaygr are attacking the Tecuban? What is happening?

		_e_tanWin2023_Academy_hiigarans_
		**Vaygr Commander**
		My lord, the Hiigarans have arrived. They are approaching for battle.

		_e_tanWin2023_Academy_combat_
		**Jochik Kaan**
		All my enemies have gathered... no matter. We will crush them all and take what we came for.

		_e_tanWin2023_Academy_jochikDownA_
		**Jochik Kaan**
		Reposition the flagship. Deploy the reserves. Destroy the Hiigarans!

		_e_tanWin2023_Academy_JochikReturn_
		**Joanna**
		Jochik has returned. All forces, engage his ship immediately!

		_e_tanWin2023_Academy_academyLow_
		**Toci Citalicue**
		The Academy is under attack! Commander, do something!

		_e_tanWin2023_Academy_tepin_
		**Tepin Papan**
		Commander, I've come to assist you! Our people shall not fail today!

		_e_tanWin2023_Academy_jochikDownB_
		**Jochik Kaan**
		Savor your insignificant victory today, Hiigarans! I will crush you the next time we meet. Consider that a promise.

		_e_tanWin2023_Academy_win_
		**Toci Citalicue**
		The Tlapallan Academy is safe. My people are protected and our enemies are on the run... I can't believe we prevailed.

		**Tepin Papan**
		The Tecuban have retreated. It seems Heyoka tried to get to the relic before Jochik did, and paid the price.

		**Toci Citalicue**
		His greed brought him to pillage the future of my people for his own gratification. I don't mourn his death.

		**Tepin Papan**
		Our people are safe for now, but the Chicuat need a voice to speak on their behalf among our allies. Toci, you could be that voice among the Hiigarans.

		**Joanna**
		We would be grateful to have you aboard, Toci. Your people are always welcome among us.

		_e_tanWin2023_Academy_failTepin_
		**Joanna**
		Tepin Papan's vessel was destroyed. We can't stop Jochik. All ships, retreat immediately!

		_e_tanWin2023_Academy_failAcademy_
		**Joanna**
		The Academy has fallen... we can't stop Jochik. All ships, retreat immediately!

### Quest [qm_t4_yaoSpr_Conjunction/The Promised Place]
**DESCRIPTION**:
	Chocoan has provided the coordinates to the next astral conjunction event. Strong hostile forces are to be expected in this system. Our goal is to both protect the civilian pilgrims and find out more about the suspected secret agenda of the Yaot Elders.

**GOALS**:
	* Task 1: Complete mission 'Conjunction T4'

### Mission [event_yaoSpr2024_Conjunction_t4/Conjunction T4]
**DESCRIPTION**: -
**LOCATION:** ZE TAVAAN system, Cangacian territory
**FACTIONS INVOLVED:** Cangacian, Yaot
		_e_yaoSpr2024_Conjunction_intro_
		**Chocoan Coatl**
		Blessings, Hiigarans The People are relieved that you are here. The pilgrimage will begin moving to the conjunction point.

		**Joanna**
		Greetings. We are ready to assist the convoy. All ships on full alert, keep your eye out for incoming pirates.

		_e_yaoSpr2024_Conjunction_interlude_
		**Chocoan Coatl**
		Behold the splendor of the Maker's works. We are blessed that they have lasted this long after the cataclysm. Truly a timeless wonder.

		_e_yaoSpr2024_Conjunction_arrival_
		**Chocoan Coatl**
		More pilgrim ships have arrived to see the conjuction. Bless the Makers.

		_e_yaoSpr2024_Conjunction_conjunctionA_
		**Chocoan Coatl**
		The Conjunction is the clearest sign that our Makers were powerful and wise. The messages they left in the alignment of the stars are profound, even if their exact meaning is lost.

		_e_yaoSpr2024_Conjunction_conjunctionB_
		**Chocoan Coatl**
		Though there are signs and portents of a great change coming, there is hope also in this change. Yes there is uncertainty, but the signs point to a great relief.

		_e_yaoSpr2024_Conjunction_deviation_
		**Joanna**
		Chocoan what's going on? You're deviating from the path! We must protect the perimeter.

		**Chocoan Coatl**
		It must be done. Our ways are... not to be questioned by outsiders. Please, maintain defensive positions.

		_e_yaoSpr2024_Conjunction_attackA_
		**Joanna**
		Hostiles incoming. Protect the pilgrims. Intercept the attackers!

		_e_yaoSpr2024_Conjunction_attackB_
		**Joanna**
		More attacks incoming. Chocoan, we need your help here!

		**Chocoan Coatl**
		I... please... I can't.

		_e_yaoSpr2024_Conjunction_catequil_
		**Catequil**
		So we meet again, Hiigarans. You won't stop me this time. I'll have that treasure, even if I have to rip it out of every ship I see! Do not let any of them escape!

		_e_yaoSpr2024_Conjunction_change_
		**Joanna**
		More hostile incoming. Chocoan, what the hell is going on? We need your help or civilians will die!

		**Chocoan Coatl**
		I... I cannot... do this any longer. We are coming to your aid, and to the hells with the Elders and their ambition!

		_e_yaoSpr2024_Conjunction_catequilLow_
		**Catequil**
		You won't always be so fortunate Hiigarans! A thousand curses upon you and your works!

		_e_yaoSpr2024_Conjunction_win_
		**Joanna**
		Perimeter is clear. The attack is over. The pilgrims are safe.

		**Chocoan Coatl**
		Under the grace of the Makers, the pilgrims are safe with minimal casualties. Thank you, Commander.

		_e_yaoSpr2024_Conjunction_end_
		**Joanna**
		Chocoan, what was going on back there?

		**Chocoan Coatl**
		I can only confess. Our Elders pervert these pilgrimages with their own causes and ambitions. We rake the ruins of the Makers, scoop them into our hulls, for some reason.

		**Joanna**
		They're looking for some Progenitor technology in those asteroids, aren't they?

		**Chocoan Coatl**
		It would seem to be so. The Elders will surely take retribution for my failure, so I am without a place for I surely cannot return. I am no longer Envoy, or shephard, of my people.

		**Joanna**
		You are always welcome among us, Chocoan. The warmth you showed your people could be a great asset to us as an envoy to the Yaot in the future.

		_e_yaoSpr2024_Conjunction_fail_
		**Joanna**
		Commander, we have Pilgrim ships going down. Critical mission failure. Abort immediately.

