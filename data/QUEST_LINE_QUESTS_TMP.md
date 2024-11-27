# HWM QUESTLINES WITH QUESTS


## ql_main_t0_tutorial

### qm_t0_tutMissions: Landing
Our arrival in this galaxy was met with tragedy.
	* Type:	Main
	* CinematicIds:	20:10:25
	* FollowUps:	ql_main_t0_station
	* Goals:	CompleteMission,0, CompleteMission,1, CompleteMission,2
	* GoalParameters:	Ids&story_A01_DuzumiGate|story_A01_DuzumiGateTut, Id&story_A02_WiracodaGate, Id&story_A03_GulfTaln

## ql_main_t0_station

### qm_t0_introStation: Lazarus Station
We were given the coordinates of a local Hiigaran settlement. We should go there.
	* Type:	Main
	* Goals:	Goto,0
	* GoalParameters:	Target&[-1822, -636];TargetMode&Station

### qm_t0_introMarket: Local Currency
The market can be accessed at stations and inside the flagship, though the selection of items in the flagship market is smaller. For now, we need to pick up some local currency to barter with the locals.
	* Type:	Main
	* FollowUps:	ql_main_t0_strikeCraft
	* Goals:	Buy,0
	* GoalParameters:	Id&pack_market_freeHC_insta

## ql_main_t0_strikeCraft

### qm_t0_introFabricator: Fabricator
Our fabricators are operational again. We should produce more strike craft in case we run into more hostiles.
	* Type:	Main
	* Goals:	Craft,0
	* GoalParameters:	Category&Crafting;Tags&Interceptor;Amount&1

### qm_t0_introEquipStrikecraft: Strike Craft
We need to ready our strike craft inside our hangars.
	* Type:	Main
	* FollowUps:	ql_main_t0_v2_signals
	* Goals:	Equip,0
	* GoalParameters:	Type&Squad

## ql_main_t0_v2_signals

### qm_t0_v2_introScanning: Scanning
We have been asked to take care of a local threat to the Lazarus Station. We need to find out where it is.
	* Type:	Main
	* Goals:	Scan,0, Scan,1
	* GoalParameters:	Tags&InSystem_Generated;Amount&1, Tags&InSystem_Generated;Amount&1;Analyzed&True

### qm_t0_v2_introSignals: Signals
We have found hostile signals in the system. We need to clear it out and return to Lazarus Station.
	* Type:	Main
	* FollowUps:	ql_main_t0_mining
	* Goals:	CompleteMission,0, Goto,1
	* GoalParameters:	Mode&Generated;Amount&1, Target&[-1822, -636];TargetMode&Station

## ql_main_t0_mining

### qm_t0_introScanBelts: Asteroid Clusters
We've been asked by Lazarus Station to help with resource scarcity. We'll need to find suitable mining opportunities by scanning for mineral-rich asteroids in nearby systems.
	* Type:	Main
	* Goals:	Goto,0, Statistic,1
	* GoalParameters:	Target&[-1747, -653], Id&ScannedBelt;Total&1

### qm_t0_introMining: Mining
We found a suitable spot for mining. Use the resource collector to mine the mineral rich asteroids.
	* Type:	Main
	* FollowUps:	ql_main_t0_support
	* Goals:	Statistic,0
	* GoalParameters:	Id&Mined0A;Amount&50

## ql_main_t0_support

### qm_t0_support: Support
Now that we have the needed minerals, we should go back to Lazarus Station to deliver them.
	* Type:	Main
	* FollowUps:	ql_main_t0_officer
	* Goals:	Pay,0
	* GoalParameters:	Id&0A;Amount&25;SysId&[-1822, -636];Mode&Station

## ql_main_t0_officer

### qm_t0_introBridge: Bridge
Gideon S'jet has offered his Progenitor expertise. We should appoint him as head of science on the bridge.
	* Type:	Main
	* FollowUps:	ql_main_t0_escorts
	* Goals:	Equip,0
	* GoalParameters:	Type&Officer;Location&Bridge

## ql_main_t0_escorts

### qm_t0_introShipyard: Shipyard
We have clearance to use the shipyards of Lazarus Station. We should build an additional assault frigate there to bolster our fleet.
	* Type:	Main
	* Goals:	Craft,0
	* GoalParameters:	Category&Crafting;Tags&AssaultFrigate;Amount&1

### qm_t0_introEquipEscorts: Escort Ships
Our new assault frigate needs to be staffed and readied. We can do that at any station through Fleet Configuration.
	* Type:	Main
	* FollowUps:	ql_main_t0_sideProg
	* Goals:	Equip,0
	* GoalParameters:	Type&Escort

## ql_main_t0_sideProg

### qm_t0_scientist_Baaekh_A: Baaekh S’jet
Baaekh S’jet was one of the foremost scientists on Progenitor culture. According to Gideon she has data that can help us with our own research into the Progenitors.
	* Type:	Main
	* Goals:	Goto,0, Goto,1, Statistic,2, Statistic,2
	* GoalParameters:	Target&[-1785, -690], Target&[-1844, -690], Id&ScannedBelt;Total&4, Id&ScannedGenerated;Amount&1

### qm_t0_scientist_Baaekh_B: Rescue Mission
We found Baaekh S'jet, but she can't come out of hiding until we have distracted the hostiles in the area.
	* Type:	Main
	* FollowUps:	ql_main_t0_relic
	* Goals:	CompleteMission,0, Goto,1
	* GoalParameters:	Mode&Generated;Amount&1, Target&[-1785, -690]

## ql_main_t0_relic

### qm_t0_relic: Relic Retrieval
With information provided by Baaekh S’jet, we now know a potential location of a Progenitor Relic in Toasiim that must be retrieved.
	* Type:	Main
	* FollowUps:	ql_main_t0_moreMining
	* Goals:	Goto,0, Scan,1, CompleteMission, 2
	* GoalParameters:	Target&[-1832, -619], Tags&InSystem;Amount&1, Id&story_A04_RelicSignature

## ql_main_t0_moreMining

### qm_t0_scientist_Hyeaa_A: Hyeaa Somtaaw
Hyeaa Somtaaw was an expert in Progenitor Materials sciences. He has established an independent lab at Nokuuna. According to Gideon, he has data that can help us with our own research into the Progenitors.
	* Type:	Main
	* FollowUps:	ql_main_t0_jolja
	* Goals:	Goto,0, Craft,1, Equip,2, Statistic,3
	* GoalParameters:	Target&[-1800, -623], Category&Crafting;Tags&RCol;Amount&1, Type&Squad;Tags&RCol, Id&Mined0A;Amount&225

## no_ql

### qm_t0_scientist_Hyeaa_B: Process Investigation
Hyeaa Somtaaw wants to investigate our fabrication processes, find a way to improve it by incorporating Progenitor technology. In return he will share his data with us.
	* Type:	Main
	* Goals:	Craft,0, Craft,0, Craft,0, Craft,1
	* GoalParameters:	Category&Crafting;Tags&RCol;Amount&1, Category&Crafting;Tags&PlasmaBomber;Amount&1, Category&Crafting;Tags&Interceptor;Amount&1, Category&Crafting;Tags&Frigate;Amount&1

### qm_t1_facHiigaran_A: Outposts: Rescue
Long-range sensors located near another hyperspace gate have registered the presence of a Hiigaran fleet that emerged here. We are asked to this location and try to help any survivors as best as we can.
	* Type:	Side
	* Goals:	Goto,0, Statistic,1, CompleteMission,1, Pay,2
	* GoalParameters:	Target&[-1558, -672], Id&ScannedGenerated;Amount&3, Mode&Generated;Amount&3, Id&1A;Amount&500

### qm_t1_facHiigaran_B: Outposts: Recon
To supply the needs of the Hiigaran fleet, we've been dispatched to look for a great mining source. Intel indicates this will put us into direct conflict with the Fleet of Rams.
	* Type:	Side
	* Goals:	Goto,0, Statistic,1, Statistic,2, Statistic,2, Goto,3
	* GoalParameters:	Target&[-1429, -553], Id&ScannedBelt;Total&10, Ids&Mined1A_Mined1B_Mined1C;Amount&500, Id&ShipsDestroyed;Amount&15, Target&[-1429, -553]

### qm_t1_facHiigaran_C: Outposts: Wall of Will
One of the only planetary settlements under Hiigaran control has been scouted by the Fleet of Rams. Until the planetary defenses are strengthened, they need military equipment to supply the defense.
	* Type:	Side
	* Goals:	Goto,0, Statistic,1, Pay,2, Pay,3, Pay,4
	* GoalParameters:	Target&[-1552, -610], Id&Mined1A;Amount&500, Id&1A;Amount&150, Id&hgn_su_rcol_01_t0;Amount&3, Id&hgn_sf_intc_01_t0;Amount&1

### qm_t1_facHiigaran_D: Outposts: Security
Hiigaran forces are working to clear systems to set up for colonization. The system in question is of special importance. We've been asked to go there and assist in securing the area.
	* Type:	Side
	* Goals:	Goto,0, Scan,1, Statistic,2, CompleteMission,2, Goto,3
	* GoalParameters:	Target&[-1525, -731], Tags&InSystem;Amount&3;Analyzed&True, Id&ShipsDestroyed;Amount&15, Mode&Generated;Amount&3, Target&[-1525, -731]

### qm_t1_facCangacian_A: Troubles: Defiance
The world of Huaca is looking for help. They are opposing conscription from Supay’s Fleet of Rams, the punishment of which is brutal assault.
	* Type:	Side
	* Goals:	Goto,0, Statistic,1, Statistic,2, Statistic,2, Goto,3
	* GoalParameters:	Target&[-1376, -709], Id&ShipsDestroyedP1;Amount&15, Ids&Mined1A_Mined1B_Mined1C;Amount&1000, Ids&Refining1N_Refining1O_Refining1P;Amount&500, Target&[-1376, -709]

### qm_t1_facCangacian_B: Troubles: Seeker
To oppose the Fleet of Rams, we were asked to undergo a mission to survey and map one of their three largest systems. We should also sabotage their efforts when the opportunity presents itself.
	* Type:	Side
	* Goals:	Goto,0, Statistic,1, CompleteMission,1, Statistic,1, Goto,2
	* GoalParameters:	Target&[-1497, -628], Id&ScannedGenerated;Amount&4, Mode&Generated;Amount&4, Id&ShipsDestroyedP1;Amount&15, Target&[-1497, -628]

### qm_t1_facCangacian_C: Troubles: Stone Hearth
We're asked to to assist the system of Acheron. They do not have a refinery set up, so we need to go there and refine metals for their construction facilities to use.
	* Type:	Side
	* Goals:	Goto,0, Statistic,1, Statistic,2, Statistic,2, Pay,3
	* GoalParameters:	Target&[-1793, -424], Id&ScannedBelt;Total&15, Id&Mined1A;Amount&1000, Id&Refining1N;Amount&500, Id&1N;Amount&300

### qm_t1_facCangacian_D: Troubles: A Black Eye
The Fleet of Rams is assembling an assault force that is aimed at a cluster of neutral systems. Intel shows that another Cangacian band plans to engage Supay’s commanding lieutenant here. We're asked to create a distraction to weaken the Fleet of Rams in the resulting battle.
	* Type:	Side
	* Goals:	Goto,0, Scan,1, Pay,2, CompleteMission,3, Goto,4
	* GoalParameters:	Target&[-1752, -861], Tags&InSystem;Amount&2;Analyzed&True, Id&hgn_sf_intc_01_t1;Amount&1, Mode&Generated;Amount&4, Target&[-1752, -861]

### qm_t1_facProgenitors_A: Components: A Wide Exchange
A few locals in this system have Progenitor technology they willing to hand to us if we agree to help them with their own problems regarding hostile Progenitor vessels and shortage of resources.
	* Type:	Side
	* Goals:	Goto,0, Statistic,1, Statistic,1, Statistic,1, Goto,2
	* GoalParameters:	Target&[-1497, -628], Id&ShipsDestroyedProgenitor;Amount&10, Ids&Mined1A_Mined1B_Mined1C;Amount&3000, Ids&Refining1N_Refining1O_Refining1P;Amount&1500, Target&[-1497, -628]

### qm_t1_facProgenitors_B: Components: Hunt
Progenitor vessels in this area are equipped with M-type fuses. We need to attack and destroy a few vessels in order to gather enough of quality for use in the prototype.
	* Type:	Side
	* Goals:	Goto,0, Statistic,1, Craft,1, CompleteMission,1, Goto,2
	* GoalParameters:	Target&[-1376, -709], Id&ScannedGenerated;Amount&5, Category&Upgrade;Tags&Weapon_Module;Amount&1, Mode&Generated;Amount&5;Tier&1, Target&[-1376, -709]

### qm_t1_facProgenitors_C: Components: A Full Quiver
Fleet command out of Lazarus frowns upon commanders that delve into Progenitor ruins without a minimum of protection. We need to bring our ship up to code and command will approve our ship for such operations in the future.
	* Type:	Side
	* Goals:	Goto,0, GainItem,1, Craft,2, CompleteMission,3, Goto,4
	* GoalParameters:	Target&[-1543, -626], Id&AA;Amount&30;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash, Category&Upgrade;Tags&Weapon_Module;Amount&2, Mode&Generated;Amount&5;Tier&1, Target&[-1543, -626]

### qm_t1_facProgenitors_D: Components: Repurpose the Past
To save time, rather than reconstruct a Particle density array, we can salvage one from advanced Progenitor craft. We need to attack enough Progenitor ships to find one that is in decent condition. The module will require rare earths in order to activate properly. We can gather them at the system as well.
	* Type:	Side
	* Goals:	Goto,0, Statistic,1, GainItem,2, Statistic,2, Goto,3
	* GoalParameters:	Target&[-1793, -424], Id&ScannedBelt;Total&20, Id&AB;Amount&10;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash, Id&ShipsDestroyedProgenitor;Amount&10, Target&[-1793, -424]

### qm_t1_facIyatequa_A: Business: An Honest Job
The Iyatequa asked us to perform a variety of simple activities and allowing them to monitor the related systems for their own research purposes.
	* Type:	Side
	* Goals:	Goto,0, Statistic,1, GainItem,1, Craft,1, Goto,2
	* GoalParameters:	Target&[-1825, -480], Ids&Mined1A_Mined1B_Mined1C;Amount&3000, Tags&RareEarth;Amount&60;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash, Category&Upgrade;Tags&Weapon_Module;Amount&2, Target&[-1825, -480]

### qm_t1_facIyatequa_B: Business: The Barrier
We've been told to deal with an attempted trade blockade set up by pirates. We will need to get some spare resources and some module upgrades before we face the enemy.
	* Type:	Side
	* Goals:	Goto,0, Statistic,1, Craft,1, Statistic,2, Goto,3
	* GoalParameters:	Target&[-1525, -731], Ids&Refining1N_Refining1O_Refining1P;Amount&1500, Category&Upgrade;Tags&Weapon_Module;Amount&1, Id&ShipsDestroyed;Amount&25, Target&[-1525, -731]

### qm_t1_facIyatequa_C: Business: The Sheriff
Hostiles have been gathering near Iyatequa trading routes. We've been asked to investigate and root out pirates and other undesirables.
	* Type:	Side
	* Goals:	Goto,0, Scan,1, CompleteMission,1, Statistic,1, Goto,2
	* GoalParameters:	Target&[-1429, -553], Tags&InSystem;Amount&5;Analyzed&True, Mode&Generated;Amount&5;Tier&1, Id&ShipsDestroyed;Amount&25, Target&[-1429, -553]

### qm_t1_facIyatequa_D: Business: The Dealer
A dealer supplying the Iyatequa has tried cutting corners and incured their wrath. We've been asked to apprehend him.
	* Type:	Side
	* Goals:	Goto,0, Goto,1, Scan,2, CompleteMission,2, Pay,3, Goto,4
	* GoalParameters:	Target&[-1552, -610], Target&[-1558, -672], Tags&InSystem;Amount&5;Analyzed&True, Mode&Generated;Amount&5;Tier&1, Id&1O;Amount&1000, Target&[-1552, -610]

### qm_t2_facCangacian_A: Incursion: Reverse Engineering
This colony was attacked by vessels incorporating non-Cangacian technology. We're asked to try to reverse engineer some of it.
	* Type:	Side
	* Goals:	Goto,0, Statistic,1, GainItem,2, Craft,3, Goto,4
	* GoalParameters:	Target&[-1491, -596], Id&ShipsDestroyed;Amount&35, Id&RP;Amount&45;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash, Tags&Research;Amount&1, Target&[-1491, -596]

### qm_t2_facCangacian_B: Incursion: Rebuilding Efforts
This colony was hit hard. We need to clear the area of remaining pirates and help with rebuilding.
	* Type:	Side
	* Goals:	Goto,0, CompleteMission,1, Pay,2, Pay,2, Pay,2, GainItem,3, Goto,4
	* GoalParameters:	Target&[-1643, -552], Mode&Generated;Amount&10;Tier&1, Id&2A;Amount&650, Id&2B;Amount&650, Id&2C;Amount&650, Id&RP;Amount&45;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash, Target&[-1643, -552]

### qm_t2_facCangacian_C: Incursion: Enemy Intentions
This colony repelled the attackers and gathered some intel. They need our help to decrypt it and find safe places for mining.
	* Type:	Side
	* Goals:	Goto,0, GainItem,1, Statistic,2, Statistic,2, Goto,3
	* GoalParameters:	Target&[-1784, -564], Id&RP;Amount&45;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash, Id&ScannedBelt;Total&30, Id&ShipsDestroyed;Amount&35, Target&[-1784, -564]

### qm_t2_facCangacian_D: Incursion: Preemptive Strike
The most recent attack. Intel shows it was just a scouting mission. We need to help with setting up quick defenses and take out the assault fleet before they can strike.
	* Type:	Side
	* Goals:	Goto,0, Pay,1, Statistic,2, CompleteMission,2, Goto,3
	* GoalParameters:	Target&[-1559, -788], Id&2O;Amount&1000, Id&ScannedGenerated;Amount&10, Mode&Generated;Amount&10;Tier&1, Target&[-1559, -788]

### qm_t2_facHiigaran_A: Repairs: Mining Opportunities
To repair Lazarus Station, new minerals are needed. We are asked to look for new places to mine and help set up the fabrication systems.
	* Type:	Side
	* Goals:	Goto,0, Scan,1, Craft,2, Pay,3
	* GoalParameters:	Target&[-1784, -564], Tags&InSystem_T2up;Amount&5;Analyzed&True, Category&Crafting;Tags&Part;Amount&450, Id&2P;Amount&1000

### qm_t2_facHiigaran_B: Repairs: Secure the Perimeter
After the recent attack, we need to secure the borders of Hiigaran space.
	* Type:	Side
	* Goals:	Goto,0, CompleteMission,1, Craft,2, Pay,3
	* GoalParameters:	Target&[-1659, -561], Mode&Generated;Amount&10;Tier&1, Category&Crafting;Tags&Part;Amount&180, Id&intmed_ship_small_t2;Amount&60

### qm_t2_facHiigaran_C: Repairs: Motivation Boost
We are asked to lead several high profile campaigns against enemy forces to rally more Hiigaran fleets and raise awareness to the rebuilding efforts of Lazarus Station.

(The blueprints for small Weapon and Machinery parts can be found in the market.)
	* Type:	Side
	* Goals:	Goto,0, CompleteMission,1, Statistic,1, Pay,2
	* GoalParameters:	Target&[-1491, -596], Mode&Strike;Amount&1, Id&ShipsDestroyed;Amount&35, Id&intmed_weapon_small_t2;Amount&60

### qm_t2_facHiigaran_D: Repairs: Empty the Lairs
The attackers still have their bases of operation. We need to clear them out to prevent future attacks.
	* Type:	Side
	* Goals:	Goto,0, Statistic,1, Statistic,1, Pay,2, Pay,2, Pay,2
	* GoalParameters:	Target&[-1780, -457], Id&ScannedBelt;Total&35, Id&ShipsDestroyed;Amount&35, Id&2A;Amount&650, Id&2B;Amount&650, Id&2C;Amount&650

### qm_t2_facIyatequa_A: Intermediary: Delivery Run
The Iyatequa want us to deliver some resources - from our own pockets. They said the rewards will compensate for our losses. We'll see.
	* Type:	Side
	* Goals:	Goto,0, Pay,1, Pay,1, Pay,1, CompleteQuest,2, Goto,3
	* GoalParameters:	Target&[-1643, -552], Id&2O;Amount&1000, Id&2P;Amount&1000, Id&intmed_ship_large_t2;Amount&20, Amount&7;Tags&Faction_Tr1_T2up, Target&[-1643, -552]

### qm_t2_facIyatequa_B: Intermediary: Patrolling Trade Routes
We're asked to patrol the Iyatequa trading routes and clear out hostiles near them.
	* Type:	Side
	* Goals:	Goto,0, Statistic,1, CompleteQuest,2, Goto,3
	* GoalParameters:	Target&[-1659, -561], Id&ShipsDestroyedProgenitor;Amount&15, Amount&15;Tags&Faction_Tr1_T2up, Target&[-1659, -561]

### qm_t2_facIyatequa_C: Intermediary: The Catch
This assignment seems simple enough. We simply have to find Cangacian fleets and destroy them.
	* Type:	Side
	* Goals:	Goto,0, Statistic,1, Statistic,2, CompleteQuest,2, Goto,3
	* GoalParameters:	Target&[-1780, -457], Id&ShipsDestroyedP1;Amount&30, Id&ShipsDestroyed;Amount&30, Amount&7;Tags&Faction_Tr1_T2up, Target&[-1780, -457]

### qm_t2_facIyatequa_D: Intermediary: Art of Escape
The Iyatequa want us to find a master thief of legendary reputation.
	* Type:	Side
	* Goals:	Goto,0, Scan,1, GainItem,2, Pay,3, Pay,3, Goto,4
	* GoalParameters:	Target&[-1559, -788], Tags&InSystem_T2up;Amount&10;Analyzed&True, Id&RP;Amount&45;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash, Id&hgn_su_rcol_01_t2;Amount&1, Id&2D;Amount&500, Target&[-1559, -788]

### qm_t2_internalRefinery: Refinery Module
Additional refinery and fabricator modules increase our economic power.
	* Type:	Main
	* Goals:	Craft,0, Equip,1
	* GoalParameters:	Tags&Refining_Factory, Type&Internal;Tags&Refining_Factory

### qm_t2_facTanoch_A: Errands: Golden Harvest
A Tanoch planetary government is experiencing a resource shortfall, and has asked for help with procuring raw material.
	* Type:	Side
	* Goals:	Statistic,0, Pay,1, Pay,1, Pay,1
	* GoalParameters:	Id&ScannedBelt;Total&40, Id&2N;Amount&350, Id&2O;Amount&350, Id&2P;Amount&350

### qm_t2_facTanoch_B: Errands: Safety and Security
Pirates are attacking Tanoch systems. We've been asked to drive them back.
	* Type:	Side
	* Goals:	Statistic,0, Statistic,0
	* GoalParameters:	Id&RepTanoch;Amount&350, Id&ShipsDestroyedP1;Amount&15

### qm_t2_facTanoch_C: Errands: Disaster Relief
A Tanoch world is having trouble getting resources from the Empire so they’ve asked anyone for help.
	* Type:	Side
	* Goals:	Craft,0, Craft,0, Pay,1, Pay,1, Pay,1
	* GoalParameters:	Category&Refining;Amount&2000;Tags&T2, Category&Crafting;Tags&Part;Amount&150, Id&2O;Amount&350, Id&intmed_module_small_t2;Amount&50, Id&hgn_su_rcol_01_t2;Amount&1

### qm_t2_facTanoch_D: Errands: Hired Defenses
The border worlds are being threatened from Yaot assaults and are desperate for defenders. They ask us to drive the Yaot back.
	* Type:	Side
	* Goals:	Scan,0, Statistic,0
	* GoalParameters:	Tags&InSystem_Generated_T2up;Amount&10;Analyzed&True, Id&ShipsDestroyedYaot;Amount&15

### qm_t2_facYaot_A: Conflict: Direct Attack
The Tanoch want us to actively engage the Yaot fleets to disrupt their activities in Tanoch space.
	* Type:	Side
	* Goals:	Statistic,0
	* GoalParameters:	Id&ShipsDestroyedYaot;Amount&30

### qm_t2_facYaot_B: Conflict: Hazardous Archeology
We are looking for evidence of a missing Progenitor hyperspace gate in the area which should be there but isn’t. According to Tanoch intelligence the Yaot are also seeking this object.
	* Type:	Side
	* Goals:	Statistic,0, Statistic,0
	* GoalParameters:	Id&ScannedBelt;Total&45, Ids&Mined2A_Mined2B_Mined2C_Mined2D;Amount&1800

### qm_t2_facYaot_C: Conflict: Seek and Find
A Hiigaran flagship has gone missing in Tanoch space. Preliminary evidence points towards Yaot involvement. Lazarus wants us to investigate.
	* Type:	Side
	* Goals:	Scan,0, CompleteMission,0, Scan,0
	* GoalParameters:	Tags&InSystem_Generated_T2up;Amount&10;Analyzed&True, Mode&Generated;Tags&T2up;Amount&10, Tags&InGalaxy_T2up;Amount&7

### qm_t2_facYaot_D: Conflict: Opposition Research
The Yaot are the first major antagonistic power we have encountered. We need to make sure our crew is properly trained and ready to handle the upcoming battles.
	* Type:	Side
	* Goals:	GainItem,0, UpgradeOfficer,0
	* GoalParameters:	Tags&Insignia;Amount&80;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash, Amount&15

### qs_unlockStrikes_t1: Rising to the Challenge
As we venture further into this galaxy, we will encounter greater and greater threats. We need to be prepared.
	* Type:	Side
	* Goals:	Goto,0, Scan,1
	* GoalParameters:	Target&[-1535, -436];MoveType&InSystem

### qt_daily_buy: Big Spender
You can buy resources or items in the market as well as in the liaison requisitions.
	* Type:	Daily
	* Goals:	Buy,0
	* GoalParameters:	Amount&1

### qt_daily_mine: Primary Sector
Ores can be mined in asteroid clusters, while gas is harvested from jovians.
	* Type:	Daily
	* Goals:	Statistic,0
	* GoalParameters:	Id&Mined;Amount&1500

### qt_daily_refine: Metallurgy
Refining ores is required to turn them into usable metals for the production process.
	* Type:	Daily
	* Goals:	Craft,0
	* GoalParameters:	Category&Refining;Amount&500

### qt_daily_craft: Means of Production
You can fabricate all sorts of products in your flagship's factories.
	* Type:	Daily
	* Goals:	Craft,0
	* GoalParameters:	Category&Crafting;Amount&10

### qt_daily_gainRP: Hoarding Knowledge
Research points are passively collected in your flagship's laboratories. They are needed to conduct research.
	* Type:	Daily
	* Goals:	GainItem,0
	* GoalParameters:	Id&RP;Amount&400;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qt_daily_insignias: Distinction
You can earn insignias by completing missions. They are needed to promote your officers, which increases their attributes.
	* Type:	Daily
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Insignia;Amount&5;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qt_daily_liaison: Adventurism
Completing missions gives you XP to level up.
	* Type:	Daily
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&3

### qt_daily_destroy: Trophies
Destroyed enemy vessels sometimes leave salvage behind which may contain resources.
	* Type:	Daily
	* Goals:	Statistic,0
	* GoalParameters:	Id&ShipsDestroyed;Amount&15

### qt_daily_signals: New Discoveries
Some objects require to be scanned several times to reveal them fully.
	* Type:	Daily
	* Goals:	Scan,0
	* GoalParameters:	Tags&InSystem;Amount&5;Analyzed&True

### qt_daily_dailyMission: Bragging Rights
A strike is a great opportunity to test your strength and train your coordination with other commanders.
	* Type:	Daily
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&1;Mode&Strike

### qt_daily_dailies: Periodic Activity
Most daily and weekly assignments grant Prestige, which can be used in the prestige section of the market to acquire special blueprints and other items.
	* Type:	Daily
	* Goals:	CompleteQuest,0
	* GoalParameters:	Amount&8;Tags&Daily

### qt_weekly_dailies: Assiduity
Daily assignments refresh once a day, make sure to claim your reward before that happens.
	* Type:	Weekly
	* Goals:	CompleteQuest,0
	* GoalParameters:	Amount&40;Tags&Daily

### qt_weekly_reputation: Connections
Completing liaison assignments improves your standing with that particular faction, which in turn unlocks new items in their liaison requisitions.
	* Type:	Weekly
	* Goals:	CompleteQuest,0
	* GoalParameters:	Amount&9;Tags&Faction

### qt_weekly_clanQuests: Stronger Together
You can only complete clan assignments while you are inside a clan. Completing these grants you clan credits as well as clan supplies for the whole clan.
	* Type:	Weekly
	* Goals:	CompleteQuest,0
	* GoalParameters:	Amount&10;Tags&Clan

### qt_weekly_levelOfficers: Ranks and File
After reaching enough levels, officers will gain a new rank, which increases their abilities.
	* Type:	Weekly
	* Goals:	UpgradeOfficer,0
	* GoalParameters:	Amount&7

### qt_weekly_upgrades: Marvels of Engineering
Module upgrades need rare earth materials and can only be done at a trading station.
	* Type:	Weekly
	* Goals:	Craft,0
	* GoalParameters:	Category&Upgrade;Amount&10

### qt_weekly_missions: Signal Sweep
New signals may appear through scanning after you have cleared out a few.
	* Type:	Weekly
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&9;Mode&Generated

### qt_weekly_research: Scientific Method
Research is conducted inside your flagship's laboratories.
	* Type:	Weekly
	* Goals:	Craft,0
	* GoalParameters:	Tags&Research;Amount&5

### qe_amaSum_2023_daily_A_t1: No header for quest qe_amaSum_2023_daily_A_t1
No description for quest qe_amaSum_2023_daily_A_t1
	* Type:	Event
	* EventId:	event_season_amaSum_2023_t1
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Asteroid_Crud_T1up;Amount&350;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

### qe_amaSum_2023_daily_B_t1: No header for quest qe_amaSum_2023_daily_B_t1
No description for quest qe_amaSum_2023_daily_B_t1
	* Type:	Event
	* EventId:	event_season_amaSum_2023_t1
	* Goals:	Craft,0
	* GoalParameters:	Category&Crafting;Tags&T1up;Amount&1

### qe_amaSum_2023_daily_C_t1: No header for quest qe_amaSum_2023_daily_C_t1
No description for quest qe_amaSum_2023_daily_C_t1
	* Type:	Event
	* EventId:	event_season_amaSum_2023_t1
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedDarkHiigaranT1_ShipsDestroyedDarkHiigaranT2_ShipsDestroyedDarkHiigaranT3_ShipsDestroyedDarkHiigaranT4;Amount&10

### qe_amaSum_2023_daily_D_t1: No header for quest qe_amaSum_2023_daily_D_t1
No description for quest qe_amaSum_2023_daily_D_t1
	* Type:	Event
	* EventId:	event_season_amaSum_2023_t1
	* Goals:	GainItem,0
	* GoalParameters:	Tags&ProgenitorRelic_T1up;Amount&1;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_amaSum_2023_daily_A_t2: No header for quest qe_amaSum_2023_daily_A_t2
No description for quest qe_amaSum_2023_daily_A_t2
	* Type:	Event
	* EventId:	event_season_amaSum_2023_t2
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Asteroid_Crud_T2up;Amount&400;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

### qe_amaSum_2023_daily_B_t2: No header for quest qe_amaSum_2023_daily_B_t2
No description for quest qe_amaSum_2023_daily_B_t2
	* Type:	Event
	* EventId:	event_season_amaSum_2023_t2
	* Goals:	Craft,0
	* GoalParameters:	Category&Crafting;Tags&Part_T2up;Amount&25

### qe_amaSum_2023_daily_C_t2: No header for quest qe_amaSum_2023_daily_C_t2
No description for quest qe_amaSum_2023_daily_C_t2
	* Type:	Event
	* EventId:	event_season_amaSum_2023_t2
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedDarkHiigaranT2_ShipsDestroyedDarkHiigaranT3_ShipsDestroyedDarkHiigaranT4;Amount&10

### qe_amaSum_2023_daily_D_t2: No header for quest qe_amaSum_2023_daily_D_t2
No description for quest qe_amaSum_2023_daily_D_t2
	* Type:	Event
	* EventId:	event_season_amaSum_2023_t2
	* Goals:	GainItem,0
	* GoalParameters:	Tags&ProgenitorRelic_T2up;Amount&1;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_amaSum_2023_daily_A_t3: No header for quest qe_amaSum_2023_daily_A_t3
No description for quest qe_amaSum_2023_daily_A_t3
	* Type:	Event
	* EventId:	event_season_amaSum_2023_t3
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Asteroid_Crud_T3up;Amount&450;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

### qe_amaSum_2023_daily_B_t3: No header for quest qe_amaSum_2023_daily_B_t3
No description for quest qe_amaSum_2023_daily_B_t3
	* Type:	Event
	* EventId:	event_season_amaSum_2023_t3
	* Goals:	Craft,0
	* GoalParameters:	Category&Crafting;Tags&Part_T3up;Amount&25

### qe_amaSum_2023_daily_C_t3: No header for quest qe_amaSum_2023_daily_C_t3
No description for quest qe_amaSum_2023_daily_C_t3
	* Type:	Event
	* EventId:	event_season_amaSum_2023_t3
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedDarkHiigaranT3_ShipsDestroyedDarkHiigaranT4;Amount&10

### qe_amaSum_2023_daily_D_t3: No header for quest qe_amaSum_2023_daily_D_t3
No description for quest qe_amaSum_2023_daily_D_t3
	* Type:	Event
	* EventId:	event_season_amaSum_2023_t3
	* Goals:	GainItem,0
	* GoalParameters:	Tags&ProgenitorRelic_T3up;Amount&1;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_amaSum_2023_daily_A_t4: No header for quest qe_amaSum_2023_daily_A_t4
No description for quest qe_amaSum_2023_daily_A_t4
	* Type:	Event
	* EventId:	event_season_amaSum_2023_t4
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Asteroid_Crud_T4up;Amount&500;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

### qe_amaSum_2023_daily_B_t4: No header for quest qe_amaSum_2023_daily_B_t4
No description for quest qe_amaSum_2023_daily_B_t4
	* Type:	Event
	* EventId:	event_season_amaSum_2023_t4
	* Goals:	Craft,0
	* GoalParameters:	Category&Crafting;Tags&Part_T4up;Amount&25

### qe_amaSum_2023_daily_C_t4: No header for quest qe_amaSum_2023_daily_C_t4
No description for quest qe_amaSum_2023_daily_C_t4
	* Type:	Event
	* EventId:	event_season_amaSum_2023_t4
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedDarkHiigaranT4;Amount&10

### qe_amaSum_2023_daily_D_t4: No header for quest qe_amaSum_2023_daily_D_t4
No description for quest qe_amaSum_2023_daily_D_t4
	* Type:	Event
	* EventId:	event_season_amaSum_2023_t4
	* Goals:	GainItem,0
	* GoalParameters:	Tags&ProgenitorRelic_T4up;Amount&1;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_mar_2024_daily_A_t1: Finds must be discovered through scanning. After being analyzed, they can be picked up to collect the reward inside.
Finds must be discovered through scanning. After being analyzed, they can be picked up to collect the reward inside.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t1
	* Goals:	Scan,0
	* GoalParameters:	Tags&InSystem_Container_T1up;Amount&1;Analyzed&True

### qe_7days_mar_2024_daily_A_t2: Finds must be discovered through scanning. After being analyzed, they can be picked up to collect the reward inside.
Finds must be discovered through scanning. After being analyzed, they can be picked up to collect the reward inside.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t2
	* Goals:	Scan,0
	* GoalParameters:	Tags&InSystem_Container_T2up;Amount&1;Analyzed&True

### qe_7days_mar_2024_daily_A_t3: Finds must be discovered through scanning. After being analyzed, they can be picked up to collect the reward inside.
Finds must be discovered through scanning. After being analyzed, they can be picked up to collect the reward inside.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t3
	* Goals:	Scan,0
	* GoalParameters:	Tags&InSystem_Container_T3up;Amount&1;Analyzed&True

### qe_7days_mar_2024_daily_A_t4: Finds must be discovered through scanning. After being analyzed, they can be picked up to collect the reward inside.
Finds must be discovered through scanning. After being analyzed, they can be picked up to collect the reward inside.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t4
	* Goals:	Scan,0
	* GoalParameters:	Tags&InSystem_Container_T4up;Amount&1;Analyzed&True

### qe_7days_mar_2024_daily_B_t1: Progenitor relics can be found in relic signature signals.
Progenitor relics can be found in relic signature signals.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t1
	* Goals:	Pay,0
	* GoalParameters:	Id&questItem_progenitorRelic_t1;Amount&1

### qe_7days_mar_2024_daily_B_t2: Progenitor relics can be found in relic signature signals.
Progenitor relics can be found in relic signature signals.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t2
	* Goals:	Pay,0
	* GoalParameters:	Id&questItem_progenitorRelic_t2;Amount&1

### qe_7days_mar_2024_daily_B_t3: Progenitor relics can be found in relic signature signals.
Progenitor relics can be found in relic signature signals.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t3
	* Goals:	Pay,0
	* GoalParameters:	Id&questItem_progenitorRelic_t3;Amount&1

### qe_7days_mar_2024_daily_B_t4: Progenitor relics can be found in relic signature signals.
Progenitor relics can be found in relic signature signals.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t4
	* Goals:	Pay,0
	* GoalParameters:	Id&questItem_progenitorRelic_t4;Amount&1

### qe_7days_mar_2024_daily_C_t1: Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.
Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t1
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&1;Tags&Rare_T1up;Mode&Generated

### qe_7days_mar_2024_daily_C_t2: Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.
Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t2
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&1;Tags&Epic_T2up;Mode&Generated

### qe_7days_mar_2024_daily_C_t3: Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.
Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t3
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&1;Tags&Epic_T3up;Mode&Generated

### qe_7days_mar_2024_daily_C_t4: Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.
Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t4
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&1;Tags&Epic_T4up;Mode&Generated

### qe_7days_mar_2024_daily_D_t1: Prestige is earned through each player level-up and by completing daily and weekly assignments.
Prestige is earned through each player level-up and by completing daily and weekly assignments.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t1
	* Goals:	GainItem,0
	* GoalParameters:	Id&LP;Amount&10;ExcludedSources&BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem

### qe_7days_mar_2024_daily_D_t2: Prestige is earned through each player level-up and by completing daily and weekly assignments.
Prestige is earned through each player level-up and by completing daily and weekly assignments.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t2
	* Goals:	GainItem,0
	* GoalParameters:	Id&LP;Amount&10;ExcludedSources&BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem

### qe_7days_mar_2024_daily_D_t3: Prestige is earned through each player level-up and by completing daily and weekly assignments.
Prestige is earned through each player level-up and by completing daily and weekly assignments.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t3
	* Goals:	GainItem,0
	* GoalParameters:	Id&LP;Amount&10;ExcludedSources&BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem

### qe_7days_mar_2024_daily_D_t4: Prestige is earned through each player level-up and by completing daily and weekly assignments.
Prestige is earned through each player level-up and by completing daily and weekly assignments.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t4
	* Goals:	GainItem,0
	* GoalParameters:	Id&LP;Amount&10;ExcludedSources&BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem

### qe_iyaFal_2023_daily_A_t1: No header for quest qe_iyaFal_2023_daily_A_t1
No description for quest qe_iyaFal_2023_daily_A_t1
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t1
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedP1T1_ShipsDestroyedP1T2_ShipsDestroyedP1T3_ShipsDestroyedP1T4;Amount&10

### qe_iyaFal_2023_daily_B_t1: No header for quest qe_iyaFal_2023_daily_B_t1
No description for quest qe_iyaFal_2023_daily_B_t1
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t1
	* Goals:	GainItem,0
	* GoalParameters:	Id&CR;Amount&1250;ExcludedSources&BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

### qe_iyaFal_2023_daily_C_t1: No header for quest qe_iyaFal_2023_daily_C_t1
No description for quest qe_iyaFal_2023_daily_C_t1
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t1
	* Goals:	Scan,0
	* GoalParameters:	Tags&InSystem_T1up;Amount&10;Analyzed&True

### qe_iyaFal_2023_daily_D_t1: No header for quest qe_iyaFal_2023_daily_D_t1
No description for quest qe_iyaFal_2023_daily_D_t1
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t1
	* Goals:	GainItem,0
	* GoalParameters:	Tags&RareEarth_T1up;Amount&20;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_iyaFal_2023_daily_A_t2: No header for quest qe_iyaFal_2023_daily_A_t2
No description for quest qe_iyaFal_2023_daily_A_t2
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t2
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedP1T2_ShipsDestroyedP1T3_ShipsDestroyedP1T4;Amount&10

### qe_iyaFal_2023_daily_B_t2: No header for quest qe_iyaFal_2023_daily_B_t2
No description for quest qe_iyaFal_2023_daily_B_t2
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t2
	* Goals:	GainItem,0
	* GoalParameters:	Id&CR;Amount&2500;ExcludedSources&BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

### qe_iyaFal_2023_daily_C_t2: No header for quest qe_iyaFal_2023_daily_C_t2
No description for quest qe_iyaFal_2023_daily_C_t2
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t2
	* Goals:	Scan,0
	* GoalParameters:	Tags&InSystem_T2up;Amount&10;Analyzed&True

### qe_iyaFal_2023_daily_D_t2: No header for quest qe_iyaFal_2023_daily_D_t2
No description for quest qe_iyaFal_2023_daily_D_t2
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t2
	* Goals:	GainItem,0
	* GoalParameters:	Tags&RareEarth_T2up;Amount&20;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_iyaFal_2023_daily_A_t3: No header for quest qe_iyaFal_2023_daily_A_t3
No description for quest qe_iyaFal_2023_daily_A_t3
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t3
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedP1T3_ShipsDestroyedP1T4;Amount&10

### qe_iyaFal_2023_daily_B_t3: No header for quest qe_iyaFal_2023_daily_B_t3
No description for quest qe_iyaFal_2023_daily_B_t3
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t3
	* Goals:	GainItem,0
	* GoalParameters:	Id&CR;Amount&5000;ExcludedSources&BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

### qe_iyaFal_2023_daily_C_t3: No header for quest qe_iyaFal_2023_daily_C_t3
No description for quest qe_iyaFal_2023_daily_C_t3
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t3
	* Goals:	Scan,0
	* GoalParameters:	Tags&InSystem_T3up;Amount&10;Analyzed&True

### qe_iyaFal_2023_daily_D_t3: No header for quest qe_iyaFal_2023_daily_D_t3
No description for quest qe_iyaFal_2023_daily_D_t3
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t3
	* Goals:	GainItem,0
	* GoalParameters:	Tags&RareEarth_T3up;Amount&20;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_iyaFal_2023_daily_A_t4: No header for quest qe_iyaFal_2023_daily_A_t4
No description for quest qe_iyaFal_2023_daily_A_t4
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t4
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedP1T4;Amount&10

### qe_iyaFal_2023_daily_B_t4: No header for quest qe_iyaFal_2023_daily_B_t4
No description for quest qe_iyaFal_2023_daily_B_t4
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t4
	* Goals:	GainItem,0
	* GoalParameters:	Id&CR;Amount&10000;ExcludedSources&BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

### qe_iyaFal_2023_daily_C_t4: No header for quest qe_iyaFal_2023_daily_C_t4
No description for quest qe_iyaFal_2023_daily_C_t4
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t4
	* Goals:	Scan,0
	* GoalParameters:	Tags&InSystem_T4up;Amount&10;Analyzed&True

### qe_iyaFal_2023_daily_D_t4: No header for quest qe_iyaFal_2023_daily_D_t4
No description for quest qe_iyaFal_2023_daily_D_t4
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t4
	* Goals:	GainItem,0
	* GoalParameters:	Tags&RareEarth_T4up;Amount&20;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_anniversary_2023_daily_A_t1: Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
	* Type:	Event
	* EventId:	event_anniversary_2023_t1
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&5;Tags&T1up;Mode&Generated

### qe_anniversary_2023_daily_B_t1: Rare earths are an occasional by-product of refining. They are required for upgrading modules.
Rare earths are an occasional by-product of refining. They are required for upgrading modules.
	* Type:	Event
	* EventId:	event_anniversary_2023_t1
	* Goals:	GainItem,0
	* GoalParameters:	Tags&RareEarth_T1up;Amount&50;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_anniversary_2023_daily_A_t2: Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
	* Type:	Event
	* EventId:	event_anniversary_2023_t2
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&5;Tags&T2up;Mode&Generated

### qe_anniversary_2023_daily_B_t2: Rare earths are an occasional by-product of refining. They are required for upgrading modules.
Rare earths are an occasional by-product of refining. They are required for upgrading modules.
	* Type:	Event
	* EventId:	event_anniversary_2023_t2
	* Goals:	GainItem,0
	* GoalParameters:	Tags&RareEarth_T2up;Amount&50;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_anniversary_2023_daily_A_t3: Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
	* Type:	Event
	* EventId:	event_anniversary_2023_t3
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&5;Tags&T3up;Mode&Generated

### qe_anniversary_2023_daily_B_t3: Rare earths are an occasional by-product of refining. They are required for upgrading modules.
Rare earths are an occasional by-product of refining. They are required for upgrading modules.
	* Type:	Event
	* EventId:	event_anniversary_2023_t3
	* Goals:	GainItem,0
	* GoalParameters:	Tags&RareEarth_T3up;Amount&50;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_anniversary_2023_daily_A_t4: Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
	* Type:	Event
	* EventId:	event_anniversary_2023_t4
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&5;Tags&T4up;Mode&Generated

### qe_anniversary_2023_daily_B_t4: Rare earths are an occasional by-product of refining. They are required for upgrading modules.
Rare earths are an occasional by-product of refining. They are required for upgrading modules.
	* Type:	Event
	* EventId:	event_anniversary_2023_t4
	* Goals:	GainItem,0
	* GoalParameters:	Tags&RareEarth_T4up;Amount&50;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_halloween_2023_daily_A_t1: Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
	* Type:	Event
	* EventId:	event_halloween_2023_t1
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&1;Tags&ProgenitorInvasion_T1up;Mode&Generated

### qe_halloween_2023_daily_B_t1: Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
	* Type:	Event
	* EventId:	event_halloween_2023_t1
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&2;Tags&ProgenitorInvasion_T1up;Mode&Generated

### qe_halloween_2023_daily_C_t1: Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
	* Type:	Event
	* EventId:	event_halloween_2023_t1
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&5;Tags&ProgenitorInvasion_T1up;Mode&Generated

### qe_halloween_2023_daily_D_t1: Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
	* Type:	Event
	* EventId:	event_halloween_2023_t1
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&10;Tags&ProgenitorInvasion_T1up;Mode&Generated

### qe_halloween_2023_daily_A_t2: Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
	* Type:	Event
	* EventId:	event_halloween_2023_t2
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&1;Tags&ProgenitorInvasion_T2up;Mode&Generated

### qe_halloween_2023_daily_B_t2: Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
	* Type:	Event
	* EventId:	event_halloween_2023_t2
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&2;Tags&ProgenitorInvasion_T2up;Mode&Generated

### qe_halloween_2023_daily_C_t2: Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
	* Type:	Event
	* EventId:	event_halloween_2023_t2
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&5;Tags&ProgenitorInvasion_T2up;Mode&Generated

### qe_halloween_2023_daily_D_t2: Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
	* Type:	Event
	* EventId:	event_halloween_2023_t2
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&10;Tags&ProgenitorInvasion_T2up;Mode&Generated

### qe_halloween_2023_daily_A_t3: Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
	* Type:	Event
	* EventId:	event_halloween_2023_t3
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&1;Tags&ProgenitorInvasion_T3up;Mode&Generated

### qe_halloween_2023_daily_B_t3: Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
	* Type:	Event
	* EventId:	event_halloween_2023_t3
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&2;Tags&ProgenitorInvasion_T3up;Mode&Generated

### qe_halloween_2023_daily_C_t3: Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
	* Type:	Event
	* EventId:	event_halloween_2023_t3
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&5;Tags&ProgenitorInvasion_T3up;Mode&Generated

### qe_halloween_2023_daily_D_t3: Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
	* Type:	Event
	* EventId:	event_halloween_2023_t3
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&10;Tags&ProgenitorInvasion_T3up;Mode&Generated

### qe_halloween_2023_daily_A_t4: Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
	* Type:	Event
	* EventId:	event_halloween_2023_t4
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&1;Tags&ProgenitorInvasion_T4up;Mode&Generated

### qe_halloween_2023_daily_B_t4: Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
	* Type:	Event
	* EventId:	event_halloween_2023_t4
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&2;Tags&ProgenitorInvasion_T4up;Mode&Generated

### qe_halloween_2023_daily_C_t4: Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
	* Type:	Event
	* EventId:	event_halloween_2023_t4
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&5;Tags&ProgenitorInvasion_T4up;Mode&Generated

### qe_halloween_2023_daily_D_t4: Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
Previously dormant progenitor ships have activated and are attacking stations and fleets across the galaxy. Missions of rampaging progenitor ships can be found through scanning, just like ordinary signals.
	* Type:	Event
	* EventId:	event_halloween_2023_t4
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&10;Tags&ProgenitorInvasion_T4up;Mode&Generated

### qe_tanWin_2023_daily_A_t1: The Chicuat collect Progenitor relics for scientific study, rather than venerate them. Their academics would gladly acquire any such objects to advance their knowledge.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
The Chicuat collect Progenitor relics for scientific study, rather than venerate them. Their academics would gladly acquire any such objects to advance their knowledge.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t1
	* Goals:	Pay,0
	* GoalParameters:	Id&questItem_progenitorRelic_t1;Amount&1

### qe_tanWin_2023_daily_B_t1: Tasks performed for the Tanoch Empire also assist the Chicuat indirectly. Gaining favor with the Empire can give them more leverage in negotiations for aid.

<color=#FBB03F>Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.</color>
Tasks performed for the Tanoch Empire also assist the Chicuat indirectly. Gaining favor with the Empire can give the Chicuat more leverage in negotiations for aid.

<color=#FBB03F>Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t1
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&5;Tags&T1up;Mode&Generated

### qe_tanWin_2023_daily_C_t1: The Chicuat are always in need of supplies and equipment to bolster their economy and support their people. Any aid to them would be welcomed.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
The Chicuat are always in need of supplies and equipment to bolster their economy and support their people. Any aid to them would be welcomed.

<color=#FBB03F>Small items such as strike craft, modules and parts can be built in the fabricator. Larger items such as escort ships and flagships must be constructed at shipyards provided at larger stations.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t1
	* Goals:	Craft,0
	* GoalParameters:	Category&Crafting;Tags&T1up;Amount&1

### qe_tanWin_2023_daily_D_t1: The conflict between the Chicuat and ethnic Tanoch people goes back centuries. Training our crew about the details of this conflict will help us navigate the inner workings of the Tanoch Empire better.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
The conflict between the Chicuat and ethnic Tanoch people goes back centuries. Training our crew about the details of this conflict will help us navigate the inner workings of the Tanoch Empire better.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t1
	* Goals:	UpgradeOfficer,0
	* GoalParameters:	Amount&1

### qe_tanWin_2023_daily_A_t2: The Chicuat collect Progenitor relics for scientific study, rather than venerate them. Their academics would gladly acquire any such objects to advance their knowledge.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
The Chicuat collect Progenitor relics for scientific study, rather than venerate them. Their academics would gladly acquire any such objects to advance their knowledge.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t2
	* Goals:	Pay,0
	* GoalParameters:	Id&questItem_progenitorRelic_t2;Amount&1

### qe_tanWin_2023_daily_B_t2: Tasks performed for the Tanoch Empire also assist the Chicuat indirectly. Gaining favor with the Empire can give them more leverage in negotiations for aid.

<color=#FBB03F>Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.</color>
Tasks performed for the Tanoch Empire also assist the Chicuat indirectly. Gaining favor with the Empire can give them more leverage in negotiations for aid.

<color=#FBB03F>Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t2
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&5;Mode&Faction;Tags&T2up_Tanoch

### qe_tanWin_2023_daily_C_t2: The Chicuat are always in need of supplies and equipment to bolster their economy and support their people. Any aid to them would be welcomed.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
The Chicuat are always in need of supplies and equipment to bolster their economy and support their people. Any aid to them would be welcomed.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t2
	* Goals:	Craft,0
	* GoalParameters:	Category&Crafting;Tags&Part_T2up;Amount&100

### qe_tanWin_2023_daily_D_t2: The conflict between the Chicuat and ethnic Tanoch people goes back centuries. Training our crew about the details of this conflict will help us navigate the inner workings of the Tanoch Empire better.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
The conflict between the Chicuat and ethnic Tanoch people goes back centuries. Training our crew about the details of this conflict will help us navigate the inner workings of the Tanoch Empire better.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t2
	* Goals:	UpgradeOfficer,0
	* GoalParameters:	Amount&2

### qe_tanWin_2023_daily_A_t3: The Chicuat collect Progenitor relics for scientific study, rather than venerate them. Their academics would gladly acquire any such objects to advance their knowledge.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
The Chicuat collect Progenitor relics for scientific study, rather than venerate them. Their academics would gladly acquire any such objects to advance their knowledge.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t3
	* Goals:	Pay,0
	* GoalParameters:	Id&questItem_progenitorRelic_t3;Amount&1

### qe_tanWin_2023_daily_B_t3: Tasks performed for the Tanoch Empire also assist the Chicuat indirectly. Gaining favor with the Empire can give them more leverage in negotiations for aid.

<color=#FBB03F>Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.</color>
Tasks performed for the Tanoch Empire also assist the Chicuat indirectly. Gaining favor with the Empire can give them more leverage in negotiations for aid.

<color=#FBB03F>Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t3
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&5;Mode&Faction;Tags&T3up_Tanoch

### qe_tanWin_2023_daily_C_t3: The Chicuat are always in need of supplies and equipment to bolster their economy and support their people. Any aid to them would be welcomed.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
The Chicuat are always in need of supplies and equipment to bolster their economy and support their people. Any aid to them would be welcomed.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t3
	* Goals:	Craft,0
	* GoalParameters:	Category&Crafting;Tags&Part_T3up;Amount&100

### qe_tanWin_2023_daily_D_t3: The conflict between the Chicuat and ethnic Tanoch people goes back centuries. Training our crew about the details of this conflict will help us navigate the inner workings of the Tanoch Empire better.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
The conflict between the Chicuat and ethnic Tanoch people goes back centuries. Training our crew about the details of this conflict will help us navigate the inner workings of the Tanoch Empire better.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t3
	* Goals:	UpgradeOfficer,0
	* GoalParameters:	Amount&3

### qe_tanWin_2023_daily_A_t4: The Chicuat collect Progenitor relics for scientific study, rather than venerate them. Their academics would gladly acquire any such objects to advance their knowledge.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
The Chicuat collect Progenitor relics for scientific study, rather than venerate them. Their academics would gladly acquire any such objects to advance their knowledge.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t4
	* Goals:	Pay,0
	* GoalParameters:	Id&questItem_progenitorRelic_t4;Amount&1

### qe_tanWin_2023_daily_B_t4: Tasks performed for the Tanoch Empire also assist the Chicuat indirectly. Gaining favor with the Empire can give them more leverage in negotiations for aid.

<color=#FBB03F>Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.</color>
Tasks performed for the Tanoch Empire also assist the Chicuat indirectly. Gaining favor with the Empire can give them more leverage in negotiations for aid.

<color=#FBB03F>Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t4
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&5;Mode&Faction;Tags&T4up_Tanoch

### qe_tanWin_2023_daily_C_t4: The Chicuat are always in need of supplies and equipment to bolster their economy and support their people. Any aid to them would be welcomed.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
The Chicuat are always in need of supplies and equipment to bolster their economy and support their people. Any aid to them would be welcomed.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t4
	* Goals:	Craft,0
	* GoalParameters:	Category&Crafting;Tags&Part_T4up;Amount&100

### qe_tanWin_2023_daily_D_t4: The conflict between the Chicuat and ethnic Tanoch people goes back centuries. Training our crew about the details of this conflict will help us navigate the inner workings of the Tanoch Empire better.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
The conflict between the Chicuat and ethnic Tanoch people goes back centuries. Training our crew about the details of this conflict will help us navigate the inner workings of the Tanoch Empire better.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t4
	* Goals:	UpgradeOfficer,0
	* GoalParameters:	Amount&5

### qe_nimbusTreasures_2024_daily_A_t1: New capacitors were installed in our scanner modules during the last maintenance cycle and must be calibrated. Test them above maximum power.

<color=#FBB03F>Batteries can be used to recharge a scanner or even to overcharge it above 100%. Some rare scannable objects can only be found by overcharged scanners.</color>
New capacitors were installed in our scanner modules during the last maintenance cycle and must be calibrated. Test them above maximum power.

<color=#FBB03F>Batteries can be used to recharge a scanner or even to overcharge it above 100%. Some rare scannable objects can only be found by overcharged scanners.</color>
	* Type:	Event
	* EventId:	event_nimbusTreasures_2024_t1
	* Goals:	ChargeScanner,0
	* GoalParameters:	NewCharge&1.5

### qe_nimbusTreasures_2024_daily_B_t1: New firmware has been installed in our scanner modules. They must complete a routine calibration cycle until they pass inspection.

<color=#FBB03F>Scannable objects, such as finds, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
New firmware has been installed in our scanner modules. They must complete a routine calibration cycle until they pass inspection.

<color=#FBB03F>Scannable objects, such as finds, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
	* Type:	Event
	* EventId:	event_nimbusTreasures_2024_t1
	* Goals:	Scan,0
	* GoalParameters:	Tags&InSystem_Container_T1up;Amount&3;Analyzed&True

### qe_nimbusTreasures_2024_daily_C1_t1: To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
	* Type:	Event
	* EventId:	event_nimbusTreasures_2024_t1
	* Goals:	Pay,0
	* GoalParameters:	Id&questItem_alienProbe_t1;Amount&1

### qe_nimbusTreasures_2024_daily_C2_t1: To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
	* Type:	Event
	* EventId:	event_nimbusTreasures_2024_t1
	* Goals:	Pay,0
	* GoalParameters:	Id&questItem_alienProbe_t1;Amount&2

### qe_nimbusTreasures_2024_daily_C3_t1: To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
	* Type:	Event
	* EventId:	event_nimbusTreasures_2024_t1
	* Goals:	Pay,0
	* GoalParameters:	Id&questItem_alienProbe_t1;Amount&3

### qe_nimbusTreasures_2024_daily_C4_t1: To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
	* Type:	Event
	* EventId:	event_nimbusTreasures_2024_t1
	* Goals:	Pay,0
	* GoalParameters:	Id&questItem_alienProbe_t1;Amount&4

### qe_nimbusTreasures_2024_daily_A_t2: New capacitors were installed in our scanner modules during the last maintenance cycle and must be calibrated. Test them above maximum power.

<color=#FBB03F>Batteries can be used to recharge a scanner or even to overcharge it above 100%. Some rare scannable objects can only be found by overcharged scanners.</color>
New capacitors were installed in our scanner modules during the last maintenance cycle and must be calibrated. Test them above maximum power.

<color=#FBB03F>Batteries can be used to recharge a scanner or even to overcharge it above 100%. Some rare scannable objects can only be found by overcharged scanners.</color>
	* Type:	Event
	* EventId:	event_nimbusTreasures_2024_t2
	* Goals:	ChargeScanner,0
	* GoalParameters:	NewCharge&1.5

### qe_nimbusTreasures_2024_daily_B_t2: New firmware has been installed in our scanner modules. They must complete a routine calibration cycle until they pass inspection.

<color=#FBB03F>Scannable objects, such as finds, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
New firmware has been installed in our scanner modules. They must complete a routine calibration cycle until they pass inspection.

<color=#FBB03F>Scannable objects, such as finds, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
	* Type:	Event
	* EventId:	event_nimbusTreasures_2024_t2
	* Goals:	Scan,0
	* GoalParameters:	Tags&InSystem_Container_T2up;Amount&3;Analyzed&True

### qe_nimbusTreasures_2024_daily_C1_t2: To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
	* Type:	Event
	* EventId:	event_nimbusTreasures_2024_t2
	* Goals:	Pay,0
	* GoalParameters:	Id&questItem_alienProbe_t2;Amount&1

### qe_nimbusTreasures_2024_daily_C2_t2: To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
	* Type:	Event
	* EventId:	event_nimbusTreasures_2024_t2
	* Goals:	Pay,0
	* GoalParameters:	Id&questItem_alienProbe_t2;Amount&2

### qe_nimbusTreasures_2024_daily_C3_t2: To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
	* Type:	Event
	* EventId:	event_nimbusTreasures_2024_t2
	* Goals:	Pay,0
	* GoalParameters:	Id&questItem_alienProbe_t2;Amount&3

### qe_nimbusTreasures_2024_daily_C4_t2: To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
	* Type:	Event
	* EventId:	event_nimbusTreasures_2024_t2
	* Goals:	Pay,0
	* GoalParameters:	Id&questItem_alienProbe_t2;Amount&4

### qe_nimbusTreasures_2024_daily_A_t3: New capacitors were installed in our scanner modules during the last maintenance cycle and must be calibrated. Test them above maximum power.

<color=#FBB03F>Batteries can be used to recharge a scanner or even to overcharge it above 100%. Some rare scannable objects can only be found by overcharged scanners.</color>
New capacitors were installed in our scanner modules during the last maintenance cycle and must be calibrated. Test them above maximum power.

<color=#FBB03F>Batteries can be used to recharge a scanner or even to overcharge it above 100%. Some rare scannable objects can only be found by overcharged scanners.</color>
	* Type:	Event
	* EventId:	event_nimbusTreasures_2024_t3
	* Goals:	ChargeScanner,0
	* GoalParameters:	NewCharge&1.5

### qe_nimbusTreasures_2024_daily_B_t3: New firmware has been installed in our scanner modules. They must complete a routine calibration cycle until they pass inspection.

<color=#FBB03F>Scannable objects, such as finds, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
New firmware has been installed in our scanner modules. They must complete a routine calibration cycle until they pass inspection.

<color=#FBB03F>Scannable objects, such as finds, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
	* Type:	Event
	* EventId:	event_nimbusTreasures_2024_t3
	* Goals:	Scan,0
	* GoalParameters:	Tags&InSystem_Container_T3up;Amount&3;Analyzed&True

### qe_nimbusTreasures_2024_daily_C1_t3: To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
	* Type:	Event
	* EventId:	event_nimbusTreasures_2024_t3
	* Goals:	Pay,0
	* GoalParameters:	Id&questItem_alienProbe_t3;Amount&1

### qe_nimbusTreasures_2024_daily_C2_t3: To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
	* Type:	Event
	* EventId:	event_nimbusTreasures_2024_t3
	* Goals:	Pay,0
	* GoalParameters:	Id&questItem_alienProbe_t3;Amount&2

### qe_nimbusTreasures_2024_daily_C3_t3: To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
	* Type:	Event
	* EventId:	event_nimbusTreasures_2024_t3
	* Goals:	Pay,0
	* GoalParameters:	Id&questItem_alienProbe_t3;Amount&3

### qe_nimbusTreasures_2024_daily_C4_t3: To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
	* Type:	Event
	* EventId:	event_nimbusTreasures_2024_t3
	* Goals:	Pay,0
	* GoalParameters:	Id&questItem_alienProbe_t3;Amount&4

### qe_nimbusTreasures_2024_daily_A_t4: New capacitors were installed in our scanner modules during the last maintenance cycle and must be calibrated. Test them above maximum power.

<color=#FBB03F>Batteries can be used to recharge a scanner or even to overcharge it above 100%. Some rare scannable objects can only be found by overcharged scanners.</color>
New capacitors were installed in our scanner modules during the last maintenance cycle and must be calibrated. Test them above maximum power.

<color=#FBB03F>Batteries can be used to recharge a scanner or even to overcharge it above 100%. Some rare scannable objects can only be found by overcharged scanners.</color>
	* Type:	Event
	* EventId:	event_nimbusTreasures_2024_t4
	* Goals:	ChargeScanner,0
	* GoalParameters:	NewCharge&1.5

### qe_nimbusTreasures_2024_daily_B_t4: New firmware has been installed in our scanner modules. They must complete a routine calibration cycle until they pass inspection.

<color=#FBB03F>Scannable objects, such as finds, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
New firmware has been installed in our scanner modules. They must complete a routine calibration cycle until they pass inspection.

<color=#FBB03F>Scannable objects, such as finds, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
	* Type:	Event
	* EventId:	event_nimbusTreasures_2024_t4
	* Goals:	Scan,0
	* GoalParameters:	Tags&InSystem_Container_T4up;Amount&3;Analyzed&True

### qe_nimbusTreasures_2024_daily_C1_t4: To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
	* Type:	Event
	* EventId:	event_nimbusTreasures_2024_t4
	* Goals:	Pay,0
	* GoalParameters:	Id&questItem_alienProbe_t4;Amount&1

### qe_nimbusTreasures_2024_daily_C2_t4: To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
	* Type:	Event
	* EventId:	event_nimbusTreasures_2024_t4
	* Goals:	Pay,0
	* GoalParameters:	Id&questItem_alienProbe_t4;Amount&2

### qe_nimbusTreasures_2024_daily_C3_t4: To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
	* Type:	Event
	* EventId:	event_nimbusTreasures_2024_t4
	* Goals:	Pay,0
	* GoalParameters:	Id&questItem_alienProbe_t4;Amount&3

### qe_nimbusTreasures_2024_daily_C4_t4: To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
To gain more information about these unusual probes, more sensors must be deployed. Lazarus Base has authorized the distribution of our sensor probes to other parties.

<color=#FBB03F>Unidentified Sensor Probes must be collected from event exclusive signal missions called 'Sensor Probe Signature'.</color>
	* Type:	Event
	* EventId:	event_nimbusTreasures_2024_t4
	* Goals:	Pay,0
	* GoalParameters:	Id&questItem_alienProbe_t4;Amount&4

### qe_yaoSpr_2024_daily_A_t1: The Cangacian pirate bands running in this area are seeking the Yaot conjunction pilgrimage fleet. Attack them to dissuade their scouting efforts.

<color=#FBB03F>The Cangacians are pirates that harass trade routes and colonies. We may find them in signals in most areas of the galaxy. They have been sighted raiding mining fleets in asteroid clusters as well.</color>
The Cangacian pirate bands running in this area are seeking the Yaot conjunction pilgrimage fleet. Attack them to dissuade their scouting efforts.

<color=#FBB03F>The Cangacians are pirates that harass trade routes and colonies. We may find them in signals in most areas of the galaxy. They have been sighted raiding mining fleets in asteroid clusters as well.</color>
	* Type:	Event
	* EventId:	event_yaotSpring_2024_t1
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedP1T1_ShipsDestroyedP1T2_ShipsDestroyedP1T3_ShipsDestroyedP1T4;Amount&10

### qe_yaoSpr_2024_daily_A_t2: The Cangacian pirate bands running in this area are seeking the Yaot conjunction pilgrimage fleet. Attack them to dissuade their scouting efforts.

<color=#FBB03F>The Cangacians are pirates that harass trade routes and colonies. We may find them in signals in most areas of the galaxy. They have been sighted raiding mining fleets in asteroid clusters as well.</color>
The Cangacian pirate bands running in this area are seeking the Yaot conjunction pilgrimage fleet. Attack them to dissuade their scouting efforts.

<color=#FBB03F>The Cangacians are pirates that harass trade routes and colonies. We may find them in signals in most areas of the galaxy. They have been sighted raiding mining fleets in asteroid clusters as well.</color>
	* Type:	Event
	* EventId:	event_yaotSpring_2024_t2
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedP1T2_ShipsDestroyedP1T3_ShipsDestroyedP1T4;Amount&10

### qe_yaoSpr_2024_daily_A_t3: The Cangacian pirate bands running in this area are seeking the Yaot conjunction pilgrimage fleet. Attack them to dissuade their scouting efforts.

<color=#FBB03F>The Cangacians are pirates that harass trade routes and colonies. We may find them in signals in most areas of the galaxy. They have been sighted raiding mining fleets in asteroid clusters as well.</color>
The Cangacian pirate bands running in this area are seeking the Yaot conjunction pilgrimage fleet. Attack them to dissuade their scouting efforts.

<color=#FBB03F>The Cangacians are pirates that harass trade routes and colonies. We may find them in signals in most areas of the galaxy. They have been sighted raiding mining fleets in asteroid clusters as well.</color>
	* Type:	Event
	* EventId:	event_yaotSpring_2024_t3
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedP1T3_ShipsDestroyedP1T4;Amount&10

### qe_yaoSpr_2024_daily_A_t4: The Cangacian pirate bands running in this area are seeking the Yaot conjunction pilgrimage fleet. Attack them to dissuade their scouting efforts.

<color=#FBB03F>The Cangacians are pirates that harass trade routes and colonies. We may find them in signals in most areas of the galaxy. They have been sighted raiding mining fleets in asteroid clusters as well.</color>
The Cangacian pirate bands running in this area are seeking the Yaot conjunction pilgrimage fleet. Attack them to dissuade their scouting efforts.

<color=#FBB03F>The Cangacians are pirates that harass trade routes and colonies. We may find them in signals in most areas of the galaxy. They have been sighted raiding mining fleets in asteroid clusters as well.</color>
	* Type:	Event
	* EventId:	event_yaotSpring_2024_t4
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedP1T4;Amount&10

### qe_yaoSpr_2024_daily_B_t1: We must learn more about the situation if we're to understand why the Yaot pilgrim fleet is being targeted. Search for any remains that are left in their path of passage.

<color=#FBB03F>Finds must be discovered through scanning. After being analyzed, they can be picked up to collect the reward inside.</color>
We must learn more about the situation if we're to understand why the Yaot pilgrim fleet is being targeted. Search for any remains that are left in their path of passage.

<color=#FBB03F>Finds must be discovered through scanning. After being analyzed, they can be picked up to collect the reward inside.</color>
	* Type:	Event
	* EventId:	event_yaotSpring_2024_t1
	* Goals:	Scan,0
	* GoalParameters:	Tags&InSystem_Container_T1up;Amount&1;Analyzed&True

### qe_yaoSpr_2024_daily_B_t2: We must learn more about the situation if we're to understand why the Yaot pilgrim fleet is being targeted. Search for any remains that are left in their path of passage.

<color=#FBB03F>Finds must be discovered through scanning. After being analyzed, they can be picked up to collect the reward inside.</color>
We must learn more about the situation if we're to understand why the Yaot pilgrim fleet is being targeted. Search for any remains that are left in their path of passage.

<color=#FBB03F>Finds must be discovered through scanning. After being analyzed, they can be picked up to collect the reward inside.</color>
	* Type:	Event
	* EventId:	event_yaotSpring_2024_t2
	* Goals:	Scan,0
	* GoalParameters:	Tags&InSystem_Container_T2up;Amount&1;Analyzed&True

### qe_yaoSpr_2024_daily_B_t3: We must learn more about the situation if we're to understand why the Yaot pilgrim fleet is being targeted. Search for any remains that are left in their path of passage.

<color=#FBB03F>Finds must be discovered through scanning. After being analyzed, they can be picked up to collect the reward inside.</color>
We must learn more about the situation if we're to understand why the Yaot pilgrim fleet is being targeted. Search for any remains that are left in their path of passage.

<color=#FBB03F>Finds must be discovered through scanning. After being analyzed, they can be picked up to collect the reward inside.</color>
	* Type:	Event
	* EventId:	event_yaotSpring_2024_t3
	* Goals:	Scan,0
	* GoalParameters:	Tags&InSystem_Container_T3up;Amount&1;Analyzed&True

### qe_yaoSpr_2024_daily_B_t4: We must learn more about the situation if we're to understand why the Yaot pilgrim fleet is being targeted. Search for any remains that are left in their path of passage.

<color=#FBB03F>Finds must be discovered through scanning. After being analyzed, they can be picked up to collect the reward inside.</color>
We must learn more about the situation if we're to understand why the Yaot pilgrim fleet is being targeted. Search for any remains that are left in their path of passage.

<color=#FBB03F>Finds must be discovered through scanning. After being analyzed, they can be picked up to collect the reward inside.</color>
	* Type:	Event
	* EventId:	event_yaotSpring_2024_t4
	* Goals:	Scan,0
	* GoalParameters:	Tags&InSystem_Container_T4up;Amount&1;Analyzed&True

### qe_yaoSpr_2024_daily_C_t1: The Yaot pilgrimage is far from home and likely out of the supply network from the Yaot fleet. Any aid we can provide them would go a long way in helping them complete their journey.

<color=#FBB03F>Tokens of the eldest can be found in lost caches within Yaot territory or in Cangacian salvage.</color>
The Yaot pilgrimage is far from home and likely out of the supply network from the Yaot fleet. Any aid we can provide them would go a long way in helping them complete their journey.

<color=#FBB03F>Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.</color>
	* Type:	Event
	* EventId:	event_yaotSpring_2024_t1
	* Goals:	Pay,0, Pay,0, Pay,0
	* GoalParameters:	Id&1N;Amount&100, Id&1O;Amount&100, Id&1P;Amount&100

### qe_yaoSpr_2024_daily_C_t2: The Yaot pilgrimage is far from home and likely out of the supply network from the Yaot fleet. Any aid we can provide them would go a long way in helping them complete their journey.

<color=#FBB03F>Tokens of the eldest can be found in lost caches within Yaot territory or in Cangacian salvage.</color>
The Yaot pilgrimage is far from home and likely out of the supply network from the Yaot fleet. Any aid we can provide them would go a long way in helping them complete their journey.

<color=#FBB03F>Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.</color>
	* Type:	Event
	* EventId:	event_yaotSpring_2024_t2
	* Goals:	Pay,0, Pay,0, Pay,0
	* GoalParameters:	Id&2N;Amount&100, Id&2O;Amount&100, Id&2P;Amount&100

### qe_yaoSpr_2024_daily_C_t3: The Yaot pilgrimage is far from home and likely out of the supply network from the Yaot fleet. Any aid we can provide them would go a long way in helping them complete their journey.

<color=#FBB03F>Tokens of the eldest can be found in lost caches within Yaot territory or in Cangacian salvage.</color>
The Yaot pilgrimage is far from home and likely out of the supply network from the Yaot fleet. Any aid we can provide them would go a long way in helping them complete their journey.

<color=#FBB03F>Tokens of the eldest can be found in lost caches within Yaot territory or in Cangacian salvage.</color>
	* Type:	Event
	* EventId:	event_yaotSpring_2024_t3
	* Goals:	Pay,0
	* GoalParameters:	Id&yao_collectable_u_01;Amount&1

### qe_yaoSpr_2024_daily_C_t4: The Yaot pilgrimage is far from home and likely out of the supply network from the Yaot fleet. Any aid we can provide them would go a long way in helping them complete their journey.

<color=#FBB03F>Tokens of the eldest can be found in lost caches within Yaot territory or in Cangacian salvage.</color>
The Yaot pilgrimage is far from home and likely out of the supply network from the Yaot fleet. Any aid we can provide them would go a long way in helping them complete their journey.

<color=#FBB03F>Tokens of the eldest can be found in lost caches within Yaot territory or in Cangacian salvage.</color>
	* Type:	Event
	* EventId:	event_yaotSpring_2024_t4
	* Goals:	Pay,0
	* GoalParameters:	Id&yao_collectable_u_01;Amount&3

### qe_yaoSpr_2024_daily_D_t1: The Yaot likely do not know this region of space well based on how rarely they're encountered here. Examine the nearby star systems to assist the Yaot pilgrims in navigating the region.

<color=#FBB03F>Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.</color>
The Yaot likely do not know this region of space well based on how rarely they're encountered here. Examine the nearby star systems to assist the Yaot pilgrims in navigating the region.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
	* Type:	Event
	* EventId:	event_yaotSpring_2024_t1
	* Goals:	Scan,0
	* GoalParameters:	Tags&InSystem_Generated_T1up;Amount&5;Analyzed&True

### qe_yaoSpr_2024_daily_D_t2: The Yaot likely do not know this region of space well based on how rarely they're encountered here. Examine the nearby star systems to assist the Yaot pilgrims in navigating the region.

<color=#FBB03F>Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.</color>
The Yaot likely do not know this region of space well based on how rarely they're encountered here. Examine the nearby star systems to assist the Yaot pilgrims in navigating the region.

<color=#FBB03F>Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.</color>
	* Type:	Event
	* EventId:	event_yaotSpring_2024_t2
	* Goals:	GainItem,0
	* GoalParameters:	Id&RP;Amount&400;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_yaoSpr_2024_daily_D_t3: The Yaot likely do not know this region of space well based on how rarely they're encountered here. Examine the nearby star systems to assist the Yaot pilgrims in navigating the region.

<color=#FBB03F>Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.</color>
The Yaot likely do not know this region of space well based on how rarely they're encountered here. Examine the nearby star systems to assist the Yaot pilgrims in navigating the region.

<color=#FBB03F>Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.</color>
	* Type:	Event
	* EventId:	event_yaotSpring_2024_t3
	* Goals:	GainItem,0
	* GoalParameters:	Id&RP;Amount&400;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_yaoSpr_2024_daily_D_t4: The Yaot likely do not know this region of space well based on how rarely they're encountered here. Examine the nearby star systems to assist the Yaot pilgrims in navigating the region.

<color=#FBB03F>Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.</color>
The Yaot likely do not know this region of space well based on how rarely they're encountered here. Examine the nearby star systems to assist the Yaot pilgrims in navigating the region.

<color=#FBB03F>Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.</color>
	* Type:	Event
	* EventId:	event_yaotSpring_2024_t4
	* Goals:	GainItem,0
	* GoalParameters:	Id&RP;Amount&400;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

## ql_main_t0_jolja

### qm_t0_Jolja: Delver
After examining the Progenitor Relic, Gideon wants us to find a Progenitor Terminal in Iniim. If we access this, we may have some answers about what happened at Wiracoda Gate.
	* Type:	Main
	* ReplayMissionId:	story_A05_Jolja, story_A05_Jolja_heroic
	* FollowUps:	ql_main_t0_setupPlayer
	* Goals:	Goto,0, Scan,1, CompleteMission,2, Goto,3
	* GoalParameters:	Target&[-1764, -703], Tags&InSystem;Amount&1, Id&story_A05_Jolja, Target&[-1822, -636];TargetMode&Station

## ql_main_t0_setupPlayer

### qm_t0_pickKiith: Blood Ties
The local Hiigaran survivors wish to know what Kiith we affiliate with. There are advantages for declaring for a specific Kiith.
	* Type:	Main
	* Goals:	SelectKiith,0

### qm_t0_pickName: Declaration
The Hiigaran survivors want to know your name, commander.
	* Type:	Main
	* FollowUps:	ql_main_t1_newOres, ql_main_t0_joinClan
	* Goals:	ChangeName,0

## ql_main_t0_joinClan

### qm_t0_joinClan: A Clan of Choice
We can increase our firepower and capabilities by joining with other battle groups.
	* Type:	Main
	* Goals:	JoinClan,0

## ql_main_t1_newOres

### qm_t1_newOres: New Minerals
The inner systems may have different resources. We should check out the asteroids for mining spots.
	* Type:	Main
	* FollowUps:	ql_esca_mineT1
	* Goals:	Goto,0, Statistic,1, Statistic,2
	* GoalParameters:	Target&[-1793, -424], Id&ScannedBelt;Total&6, Ids&Mined1A_Mined1B_Mined1C;Amount&200

### qm_t1_introRefining: Refinery
The new ores require refining to be usable for construction purposes. Luckily we have refining facilities on board.
	* Type:	Main
	* FollowUps:	ql_main_t1_sideHiig, qm_t1_facHiigaran_A, qm_t1_facHiigaran_B, qm_t1_facHiigaran_C, qm_t1_facHiigaran_D
	* Goals:	Statistic,0, Goto,1
	* GoalParameters:	Ids&Refining1N_Refining1O_Refining1P;Amount&100, Target&[-1822, -636];TargetMode&Station

## ql_main_t1_sideHiig

### qm_t1_facHiigaran: Hiigaran Outposts
Lazarus station asked us to help some Hiigaran outposts on the frontier.
	* Type:	Main
	* FollowUps:	ql_main_t1_strikeCraft
	* Goals:	CompleteQuest,0, Goto,1
	* GoalParameters:	Amount&3;Ids&qm_t1_facHiigaran_A|qm_t1_facHiigaran_B|qm_t1_facHiigaran_C|qm_t1_facHiigaran_D, Target&[-1822, -636];TargetMode&Station

## ql_main_t1_strikeCraft

### qm_t1_strikeCraft: New Strike Craft
We have found a way to incorporate the new materials into our ship design.
	* Type:	Main
	* FollowUps:	ql_main_t1_advCombat_01, ql_main_t1_RCol
	* Goals:	Craft,0, Craft,0, Equip,1, Equip,1
	* GoalParameters:	Category&Crafting;Tags&Interceptor_T1;Amount&1, Category&Crafting;Tags&PlasmaBomber_T1;Amount&1, Type&Squad;Tags&Interceptor_T1up, Type&Squad;Tags&PlasmaBomber_T1up

## ql_main_t1_RCol

### qm_t1_RColEquip: New Resource Collector
The new ores are more difficult to mine. We should build resource collectors that are equipped to deal with these denser metals.
	* Type:	Main
	* Goals:	Craft,0, Equip,1
	* GoalParameters:	Category&Crafting;Tags&RCol_T1;Amount&1, Type&Squad;Tags&RCol_T1up

### qm_t1_RColMine: Mining Spree
We should put our new resource collectors to the test and stockpile some ores.
	* Type:	Main
	* Goals:	Statistic,0
	* GoalParameters:	Ids&Mined1A_Mined1B_Mined1C;Amount&4500

## ql_main_t1_advCombat_01

### qm_t1_advCombat_01: Combat Trials
Our Hiigaran allies have prepared a combat area to test our improved strike craft.
	* Type:	Main
	* ReplayMissionId:	story_B01_CombatTrials, story_B01_CombatTrials_heroic
	* Goals:	CompleteMission,0
	* GoalParameters:	Id&story_B01_CombatTrials

### qm_t1_killEnemyShips: Hostiles
These inner systems are crawling with enemies. We should thin their numbers. Enemies are found in asteroid clusters and signals.
	* Type:	Main
	* FollowUps:	ql_main_t1_promoteOfficer
	* Goals:	Statistic,0
	* GoalParameters:	Id&ShipsDestroyed;Amount&25

## ql_main_t1_promoteOfficer

### qm_t1_introPromoteOfficer: Crew Experience
Training our officers will increase their performance significantly. To train an officer we need to find insignias. Insignias can be gained from discharging officers and may be rewarded from completing signals.
	* Type:	Main
	* FollowUps:	ql_main_t1_escorts
	* Goals:	UpgradeOfficer,0
	* GoalParameters:	Amount&1

### qm_t1_rankUpOfficer: Crew Promotion
We should promote our most experienced officers to further improve their performance. Promoting an officer increase their special ability or may even grant them a second.
	* Type:	Side
	* Goals:	UpgradeOfficer,0
	* GoalParameters:	Amount&1;MinLevel&10

## ql_main_t1_escorts

### qm_t1_escort: New Escorts
We should bolster our fleet with frigates made from the new metals.
	* Type:	Main
	* FollowUps:	ql_main_t1_advCombat_02
	* Goals:	Craft,0, Equip,1
	* GoalParameters:	Category&Crafting;Tags&AssaultFrigate_T1;Amount&1, Type&Escort;Tags&AssaultFrigate_T1up

## ql_main_t1_advCombat_02

### qm_t1_advCombat_02: Meropis Defense
We received a message that Meropis, a Iyatequa communications station, is asking for support in an expected Cangacian attack.
	* Type:	Main
	* ReplayMissionId:	story_B02_MeropisDefense, story_B02_MeropisDefense_heroic
	* Goals:	CompleteMission,0
	* GoalParameters:	Id&story_B02_MeropisDefense

### qm_t1_doSignals: Signal Tracking
The Cangacians have been repelled, but we should disrupt their activities by hunting down hostile signals in the area.
	* Type:	Main
	* FollowUps:	ql_main_t1_sideCang, ql_esca_killPirate1, qm_t1_facCangacian_A, qm_t1_facCangacian_B, qm_t1_facCangacian_C, qm_t1_facCangacian_D
	* Goals:	CompleteMission,0
	* GoalParameters:	Mode&Generated;Amount&1;Tier&1

## ql_main_t1_sideCang

### qm_t1_facCangacian: Cangacian Troubles
Cangacians are attacking colonies. We should help them in whatever way we can.
	* Type:	Main
	* FollowUps:	ql_main_t1_flagship
	* Goals:	CompleteQuest,0, Goto,1
	* GoalParameters:	Amount&3;Ids&qm_t1_facCangacian_A|qm_t1_facCangacian_B|qm_t1_facCangacian_C|qm_t1_facCangacian_D, Target&[-1822, -636];TargetMode&Station

## ql_main_t1_flagship

### qm_t1_introCraftFlagship: Flagship Construction
We have an Explorer-class flagship blueprint utilizing the new minerals found in this region.
	* Type:	Main
	* FollowUps:	ql_main_t1_killCangacians
	* Goals:	StartCraft,0
	* GoalParameters:	Category&Crafting;Tags&Flagship_Ship;Amount&1

### qm_t1_introEquipFlagship: New Flagship
Once the flagship construction has finished, we should move over to the new flagship, including our ships and officers. This is done via the fleet configuration.
	* Type:	Main
	* FollowUps:	ql_main_t1_advCombat_03
	* Goals:	Craft,0, Equip,1, Equip,2, Equip,2, Equip,2
	* GoalParameters:	Category&Crafting;Tags&Flagship_Ship;Amount&1, Type&Flagship, Type&Squad, Type&Escort, Type&Officer;Location&Bridge

## ql_main_t1_killCangacians

### qm_t1_killCangacians: Pest Control
While we wait for the flagship construction to finish, we might as well make this galaxy a safer place.
	* Type:	Side
	* Goals:	Statistic,0
	* GoalParameters:	Id&ShipsDestroyedP1;Amount&20

## ql_main_t1_advCombat_03

### qm_t1_advCombat_03: The Pool
The Iyatequa have flagged a location for suspicious hostile activity. They've asked us to investigate on their behalf.
	* Type:	Main
	* ReplayMissionId:	story_B03_ThePool, story_B03_ThePool_heroic
	* Goals:	CompleteMission,0
	* GoalParameters:	Id&story_B03_ThePool

### qm_t1_killProgenitors: Hostile History
The Progenitor remnants present a danger to the people living in this galaxy. We should thin their numbers.
	* Type:	Main
	* FollowUps:	ql_main_t1_turrets
	* Goals:	Statistic,0
	* GoalParameters:	Id&ShipsDestroyedProgenitor;Amount&10

## ql_main_t1_turrets

### qm_t1_craftTurret: Weapon Turrets
The new flagship follows modular design principles, allowing us to outfit it with turrets as we choose. First we should build a weapon turret.
	* Type:	Main
	* Goals:	Craft,0
	* GoalParameters:	Category&Crafting;Tags&Weapon_Module_T1;Amount&1

### qm_t1_mountTurret: Mounting Turrets
Now that we have a turret module, we should mount it on our flagship. Turrets can be managed in the external module view of our flagship.
	* Type:	Main
	* FollowUps:	ql_main_t1_upgrades
	* Goals:	Equip,0
	* GoalParameters:	Type&Weapon

## ql_main_t1_upgrades

### qm_t1_rareEarths: Rare Elements
When refining ores in the refinery there is a chance for rare earths to appear in addition to the refined metals.
	* Type:	Main
	* Goals:	GainItem,0
	* GoalParameters:	Tags&RareEarth;Amount&5;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qm_t1_upgradeTurret: Turret Upgrades
The rare minerals we have extracted can be used to improve our modules.
	* Type:	Main
	* FollowUps:	ql_main_t1_sideProg, qm_t1_facProgenitors_A, qm_t1_facProgenitors_B, qm_t1_facProgenitors_C, qm_t1_facProgenitors_D
	* Goals:	Craft,0
	* GoalParameters:	Category&Upgrade;Tags&Weapon_Module;Amount&1

### qm_t1_upgradeTurret_3: Turret Upgrades Level 3
A module can be upgraded multiple times, vastly increasing its power.
	* Type:	Side
	* Goals:	Craft,0
	* GoalParameters:	Category&Upgrade;Tags&Weapon_Module;Amount&1;MinLevel&3

### qm_t1_upgradeTurret_4: Turret Upgrades Level 4
A module can be upgraded multiple times, vastly increasing its power.
	* Type:	Side
	* Goals:	Craft,0
	* GoalParameters:	Category&Upgrade;Tags&Weapon_Module;Amount&1;MinLevel&4

### qm_t1_upgradeTurret_5: Turret Upgrades Level 5
A module can be upgraded multiple times, vastly increasing its power.
	* Type:	Side
	* Goals:	Craft,0
	* GoalParameters:	Category&Upgrade;Tags&Weapon_Module;Amount&1;MinLevel&5

### qm_t1_upgradeTurret_6: Turret Upgrades Level 6
A module can be upgraded multiple times, vastly increasing its power.
	* Type:	Side
	* Goals:	Craft,0
	* GoalParameters:	Category&Upgrade;Tags&Weapon_Module;Amount&1;MinLevel&6

### qm_t1_upgradeTurret_7: Turret Upgrades Level 7
A module can be upgraded multiple times, vastly increasing its power.
	* Type:	Side
	* Goals:	Craft,0
	* GoalParameters:	Category&Upgrade;Tags&Weapon_Module;Amount&1;MinLevel&7

### qm_t1_upgradeTurret_8: Turret Upgrades Level 8
A module can be upgraded multiple times, vastly increasing its power.
	* Type:	Side
	* Goals:	Craft,0
	* GoalParameters:	Category&Upgrade;Tags&Weapon_Module;Amount&1;MinLevel&8

### qm_t1_upgradeTurretMax: Final Turret Upgrades
Once a module has been upgraded to level 9, it is at its maximum level and cannot be upgraded further.
	* Type:	Side
	* Goals:	Craft,0
	* GoalParameters:	Category&Upgrade;Tags&Weapon_Module;Amount&1;MinLevel&9

## ql_main_t1_sideProg

### qm_t1_facProgenitors: Progenitor Components
To improve our scanner, we should gather data on Progenitor vessels. Once we have enough data, we can create a new scanner blueprint.
	* Type:	Main
	* FollowUps:	ql_main_t1_scanner
	* Goals:	CompleteQuest,0, Goto,1
	* GoalParameters:	Amount&3;Ids&qm_t1_facProgenitors_A|qm_t1_facProgenitors_B|qm_t1_facProgenitors_C|qm_t1_facProgenitors_D, Target&[-1822, -636];TargetMode&Station

## ql_main_t1_scanner

### qm_t1_scannerModule: New Scanner
Based on the data from the Progenitor fragments, our engineers have created a new scanner blueprint.
	* Type:	Main
	* FollowUps:	ql_main_t2_strike, ql_esca_scan, ql_main_t1_scannerCharge
	* Goals:	Craft,0, Equip,1
	* GoalParameters:	Category&Crafting;Tags&Sensor_Module_T1;Amount&1, Type&Sensor;Tags&T1up

## ql_main_t1_scannerCharge

### qm_t1_scannerOvercharge: Rare Find
Some objects are too hidden to find them with our scanner under regular circumstances. Luckily, we can use special batteries to overcharge the scanner beyond its normal abilities to be able to find those.
	* Type:	Side
	* Goals:	ChargeScanner,0, Scan,1
	* GoalParameters:	NewCharge&1.25, Tags&InSystem_Rare;Amount&1

## ql_main_t2_strike

### qm_t2_findPirateHideout: Hidden in the Dark
We need to find the system from where the recent Cangacian activity originates. Reports indicate the system might be near Saraal. We should go there and use our long range scanners.
	* Type:	Main
	* FollowUps:	ql_raid_013, ql_main_t1_upgradeExternals, ql_main_t1_introLiaison
	* Goals:	Scan,0, Goto,0
	* GoalParameters:	Tags&InGalaxy_T1up;Amount&1;Analyzed&True, Target&[-1793, -424]

### qm_t2_strikePirateHideout: Cangacian Hideout
We have located the pirate hideout. Now is the time to strike.
	* Type:	Main
	* Goals:	CompleteQuest,0
	* GoalParameters:	Ids&qr_013;Amount&1

## ql_main_t1_upgradeExternals

### qm_t1_upgradeModules: Exploration Upgrades
In order to move deeper into the galaxy we should upgrade our scanner and drives core.
	* Type:	Main
	* FollowUps:	ql_main_t1_introInternals
	* Goals:	Craft,0, Craft,0
	* GoalParameters:	Category&Upgrade;Tags&Sensor;Amount&1;MinLevel&5, Category&Upgrade;Tags&Engine;Amount&1;MinLevel&5

## ql_main_t1_introLiaison

### qm_t1_introLiaison: Reaching Out
The Iyatequa are interested in doing business with us. Completing liaison assignments for them will allow us to increase our reputation, which allows us to buy special items and blueprints in their liaison requisitions office.
	* Type:	Side
	* Goals:	CompleteQuest,0
	* GoalParameters:	Amount&3;Tags&Faction

## ql_main_t1_introInternals

### qm_t1_introInternals: Internal Modules
Our flagship has a configurable interior, which we can use to boost our exploration, production or combat abilities using internal modules.
	* Type:	Main
	* Goals:	Craft,0, Equip,1
	* GoalParameters:	Tags&Crafting_Factory, Type&Internal;Tags&Crafting_Factory

### qm_t1_upgradeInternals: Internal Module Upgrades
Just like with weapon turrets, we can improve our internal module's performance through upgrades.
	* Type:	Main
	* FollowUps:	ql_main_t1_sideIyat, qm_t1_facIyatequa_A, qm_t1_facIyatequa_B, qm_t1_facIyatequa_C, qm_t1_facIyatequa_D
	* Goals:	Craft,0
	* GoalParameters:	Category&Upgrade;Tags&Factory;MinLevel&2

## ql_main_t1_sideIyat

### qm_t1_facIyatequa: Iyatequa Business
The Iyatequa have heard of our plan to meet the Tanoch and agreed to help us set up our science facilities to research better drives. For a price, of course.
	* Type:	Main
	* FollowUps:	ql_main_t2_research
	* Goals:	CompleteQuest,0, Goto,1
	* GoalParameters:	Amount&3;Ids&qm_t1_facIyatequa_A|qm_t1_facIyatequa_B|qm_t1_facIyatequa_C|qm_t1_facIyatequa_D, Target&[-1822, -636];TargetMode&Station

## ql_main_t2_research

### qm_t2_introRP: Laboratories
Our scientists have brought our on-ship laboratories online. We can collect the data of their findings there.
	* Type:	Main
	* Goals:	GainItem,0
	* GoalParameters:	Id&RP;Amount&15;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qm_t2_introResearch: Research Center
Lazarus Base has given us access to a workshop module attached to the station. We can perform further research there and develop new technologies.
	* Type:	Main
	* FollowUps:	ql_main_t2_newResources
	* Goals:	Craft,0
	* GoalParameters:	Category&Research;Id&rp_catExpl_hyperCap_t2_c;Tags&T2

## ql_main_t2_newResources

### qm_t2_newResources: New Resources T2
It seems the deeper we move into the galaxy the more minerals we find.
	* Type:	Main
	* FollowUps:	ql_main_t2_sideCang, qm_t2_facCangacian_A, qm_t2_facCangacian_B, qm_t2_facCangacian_C, qm_t2_facCangacian_D
	* Goals:	Goto,0, Statistic,1, Statistic,2, Craft,3, Goto,4
	* GoalParameters:	Target&[-1491, -596], Id&ScannedBelt;Total&25, Ids&Mined2A_Mined2B_Mined2C_Mined2D;Amount&3000, Category&Refining;Amount&1500;Tags&T2, Target&[-1822, -636];TargetMode&Station

## ql_main_t2_sideCang

### qm_t2_facCangacian: Cangacian Incursion
Several Hiigaran colonies are under attack by Cangacians. Lazarus command has asked us to help as much as we can.
	* Type:	Main
	* FollowUps:	ql_main_t2_strikeCraftResearch
	* Goals:	CompleteQuest,0, Goto,1
	* GoalParameters:	Amount&3;Ids&qm_t2_facCangacian_A|qm_t2_facCangacian_B|qm_t2_facCangacian_C|qm_t2_facCangacian_D, Target&[-1822, -636];TargetMode&Station

## ql_main_t2_strikeCraftResearch

### qm_t2_startResearchT2Intc: Interceptor T2
We can research better ship blueprints using the new materials found in this region.
	* Type:	Main
	* FollowUps:	ql_main_t2_strikeCraftCraft
	* Goals:	StartCraft,0
	* GoalParameters:	Category&Research;Id&rp_catStrCraft_bp_sf_intc_t2_c

### qm_t2_finResearchT2Intc: Interceptor Schematics
Schematics research unlock new blueprints for the fabricators and shipyard.
	* Type:	Main
	* Goals:	Craft,0
	* GoalParameters:	Category&Research;Id&rp_catStrCraft_bp_sf_intc_t2_c

## ql_main_t2_strikeCraftCraft

### qm_t2_introParts: Ship Parts Assembly
The new constructions will require the use of specially fabricated parts.

The blueprints for small Hull, Weapon and Machinery parts can be found in the market.
	* Type:	Main
	* Goals:	Buy,0, Craft,1
	* GoalParameters:	Id&bp_intmed_ship_small_t2, Tags&Part_Ship_S_T2;Amount&400;Category&Crafting

### qm_t2_strikeCraft: Strike Craft T2
Now that we have finished the research and crafted the necessary parts, we can craft an interceptor squadron.
	* Type:	Main
	* FollowUps:	ql_main_t2_sideHiig, ql_main_t2_RCol, ql_raid_016, qm_t2_facHiigaran_A, qm_t2_facHiigaran_B, qm_t2_facHiigaran_C, qm_t2_facHiigaran_D
	* Goals:	CompleteQuest,0, Craft,1
	* GoalParameters:	Ids&qm_t2_finResearchT2Intc;Amount&1, Category&Crafting;Tags&Interceptor_T2;Amount&1

## ql_main_t2_sideHiig

### qm_t2_facHiigaran: Lazarus Repairs
Lazarus Station was recently attacked. Command asked us to help with rebuilding efforts.
	* Type:	Main
	* FollowUps:	ql_main_t2_researchEscort
	* Goals:	CompleteQuest,0
	* GoalParameters:	Amount&3;Ids&qm_t2_facHiigaran_A|qm_t2_facHiigaran_B|qm_t2_facHiigaran_C|qm_t2_facHiigaran_D

## ql_main_t2_RCol

### qm_t2_craftRCol: Resource Collector T2
Mining the new ores can be done faster with special resource collectors equipped with better mining gear.
	* Type:	Side
	* Goals:	Craft,0
	* GoalParameters:	Category&Crafting;Tags&RCol_T2;Amount&1

### qm_t2_RColMining: Ore Deal
With our new resource collectors, we can mine ores much faster than before.
	* Type:	Side
	* FollowUps:	ql_main_t2_RCon
	* Goals:	Statistic,0
	* GoalParameters:	Ids&Mined2A_Mined2B_Mined2C_Mined2D;Amount&9000

## ql_main_t2_RCon

### qm_t2_craftRCon: Resource Controller
We acquired a blueprint for the Resource Controller, an escort ship we can send on independent mining missions. Like other escort ships, it must be built in the shipyard.
	* Type:	Side
	* Goals:	Craft,0
	* GoalParameters:	Category&Crafting;Tags&RCon;Amount&1

### qm_t2_introIdleMine: Remote Mining
Resource Controllers can be sent away to mine ores without our supervision. To do that, it must be assigned to an escort slot in fleet configuration.
	* Type:	Side
	* Goals:	Statistic,0
	* GoalParameters:	Ids&IdleMined;Amount&5000

## ql_main_t2_researchEscort

### qm_t2_startResearchT2Frig: Assault Frigate T2
We can research a better assault frigate blueprint using the new minerals.
	* Type:	Main
	* FollowUps:	ql_main_t2_oreD
	* Goals:	StartCraft,0
	* GoalParameters:	Category&Research;Id&rp_catEscorts_bp_cf_assa_t2_c

### qm_t2_finResearchT2Frig: Assault Frigate Schematics
Our scientists are at work developing new schematics for the assault frigate.
	* Type:	Main
	* FollowUps:	ql_main_t2_craftEscort, ql_main_t2_researchPulsarCorvette
	* Goals:	Craft,0
	* GoalParameters:	Category&Research;Id&rp_catEscorts_bp_cf_assa_t2_c

## ql_main_t2_oreD

### qm_t2_introOreD: Gold Rush
Some asteroids in this region contain a rare ore we can use for advanced constructions.
	* Type:	Side
	* Goals:	Statistic,0, Craft,1
	* GoalParameters:	Id&Mined2D;Amount&3500, Category&Refining;Amount&1500;Id&2Q

### qm_t2_craftUncShip: Elite Ships
We acquired a blueprint for an advanced ship design. It requires the rare ore to be built.
	* Type:	Side
	* Goals:	Craft,0
	* GoalParameters:	Id&hgn_sf_intc_01_u_t2

## ql_main_t2_researchPulsarCorvette

### qm_t2_researchPulsarCorvette: Pulsar Corvette Schematics
Uncommon, rare and epic researches are not part of the central research path and must be found in order to be researched.

The Pulsar Corvette Schematics can be found in the code fragment market.
	* Type:	Side
	* FollowUps:	ql_main_t2_pulsarCorvette
	* Goals:	Craft,0
	* GoalParameters:	Category&Research;Id&rp_catStrCraft_bp_sc_puls_t2_c;MinLevel&1

## ql_main_t2_pulsarCorvette

### qm_t2_pulsarCorvette: Pulsar Corvette
Pulsar Corvettes are effective against other corvettes and small escort ships.
	* Type:	Side
	* Goals:	Craft,0
	* GoalParameters:	Category&Crafting;Tags&PulsarCorvette_T2;Amount&1

## ql_main_t2_craftEscort

### qm_t2_largeHullParts: Large Hull Parts Assembly
The frigate blueprint requires a large version of the hull parts.

The blueprint for large hull parts can be found in the market.
	* Type:	Main
	* Goals:	Buy,0, Craft,1
	* GoalParameters:	Id&bp_intmed_ship_large_t2, Tags&Part_Ship_L_T2;Amount&400;Category&Crafting

### qm_t2_escort: Escort Ships T2
With the large hull parts we can finally construct the frigate.
	* Type:	Main
	* FollowUps:	ql_main_t2_introLiaison, ql_main_t2_strikeStationDefense, ql_raid_014
	* Goals:	Craft,0
	* GoalParameters:	Category&Crafting;Tags&AssaultFrigate_T2;Amount&1

## ql_main_t2_introLiaison

### qm_t2_introLiaison: Liaison Office
Doing assignments for the liaison office will allow us to requisition better blueprints and better equipment.
	* Type:	Main
	* FollowUps:	ql_main_t2_sideIyat, qm_t2_facIyatequa_A, qm_t2_facIyatequa_B, qm_t2_facIyatequa_C, qm_t2_facIyatequa_D
	* Goals:	CompleteQuest,0
	* GoalParameters:	Amount&3;Tags&Faction

## ql_main_t2_sideIyat

### qm_t2_facIyatequa: Iyatequa Intermediary
The Iyatequa have offered to liaison between us and the Tanoch if we agree to run some errands for them.
	* Type:	Main
	* FollowUps:	ql_main_t2_largeWpnParts, ql_main_t2_largeMchParts
	* Goals:	CompleteQuest,0, Goto,1
	* GoalParameters:	Amount&3;Ids&qm_t2_facIyatequa_A|qm_t2_facIyatequa_B|qm_t2_facIyatequa_C|qm_t2_facIyatequa_D, Target&[-1822, -636];TargetMode&Station

## ql_main_t2_strikeStationDefense

### qm_t2_strikeStationDefense: Station Defense
A large Tanoch station is under attack by a large fleet of pirates. We should band together with other fleets to repel the attackers.
	* Type:	Side
	* Goals:	CompleteQuest,0
	* GoalParameters:	Ids&qr_014;Amount&1

## ql_main_t2_largeWpnParts

### qm_t2_liaisonTanoch: Tanoch Relations
The Tanoch liaison office will offer better items the higher our reputation is.
	* Type:	Main
	* Goals:	CompleteQuest,0
	* GoalParameters:	Amount&10;Tags&Faction_Tanoch_T2up

### qm_t2_largeWeaponParts: Large Weapon Parts Assembly
Large weapon parts are required for building flagships and weapon modules.

The blueprint for large weapon parts can be found in the Tanoch liaison requisitions office.
	* Type:	Main
	* FollowUps:	ql_main_t2_flagship
	* Goals:	Craft,0
	* GoalParameters:	Tags&Part_Weapon_L_T2;Amount&100;Category&Crafting

## ql_main_t2_largeMchParts

### qm_t2_liaisonIyatequa: Iyatequa Relations
The Iyatequa liaison office will offer better items the higher our reputation is.
	* Type:	Main
	* Goals:	CompleteQuest,0
	* GoalParameters:	Amount&10;Tags&Faction_Tr1_T2up

### qm_t2_largeMachineParts: Large Machinery Parts Assembly
Large machinery parts are required for building flagships and non-weapon modules.

The blueprint for large machinery parts can be found in the Iyatequa liaison requisitions office.
	* Type:	Main
	* FollowUps:	ql_main_t2_flagship
	* Goals:	Craft,0
	* GoalParameters:	Tags&Part_Module_L_T2;Amount&100;Category&Crafting

## ql_main_t2_flagship

### qm_t2_startCraftFlagship: Flagship Construction T2
Now that we have the necessary resources, we can start building our new flagship. Its larger drive core will allow us to enter Tanoch territory. Flagship blueprints are available in the market.
	* Type:	Main
	* FollowUps:	ql_Keid, ql_main_t2_strikePahrasRock, ql_raid_015
	* Goals:	CompleteQuest,0, StartCraft,1
	* GoalParameters:	Amount&2;Ids&qm_t2_largeWeaponParts|qm_t2_largeMachineParts, Category&Crafting;Tags&Flagship_Ship_T2

### qm_t2_finCraftFlagship: Flagship T2
The construction of our new flagship is under way. Once it's finished, we can switch over and move our squadrons and officers as well as modules to the new flagship.
	* Type:	Main
	* FollowUps:	ql_main_t2_tanochet, ql_main_t2_turrets
	* Goals:	Craft,0
	* GoalParameters:	Category&Crafting;Tags&Flagship_Ship_T2

## ql_main_t2_strikePahrasRock

### qm_t2_strikePahrasRock: Pahra's Rock
Pirate's major Asteroid Base in the area has been threatening the Hiigaran settlements. Hiigaran Flagships have been gathered to strike on this Base.​
	* Type:	Side
	* Goals:	CompleteQuest,0
	* GoalParameters:	Ids&qr_015;Amount&1

## ql_main_t2_turrets

### qm_t2_turrets: Weapon Turrets T2
We should stay up to date on weapon technology. Researching new weapon schematics will unlock better modules.
	* Type:	Side
	* Goals:	Craft,0, Craft,1, Equip,2
	* GoalParameters:	Category&Research;Id&rp_catTurrets1_bp_kinetic_t2_c, Category&Crafting;Tags&Weapon_Module_T2;Amount&1, Type&Weapon;Tags&T2up

## ql_main_t2_tanochet

### qm_t2_tanochet: Tanochet
We can finally reach the Tanoch capital. It is time to meet the emperor.
	* Type:	Main
	* CinematicIds:	30
	* ReplayMissionId:	story_C01_Tanochet, story_C01_Tanochet_heroic
	* FollowUps:	ql_main_t2_sideTano, ql_main_t2_epicSignals, qm_t2_facTanoch_A, qm_t2_facTanoch_B, qm_t2_facTanoch_C, qm_t2_facTanoch_D
	* Goals:	CompleteMission,0
	* GoalParameters:	Id&story_C01_Tanochet

## ql_main_t2_internals

### qm_t2_internalFabricator: Fabricator Module
Our new flagship offers the ability to reconfigure its internal layout.
	* Type:	Main
	* Goals:	Craft,0, Equip,1
	* GoalParameters:	Tags&Crafting_Factory, Type&Internal;Tags&Crafting_Factory

## ql_main_t2_epicSignals

### qm_t2_epicSignals: High Risk High Reward
Occasionally we come across high energy signals. It might be worth checking out, but it could also be a potential danger. We should proceed with caution.
	* Type:	Side
	* Goals:	Scan,0, CompleteMission,0
	* GoalParameters:	Tags&InGalaxy_T2up;Amount&1;Analyzed&True, Mode&Generated;Tags&Epic_T2up;Amount&1

## ql_main_t2_sideTano

### qm_t2_facTanoch: Tanoch Errands
The Tanoch have asked us to run some errands for them. This could be a chance for us to gain their trust.
	* Type:	Main
	* FollowUps:	ql_main_t2_sideYaot, ql_main_t2_compartments, qm_t2_facYaot_A, qm_t2_facYaot_B, qm_t2_facYaot_C, qm_t2_facYaot_D
	* Goals:	CompleteQuest,0, Goto,1
	* GoalParameters:	Amount&3;Ids&qm_t2_facTanoch_A|qm_t2_facTanoch_B|qm_t2_facTanoch_C|qm_t2_facTanoch_D, Target&[-1240, -410]

## ql_main_t2_upgradeInternals

### qm_t2_upgradeInternals: Internal Module Upgrades
Just like with weapon turrets, we can improve our internal module's performance through upgrades.
	* Type:	Main
	* Goals:	Craft,0
	* GoalParameters:	Category&Upgrade;Tags&Factory;Amount&2;MinLevel&5

### qm_t2_otherInternals: Compartments
Our flagship is sectioned into three compartments. We can install different modules in different compartments.
	* Type:	Side
	* Goals:	Equip,0, Equip,0
	* GoalParameters:	Type&Internal;Tags&Front, Type&Internal;Tags&Back

## ql_main_t2_compartments

### qm_t2_compartments: Compartments
Our flagship is sectioned into three compartments. We can install different modules in different compartments.
	* Type:	Side
	* Goals:	Equip,0, Equip,0
	* GoalParameters:	Type&Internal;Tags&Front, Type&Internal;Tags&Back

## ql_main_t2_sideYaot

### qm_t2_facYaot: Yaot Conflict
We have received assignments from both Tanochetlan and Lazarus station. They asked us to investigate the Yaot threat.
	* Type:	Main
	* FollowUps:	ql_main_t2_templeTonaati
	* Goals:	CompleteQuest,0, Goto,1
	* GoalParameters:	Amount&3;Ids&qm_t2_facYaot_A|qm_t2_facYaot_B|qm_t2_facYaot_C|qm_t2_facYaot_D, Target&[-1240, -410]

## ql_main_t2_templeTonaati

### qm_t2_templeTonaati: Temple Tonaati
We are following Vaygr fleet to find out their hidden plan.
	* Type:	Main
	* ReplayMissionId:	story_C02_TempleTonaati, story_C02_TempleTonaati_heroic
	* FollowUps:	ql_Exile, ql_side_exploration, ql_main_t3_jumpCap
	* Goals:	CompleteMission,0
	* GoalParameters:	Id&story_C02_TempleTonaati

## ql_main_t3_jumpCap

### qm_t3_researchJumpCap: Expanding the Horizon
Our scientists have come up with new theories on how to increase the power of our engines. With the new technology we should be able to enter space that was previously inaccessible to us.
	* Type:	Main
	* FollowUps:	ql_main_t3_intro
	* Goals:	Craft,0
	* GoalParameters:	Category&Research;Id&rp_catExpl_hyperCap_t3_c;MinLevel&1

## ql_main_t3_intro

### qm_t3_scouting: New Frontiers
With our improved hyperjump technology, we should upgrade our engines and sensors to explore the new areas.
	* Type:	Main
	* Goals:	Craft,0, Craft,0
	* GoalParameters:	Category&Upgrade;Tags&Engine;Amount&1;MinLevel&6, Category&Upgrade;Tags&Sensor;Amount&1;MinLevel&6

### qm_t3_scouting_scanBelts: Resource Scouting
Fleet command wants accurate maps of nearby asteroid clusters in order to chart resources and hazards. Contribute to this effort by scanning asteroid clusters.
	* Type:	Main
	* Goals:	Statistic,0
	* GoalParameters:	Id&ScannedBelt;Total&55

### qm_t3_scouting_scanJovian: Gas Giant Scan
New scanning protocols for scanning gas giants are being tested. Contribute to this test by fully scanning a gas giant.
	* Type:	Main
	* FollowUps:	ql_main_t3_gasMining, ql_main_t3_yaotLiaison
	* Goals:	Statistic,0
	* GoalParameters:	Id&ScannedJovian;Total&1

## ql_main_t3_gasMining

### qm_t3_gasMining: A New Resource
We found a new type of resource that warrants a closer look. We should take some samples for study. To harvest gas, simply send a Gas Collector into the atmosphere of a gas planet. Be careful. Deeper layers will deal more damage to your ships! The blueprint for the Gas Collector can be found in the Market.
	* Type:	Main
	* FollowUps:	ql_main_t3_sideYaot, ql_main_t3_sideYaot_A, ql_main_t3_sideYaot_B, ql_main_t3_sideYaot_C
	* Goals:	Craft,0, Statistic,1
	* GoalParameters:	Category&Crafting;Tags&GCol;Amount&1, Ids&Mined3E_Mined3F_Mined3G_Mined3H;Amount&1000

## ql_main_t3_yaotLiaison

### qm_t3_yaotLiaison: Yaot Relations
The Yaot have opened their liaison office to us.
	* Type:	Side
	* Goals:	Statistic,0
	* GoalParameters:	Id&RepYaot;Total&1000

## ql_main_t3_sideYaot

### qm_t3_facYaot: Uneasy Allies
The Yaot are interested in opening relations with us and wish to begin a dialogue.
	* Type:	Main
	* FollowUps:	ql_raid_017, ql_main_t3_sideTanoch, ql_main_t3_sideTanoch_A, ql_main_t3_sideTanoch_B, ql_main_t3_sideTanoch_C, ql_orb_t3_intro
	* Goals:	CompleteQuest,0, Goto,1
	* GoalParameters:	Amount&2;Ids&qm_t3_sideYaot_A_3|qm_t3_sideYaot_B_3|qm_t3_sideYaot_C_3, Target&[-942, -820]

## ql_main_t3_sideYaot_A

### qm_t3_sideYaot_A_1: Truce: Loadstones I
The Yaot present a simple request to map and gather resources in order to test our capabilities and their trust in us.
	* Type:	Side
	* Goals:	Statistic,0, Pay,0
	* GoalParameters:	Id&ScannedBelt;Total&65, Id&3O;Amount&50

### qm_t3_sideYaot_A_2: Truce: Loadstones II
The Yaot have asked us to collect further resources and clear the mining areas of hostiles.
	* Type:	Side
	* Goals:	Statistic,0, Statistic,0
	* GoalParameters:	Id&Mined3C;Amount&2500, Id&ShipsDestroyed;Amount&30

### qm_t3_sideYaot_A_3: Truce: Loadstones III
The Yaot are interested in learning our capacity for materials refining. We'll be compensated well.
	* Type:	Side
	* Goals:	Statistic,0, Pay,0
	* GoalParameters:	Id&Refining3N;Amount&300, Id&3N;Amount&100

## ql_main_t3_sideYaot_B

### qm_t3_sideYaot_B_1: Truce: The Privateer I
The Yaot have a supply line they want protected, and are willing to hire us to clear it of hostiles.
	* Type:	Side
	* Goals:	Scan,0, CompleteMission,0
	* GoalParameters:	Tags&InSystem_Generated_T3up;Amount&5;Analyzed&True, Amount&6;Tags&T2up;Mode&Generated

### qm_t3_sideYaot_B_2: Truce: The Privateer II
The Yaot wish to commission us to guard this patrol route until their own patrols can relieve us.
	* Type:	Side
	* Goals:	Statistic,0, GainItem,0
	* GoalParameters:	Id&ShipsDestroyed;Amount&30, Tags&Insignia;Amount&50;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qm_t3_sideYaot_B_3: Truce: The Privateer III
The Yaot are impressed with our combat capabilities and want to see how we fare against stronger enemies.
	* Type:	Side
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&3;Tags&T2up;Mode&Strike

## ql_main_t3_sideYaot_C

### qm_t3_sideYaot_C_1: Truce: Exchange of Ideas I
The Yaot have made more contracts available to us on a trial basis. We should engage them.
	* Type:	Side
	* Goals:	CompleteQuest,0
	* GoalParameters:	Amount&5;Tags&Faction_Yaot_T3up

### qm_t3_sideYaot_C_2: Truce: Exchange of Ideas II
The Yaot are becoming more comfortable with employing us. More work for them will go a long way to improving relations.
	* Type:	Side
	* Goals:	Statistic,0, Statistic,0
	* GoalParameters:	Id&RepYaot;Amount&250, Id&ShipsDestroyed;Amount&30

### qm_t3_sideYaot_C_3: Truce: Exchange of Ideas III
The Yaot trust us enough to employ our services on a contract basis. More work is available.
	* Type:	Side
	* Goals:	GainItem,0, Statistic,0
	* GoalParameters:	Tags&Insignia;Amount&65;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash, Id&RepYaot;Total&4050

## ql_main_t3_sideTanoch

### qm_t3_facTanoch: Inside the Empire
We have been contacted by the Chicuat people within the Tanoch empire. They have been denied Imperial services and are asking us for help.
	* Type:	Main
	* FollowUps:	ql_raid_018, ql_main_t3_starTotek
	* Goals:	CompleteQuest,0, Goto,1
	* GoalParameters:	Amount&2;Ids&qm_t3_sideTanoch_A_3|qm_t3_sideTanoch_B_3|qm_t3_sideTanoch_C_3, Target&[-1240, -410]

## ql_main_t3_sideTanoch_A

### qm_t3_sideTanoch_A_1: Chicuat: Dry Well I
Next to no Imperial resources are reaching the Chicuat worlds. They are asking us to provide what we spare.
	* Type:	Side
	* Goals:	Pay,0, Pay,0, Pay,0
	* GoalParameters:	Id&3A;Amount&400, Id&3B;Amount&200, Id&3C;Amount&1400

### qm_t3_sideTanoch_A_2: Chicuat: Dry Well II
The Chicuat refineries are busy with the ores we have provided. Meanwhile, an agricultural colony providing most of the food in the sector is running on systems that are barely holding together. They have asked us for spare parts.
	* Type:	Side
	* Goals:	Pay,0
	* GoalParameters:	Id&intmed_module_large_t2;Amount&15

### qm_t3_sideTanoch_A_3: Chicuat: Dry Well III
The economic system has been stabilized, but without proper defenses, raiders will undo everything we've done. We should provide them with some fighters of their own and give their militia some training.
	* Type:	Side
	* Goals:	Pay,0, Pay,0, CompleteMission,1
	* GoalParameters:	Id&intmed_ship_small_t3;Amount&50, Id&intmed_weapon_small_t3;Amount&50, Amount&5

## ql_main_t3_sideTanoch_B

### qm_t3_sideTanoch_B_1: Chicuat: Exposed I
Without Imperial patrols, Chicuat space is vulnerable against raiders. They have asked us to make a sweep across their space to clear the sector of hostiles.
	* Type:	Side
	* Goals:	Scan,0, Statistic,0
	* GoalParameters:	Tags&InSystem_T3up;Amount&6;Analyzed&True, Id&ShipsDestroyed;Amount&35

### qm_t3_sideTanoch_B_2: Chicuat: Exposed II
Most hostiles have been chased off, but some bold bands of the Fleet of Rams have refused to be intimidated. It is time to make a statement.
	* Type:	Side
	* Goals:	CompleteMission,0, Statistic,0
	* GoalParameters:	Amount&7, Id&ShipsDestroyedP1;Amount&25

### qm_t3_sideTanoch_B_3: Chicuat: Exposed III
The Chicuat officials have seen our results and several of them want to see us in action. They hope to learn from us how to organize their defenses better.
	* Type:	Side
	* Goals:	CompleteMission,0, GainItem,0
	* GoalParameters:	Amount&3;Tags&T2up;Mode&Strike, Tags&StrikeToken;Amount&6;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

## ql_main_t3_sideTanoch_C

### qm_t3_sideTanoch_C_1: Chicuat: Favors I
Our contact has suggested running some errands for the Tanoch in the name of the Chicuat people. Doing so would hopefully increase the Chicuat's standing within the Empire.
	* Type:	Side
	* Goals:	Statistic,0
	* GoalParameters:	Id&RepTanoch;Amount&500

### qm_t3_sideTanoch_C_2: Chicuat: Favors II
The Empire is reacting to our support of the Chicuat people. While we wait to learn more about the outcome, the Chicuat have asked if their officers can cross-train with ours.
	* Type:	Side
	* Goals:	UpgradeOfficer,0, CompleteQuest,0
	* GoalParameters:	Amount&15, Amount&7;Tags&Faction_Tanoch_T2up

### qm_t3_sideTanoch_C_3: Chicuat: Favors III
After lengthy negotiations with the Chicuat, the Empire reluctantly has agreed to a relief operation, sending resources to worlds in need. Naturally they ask us for support instead of sending their own materials...
	* Type:	Side
	* Goals:	Statistic,0, Statistic,0
	* GoalParameters:	Id&RepTanoch;Total&8500, Ids&Refining3N_Refining3O_Refining3P_Refining3Q;Amount&600

## ql_main_t3_starTotek

### qm_t3_starTotek: Star Totek
We are closing in on possible Vaygr transmissions close to the star.
	* Type:	Main
	* ReplayMissionId:	story_C03_StarTotek, story_C03_StarTotek_heroic
	* FollowUps:	ql_main_t3_sideHiig, ql_main_t3_sideHiig_A, ql_main_t3_sideHiig_B, ql_main_t3_sideHiig_C, ql_main_t3_strikeBreach, ql_raid_019
	* Goals:	CompleteMission,0
	* GoalParameters:	Id&story_C03_StarTotek

## ql_main_t3_strikeBreach

### qm_t3_strikeBreach: Breach
We found an enemy base that is heavily fortified. Breaching its defenses will not be easy.
	* Type:	Side
	* Goals:	CompleteQuest,0
	* GoalParameters:	Ids&qr_019;Amount&1

## ql_main_t3_sideHiig

### qm_t3_facHiigaran: Planting the Flag
Lazarus Base calls us back to the Hiigaran colonies to establish a presence there and keep the peace.
	* Type:	Main
	* FollowUps:	ql_main_t3_sideIyat, ql_main_t3_sideIyat_A, ql_main_t3_sideIyat_B, ql_main_t3_sideIyat_C
	* Goals:	CompleteQuest,0, Goto,1
	* GoalParameters:	Amount&2;Ids&qm_t3_sideHiigaran_A_3|qm_t3_sideHiigaran_B_3|qm_t3_sideHiigaran_C_3, Target&[-1822, -636]

## ql_main_t3_sideHiig_A

### qm_t3_sideHiigaran_A_1: Colonies: Brick Making I
Hiigaran resource efforts are very short handed, so we’ll be going to assist gas collection in deep space.
	* Type:	Side
	* Goals:	Statistic,0, Statistic,0
	* GoalParameters:	Id&ScannedJovian;Total&20, Ids&Mined3E_Mined3F_Mined3G_Mined3H;Amount&600

### qm_t3_sideHiigaran_A_2: Colonies: Brick Making II
Our assistance has been helpful so far, but we are asked to provide and analyze some ore samples from the deeper regions of the galaxy.
	* Type:	Side
	* Goals:	Statistic,0, GainItem,0
	* GoalParameters:	Ids&Mined3A_Mined3B_Mined3C_Mined3D;Amount&5000, Id&RP;Amount&35;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qm_t3_sideHiigaran_A_3: Colonies: Brick Making III
The logistics have been set up for the most part, but we are asked to help with some deliveries.
	* Type:	Side
	* Goals:	Pay,0, Pay,0, Pay,0
	* GoalParameters:	Id&3G;Amount&100, Id&3O;Amount&200, Id&intmed_ship_small_t3;Amount&40

## ql_main_t3_sideHiig_B

### qm_t3_sideHiigaran_B_1: Colonies: Security Blanket I
Lazarus base has established a quota for all commanders hunting loose pirates in Hiigaran space.
	* Type:	Side
	* Goals:	Statistic,0, GainItem,0
	* GoalParameters:	Id&ShipsDestroyedP1;Amount&30, Tags&Insignia;Amount&40;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qm_t3_sideHiigaran_B_2: Colonies: Security Blanket II
Most pirates have gone into hiding, but we are asked to make sweeps of local space, to flush out the remaining hostiles.
	* Type:	Side
	* Goals:	Scan,0, CompleteMission,0
	* GoalParameters:	Tags&InSystem_Generated_T3up;Amount&7;Analyzed&True, Amount&5;Tags&T3up;Mode&Generated

### qm_t3_sideHiigaran_B_3: Colonies: Security Blanket III
The hostile presence has been reduced to a manageable level, but Progenitor craft threaten research vessels. We need to get rid of them and analyze some of the debris.
	* Type:	Side
	* Goals:	Statistic,0, GainItem,0
	* GoalParameters:	Id&ShipsDestroyedProgenitor;Amount&15, Id&RP;Amount&45;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

## ql_main_t3_sideHiig_C

### qm_t3_sideHiigaran_C_1: Colonies: The Next Generation I
Lazarus has sent us some trainees to get some practical experience on our ship.
	* Type:	Side
	* Goals:	GainItem,0, Statistic,0
	* GoalParameters:	Id&LP;Amount&12;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash, Id&PlayerXP;Amount&2000

### qm_t3_sideHiigaran_C_2: Colonies: The Next Generation II
Many of the trainees are going to become pilots and navigators, but have so far trained in controlled or virtual flight simulators. They need some real experience.
	* Type:	Side
	* Goals:	Craft,0, UpgradeOfficer,0
	* GoalParameters:	Category&Crafting;Tags&Ship_Unit_T3up;Amount&5, Amount&20

### qm_t3_sideHiigaran_C_3: Colonies: The Next Generation III
The final course is the graduation level for the trainees, who must see actual combat. You are to take the crew into battle and complete the course. Once finished, they return to Lazarus to finish up their coursework.
	* Type:	Side
	* Goals:	CompleteMission,0, UpgradeOfficer,1
	* GoalParameters:	Amount&10, Amount&5;MinLevel&20

## ql_main_t3_sideIyat

### qm_t3_facIyatequa: Blue Collar Work
Ekekko informed us about exclusive work needed by the Iyatequa, and the traders will pay well for this assistance. This is below the table work on various jobs they don’t widely advertise for. They do not say what the ultimate purpose of this work is, though.
	* Type:	Main
	* FollowUps:	ql_main_t3_Cang, ql_main_t3_Cang_A, ql_main_t3_Cang_B, ql_main_t3_Cang_C
	* Goals:	CompleteQuest,0, Goto,1
	* GoalParameters:	Amount&2;Ids&qm_t3_sideIyatequa_A_3|qm_t3_sideIyatequa_B_3|qm_t3_sideIyatequa_C_3, Target&[-1543, -626]

## ql_main_t3_sideIyat_A

### qm_t3_sideIyatequa_A_1: Contracts: The Empty Quarter I
A small world in the Empty Quarter is looking for trustworthy connections. They offer an assortment of various tasks.
	* Type:	Side
	* Goals:	CompleteQuest,0, Statistic,0
	* GoalParameters:	Amount&7;Tags&Faction_Tr1_T3up, Id&PlayerXP;Amount&2250

### qm_t3_sideIyatequa_A_2: Contracts: The Empty Quarter II
A wealthy socialite has heard of our accomplishments and wants some things done. Discreetly, of course.
	* Type:	Side
	* Goals:	Statistic,0, Statistic,0
	* GoalParameters:	Id&RepTr1;Amount&500, Ids&Refining3N_Refining3O_Refining3P_Refining3Q;Amount&1000

### qm_t3_sideIyatequa_A_3: Contracts: The Empty Quarter III
Our contact in the Empty Quarter is looking for new opportunities and has been pleased with our work so far. They want us to scout out new areas of space in order to expand their influence.
	* Type:	Side
	* Goals:	Statistic,0, Scan,0
	* GoalParameters:	Id&RepTr1;Total&8500, Tags&InGalaxy_T3up;Amount&5;Analyzed&True

## ql_main_t3_sideIyat_B

### qm_t3_sideIyatequa_B_1: Contracts: Territory Claim I
The Iyatequa plan to set up new trading routes in space currently riddled by pirates. They asked us to clean up the area.
	* Type:	Side
	* Goals:	Scan,0, Statistic,0
	* GoalParameters:	Tags&InSystem_Generated_T3up;Amount&8;Analyzed&True, Id&ShipsDestroyedP1;Amount&35

### qm_t3_sideIyatequa_B_2: Contracts: Territory Claim II
Some pirates apparently didn't get the hint yet. We should show them the Iyatequa mean business.
	* Type:	Side
	* Goals:	CompleteMission,0, GainItem,0
	* GoalParameters:	Amount&8;Tags&T3up;Mode&Generated, Tags&Insignia;Amount&60;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qm_t3_sideIyatequa_B_3: Contracts: Territory Claim III
Most pirates have dispersed, but just to make sure they do not come back we should increase our reputation so future raiders will think twice before setting up nests here.
	* Type:	Side
	* Goals:	CompleteMission,0, CompleteMission,0
	* GoalParameters:	Amount&5;Tags&T2up;Mode&Strike, Amount&2;Tags&T3up;Mode&Strike

## ql_main_t3_sideIyat_C

### qm_t3_sideIyatequa_C_1: Contracts: Supplies I
A local world wants help building and supplying a space station. We are asked to test possible mining sites and clear them of hostiles.
	* Type:	Side
	* Goals:	Statistic,0, Statistic,0
	* GoalParameters:	Ids&Mined3A_Mined3B_Mined3C_Mined3D;Amount&6000, Id&ShipsDestroyed;Amount&55

### qm_t3_sideIyatequa_C_2: Contracts: Supplies II
Mining ships have departed for the asteroids we have charted, but the internal systems require special gases. We are asked to sample the gases at promising jovians.
	* Type:	Side
	* Goals:	Statistic,0, Statistic,0
	* GoalParameters:	Ids&Mined3E_Mined3F_Mined3G_Mined3H;Amount&600, Id&Mined3H;Amount&100

### qm_t3_sideIyatequa_C_3: Contracts: Supplies III
The mining sites have been prepared, but the Iyatequa asked us with further assistance through supplies and mining craft.
	* Type:	Side
	* Goals:	Pay,0, Pay,0, Pay,0
	* GoalParameters:	Id&3G;Amount&150, Id&3O;Amount&300, Id&intmed_ship_small_t3;Amount&50

## ql_main_t3_Cang

### qm_t3_facCangacian: Roadblocks
Reports at the Tanoch border are coming in stating that the Fleet of Rams, Supay’s army, is on the move at last.
	* Type:	Main
	* FollowUps:	ql_main_t3_sijinLighthouse
	* Goals:	CompleteQuest,0
	* GoalParameters:	Amount&2;Ids&qm_t3_sideCangacian_A_3|qm_t3_sideCangacian_B_3|qm_t3_sideCangacian_C_3

## ql_main_t3_Cang_A

### qm_t3_sideCangacian_A_1: Defense: Intercept I
We are asked to intercept as many Cangacian fleets as we can.
	* Type:	Side
	* Goals:	Statistic,0, GainItem,0
	* GoalParameters:	Id&ShipsDestroyedP1;Amount&40, Id&LP;Amount&12;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qm_t3_sideCangacian_A_2: Defense: Intercept II
The Cangacians continue to probe the Tanoch defenses. We should look for suspicious activity.
	* Type:	Side
	* Goals:	Scan,0, CompleteMission,0
	* GoalParameters:	Tags&InSystem_Generated_T3up;Amount&9;Analyzed&True, Amount&9;Tags&T3up;Mode&Generated

### qm_t3_sideCangacian_A_3: Defense: Intercept III
Supay's fleets may have holdouts in systems we have not been looking yet. We should find those and flush them out.
	* Type:	Side
	* Goals:	CompleteMission,0, Scan,0
	* GoalParameters:	Amount&4;Tags&T3up;Mode&Strike, Tags&InGalaxy_T3up;Amount&10;Analyzed&True

## ql_main_t3_Cang_B

### qm_t3_sideCangacian_B_1: Defense: Assist I
To counter these attacks our crew must be well trained.
	* Type:	Side
	* Goals:	GainItem,0, UpgradeOfficer,0
	* GoalParameters:	Tags&Insignia;Amount&80;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash, Amount&25

### qm_t3_sideCangacian_B_2: Defense: Assist II
Our crew is analyzing the attack patterns to find ways to predict where the Fleet of Rams may strike next.
	* Type:	Side
	* Goals:	GainItem,0, Statistic,0
	* GoalParameters:	Id&RP;Amount&50;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash, Id&PlayerXP;Amount&2500

### qm_t3_sideCangacian_B_3: Defense: Assist III
Several smaller worlds on the border have sent us some of their recruits, in hopes they could get some practical experience from our battles with the Cangacians.
	* Type:	Side
	* Goals:	CompleteMission,0, UpgradeOfficer,1
	* GoalParameters:	Amount&10, Amount&5;MinLevel&25

## ql_main_t3_Cang_C

### qm_t3_sideCangacian_C_1: Defense: Barricade I
Several mining fleets of the border systems have taken losses and are asking us to provide them with safe locations to find resources.
	* Type:	Side
	* Goals:	Statistic,0, Statistic,0
	* GoalParameters:	Id&ScannedBelt;Total&80, Ids&Refining3N_Refining3O_Refining3P_Refining3Q;Amount&1500

### qm_t3_sideCangacian_C_2: Defense: Barricade II
The remaining mining fleets are flocking to the new mining spots, but they require gases for advanced weaponry.
	* Type:	Side
	* Goals:	Statistic,0, Statistic,0
	* GoalParameters:	Id&ScannedJovian;Total&40, Ids&Mined3E_Mined3F_Mined3G_Mined3H;Amount&750

### qm_t3_sideCangacian_C_3: Defense: Barricade III
The border worlds' new mining lanes are buzzing with activity, but they need supplies to build up defenses against future raids.
	* Type:	Side
	* Goals:	Pay,0, Pay,0, Pay,0
	* GoalParameters:	Id&intmed_ship_small_t3;Amount&20, Id&intmed_weapon_small_t3;Amount&20, Id&intmed_module_small_t3;Amount&20

## ql_main_t3_sijinLighthouse

### qm_t3_sijinLighthouse: Sijin Lighthouse
We detected a possible signal from the missing Khar-Kalaad.
	* Type:	Main
	* CinematicIds:	40
	* ReplayMissionId:	story_D01_SijinLighthouse, story_D01_SijinLighthouse_heroic
	* FollowUps:	ql_main_t4_intro
	* Goals:	CompleteMission,0
	* GoalParameters:	Id&story_D01_SijinLighthouse

## ql_main_t4_intro

### qm_t4_researchJumpCap: Mind the Gap
Crossing the Nightmare Gulf requires an upgrade to our hyperjump technology. After some scans of the gate at Sijin Lighthouse, our scientists think they are able to make the leap possible.
	* Type:	Main
	* FollowUps:	ql_main_t4_iliyinLighthouse
	* Goals:	Craft,0
	* GoalParameters:	Category&Research;Id&rp_catExpl_hyperCap_t4_c;MinLevel&1

## ql_main_t4_iliyinLighthouse

### qm_t4_iliyinLighthouse: Iliyin Lighthouse
We have arrived at another lighthouse in uncharted territory. Be prepared for anything.
	* Type:	Main
	* ReplayMissionId:	story_D02_IliyinLighthouse, story_D02_IliyinLighthouse_heroic
	* FollowUps:	ql_raid_020, ql_raid_021, ql_raid_022, ql_main_t4_amassariLiaison, ql_main_t4_moonResources
	* Goals:	CompleteMission,0
	* GoalParameters:	Id&story_D02_IliyinLighthouse

## ql_main_t4_amassariLiaison

### qm_t4_amassariLiaison: Amassari Relations
The Amassari have opened their liaison office to us.
	* Type:	Side
	* Goals:	Statistic,0
	* GoalParameters:	Id&RepAmassari;Total&1000

## ql_main_t4_moonResources

### qm_t4_moonResources: Crystals
Crystals are a new type of resource that can be combined with refined metals into a composite material needed for advanced constructions. So far we have only been able to find them by chance in <color=#FBB03F>signals and liaison missions</color>.
	* Type:	Main
	* FollowUps:	ql_main_t4_brightTemple
	* Goals:	GainItem,0, Statistic,1
	* GoalParameters:	Tags&Moon_Crud;Amount&200;ExcludedSources&PayGoal_BuyItem_SellItem_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash, Ids&Refining4V_Refining4W_Refining4X_Refining4Y;Amount&100

## ql_main_t4_brightTemple

### qm_t4_brightTemple: Bright Temple
The Amassari here may contain answers about the nature of the Progenitor observer.
	* Type:	Main
	* ReplayMissionId:	story_D03_BrightTemple, story_D03_BrightTemple_heroic
	* FollowUps:	ql_main_t4_postBrightTemple
	* Goals:	CompleteMission,0
	* GoalParameters:	Id&story_D03_BrightTemple

## ql_main_t4_postBrightTemple

### qm_t4_postBrightTemple_1: Among the People
We should take this time to become better acquainted with the Amassari and their culture. Performing tasks for the assorted groups will accomplish this.
	* Type:	Main
	* Goals:	Statistic,0
	* GoalParameters:	Id&RepAmassari;Amount&1000

### qm_t4_postBrightTemple_2: Fabrication Methods
A new technique for refining was discovered from the Amassari. Test this process by refining rare earths.
	* Type:	Main
	* Goals:	GainItem,0
	* GoalParameters:	Tags&RareEarth_T4up;Amount&300;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qm_t4_postBrightTemple_3: Experience and Knowledge
Our crews need a new round of training to become familiar with Amassari practices and tactics.
	* Type:	Main
	* FollowUps:	ql_main_t4_hataldan
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Insignia;Amount&600;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

## ql_main_t4_hataldan

### qm_t4_hataldan: Hataldan
The fallen capital of the Amassari, and last known position of the Observer.
	* Type:	Main
	* ReplayMissionId:	story_D04_Hataldan, story_D04_Hataldan_heroic
	* FollowUps:	ql_main_t4_postHataldan
	* Goals:	CompleteMission,0
	* GoalParameters:	Id&story_D04_Hataldan

## ql_main_t4_postHataldan

### qm_t4_postHataldan_1: The Hunt Begins
The search begins for Kidara and the stolen Observer. We must examine any objects we can find scattered around for clues about her whereabouts.
	* Type:	Main
	* Goals:	Scan,0
	* GoalParameters:	Tags&InSystem_Container_T4up;Amount&10;Analyzed&True

### qm_t4_postHataldan_2: Forcible Interrogation
Destroying Kiithless ships and scavenging their databanks could fill some gaps in our intelligence about the Kiithless. The hunt continues!
	* Type:	Main
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedDarkHiigaranT4;Amount&50

### qm_t4_postHataldan_3: Pieces of the Puzzle
A cryptic clue that emerged from harvesting Kiithless vessels may have a solution if we can piece together a saga from the Hagthar Empire. Collect relics from these ancient people.
	* Type:	Main
	* FollowUps:	ql_main_t4_nightmareGulf
	* Goals:	GainItem,0
	* GoalParameters:	Id&ama_collectable_u_01;Amount&15;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

## ql_main_t4_nightmareGulf

### qm_t4_nightmareGulf: Nightmare Gulf
The Hagthar knew of pockets and safe regions close to this massive interstellar storm. We now know the way to Kidara's hideout in The Nightmare Gulf. It's time to end this.
	* Type:	Main
	* ReplayMissionId:	story_D05_NightmareGulf, story_D05_NightmareGulf_heroic
	* FollowUps:	ql_raid_023, ql_main_t4_strikeNightmareGulf, ql_main_t4_tanWin
	* Goals:	CompleteMission,0
	* GoalParameters:	Id&story_D05_NightmareGulf

## ql_main_t4_strikeNightmareGulf

### qm_t4_strikeNightmareGulf: Strike at Nightmare Gulf
The Hagthar knew of pockets and safe regions close to this massive interstellar storm. We now know the way to Kidara's hideout in The Nightmare Gulf. It's time to end this.
	* Type:	Side
	* Goals:	CompleteQuest,0
	* GoalParameters:	Ids&qr_023;Amount&1

## ql_main_t4_tanWin

### qm_t4_tanWin_DefendBase: Gesture of Aid
We received emergency communication from the Chicuat Elders. They anticipate a raid on one of their remote trading stations. Toci asks us to take on the defense in order to relieve the weakened and overextended Chicuat forces.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
	* Type:	Main
	* ReplayMissionId:	event_tanWin2023_DefendBase_t4
	* Goals:	CompleteMission,0
	* GoalParameters:	Id&event_tanWin2023_DefendBase_t4

### qm_t4_tanWin_AttackBase: In the Shadows
Intelligence from the Chicuat points to a Tecuban base operating around an uninhabited planet. We must go there and eliminate this base to stop the raids.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
	* Type:	Main
	* ReplayMissionId:	event_tanWin2023_AttackBase_t4
	* Goals:	CompleteMission,0
	* GoalParameters:	Id&event_tanWin2023_AttackBase_t4

### qm_t4_tanWin_Relic: Attack the Vaygr
In our search for the Vaygr involved with the Tecuban, we aquired one of their communication frequencies. If we contact the Vaygr now, we should be able to trace their signal and hyper jump to their exact location.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
	* Type:	Main
	* ReplayMissionId:	event_tanWin2023_Relic_t4
	* Goals:	CompleteMission,0
	* GoalParameters:	Id&event_tanWin2023_Relic_t4

### qm_t4_tanWin_Academy: Showdown at the Academy
We finally learned Jochik Kaan's intentions. He sparked the flames of war to weaken the Chicuat defenses and steal the Baetyl from Tlapallan Academy, one of their key centers of learning. We must travel there at once, before it is too late.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
	* Type:	Main
	* ReplayMissionId:	event_tanWin2023_Academy_t4
	* FollowUps:	ql_main_t4_yaoSpr
	* Goals:	CompleteMission,0
	* GoalParameters:	Id&event_tanWin2023_Academy_t4

## ql_main_t4_yaoSpr

### qm_t4_yaoSpr_Conjunction: The Promised Place
Chocoan has provided the coordinates to the next astral conjunction event. Strong hostile forces are to be expected in this system. Our goal is to both protect the civilian pilgrims and find out more about the suspected secret agenda of the Yaot Elders.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
	* Type:	Main
	* ReplayMissionId:	event_yaoSpr2024_Conjunction_t4
	* Goals:	CompleteMission,0
	* GoalParameters:	Id&event_yaoSpr2024_Conjunction_t4

## ql_orb_t3_intro

### qm_orb_t3_components: Starbase Components
<color=#FBB03F>The blueprints for starbase components can be found in the liaison requisitions offices.</color>

Our engineers have come up with a plan to build a starbase, which will serve as our base of operations. Before we can do that, however, we need to construct the necessary components.
	* Type:	Side
	* Goals:	Craft,0, Craft,0, Craft,0
	* GoalParameters:	Id&playerOrb_comp_stabilizer_t3, Id&playerOrb_comp_frame_t3, Id&playerOrb_comp_lifeSupport_t3

### qm_orb_t3_orbital: Starbase
<color=#FBB03F>The blueprint for the starbase can be found in the regular market.</color>

Now that we have the components, we can build the starbase proper. Once the pieces have been constructed, it can be quickly assembled in orbit around celestial objects.
	* Type:	Side
	* Goals:	Craft,0
	* GoalParameters:	Id&hgn_co_orbi_01_t1

### qm_orb_t3_placeOrbital: Starbase Placement
<color=#FBB03F>Place or relocate your starbase by selecting a celestial object in the target list inside the star system view.</color>

Our finished starbase is ready and can be placed in orbit of a planet or moon.
	* Type:	Side
	* Goals:	PlaceOrbital,0
	* GoalParameters:	NoParameter&None

### qm_orb_t3_modules: Starbase Modules
<color=#FBB03F>The regular fabricator and refinery module can be mounted on the starbase, but there are specialized starbase modules. Blueprints for some of those can be found in the liaison requisitions offices.</color>

Now that our starbase is finished, we can start filling it up with modules.
	* Type:	Side
	* Goals:	Equip,0
	* GoalParameters:	Type&Internal;Tags&Orbital;Target&hgn_co_orbi_01_t1

## ql_side_exploration

### qs_exploration_01: Exploration I
We should explore this galaxy further. Who knows what we could find.
	* Type:	Side
	* FollowUps:	ql_side_001
	* Goals:	Scan,0, CompleteMission,0
	* GoalParameters:	Tags&InSystem;Amount&15;Analyzed&True, Amount&10;Tier&2;Mode&Generated

### qs_exploration_02: Exploration II
We have made discoveries that will keep our scientists busy for months.
	* Type:	Side
	* FollowUps:	ql_side_002
	* Goals:	GainItem,0
	* GoalParameters:	Id&RP;Amount&900;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qs_exploration_03: Exploration III
This galaxy is full of danger and opportunity. We should analyze and prepare.
	* Type:	Side
	* FollowUps:	ql_Ytep
	* Goals:	Scan,0, Pay,1
	* GoalParameters:	Tags&InSystem;Amount&25;Analyzed&True, Id&2P;Amount&5000

## ql_side_001

### qs_economy_01: Production I
Building up a fleet requires a constant supply of materials.
	* Type:	Side
	* Goals:	Craft,0, CompleteMission,0
	* GoalParameters:	Category&Refining;Amount&2000, Amount&5;Tier&2;Mode&Generated

### qs_economy_02: Production II
We should not let our fabrication modules go idle.
	* Type:	Side
	* Goals:	Craft,0
	* GoalParameters:	Category&Crafting;Amount&50

### qs_economy_03: Production III
Building bigger and greater ships will require bigger and greater materials.
	* Type:	Side
	* Goals:	Craft,0, Pay,1
	* GoalParameters:	Category&Refining;Amount&4500, Id&2N;Amount&5000

## ql_side_002

### qs_battle_01: Combat I
Space is full of danger. We need to be prepared.
	* Type:	Side
	* Goals:	Craft,0, CompleteMission,0
	* GoalParameters:	Category&Upgrade;Amount&10, Amount&15;Tier&2;Mode&Generated

### qs_battle_02: Combat II
We need allies if we are to survive in this galaxy.
	* Type:	Side
	* Goals:	CompleteQuest,0
	* GoalParameters:	Amount&25;Tags&Faction_T2up

### qs_battle_03: Combat III
Only great challenges yield great rewards.
	* Type:	Side
	* Goals:	CompleteMission,0, Pay,1
	* GoalParameters:	Amount&1;Tier&2;Mode&Strike, Id&2O;Amount&5000

## ql_side_unlockStrikes_t2

### qs_unlockStrikes_t2: Rising to the Challenge
As we venture further into this galaxy, we will encounter greater and greater threats. We need to be prepared.
	* Type:	Side
	* FollowUps:	ql_raid_014, ql_raid_015, ql_raid_016
	* Goals:	Equip,0
	* GoalParameters:	Type&Flagship;Tags&T1

## ql_side_unlockStrikes_t3

### qs_unlockStrikes_t3: Rising to the Challenge
As we venture further into this galaxy, we will encounter greater and greater threats. We need to be prepared.
	* Type:	Side
	* FollowUps:	ql_raid_017, ql_raid_018
	* Goals:	Equip,0
	* GoalParameters:	Type&Flagship;Tags&T2

## ql_Keid

### qs_Keid_01: The Siege of Keid
Keid is struggling under the weight of enemy attacks and depleted resources. Help them take back control of the system.
	* Type:	Side
	* Goals:	Goto,0, Scan,1, CompleteMission,1, Statistic,1
	* GoalParameters:	Target&[-1784, -564];TargetMode&Station, Tags&InSystem_T2up;Amount&10;Analyzed&True, Mode&Generated;Tier&2;Amount&10, Id&ShipsDestroyedT2;Amount&50

### qs_Keid_02: Rebuilding Keid
The people of Keid suffer from a lack of resources. Support them by collecting and refining resources.
	* Type:	Side
	* Goals:	Statistic,0, Statistic,0, Statistic,0, Statistic,0, Statistic,1, Statistic,1, Statistic,1, Statistic,1
	* GoalParameters:	Id&Mined2A;Amount&2000, Id&Mined2B;Amount&2000, Id&Mined2C;Amount&2000, Id&Mined2D;Amount&1500, Id&Refining2N;Amount&1000, Id&Refining2O;Amount&1000, Id&Refining2P;Amount&1000, Id&Refining2Q;Amount&700

### qs_Keid_03: The Future of Keid
Donate your hard-earned resources and credits so that the people of Keid may fight on.
	* Type:	Side
	* Goals:	Pay,0, Pay,0, Pay,0, Pay,1, Pay,1
	* GoalParameters:	Id&2N;Amount&1000;SysId&[-1784, -564], Id&2O;Amount&1000;SysId&[-1784, -564], Id&2P;Amount&1000;SysId&[-1784, -564], Id&2Q;Amount&700;SysId&[-1784, -564], Id&CR;Amount&10000;SysId&[-1784, -564]

## ql_Exile

### qs_Exile_01: A Test of Might
Destroy pirates and complete strikes to prove your strength.
	* Type:	Side
	* Goals:	CompleteMission,0, Statistic,0
	* GoalParameters:	Amount&10;Tier&2;Mode&Strike, Id&ShipsDestroyedP1;Amount&150

### qs_Exile_02: The Nomad's Walk
Gather resources and craft units to demonstrate your independence and self-reliance.
	* Type:	Side
	* Goals:	Statistic,0, Statistic,0, Statistic,0, Craft,1
	* GoalParameters:	Id&Mined2A;Amount&15000, Id&Mined2B;Amount&15000, Id&Mined2C;Amount&15000, Category&Crafting;Amount&10;Tags&Squad_T2up

### qs_Exile_03: The Cartographer's Promise
Travel across the galaxy and discover new locations to help chart the unknown.
	* Type:	Side
	* Goals:	Goto,0, Goto,0, Goto,0, Scan,1
	* GoalParameters:	Target&[-1752, -861];TargetMode&Station, Target&[-1020, -650];TargetMode&Station, Target&[-1665, 176];TargetMode&Station, Tags&InSystem_T2up;Amount&50;Analyzed&True

## ql_Ytep

### qs_Ytep_01: Ytep Under Fire
Help the people of Ytep take back control of the system by pushing back enemies.
	* Type:	Side
	* Goals:	Goto,0, Scan,1, CompleteMission,1, Statistic,1
	* GoalParameters:	Target&[-946, -690];TargetMode&Station, Tags&InSystem_T3up;Amount&10;Analyzed&True, Mode&Generated;Tier&3;Amount&10, Id&ShipsDestroyedT3;Amount&75

### qs_Ytep_02: Supplying the War Effort
Collect enough parts and ships to support the war effort in Ytep.
	* Type:	Side
	* Goals:	Craft,0, Craft,0, Craft,0, Craft,1, Craft,1
	* GoalParameters:	Tags&Part_Ship_S_T2;Amount&2000;Category&Crafting, Tags&Part_Weapon_S_T2;Amount&2000;Category&Crafting, Tags&Part_Module_S_T2;Amount&2000;Category&Crafting, Type&Squad;Tags&Interceptor_T2;Amount&1;Category&Crafting, Type&Squad;Tags&AssaultCorvette_T2;Amount&1;Category&Crafting

### qs_Ytep_03: To Strengthen Ytep
Donate T2 parts and ships to help the people of Ytep fight after you are gone.
	* Type:	Side
	* Goals:	Pay,0, Pay,0, Pay,0, Pay,1, Pay,1
	* GoalParameters:	Id&intmed_ship_small_t2;Amount&20;SysId&[-946, -690], Id&intmed_weapon_small_t2;Amount&800;SysId&[-946, -690], Id&intmed_module_small_t2;Amount&800;SysId&[-946, -690], Id&hgn_sf_intc_01_t2;Amount&1;SysId&[-946, -690], Id&hgn_sc_assa_01_t2;Amount&1;SysId&[-946, -690]

## ql_esca_killPirate1

### qs_killPirate1_pre01: Cangacian Raider Fleets I
Pirates known as the Cangacians are harassing trade fleets of the Iyatequa.
	* Type:	Achievement
	* Goals:	Statistic,0
	* GoalParameters:	Id&ShipsDestroyedP1;Total&10

### qs_killPirate1_00: Cangacian Raider Fleets II
More Cangacian activity is being reported.
	* Type:	Achievement
	* Goals:	Statistic,0
	* GoalParameters:	Id&ShipsDestroyedP1;Total&25

### qs_killPirate1_01: Cangacian Raider Fleets III
Give the pirates a bloody nose. Show them you're no pushover.
	* Type:	Achievement
	* Goals:	Statistic,0
	* GoalParameters:	Id&ShipsDestroyedP1;Total&50

### qs_killPirate1_02: Cangacian Raider Fleets IV
Hunt down pirate ships to suppress their activities in the area.
	* Type:	Achievement
	* Goals:	Statistic,0
	* GoalParameters:	Id&ShipsDestroyedP1;Total&100

### qs_killPirate1_03: Cangacian Raider Fleets V
Beat back the local pirates by eliminating most of their forces.
	* Type:	Achievement
	* FollowUps:	ql_esca_killYaot
	* Goals:	Statistic,0
	* GoalParameters:	Id&ShipsDestroyedP1;Total&200

### qs_killPirate1_04: Cangacian Raider Fleets VI
An organized pirate force has moved into the area. Show them they are not welcome.
	* Type:	Achievement
	* Goals:	Statistic,0
	* GoalParameters:	Id&ShipsDestroyedP1;Total&400

### qs_killPirate1_05: Cangacian Raider Fleets VII
The Fleet of Rams has increased their presence. Meet them with equal enmity.
	* Type:	Achievement
	* Goals:	Statistic,0
	* GoalParameters:	Id&ShipsDestroyedP1;Total&800

### qs_killPirate1_06: Cangacian Raider Fleets VIII
The Fleet of Rams is hunting the local defenders. Oppose them with force!
	* Type:	Achievement
	* Goals:	Statistic,0
	* GoalParameters:	Id&ShipsDestroyedP1;Total&1600

### qs_killPirate1_07: Cangacian Raider Fleets IX
Supay himself has routed one of his fleets to the area. Engage them at will!
	* Type:	Achievement
	* Goals:	Statistic,0
	* GoalParameters:	Id&ShipsDestroyedP1;Total&3200

### qs_killPirate1_08: Cangacian Raider Fleets X
Send a message to Supay, warlord of the Fleet of Rams. Destroy one of his fleets.
	* Type:	Achievement
	* Goals:	Statistic,0
	* GoalParameters:	Id&ShipsDestroyedP1;Total&6400

## ql_esca_killTanoch

### qs_killTanoch_pre01: Tanoch Renegade Fleets I
Renegades of the Tanoch nation are disrupting the peace of the empire.
	* Type:	Achievement
	* Goals:	Statistic,0
	* GoalParameters:	Id&ShipsDestroyedTanoch;Total&10

### qs_killTanoch_00: Tanoch Renegade Fleets II
More renegade fleets are being reported.
	* Type:	Achievement
	* Goals:	Statistic,0
	* GoalParameters:	Id&ShipsDestroyedTanoch;Total&25

### qs_killTanoch_01: Tanoch Renegade Fleets III
Poach Tanoch patrols to weaken their activities in the area. Hostile Tanoch signals have been located in T2 systems and higher.
	* Type:	Achievement
	* Goals:	Statistic,0
	* GoalParameters:	Id&ShipsDestroyedTanoch;Total&50

### qs_killTanoch_02: Tanoch Renegade Fleets IV
Continue to attack Tanoch patrols to weaken their local status. Hostile Tanoch signals have been located in T2 systems and higher.
	* Type:	Achievement
	* Goals:	Statistic,0
	* GoalParameters:	Id&ShipsDestroyedTanoch;Total&100

### qs_killTanoch_03: Tanoch Renegade Fleets V
Tanoch freighter crews fear your arrival. Continue the attacks! Hostile Tanoch signals have been located in T2 systems and higher.
	* Type:	Achievement
	* Goals:	Statistic,0
	* GoalParameters:	Id&ShipsDestroyedTanoch;Total&200

### qs_killTanoch_04: Tanoch Renegade Fleets VI
Tanoch freighters request action against you. Continue the attacks! Hostile Tanoch signals have been located in T2 systems and higher.
	* Type:	Achievement
	* Goals:	Statistic,0
	* GoalParameters:	Id&ShipsDestroyedTanoch;Total&400

### qs_killTanoch_05: Tanoch Renegade Fleets VII
The Tanoch patrol force recognizes you on sight. Continue the attacks! Hostile Tanoch signals have been located in T2 systems and higher.
	* Type:	Achievement
	* Goals:	Statistic,0
	* GoalParameters:	Id&ShipsDestroyedTanoch;Total&800

### qs_killTanoch_06: Tanoch Renegade Fleets VIII
Tanoch warning stations alert the Empire to your presence. Continue your attacks! Hostile Tanoch signals have been located in T2 systems and higher.
	* Type:	Achievement
	* Goals:	Statistic,0
	* GoalParameters:	Id&ShipsDestroyedTanoch;Total&1600

### qs_killTanoch_07: Tanoch Renegade Fleets IX
The Tanoch regard you as a fleet-level threat. Continue your assaults against them! Hostile Tanoch signals have been located in T2 systems and higher.
	* Type:	Achievement
	* Goals:	Statistic,0
	* GoalParameters:	Id&ShipsDestroyedTanoch;Total&3200

### qs_killTanoch_08: Tanoch Renegade Fleets X
The Emperor will know your name. Hostile Tanoch signals have been located in T2 systems and higher.
	* Type:	Achievement
	* Goals:	Statistic,0
	* GoalParameters:	Id&ShipsDestroyedTanoch;Total&6400

## ql_esca_killYaot

### qs_killYaot_pre01: Yaot Rebel Fleets I
Some Yaot that are dissatisfied with the government have begun causing chaos in regional space.
	* Type:	Achievement
	* Goals:	Statistic,0
	* GoalParameters:	Id&ShipsDestroyedYaot;Total&10

### qs_killYaot_00: Yaot Rebel Fleets II
More Yaot rebels have been reported.
	* Type:	Achievement
	* Goals:	Statistic,0
	* GoalParameters:	Id&ShipsDestroyedYaot;Total&25

### qs_killYaot_01: Yaot Rebel Fleets III
Attack the Yaot patrols to drive them from this area.
	* Type:	Achievement
	* Goals:	Statistic,0
	* GoalParameters:	Id&ShipsDestroyedYaot;Total&50

### qs_killYaot_02: Yaot Rebel Fleets IV
Continue attacking the Yaot to drive them from the region.
	* Type:	Achievement
	* Goals:	Statistic,0
	* GoalParameters:	Id&ShipsDestroyedYaot;Total&100

### qs_killYaot_03: Yaot Rebel Fleets V
Yaot Fleet captains recognize your silhouette. Continue the attack.
	* Type:	Achievement
	* FollowUps:	ql_esca_killTanoch
	* Goals:	Statistic,0
	* GoalParameters:	Id&ShipsDestroyedYaot;Total&200

### qs_killYaot_04: Yaot Rebel Fleets VI
Yaot sensors are alerted to your presence. Continue the attack!
	* Type:	Achievement
	* Goals:	Statistic,0
	* GoalParameters:	Id&ShipsDestroyedYaot;Total&400

### qs_killYaot_05: Yaot Rebel Fleets VII
Yaot Fleet commanders are watching out for you. Continue your assaults against them!
	* Type:	Achievement
	* Goals:	Statistic,0
	* GoalParameters:	Id&ShipsDestroyedYaot;Total&800

### qs_killYaot_06: Yaot Rebel Fleets VIII
Your name is mentioned between Yaot Fleet commanders. Continue your attacks!
	* Type:	Achievement
	* Goals:	Statistic,0
	* GoalParameters:	Id&ShipsDestroyedYaot;Total&1600

### qs_killYaot_07: Yaot Rebel Fleets IX
You are impacting Yaot fleet operations in this area. Continue your attack!
	* Type:	Achievement
	* Goals:	Statistic,0
	* GoalParameters:	Id&ShipsDestroyedYaot;Total&3200

### qs_killYaot_08: Yaot Rebel Fleets X
Your threat level among the Yaot is higher than most Tanoch fleets. Continue the attack!
	* Type:	Achievement
	* Goals:	Statistic,0
	* GoalParameters:	Id&ShipsDestroyedYaot;Total&6400

## ql_esca_mineT1

### qs_mineT1ABC_pre01: Mining Procedures I
We need to test our mining equipment.
	* Type:	Achievement
	* Goals:	Statistic,0, Statistic,0, Statistic,0
	* GoalParameters:	Id&Mined1A;Total&1000, Id&Mined1B;Total&1000, Id&Mined1C;Total&1000

### qs_mineT1ABC_00: Mining Procedures II
We should check our mining procedures and see if we could streamline the process.
	* Type:	Achievement
	* Goals:	Statistic,0, Statistic,0, Statistic,0
	* GoalParameters:	Id&Mined1A;Total&3000, Id&Mined1B;Total&3000, Id&Mined1C;Total&3000

### qs_mineT1ABC_01: Mining Procedures III
Start collecting asteroids to calibrate our resource refinery methods.
	* Type:	Achievement
	* Goals:	Statistic,0, Statistic,0, Statistic,0
	* GoalParameters:	Id&Mined1A;Total&6000, Id&Mined1B;Total&6000, Id&Mined1C;Total&6000

### qs_mineT1ABC_02: Mining Procedures IV
More materials are necessary to establish our baseline. Harvest more asteroids.
	* Type:	Achievement
	* Goals:	Statistic,0, Statistic,0, Statistic,0
	* GoalParameters:	Id&Mined1A;Total&12000, Id&Mined1B;Total&12000, Id&Mined1C;Total&12000

### qs_mineT1ABC_03: Mining Procedures V
Our refineries have been calibrated to local nimbus materials. Begin our first production haul.
	* Type:	Achievement
	* FollowUps:	ql_esca_mineT2
	* Goals:	Statistic,0, Statistic,0, Statistic,0
	* GoalParameters:	Id&Mined1A;Total&24000, Id&Mined1B;Total&24000, Id&Mined1C;Total&24000

### qs_mineT1ABC_04: Mining Procedures VI
Begin our second production haul for processing.
	* Type:	Achievement
	* Goals:	Statistic,0, Statistic,0, Statistic,0
	* GoalParameters:	Id&Mined1A;Total&48000, Id&Mined1B;Total&48000, Id&Mined1C;Total&48000

### qs_mineT1ABC_05: Mining Procedures VII
Begin our third production haul for processing.
	* Type:	Achievement
	* Goals:	Statistic,0, Statistic,0, Statistic,0
	* GoalParameters:	Id&Mined1A;Total&96000, Id&Mined1B;Total&96000, Id&Mined1C;Total&96000

### qs_mineT1ABC_06: Mining Procedures VIII
Begin our fourth production haul for processing.
	* Type:	Achievement
	* Goals:	Statistic,0, Statistic,0, Statistic,0
	* GoalParameters:	Id&Mined1A;Total&192000, Id&Mined1B;Total&192000, Id&Mined1C;Total&192000

### qs_mineT1ABC_07: Mining Procedures IX
One final haul is needed to certify the refinery for full operations.
	* Type:	Achievement
	* Goals:	Statistic,0, Statistic,0, Statistic,0
	* GoalParameters:	Id&Mined1A;Total&384000, Id&Mined1B;Total&384000, Id&Mined1C;Total&384000

### qs_mineT1ABC_08: Mining Procedures X
One last production haul is needed to certify the refinery for Grade 1 Procesing.
	* Type:	Achievement
	* Goals:	Statistic,0, Statistic,0, Statistic,0
	* GoalParameters:	Id&Mined1A;Total&768000, Id&Mined1B;Total&768000, Id&Mined1C;Total&768000

## ql_esca_mineT2

### qs_mineT2ABC_pre01: New Mining Procedures I
We need to test our mining equipment on these new types of minerals.
	* Type:	Achievement
	* Goals:	Statistic,0, Statistic,0, Statistic,0
	* GoalParameters:	Id&Mined2A;Total&1000, Id&Mined2B;Total&1000, Id&Mined2C;Total&1000

### qs_mineT2ABC_00: New Mining Procedures II
We should check our mining procedures on these new types of minerals.
	* Type:	Achievement
	* Goals:	Statistic,0, Statistic,0, Statistic,0
	* GoalParameters:	Id&Mined2A;Total&3000, Id&Mined2B;Total&3000, Id&Mined2C;Total&3000

### qs_mineT2ABC_01: New Mining Procedures III
Engineering has proposed minor upgrades to the refinery process. Harvest larger asteroids for testing.
	* Type:	Achievement
	* Goals:	Statistic,0, Statistic,0, Statistic,0
	* GoalParameters:	Id&Mined2A;Total&6000, Id&Mined2B;Total&6000, Id&Mined2C;Total&6000

### qs_mineT2ABC_02: New Mining Procedures IV
Engineering is ready to implement these minor changes. Continue supplying larger resources.
	* Type:	Achievement
	* Goals:	Statistic,0, Statistic,0, Statistic,0
	* GoalParameters:	Id&Mined2A;Total&12000, Id&Mined2B;Total&12000, Id&Mined2C;Total&12000

### qs_mineT2ABC_03: New Mining Procedures V
Engineering wants to test further refits to the refinery. Supply additional resources for testing.
	* Type:	Achievement
	* FollowUps:	ql_esca_mineT3
	* Goals:	Statistic,0, Statistic,0, Statistic,0
	* GoalParameters:	Id&Mined2A;Total&24000, Id&Mined2B;Total&24000, Id&Mined2C;Total&24000

### qs_mineT2ABC_04: New Mining Procedures VI
Continue refinery trials. Provide larger resources.
	* Type:	Achievement
	* Goals:	Statistic,0, Statistic,0, Statistic,0
	* GoalParameters:	Id&Mined2A;Total&48000, Id&Mined2B;Total&48000, Id&Mined2C;Total&48000

### qs_mineT2ABC_05: New Mining Procedures VII
Continue refinery trials. Provide larger resources.
	* Type:	Achievement
	* Goals:	Statistic,0, Statistic,0, Statistic,0
	* GoalParameters:	Id&Mined2A;Total&96000, Id&Mined2B;Total&96000, Id&Mined2C;Total&96000

### qs_mineT2ABC_06: New Mining Procedures VIII
Continue refinery trials. Provide larger resources.
	* Type:	Achievement
	* Goals:	Statistic,0, Statistic,0, Statistic,0
	* GoalParameters:	Id&Mined2A;Total&192000, Id&Mined2B;Total&192000, Id&Mined2C;Total&192000

### qs_mineT2ABC_07: New Mining Procedures IX
Continue refinery trials. Provide larger resources.
	* Type:	Achievement
	* Goals:	Statistic,0, Statistic,0, Statistic,0
	* GoalParameters:	Id&Mined2A;Total&384000, Id&Mined2B;Total&384000, Id&Mined2C;Total&384000

### qs_mineT2ABC_08: New Mining Procedures X
One final load is necessary to approve the new refit to the refinery.
	* Type:	Achievement
	* Goals:	Statistic,0, Statistic,0, Statistic,0
	* GoalParameters:	Id&Mined2A;Total&768000, Id&Mined2B;Total&768000, Id&Mined2C;Total&768000

## ql_esca_mineT3

### qs_mineT3ABC_pre01: Advanced Mining Procedures I
We need to test our mining equipment on these new types of minerals.
	* Type:	Achievement
	* Goals:	Statistic,0, Statistic,0, Statistic,0
	* GoalParameters:	Id&Mined3A;Total&1000, Id&Mined3B;Total&1000, Id&Mined3C;Total&1000

### qs_mineT3ABC_00: Advanced Mining Procedures II
We should check our mining procedures on these new types of minerals.
	* Type:	Achievement
	* Goals:	Statistic,0, Statistic,0, Statistic,0
	* GoalParameters:	Id&Mined3A;Total&3000, Id&Mined3B;Total&3000, Id&Mined3C;Total&3000

### qs_mineT3ABC_01: Advanced Mining Procedures III
Refinery teams propose a new chemical process for resource extraction.
	* Type:	Achievement
	* Goals:	Statistic,0, Statistic,0, Statistic,0
	* GoalParameters:	Id&Mined3A;Total&6000, Id&Mined3B;Total&6000, Id&Mined3C;Total&6000

### qs_mineT3ABC_02: Advanced Mining Procedures IV
Supply reduced manpower tests by harvesting further resources.
	* Type:	Achievement
	* Goals:	Statistic,0, Statistic,0, Statistic,0
	* GoalParameters:	Id&Mined3A;Total&12000, Id&Mined3B;Total&12000, Id&Mined3C;Total&12000

### qs_mineT3ABC_03: Advanced Mining Procedures V
Conducting reduced manpower stress test on refinery complex.
	* Type:	Achievement
	* Goals:	Statistic,0, Statistic,0, Statistic,0
	* GoalParameters:	Id&Mined3A;Total&24000, Id&Mined3B;Total&24000, Id&Mined3C;Total&24000

### qs_mineT3ABC_04: Advanced Mining Procedures VI
Conducting reduced manpower stress test on refinery complex.
	* Type:	Achievement
	* Goals:	Statistic,0, Statistic,0, Statistic,0
	* GoalParameters:	Id&Mined3A;Total&48000, Id&Mined3B;Total&48000, Id&Mined3C;Total&48000

### qs_mineT3ABC_05: Advanced Mining Procedures VII
Conducting reduced manpower stress test on refinery complex.
	* Type:	Achievement
	* Goals:	Statistic,0, Statistic,0, Statistic,0
	* GoalParameters:	Id&Mined3A;Total&96000, Id&Mined3B;Total&96000, Id&Mined3C;Total&96000

### qs_mineT3ABC_06: Advanced Mining Procedures VIII
Conducting reduced manpower stress test on refinery complex.
	* Type:	Achievement
	* Goals:	Statistic,0, Statistic,0, Statistic,0
	* GoalParameters:	Id&Mined3A;Total&192000, Id&Mined3B;Total&192000, Id&Mined3C;Total&192000

### qs_mineT3ABC_07: Advanced Mining Procedures IX
Final test of reduced crew capacity through new refinery process. Procure resources.
	* Type:	Achievement
	* Goals:	Statistic,0, Statistic,0, Statistic,0
	* GoalParameters:	Id&Mined3A;Total&384000, Id&Mined3B;Total&384000, Id&Mined3C;Total&384000

### qs_mineT3ABC_08: Advanced Mining Procedures X
Final certification of refinery postprocessing procedure. Supply resources for this test.
	* Type:	Achievement
	* Goals:	Statistic,0, Statistic,0, Statistic,0
	* GoalParameters:	Id&Mined3A;Total&768000, Id&Mined3B;Total&768000, Id&Mined3C;Total&768000

## ql_esca_scan

### qs_scan_pre01: System Charts I
We should explore the star systems in this new galaxy.
	* Type:	Achievement
	* Goals:	Statistic,0
	* GoalParameters:	Id&Scanned;Total&50

### qs_scan_00: System Charts II
We need to fill our system charts with actual data.
	* Type:	Achievement
	* Goals:	Statistic,0
	* GoalParameters:	Id&Scanned;Total&150

### qs_scan_01: System Charts III
The new sensor suite needs raw data to begin configuring the array. Begin scanning.
	* Type:	Achievement
	* FollowUps:	ql_esca_generated
	* Goals:	Statistic,0
	* GoalParameters:	Id&Scanned;Total&300

### qs_scan_02: System Charts IV
The array is ready to begin trials. Begin scanning targets.
	* Type:	Achievement
	* Goals:	Statistic,0
	* GoalParameters:	Id&Scanned;Total&600

### qs_scan_03: System Charts V
Begin testing short range detection sensors. Begin scanning targets.
	* Type:	Achievement
	* Goals:	Statistic,0
	* GoalParameters:	Id&Scanned;Total&1200

### qs_scan_04: System Charts VI
Conduct scans. Calibration will focus on short range performance.
	* Type:	Achievement
	* Goals:	Statistic,0
	* GoalParameters:	Id&Scanned;Total&2500

### qs_scan_05: System Charts VII
Conduct scans. Calibration will focus on long range performance.
	* Type:	Achievement
	* Goals:	Statistic,0
	* GoalParameters:	Id&Scanned;Total&5000

### qs_scan_06: System Charts VIII
Conduct Scans. Calibration will focus on hyperspace oddities.
	* Type:	Achievement
	* Goals:	Statistic,0
	* GoalParameters:	Id&Scanned;Total&10000

### qs_scan_07: System Charts IX
Conduct scans. Calibration will focus on signals moving at distance.
	* Type:	Achievement
	* Goals:	Statistic,0
	* GoalParameters:	Id&Scanned;Total&20000

### qs_scan_08: System Charts X
Final comprehensive test of all sensor systems.
	* Type:	Achievement
	* Goals:	Statistic,0
	* GoalParameters:	Id&Scanned;Total&40000

## ql_esca_generated

### qs_finishGenerated_pre01: Signal Search I
We should look out for possible signals in deep space. They could represent opportunities for us.
	* Type:	Achievement
	* Goals:	Statistic,0
	* GoalParameters:	Id&MissionsDoneGenerated;Total&2

### qs_finishGenerated_00: Signal Search II
We should actively search for signals in deep space.
	* Type:	Achievement
	* Goals:	Statistic,0
	* GoalParameters:	Id&MissionsDoneGenerated;Total&5

### qs_finishGenerated_01: Signal Search III
Signals investigation for pathfinding and reconnaissance.
	* Type:	Achievement
	* Goals:	Statistic,0
	* GoalParameters:	Id&MissionsDoneGenerated;Total&10

### qs_finishGenerated_02: Signal Search IV
Further investigate mysterious signals for pathfinding and reconnaissance.
	* Type:	Achievement
	* Goals:	Statistic,0
	* GoalParameters:	Id&MissionsDoneGenerated;Total&20

### qs_finishGenerated_03: Signal Search V
Hunt for anomalous signals to unlock further discoveries and rewards.
	* Type:	Achievement
	* Goals:	Statistic,0
	* GoalParameters:	Id&MissionsDoneGenerated;Total&40

### qs_finishGenerated_04: Signal Search VI
Establish signal gain and investigation methods.
	* Type:	Achievement
	* Goals:	Statistic,0
	* GoalParameters:	Id&MissionsDoneGenerated;Total&80

### qs_finishGenerated_05: Signal Search VII
Routine investigation of anomalous signals.
	* Type:	Achievement
	* Goals:	Statistic,0
	* GoalParameters:	Id&MissionsDoneGenerated;Total&160

### qs_finishGenerated_06: Signal Search VIII
Special teams designated for signal investigations response.
	* Type:	Achievement
	* Goals:	Statistic,0
	* GoalParameters:	Id&MissionsDoneGenerated;Total&320

### qs_finishGenerated_07: Signal Search IX
Catalogue of anomalous activities established.
	* Type:	Achievement
	* Goals:	Statistic,0
	* GoalParameters:	Id&MissionsDoneGenerated;Total&640

### qs_finishGenerated_08: Signal Search X
Investigative mastery.
	* Type:	Achievement
	* Goals:	Statistic,0
	* GoalParameters:	Id&MissionsDoneGenerated;Total&1300

## ql_raid_013

### qr_013: Pirate Hideout
A lot of pirate activity has been reported in this region. The local pirate faction must have a major base here. Our task is to find the base, and destroy any pirate vessel and structure in this sector.
	* Type:	Strike
	* Goals:	CompleteMission,0
	* GoalParameters:	Id&strike_01_PirateHideout

## ql_raid_016

### qr_016: Pirate Hideout (Heroic)
A lot of pirate activity has been reported in this region. The local pirate faction must have a major base here. Our task is to find the base, and destroy any pirate vessel and structure in this sector.
	* Type:	Strike
	* Goals:	CompleteMission,0
	* GoalParameters:	Id&strike_01_PirateHideout_heroic

## ql_raid_014

### qr_014: Station Defense
We have received intel that enemy forces are planning to attack a local trading station. In order to defend the station, we must immediately move our fleet into defensive position.
	* Type:	Strike
	* Goals:	CompleteMission,0
	* GoalParameters:	Id&strike_02_StationDefense

## ql_raid_017

### qr_017: Station Defense (Heroic)
We have received intel that enemy forces are planning to attack a local trading station. In order to defend the station, we must immediately move our fleet into defensive position.
	* Type:	Strike
	* Goals:	CompleteMission,0
	* GoalParameters:	Id&strike_02_StationDefense_heroic

## ql_raid_021

### qr_021: Station Defense (Mythic)
We have received intel that enemy forces are planning to attack a local trading station. In order to defend the station, we must immediately move our fleet into defensive position.
	* Type:	Strike
	* Goals:	CompleteMission,0
	* GoalParameters:	Id&strike_02_StationDefense_mythic

## ql_raid_015

### qr_015: Pahra's Rock
The presence of a large Cangacian asteroid base in this area has been threatening the Hiigaran settlements. Our task is to perform an attack on this base, destroy it and any Cangacian fleet nearby.
	* Type:	Strike
	* Goals:	CompleteMission,0
	* GoalParameters:	Id&strike_03_PahrasRock

## ql_raid_018

### qr_018: Pahra's Rock (Heroic)
The presence of a large Cangacian asteroid base in this area has been threatening the Hiigaran settlements. Our task is to perform an attack on this base, destroy it and any Cangacian fleet nearby.
	* Type:	Strike
	* Goals:	CompleteMission,0
	* GoalParameters:	Id&strike_03_PahrasRock_heroic

## ql_raid_022

### qr_022: Pahra's Rock (Mythic)
The presence of a large Cangacian asteroid base in this area has been threatening the Hiigaran settlements. Our task is to perform an attack on this base, destroy it and any Cangacian fleet nearby.
	* Type:	Strike
	* Goals:	CompleteMission,0
	* GoalParameters:	Id&strike_03_PahrasRock_mythic

## ql_raid_019

### qr_019: Breach
Sitting in a safe pocket inside an electromagnetic asteroid field, this station is a crucial base of operation. As it is heavily defended, we came up with the cunning plan to fill an old freighter with explosives and escort it to the base.
	* Type:	Strike
	* Goals:	CompleteMission,0
	* GoalParameters:	Id&strike_04_Breach

## ql_raid_020

### qr_020: Breach (Heroic)
Sitting in a safe pocket inside an electromagnetic asteroid field, this station is a crucial base of operation. As it is heavily defended, we came up with the cunning plan to fill an old freighter with explosives and escort it to the base.
	* Type:	Strike
	* Goals:	CompleteMission,0
	* GoalParameters:	Id&strike_04_Breach_heroic

## ql_raid_023

### qr_023: Nightmare Gulf
A base used by Kiithless raiders has been located in this area of the nightmare gulf. A large attack force will be needed to destroy it and free the Progenitor assets held at this location.
	* Type:	Strike
	* Goals:	CompleteMission,0
	* GoalParameters:	Id&strike_05_NightmareGulf

## ql_event_test_1

### qe_test_eventtestquest_1: No header for quest qe_test_eventtestquest_1
No description for quest qe_test_eventtestquest_1
	* Type:	Event
	* Goals:	Craft,0
	* GoalParameters:	Category&Crafting;Amount&10

## ql_event_test_2

### qe_test_eventtestquest_2: No header for quest qe_test_eventtestquest_2
No description for quest qe_test_eventtestquest_2
	* Type:	Event
	* Goals:	Pay,0
	* GoalParameters:	Id&CR;Amount&10

## ql_event_test_3

### qe_test_eventtestquest_3: No header for quest qe_test_eventtestquest_3
No description for quest qe_test_eventtestquest_3
	* Type:	Event
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&1

## ql_yaot_spring_2023_daily_A_t2

### qe_yaot_spring_2023_daily_A_t2: No header for quest qe_yaot_spring_2023_daily_A_t2
No description for quest qe_yaot_spring_2023_daily_A_t2
	* Type:	Event
	* EventId:	event_season_yaoSpr_2023
	* Goals:	GainItem,0
	* GoalParameters:	Id&RP;Amount&200;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

## ql_yaot_spring_2023_daily_B_t2

### qe_yaot_spring_2023_daily_B_t2: No header for quest qe_yaot_spring_2023_daily_B_t2
No description for quest qe_yaot_spring_2023_daily_B_t2
	* Type:	Event
	* EventId:	event_season_yaoSpr_2023
	* Goals:	Statistic,0
	* GoalParameters:	Id&ShipsDestroyedTanoch;Amount&10

## ql_yaot_spring_2023_daily_C_t3

### qe_yaot_spring_2023_daily_C_t3: No header for quest qe_yaot_spring_2023_daily_C_t3
No description for quest qe_yaot_spring_2023_daily_C_t3
	* Type:	Event
	* EventId:	event_season_yaoSpr_2023
	* Goals:	Statistic,0
	* GoalParameters:	Ids&Mined3E_Mined3F_Mined3G_Mined3H_Mined4E_Mined4F_Mined4G_Mined4H;Amount&100

## ql_yaot_spring_2023_daily_D_t3

### qe_yaot_spring_2023_daily_D_t3: No header for quest qe_yaot_spring_2023_daily_D_t3
No description for quest qe_yaot_spring_2023_daily_D_t3
	* Type:	Event
	* EventId:	event_season_yaoSpr_2023
	* Goals:	CompleteQuest,0
	* GoalParameters:	Amount&5;Tags&Faction_Yaot

## ql_event_yaot_spring_2023

### qe_yaot_spring_2023_day1: No header for quest qe_yaot_spring_2023_day1
No description for quest qe_yaot_spring_2023_day1
	* Type:	Event
	* EventId:	event_season_yaoSpr_2023
	* Goals:	Statistic,0
	* GoalParameters:	Id&Mined;Amount&750

### qe_yaot_spring_2023_day2: No header for quest qe_yaot_spring_2023_day2
No description for quest qe_yaot_spring_2023_day2
	* Type:	Event
	* EventId:	event_season_yaoSpr_2023
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&3;Mode&Generated

### qe_yaot_spring_2023_day3: No header for quest qe_yaot_spring_2023_day3
No description for quest qe_yaot_spring_2023_day3
	* Type:	Event
	* EventId:	event_season_yaoSpr_2023
	* Goals:	Craft,0
	* GoalParameters:	Category&Refining;Amount&500

### qe_yaot_spring_2023_day4: No header for quest qe_yaot_spring_2023_day4
No description for quest qe_yaot_spring_2023_day4
	* Type:	Event
	* EventId:	event_season_yaoSpr_2023
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Insignia;Amount&15;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_yaot_spring_2023_day5: No header for quest qe_yaot_spring_2023_day5
No description for quest qe_yaot_spring_2023_day5
	* Type:	Event
	* EventId:	event_season_yaoSpr_2023
	* Goals:	UpgradeOfficer,0
	* GoalParameters:	Amount&3

### qe_yaot_spring_2023_day6: No header for quest qe_yaot_spring_2023_day6
No description for quest qe_yaot_spring_2023_day6
	* Type:	Event
	* EventId:	event_season_yaoSpr_2023
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&3;Mode&Generated

### qe_yaot_spring_2023_day7: No header for quest qe_yaot_spring_2023_day7
No description for quest qe_yaot_spring_2023_day7
	* Type:	Event
	* EventId:	event_season_yaoSpr_2023
	* Goals:	Statistic,0
	* GoalParameters:	Id&Mined;Amount&750

### qe_yaot_spring_2023_day8: No header for quest qe_yaot_spring_2023_day8
No description for quest qe_yaot_spring_2023_day8
	* Type:	Event
	* EventId:	event_season_yaoSpr_2023
	* Goals:	GainItem,0
	* GoalParameters:	Tags&ProgenitorRelic;Amount&1;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_yaot_spring_2023_day9: No header for quest qe_yaot_spring_2023_day9
No description for quest qe_yaot_spring_2023_day9
	* Type:	Event
	* EventId:	event_season_yaoSpr_2023
	* Goals:	Craft,0
	* GoalParameters:	Category&Refining;Amount&500

### qe_yaot_spring_2023_day10: No header for quest qe_yaot_spring_2023_day10
No description for quest qe_yaot_spring_2023_day10
	* Type:	Event
	* EventId:	event_season_yaoSpr_2023
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&3;Mode&Generated

### qe_yaot_spring_2023_day11: No header for quest qe_yaot_spring_2023_day11
No description for quest qe_yaot_spring_2023_day11
	* Type:	Event
	* EventId:	event_season_yaoSpr_2023
	* Goals:	Statistic,0
	* GoalParameters:	Id&Mined;Amount&750

### qe_yaot_spring_2023_day12: No header for quest qe_yaot_spring_2023_day12
No description for quest qe_yaot_spring_2023_day12
	* Type:	Event
	* EventId:	event_season_yaoSpr_2023
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Insignia;Amount&15;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_yaot_spring_2023_day13: No header for quest qe_yaot_spring_2023_day13
No description for quest qe_yaot_spring_2023_day13
	* Type:	Event
	* EventId:	event_season_yaoSpr_2023
	* Goals:	UpgradeOfficer,0
	* GoalParameters:	Amount&3

### qe_yaot_spring_2023_day14: No header for quest qe_yaot_spring_2023_day14
No description for quest qe_yaot_spring_2023_day14
	* Type:	Event
	* EventId:	event_season_yaoSpr_2023
	* Goals:	CompleteMission,0
	* GoalParameters:	Id&story_C01_Tanochet_event_heroic

## ql_event_amaSum_2023_t1

### qe_amaSum_2023_day1_t1: No header for quest qe_amaSum_2023_day1_t1
No description for quest qe_amaSum_2023_day1_t1
	* Type:	Event
	* EventId:	event_season_amaSum_2023_t1
	* Goals:	Craft,0
	* GoalParameters:	Category&Refining;Tags&Asteroid_Refined_T1up;Amount&350

### qe_amaSum_2023_day2_t1: No header for quest qe_amaSum_2023_day2_t1
No description for quest qe_amaSum_2023_day2_t1
	* Type:	Event
	* EventId:	event_season_amaSum_2023_t1
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&3;Tags&T1up;Mode&Generated

### qe_amaSum_2023_day3_t1: No header for quest qe_amaSum_2023_day3_t1
No description for quest qe_amaSum_2023_day3_t1
	* Type:	Event
	* EventId:	event_season_amaSum_2023_t1
	* Goals:	UpgradeOfficer,0
	* GoalParameters:	Amount&3

### qe_amaSum_2023_day4_t1: No header for quest qe_amaSum_2023_day4_t1
No description for quest qe_amaSum_2023_day4_t1
	* Type:	Event
	* EventId:	event_season_amaSum_2023_t1
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&3;Tags&T1up;Mode&Generated

### qe_amaSum_2023_day5_t1: No header for quest qe_amaSum_2023_day5_t1
No description for quest qe_amaSum_2023_day5_t1
	* Type:	Event
	* EventId:	event_season_amaSum_2023_t1
	* Goals:	Craft,0
	* GoalParameters:	Category&Refining;Tags&Asteroid_Refined_T1up;Amount&350

### qe_amaSum_2023_day6_t1: No header for quest qe_amaSum_2023_day6_t1
No description for quest qe_amaSum_2023_day6_t1
	* Type:	Event
	* EventId:	event_season_amaSum_2023_t1
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&3;Tags&T1up;Mode&Generated

### qe_amaSum_2023_day7_t1: No header for quest qe_amaSum_2023_day7_t1
No description for quest qe_amaSum_2023_day7_t1
	* Type:	Event
	* EventId:	event_season_amaSum_2023_t1
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Insignia_T1up;Amount&15;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_amaSum_2023_day8_t1: No header for quest qe_amaSum_2023_day8_t1
No description for quest qe_amaSum_2023_day8_t1
	* Type:	Event
	* EventId:	event_season_amaSum_2023_t1
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&3;Tags&T1up;Mode&Generated

### qe_amaSum_2023_day9_t1: No header for quest qe_amaSum_2023_day9_t1
No description for quest qe_amaSum_2023_day9_t1
	* Type:	Event
	* EventId:	event_season_amaSum_2023_t1
	* Goals:	Craft,0
	* GoalParameters:	Category&Refining;Tags&Asteroid_Refined_T1up;Amount&350

### qe_amaSum_2023_day10_t1: No header for quest qe_amaSum_2023_day10_t1
No description for quest qe_amaSum_2023_day10_t1
	* Type:	Event
	* EventId:	event_season_amaSum_2023_t1
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&3;Tags&T1up;Mode&Generated

### qe_amaSum_2023_day11_t1: No header for quest qe_amaSum_2023_day11_t1
No description for quest qe_amaSum_2023_day11_t1
	* Type:	Event
	* EventId:	event_season_amaSum_2023_t1
	* Goals:	UpgradeOfficer,0
	* GoalParameters:	Amount&3

### qe_amaSum_2023_day12_t1: No header for quest qe_amaSum_2023_day12_t1
No description for quest qe_amaSum_2023_day12_t1
	* Type:	Event
	* EventId:	event_season_amaSum_2023_t1
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&3;Tags&T1up;Mode&Generated

### qe_amaSum_2023_day13_t1: No header for quest qe_amaSum_2023_day13_t1
No description for quest qe_amaSum_2023_day13_t1
	* Type:	Event
	* EventId:	event_season_amaSum_2023_t1
	* Goals:	Craft,0
	* GoalParameters:	Category&Refining;Tags&Asteroid_Refined_T1up;Amount&350

### qe_amaSum_2023_day14_t1: No header for quest qe_amaSum_2023_day14_t1
No description for quest qe_amaSum_2023_day14_t1
	* Type:	Event
	* EventId:	event_season_amaSum_2023_t1
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Insignia_T1up;Amount&15;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_amaSum_2023_day15_t1: No header for quest qe_amaSum_2023_day15_t1
No description for quest qe_amaSum_2023_day15_t1
	* Type:	Event
	* EventId:	event_season_amaSum_2023_t1
	* Goals:	CompleteMission,0
	* GoalParameters:	Id&event_01_StationDefense

## ql_event_amaSum_2023_t2

### qe_amaSum_2023_day1_t2: No header for quest qe_amaSum_2023_day1_t2
No description for quest qe_amaSum_2023_day1_t2
	* Type:	Event
	* EventId:	event_season_amaSum_2023_t2
	* Goals:	Craft,0
	* GoalParameters:	Category&Refining;Tags&Asteroid_Refined_T2up;Amount&400

### qe_amaSum_2023_day2_t2: No header for quest qe_amaSum_2023_day2_t2
No description for quest qe_amaSum_2023_day2_t2
	* Type:	Event
	* EventId:	event_season_amaSum_2023_t2
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&3;Tags&T2up;Mode&Generated

### qe_amaSum_2023_day3_t2: No header for quest qe_amaSum_2023_day3_t2
No description for quest qe_amaSum_2023_day3_t2
	* Type:	Event
	* EventId:	event_season_amaSum_2023_t2
	* Goals:	UpgradeOfficer,0
	* GoalParameters:	Amount&3

### qe_amaSum_2023_day4_t2: No header for quest qe_amaSum_2023_day4_t2
No description for quest qe_amaSum_2023_day4_t2
	* Type:	Event
	* EventId:	event_season_amaSum_2023_t2
	* Goals:	CompleteQuest,0
	* GoalParameters:	Amount&5;Tags&Faction_T2up

### qe_amaSum_2023_day5_t2: No header for quest qe_amaSum_2023_day5_t2
No description for quest qe_amaSum_2023_day5_t2
	* Type:	Event
	* EventId:	event_season_amaSum_2023_t2
	* Goals:	Craft,0
	* GoalParameters:	Category&Refining;Tags&Asteroid_Refined_T2up;Amount&400

### qe_amaSum_2023_day6_t2: No header for quest qe_amaSum_2023_day6_t2
No description for quest qe_amaSum_2023_day6_t2
	* Type:	Event
	* EventId:	event_season_amaSum_2023_t2
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&3;Tags&T2up;Mode&Generated

### qe_amaSum_2023_day7_t2: No header for quest qe_amaSum_2023_day7_t2
No description for quest qe_amaSum_2023_day7_t2
	* Type:	Event
	* EventId:	event_season_amaSum_2023_t2
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Insignia_T2up;Amount&15;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_amaSum_2023_day8_t2: No header for quest qe_amaSum_2023_day8_t2
No description for quest qe_amaSum_2023_day8_t2
	* Type:	Event
	* EventId:	event_season_amaSum_2023_t2
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&1;Mode&Strike;Tags&T1up

### qe_amaSum_2023_day9_t2: No header for quest qe_amaSum_2023_day9_t2
No description for quest qe_amaSum_2023_day9_t2
	* Type:	Event
	* EventId:	event_season_amaSum_2023_t2
	* Goals:	Craft,0
	* GoalParameters:	Category&Refining;Tags&Asteroid_Refined_T2up;Amount&400

### qe_amaSum_2023_day10_t2: No header for quest qe_amaSum_2023_day10_t2
No description for quest qe_amaSum_2023_day10_t2
	* Type:	Event
	* EventId:	event_season_amaSum_2023_t2
	* Goals:	CompleteQuest,0
	* GoalParameters:	Amount&5;Tags&Faction_T2up

### qe_amaSum_2023_day11_t2: No header for quest qe_amaSum_2023_day11_t2
No description for quest qe_amaSum_2023_day11_t2
	* Type:	Event
	* EventId:	event_season_amaSum_2023_t2
	* Goals:	UpgradeOfficer,0
	* GoalParameters:	Amount&3

### qe_amaSum_2023_day12_t2: No header for quest qe_amaSum_2023_day12_t2
No description for quest qe_amaSum_2023_day12_t2
	* Type:	Event
	* EventId:	event_season_amaSum_2023_t2
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&1;Mode&Strike;Tags&T1up

### qe_amaSum_2023_day13_t2: No header for quest qe_amaSum_2023_day13_t2
No description for quest qe_amaSum_2023_day13_t2
	* Type:	Event
	* EventId:	event_season_amaSum_2023_t2
	* Goals:	Craft,0
	* GoalParameters:	Category&Refining;Tags&Asteroid_Refined_T2up;Amount&400

### qe_amaSum_2023_day14_t2: No header for quest qe_amaSum_2023_day14_t2
No description for quest qe_amaSum_2023_day14_t2
	* Type:	Event
	* EventId:	event_season_amaSum_2023_t2
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Insignia_T2up;Amount&15;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_amaSum_2023_day15_t2: No header for quest qe_amaSum_2023_day15_t2
No description for quest qe_amaSum_2023_day15_t2
	* Type:	Event
	* EventId:	event_season_amaSum_2023_t2
	* Goals:	CompleteMission,0
	* GoalParameters:	Id&event_02_StationDefense

## ql_event_amaSum_2023_t3

### qe_amaSum_2023_day1_t3: No header for quest qe_amaSum_2023_day1_t3
No description for quest qe_amaSum_2023_day1_t3
	* Type:	Event
	* EventId:	event_season_amaSum_2023_t3
	* Goals:	Craft,0
	* GoalParameters:	Category&Refining;Tags&Asteroid_Refined_T3up;Amount&450

### qe_amaSum_2023_day2_t3: No header for quest qe_amaSum_2023_day2_t3
No description for quest qe_amaSum_2023_day2_t3
	* Type:	Event
	* EventId:	event_season_amaSum_2023_t3
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&3;Tags&T3up;Mode&Generated

### qe_amaSum_2023_day3_t3: No header for quest qe_amaSum_2023_day3_t3
No description for quest qe_amaSum_2023_day3_t3
	* Type:	Event
	* EventId:	event_season_amaSum_2023_t3
	* Goals:	UpgradeOfficer,0
	* GoalParameters:	Amount&3

### qe_amaSum_2023_day4_t3: No header for quest qe_amaSum_2023_day4_t3
No description for quest qe_amaSum_2023_day4_t3
	* Type:	Event
	* EventId:	event_season_amaSum_2023_t3
	* Goals:	CompleteQuest,0
	* GoalParameters:	Amount&5;Tags&Faction_T3up

### qe_amaSum_2023_day5_t3: No header for quest qe_amaSum_2023_day5_t3
No description for quest qe_amaSum_2023_day5_t3
	* Type:	Event
	* EventId:	event_season_amaSum_2023_t3
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Gas_T3up;Amount&800;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

### qe_amaSum_2023_day6_t3: No header for quest qe_amaSum_2023_day6_t3
No description for quest qe_amaSum_2023_day6_t3
	* Type:	Event
	* EventId:	event_season_amaSum_2023_t3
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&3;Tags&T3up;Mode&Generated

### qe_amaSum_2023_day7_t3: No header for quest qe_amaSum_2023_day7_t3
No description for quest qe_amaSum_2023_day7_t3
	* Type:	Event
	* EventId:	event_season_amaSum_2023_t3
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Insignia_T3up;Amount&15;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_amaSum_2023_day8_t3: No header for quest qe_amaSum_2023_day8_t3
No description for quest qe_amaSum_2023_day8_t3
	* Type:	Event
	* EventId:	event_season_amaSum_2023_t3
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&3;Mode&Strike;Tags&T2up

### qe_amaSum_2023_day9_t3: No header for quest qe_amaSum_2023_day9_t3
No description for quest qe_amaSum_2023_day9_t3
	* Type:	Event
	* EventId:	event_season_amaSum_2023_t3
	* Goals:	Craft,0
	* GoalParameters:	Category&Refining;Tags&Asteroid_Refined_T3up;Amount&450

### qe_amaSum_2023_day10_t3: No header for quest qe_amaSum_2023_day10_t3
No description for quest qe_amaSum_2023_day10_t3
	* Type:	Event
	* EventId:	event_season_amaSum_2023_t3
	* Goals:	CompleteQuest,0
	* GoalParameters:	Amount&5;Tags&Faction_T3up

### qe_amaSum_2023_day11_t3: No header for quest qe_amaSum_2023_day11_t3
No description for quest qe_amaSum_2023_day11_t3
	* Type:	Event
	* EventId:	event_season_amaSum_2023_t3
	* Goals:	UpgradeOfficer,0
	* GoalParameters:	Amount&3

### qe_amaSum_2023_day12_t3: No header for quest qe_amaSum_2023_day12_t3
No description for quest qe_amaSum_2023_day12_t3
	* Type:	Event
	* EventId:	event_season_amaSum_2023_t3
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&3;Mode&Strike;Tags&T2up

### qe_amaSum_2023_day13_t3: No header for quest qe_amaSum_2023_day13_t3
No description for quest qe_amaSum_2023_day13_t3
	* Type:	Event
	* EventId:	event_season_amaSum_2023_t3
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Gas_T3up;Amount&800;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

### qe_amaSum_2023_day14_t3: No header for quest qe_amaSum_2023_day14_t3
No description for quest qe_amaSum_2023_day14_t3
	* Type:	Event
	* EventId:	event_season_amaSum_2023_t3
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Insignia_T3up;Amount&15;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_amaSum_2023_day15_t3: No header for quest qe_amaSum_2023_day15_t3
No description for quest qe_amaSum_2023_day15_t3
	* Type:	Event
	* EventId:	event_season_amaSum_2023_t3
	* Goals:	CompleteMission,0
	* GoalParameters:	Id&event_03_StationDefense

## ql_event_amaSum_2023_t4

### qe_amaSum_2023_day1_t4: No header for quest qe_amaSum_2023_day1_t4
No description for quest qe_amaSum_2023_day1_t4
	* Type:	Event
	* EventId:	event_season_amaSum_2023_t4
	* Goals:	Craft,0
	* GoalParameters:	Category&Refining;Tags&Asteroid_Refined_T4up;Amount&500

### qe_amaSum_2023_day2_t4: No header for quest qe_amaSum_2023_day2_t4
No description for quest qe_amaSum_2023_day2_t4
	* Type:	Event
	* EventId:	event_season_amaSum_2023_t4
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&3;Tags&T4up;Mode&Generated

### qe_amaSum_2023_day3_t4: No header for quest qe_amaSum_2023_day3_t4
No description for quest qe_amaSum_2023_day3_t4
	* Type:	Event
	* EventId:	event_season_amaSum_2023_t4
	* Goals:	UpgradeOfficer,0
	* GoalParameters:	Amount&3

### qe_amaSum_2023_day4_t4: No header for quest qe_amaSum_2023_day4_t4
No description for quest qe_amaSum_2023_day4_t4
	* Type:	Event
	* EventId:	event_season_amaSum_2023_t4
	* Goals:	CompleteQuest,0
	* GoalParameters:	Amount&5;Tags&Faction_Amassari_T4up

### qe_amaSum_2023_day5_t4: No header for quest qe_amaSum_2023_day5_t4
No description for quest qe_amaSum_2023_day5_t4
	* Type:	Event
	* EventId:	event_season_amaSum_2023_t4
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Gas_T4up;Amount&1000;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

### qe_amaSum_2023_day6_t4: No header for quest qe_amaSum_2023_day6_t4
No description for quest qe_amaSum_2023_day6_t4
	* Type:	Event
	* EventId:	event_season_amaSum_2023_t4
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&3;Tags&T4up;Mode&Generated

### qe_amaSum_2023_day7_t4: No header for quest qe_amaSum_2023_day7_t4
No description for quest qe_amaSum_2023_day7_t4
	* Type:	Event
	* EventId:	event_season_amaSum_2023_t4
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Insignia_T4up;Amount&15;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_amaSum_2023_day8_t4: No header for quest qe_amaSum_2023_day8_t4
No description for quest qe_amaSum_2023_day8_t4
	* Type:	Event
	* EventId:	event_season_amaSum_2023_t4
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&5;Mode&Strike;Tags&T3up

### qe_amaSum_2023_day9_t4: No header for quest qe_amaSum_2023_day9_t4
No description for quest qe_amaSum_2023_day9_t4
	* Type:	Event
	* EventId:	event_season_amaSum_2023_t4
	* Goals:	Craft,0
	* GoalParameters:	Category&Refining;Tags&Asteroid_Refined_T4up;Amount&500

### qe_amaSum_2023_day10_t4: No header for quest qe_amaSum_2023_day10_t4
No description for quest qe_amaSum_2023_day10_t4
	* Type:	Event
	* EventId:	event_season_amaSum_2023_t4
	* Goals:	CompleteQuest,0
	* GoalParameters:	Amount&5;Tags&Faction_Amassari_T4up

### qe_amaSum_2023_day11_t4: No header for quest qe_amaSum_2023_day11_t4
No description for quest qe_amaSum_2023_day11_t4
	* Type:	Event
	* EventId:	event_season_amaSum_2023_t4
	* Goals:	UpgradeOfficer,0
	* GoalParameters:	Amount&3

### qe_amaSum_2023_day12_t4: No header for quest qe_amaSum_2023_day12_t4
No description for quest qe_amaSum_2023_day12_t4
	* Type:	Event
	* EventId:	event_season_amaSum_2023_t4
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&5;Mode&Strike;Tags&T3up

### qe_amaSum_2023_day13_t4: No header for quest qe_amaSum_2023_day13_t4
No description for quest qe_amaSum_2023_day13_t4
	* Type:	Event
	* EventId:	event_season_amaSum_2023_t4
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Gas_T4up;Amount&1000;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

### qe_amaSum_2023_day14_t4: No header for quest qe_amaSum_2023_day14_t4
No description for quest qe_amaSum_2023_day14_t4
	* Type:	Event
	* EventId:	event_season_amaSum_2023_t4
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Insignia_T4up;Amount&15;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_amaSum_2023_day15_t4: No header for quest qe_amaSum_2023_day15_t4
No description for quest qe_amaSum_2023_day15_t4
	* Type:	Event
	* EventId:	event_season_amaSum_2023_t4
	* Goals:	CompleteMission,0
	* GoalParameters:	Id&event_04_StationDefense

## ql_7days_mar_2024_day1_t1

### qe_7days_mar_2024_day1_a_t1: Day 1: Lay of the Land
Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t1
	* Goals:	Scan,0
	* GoalParameters:	Tags&InSystem_T1up;Amount&10;Analyzed&True

### qe_7days_mar_2024_day1_b_t1: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t1
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedT1_ShipsDestroyedT2_ShipsDestroyedT3_ShipsDestroyedT4;Amount&15

### qe_7days_mar_2024_day1_c_t1: Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.
Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t1
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Asteroid_Crud_T1up;Amount&800;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_mar_2024_day1_d_t1: Rare earths are an occasional by-product of refining. They are required for upgrading modules.
Rare earths are an occasional by-product of refining. They are required for upgrading modules.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t1
	* Goals:	GainItem,0
	* GoalParameters:	Tags&RareEarth_T1up;Amount&15;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

## ql_7days_mar_2024_day1_t2

### qe_7days_mar_2024_day1_a_t2: Day 1: Lay of the Land
Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t2
	* Goals:	Scan,0
	* GoalParameters:	Tags&InSystem_T2up;Amount&10;Analyzed&True

### qe_7days_mar_2024_day1_b_t2: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t2
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedT2_ShipsDestroyedT3_ShipsDestroyedT4;Amount&15

### qe_7days_mar_2024_day1_c_t2: Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.
Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t2
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Asteroid_Crud_T2up;Amount&1000;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_mar_2024_day1_d_t2: Rare earths are an occasional by-product of refining. They are required for upgrading modules.
Rare earths are an occasional by-product of refining. They are required for upgrading modules.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t2
	* Goals:	GainItem,0
	* GoalParameters:	Tags&RareEarth_T2up;Amount&15;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

## ql_7days_mar_2024_day1_t3

### qe_7days_mar_2024_day1_a_t3: Day 1: Lay of the Land
Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t3
	* Goals:	Scan,0
	* GoalParameters:	Tags&InSystem_T3up;Amount&10;Analyzed&True

### qe_7days_mar_2024_day1_b_t3: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t3
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedT3_ShipsDestroyedT4;Amount&15

### qe_7days_mar_2024_day1_c_t3: Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.
Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t3
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Gas_T3up;Amount&800;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_mar_2024_day1_d_t3: Rare earths are an occasional by-product of refining. They are required for upgrading modules.
Rare earths are an occasional by-product of refining. They are required for upgrading modules.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t3
	* Goals:	GainItem,0
	* GoalParameters:	Tags&RareEarth_T3up;Amount&15;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

## ql_7days_mar_2024_day1_t4

### qe_7days_mar_2024_day1_a_t4: Day 1: Lay of the Land
Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t4
	* Goals:	Scan,0
	* GoalParameters:	Tags&InSystem_T4up;Amount&10;Analyzed&True

### qe_7days_mar_2024_day1_b_t4: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t4
	* Goals:	Statistic,0
	* GoalParameters:	Id&ShipsDestroyedT4;Amount&15

### qe_7days_mar_2024_day1_c_t4: Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.
Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t4
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Gas_T4up;Amount&1000;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_mar_2024_day1_d_t4: Rare earths are an occasional by-product of refining. They are required for upgrading modules.
Rare earths are an occasional by-product of refining. They are required for upgrading modules.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t4
	* Goals:	GainItem,0
	* GoalParameters:	Tags&RareEarth_T4up;Amount&15;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

## ql_7days_mar_2024_day2_t1

### qe_7days_mar_2024_day2_a_t1: Day 2: Meet & Greet
There are different types of assignments available in your assignment log.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t1
	* Goals:	CompleteQuest,0
	* GoalParameters:	Amount&5;Tags&T1up

### qe_7days_mar_2024_day2_b_t1: Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.
During missions you will usually fight against enemy ships. They can be part of an assignment, or they can be found as signals through scanning.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t1
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&3;Tags&T1up

### qe_7days_mar_2024_day2_c_t1: Complete liaison assignments to gain reputation for that faction. A higher reputation unlocks more items in that faction's liaison requisitions office.
Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t1
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Insignia_T1up;Amount&50;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_mar_2024_day2_d_t1: Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t1
	* Goals:	UpgradeOfficer,0
	* GoalParameters:	Amount&1

## ql_7days_mar_2024_day2_t2

### qe_7days_mar_2024_day2_a_t2: Day 2: Meet & Greet
Completing liaison assignments for a faction increases your reputation level for that faction. Higher reputation levels unlock additional items in that faction's liaison requisitions office.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t2
	* Goals:	CompleteQuest,0
	* GoalParameters:	Amount&5;Tags&Faction_T2up

### qe_7days_mar_2024_day2_b_t2: Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.
Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t2
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&3;Mode&Faction;Tags&T2up

### qe_7days_mar_2024_day2_c_t2: Complete liaison assignments to gain reputation for that faction. A higher reputation unlocks more items in that faction's liaison requisitions office.
Complete liaison assignments to gain reputation for that faction. A higher reputation unlocks more items in that faction's liaison requisitions office.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t2
	* Goals:	Statistic,0
	* GoalParameters:	Ids&RepTr1_RepTanoch_RepYaot_RepAmassari;Amount&135

### qe_7days_mar_2024_day2_d_t2: Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t2
	* Goals:	UpgradeOfficer,0
	* GoalParameters:	Amount&2

## ql_7days_mar_2024_day2_t3

### qe_7days_mar_2024_day2_a_t3: Day 2: Meet & Greet
Completing liaison assignments for a faction increases your reputation level for that faction. Higher reputation levels unlock additional items in that faction's liaison requisitions office.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t3
	* Goals:	CompleteQuest,0
	* GoalParameters:	Amount&5;Tags&Faction_T3up

### qe_7days_mar_2024_day2_b_t3: Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.
Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t3
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&3;Mode&Faction;Tags&T3up

### qe_7days_mar_2024_day2_c_t3: Complete liaison assignments to gain reputation for that faction. A higher reputation unlocks more items in that faction's liaison requisitions office.
Complete liaison assignments to gain reputation for that faction. A higher reputation unlocks more items in that faction's liaison requisitions office.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t3
	* Goals:	Statistic,0
	* GoalParameters:	Ids&RepTr1_RepTanoch_RepYaot_RepAmassari;Amount&180

### qe_7days_mar_2024_day2_d_t3: Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t3
	* Goals:	UpgradeOfficer,0
	* GoalParameters:	Amount&3

## ql_7days_mar_2024_day2_t4

### qe_7days_mar_2024_day2_a_t4: Day 2: Meet & Greet
Completing liaison assignments for a faction increases your reputation level for that faction. Higher reputation levels unlock additional items in that faction's liaison requisitions office.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t4
	* Goals:	CompleteQuest,0
	* GoalParameters:	Amount&5;Tags&Faction_T4up

### qe_7days_mar_2024_day2_b_t4: Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.
Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t4
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&3;Mode&Faction;Tags&T4up

### qe_7days_mar_2024_day2_c_t4: Complete liaison assignments to gain reputation for that faction. A higher reputation unlocks more items in that faction's liaison requisitions office.
Complete liaison assignments to gain reputation for that faction. A higher reputation unlocks more items in that faction's liaison requisitions office.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t4
	* Goals:	Statistic,0
	* GoalParameters:	Ids&RepTr1_RepTanoch_RepYaot_RepAmassari;Amount&225

### qe_7days_mar_2024_day2_d_t4: Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t4
	* Goals:	UpgradeOfficer,0
	* GoalParameters:	Amount&5

## ql_7days_mar_2024_day3_t1

### qe_7days_mar_2024_day3_a_t1: Day 3: Raw Materials
Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t1
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Asteroid_Crud_T1up;Amount&800;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_mar_2024_day3_b_t1: Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.
Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t1
	* Goals:	Craft,0
	* GoalParameters:	Category&Refining;Tags&Asteroid_Refined_T1up;Amount&500

### qe_7days_mar_2024_day3_c_t1: Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.
Small items such as strike craft, modules and parts can be built in the fabricator. Larger items such as escort ships and flagships must be constructed at shipyards provided at larger stations.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t1
	* Goals:	Craft,0
	* GoalParameters:	Category&Crafting;Tags&T1up;Amount&1

### qe_7days_mar_2024_day3_d_t1: Items and resources can be sold for credits in the market at stations.
Items and resources can be sold for credits in the market at stations.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t1
	* Goals:	GainItem,0
	* GoalParameters:	Id&CR;Amount&150;ExcludedSources&BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

## ql_7days_mar_2024_day3_t2

### qe_7days_mar_2024_day3_a_t2: Day 3: Raw Materials
Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t2
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Asteroid_Crud_T2up;Amount&1000;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_mar_2024_day3_b_t2: Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.
Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t2
	* Goals:	Craft,0
	* GoalParameters:	Category&Refining;Tags&Asteroid_Refined_T2up;Amount&500

### qe_7days_mar_2024_day3_c_t2: Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.
Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t2
	* Goals:	Craft,0
	* GoalParameters:	Category&Crafting;Tags&Part_T2up;Amount&25

### qe_7days_mar_2024_day3_d_t2: Items and resources can be sold for credits in the market at stations.
Items and resources can be sold for credits in the market at stations.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t2
	* Goals:	GainItem,0
	* GoalParameters:	Id&CR;Amount&300;ExcludedSources&BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

## ql_7days_mar_2024_day3_t3

### qe_7days_mar_2024_day3_a_t3: Day 3: Raw Materials
Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t3
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Asteroid_Crud_T3up;Amount&1200;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_mar_2024_day3_b_t3: Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.
Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t3
	* Goals:	Craft,0
	* GoalParameters:	Category&Refining;Tags&Asteroid_Refined_T3up;Amount&500

### qe_7days_mar_2024_day3_c_t3: Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.
Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t3
	* Goals:	Craft,0
	* GoalParameters:	Category&Crafting;Tags&Part_T3up;Amount&25

### qe_7days_mar_2024_day3_d_t3: Items and resources can be sold for credits in the market at stations.
Items and resources can be sold for credits in the market at stations.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t3
	* Goals:	GainItem,0
	* GoalParameters:	Id&CR;Amount&600;ExcludedSources&BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

## ql_7days_mar_2024_day3_t4

### qe_7days_mar_2024_day3_a_t4: Day 3: Raw Materials
Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t4
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Asteroid_Crud_T4up;Amount&1400;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_mar_2024_day3_b_t4: Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.
Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t4
	* Goals:	Craft,0
	* GoalParameters:	Category&Refining;Tags&Asteroid_Refined_T4up;Amount&500

### qe_7days_mar_2024_day3_c_t4: Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.
Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t4
	* Goals:	Craft,0
	* GoalParameters:	Category&Crafting;Tags&Part_T4up;Amount&25

### qe_7days_mar_2024_day3_d_t4: Items and resources can be sold for credits in the market at stations.
Items and resources can be sold for credits in the market at stations.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t4
	* Goals:	GainItem,0
	* GoalParameters:	Id&CR;Amount&1200;ExcludedSources&BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

## ql_7days_mar_2024_day4_t1

### qe_7days_mar_2024_day4_a_t1: Day 4: Hypothesis
Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t1
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&3;Tags&T1up;Mode&Generated

### qe_7days_mar_2024_day4_b_t1: Progenitor relics can be found in relic signature signals. Relics can be sold on the market for credits, though some liaison offices may be interested in relics as well.
Progenitor relics can be found in relic signature signals. Relics can be sold on the market for credits, though some liaison offices may be interested in relics as well.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t1
	* Goals:	GainItem,0
	* GoalParameters:	Tags&ProgenitorRelic_T1up;Amount&1;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_mar_2024_day4_c_t1: Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.
Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t1
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedProgenitorT1_ShipsDestroyedProgenitorT2_ShipsDestroyedProgenitorT3_ShipsDestroyedProgenitorT4;Amount&7

### qe_7days_mar_2024_day4_d_t1: Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.
Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t1
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&1;Tags&Rare_T1up;Mode&Generated

## ql_7days_mar_2024_day4_t2

### qe_7days_mar_2024_day4_a_t2: Day 4: Hypothesis
Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t2
	* Goals:	GainItem,0
	* GoalParameters:	Id&RP;Amount&200;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_mar_2024_day4_b_t2: Progenitor relics can be found in relic signature signals. Relics can be sold on the market for credits, though some liaison offices may be interested in relics as well.
Progenitor relics can be found in relic signature signals. Relics can be sold on the market for credits, though some liaison offices may be interested in relics as well.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t2
	* Goals:	GainItem,0
	* GoalParameters:	Tags&ProgenitorRelic_T2up;Amount&1;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_mar_2024_day4_c_t2: Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.
Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t2
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedProgenitorT2_ShipsDestroyedProgenitorT3_ShipsDestroyedProgenitorT4;Amount&7

### qe_7days_mar_2024_day4_d_t2: Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.
Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t2
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&1;Tags&Epic_T2up;Mode&Generated

## ql_7days_mar_2024_day4_t3

### qe_7days_mar_2024_day4_a_t3: Day 4: Hypothesis
Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t3
	* Goals:	GainItem,0
	* GoalParameters:	Id&RP;Amount&200;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_mar_2024_day4_b_t3: Progenitor relics can be found in relic signature signals. Relics can be sold on the market for credits, though some liaison offices may be interested in relics as well.
Progenitor relics can be found in relic signature signals. Relics can be sold on the market for credits, though some liaison offices may be interested in relics as well.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t3
	* Goals:	GainItem,0
	* GoalParameters:	Tags&ProgenitorRelic_T3up;Amount&1;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_mar_2024_day4_c_t3: Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.
Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t3
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedProgenitorT3_ShipsDestroyedProgenitorT4;Amount&7

### qe_7days_mar_2024_day4_d_t3: Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.
Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t3
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&1;Tags&Epic_T3up;Mode&Generated

## ql_7days_mar_2024_day4_t4

### qe_7days_mar_2024_day4_a_t4: Day 4: Hypothesis
Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t4
	* Goals:	GainItem,0
	* GoalParameters:	Id&RP;Amount&200;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_mar_2024_day4_b_t4: Progenitor relics can be found in relic signature signals. Relics can be sold on the market for credits, though some liaison offices may be interested in relics as well.
Progenitor relics can be found in relic signature signals. Relics can be sold on the market for credits, though some liaison offices may be interested in relics as well.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t4
	* Goals:	GainItem,0
	* GoalParameters:	Tags&ProgenitorRelic_T4up;Amount&1;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_mar_2024_day4_c_t4: Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.
Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t4
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedProgenitorT4;Amount&7

### qe_7days_mar_2024_day4_d_t4: Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.
Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t4
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&1;Tags&Epic_T4up;Mode&Generated

## ql_7days_mar_2024_day5_t1

### qe_7days_mar_2024_day5_a_t1: Day 5: Lessons
Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t1
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&3;Tags&T1up;Mode&Generated

### qe_7days_mar_2024_day5_b_t1: Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.
Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t1
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Insignia_T1up;Amount&50;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_mar_2024_day5_c_t1: Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t1
	* Goals:	UpgradeOfficer,0
	* GoalParameters:	Amount&1

### qe_7days_mar_2024_day5_d_t1: Discharging officers grants credits and insignias, which can be used to level up other officers.
Discharging officers grants credits and insignias, which can be used to level up other officers.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t1
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Insignia;Amount&2;ExcludedSources&OpenContainer_QuestReward_MissionReward_ClaimMail_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_BuyItem_SellItem

## ql_7days_mar_2024_day5_t2

### qe_7days_mar_2024_day5_a_t2: Day 5: Lessons
Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t2
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&3;Tags&T2up;Mode&Generated

### qe_7days_mar_2024_day5_b_t2: Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.
Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t2
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Insignia_T2up;Amount&50;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_mar_2024_day5_c_t2: Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t2
	* Goals:	UpgradeOfficer,0
	* GoalParameters:	Amount&2

### qe_7days_mar_2024_day5_d_t2: Discharging officers grants credits and insignias, which can be used to level up other officers.
Discharging officers grants credits and insignias, which can be used to level up other officers.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t2
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Insignia;Amount&4;ExcludedSources&OpenContainer_QuestReward_MissionReward_ClaimMail_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_BuyItem_SellItem

## ql_7days_mar_2024_day5_t3

### qe_7days_mar_2024_day5_a_t3: Day 5: Lessons
Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t3
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&3;Tags&T3up;Mode&Generated

### qe_7days_mar_2024_day5_b_t3: Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.
Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t3
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Insignia_T3up;Amount&50;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_mar_2024_day5_c_t3: Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t3
	* Goals:	UpgradeOfficer,0
	* GoalParameters:	Amount&3

### qe_7days_mar_2024_day5_d_t3: Discharging officers grants credits and insignias, which can be used to level up other officers.
Discharging officers grants credits and insignias, which can be used to level up other officers.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t3
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Insignia;Amount&6;ExcludedSources&OpenContainer_QuestReward_MissionReward_ClaimMail_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_BuyItem_SellItem

## ql_7days_mar_2024_day5_t4

### qe_7days_mar_2024_day5_a_t4: Day 5: Lessons
Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t4
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&3;Tags&T4up;Mode&Generated

### qe_7days_mar_2024_day5_b_t4: Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.
Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t4
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Insignia_T4up;Amount&50;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_mar_2024_day5_c_t4: Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t4
	* Goals:	UpgradeOfficer,0
	* GoalParameters:	Amount&5

### qe_7days_mar_2024_day5_d_t4: Discharging officers grants credits and insignias, which can be used to level up other officers.
Discharging officers grants credits and insignias, which can be used to level up other officers.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t4
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Insignia;Amount&10;ExcludedSources&OpenContainer_QuestReward_MissionReward_ClaimMail_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_BuyItem_SellItem

## ql_7days_mar_2024_day6_t1

### qe_7days_mar_2024_day6_a_t1: Day 6: Stockpile
Rare earths are an occasional by-product of refining. They are required for upgrading modules.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t1
	* Goals:	GainItem,0
	* GoalParameters:	Tags&RareEarth_T1up;Amount&15;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_mar_2024_day6_b_t1: The strength of modules can be increased through upgrades, which cost rare earths.
Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t1
	* Goals:	UpgradeOfficer,0
	* GoalParameters:	Amount&1

### qe_7days_mar_2024_day6_c_t1: The strength of modules can be increased through upgrades, which cost rare earths.
Small items such as strike craft, modules and parts can be built in the fabricator. Larger items such as escort ships and flagships must be constructed at shipyards provided at larger stations.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t1
	* Goals:	Craft,0
	* GoalParameters:	Category&Crafting;Tags&T1up;Amount&1

### qe_7days_mar_2024_day6_d_t1: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t1
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedT1_ShipsDestroyedT2_ShipsDestroyedT3_ShipsDestroyedT4;Amount&15

## ql_7days_mar_2024_day6_t2

### qe_7days_mar_2024_day6_a_t2: Day 6: Stockpile
Rare earths are an occasional by-product of refining. They are required for upgrading modules.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t2
	* Goals:	GainItem,0
	* GoalParameters:	Tags&RareEarth_T2up;Amount&15;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_mar_2024_day6_b_t2: The strength of modules can be increased through upgrades, which cost rare earths.
The strength of modules can be increased through upgrades, which cost rare earths.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t2
	* Goals:	Craft,0
	* GoalParameters:	Category&Upgrade;Tags&External_Module_T1up;Amount&1

### qe_7days_mar_2024_day6_c_t2: The strength of modules can be increased through upgrades, which cost rare earths.
Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t2
	* Goals:	Craft,0
	* GoalParameters:	Category&Crafting;Tags&Part_T2up;Amount&25

### qe_7days_mar_2024_day6_d_t2: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t2
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedT2_ShipsDestroyedT3_ShipsDestroyedT4;Amount&15

## ql_7days_mar_2024_day6_t3

### qe_7days_mar_2024_day6_a_t3: Day 6: Stockpile
Rare earths are an occasional by-product of refining. They are required for upgrading modules.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t3
	* Goals:	GainItem,0
	* GoalParameters:	Tags&RareEarth_T3up;Amount&15;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_mar_2024_day6_b_t3: The strength of modules can be increased through upgrades, which cost rare earths.
The strength of modules can be increased through upgrades, which cost rare earths.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t3
	* Goals:	Craft,0
	* GoalParameters:	Category&Upgrade;Tags&External_Module_T2up;Amount&1

### qe_7days_mar_2024_day6_c_t3: The strength of modules can be increased through upgrades, which cost rare earths.
The strength of modules can be increased through upgrades, which cost rare earths.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t3
	* Goals:	Craft,0
	* GoalParameters:	Category&Upgrade;Tags&Internal_Module_T2up;Amount&1

### qe_7days_mar_2024_day6_d_t3: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t3
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedT3_ShipsDestroyedT4;Amount&15

## ql_7days_mar_2024_day6_t4

### qe_7days_mar_2024_day6_a_t4: Day 6: Stockpile
Rare earths are an occasional by-product of refining. They are required for upgrading modules.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t4
	* Goals:	GainItem,0
	* GoalParameters:	Tags&RareEarth_T4up;Amount&15;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_mar_2024_day6_b_t4: The strength of modules can be increased through upgrades, which cost rare earths.
The strength of modules can be increased through upgrades, which cost rare earths.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t4
	* Goals:	Craft,0
	* GoalParameters:	Category&Upgrade;Tags&External_Module_T3up;Amount&1

### qe_7days_mar_2024_day6_c_t4: The strength of modules can be increased through upgrades, which cost rare earths.
The strength of modules can be increased through upgrades, which cost rare earths.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t4
	* Goals:	Craft,0
	* GoalParameters:	Category&Upgrade;Tags&Internal_Module_T3up;Amount&1

### qe_7days_mar_2024_day6_d_t4: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t4
	* Goals:	Statistic,0
	* GoalParameters:	Id&ShipsDestroyedT4;Amount&15

## ql_7days_mar_2024_day7_t1

### qe_7days_mar_2024_day7_a_t1: Day 7: Enemy Contact
Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t1
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&3;Tags&T1up;Mode&Generated

### qe_7days_mar_2024_day7_b_t1: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t1
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedT1_ShipsDestroyedT2_ShipsDestroyedT3_ShipsDestroyedT4;Amount&15

### qe_7days_mar_2024_day7_c_t1: When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.
When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t1
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Salvage_T1up;Amount&3;ExcludedSources&MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_mar_2024_day7_d_t1: Strikes are difficult missions that require a strong fleet from several commanders to beat. Completing a strike rewards code fragments, which can be turned in for special blueprints.
Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t1
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&3;Tags&T1up;Mode&Generated

## ql_7days_mar_2024_day7_t2

### qe_7days_mar_2024_day7_a_t2: Day 7: Enemy Contact
Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t2
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&3;Tags&T2up;Mode&Generated

### qe_7days_mar_2024_day7_b_t2: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t2
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedT2_ShipsDestroyedT3_ShipsDestroyedT4;Amount&15

### qe_7days_mar_2024_day7_c_t2: When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.
When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t2
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Salvage_T2up;Amount&3;ExcludedSources&MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_mar_2024_day7_d_t2: Strikes are difficult missions that require a strong fleet from several commanders to beat. Completing a strike rewards code fragments, which can be turned in for special blueprints.
Strikes are difficult missions that require a strong fleet from several commanders to beat. Completing a strike rewards code fragments, which can be turned in for special blueprints.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t2
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&1;Mode&Strike;Tags&T1up

## ql_7days_mar_2024_day7_t3

### qe_7days_mar_2024_day7_a_t3: Day 7: Enemy Contact
Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t3
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&3;Tags&T3up;Mode&Generated

### qe_7days_mar_2024_day7_b_t3: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t3
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedT3_ShipsDestroyedT4;Amount&15

### qe_7days_mar_2024_day7_c_t3: When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.
When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t3
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Salvage_T3up;Amount&3;ExcludedSources&MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_mar_2024_day7_d_t3: Strikes are difficult missions that require a strong fleet from several commanders to beat. Completing a strike rewards code fragments, which can be turned in for special blueprints.
Strikes are difficult missions that require a strong fleet from several commanders to beat. Completing a strike rewards code fragments, which can be turned in for special blueprints.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t3
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&1;Mode&Strike;Tags&T2up

## ql_7days_mar_2024_day7_t4

### qe_7days_mar_2024_day7_a_t4: Day 7: Enemy Contact
Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t4
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&3;Tags&T4up;Mode&Generated

### qe_7days_mar_2024_day7_b_t4: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t4
	* Goals:	Statistic,0
	* GoalParameters:	Id&ShipsDestroyedT4;Amount&15

### qe_7days_mar_2024_day7_c_t4: When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.
When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t4
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Salvage_T4up;Amount&3;ExcludedSources&MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_mar_2024_day7_d_t4: Strikes are difficult missions that require a strong fleet from several commanders to beat. Completing a strike rewards code fragments, which can be turned in for special blueprints.
Strikes are difficult missions that require a strong fleet from several commanders to beat. Completing a strike rewards code fragments, which can be turned in for special blueprints.
	* Type:	Event
	* EventId:	event_monthlyEvent_2024_03_01_t4
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&1;Mode&Strike;Tags&T3up

## ql_7days_2023_08_day1_t1

### qe_7days_2023_08_day1_a_t1: Day 1: Lay of the Land
Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t1
	* Goals:	Scan,0
	* GoalParameters:	Tags&InSystem_T1up;Amount&10;Analyzed&True

### qe_7days_2023_08_day1_b_t1: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t1
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedT1_ShipsDestroyedT2_ShipsDestroyedT3_ShipsDestroyedT4;Amount&15

### qe_7days_2023_08_day1_c_t1: Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.
Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t1
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Asteroid_Crud_T1up;Amount&800;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_2023_08_day1_d_t1: Rare earths are an occasional by-product of refining. They are required for upgrading modules.
Rare earths are an occasional by-product of refining. They are required for upgrading modules.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t1
	* Goals:	GainItem,0
	* GoalParameters:	Tags&RareEarth_T1up;Amount&15;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

## ql_7days_2023_08_day1_t2

### qe_7days_2023_08_day1_a_t2: Day 1: Lay of the Land
Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t2
	* Goals:	Scan,0
	* GoalParameters:	Tags&InSystem_T2up;Amount&10;Analyzed&True

### qe_7days_2023_08_day1_b_t2: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t2
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedT2_ShipsDestroyedT3_ShipsDestroyedT4;Amount&15

### qe_7days_2023_08_day1_c_t2: Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.
Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t2
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Asteroid_Crud_T2up;Amount&1000;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_2023_08_day1_d_t2: Rare earths are an occasional by-product of refining. They are required for upgrading modules.
Rare earths are an occasional by-product of refining. They are required for upgrading modules.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t2
	* Goals:	GainItem,0
	* GoalParameters:	Tags&RareEarth_T2up;Amount&15;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

## ql_7days_2023_08_day1_t3

### qe_7days_2023_08_day1_a_t3: Day 1: Lay of the Land
Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t3
	* Goals:	Scan,0
	* GoalParameters:	Tags&InSystem_T3up;Amount&10;Analyzed&True

### qe_7days_2023_08_day1_b_t3: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t3
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedT3_ShipsDestroyedT4;Amount&15

### qe_7days_2023_08_day1_c_t3: Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.
Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t3
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Gas_T3up;Amount&800;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_2023_08_day1_d_t3: Rare earths are an occasional by-product of refining. They are required for upgrading modules.
Rare earths are an occasional by-product of refining. They are required for upgrading modules.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t3
	* Goals:	GainItem,0
	* GoalParameters:	Tags&RareEarth_T3up;Amount&15;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

## ql_7days_2023_08_day1_t4

### qe_7days_2023_08_day1_a_t4: Day 1: Lay of the Land
Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t4
	* Goals:	Scan,0
	* GoalParameters:	Tags&InSystem_T4up;Amount&10;Analyzed&True

### qe_7days_2023_08_day1_b_t4: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t4
	* Goals:	Statistic,0
	* GoalParameters:	Id&ShipsDestroyedT4;Amount&15

### qe_7days_2023_08_day1_c_t4: Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.
Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t4
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Gas_T4up;Amount&1000;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_2023_08_day1_d_t4: Rare earths are an occasional by-product of refining. They are required for upgrading modules.
Rare earths are an occasional by-product of refining. They are required for upgrading modules.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t4
	* Goals:	GainItem,0
	* GoalParameters:	Tags&RareEarth_T4up;Amount&15;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

## ql_7days_2023_08_day2_t1

### qe_7days_2023_08_day2_a_t1: Day 2: Meet & Greet
There are different types of assignments available in your assignment log.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t1
	* Goals:	CompleteQuest,0
	* GoalParameters:	Amount&5;Tags&T1up

### qe_7days_2023_08_day2_b_t1: Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.
During missions you will usually fight against enemy ships. They can be part of an assignment, or they can be found as signals through scanning.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t1
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&3;Tags&T1up

### qe_7days_2023_08_day2_c_t1: Complete liaison assignments to gain reputation for that faction. A higher reputation unlocks more items in that faction's liaison requisitions office.
Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t1
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Insignia_T1up;Amount&50;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_2023_08_day2_d_t1: Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t1
	* Goals:	UpgradeOfficer,0
	* GoalParameters:	Amount&1

## ql_7days_2023_08_day2_t2

### qe_7days_2023_08_day2_a_t2: Day 2: Meet & Greet
Completing liaison assignments for a faction increases your reputation level for that faction. Higher reputation levels unlock additional items in that faction's liaison requisitions office.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t2
	* Goals:	CompleteQuest,0
	* GoalParameters:	Amount&5;Tags&Faction_T2up

### qe_7days_2023_08_day2_b_t2: Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.
Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t2
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&3;Mode&Faction;Tags&T2up

### qe_7days_2023_08_day2_c_t2: Complete liaison assignments to gain reputation for that faction. A higher reputation unlocks more items in that faction's liaison requisitions office.
Complete liaison assignments to gain reputation for that faction. A higher reputation unlocks more items in that faction's liaison requisitions office.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t2
	* Goals:	Statistic,0
	* GoalParameters:	Ids&RepTr1_RepTanoch_RepYaot_RepAmassari;Amount&135

### qe_7days_2023_08_day2_d_t2: Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t2
	* Goals:	UpgradeOfficer,0
	* GoalParameters:	Amount&2

## ql_7days_2023_08_day2_t3

### qe_7days_2023_08_day2_a_t3: Day 2: Meet & Greet
Completing liaison assignments for a faction increases your reputation level for that faction. Higher reputation levels unlock additional items in that faction's liaison requisitions office.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t3
	* Goals:	CompleteQuest,0
	* GoalParameters:	Amount&5;Tags&Faction_T3up

### qe_7days_2023_08_day2_b_t3: Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.
Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t3
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&3;Mode&Faction;Tags&T3up

### qe_7days_2023_08_day2_c_t3: Complete liaison assignments to gain reputation for that faction. A higher reputation unlocks more items in that faction's liaison requisitions office.
Complete liaison assignments to gain reputation for that faction. A higher reputation unlocks more items in that faction's liaison requisitions office.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t3
	* Goals:	Statistic,0
	* GoalParameters:	Ids&RepTr1_RepTanoch_RepYaot_RepAmassari;Amount&180

### qe_7days_2023_08_day2_d_t3: Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t3
	* Goals:	UpgradeOfficer,0
	* GoalParameters:	Amount&3

## ql_7days_2023_08_day2_t4

### qe_7days_2023_08_day2_a_t4: Day 2: Meet & Greet
Completing liaison assignments for a faction increases your reputation level for that faction. Higher reputation levels unlock additional items in that faction's liaison requisitions office.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t4
	* Goals:	CompleteQuest,0
	* GoalParameters:	Amount&5;Tags&Faction_T4up

### qe_7days_2023_08_day2_b_t4: Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.
Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t4
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&3;Mode&Faction;Tags&T4up

### qe_7days_2023_08_day2_c_t4: Complete liaison assignments to gain reputation for that faction. A higher reputation unlocks more items in that faction's liaison requisitions office.
Complete liaison assignments to gain reputation for that faction. A higher reputation unlocks more items in that faction's liaison requisitions office.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t4
	* Goals:	Statistic,0
	* GoalParameters:	Ids&RepTr1_RepTanoch_RepYaot_RepAmassari;Amount&225

### qe_7days_2023_08_day2_d_t4: Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t4
	* Goals:	UpgradeOfficer,0
	* GoalParameters:	Amount&5

## ql_7days_2023_08_day3_t1

### qe_7days_2023_08_day3_a_t1: Day 3: Raw Materials
Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t1
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Asteroid_Crud_T1up;Amount&800;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_2023_08_day3_b_t1: Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.
Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t1
	* Goals:	Craft,0
	* GoalParameters:	Category&Refining;Tags&Asteroid_Refined_T1up;Amount&500

### qe_7days_2023_08_day3_c_t1: Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.
Small items such as strike craft, modules and parts can be built in the fabricator. Larger items such as escort ships and flagships must be constructed at shipyards provided at larger stations.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t1
	* Goals:	Craft,0
	* GoalParameters:	Category&Crafting;Tags&T1up;Amount&1

### qe_7days_2023_08_day3_d_t1: Items and resources can be sold for credits in the market at stations.
Items and resources can be sold for credits in the market at stations.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t1
	* Goals:	GainItem,0
	* GoalParameters:	Id&CR;Amount&150;ExcludedSources&BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

## ql_7days_2023_08_day3_t2

### qe_7days_2023_08_day3_a_t2: Day 3: Raw Materials
Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t2
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Asteroid_Crud_T2up;Amount&1000;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_2023_08_day3_b_t2: Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.
Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t2
	* Goals:	Craft,0
	* GoalParameters:	Category&Refining;Tags&Asteroid_Refined_T2up;Amount&500

### qe_7days_2023_08_day3_c_t2: Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.
Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t2
	* Goals:	Craft,0
	* GoalParameters:	Category&Crafting;Tags&Part_T2up;Amount&25

### qe_7days_2023_08_day3_d_t2: Items and resources can be sold for credits in the market at stations.
Items and resources can be sold for credits in the market at stations.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t2
	* Goals:	GainItem,0
	* GoalParameters:	Id&CR;Amount&300;ExcludedSources&BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

## ql_7days_2023_08_day3_t3

### qe_7days_2023_08_day3_a_t3: Day 3: Raw Materials
Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t3
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Asteroid_Crud_T3up;Amount&1200;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_2023_08_day3_b_t3: Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.
Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t3
	* Goals:	Craft,0
	* GoalParameters:	Category&Refining;Tags&Asteroid_Refined_T3up;Amount&500

### qe_7days_2023_08_day3_c_t3: Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.
Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t3
	* Goals:	Craft,0
	* GoalParameters:	Category&Crafting;Tags&Part_T3up;Amount&25

### qe_7days_2023_08_day3_d_t3: Items and resources can be sold for credits in the market at stations.
Items and resources can be sold for credits in the market at stations.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t3
	* Goals:	GainItem,0
	* GoalParameters:	Id&CR;Amount&600;ExcludedSources&BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

## ql_7days_2023_08_day3_t4

### qe_7days_2023_08_day3_a_t4: Day 3: Raw Materials
Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t4
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Asteroid_Crud_T4up;Amount&1400;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_2023_08_day3_b_t4: Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.
Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t4
	* Goals:	Craft,0
	* GoalParameters:	Category&Refining;Tags&Asteroid_Refined_T4up;Amount&500

### qe_7days_2023_08_day3_c_t4: Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.
Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t4
	* Goals:	Craft,0
	* GoalParameters:	Category&Crafting;Tags&Part_T4up;Amount&25

### qe_7days_2023_08_day3_d_t4: Items and resources can be sold for credits in the market at stations.
Items and resources can be sold for credits in the market at stations.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t4
	* Goals:	GainItem,0
	* GoalParameters:	Id&CR;Amount&1200;ExcludedSources&BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

## ql_7days_2023_08_day4_t1

### qe_7days_2023_08_day4_a_t1: Day 4: Hypothesis
Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t1
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&3;Tags&T1up;Mode&Generated

### qe_7days_2023_08_day4_b_t1: Progenitor relics can be found in relic signature signals. Relics can be sold on the market for credits, though some liaison offices may be interested in relics as well.
Progenitor relics can be found in relic signature signals. Relics can be sold on the market for credits, though some liaison offices may be interested in relics as well.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t1
	* Goals:	GainItem,0
	* GoalParameters:	Tags&ProgenitorRelic_T1up;Amount&1;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_2023_08_day4_c_t1: Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.
Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t1
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedProgenitorT1_ShipsDestroyedProgenitorT2_ShipsDestroyedProgenitorT3_ShipsDestroyedProgenitorT4;Amount&7

### qe_7days_2023_08_day4_d_t1: Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.
Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t1
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&1;Tags&Rare_T1up;Mode&Generated

## ql_7days_2023_08_day4_t2

### qe_7days_2023_08_day4_a_t2: Day 4: Hypothesis
Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t2
	* Goals:	GainItem,0
	* GoalParameters:	Id&RP;Amount&200;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_2023_08_day4_b_t2: Progenitor relics can be found in relic signature signals. Relics can be sold on the market for credits, though some liaison offices may be interested in relics as well.
Progenitor relics can be found in relic signature signals. Relics can be sold on the market for credits, though some liaison offices may be interested in relics as well.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t2
	* Goals:	GainItem,0
	* GoalParameters:	Tags&ProgenitorRelic_T2up;Amount&1;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_2023_08_day4_c_t2: Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.
Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t2
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedProgenitorT2_ShipsDestroyedProgenitorT3_ShipsDestroyedProgenitorT4;Amount&7

### qe_7days_2023_08_day4_d_t2: Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.
Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t2
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&1;Tags&Epic_T2up;Mode&Generated

## ql_7days_2023_08_day4_t3

### qe_7days_2023_08_day4_a_t3: Day 4: Hypothesis
Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t3
	* Goals:	GainItem,0
	* GoalParameters:	Id&RP;Amount&200;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_2023_08_day4_b_t3: Progenitor relics can be found in relic signature signals. Relics can be sold on the market for credits, though some liaison offices may be interested in relics as well.
Progenitor relics can be found in relic signature signals. Relics can be sold on the market for credits, though some liaison offices may be interested in relics as well.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t3
	* Goals:	GainItem,0
	* GoalParameters:	Tags&ProgenitorRelic_T3up;Amount&1;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_2023_08_day4_c_t3: Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.
Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t3
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedProgenitorT3_ShipsDestroyedProgenitorT4;Amount&7

### qe_7days_2023_08_day4_d_t3: Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.
Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t3
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&1;Tags&Epic_T3up;Mode&Generated

## ql_7days_2023_08_day4_t4

### qe_7days_2023_08_day4_a_t4: Day 4: Hypothesis
Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t4
	* Goals:	GainItem,0
	* GoalParameters:	Id&RP;Amount&200;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_2023_08_day4_b_t4: Progenitor relics can be found in relic signature signals. Relics can be sold on the market for credits, though some liaison offices may be interested in relics as well.
Progenitor relics can be found in relic signature signals. Relics can be sold on the market for credits, though some liaison offices may be interested in relics as well.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t4
	* Goals:	GainItem,0
	* GoalParameters:	Tags&ProgenitorRelic_T4up;Amount&1;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_2023_08_day4_c_t4: Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.
Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t4
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedProgenitorT4;Amount&7

### qe_7days_2023_08_day4_d_t4: Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.
Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t4
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&1;Tags&Epic_T4up;Mode&Generated

## ql_7days_2023_08_day5_t1

### qe_7days_2023_08_day5_a_t1: Day 5: Lessons
Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t1
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&3;Tags&T1up;Mode&Generated

### qe_7days_2023_08_day5_b_t1: Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.
Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t1
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Insignia_T1up;Amount&50;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_2023_08_day5_c_t1: Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t1
	* Goals:	UpgradeOfficer,0
	* GoalParameters:	Amount&1

### qe_7days_2023_08_day5_d_t1: Discharging officers grants credits and insignias, which can be used to level up other officers.
Discharging officers grants credits and insignias, which can be used to level up other officers.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t1
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Insignia;Amount&2;ExcludedSources&OpenContainer_QuestReward_MissionReward_ClaimMail_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_BuyItem_SellItem

## ql_7days_2023_08_day5_t2

### qe_7days_2023_08_day5_a_t2: Day 5: Lessons
Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t2
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&3;Tags&T2up;Mode&Generated

### qe_7days_2023_08_day5_b_t2: Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.
Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t2
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Insignia_T2up;Amount&50;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_2023_08_day5_c_t2: Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t2
	* Goals:	UpgradeOfficer,0
	* GoalParameters:	Amount&2

### qe_7days_2023_08_day5_d_t2: Discharging officers grants credits and insignias, which can be used to level up other officers.
Discharging officers grants credits and insignias, which can be used to level up other officers.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t2
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Insignia;Amount&4;ExcludedSources&OpenContainer_QuestReward_MissionReward_ClaimMail_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_BuyItem_SellItem

## ql_7days_2023_08_day5_t3

### qe_7days_2023_08_day5_a_t3: Day 5: Lessons
Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t3
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&3;Tags&T3up;Mode&Generated

### qe_7days_2023_08_day5_b_t3: Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.
Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t3
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Insignia_T3up;Amount&50;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_2023_08_day5_c_t3: Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t3
	* Goals:	UpgradeOfficer,0
	* GoalParameters:	Amount&3

### qe_7days_2023_08_day5_d_t3: Discharging officers grants credits and insignias, which can be used to level up other officers.
Discharging officers grants credits and insignias, which can be used to level up other officers.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t3
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Insignia;Amount&6;ExcludedSources&OpenContainer_QuestReward_MissionReward_ClaimMail_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_BuyItem_SellItem

## ql_7days_2023_08_day5_t4

### qe_7days_2023_08_day5_a_t4: Day 5: Lessons
Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t4
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&3;Tags&T4up;Mode&Generated

### qe_7days_2023_08_day5_b_t4: Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.
Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t4
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Insignia_T4up;Amount&50;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_2023_08_day5_c_t4: Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t4
	* Goals:	UpgradeOfficer,0
	* GoalParameters:	Amount&5

### qe_7days_2023_08_day5_d_t4: Discharging officers grants credits and insignias, which can be used to level up other officers.
Discharging officers grants credits and insignias, which can be used to level up other officers.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t4
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Insignia;Amount&10;ExcludedSources&OpenContainer_QuestReward_MissionReward_ClaimMail_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_BuyItem_SellItem

## ql_7days_2023_08_day6_t1

### qe_7days_2023_08_day6_a_t1: Day 6: Stockpile
Rare earths are an occasional by-product of refining. They are required for upgrading modules.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t1
	* Goals:	GainItem,0
	* GoalParameters:	Tags&RareEarth_T1up;Amount&15;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_2023_08_day6_b_t1: The strength of modules can be increased through upgrades, which cost rare earths.
Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t1
	* Goals:	UpgradeOfficer,0
	* GoalParameters:	Amount&1

### qe_7days_2023_08_day6_c_t1: The strength of modules can be increased through upgrades, which cost rare earths.
Small items such as strike craft, modules and parts can be built in the fabricator. Larger items such as escort ships and flagships must be constructed at shipyards provided at larger stations.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t1
	* Goals:	Craft,0
	* GoalParameters:	Category&Crafting;Tags&T1up;Amount&1

### qe_7days_2023_08_day6_d_t1: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t1
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedT1_ShipsDestroyedT2_ShipsDestroyedT3_ShipsDestroyedT4;Amount&15

## ql_7days_2023_08_day6_t2

### qe_7days_2023_08_day6_a_t2: Day 6: Stockpile
Rare earths are an occasional by-product of refining. They are required for upgrading modules.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t2
	* Goals:	GainItem,0
	* GoalParameters:	Tags&RareEarth_T2up;Amount&15;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_2023_08_day6_b_t2: The strength of modules can be increased through upgrades, which cost rare earths.
The strength of modules can be increased through upgrades, which cost rare earths.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t2
	* Goals:	Craft,0
	* GoalParameters:	Category&Upgrade;Tags&External_Module_T1up;Amount&1

### qe_7days_2023_08_day6_c_t2: The strength of modules can be increased through upgrades, which cost rare earths.
Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t2
	* Goals:	Craft,0
	* GoalParameters:	Category&Crafting;Tags&Part_T2up;Amount&25

### qe_7days_2023_08_day6_d_t2: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t2
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedT2_ShipsDestroyedT3_ShipsDestroyedT4;Amount&15

## ql_7days_2023_08_day6_t3

### qe_7days_2023_08_day6_a_t3: Day 6: Stockpile
Rare earths are an occasional by-product of refining. They are required for upgrading modules.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t3
	* Goals:	GainItem,0
	* GoalParameters:	Tags&RareEarth_T3up;Amount&15;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_2023_08_day6_b_t3: The strength of modules can be increased through upgrades, which cost rare earths.
The strength of modules can be increased through upgrades, which cost rare earths.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t3
	* Goals:	Craft,0
	* GoalParameters:	Category&Upgrade;Tags&External_Module_T2up;Amount&1

### qe_7days_2023_08_day6_c_t3: The strength of modules can be increased through upgrades, which cost rare earths.
The strength of modules can be increased through upgrades, which cost rare earths.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t3
	* Goals:	Craft,0
	* GoalParameters:	Category&Upgrade;Tags&Internal_Module_T2up;Amount&1

### qe_7days_2023_08_day6_d_t3: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t3
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedT3_ShipsDestroyedT4;Amount&15

## ql_7days_2023_08_day6_t4

### qe_7days_2023_08_day6_a_t4: Day 6: Stockpile
Rare earths are an occasional by-product of refining. They are required for upgrading modules.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t4
	* Goals:	GainItem,0
	* GoalParameters:	Tags&RareEarth_T4up;Amount&15;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_2023_08_day6_b_t4: The strength of modules can be increased through upgrades, which cost rare earths.
The strength of modules can be increased through upgrades, which cost rare earths.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t4
	* Goals:	Craft,0
	* GoalParameters:	Category&Upgrade;Tags&External_Module_T3up;Amount&1

### qe_7days_2023_08_day6_c_t4: The strength of modules can be increased through upgrades, which cost rare earths.
The strength of modules can be increased through upgrades, which cost rare earths.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t4
	* Goals:	Craft,0
	* GoalParameters:	Category&Upgrade;Tags&Internal_Module_T3up;Amount&1

### qe_7days_2023_08_day6_d_t4: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t4
	* Goals:	Statistic,0
	* GoalParameters:	Id&ShipsDestroyedT4;Amount&15

## ql_7days_2023_08_day7_t1

### qe_7days_2023_08_day7_a_t1: Day 7: Enemy Contact
Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t1
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&3;Tags&T1up;Mode&Generated

### qe_7days_2023_08_day7_b_t1: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t1
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedT1_ShipsDestroyedT2_ShipsDestroyedT3_ShipsDestroyedT4;Amount&15

### qe_7days_2023_08_day7_c_t1: When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.
When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t1
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Salvage_T1up;Amount&3;ExcludedSources&MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_2023_08_day7_d_t1: Strikes are difficult missions that require a strong fleet from several commanders to beat. Completing a strike rewards code fragments, which can be turned in for special blueprints.
Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t1
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&3;Tags&T1up;Mode&Generated

## ql_7days_2023_08_day7_t2

### qe_7days_2023_08_day7_a_t2: Day 7: Enemy Contact
Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t2
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&3;Tags&T2up;Mode&Generated

### qe_7days_2023_08_day7_b_t2: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t2
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedT2_ShipsDestroyedT3_ShipsDestroyedT4;Amount&15

### qe_7days_2023_08_day7_c_t2: When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.
When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t2
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Salvage_T2up;Amount&3;ExcludedSources&MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_2023_08_day7_d_t2: Strikes are difficult missions that require a strong fleet from several commanders to beat. Completing a strike rewards code fragments, which can be turned in for special blueprints.
Strikes are difficult missions that require a strong fleet from several commanders to beat. Completing a strike rewards code fragments, which can be turned in for special blueprints.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t2
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&1;Mode&Strike;Tags&T1up

## ql_7days_2023_08_day7_t3

### qe_7days_2023_08_day7_a_t3: Day 7: Enemy Contact
Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t3
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&3;Tags&T3up;Mode&Generated

### qe_7days_2023_08_day7_b_t3: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t3
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedT3_ShipsDestroyedT4;Amount&15

### qe_7days_2023_08_day7_c_t3: When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.
When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t3
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Salvage_T3up;Amount&3;ExcludedSources&MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_2023_08_day7_d_t3: Strikes are difficult missions that require a strong fleet from several commanders to beat. Completing a strike rewards code fragments, which can be turned in for special blueprints.
Strikes are difficult missions that require a strong fleet from several commanders to beat. Completing a strike rewards code fragments, which can be turned in for special blueprints.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t3
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&1;Mode&Strike;Tags&T2up

## ql_7days_2023_08_day7_t4

### qe_7days_2023_08_day7_a_t4: Day 7: Enemy Contact
Signals can be found through scanning. A better sensor module increases the chance to reveal a signal.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t4
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&3;Tags&T4up;Mode&Generated

### qe_7days_2023_08_day7_b_t4: The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t4
	* Goals:	Statistic,0
	* GoalParameters:	Id&ShipsDestroyedT4;Amount&15

### qe_7days_2023_08_day7_c_t4: When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.
When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t4
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Salvage_T4up;Amount&3;ExcludedSources&MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_7days_2023_08_day7_d_t4: Strikes are difficult missions that require a strong fleet from several commanders to beat. Completing a strike rewards code fragments, which can be turned in for special blueprints.
Strikes are difficult missions that require a strong fleet from several commanders to beat. Completing a strike rewards code fragments, which can be turned in for special blueprints.
	* Type:	Event
	* EventId:	event_7days_2023_08_21_t4
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&1;Mode&Strike;Tags&T3up

## ql_event_iyaFal_2023_t1

### qe_iyaFal_2023_day01_t1: No header for quest qe_iyaFal_2023_day01_t1
No description for quest qe_iyaFal_2023_day01_t1
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t1
	* Goals:	CompleteQuest,0
	* GoalParameters:	Amount&5;Tags&T1up

### qe_iyaFal_2023_day02_t1: No header for quest qe_iyaFal_2023_day02_t1
No description for quest qe_iyaFal_2023_day02_t1
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t1
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Salvage_T1up;Amount&5;ExcludedSources&MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_iyaFal_2023_day03_t1: No header for quest qe_iyaFal_2023_day03_t1
No description for quest qe_iyaFal_2023_day03_t1
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t1
	* Goals:	Craft,0
	* GoalParameters:	Category&Crafting;Tags&T1up;Amount&5

### qe_iyaFal_2023_day04_t1: No header for quest qe_iyaFal_2023_day04_t1
No description for quest qe_iyaFal_2023_day04_t1
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t1
	* MailsOnCompletion:	m_iyaFal_day4_log
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&3;Tags&T1up;Mode&Generated

### qe_iyaFal_2023_day05_t1: No header for quest qe_iyaFal_2023_day05_t1
No description for quest qe_iyaFal_2023_day05_t1
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t1
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&3;Tags&T1up

### qe_iyaFal_2023_day06_t1: No header for quest qe_iyaFal_2023_day06_t1
No description for quest qe_iyaFal_2023_day06_t1
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t1
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Insignia_T1up;Amount&50;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_iyaFal_2023_day07_t1: No header for quest qe_iyaFal_2023_day07_t1
No description for quest qe_iyaFal_2023_day07_t1
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t1
	* Goals:	UpgradeOfficer,0
	* GoalParameters:	Amount&1

### qe_iyaFal_2023_day08_t1: No header for quest qe_iyaFal_2023_day08_t1
No description for quest qe_iyaFal_2023_day08_t1
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t1
	* MailsOnCompletion:	m_iyaFal_day8_log
	* Goals:	GainItem,0
	* GoalParameters:	Tags&ProgenitorRelic_T1up;Amount&1;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_iyaFal_2023_day09_t1: No header for quest qe_iyaFal_2023_day09_t1
No description for quest qe_iyaFal_2023_day09_t1
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t1
	* Goals:	CompleteQuest,0
	* GoalParameters:	Amount&5;Tags&T1up

### qe_iyaFal_2023_day10_t1: No header for quest qe_iyaFal_2023_day10_t1
No description for quest qe_iyaFal_2023_day10_t1
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t1
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Salvage_T1up;Amount&5;ExcludedSources&MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_iyaFal_2023_day11_t1: No header for quest qe_iyaFal_2023_day11_t1
No description for quest qe_iyaFal_2023_day11_t1
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t1
	* Goals:	Craft,0
	* GoalParameters:	Category&Crafting;Tags&T1up;Amount&5

### qe_iyaFal_2023_day12_t1: No header for quest qe_iyaFal_2023_day12_t1
No description for quest qe_iyaFal_2023_day12_t1
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t1
	* MailsOnCompletion:	m_iyaFal_day12_log
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&1;Tags&Rare_T1up;Mode&Generated

### qe_iyaFal_2023_day13_t1: No header for quest qe_iyaFal_2023_day13_t1
No description for quest qe_iyaFal_2023_day13_t1
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t1
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Insignia_T1up;Amount&50;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_iyaFal_2023_day14_t1: No header for quest qe_iyaFal_2023_day14_t1
No description for quest qe_iyaFal_2023_day14_t1
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t1
	* Goals:	GainItem,0
	* GoalParameters:	Tags&ProgenitorRelic_T1up;Amount&1;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_iyaFal_2023_day15_t1: No header for quest qe_iyaFal_2023_day15_t1
No description for quest qe_iyaFal_2023_day15_t1
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t1
	* Goals:	CompleteMission,0
	* GoalParameters:	Id&event_iyaFal2023_Escort_t1

## ql_event_iyaFal_2023_epilog_t1

### qe_iyaFal_2023_epi01_t1: No header for quest qe_iyaFal_2023_epi01_t1
No description for quest qe_iyaFal_2023_epi01_t1
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t1
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Asteroid_Crud_T1up;Amount&1000;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_iyaFal_2023_epi02_t1: No header for quest qe_iyaFal_2023_epi02_t1
No description for quest qe_iyaFal_2023_epi02_t1
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t1
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedProgenitorT1_ShipsDestroyedProgenitorT2_ShipsDestroyedProgenitorT3_ShipsDestroyedProgenitorT4;Amount&10

### qe_iyaFal_2023_epi03_t1: No header for quest qe_iyaFal_2023_epi03_t1
No description for quest qe_iyaFal_2023_epi03_t1
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t1
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Insignia_T1up;Amount&50;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_iyaFal_2023_epi04_t1: No header for quest qe_iyaFal_2023_epi04_t1
No description for quest qe_iyaFal_2023_epi04_t1
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t1
	* Goals:	UpgradeOfficer,0
	* GoalParameters:	Amount&1

### qe_iyaFal_2023_epi05_t1: No header for quest qe_iyaFal_2023_epi05_t1
No description for quest qe_iyaFal_2023_epi05_t1
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t1
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&1;Tags&Rare_T1up;Mode&Generated

## ql_event_iyaFal_2023_t2

### qe_iyaFal_2023_day01_t2: No header for quest qe_iyaFal_2023_day01_t2
No description for quest qe_iyaFal_2023_day01_t2
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t2
	* Goals:	CompleteQuest,0
	* GoalParameters:	Amount&5;Tags&Faction_Tr1_T2up

### qe_iyaFal_2023_day02_t2: No header for quest qe_iyaFal_2023_day02_t2
No description for quest qe_iyaFal_2023_day02_t2
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t2
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Salvage_T2up;Amount&5;ExcludedSources&MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_iyaFal_2023_day03_t2: No header for quest qe_iyaFal_2023_day03_t2
No description for quest qe_iyaFal_2023_day03_t2
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t2
	* Goals:	Craft,0
	* GoalParameters:	Category&Crafting;Tags&Part_T2up;Amount&100

### qe_iyaFal_2023_day04_t2: No header for quest qe_iyaFal_2023_day04_t2
No description for quest qe_iyaFal_2023_day04_t2
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t2
	* MailsOnCompletion:	m_iyaFal_day4_log
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&3;Tags&T2up;Mode&Generated

### qe_iyaFal_2023_day05_t2: No header for quest qe_iyaFal_2023_day05_t2
No description for quest qe_iyaFal_2023_day05_t2
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t2
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&3;Mode&Faction;Tags&T2up

### qe_iyaFal_2023_day06_t2: No header for quest qe_iyaFal_2023_day06_t2
No description for quest qe_iyaFal_2023_day06_t2
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t2
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Insignia_T2up;Amount&50;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_iyaFal_2023_day07_t2: No header for quest qe_iyaFal_2023_day07_t2
No description for quest qe_iyaFal_2023_day07_t2
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t2
	* Goals:	UpgradeOfficer,0
	* GoalParameters:	Amount&2

### qe_iyaFal_2023_day08_t2: No header for quest qe_iyaFal_2023_day08_t2
No description for quest qe_iyaFal_2023_day08_t2
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t2
	* MailsOnCompletion:	m_iyaFal_day8_log
	* Goals:	GainItem,0
	* GoalParameters:	Tags&ProgenitorRelic_T2up;Amount&1;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_iyaFal_2023_day09_t2: No header for quest qe_iyaFal_2023_day09_t2
No description for quest qe_iyaFal_2023_day09_t2
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t2
	* Goals:	CompleteQuest,0
	* GoalParameters:	Amount&5;Tags&Faction_Tr1_T2up

### qe_iyaFal_2023_day10_t2: No header for quest qe_iyaFal_2023_day10_t2
No description for quest qe_iyaFal_2023_day10_t2
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t2
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Salvage_T2up;Amount&5;ExcludedSources&MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_iyaFal_2023_day11_t2: No header for quest qe_iyaFal_2023_day11_t2
No description for quest qe_iyaFal_2023_day11_t2
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t2
	* Goals:	GainItem,0
	* GoalParameters:	Id&RP;Amount&400;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_iyaFal_2023_day12_t2: No header for quest qe_iyaFal_2023_day12_t2
No description for quest qe_iyaFal_2023_day12_t2
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t2
	* MailsOnCompletion:	m_iyaFal_day12_log
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&1;Tags&Epic_T2up;Mode&Generated

### qe_iyaFal_2023_day13_t2: No header for quest qe_iyaFal_2023_day13_t2
No description for quest qe_iyaFal_2023_day13_t2
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t2
	* Goals:	Statistic,0
	* GoalParameters:	Ids&RepTr1;Amount&135

### qe_iyaFal_2023_day14_t2: No header for quest qe_iyaFal_2023_day14_t2
No description for quest qe_iyaFal_2023_day14_t2
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t2
	* Goals:	GainItem,0
	* GoalParameters:	Tags&ProgenitorRelic_T2up;Amount&1;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_iyaFal_2023_day15_t2: No header for quest qe_iyaFal_2023_day15_t2
No description for quest qe_iyaFal_2023_day15_t2
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t2
	* Goals:	CompleteMission,0
	* GoalParameters:	Id&event_iyaFal2023_Escort_t2

## ql_event_iyaFal_2023_epilog_t2

### qe_iyaFal_2023_epi01_t2: No header for quest qe_iyaFal_2023_epi01_t2
No description for quest qe_iyaFal_2023_epi01_t2
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t2
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Asteroid_Crud_T2up;Amount&1200;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_iyaFal_2023_epi02_t2: No header for quest qe_iyaFal_2023_epi02_t2
No description for quest qe_iyaFal_2023_epi02_t2
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t2
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedProgenitorT2_ShipsDestroyedProgenitorT3_ShipsDestroyedProgenitorT4;Amount&10

### qe_iyaFal_2023_epi03_t2: No header for quest qe_iyaFal_2023_epi03_t2
No description for quest qe_iyaFal_2023_epi03_t2
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t2
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Insignia_T2up;Amount&50;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_iyaFal_2023_epi04_t2: No header for quest qe_iyaFal_2023_epi04_t2
No description for quest qe_iyaFal_2023_epi04_t2
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t2
	* Goals:	UpgradeOfficer,0
	* GoalParameters:	Amount&2

### qe_iyaFal_2023_epi05_t2: No header for quest qe_iyaFal_2023_epi05_t2
No description for quest qe_iyaFal_2023_epi05_t2
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t2
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&1;Mode&Strike;Tags&T1up

## ql_event_iyaFal_2023_t3

### qe_iyaFal_2023_day01_t3: No header for quest qe_iyaFal_2023_day01_t3
No description for quest qe_iyaFal_2023_day01_t3
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t3
	* Goals:	CompleteQuest,0
	* GoalParameters:	Amount&5;Tags&Faction_Tr1_T3up

### qe_iyaFal_2023_day02_t3: No header for quest qe_iyaFal_2023_day02_t3
No description for quest qe_iyaFal_2023_day02_t3
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t3
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Salvage_T3up;Amount&5;ExcludedSources&MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_iyaFal_2023_day03_t3: No header for quest qe_iyaFal_2023_day03_t3
No description for quest qe_iyaFal_2023_day03_t3
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t3
	* Goals:	Craft,0
	* GoalParameters:	Category&Crafting;Tags&Part_T3up;Amount&100

### qe_iyaFal_2023_day04_t3: No header for quest qe_iyaFal_2023_day04_t3
No description for quest qe_iyaFal_2023_day04_t3
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t3
	* MailsOnCompletion:	m_iyaFal_day4_log
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&3;Tags&T3up;Mode&Generated

### qe_iyaFal_2023_day05_t3: No header for quest qe_iyaFal_2023_day05_t3
No description for quest qe_iyaFal_2023_day05_t3
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t3
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&3;Mode&Faction;Tags&T3up

### qe_iyaFal_2023_day06_t3: No header for quest qe_iyaFal_2023_day06_t3
No description for quest qe_iyaFal_2023_day06_t3
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t3
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Insignia_T3up;Amount&50;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_iyaFal_2023_day07_t3: No header for quest qe_iyaFal_2023_day07_t3
No description for quest qe_iyaFal_2023_day07_t3
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t3
	* Goals:	UpgradeOfficer,0
	* GoalParameters:	Amount&3

### qe_iyaFal_2023_day08_t3: No header for quest qe_iyaFal_2023_day08_t3
No description for quest qe_iyaFal_2023_day08_t3
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t3
	* MailsOnCompletion:	m_iyaFal_day8_log
	* Goals:	GainItem,0
	* GoalParameters:	Tags&ProgenitorRelic_T3up;Amount&1;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_iyaFal_2023_day09_t3: No header for quest qe_iyaFal_2023_day09_t3
No description for quest qe_iyaFal_2023_day09_t3
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t3
	* Goals:	CompleteQuest,0
	* GoalParameters:	Amount&5;Tags&Faction_Tr1_T3up

### qe_iyaFal_2023_day10_t3: No header for quest qe_iyaFal_2023_day10_t3
No description for quest qe_iyaFal_2023_day10_t3
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t3
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Salvage_T3up;Amount&5;ExcludedSources&MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_iyaFal_2023_day11_t3: No header for quest qe_iyaFal_2023_day11_t3
No description for quest qe_iyaFal_2023_day11_t3
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t3
	* Goals:	GainItem,0
	* GoalParameters:	Id&RP;Amount&400;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_iyaFal_2023_day12_t3: No header for quest qe_iyaFal_2023_day12_t3
No description for quest qe_iyaFal_2023_day12_t3
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t3
	* MailsOnCompletion:	m_iyaFal_day12_log
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&1;Tags&Epic_T3up;Mode&Generated

### qe_iyaFal_2023_day13_t3: No header for quest qe_iyaFal_2023_day13_t3
No description for quest qe_iyaFal_2023_day13_t3
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t3
	* Goals:	Statistic,0
	* GoalParameters:	Ids&RepTr1;Amount&180

### qe_iyaFal_2023_day14_t3: No header for quest qe_iyaFal_2023_day14_t3
No description for quest qe_iyaFal_2023_day14_t3
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t3
	* Goals:	GainItem,0
	* GoalParameters:	Tags&ProgenitorRelic_T3up;Amount&1;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_iyaFal_2023_day15_t3: No header for quest qe_iyaFal_2023_day15_t3
No description for quest qe_iyaFal_2023_day15_t3
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t3
	* Goals:	CompleteMission,0
	* GoalParameters:	Id&event_iyaFal2023_Escort_t3

## ql_event_iyaFal_2023_epilog_t3

### qe_iyaFal_2023_epi01_t3: No header for quest qe_iyaFal_2023_epi01_t3
No description for quest qe_iyaFal_2023_epi01_t3
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t3
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Gas_T3up;Amount&1000;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_iyaFal_2023_epi02_t3: No header for quest qe_iyaFal_2023_epi02_t3
No description for quest qe_iyaFal_2023_epi02_t3
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t3
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedProgenitorT3_ShipsDestroyedProgenitorT4;Amount&10

### qe_iyaFal_2023_epi03_t3: No header for quest qe_iyaFal_2023_epi03_t3
No description for quest qe_iyaFal_2023_epi03_t3
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t3
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Insignia_T3up;Amount&50;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_iyaFal_2023_epi04_t3: No header for quest qe_iyaFal_2023_epi04_t3
No description for quest qe_iyaFal_2023_epi04_t3
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t3
	* Goals:	UpgradeOfficer,0
	* GoalParameters:	Amount&3

### qe_iyaFal_2023_epi05_t3: No header for quest qe_iyaFal_2023_epi05_t3
No description for quest qe_iyaFal_2023_epi05_t3
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t3
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&3;Mode&Strike;Tags&T2up

## ql_event_iyaFal_2023_t4

### qe_iyaFal_2023_day01_t4: No header for quest qe_iyaFal_2023_day01_t4
No description for quest qe_iyaFal_2023_day01_t4
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t4
	* Goals:	CompleteQuest,0
	* GoalParameters:	Amount&5;Tags&Faction_T4up

### qe_iyaFal_2023_day02_t4: No header for quest qe_iyaFal_2023_day02_t4
No description for quest qe_iyaFal_2023_day02_t4
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t4
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Salvage_T4up;Amount&5;ExcludedSources&MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_iyaFal_2023_day03_t4: No header for quest qe_iyaFal_2023_day03_t4
No description for quest qe_iyaFal_2023_day03_t4
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t4
	* Goals:	Craft,0
	* GoalParameters:	Category&Crafting;Tags&Part_T4up;Amount&100

### qe_iyaFal_2023_day04_t4: No header for quest qe_iyaFal_2023_day04_t4
No description for quest qe_iyaFal_2023_day04_t4
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t4
	* MailsOnCompletion:	m_iyaFal_day4_log
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&3;Tags&T4up;Mode&Generated

### qe_iyaFal_2023_day05_t4: No header for quest qe_iyaFal_2023_day05_t4
No description for quest qe_iyaFal_2023_day05_t4
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t4
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&3;Mode&Faction;Tags&T4up

### qe_iyaFal_2023_day06_t4: No header for quest qe_iyaFal_2023_day06_t4
No description for quest qe_iyaFal_2023_day06_t4
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t4
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Insignia_T4up;Amount&50;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_iyaFal_2023_day07_t4: No header for quest qe_iyaFal_2023_day07_t4
No description for quest qe_iyaFal_2023_day07_t4
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t4
	* Goals:	UpgradeOfficer,0
	* GoalParameters:	Amount&5

### qe_iyaFal_2023_day08_t4: No header for quest qe_iyaFal_2023_day08_t4
No description for quest qe_iyaFal_2023_day08_t4
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t4
	* MailsOnCompletion:	m_iyaFal_day8_log
	* Goals:	GainItem,0
	* GoalParameters:	Tags&ProgenitorRelic_T4up;Amount&1;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_iyaFal_2023_day09_t4: No header for quest qe_iyaFal_2023_day09_t4
No description for quest qe_iyaFal_2023_day09_t4
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t4
	* Goals:	CompleteQuest,0
	* GoalParameters:	Amount&5;Tags&Faction_T4up

### qe_iyaFal_2023_day10_t4: No header for quest qe_iyaFal_2023_day10_t4
No description for quest qe_iyaFal_2023_day10_t4
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t4
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Salvage_T4up;Amount&5;ExcludedSources&MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_iyaFal_2023_day11_t4: No header for quest qe_iyaFal_2023_day11_t4
No description for quest qe_iyaFal_2023_day11_t4
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t4
	* Goals:	GainItem,0
	* GoalParameters:	Id&RP;Amount&400;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_iyaFal_2023_day12_t4: No header for quest qe_iyaFal_2023_day12_t4
No description for quest qe_iyaFal_2023_day12_t4
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t4
	* MailsOnCompletion:	m_iyaFal_day12_log
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&1;Tags&Epic_T4up;Mode&Generated

### qe_iyaFal_2023_day13_t4: No header for quest qe_iyaFal_2023_day13_t4
No description for quest qe_iyaFal_2023_day13_t4
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t4
	* Goals:	Statistic,0
	* GoalParameters:	Ids&RepTr1;Amount&225

### qe_iyaFal_2023_day14_t4: No header for quest qe_iyaFal_2023_day14_t4
No description for quest qe_iyaFal_2023_day14_t4
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t4
	* Goals:	GainItem,0
	* GoalParameters:	Tags&ProgenitorRelic_T4up;Amount&1;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_iyaFal_2023_day15_t4: No header for quest qe_iyaFal_2023_day15_t4
No description for quest qe_iyaFal_2023_day15_t4
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t4
	* Goals:	CompleteMission,0
	* GoalParameters:	Id&event_iyaFal2023_Escort_t4

## ql_event_iyaFal_2023_epilog_t4

### qe_iyaFal_2023_epi01_t4: No header for quest qe_iyaFal_2023_epi01_t4
No description for quest qe_iyaFal_2023_epi01_t4
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t4
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Gas_T4up;Amount&1200;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_iyaFal_2023_epi02_t4: No header for quest qe_iyaFal_2023_epi02_t4
No description for quest qe_iyaFal_2023_epi02_t4
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t4
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedProgenitorT4;Amount&10

### qe_iyaFal_2023_epi03_t4: No header for quest qe_iyaFal_2023_epi03_t4
No description for quest qe_iyaFal_2023_epi03_t4
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t4
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Insignia_T4up;Amount&50;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_iyaFal_2023_epi04_t4: No header for quest qe_iyaFal_2023_epi04_t4
No description for quest qe_iyaFal_2023_epi04_t4
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t4
	* Goals:	UpgradeOfficer,0
	* GoalParameters:	Amount&5

### qe_iyaFal_2023_epi05_t4: No header for quest qe_iyaFal_2023_epi05_t4
No description for quest qe_iyaFal_2023_epi05_t4
	* Type:	Event
	* EventId:	event_season_iyaFal_2023_t4
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&5;Mode&Strike;Tags&T3up

## ql_event_anniversary_2023_t1

### qe_anniversary_2023_day01_A_t1: Day 1: Research Directive
We received priority communication from Lazarus Base concerning Gideon S'jet. The transmission is encrypted with a specific vibration that can only be found on Hiigaran fabricators. We need to construct any item to match the encryption.

<color=#FBB03F>Small items such as strike craft, modules and parts can be built in the fabricator. Larger items such as escort ships and flagships must be constructed at shipyards provided at larger stations.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t1
	* Goals:	Craft,0
	* GoalParameters:	Category&Crafting;Tags&T1up;Amount&1

### qe_anniversary_2023_day01_B_t1: The list given to us by Gideon includes many components found only in Progenitor ships. The easiest way to collect them is to harvest them from downed Progenitor units.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
The list given to us by Gideon includes many components found only in Progenitor ships. The easiest way to collect them is to harvest them from downed Progenitor units.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t1
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedProgenitorT1_ShipsDestroyedProgenitorT2_ShipsDestroyedProgenitorT3_ShipsDestroyedProgenitorT4;Amount&7

### qe_anniversary_2023_day01_C_t1: Progenitor Cognition Nodes are a fragile component often found floating in free space near ancient wreckages.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
Progenitor Cognition Nodes are a fragile component often found floating in free space near ancient wreckages.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t1
	* Goals:	GainItem,0
	* GoalParameters:	Tags&ProgenitorRelic_T1up;Amount&1;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_anniversary_2023_day02_A_t1: Day 2: Cash Money
Ekekko can bring us in contact with traders specialized in Progenitor technology. But knowing the Iyatequa, everything has a price. We should mine minerals to recuperate the losses we'll have to pay.

<color=#FBB03F>Ore can be mined from asteroids in asteroid fields. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t1
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Asteroid_Crud_T1up;Amount&800;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_anniversary_2023_day02_B_t1: To impress the Iyatequa traders and procure the Progenitor components for Gideon, we will have to work on our reputation among a certain clientele.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
To impress the Iyatequa traders and buy the Progenitor components for Gideon, we will have to work on our reputation.

<color=#FBB03F>You can earn insignias by completing missions.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t1
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Insignia_T1up;Amount&25;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_anniversary_2023_day02_C_t1: In order to raise funds to acquire the needed Progenitor components for Gideon, we must sell some of our stored items on the local market.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
In order to raise funds to acquire the needed Progenitor components for Gideon, we must sell some of our stored items on the local market.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t1
	* Goals:	GainItem,0
	* GoalParameters:	Id&CR;Amount&1250;ExcludedSources&BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

### qe_anniversary_2023_day03_A_t1: Day 3: Stop Scouting
We need to search for recent communications data in this sector to pick up a lead on Guahai's Yaot fleet. We should find what we are looking for on recently destroyed ships.

<color=#FBB03F>The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t1
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedT1_ShipsDestroyedT2_ShipsDestroyedT3_ShipsDestroyedT4;Amount&15

### qe_anniversary_2023_day03_B_t1: We are in search of the missing data disk Guahai mentioned in his transmission. We might be able to find it in salvage crates from local outlaws.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
We are in search of the missing data disk Guahai mentioned in his transmission. We might be able to find it in salvage crates from local outlaws.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t1
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Salvage_T1up;Amount&3;ExcludedSources&MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_OpenContainer

### qe_anniversary_2023_day03_C_t1: The reconnaissance disk gave us a lead on the Progenitor component the Yaot call the Stambha. Enemy activity is high in the target location.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
The data disk gave us a lead on the Progenitor component the Yaot call the Stambah. It seems to be located inside a sector with strong enemy activity.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t1
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&1;Tags&Rare_T1up;Mode&Generated

### qe_anniversary_2023_day04_A_t1: Day 4: Lost and Found
Gideon has emerged from his laboratory. He talks of the possibility to build a device that could change the fortunes of Hiigarans in Nimbus. However, we must search for a final component.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t1
	* Goals:	Scan,0
	* GoalParameters:	Tags&InSystem_T1up;Amount&5;Analyzed&True

### qe_anniversary_2023_day04_B_t1: Gideon is in need of raw materials to construct a secret device. We should look for a jovian planet to collect some gas.

<color=#FBB03F>Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.</color>
Gideon is in need of raw materials to construct his secret device. We have to mine some minerals for him.

<color=#FBB03F>Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t1
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Asteroid_Crud_T1up;Amount&800;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_anniversary_2023_day04_C_t1: According to Ekekko, the last component on Gideon's list might be in the hands of a powerful enemy. The search for additional information is sending us into the most dangerous areas of this sector.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
According to Ekekko, the last component on Gideon's list might be in the hands of a powerful enemy. The search for additional information is sending us into the most dangerous areas of this sector.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t1
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&1;Tags&Rare_T1up;Mode&Generated

### qe_anniversary_2023_day05_A_t1: Day 5: Help Wanted
We want to make contact with Tepin Papan, commander of the Tanoch Empire. To open up a communication channel, we should do some hired work for the local authorities.

<color=#FBB03F>There are different types of assignments available in your assignment log.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t1
	* Goals:	CompleteQuest,0
	* GoalParameters:	Amount&5;Tags&T1up

### qe_anniversary_2023_day05_B_t1: Tepin Papan has offered to provide information on Gideon's last component if we help him with a security issue he currently faces.

<color=#FBB03F>Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.</color>
Tepin Papan has offered to provide information on Gideon's last component if we help him with a security issue he currently faces.

<color=#FBB03F>The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t1
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedT1_ShipsDestroyedT2_ShipsDestroyedT3_ShipsDestroyedT4;Amount&15

### qe_anniversary_2023_day05_C_t1: According to Tepin Papan, some of the Tanoch sectors require assistance. We should seek out their liaison offices and complete assignments.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
Tepin Papan wants us to retrieve some stolen goods. We should begin salvaging crates in the areas indicated by Tanoch data.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t1
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Salvage_T1up;Amount&3;ExcludedSources&MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_OpenContainer

### qe_anniversary_2023_day06_A_t1: Day 6: Training Day
While Lazarus Base is processing the reports on the stolen Progenitor component, Gideon wants us to train a crew to handle the device he's constructing.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t1
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Insignia_T1up;Amount&25;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_anniversary_2023_day06_B_t1: With Gideon's new program, we should start training the crew that will man his enigmatic device.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
With Gideon's new program, we should start training the crew that will man his enigmatic device.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t1
	* Goals:	UpgradeOfficer,0
	* GoalParameters:	Amount&1

### qe_anniversary_2023_day06_C_t1: It is time to put our newly trained crew to the test. We received a task from Lazarus Base to engage a hostile fleet nearby.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
It is time to put our newly trained crew to the test. We received a task from Lazarus Base to engage a hostile fleet nearby.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t1
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&1;Tags&Rare_T1up;Mode&Generated

### qe_anniversary_2023_day07_A_t1: Day 7: Simple Collection
Guhai is a high ranking Yaot official and Lazarus Base has advised us to follow his instructions for now. His first transmitted task needs us to mine resources.

<color=#FBB03F>Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t1
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Asteroid_Crud_T1up;Amount&800;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_anniversary_2023_day07_B_t1: We continue to follow Guahai’s orders. His next task for us is to produce refined material.

<color=#FBB03F>Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.</color>
We continue to follow Guahai’s orders. His next task for us is to produce refined material.

<color=#FBB03F>Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t1
	* Goals:	Craft,0
	* GoalParameters:	Category&Refining;Tags&Asteroid_Refined_T1up;Amount&500

### qe_anniversary_2023_day07_C_t1: Guahai requires us to build specific items for his fleet, as repayment for stealing their cultural item.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
Guahai requires us to build specific items for his fleet, as repayment for stealing their cultural item.

<color=#FBB03F>Small items such as strike craft, modules and parts can be built in the fabricator. Larger items such as escort ships and flagships must be constructed at shipyards provided at larger stations.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t1
	* Goals:	Craft,0
	* GoalParameters:	Category&Crafting;Tags&T1up;Amount&1

### qe_anniversary_2023_day08_A_t1: Day 8: Cangacian Patrol
Lazarus Base has informed us that the Tanoch reports on the stolen Progenitor component point towards an infamous pirate group called The Fleet of Rams. We should hunt down Cangacian vessels for more information.

<color=#FBB03F>The Cangacians are pirates that harass trade routes and colonies. We may find them in signals in most areas of the galaxy. They have been sighted raiding mining fleets in asteroid clusters as well.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t1
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedP1T1_ShipsDestroyedP1T2_ShipsDestroyedP1T3_ShipsDestroyedP1T4;Amount&10

### qe_anniversary_2023_day08_B_t1: The last item Gideon needs to build his device is in the possession of Catequil, Lieutenant of the Fleet of Rams. We have to find communications data from hostile ships to locate his position.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
The last item Gideon needs to build his device is in the possession of Catequil, Lieutenant of the Fleet of Rams. We have to find communications data from hostile ships to locate his position.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t1
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Salvage_T1up;Amount&3;ExcludedSources&MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_OpenContainer

### qe_anniversary_2023_day08_C_t1: Our engineers were able to triangulate Catequil's transmission. We must chase him down to attain the last Progenitor component for Gideon.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
Our engineers were able to triangulate Catequil's transmission. We must chase him down to attain the last Progenitor component for Gideon.

<color=#FBB03F>The Cangacians are pirates that harass trade routes and colonies. We may find them in signals in most areas of the galaxy. They have been sighted raiding mining fleets in asteroid clusters as well.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t1
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedP1T1_ShipsDestroyedP1T2_ShipsDestroyedP1T3_ShipsDestroyedP1T4;Amount&20

### qe_anniversary_2023_day09_A_t1: Day 9: Special Instructions
While Gideon is finalizing the construction of the Progenitor Negotiator, one of our officers must be trained to utilize it in action.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t1
	* Goals:	UpgradeOfficer,0
	* GoalParameters:	Amount&1

### qe_anniversary_2023_day09_B_t1: Before we embark on Gideon's special operation, we should further increase our fleet's power to ensure we are ready for any eventuality.

<color=#FBB03F>Internal Modules can be upgraded in the Internal Module screen which increases their attributes. Upgrading one level costs credits and RE.</color>
We have to fabricate several items to modify a common freighter for Gideon's special operation.

<color=#FBB03F>Small items such as strike craft, modules and parts can be built in the fabricator. Larger items such as escort ships and flagships must be constructed at shipyards provided at larger stations.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t1
	* Goals:	Craft,0
	* GoalParameters:	Category&Crafting;Tags&T1up;Amount&1

### qe_anniversary_2023_day09_C_t1: We are instructed to perform one final operations readiness test. All forces must be fully prepared for whatever Gideon is planning.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
We are instructed to perform one final operations readiness test. All forces must be fully prepared for whatever Gideon is planning.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t1
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&1;Tags&Rare_T1up;Mode&Generated

### qe_anniversary_2023_day10_A_t1: Day 10: The Special Operation
Gideon has finally revealed his plan. From the Progenitor components we collected he constructed a communication device to retake control of Wiracoda Gate. We are trying to go home.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t1
	* MailsOnCompletion:	m_anniversary_enoch_log
	* Goals:	CompleteMission,0
	* GoalParameters:	Id&event_anniversary2023_Wiracoda_t1

## ql_event_anniversary_2023_t2

### qe_anniversary_2023_day01_A_t2: We received priority communication from Hiigaran Command of Lazarus Base concerning Gideon S'jet. We need to decrypt it in our laboratory first before we can read it.

<color=#FBB03F>Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.</color>
We received priority communication from Hiigaran Command of Lazarus Base concerning Gideon S'jet. We need to decrypt it in our laboratory first before we can read it.

<color=#FBB03F>Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t2
	* Goals:	GainItem,0
	* GoalParameters:	Id&RP;Amount&200;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_anniversary_2023_day01_B_t2: The list given to us by Gideon includes many components found only in Progenitor ships. The easiest way to collect them is to harvest them from downed Progenitor units.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
The list given to us by Gideon includes many components found only in Progenitor ships. The easiest way to collect them is to harvest them from downed Progenitor units.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t2
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedProgenitorT2_ShipsDestroyedProgenitorT3_ShipsDestroyedProgenitorT4;Amount&7

### qe_anniversary_2023_day01_C_t2: Progenitor Cognition Nodes are a fragile component often found floating in free space near ancient wreckages.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
Progenitor Cognition Nodes are a fragile component often found floating in free space near ancient wreckages.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t2
	* Goals:	GainItem,0
	* GoalParameters:	Tags&ProgenitorRelic_T2up;Amount&1;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_anniversary_2023_day02_A_t2: Ekekko can bring us in contact with traders specialized in Progenitor technology. But knowing the Iyatequa, everything has a price. We should mine minerals to recuperate the losses we'll have to pay.

<color=#FBB03F>Type D ore is not abundant enough to form asteroid clusters on its own. Instead, asteroids with D type ore can be found within clusters rich with other types of ore.</color>
Ekekko can bring us in contact with traders specialized in Progenitor technology. But knowing the Iyatequa, everything has a price. We should mine minerals to recuperate the losses we'll have to pay.

<color=#FBB03F>Type D ore is not abundant enough to form asteroid clusters on its own. Instead, asteroids with D type ore can be found within clusters rich with other types of ore.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t2
	* Goals:	GainItem,0
	* GoalParameters:	Tags&AsteroidD_Crud_T2up;Amount&400;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_anniversary_2023_day02_B_t2: To impress the Iyatequa traders and procure the Progenitor components for Gideon, we will have to work on our reputation among a certain clientele.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
To impress the Iyatequa traders and procure the Progenitor components for Gideon, we will have to work on our reputation among a certain clientele.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t2
	* Goals:	Statistic,0
	* GoalParameters:	Ids&RepTr1;Amount&135

### qe_anniversary_2023_day02_C_t2: In order to raise funds to acquire the needed Progenitor components for Gideon, we must sell some of our stored items on the local market.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
In order to raise funds to acquire the needed Progenitor components for Gideon, we must sell some of our stored items on the local market.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t2
	* Goals:	GainItem,0
	* GoalParameters:	Id&CR;Amount&2500;ExcludedSources&BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

### qe_anniversary_2023_day03_A_t2: We need to search for recent communications data in this sector to pick up a lead on Guahai's Yaot fleet. We should find what we are looking for on recently destroyed ships.

<color=#FBB03F>The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.</color>
We need to search for recent communications data in this sector to pick up a lead on Guahai's Yaot fleet. We should find what we are looking for on recently destroyed ships.

<color=#FBB03F>The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t2
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedT2_ShipsDestroyedT3_ShipsDestroyedT4;Amount&15

### qe_anniversary_2023_day03_B_t2: We are in search of the missing data disk Guahai mentioned in his transmission. We might be able to find it in salvage crates from local outlaws.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
We are in search of the missing data disk Guahai mentioned in his transmission. We might be able to find it in salvage crates from local outlaws.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t2
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Salvage_T2up;Amount&3;ExcludedSources&MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_OpenContainer

### qe_anniversary_2023_day03_C_t2: The reconnaissance disk gave us a lead on the Progenitor component the Yaot call the Stambha. Enemy activity is high in the target location.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
The reconnaissance disk gave us a lead on the Progenitor component the Yaot call the Stambha. Enemy activity is high in the target location.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t2
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&1;Mode&Strike;Tags&T1up

### qe_anniversary_2023_day04_A_t2: Gideon has emerged from his laboratory. He talks of the possibility to build a device that could change the fortunes of Hiigarans in Nimbus. However, we must search for a final component.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
Gideon has emerged from his laboratory. He talks of the possibility to build a device that could change the fortunes of Hiigarans in Nimbus. However, we must search for a final component.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t2
	* Goals:	Scan,0
	* GoalParameters:	Tags&InSystem_T2up;Amount&5;Analyzed&True

### qe_anniversary_2023_day04_B_t2: Gideon is in need of raw materials to construct a secret device. We should look for a jovian planet to collect some gas.

<color=#FBB03F>Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.</color>
Gideon is in need of raw materials to construct his secret device. We have to mine some minerals for him.

<color=#FBB03F>Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t2
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Asteroid_Crud_T2up;Amount&1000;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_anniversary_2023_day04_C_t2: According to Ekekko, the last component on Gideon's list might be in the hands of a powerful enemy. The search for additional information is sending us into the most dangerous areas of this sector.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
According to Ekekko, the last component on Gideon's list might be in the hands of a powerful enemy. The search for additional information is sending us into the most dangerous areas of this sector.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t2
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&1;Tags&Epic_T2up;Mode&Generated

### qe_anniversary_2023_day05_A_t2: We want to make contact with Tepin Papan, commander of the Tanoch Empire. To find a communication channel, we should do some hired work for the local authorities.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
We want to make contact with Tepin Papan, commander of the Tanoch Empire. To find a communication channel, we should do some hired work for the local authorities.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t2
	* Goals:	CompleteQuest,0
	* GoalParameters:	Amount&5;Tags&Faction_T2up

### qe_anniversary_2023_day05_B_t2: Tepin Papan has offered to provide information on Gideon's last component if we help him with a security issue he currently faces.

<color=#FBB03F>Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.</color>
Tepin Papan has offered to provide information on Gideon's last component if we help him with a security issue he currently faces.

<color=#FBB03F>Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t2
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&3;Mode&Faction;Tags&T2up_Tanoch

### qe_anniversary_2023_day05_C_t2: According to Tepin Papan, some of the Tanoch sectors require assistance. We should seek out their liaison offices and complete assignments.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
According to Tepin Papan, some of the Tanoch sectors require assistance. We should seek out their liaison offices and complete assignments.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t2
	* Goals:	Statistic,0
	* GoalParameters:	Id&RepTanoch;Amount&135

### qe_anniversary_2023_day06_A_t2: While Lazarus Base is processing the reports on the stolen Progenitor component, Gideon wants us to train a crew to handle the device he's constructing.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.</color>
While Lazarus Base is processing the reports on the stolen Progenitor component, Gideon wants us to train a crew to handle the device he's constructing.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t2
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Insignia_T2up;Amount&25;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_anniversary_2023_day06_B_t2: With Gideon's new program, we should start training the crew that will man his enigmatic device.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
With Gideon's new program, we should start training the crew that will man his enigmatic device.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t2
	* Goals:	UpgradeOfficer,0
	* GoalParameters:	Amount&2

### qe_anniversary_2023_day06_C_t2: It is time to put our newly trained crew to the test. We received a task from Lazarus Base to engage a hostile fleet nearby.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
It is time to put our newly trained crew to the test. We received a task from Lazarus Base to engage a hostile fleet nearby.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t2
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&1;Mode&Strike;Tags&T1up

### qe_anniversary_2023_day07_A_t2: Guhai is a high ranking Yaot official and Lazarus Base has advised us to follow his instructions for now. His first transmitted task needs us to mine resources.

<color=#FBB03F>Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
Guhai is a high ranking Yaot official and Lazarus Base has advised us to follow his instructions for now. His first transmitted task needs us to mine resources.

<color=#FBB03F>Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t2
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Asteroid_Crud_T2up;Amount&1000;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_anniversary_2023_day07_B_t2: We continue to follow Guahai’s orders. His next task for us is to produce refined material.

<color=#FBB03F>Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.</color>
We continue to follow Guahai’s orders. His next task for us is to produce refined material.

<color=#FBB03F>Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t2
	* Goals:	Craft,0
	* GoalParameters:	Category&Refining;Tags&Asteroid_Refined_T2up;Amount&500

### qe_anniversary_2023_day07_C_t2: Guahai requires us to build specific items for his fleet, as repayment for stealing their cultural item.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
Guahai requires us to build specific items for his fleet, as repayment for stealing their cultural item.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t2
	* Goals:	Craft,0
	* GoalParameters:	Category&Crafting;Tags&Part_T2up;Amount&50

### qe_anniversary_2023_day08_A_t2: Lazarus Base has informed us that the Tanoch reports on the stolen Progenitor component point towards an infamous pirate group called The Fleet of Rams. We should hunt down Cangacian vessels for more information.

<color=#FBB03F>The Cangacians are pirates that harass trade routes and colonies. We may find them in signals in most areas of the galaxy. They have been sighted raiding mining fleets in asteroid clusters as well.</color>
Lazarus Base has informed us that the Tanoch reports on the stolen Progenitor component point towards an infamous pirate group called The Fleet of Rams. We should hunt down Cangacian vessels for more information.

<color=#FBB03F>The Cangacians are pirates that harass trade routes and colonies. We may find them in signals in most areas of the galaxy. They have been sighted raiding mining fleets in asteroid clusters as well.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t2
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedP1T2_ShipsDestroyedP1T3_ShipsDestroyedP1T4;Amount&10

### qe_anniversary_2023_day08_B_t2: The last item Gideon needs to build his device is in the possession of Catequil, Lieutenant of the Fleet of Rams. We have to find communications data from hostile ships to locate his position.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
The last item Gideon needs to build his device is in the possession of Catequil, Lieutenant of the Fleet of Rams. We have to find communications data from hostile ships to locate his position.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t2
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Salvage_T2up;Amount&3;ExcludedSources&MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_OpenContainer

### qe_anniversary_2023_day08_C_t2: Our engineers were able to triangulate Catequil's transmission. We must chase him down to attain the last Progenitor component for Gideon.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
Our engineers were able to triangulate Catequil's transmission. We must chase him down to attain the last Progenitor component for Gideon.

<color=#FBB03F>The Cangacians are pirates that harass trade routes and colonies. We may find them in signals in most areas of the galaxy. They have been sighted raiding mining fleets in asteroid clusters as well.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t2
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedP1T2_ShipsDestroyedP1T3_ShipsDestroyedP1T4;Amount&20

### qe_anniversary_2023_day09_A_t2: While Gideon is finalizing the construction of the Progenitor Negotiator, we should increase our fleet's power to protect it in action.

<color=#FBB03F>External modules, such as turrets or sensors, can be upgraded in the External Module screen which will increase their power. Upgrading one level costs credits and RE.</color>
While Gideon is finalizing the construction of the Progenitor Negotiator, we should increase our fleet's power to protect it in action.

<color=#FBB03F>External modules, such as turrets or sensors, can be upgraded in the External Module screen which will increase their power. Upgrading one level costs credits and RE.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t2
	* Goals:	Craft,0
	* GoalParameters:	Category&Upgrade;Tags&External_Module_T1up;Amount&1

### qe_anniversary_2023_day09_B_t2: Before we embark on Gideon's special operation, we should further increase our fleet's power to ensure we are ready for any eventuality.

<color=#FBB03F>Internal Modules can be upgraded in the Internal Module screen which increases their attributes. Upgrading one level costs credits and RE.</color>
We have to fabricate several items to modify a common freighter for Gideon's special operation.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t2
	* Goals:	Craft,0
	* GoalParameters:	Category&Crafting;Tags&Part_T2up;Amount&50

### qe_anniversary_2023_day09_C_t2: We are instructed to perform one final operations readiness test. All forces must be fully prepared for whatever Gideon is planning.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
We are instructed to perform one final operations readiness test. All forces must be fully prepared for whatever Gideon is planning.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t2
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&1;Mode&Strike;Tags&T1up

### qe_anniversary_2023_day10_A_t2: Gideon has finally revealed his plan. From the Progenitor components we collected he constructed a communication device to retake control of Wiracoda Gate. We are trying to go home.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
Gideon has finally revealed his plan. From the Progenitor components we collected he constructed a communication device to retake control of Wiracoda Gate. We are trying to go home.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t2
	* MailsOnCompletion:	m_anniversary_enoch_log
	* Goals:	CompleteMission,0
	* GoalParameters:	Id&event_anniversary2023_Wiracoda_t2

## ql_event_anniversary_2023_t3

### qe_anniversary_2023_day01_A_t3: We received priority communication from Hiigaran Command of Lazarus Base concerning Gideon S'jet. We need to decrypt it in our laboratory first before we can read it.

<color=#FBB03F>Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.</color>
We received priority communication from Hiigaran Command of Lazarus Base concerning Gideon S'jet. We need to decrypt it in our laboratory first before we can read it.

<color=#FBB03F>Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t3
	* Goals:	GainItem,0
	* GoalParameters:	Id&RP;Amount&200;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_anniversary_2023_day01_B_t3: The list given to us by Gideon includes many components found only in Progenitor ships. The easiest way to collect them is to harvest them from downed Progenitor units.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
The list given to us by Gideon includes many components found only in Progenitor ships. The easiest way to collect them is to harvest them from downed Progenitor units.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t3
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedProgenitorT3_ShipsDestroyedProgenitorT4;Amount&7

### qe_anniversary_2023_day01_C_t3: Progenitor Cognition Nodes are a fragile component often found floating in free space near ancient wreckages.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
Progenitor Cognition Nodes are a fragile component often found floating in free space near ancient wreckages.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t3
	* Goals:	GainItem,0
	* GoalParameters:	Tags&ProgenitorRelic_T3up;Amount&1;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_anniversary_2023_day02_A_t3: Ekekko can bring us in contact with traders specialized in Progenitor technology. But knowing the Iyatequa, everything has a price. We should mine minerals to recuperate the losses we'll have to pay.

<color=#FBB03F>Type D ore is not abundant enough to form asteroid clusters on its own. Instead, asteroids with D type ore can be found within clusters rich with other types of ore.</color>
Ekekko can bring us in contact with traders specialized in Progenitor technology. But knowing the Iyatequa, everything has a price. We should mine minerals to recuperate the losses we'll have to pay.

<color=#FBB03F>Type D ore is not abundant enough to form asteroid clusters on its own. Instead, asteroids with D type ore can be found within clusters rich with other types of ore.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t3
	* Goals:	GainItem,0
	* GoalParameters:	Tags&AsteroidD_Crud_T3up;Amount&500;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_anniversary_2023_day02_B_t3: To impress the Iyatequa traders and procure the Progenitor components for Gideon, we will have to work on our reputation among a certain clientele.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
To impress the Iyatequa traders and procure the Progenitor components for Gideon, we will have to work on our reputation among a certain clientele.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t3
	* Goals:	Statistic,0
	* GoalParameters:	Ids&RepTr1;Amount&180

### qe_anniversary_2023_day02_C_t3: In order to raise funds to acquire the needed Progenitor components for Gideon, we must sell some of our stored items on the local market.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
In order to raise funds to acquire the needed Progenitor components for Gideon, we must sell some of our stored items on the local market.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t3
	* Goals:	GainItem,0
	* GoalParameters:	Id&CR;Amount&5000;ExcludedSources&BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

### qe_anniversary_2023_day03_A_t3: We need to search for recent communications data in this sector to pick up a lead on Guahai's Yaot fleet. We should find what we are looking for on recently destroyed ships.

<color=#FBB03F>The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.</color>
We need to search for recent communications data in this sector to pick up a lead on Guahai's Yaot fleet. We should find what we are looking for on recently destroyed ships.

<color=#FBB03F>The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t3
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedT3_ShipsDestroyedT4;Amount&15

### qe_anniversary_2023_day03_B_t3: We are in search of the missing data disk Guahai mentioned in his transmission. We might be able to find it in salvage crates from local outlaws.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
We are in search of the missing data disk Guahai mentioned in his transmission. We might be able to find it in salvage crates from local outlaws.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t3
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Salvage_T3up;Amount&3;ExcludedSources&MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_OpenContainer

### qe_anniversary_2023_day03_C_t3: The reconnaissance disk gave us a lead on the Progenitor component the Yaot call the Stambha. Enemy activity is high in the target location.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
The reconnaissance disk gave us a lead on the Progenitor component the Yaot call the Stambha. Enemy activity is high in the target location.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t3
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&1;Mode&Strike;Tags&T2up

### qe_anniversary_2023_day04_A_t3: Gideon has emerged from his laboratory. He talks of the possibility to build a device that could change the fortunes of Hiigarans in Nimbus. However, we must search for a final component.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
Gideon has emerged from his laboratory. He talks of the possibility to build a device that could change the fortunes of Hiigarans in Nimbus. However, we must search for a final component.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t3
	* Goals:	Scan,0
	* GoalParameters:	Tags&InSystem_T3up;Amount&5;Analyzed&True

### qe_anniversary_2023_day04_B_t3: Gideon is in need of raw materials to construct a secret device. We should look for a jovian planet to collect some gas.

<color=#FBB03F>Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.</color>
Gideon is in need of raw materials to construct a secret device. We should look for a jovian planet to collect some gas.

<color=#FBB03F>Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t3
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Gas_T3up;Amount&800;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_anniversary_2023_day04_C_t3: According to Ekekko, the last component on Gideon's list might be in the hands of a powerful enemy. The search for additional information is sending us into the most dangerous areas of this sector.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
According to Ekekko, the last component on Gideon's list might be in the hands of a powerful enemy. The search for additional information is sending us into the most dangerous areas of this sector.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t3
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&1;Tags&Epic_T3up;Mode&Generated

### qe_anniversary_2023_day05_A_t3: We want to make contact with Tepin Papan, commander of the Tanoch Empire. To find a communication channel, we should do some hired work for the local authorities.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
We want to make contact with Tepin Papan, commander of the Tanoch Empire. To find a communication channel, we should do some hired work for the local authorities.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t3
	* Goals:	CompleteQuest,0
	* GoalParameters:	Amount&5;Tags&Faction_T3up

### qe_anniversary_2023_day05_B_t3: Tepin Papan has offered to provide information on Gideon's last component if we help him with a security issue he currently faces.

<color=#FBB03F>Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.</color>
Tepin Papan has offered to provide information on Gideon's last component if we help him with a security issue he currently faces.

<color=#FBB03F>Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t3
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&3;Mode&Faction;Tags&T3up_Tanoch

### qe_anniversary_2023_day05_C_t3: According to Tepin Papan, some of the Tanoch sectors require assistance. We should seek out their liaison offices and complete assignments.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
According to Tepin Papan, some of the Tanoch sectors require assistance. We should seek out their liaison offices and complete assignments.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t3
	* Goals:	Statistic,0
	* GoalParameters:	Id&RepTanoch;Amount&180

### qe_anniversary_2023_day06_A_t3: While Lazarus Base is processing the reports on the stolen Progenitor component, Gideon wants us to train a crew to handle the device he's constructing.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.</color>
While Lazarus Base is processing the reports on the stolen Progenitor component, Gideon wants us to train a crew to handle the device he's constructing.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t3
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Insignia_T3up;Amount&25;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_anniversary_2023_day06_B_t3: With Gideon's new program, we should start training the crew that will man his enigmatic device.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
With Gideon's new program, we should start training the crew that will man his enigmatic device.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t3
	* Goals:	UpgradeOfficer,0
	* GoalParameters:	Amount&3

### qe_anniversary_2023_day06_C_t3: It is time to put our newly trained crew to the test. We received a task from Lazarus Base to engage a hostile fleet nearby.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
It is time to put our newly trained crew to the test. We received a task from Lazarus Base to engage a hostile fleet nearby.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t3
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&1;Mode&Strike;Tags&T2up

### qe_anniversary_2023_day07_A_t3: Guhai is a high ranking Yaot official and Lazarus Base has advised us to follow his instructions for now. His first transmitted task needs us to mine resources.

<color=#FBB03F>Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
Guhai is a high ranking Yaot official and Lazarus Base has advised us to follow his instructions for now. His first transmitted task needs us to mine resources.

<color=#FBB03F>Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t3
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Asteroid_Crud_T3up;Amount&1200;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_anniversary_2023_day07_B_t3: We continue to follow Guahai’s orders. His next task for us is to produce refined material.

<color=#FBB03F>Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.</color>
We continue to follow Guahai’s orders. His next task for us is to produce refined material.

<color=#FBB03F>Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t3
	* Goals:	Craft,0
	* GoalParameters:	Category&Refining;Tags&Asteroid_Refined_T3up;Amount&500

### qe_anniversary_2023_day07_C_t3: Guahai requires us to build specific items for his fleet, as repayment for stealing their cultural item.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
Guahai requires us to build specific items for his fleet, as repayment for stealing their cultural item.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t3
	* Goals:	Craft,0
	* GoalParameters:	Category&Crafting;Tags&Part_T3up;Amount&50

### qe_anniversary_2023_day08_A_t3: Lazarus Base has informed us that the Tanoch reports on the stolen Progenitor component point towards an infamous pirate group called The Fleet of Rams. We should hunt down Cangacian vessels for more information.

<color=#FBB03F>The Cangacians are pirates that harass trade routes and colonies. We may find them in signals in most areas of the galaxy. They have been sighted raiding mining fleets in asteroid clusters as well.</color>
Lazarus Base has informed us that the Tanoch reports on the stolen Progenitor component point towards an infamous pirate group called The Fleet of Rams. We should hunt down Cangacian vessels for more information.

<color=#FBB03F>The Cangacians are pirates that harass trade routes and colonies. We may find them in signals in most areas of the galaxy. They have been sighted raiding mining fleets in asteroid clusters as well.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t3
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedP1T3_ShipsDestroyedP1T4;Amount&10

### qe_anniversary_2023_day08_B_t3: The last item Gideon needs to build his device is in the possession of Catequil, Lieutenant of the Fleet of Rams. We have to find communications data from hostile ships to locate his position.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
The last item Gideon needs to build his device is in the possession of Catequil, Lieutenant of the Fleet of Rams. We have to find communications data from hostile ships to locate his position.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t3
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Salvage_T3up;Amount&3;ExcludedSources&MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_OpenContainer

### qe_anniversary_2023_day08_C_t3: Our engineers were able to triangulate Catequil's transmission. We must chase him down to attain the last Progenitor component for Gideon.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
Our engineers were able to triangulate Catequil's transmission. We must chase him down to attain the last Progenitor component for Gideon.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t3
	* Goals:	CompleteQuest,0
	* GoalParameters:	Id&qr_015

### qe_anniversary_2023_day09_A_t3: While Gideon is finalizing the construction of the Progenitor Negotiator, we should increase our fleet's power to protect it in action.

<color=#FBB03F>External modules, such as turrets or sensors, can be upgraded in the External Module screen which will increase their power. Upgrading one level costs credits and RE.</color>
While Gideon is finalizing the construction of the Progenitor Negotiator, we should increase our fleet's power to protect it in action.

<color=#FBB03F>External modules, such as turrets or sensors, can be upgraded in the External Module screen which will increase their power. Upgrading one level costs credits and RE.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t3
	* Goals:	Craft,0
	* GoalParameters:	Category&Upgrade;Tags&External_Module_T2up;Amount&1

### qe_anniversary_2023_day09_B_t3: Before we embark on Gideon's special operation, we should further increase our fleet's power to ensure we are ready for any eventuality.

<color=#FBB03F>Internal Modules can be upgraded in the Internal Module screen which increases their attributes. Upgrading one level costs credits and RE.</color>
Before we embark on Gideon's special operation, we should further increase our fleet's power to ensure we are ready for any eventuality.

<color=#FBB03F>Internal Modules can be upgraded in the Internal Module screen which increases their attributes. Upgrading one level costs credits and RE.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t3
	* Goals:	Craft,0
	* GoalParameters:	Category&Upgrade;Tags&Internal_Module_T2up;Amount&1

### qe_anniversary_2023_day09_C_t3: We are instructed to perform one final operations readiness test. All forces must be fully prepared for whatever Gideon is planning.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
We are instructed to perform one final operations readiness test. All forces must be fully prepared for whatever Gideon is planning.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t3
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&1;Mode&Strike;Tags&T2up

### qe_anniversary_2023_day10_A_t3: Gideon has finally revealed his plan. From the Progenitor components we collected he constructed a communication device to retake control of Wiracoda Gate. We are trying to go home.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
Gideon has finally revealed his plan. From the Progenitor components we collected he constructed a communication device to retake control of Wiracoda Gate. We are trying to go home.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t3
	* MailsOnCompletion:	m_anniversary_enoch_log
	* Goals:	CompleteMission,0
	* GoalParameters:	Id&event_anniversary2023_Wiracoda_t3

## ql_event_anniversary_2023_t4

### qe_anniversary_2023_day01_A_t4: We received priority communication from Hiigaran Command of Lazarus Base concerning Gideon S'jet. We need to decrypt it in our laboratory first before we can read it.

<color=#FBB03F>Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.</color>
We received priority communication from Hiigaran Command of Lazarus Base concerning Gideon S'jet. We need to decrypt it in our laboratory first before we can read it.

<color=#FBB03F>Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t4
	* Goals:	GainItem,0
	* GoalParameters:	Id&RP;Amount&200;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_anniversary_2023_day01_B_t4: The list given to us by Gideon includes many components found only in Progenitor ships. The easiest way to collect them is to harvest them from downed Progenitor units.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
The list given to us by Gideon includes many components found only in Progenitor ships. The easiest way to collect them is to harvest them from downed Progenitor units.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t4
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedProgenitorT4;Amount&7

### qe_anniversary_2023_day01_C_t4: Progenitor Cognition Nodes are a fragile component often found floating in free space near ancient wreckages.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
Progenitor Cognition Nodes are a fragile component often found floating in free space near ancient wreckages.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t4
	* Goals:	GainItem,0
	* GoalParameters:	Tags&ProgenitorRelic_T4up;Amount&1;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_anniversary_2023_day02_A_t4: Ekekko can bring us in contact with traders specialized in Progenitor technology. But knowing the Iyatequa, everything has a price. We should mine minerals to recuperate the losses we'll have to pay.

<color=#FBB03F>Type D ore is not abundant enough to form asteroid clusters on its own. Instead, asteroids with D type ore can be found within clusters rich with other types of ore.</color>
Ekekko can bring us in contact with traders specialized in Progenitor technology. But knowing the Iyatequa, everything has a price. We should mine minerals to recuperate the losses we'll have to pay.

<color=#FBB03F>Type D ore is not abundant enough to form asteroid clusters on its own. Instead, asteroids with D type ore can be found within clusters rich with other types of ore.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t4
	* Goals:	GainItem,0
	* GoalParameters:	Tags&AsteroidD_Crud_T4up;Amount&600;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_anniversary_2023_day02_B_t4: To impress the Iyatequa traders and procure the Progenitor components for Gideon, we will have to work on our reputation among a certain clientele.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
To impress the Iyatequa traders and procure the Progenitor components for Gideon, we will have to work on our reputation among a certain clientele.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t4
	* Goals:	Statistic,0
	* GoalParameters:	Ids&RepTr1;Amount&225

### qe_anniversary_2023_day02_C_t4: In order to raise funds to acquire the needed Progenitor components for Gideon, we must sell some of our stored items on the local market.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
In order to raise funds to acquire the needed Progenitor components for Gideon, we must sell some of our stored items on the local market.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t4
	* Goals:	GainItem,0
	* GoalParameters:	Id&CR;Amount&10000;ExcludedSources&BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

### qe_anniversary_2023_day03_A_t4: We need to search for recent communications data in this sector to pick up a lead on Guahai's Yaot fleet. We should find what we are looking for on recently destroyed ships.

<color=#FBB03F>The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.</color>
We need to search for recent communications data in this sector to pick up a lead on Guahai's Yaot fleet. We should find what we are looking for on recently destroyed ships.

<color=#FBB03F>The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t4
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedT4;Amount&15

### qe_anniversary_2023_day03_B_t4: We are in search of the missing data disk Guahai mentioned in his transmission. We might be able to find it in salvage crates from local outlaws.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
We are in search of the missing data disk Guahai mentioned in his transmission. We might be able to find it in salvage crates from local outlaws.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t4
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Salvage_T4up;Amount&3;ExcludedSources&MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_OpenContainer

### qe_anniversary_2023_day03_C_t4: The reconnaissance disk gave us a lead on the Progenitor component the Yaot call the Stambha. Enemy activity is high in the target location.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
The reconnaissance disk gave us a lead on the Progenitor component the Yaot call the Stambha. Enemy activity is high in the target location.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t4
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&1;Mode&Strike;Tags&T3up

### qe_anniversary_2023_day04_A_t4: Gideon has emerged from his laboratory. He talks of the possibility to build a device that could change the fortunes of Hiigarans in Nimbus. However, we must search for a final component.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
Gideon has emerged from his laboratory. He talks of the possibility to build a device that could change the fortunes of Hiigarans in Nimbus. However, we must search for a final component.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t4
	* Goals:	Scan,0
	* GoalParameters:	Tags&InSystem_T4up;Amount&5;Analyzed&True

### qe_anniversary_2023_day04_B_t4: Gideon is in need of raw materials to construct a secret device. We should look for a jovian planet to collect some gas.

<color=#FBB03F>Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.</color>
Gideon is in need of raw materials to construct a secret device. We should look for a jovian planet to collect some gas.

<color=#FBB03F>Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t4
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Gas_T4up;Amount&1000;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_anniversary_2023_day04_C_t4: According to Ekekko, the last component on Gideon's list might be in the hands of a powerful enemy. The search for additional information is sending us into the most dangerous areas of this sector.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
According to Ekekko, the last component on Gideon's list might be in the hands of a powerful enemy. The search for additional information is sending us into the most dangerous areas of this sector.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t4
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&1;Tags&Epic_T4up;Mode&Generated

### qe_anniversary_2023_day05_A_t4: We want to make contact with Tepin Papan, commander of the Tanoch Empire. To find a communication channel, we should do some hired work for the local authorities.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
We want to make contact with Tepin Papan, commander of the Tanoch Empire. To find a communication channel, we should do some hired work for the local authorities.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t4
	* Goals:	CompleteQuest,0
	* GoalParameters:	Amount&5;Tags&Faction_T4up

### qe_anniversary_2023_day05_B_t4: Tepin Papan has offered to provide information on Gideon's last component if we help him with a security issue he currently faces.

<color=#FBB03F>Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.</color>
Tepin Papan has offered to provide information on Gideon's last component if we help him with a security issue he currently faces.

<color=#FBB03F>Many liaison assignments require you to complete missions. Some even require you to complete multiple missions.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t4
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&3;Mode&Faction;Tags&T4up_Tanoch

### qe_anniversary_2023_day05_C_t4: According to Tepin Papan, some of the Tanoch sectors require assistance. We should seek out their liaison offices and complete assignments.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
According to Tepin Papan, some of the Tanoch sectors require assistance. We should seek out their liaison offices and complete assignments.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t4
	* Goals:	Statistic,0
	* GoalParameters:	Id&RepTanoch;Amount&225

### qe_anniversary_2023_day06_A_t4: While Lazarus Base is processing the reports on the stolen Progenitor component, Gideon wants us to train a crew to handle the device he's constructing.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.</color>
While Lazarus Base is processing the reports on the stolen Progenitor component, Gideon wants us to train a crew to handle the device he's constructing.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t4
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Insignia_T4up;Amount&25;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_anniversary_2023_day06_B_t4: With Gideon's new program, we should start training the crew that will man his enigmatic device.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
With Gideon's new program, we should start training the crew that will man his enigmatic device.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t4
	* Goals:	UpgradeOfficer,0
	* GoalParameters:	Amount&5

### qe_anniversary_2023_day06_C_t4: It is time to put our newly trained crew to the test. We received a task from Lazarus Base to engage a hostile fleet nearby.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
It is time to put our newly trained crew to the test. We received a task from Lazarus Base to engage a hostile fleet nearby.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t4
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&1;Mode&Strike;Tags&T3up

### qe_anniversary_2023_day07_A_t4: Guhai is a high ranking Yaot official and Lazarus Base has advised us to follow his instructions for now. His first transmitted task needs us to mine resources.

<color=#FBB03F>Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
Guhai is a high ranking Yaot official and Lazarus Base has advised us to follow his instructions for now. His first transmitted task needs us to mine resources.

<color=#FBB03F>Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t4
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Asteroid_Crud_T4up;Amount&1400;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_anniversary_2023_day07_B_t4: We continue to follow Guahai’s orders. His next task for us is to produce refined material.

<color=#FBB03F>Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.</color>
We continue to follow Guahai’s orders. His next task for us is to produce refined material.

<color=#FBB03F>Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t4
	* Goals:	Craft,0
	* GoalParameters:	Category&Refining;Tags&Asteroid_Refined_T4up;Amount&500

### qe_anniversary_2023_day07_C_t4: Guahai requires us to build specific items for his fleet, as repayment for stealing their cultural item.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
Guahai requires us to build specific items for his fleet, as repayment for stealing their cultural item.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t4
	* Goals:	Craft,0
	* GoalParameters:	Category&Crafting;Tags&Part_T4up;Amount&50

### qe_anniversary_2023_day08_A_t4: Lazarus Base has informed us that the Tanoch reports on the stolen Progenitor component point towards an infamous pirate group called The Fleet of Rams. We should hunt down Cangacian vessels for more information.

<color=#FBB03F>The Cangacians are pirates that harass trade routes and colonies. We may find them in signals in most areas of the galaxy. They have been sighted raiding mining fleets in asteroid clusters as well.</color>
Lazarus Base has informed us that the Tanoch reports on the stolen Progenitor component point towards an infamous pirate group called The Fleet of Rams. We should hunt down Cangacian vessels for more information.

<color=#FBB03F>The Cangacians are pirates that harass trade routes and colonies. We may find them in signals in most areas of the galaxy. They have been sighted raiding mining fleets in asteroid clusters as well.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t4
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedP1T4;Amount&10

### qe_anniversary_2023_day08_B_t4: The last item Gideon needs to build his device is in the possession of Catequil, Lieutenant of the Fleet of Rams. We have to find communications data from hostile ships to locate his position.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
The last item Gideon needs to build his device is in the possession of Catequil, Lieutenant of the Fleet of Rams. We have to find communications data from hostile ships to locate his position.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t4
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Salvage_T4up;Amount&3;ExcludedSources&MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_OpenContainer

### qe_anniversary_2023_day08_C_t4: Our engineers were able to triangulate Catequil's transmission. We must chase him down to attain the last Progenitor component for Gideon.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
Our engineers were able to triangulate Catequil's transmission. We must chase him down to attain the last Progenitor component for Gideon.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t4
	* Goals:	CompleteQuest,0
	* GoalParameters:	Id&qr_018

### qe_anniversary_2023_day09_A_t4: While Gideon is finalizing the construction of the Progenitor Negotiator, we should increase our fleet's power to protect it in action.

<color=#FBB03F>External modules, such as turrets or sensors, can be upgraded in the External Module screen which will increase their power. Upgrading one level costs credits and RE.</color>
While Gideon is finalizing the construction of the Progenitor Negotiator, we should increase our fleet's power to protect it in action.

<color=#FBB03F>External modules, such as turrets or sensors, can be upgraded in the External Module screen which will increase their power. Upgrading one level costs credits and RE.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t4
	* Goals:	Craft,0
	* GoalParameters:	Category&Upgrade;Tags&External_Module_T3up;Amount&1

### qe_anniversary_2023_day09_B_t4: Before we embark on Gideon's special operation, we should further increase our fleet's power to ensure we are ready for any eventuality.

<color=#FBB03F>Internal Modules can be upgraded in the Internal Module screen which increases their attributes. Upgrading one level costs credits and RE.</color>
Before we embark on Gideon's special operation, we should further increase our fleet's power to ensure we are ready for any eventuality.

<color=#FBB03F>Internal Modules can be upgraded in the Internal Module screen which increases their attributes. Upgrading one level costs credits and RE.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t4
	* Goals:	Craft,0
	* GoalParameters:	Category&Upgrade;Tags&Internal_Module_T3up;Amount&1

### qe_anniversary_2023_day09_C_t4: We are instructed to perform one final operations readiness test. All forces must be fully prepared for whatever Gideon is planning.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
We are instructed to perform one final operations readiness test. All forces must be fully prepared for whatever Gideon is planning.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t4
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&1;Mode&Strike;Tags&T3up

### qe_anniversary_2023_day10_A_t4: Gideon has finally revealed his plan. From the Progenitor components we collected he constructed a communication device to retake control of Wiracoda Gate. We are trying to go home.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
Gideon has finally revealed his plan. From the Progenitor components we collected he constructed a communication device to retake control of Wiracoda Gate. We are trying to go home.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
	* Type:	Event
	* EventId:	event_anniversary_2023_t4
	* MailsOnCompletion:	m_anniversary_enoch_log
	* Goals:	CompleteMission,0
	* GoalParameters:	Id&event_anniversary2023_Wiracoda_t4

## ql_event_halloween_2023_t1

### qe_halloween_2023_day01_t1: Day 1: Sentinel Duty
We are receiving disturbing reports from all over the galaxy. The disaster at Wiracoda Gate has sent the Progenitors into a frenzy! We must assist the defensive efforts wherever we can until we understand what is happening.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
	* Type:	Event
	* EventId:	event_halloween_2023_t1
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedProgenitorT1_ShipsDestroyedProgenitorT2_ShipsDestroyedProgenitorT3_ShipsDestroyedProgenitorT4;Amount&10

### qe_halloween_2023_day02_t1: Day 2: Prospector
Refineries are being targeted by the Progenitors in many sectors of Nimbus. Stocks need to be replenished if the defenders are to hold off this calamity.

<color=#FBB03F>Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
	* Type:	Event
	* EventId:	event_halloween_2023_t1
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Asteroid_Crud_T1up;Amount&800;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_halloween_2023_day03_t1: Day 3: Deep Space Recovery
Gideon wants to collect any evidence which points to the Progenitor’s current activity. We should collect data from ships that were in combat with the abnormal Progenitor vessels.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
	* Type:	Event
	* EventId:	event_halloween_2023_t1
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Salvage_T1up;Amount&5;ExcludedSources&MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_OpenContainer

### qe_halloween_2023_day04_t1: Day 4: Smelt and Refine
Many planets are still in desperate need of resources to hold off the Progenitors. Especially rare resources have been in high demand to increase defensive capabilities.

<color=#FBB03F>Rare earths are an occasional by-product of refining. They are required for upgrading modules.</color>
	* Type:	Event
	* EventId:	event_halloween_2023_t1
	* Goals:	GainItem,0
	* GoalParameters:	Tags&RareEarth_T1up;Amount&20;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_halloween_2023_day05_t1: Day 5: The Guidepost
Gideon has identified a specific Progenitor component we must find in order to decrypt the errant Keeper's command frequency.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
	* Type:	Event
	* EventId:	event_halloween_2023_t1
	* Goals:	GainItem,0
	* GoalParameters:	Tags&ProgenitorRelic_T1up;Amount&1;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_halloween_2023_day06_t1: Day 6: Replacement Parts
Many sectors have suffered heavy damages from the ongoing Progenitor attacks. More parts are needed to replenish the defending fleets.

<color=#FBB03F>Small items such as strike craft, modules and parts can be built in the fabricator. Larger items such as escort ships and flagships must be constructed at shipyards provided at larger stations.</color>
	* Type:	Event
	* EventId:	event_halloween_2023_t1
	* Goals:	Craft,0
	* GoalParameters:	Category&Crafting;Tags&T1up;Amount&5

### qe_halloween_2023_day07_t1: Day 7: Triangulation
In order for Gideon to triangulate the location of the errant Keeper we need to hunt down Progenitor vessels receiving its command signal.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
	* Type:	Event
	* EventId:	event_halloween_2023_t1
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedProgenitorT1_ShipsDestroyedProgenitorT2_ShipsDestroyedProgenitorT3_ShipsDestroyedProgenitorT4;Amount&10

### qe_halloween_2023_day08_t1: Day 8: Officer Training
We are unsure what awaits us when we'll face the corrupted Keeper once again. Gideon has advised us to train our officers in Progenitor communication theory to effectively analyze the situation in the field.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
	* Type:	Event
	* EventId:	event_halloween_2023_t1
	* Goals:	UpgradeOfficer,0
	* GoalParameters:	Amount&1

### qe_halloween_2023_day09_t1: Day 9: Military Exercise
In order to be fully prepared for the confrontation with the corrupted Keeper, we need to perform a fleet wide ready-check for all systems. We can engage enemies that have been preying on the local area lately due to the diminished security situation.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
	* Type:	Event
	* EventId:	event_halloween_2023_t1
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&1;Tags&Rare_T1up;Mode&Generated

### qe_halloween_2023_day10_t1: Day 10: Safe Passage
The Iyatequa promised to negotiate a deal for safe passage into Cangacian space. However, even though the galaxy is at stake, the traders still insist on receiving a hefty price.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
	* Type:	Event
	* EventId:	event_halloween_2023_t1
	* Goals:	GainItem,0
	* GoalParameters:	Id&CR;Amount&1250;ExcludedSources&BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

### qe_halloween_2023_day11_t1: Day 11: Confrontation
We must confront the corrupted Keeper Malik and end the Progenitor incursion.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
	* Type:	Event
	* EventId:	event_halloween_2023_t1
	* Goals:	CompleteMission,0
	* GoalParameters:	Id&event_halloween2023_Rashidun_t1

## ql_event_halloween_2023_t2

### qe_halloween_2023_day01_t2: We are receiving disturbing reports from all over the galaxy. The disaster at Wiracoda Gate has sent the Progenitors into a frenzy! We must assist the defensive efforts wherever we can until we understand what is happening.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
We are receiving disturbing reports from all over the galaxy. The disaster at Wiracoda Gate has sent the Progenitors into a frenzy! We must assist the defensive efforts wherever we can until we understand what is happening.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
	* Type:	Event
	* EventId:	event_halloween_2023_t2
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedProgenitorT2_ShipsDestroyedProgenitorT3_ShipsDestroyedProgenitorT4;Amount&10

### qe_halloween_2023_day02_t2: Gas refineries are being targeted by the Progenitors in many sectors of Nimbus. Stocks need to be replenished if the defenders are to hold off this calamity.

<color=#FBB03F>Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.</color>
Refineries are being targeted by the Progenitors in many sectors of Nimbus. Stocks need to be replenished if the defenders are to hold off this calamity.

<color=#FBB03F>Ore can be mined from asteroids. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
	* Type:	Event
	* EventId:	event_halloween_2023_t2
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Asteroid_Crud_T2up;Amount&1000;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_halloween_2023_day03_t2: Gideon wants to collect any evidence which points to the Progenitor’s current activity. We should collect data from ships that were in combat with the abnormal Progenitor vessels.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
Gideon wants to collect any evidence which points to the Progenitor’s current activity. We should collect data from ships that were in combat with the abnormal Progenitor vessels.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
	* Type:	Event
	* EventId:	event_halloween_2023_t2
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Salvage_T2up;Amount&5;ExcludedSources&MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_OpenContainer

### qe_halloween_2023_day04_t2: Many planets are still in desperate need of resources to hold off the Progenitors. Especially rare resources have been in high demand to increase defensive capabilities.

<color=#FBB03F>Rare earths are an occasional by-product of refining. They are required for upgrading modules.</color>
Many planets are still in desperate need of resources to hold off the Progenitors. Especially rare resources have been in high demand to increase defensive capabilities.

<color=#FBB03F>Rare earths are an occasional by-product of refining. They are required for upgrading modules.</color>
	* Type:	Event
	* EventId:	event_halloween_2023_t2
	* Goals:	GainItem,0
	* GoalParameters:	Tags&RareEarth_T2up;Amount&20;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_halloween_2023_day05_t2: Gideon has identified a specific Progenitor component we must find in order to decrypt the errant Keeper's command frequency.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
Gideon has identified a specific Progenitor component we must find in order to decrypt the errant Keeper's command frequency.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
	* Type:	Event
	* EventId:	event_halloween_2023_t2
	* Goals:	GainItem,0
	* GoalParameters:	Tags&ProgenitorRelic_T2up;Amount&1;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_halloween_2023_day06_t2: Many sectors have suffered heavy damages from the ongoing Progenitor attacks. More parts are needed to replenish the defending fleets.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
Many sectors have suffered heavy damages from the ongoing Progenitor attacks. More parts are needed to replenish the defending fleets.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
	* Type:	Event
	* EventId:	event_halloween_2023_t2
	* Goals:	Craft,0
	* GoalParameters:	Category&Crafting;Tags&Part_T2up;Amount&100

### qe_halloween_2023_day07_t2: In order for Gideon to triangulate the location of the errant Keeper we need to hunt down Progenitor vessels receiving its command signal.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
In order for Gideon to triangulate the location of the errant Keeper we need to hunt down Progenitor vessels receiving its command signal.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
	* Type:	Event
	* EventId:	event_halloween_2023_t2
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedProgenitorT2_ShipsDestroyedProgenitorT3_ShipsDestroyedProgenitorT4;Amount&10

### qe_halloween_2023_day08_t2: We are unsure what awaits us when we'll face the corrupted Keeper once again. Gideon has advised us to train our officers in Progenitor communication theory to effectively analyze the situation in the field.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
We are unsure what awaits us when we'll face the corrupted Keeper once again. Gideon has advised us to train our officers in Progenitor communication theory to effectively analyze the situation in the field.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
	* Type:	Event
	* EventId:	event_halloween_2023_t2
	* Goals:	UpgradeOfficer,0
	* GoalParameters:	Amount&2

### qe_halloween_2023_day09_t2: In order to be fully prepared for the confrontation with the corrupted Keeper, we need to perform a fleet wide ready-check for all systems. We can engage enemies that have been preying on the local area lately due to the diminished security situation.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
In order to be fully prepared for the confrontation with the corrupted Keeper, we need to perform a fleet wide ready-check for all systems. We can engage enemies that have been preying on the local area lately due to the diminished security situation.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
	* Type:	Event
	* EventId:	event_halloween_2023_t2
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&1;Mode&Strike;Tags&T1up

### qe_halloween_2023_day10_t2: The Iyatequa promised to negotiate a deal for safe passage into Cangacian space. However, even though the galaxy is at stake, the traders still insist on receiving a hefty price.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
The Iyatequa promised to negotiate a deal for safe passage into Cangacian space. However, even though the galaxy is at stake, the traders still insist on receiving a hefty price.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
	* Type:	Event
	* EventId:	event_halloween_2023_t2
	* Goals:	GainItem,0
	* GoalParameters:	Id&CR;Amount&2500;ExcludedSources&BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

### qe_halloween_2023_day11_t2: We must confront the corrupted Keeper Malik and end the Progenitor incursion.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
We must confront the corrupted Keeper Malik and end the Progenitor incursion.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
	* Type:	Event
	* EventId:	event_halloween_2023_t2
	* Goals:	CompleteMission,0
	* GoalParameters:	Id&event_halloween2023_Rashidun_t2

## ql_event_halloween_2023_t3

### qe_halloween_2023_day01_t3: We are receiving disturbing reports from all over the galaxy. The disaster at Wiracoda Gate has sent the Progenitors into a frenzy! We must assist the defensive efforts wherever we can until we understand what is happening.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
We are receiving disturbing reports from all over the galaxy. The disaster at Wiracoda Gate has sent the Progenitors into a frenzy! We must assist the defensive efforts wherever we can until we understand what is happening.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
	* Type:	Event
	* EventId:	event_halloween_2023_t3
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedProgenitorT3_ShipsDestroyedProgenitorT4;Amount&10

### qe_halloween_2023_day02_t3: Gas refineries are being targeted by the Progenitors in many sectors of Nimbus. Stocks need to be replenished if the defenders are to hold off this calamity.

<color=#FBB03F>Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.</color>
Gas refineries are being targeted by the Progenitors in many sectors of Nimbus. Stocks need to be replenished if the defenders are to hold off this calamity.

<color=#FBB03F>Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.</color>
	* Type:	Event
	* EventId:	event_halloween_2023_t3
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Gas_T3up;Amount&1000;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_halloween_2023_day03_t3: Gideon wants to collect any evidence which points to the Progenitor’s current activity. We should collect data from ships that were in combat with the abnormal Progenitor vessels.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
Gideon wants to collect any evidence which points to the Progenitor’s current activity. We should collect data from ships that were in combat with the abnormal Progenitor vessels.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
	* Type:	Event
	* EventId:	event_halloween_2023_t3
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Salvage_T3up;Amount&5;ExcludedSources&MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_OpenContainer

### qe_halloween_2023_day04_t3: Many planets are still in desperate need of resources to hold off the Progenitors. Especially rare resources have been in high demand to increase defensive capabilities.

<color=#FBB03F>Rare earths are an occasional by-product of refining. They are required for upgrading modules.</color>
Many planets are still in desperate need of resources to hold off the Progenitors. Especially rare resources have been in high demand to increase defensive capabilities.

<color=#FBB03F>Rare earths are an occasional by-product of refining. They are required for upgrading modules.</color>
	* Type:	Event
	* EventId:	event_halloween_2023_t3
	* Goals:	GainItem,0
	* GoalParameters:	Tags&RareEarth_T3up;Amount&20;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_halloween_2023_day05_t3: Gideon has identified a specific Progenitor component we must find in order to decrypt the errant Keeper's command frequency.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
Gideon has identified a specific Progenitor component we must find in order to decrypt the errant Keeper's command frequency.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
	* Type:	Event
	* EventId:	event_halloween_2023_t3
	* Goals:	GainItem,0
	* GoalParameters:	Tags&ProgenitorRelic_T3up;Amount&1;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_halloween_2023_day06_t3: Many sectors have suffered heavy damages from the ongoing Progenitor attacks. More parts are needed to replenish the defending fleets.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
Many sectors have suffered heavy damages from the ongoing Progenitor attacks. More parts are needed to replenish the defending fleets.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
	* Type:	Event
	* EventId:	event_halloween_2023_t3
	* Goals:	Craft,0
	* GoalParameters:	Category&Crafting;Tags&Part_T3up;Amount&100

### qe_halloween_2023_day07_t3: In order for Gideon to triangulate the location of the errant Keeper we need to hunt down Progenitor vessels receiving its command signal.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
In order for Gideon to triangulate the location of the errant Keeper we need to hunt down Progenitor vessels receiving its command signal.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
	* Type:	Event
	* EventId:	event_halloween_2023_t3
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedProgenitorT3_ShipsDestroyedProgenitorT4;Amount&10

### qe_halloween_2023_day08_t3: We are unsure what awaits us when we'll face the corrupted Keeper once again. Gideon has advised us to train our officers in Progenitor communication theory to effectively analyze the situation in the field.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
We are unsure what awaits us when we'll face the corrupted Keeper once again. Gideon has advised us to train our officers in Progenitor communication theory to effectively analyze the situation in the field.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
	* Type:	Event
	* EventId:	event_halloween_2023_t3
	* Goals:	UpgradeOfficer,0
	* GoalParameters:	Amount&3

### qe_halloween_2023_day09_t3: In order to be fully prepared for the confrontation with the corrupted Keeper, we need to perform a fleet wide ready-check for all systems. We can engage enemies that have been preying on the local area lately due to the diminished security situation.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
In order to be fully prepared for the confrontation with the corrupted Keeper, we need to perform a fleet wide ready-check for all systems. We can engage enemies that have been preying on the local area lately due to the diminished security situation.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
	* Type:	Event
	* EventId:	event_halloween_2023_t3
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&3;Mode&Strike;Tags&T2up

### qe_halloween_2023_day10_t3: The Iyatequa promised to negotiate a deal for safe passage into Cangacian space. However, even though the galaxy is at stake, the traders still insist on receiving a hefty price.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
The Iyatequa promised to negotiate a deal for safe passage into Cangacian space. However, even though the galaxy is at stake, the traders still insist on receiving a hefty price.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
	* Type:	Event
	* EventId:	event_halloween_2023_t3
	* Goals:	GainItem,0
	* GoalParameters:	Id&CR;Amount&5000;ExcludedSources&BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

### qe_halloween_2023_day11_t3: We must confront the corrupted Keeper Malik and end the Progenitor incursion.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
We must confront the corrupted Keeper Malik and end the Progenitor incursion.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
	* Type:	Event
	* EventId:	event_halloween_2023_t3
	* Goals:	CompleteMission,0
	* GoalParameters:	Id&event_halloween2023_Rashidun_t3

## ql_event_halloween_2023_t4

### qe_halloween_2023_day01_t4: We are receiving disturbing reports from all over the galaxy. The disaster at Wiracoda Gate has sent the Progenitors into a frenzy! We must assist the defensive efforts wherever we can until we understand what is happening.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
We are receiving disturbing reports from all over the galaxy. The disaster at Wiracoda Gate has sent the Progenitors into a frenzy! We must assist the defensive efforts wherever we can until we understand what is happening.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
	* Type:	Event
	* EventId:	event_halloween_2023_t4
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedProgenitorT4;Amount&10

### qe_halloween_2023_day02_t4: Gas refineries are being targeted by the Progenitors in many sectors of Nimbus. Stocks need to be replenished if the defenders are to hold off this calamity.

<color=#FBB03F>Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.</color>
Gas refineries are being targeted by the Progenitors in many sectors of Nimbus. Stocks need to be replenished if the defenders are to hold off this calamity.

<color=#FBB03F>Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.</color>
	* Type:	Event
	* EventId:	event_halloween_2023_t4
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Gas_T4up;Amount&1200;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_halloween_2023_day03_t4: Gideon wants to collect any evidence which points to the Progenitor’s current activity. We should collect data from ships that were in combat with the abnormal Progenitor vessels.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
Gideon wants to collect any evidence which points to the Progenitor’s current activity. We should collect data from ships that were in combat with the abnormal Progenitor vessels.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
	* Type:	Event
	* EventId:	event_halloween_2023_t4
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Salvage_T4up;Amount&5;ExcludedSources&MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_OpenContainer

### qe_halloween_2023_day04_t4: Many planets are still in desperate need of resources to hold off the Progenitors. Especially rare resources have been in high demand to increase defensive capabilities.

<color=#FBB03F>Rare earths are an occasional by-product of refining. They are required for upgrading modules.</color>
Many planets are still in desperate need of resources to hold off the Progenitors. Especially rare resources have been in high demand to increase defensive capabilities.

<color=#FBB03F>Rare earths are an occasional by-product of refining. They are required for upgrading modules.</color>
	* Type:	Event
	* EventId:	event_halloween_2023_t4
	* Goals:	GainItem,0
	* GoalParameters:	Tags&RareEarth_T4up;Amount&20;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_halloween_2023_day05_t4: Gideon has identified a specific Progenitor component we must find in order to decrypt the errant Keeper's command frequency.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
Gideon has identified a specific Progenitor component we must find in order to decrypt the errant Keeper's command frequency.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
	* Type:	Event
	* EventId:	event_halloween_2023_t4
	* Goals:	GainItem,0
	* GoalParameters:	Tags&ProgenitorRelic_T4up;Amount&1;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_halloween_2023_day06_t4: Many sectors have suffered heavy damages from the ongoing Progenitor attacks. More parts are needed to replenish the defending fleets.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
Many sectors have suffered heavy damages from the ongoing Progenitor attacks. More parts are needed to replenish the defending fleets.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
	* Type:	Event
	* EventId:	event_halloween_2023_t4
	* Goals:	Craft,0
	* GoalParameters:	Category&Crafting;Tags&Part_T4up;Amount&100

### qe_halloween_2023_day07_t4: In order for Gideon to triangulate the location of the errant Keeper we need to hunt down Progenitor vessels receiving its command signal.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
In order for Gideon to triangulate the location of the errant Keeper we need to hunt down Progenitor vessels receiving its command signal.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
	* Type:	Event
	* EventId:	event_halloween_2023_t4
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedProgenitorT4;Amount&10

### qe_halloween_2023_day08_t4: We are unsure what awaits us when we'll face the corrupted Keeper once again. Gideon has advised us to train our officers in Progenitor communication theory to effectively analyze the situation in the field.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
We are unsure what awaits us when we'll face the corrupted Keeper once again. Gideon has advised us to train our officers in Progenitor communication theory to effectively analyze the situation in the field.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
	* Type:	Event
	* EventId:	event_halloween_2023_t4
	* Goals:	UpgradeOfficer,0
	* GoalParameters:	Amount&5

### qe_halloween_2023_day09_t4: In order to be fully prepared for the confrontation with the corrupted Keeper, we need to perform a fleet wide ready-check for all systems. We can engage enemies that have been preying on the local area lately due to the diminished security situation.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
In order to be fully prepared for the confrontation with the corrupted Keeper, we need to perform a fleet wide ready-check for all systems. We can engage enemies that have been preying on the local area lately due to the diminished security situation.

<color=#FBB03F>Strikes are difficult missions that require a strong fleet from several commanders to beat.</color>
	* Type:	Event
	* EventId:	event_halloween_2023_t4
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&5;Mode&Strike;Tags&T3up

### qe_halloween_2023_day10_t4: The Iyatequa promised to negotiate a deal for safe passage into Cangacian space. However, even though the galaxy is at stake, the traders still insist on receiving a hefty price.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
The Iyatequa promised to negotiate a deal for safe passage into Cangacian space. However, even though the galaxy is at stake, the traders still insist on receiving a hefty price.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
	* Type:	Event
	* EventId:	event_halloween_2023_t4
	* Goals:	GainItem,0
	* GoalParameters:	Id&CR;Amount&10000;ExcludedSources&BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

### qe_halloween_2023_day11_t4: We must confront the corrupted Keeper Malik and end the Progenitor incursion.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
We must confront the corrupted Keeper Malik and end the Progenitor incursion.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
	* Type:	Event
	* EventId:	event_halloween_2023_t4
	* Goals:	CompleteMission,0
	* GoalParameters:	Id&event_halloween2023_Rashidun_t4

## ql_event_tanochWinter_2023_t1

### qe_tanWin_2023_day01_t1: Day 1: Resource Relief
We received priority communication from Lazarus Base. A subfaction of the Tanoch, the Chicuat, have made contact with Hiigaran representatives and requested aid. Fleet Command wants us to support the Chicuat and establish friendly ties. Our first task is to provide basic resources.

<color=#FBB03F>Ore can be mined from asteroids in asteroid fields. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t1
	* MailsOnCompletion:	m_tanWin_2023_d01_log
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Asteroid_Crud_T1up;Amount&1000;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_tanWin_2023_day02_t1: Day 2: Processor Surrogate
The Chicuat infrastructure is badly degraded with age and suffered heavy damage in recent attacks. We're asked to refine materials to support their restoration efforts.

<color=#FBB03F>Rare earths are an occasional by-product of refining. They are required for upgrading modules.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t1
	* Goals:	GainItem,0
	* GoalParameters:	Tags&RareEarth_T1up;Amount&50;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_tanWin_2023_day03_t1: Day 3: Wayward Cargo
The Chicuat have informed us several critical supply convoys have gone missing. We should try to retrieve any goods by hunting down local bandits.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t1
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Salvage_T1up;Amount&5;ExcludedSources&MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_OpenContainer

### qe_tanWin_2023_day04_t1: Day 4: Relief Package
Ekekko, our Iyatequa liaison, has suggested to negotiate a trade deal with his contacts to support the Chicuat's need for basic supplies. We should sell some of our own items to get the traders interested.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t1
	* Goals:	GainItem,0
	* GoalParameters:	Id&CR;Amount&1250;ExcludedSources&BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

### qe_tanWin_2023_day05_t1: Day 5: Gesture of Aid
We received emergency communication from the Chicuat Elders. They anticipate a raid on one of their remote trading stations. Toci asks us to take on the defense in order to relieve the weakened and overextended Chicuat forces.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t1
	* Goals:	CompleteMission,0
	* GoalParameters:	Id&event_tanWin2023_DefendBase_t1

### qe_tanWin_2023_day06_t1: Day 6: Imperial Appeal
We must find out whether the Tecuban really are behind the recent attacks on the Chicuat. Our contact in the Tanoch Empire might be able to provide information. We should do some assignments to show good faith.

<color=#FBB03F>There are different types of assignments available in your assignment log.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t1
	* MailsOnCompletion:	m_tanWin_2023_d06_log
	* Goals:	CompleteQuest,0
	* GoalParameters:	Amount&5;Tags&T1up

### qe_tanWin_2023_day07_t1: Day 7: Black Eye
Lazarus Base has processed Tepin Papan's information. There are reports about the rising influence of an ambitous leader named Heyoka. He is promoting expansionist ideas and has a particular disdain for the Chicuat. We should find out if the name is familiar in the criminal underworld here.

<color=#FBB03F>The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t1
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedT1_ShipsDestroyedT2_ShipsDestroyedT3_ShipsDestroyedT4;Amount&15

### qe_tanWin_2023_day08_t1: Day 8: Catch and Kill
Our investigations produced evidence for contact between the Tecuban leader Heyoka and high profile criminals. We must hunt down these outlaws to learn more.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t1
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&1;Tags&Rare_T1up;Mode&Generated

### qe_tanWin_2023_day09_t1: Day 9: Raise the Stakes
The Chicuat Elders have asked us to wait for their intelligence report on possible Tecuban forces within Acatla. In the meanwhile we should strengthen our forces to prepare for battle.

<color=#FBB03F>Most ores need to be refined to be used for constructions. The refining process may result in rare earths as well.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t1
	* Goals:	GainItem,0
	* GoalParameters:	Tags&RareEarth_T1up;Amount&50;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_tanWin_2023_day10_t1: Day 10: In the Shadows
Intelligence from the Chicuat points to a Tecuban base operating around an uninhabited planet. We must go there and eliminate this base to stop the raids.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t1
	* Goals:	CompleteMission,0
	* GoalParameters:	Id&event_tanWin2023_AttackBase_t1

### qe_tanWin_2023_day11_t1: Day 11: Imperial Rumors
In order to gather information about the Vaygr's activity we must contact Tepin Papan once more. We should do some assignments to compensate him for his assistance.

<color=#FBB03F>There are different types of assignments available in your assignment log.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t1
	* MailsOnCompletion:	m_tanWin_2023_d11_log
	* Goals:	CompleteQuest,0
	* GoalParameters:	Amount&5;Tags&T1up

### qe_tanWin_2023_day12_t1: Day 12: Seek and Recover
While Tepin Papan is trying to gather information about the Vaygr's involvement with the Tecuban, we should scan some systems and see if we can find any clues about their whereabouts.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t1
	* Goals:	Scan,0
	* GoalParameters:	Tags&InSystem_T1up;Amount&10;Analyzed&True

### qe_tanWin_2023_day13_t1: Day 13: Among the People
We hope to learn more about the Vaygr's activity from the local people. We should do some good deeds around here to gain their trust.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t1
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Insignia_T1up;Amount&25;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_tanWin_2023_day14_t1: Day 14: Active Search
Some local folks have agreed to provide information that could lead to the Vaygr. However, before they hand it over, they want us help them with a particularly challenging mission.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t1
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&1;Tags&Rare_T1up;Mode&Generated

### qe_tanWin_2023_day15_t1: Day 15: Hunting Party
We must hunt down a group of thugs that is suspected to be working for the Vaygr.

<color=#FBB03F>The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t1
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedT1_ShipsDestroyedT2_ShipsDestroyedT3_ShipsDestroyedT4;Amount&15

### qe_tanWin_2023_day16_t1: Day 16: Attack the Vaygr
In our search for the Vaygr involved with the Tecuban, we aquired one of their communication frequencies. If we contact the Vaygr now, we should be able to trace their signal and hyper jump to their exact location.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t1
	* Goals:	CompleteMission,0
	* GoalParameters:	Id&event_tanWin2023_Relic_t1

### qe_tanWin_2023_day17_t1: Day 17: Polite Inquiries
There is still no answer from Tepin Papan since we last spoke with him. We should do some more assignments to gain his attention and see if he was able to gather any information about the Vaygr's intentions.

<color=#FBB03F>There are different types of assignments available in your assignment log.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t1
	* MailsOnCompletion:	m_tanWin_2023_d17_log
	* Goals:	CompleteQuest,0
	* GoalParameters:	Amount&5;Tags&T1up

### qe_tanWin_2023_day18_t1: Day 18: Purchased Whispers
Ekekko wants us to trade on the local markets and see if we find someone who's willing to sell information on Jochik Kaan's motives.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t1
	* Goals:	GainItem,0
	* GoalParameters:	Id&CR;Amount&1250;ExcludedSources&BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

### qe_tanWin_2023_day19_t1: Day 19: Getting There First
We contacted the Chicuat Elders and told them about Jochik Kaan's possible intention to obtain a particular Progenitor object. They have given us intel about a criminal organization that deals with Progenitor objects within the Tanoch Empire. We should investigate.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t1
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&1;Tags&Rare_T1up;Mode&Generated

### qe_tanWin_2023_day20_t1: Day 20: Providing Protection
While Gideon S'jet is researching the data set of Progenitor objects, the Chicuat Elders have informed us of a resurgance of Tecuban activity within their territory. We should support the defensive efforts.

<color=#FBB03F>The strength of enemies is dependent on a signal's or asteroid cluster's tier and subtier. The subtier is the number next to the tier icon.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t1
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedT1_ShipsDestroyedT2_ShipsDestroyedT3_ShipsDestroyedT4;Amount&15

### qe_tanWin_2023_day21_t1: Day 21: Hunt for Knowledge
Gideon S'jet's research into the data set of Progenitor objects turned out more difficult than expected. He asked us to support him to accelerate the process.

<color=#FBB03F>Progenitor ships can be found in signals. They are strong enemies, but their salvage contains resources that cannot be found in the salvage of other ships.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t1
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedProgenitorT1_ShipsDestroyedProgenitorT2_ShipsDestroyedProgenitorT3_ShipsDestroyedProgenitorT4;Amount&10

### qe_tanWin_2023_day22_t1: Day 22: Showdown at the Academy
We finally learned Jochik Kaan's intentions. He sparked the flames of war to weaken the Chicuat defenses and steal the Baetyl from Tlapallan Academy, one of their key centers of learning. We must travel there at once, before it is too late.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t1
	* MailsOnCompletion:	m_tanWin_2023_d22_log
	* Goals:	CompleteMission,0
	* GoalParameters:	Id&event_tanWin2023_Academy_t1

## ql_event_tanochWinter_2023_t2

### qe_tanWin_2023_day01_t2: We received priority communication from Lazarus Base. A subfaction of the Tanoch, the Chicuat, have made contact with Hiigaran representatives and requested aid. Fleet Command wants us to support the Chicuat and establish friendly ties. Our first task is to provide basic resources.

<color=#FBB03F>Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.</color>
We received priority communication from Lazarus Base. A subfaction of the Tanoch, the Chicuat, have made contact with Hiigaran representatives and requested aid. Fleet Command wants us to support the Chicuat and establish friendly ties. Our first task is to provide basic resources.

<color=#FBB03F>Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t2
	* MailsOnCompletion:	m_tanWin_2023_d01_log
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Asteroid_Crud_T2up;Amount&1200;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_tanWin_2023_day02_t2: The Chicuat infrastructure is badly degraded with age and suffered heavy damage in recent attacks. We're asked to refine materials to support their restoration efforts.

<color=#FBB03F>Rare earths are an occasional by-product of refining. They are required for upgrading modules.</color>
The Chicuat infrastructure is badly degraded with age and suffered heavy damage in recent attacks. We're asked to refine materials to support their restoration efforts.

<color=#FBB03F>Rare earths are an occasional by-product of refining. They are required for upgrading modules.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t2
	* Goals:	GainItem,0
	* GoalParameters:	Tags&RareEarth_T2up;Amount&50;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_tanWin_2023_day03_t2: The Chicuat have informed us several critical supply convoys have gone missing. We should try to retrieve any goods by hunting down local bandits.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
The Chicuat have informed us several critical supply convoys have gone missing. We should try to retrieve any goods by hunting down local bandits.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t2
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Salvage_T2up;Amount&5;ExcludedSources&MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_OpenContainer

### qe_tanWin_2023_day04_t2: Ekekko, our Iyatequa liaison, has suggested to negotiate a trade deal with his contacts to support the Chicuat's need for basic supplies. We should sell some of our own items to get the traders interested.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
Ekekko, our Iyatequa liaison, has suggested to negotiate a trade deal with his contacts to support the Chicuat's need for basic supplies. We should sell some of our own items to get the traders interested.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t2
	* Goals:	GainItem,0
	* GoalParameters:	Id&CR;Amount&2500;ExcludedSources&BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

### qe_tanWin_2023_day05_t2: We received emergency communication from the Chicuat Elders. They anticipate a raid on one of their remote trading stations. Toci asks us to take on the defense in order to relieve the weakened and overextended Chicuat forces.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
We received emergency communication from the Chicuat Elders. They anticipate a raid on one of their remote trading stations. Toci asks us to take on the defense in order to relieve the weakened and overextended Chicuat forces.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t2
	* Goals:	CompleteMission,0
	* GoalParameters:	Id&event_tanWin2023_DefendBase_t2

### qe_tanWin_2023_day06_t2: We must find out whether the Tecuban really are behind the recent attacks on the Chicuat. Our contact in the Tanoch Empire might be able to provide information. We should do some assignments to show good faith.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
We must find out whether the Tecuban really are behind the recent attacks on the Chicuat. Our contact in the Tanoch Empire might be able to provide information. We should do some assignments to show good faith.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t2
	* MailsOnCompletion:	m_tanWin_2023_d06_log
	* Goals:	CompleteQuest,0
	* GoalParameters:	Amount&5;Tags&Faction_Tanoch_T2up

### qe_tanWin_2023_day07_t2: Lazarus Base has processed Tepin Papan's information. There are reports about the rising influence of an ambitous leader named Heyoka. He is promoting expansionist ideas and has a particular disdain for the Chicuat. We should find out if the name is familiar in the criminal underworld here.

<color=#FBB03F>Some Tanoch fleets have broken away from the Tanoch empire to pursue their own agenda. These renegades can be found in signals, prowling Yaot space to continue ancient feuds.</color>
Lazarus Base has processed Tepin Papan's information. There are reports about the rising influence of an ambitous leader named Heyoka. He is promoting expansionist ideas and has a particular disdain for the Chicuat. We should find out if the name is familiar in the criminal underworld here.

<color=#FBB03F>Some Tanoch fleets have broken away from the Tanoch empire to pursue their own agenda. These renegades can be found in signals, prowling Yaot space to continue ancient feuds.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t2
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedTanochT2_ShipsDestroyedTanochT3_ShipsDestroyedTanochT4;Amount&10

### qe_tanWin_2023_day08_t2: Our investigations produced evidence for contact between the Tecuban leader Heyoka and high profile criminals. We must hunt down these outlaws to learn more.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
Our investigations produced evidence for contact between the Tecuban leader Heyoka and high profile criminals. We must hunt down these outlaws to learn more.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t2
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&1;Tags&Epic_T2up;Mode&Generated

### qe_tanWin_2023_day09_t2: The Chicuat Elders have asked us to wait for their intelligence report on possible Tecuban forces within Acatla. In the meanwhile we should strengthen our forces to prepare for battle.

<color=#FBB03F>External modules, such as turrets or sensors, can be upgraded in the External Module screen which will increase their power. Upgrading one level costs credits and RE.</color>
The Chicuat Elders have asked us to wait for their intelligence report on possible Tecuban forces within Acatla. In the meanwhile we should strengthen our forces to prepare for battle.

<color=#FBB03F>External modules, such as turrets or sensors, can be upgraded in the External Module screen which will increase their power. Upgrading one level costs credits and RE.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t2
	* Goals:	Craft,0
	* GoalParameters:	Category&Upgrade;Tags&External_Module_T1up;Amount&1

### qe_tanWin_2023_day10_t2: Intelligence from the Chicuat points to a Tecuban base operating around an uninhabited planet. We must go there and eliminate this base to stop the raids.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
Intelligence from the Chicuat points to a Tecuban base operating around an uninhabited planet. We must go there and eliminate this base to stop the raids.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t2
	* Goals:	CompleteMission,0
	* GoalParameters:	Id&event_tanWin2023_AttackBase_t2

### qe_tanWin_2023_day11_t2: In order to gather information about the Vaygr's activity we must contact Tepin Papan once more. We should do some assignments to compensate him for his assistance.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
In order to gather information about the Vaygr's activity we must contact Tepin Papan once more. We should do some assignments to compensate him for his assistance.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t2
	* MailsOnCompletion:	m_tanWin_2023_d11_log
	* Goals:	Statistic,0
	* GoalParameters:	Id&RepTanoch;Amount&135

### qe_tanWin_2023_day12_t2: While Tepin Papan is trying to gather information about the Vaygr's involvement with the Tecuban, we should scan some systems and see if we can find any clues about their whereabouts.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
While Tepin Papan is trying to gather information about the Vaygr's involvement with the Tecuban, we should scan some systems and see if we can find any clues about their whereabouts.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t2
	* Goals:	Scan,0
	* GoalParameters:	Tags&InSystem_T2up;Amount&10;Analyzed&True

### qe_tanWin_2023_day13_t2: We hope to learn more about the Vaygr's activity from the local people. We should do some good deeds around here to gain their trust.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.</color>
We hope to learn more about the Vaygr's activity from the local people. We should do some good deeds around here to gain their trust.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t2
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Insignia_T2up;Amount&25;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_tanWin_2023_day14_t2: Some local folks have agreed to provide information that could lead to the Vaygr. However, before they hand it over, they want us help them with a particularly challenging mission.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
Some local folks have agreed to provide information that could lead to the Vaygr. However, before they hand it over, they want us help them with a particularly challenging mission.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t2
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&1;Tags&Epic_T2up;Mode&Generated

### qe_tanWin_2023_day15_t2: We must hunt down a group of thugs that is suspected to be working for the Vaygr.

<color=#FBB03F>Some Tanoch fleets have broken away from the Tanoch empire to pursue their own agenda. These renegades can be found in signals, prowling Yaot space to continue ancient feuds.</color>
We must hunt down a group of thugs that is suspected to be working for the Vaygr.

<color=#FBB03F>Some Tanoch fleets have broken away from the Tanoch empire to pursue their own agenda. These renegades can be found in signals, prowling Yaot space to continue ancient feuds.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t2
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedTanochT2_ShipsDestroyedTanochT3_ShipsDestroyedTanochT4;Amount&10

### qe_tanWin_2023_day16_t2: In our search for the Vaygr involved with the Tecuban, we aquired one of their communication frequencies. If we contact the Vaygr now, we should be able to trace their signal and hyper jump to their exact location.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
In our search for the Vaygr involved with the Tecuban, we aquired one of their communication frequencies. If we contact the Vaygr now, we should be able to trace their signal and hyper jump to their exact location.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t2
	* Goals:	CompleteMission,0
	* GoalParameters:	Id&event_tanWin2023_Relic_t2

### qe_tanWin_2023_day17_t2: There is still no answer from Tepin Papan since we last spoke with him. We should do some more assignments to gain his attention and see if he was able to gather any information about the Vaygr's intentions.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
There is still no answer from Tepin Papan since we last spoke with him. We should do some more assignments to gain his attention and see if he was able to gather any information about the Vaygr's intentions.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t2
	* MailsOnCompletion:	m_tanWin_2023_d17_log
	* Goals:	CompleteQuest,0
	* GoalParameters:	Amount&5;Tags&Faction_Tanoch_T2up

### qe_tanWin_2023_day18_t2: Ekekko wants us to trade on the local markets and see if we find someone who's willing to sell information on Jochik Kaan's motives.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
Ekekko wants us to trade on the local markets and see if we find someone who's willing to sell information on Jochik Kaan's motives.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t2
	* Goals:	GainItem,0
	* GoalParameters:	Id&CR;Amount&2500;ExcludedSources&BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

### qe_tanWin_2023_day19_t2: We contacted the Chicuat Elders and told them about Jochik Kaan's possible intention to obtain a particular Progenitor object. They have given us intel about a criminal organization that deals with Progenitor objects within the Tanoch Empire. We should investigate.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
We contacted the Chicuat Elders and told them about Jochik Kaan's possible intention to obtain a particular Progenitor object. They have given us intel about a criminal organization that deals with Progenitor objects within the Tanoch Empire. We should investigate.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t2
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&1;Tags&Epic_T2up;Mode&Generated

### qe_tanWin_2023_day20_t2: While Gideon S'jet is researching the data set of Progenitor objects, the Chicuat Elders have informed us of a resurgance of Tecuban activity within their territory. We should support the defensive efforts.

<color=#FBB03F>Some Tanoch fleets have broken away from the Tanoch empire to pursue their own agenda. These renegades can be found in signals, prowling Yaot space to continue ancient feuds.</color>
While Gideon S'jet is researching the data set of Progenitor objects, the Chicuat Elders have informed us of a resurgance of Tecuban activity within their territory. We should support the defensive efforts.

<color=#FBB03F>Some Tanoch fleets have broken away from the Tanoch empire to pursue their own agenda. These renegades can be found in signals, prowling Yaot space to continue ancient feuds.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t2
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedTanochT2_ShipsDestroyedTanochT3_ShipsDestroyedTanochT4;Amount&10

### qe_tanWin_2023_day21_t2: Gideon S'jet's research into the data set of Progenitor objects turned out more difficult than expected. He asked us to support him to accelerate the process.

<color=#FBB03F>Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.</color>
Gideon S'jet's research into the data set of Progenitor objects turned out more difficult than expected. He asked us to support him to accelerate the process.

<color=#FBB03F>Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t2
	* Goals:	GainItem,0
	* GoalParameters:	Id&RP;Amount&200;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_tanWin_2023_day22_t2: We finally learned Jochik Kaan's intentions. He sparked the flames of war to weaken the Chicuat defenses and steal the Baetyl from Tlapallan Academy, one of their key centers of learning. We must travel there at once, before it is too late.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
We finally learned Jochik Kaan's intentions. He sparked the flames of war to weaken the Chicuat defenses and steal the Baetyl from Tlapallan Academy, one of their key centers of learning. We must travel there at once, before it is too late.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t2
	* MailsOnCompletion:	m_tanWin_2023_d22_log
	* Goals:	CompleteMission,0
	* GoalParameters:	Id&event_tanWin2023_Academy_t2

## ql_event_tanochWinter_2023_t3

### qe_tanWin_2023_day01_t3: We received priority communication from Lazarus Base. A subfaction of the Tanoch, the Chicuat, have made contact with Hiigaran representatives and requested aid. Fleet Command wants us to support the Chicuat and establish friendly ties. Our first task is to provide basic resources.

<color=#FBB03F>Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.</color>
We received priority communication from Lazarus Base. A subfaction of the Tanoch, the Chicuat, have made contact with Hiigaran representatives and requested aid. Fleet Command wants us to support the Chicuat and establish friendly ties. Our first task is to provide basic resources.

<color=#FBB03F>Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t3
	* MailsOnCompletion:	m_tanWin_2023_d01_log
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Gas_T3up;Amount&1000;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_tanWin_2023_day02_t3: The Chicuat infrastructure is badly degraded with age and suffered heavy damage in recent attacks. We're asked to refine materials to support their restoration efforts.

<color=#FBB03F>Rare earths are an occasional by-product of refining. They are required for upgrading modules.</color>
The Chicuat infrastructure is badly degraded with age and suffered heavy damage in recent attacks. We're asked to refine materials to support their restoration efforts.

<color=#FBB03F>Rare earths are an occasional by-product of refining. They are required for upgrading modules.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t3
	* Goals:	GainItem,0
	* GoalParameters:	Tags&RareEarth_T3up;Amount&50;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_tanWin_2023_day03_t3: The Chicuat have informed us several critical supply convoys have gone missing. We should try to retrieve any goods by hunting down local bandits.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
The Chicuat have informed us several critical supply convoys have gone missing. We should try to retrieve any goods by hunting down local bandits.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t3
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Salvage_T3up;Amount&5;ExcludedSources&MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_OpenContainer

### qe_tanWin_2023_day04_t3: Ekekko, our Iyatequa liaison, has suggested to negotiate a trade deal with his contacts to support the Chicuat's need for basic supplies. We should sell some of our own items to get the traders interested.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
Ekekko, our Iyatequa liaison, has suggested to negotiate a trade deal with his contacts to support the Chicuat's need for basic supplies. We should sell some of our own items to get the traders interested.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t3
	* Goals:	GainItem,0
	* GoalParameters:	Id&CR;Amount&5000;ExcludedSources&BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

### qe_tanWin_2023_day05_t3: We received emergency communication from the Chicuat Elders. They anticipate a raid on one of their remote trading stations. Toci asks us to take on the defense in order to relieve the weakened and overextended Chicuat forces.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
We received emergency communication from the Chicuat Elders. They anticipate a raid on one of their remote trading stations. Toci asks us to take on the defense in order to relieve the weakened and overextended Chicuat forces.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t3
	* Goals:	CompleteMission,0
	* GoalParameters:	Id&event_tanWin2023_DefendBase_t3

### qe_tanWin_2023_day06_t3: We must find out whether the Tecuban really are behind the recent attacks on the Chicuat. Our contact in the Tanoch Empire might be able to provide information. We should do some assignments to show good faith.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
We must find out whether the Tecuban really are behind the recent attacks on the Chicuat. Our contact in the Tanoch Empire might be able to provide information. We should do some assignments to show good faith.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t3
	* MailsOnCompletion:	m_tanWin_2023_d06_log
	* Goals:	CompleteQuest,0
	* GoalParameters:	Amount&5;Tags&Faction_Tanoch_T3up

### qe_tanWin_2023_day07_t3: Lazarus Base has processed Tepin Papan's information. There are reports about the rising influence of an ambitous leader named Heyoka. He is promoting expansionist ideas and has a particular disdain for the Chicuat. We should find out if the name is familiar in the criminal underworld here.

<color=#FBB03F>Some Tanoch fleets have broken away from the Tanoch empire to pursue their own agenda. These renegades can be found in signals, prowling Yaot space to continue ancient feuds.</color>
Lazarus Base has processed Tepin Papan's information. There are reports about the rising influence of an ambitous leader named Heyoka. He is promoting expansionist ideas and has a particular disdain for the Chicuat. We should find out if the name is familiar in the criminal underworld here.

<color=#FBB03F>Some Tanoch fleets have broken away from the Tanoch empire to pursue their own agenda. These renegades can be found in signals, prowling Yaot space to continue ancient feuds.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t3
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedTanochT3_ShipsDestroyedTanochT4;Amount&10

### qe_tanWin_2023_day08_t3: Our investigations produced evidence for contact between the Tecuban leader Heyoka and high profile criminals. We must hunt down these outlaws to learn more.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
Our investigations produced evidence for contact between the Tecuban leader Heyoka and high profile criminals. We must hunt down these outlaws to learn more.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t3
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&1;Tags&Epic_T3up;Mode&Generated

### qe_tanWin_2023_day09_t3: The Chicuat Elders have asked us to wait for their intelligence report on possible Tecuban forces within Acatla. In the meanwhile we should strengthen our forces to prepare for battle.

<color=#FBB03F>External modules, such as turrets or sensors, can be upgraded in the External Module screen which will increase their power. Upgrading one level costs credits and RE.</color>
The Chicuat Elders have asked us to wait for their intelligence report on possible Tecuban forces within Acatla. In the meanwhile we should strengthen our forces to prepare for battle.

<color=#FBB03F>External modules, such as turrets or sensors, can be upgraded in the External Module screen which will increase their power. Upgrading one level costs credits and RE.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t3
	* Goals:	Craft,0
	* GoalParameters:	Category&Upgrade;Tags&External_Module_T2up;Amount&1

### qe_tanWin_2023_day10_t3: Intelligence from the Chicuat points to a Tecuban base operating around an uninhabited planet. We must go there and eliminate this base to stop the raids.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
Intelligence from the Chicuat points to a Tecuban base operating around an uninhabited planet. We must go there and eliminate this base to stop the raids.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t3
	* Goals:	CompleteMission,0
	* GoalParameters:	Id&event_tanWin2023_AttackBase_t3

### qe_tanWin_2023_day11_t3: In order to gather information about the Vaygr's activity we must contact Tepin Papan once more. We should do some assignments to compensate him for his assistance.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
In order to gather information about the Vaygr's activity we must contact Tepin Papan once more. We should do some assignments to compensate him for his assistance.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t3
	* MailsOnCompletion:	m_tanWin_2023_d11_log
	* Goals:	Statistic,0
	* GoalParameters:	Id&RepTanoch;Amount&180

### qe_tanWin_2023_day12_t3: While Tepin Papan is trying to gather information about the Vaygr's involvement with the Tecuban, we should scan some systems and see if we can find any clues about their whereabouts.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
While Tepin Papan is trying to gather information about the Vaygr's involvement with the Tecuban, we should scan some systems and see if we can find any clues about their whereabouts.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t3
	* Goals:	Scan,0
	* GoalParameters:	Tags&InSystem_T3up;Amount&10;Analyzed&True

### qe_tanWin_2023_day13_t3: We hope to learn more about the Vaygr's activity from the local people. We should do some good deeds around here to gain their trust.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.</color>
We hope to learn more about the Vaygr's activity from the local people. We should do some good deeds around here to gain their trust.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t3
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Insignia_T3up;Amount&25;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_tanWin_2023_day14_t3: Some local folks have agreed to provide information that could lead to the Vaygr. However, before they hand it over, they want us help them with a particularly challenging mission.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
Some local folks have agreed to provide information that could lead to the Vaygr. However, before they hand it over, they want us help them with a particularly challenging mission.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t3
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&1;Tags&Epic_T3up;Mode&Generated

### qe_tanWin_2023_day15_t3: We must hunt down a group of thugs that is suspected to be working for the Vaygr.

<color=#FBB03F>Some Tanoch fleets have broken away from the Tanoch empire to pursue their own agenda. These renegades can be found in signals, prowling Yaot space to continue ancient feuds.</color>
We must hunt down a group of thugs that is suspected to be working for the Vaygr.

<color=#FBB03F>Some Tanoch fleets have broken away from the Tanoch empire to pursue their own agenda. These renegades can be found in signals, prowling Yaot space to continue ancient feuds.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t3
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedTanochT3_ShipsDestroyedTanochT4;Amount&10

### qe_tanWin_2023_day16_t3: In our search for the Vaygr involved with the Tecuban, we aquired one of their communication frequencies. If we contact the Vaygr now, we should be able to trace their signal and hyper jump to their exact location.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
In our search for the Vaygr involved with the Tecuban, we aquired one of their communication frequencies. If we contact the Vaygr now, we should be able to trace their signal and hyper jump to their exact location.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t3
	* Goals:	CompleteMission,0
	* GoalParameters:	Id&event_tanWin2023_Relic_t3

### qe_tanWin_2023_day17_t3: There is still no answer from Tepin Papan since we last spoke with him. We should do some more assignments to gain his attention and see if he was able to gather any information about the Vaygr's intentions.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
There is still no answer from Tepin Papan since we last spoke with him. We should do some more assignments to gain his attention and see if he was able to gather any information about the Vaygr's intentions.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t3
	* MailsOnCompletion:	m_tanWin_2023_d17_log
	* Goals:	CompleteQuest,0
	* GoalParameters:	Amount&5;Tags&Faction_Tanoch_T3up

### qe_tanWin_2023_day18_t3: Ekekko wants us to trade on the local markets and see if we find someone who's willing to sell information on Jochik Kaan's motives.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
Ekekko wants us to trade on the local markets and see if we find someone who's willing to sell information on Jochik Kaan's motives.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t3
	* Goals:	GainItem,0
	* GoalParameters:	Id&CR;Amount&5000;ExcludedSources&BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

### qe_tanWin_2023_day19_t3: We contacted the Chicuat Elders and told them about Jochik Kaan's possible intention to obtain a particular Progenitor object. They have given us intel about a criminal organization that deals with Progenitor objects within the Tanoch Empire. We should investigate.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
We contacted the Chicuat Elders and told them about Jochik Kaan's possible intention to obtain a particular Progenitor object. They have given us intel about a criminal organization that deals with Progenitor objects within the Tanoch Empire. We should investigate.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t3
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&1;Tags&Epic_T3up;Mode&Generated

### qe_tanWin_2023_day20_t3: While Gideon S'jet is researching the data set of Progenitor objects, the Chicuat Elders have informed us of a resurgance of Tecuban activity within their territory. We should support the defensive efforts.

<color=#FBB03F>Some Tanoch fleets have broken away from the Tanoch empire to pursue their own agenda. These renegades can be found in signals, prowling Yaot space to continue ancient feuds.</color>
While Gideon S'jet is researching the data set of Progenitor objects, the Chicuat Elders have informed us of a resurgance of Tecuban activity within their territory. We should support the defensive efforts.

<color=#FBB03F>Some Tanoch fleets have broken away from the Tanoch empire to pursue their own agenda. These renegades can be found in signals, prowling Yaot space to continue ancient feuds.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t3
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedTanochT3_ShipsDestroyedTanochT4;Amount&10

### qe_tanWin_2023_day21_t3: Gideon S'jet's research into the data set of Progenitor objects turned out more difficult than expected. He asked us to support him to accelerate the process.

<color=#FBB03F>Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.</color>
Gideon S'jet's research into the data set of Progenitor objects turned out more difficult than expected. He asked us to support him to accelerate the process.

<color=#FBB03F>Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t3
	* Goals:	GainItem,0
	* GoalParameters:	Id&RP;Amount&200;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_tanWin_2023_day22_t3: We finally learned Jochik Kaan's intentions. He sparked the flames of war to weaken the Chicuat defenses and steal the Baetyl from Tlapallan Academy, one of their key centers of learning. We must travel there at once, before it is too late.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
We finally learned Jochik Kaan's intentions. He sparked the flames of war to weaken the Chicuat defenses and steal the Baetyl from Tlapallan Academy, one of their key centers of learning. We must travel there at once, before it is too late.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t3
	* MailsOnCompletion:	m_tanWin_2023_d22_log
	* Goals:	CompleteMission,0
	* GoalParameters:	Id&event_tanWin2023_Academy_t3

## ql_event_tanochWinter_2023_t4

### qe_tanWin_2023_day01_t4: We received priority communication from Lazarus Base. A subfaction of the Tanoch, the Chicuat, have made contact with Hiigaran representatives and requested aid. Fleet Command wants us to support the Chicuat and establish friendly ties. Our first task is to provide basic resources.

<color=#FBB03F>Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.</color>
We received priority communication from Lazarus Base. A subfaction of the Tanoch, the Chicuat, have made contact with Hiigaran representatives and requested aid. Fleet Command wants us to support the Chicuat and establish friendly ties. Our first task is to provide basic resources.

<color=#FBB03F>Gases are used for the fabrication of Tier 3 and 4 parts. Special gas collectors can harvest them from the dangerous atmosphere of jovians.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t4
	* MailsOnCompletion:	m_tanWin_2023_d01_log
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Gas_T4up;Amount&1200;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_tanWin_2023_day02_t4: The Chicuat infrastructure is badly degraded with age and suffered heavy damage in recent attacks. We're asked to refine materials to support their restoration efforts.

<color=#FBB03F>Rare earths are an occasional by-product of refining. They are required for upgrading modules.</color>
The Chicuat infrastructure is badly degraded with age and suffered heavy damage in recent attacks. We're asked to refine materials to support their restoration efforts.

<color=#FBB03F>Rare earths are an occasional by-product of refining. They are required for upgrading modules.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t4
	* Goals:	GainItem,0
	* GoalParameters:	Tags&RareEarth_T4up;Amount&50;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_tanWin_2023_day03_t4: The Chicuat have informed us several critical supply convoys have gone missing. We should try to retrieve any goods by hunting down local bandits.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
The Chicuat have informed us several critical supply convoys have gone missing. We should try to retrieve any goods by hunting down local bandits.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t4
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Salvage_T4up;Amount&5;ExcludedSources&MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_OpenContainer

### qe_tanWin_2023_day04_t4: Ekekko, our Iyatequa liaison, has suggested to negotiate a trade deal with his contacts to support the Chicuat's need for basic supplies. We should sell some of our own items to get the traders interested.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
Ekekko, our Iyatequa liaison, has suggested to negotiate a trade deal with his contacts to support the Chicuat's need for basic supplies. We should sell some of our own items to get the traders interested.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t4
	* Goals:	GainItem,0
	* GoalParameters:	Id&CR;Amount&10000;ExcludedSources&BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

### qe_tanWin_2023_day05_t4: We received emergency communication from the Chicuat Elders. They anticipate a raid on one of their remote trading stations. Toci asks us to take on the defense in order to relieve the weakened and overextended Chicuat forces.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
We received emergency communication from the Chicuat Elders. They anticipate a raid on one of their remote trading stations. Toci asks us to take on the defense in order to relieve the weakened and overextended Chicuat forces.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t4
	* Goals:	CompleteMission,0
	* GoalParameters:	Id&event_tanWin2023_DefendBase_t4

### qe_tanWin_2023_day06_t4: We must find out whether the Tecuban really are behind the recent attacks on the Chicuat. Our contact in the Tanoch Empire might be able to provide information. We should do some assignments to show good faith.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
We must find out whether the Tecuban really are behind the recent attacks on the Chicuat. Our contact in the Tanoch Empire might be able to provide information. We should do some assignments to show good faith.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t4
	* MailsOnCompletion:	m_tanWin_2023_d06_log
	* Goals:	CompleteQuest,0
	* GoalParameters:	Amount&5;Tags&Faction_Tanoch_T4up

### qe_tanWin_2023_day07_t4: Lazarus Base has processed Tepin Papan's information. There are reports about the rising influence of an ambitous leader named Heyoka. He is promoting expansionist ideas and has a particular disdain for the Chicuat. We should find out if the name is familiar in the criminal underworld here.

<color=#FBB03F>Some Tanoch fleets have broken away from the Tanoch empire to pursue their own agenda. These renegades can be found in signals, prowling Yaot space to continue ancient feuds.</color>
Lazarus Base has processed Tepin Papan's information. There are reports about the rising influence of an ambitous leader named Heyoka. He is promoting expansionist ideas and has a particular disdain for the Chicuat. We should find out if the name is familiar in the criminal underworld here.

<color=#FBB03F>Some Tanoch fleets have broken away from the Tanoch empire to pursue their own agenda. These renegades can be found in signals, prowling Yaot space to continue ancient feuds.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t4
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedTanochT4;Amount&10

### qe_tanWin_2023_day08_t4: Our investigations produced evidence for contact between the Tecuban leader Heyoka and high profile criminals. We must hunt down these outlaws to learn more.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
Our investigations produced evidence for contact between the Tecuban leader Heyoka and high profile criminals. We must hunt down these outlaws to learn more.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t4
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&1;Tags&Epic_T4up;Mode&Generated

### qe_tanWin_2023_day09_t4: The Chicuat Elders have asked us to wait for their intelligence report on possible Tecuban forces within Acatla. In the meanwhile we should strengthen our forces to prepare for battle.

<color=#FBB03F>External modules, such as turrets or sensors, can be upgraded in the External Module screen which will increase their power. Upgrading one level costs credits and RE.</color>
The Chicuat Elders have asked us to wait for their intelligence report on possible Tecuban forces within Acatla. In the meanwhile we should strengthen our forces to prepare for battle.

<color=#FBB03F>External modules, such as turrets or sensors, can be upgraded in the External Module screen which will increase their power. Upgrading one level costs credits and RE.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t4
	* Goals:	Craft,0
	* GoalParameters:	Category&Upgrade;Tags&External_Module_T3up;Amount&1

### qe_tanWin_2023_day10_t4: Intelligence from the Chicuat points to a Tecuban base operating around an uninhabited planet. We must go there and eliminate this base to stop the raids.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
Intelligence from the Chicuat points to a Tecuban base operating around an uninhabited planet. We must go there and eliminate this base to stop the raids.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t4
	* Goals:	CompleteMission,0
	* GoalParameters:	Id&event_tanWin2023_AttackBase_t4

### qe_tanWin_2023_day11_t4: In order to gather information about the Vaygr's activity we must contact Tepin Papan once more. We should do some assignments to compensate him for his assistance.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
In order to gather information about the Vaygr's activity we must contact Tepin Papan once more. We should do some assignments to compensate him for his assistance.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t4
	* MailsOnCompletion:	m_tanWin_2023_d11_log
	* Goals:	Statistic,0
	* GoalParameters:	Id&RepTanoch;Amount&225

### qe_tanWin_2023_day12_t4: While Tepin Papan is trying to gather information about the Vaygr's involvement with the Tecuban, we should scan some systems and see if we can find any clues about their whereabouts.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
While Tepin Papan is trying to gather information about the Vaygr's involvement with the Tecuban, we should scan some systems and see if we can find any clues about their whereabouts.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t4
	* Goals:	Scan,0
	* GoalParameters:	Tags&InSystem_T4up;Amount&10;Analyzed&True

### qe_tanWin_2023_day13_t4: We hope to learn more about the Vaygr's activity from the local people. We should do some good deeds around here to gain their trust.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.</color>
We hope to learn more about the Vaygr's activity from the local people. We should do some good deeds around here to gain their trust.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from discharging officers and are earned through completing signals.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t4
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Insignia_T4up;Amount&25;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_tanWin_2023_day14_t4: Some local folks have agreed to provide information that could lead to the Vaygr. However, before they hand it over, they want us help them with a particularly challenging mission.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
Some local folks have agreed to provide information that could lead to the Vaygr. However, before they hand it over, they want us help them with a particularly challenging mission.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t4
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&1;Tags&Epic_T4up;Mode&Generated

### qe_tanWin_2023_day15_t4: We must hunt down a group of thugs that is suspected to be working for the Vaygr.

<color=#FBB03F>Some Tanoch fleets have broken away from the Tanoch empire to pursue their own agenda. These renegades can be found in signals, prowling Yaot space to continue ancient feuds.</color>
We must hunt down a group of thugs that is suspected to be working for the Vaygr.

<color=#FBB03F>Some Tanoch fleets have broken away from the Tanoch empire to pursue their own agenda. These renegades can be found in signals, prowling Yaot space to continue ancient feuds.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t4
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedTanochT4;Amount&10

### qe_tanWin_2023_day16_t4: In our search for the Vaygr involved with the Tecuban, we aquired one of their communication frequencies. If we contact the Vaygr now, we should be able to trace their signal and hyper jump to their exact location.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
In our search for the Vaygr involved with the Tecuban, we aquired one of their communication frequencies. If we contact the Vaygr now, we should be able to trace their signal and hyper jump to their exact location.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t4
	* Goals:	CompleteMission,0
	* GoalParameters:	Id&event_tanWin2023_Relic_t4

### qe_tanWin_2023_day17_t4: There is still no answer from Tepin Papan since we last spoke with him. We should do some more assignments to gain his attention and see if he was able to gather any information about the Vaygr's intentions.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
There is still no answer from Tepin Papan since we last spoke with him. We should do some more assignments to gain his attention and see if he was able to gather any information about the Vaygr's intentions.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t4
	* MailsOnCompletion:	m_tanWin_2023_d17_log
	* Goals:	CompleteQuest,0
	* GoalParameters:	Amount&5;Tags&Faction_Tanoch_T4up

### qe_tanWin_2023_day18_t4: Ekekko wants us to trade on the local markets and see if we find someone who's willing to sell information on Jochik Kaan's motives.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
Ekekko wants us to trade on the local markets and see if we find someone who's willing to sell information on Jochik Kaan's motives.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t4
	* Goals:	GainItem,0
	* GoalParameters:	Id&CR;Amount&10000;ExcludedSources&BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

### qe_tanWin_2023_day19_t4: We contacted the Chicuat Elders and told them about Jochik Kaan's possible intention to obtain a particular Progenitor object. They have given us intel about a criminal organization that deals with Progenitor objects within the Tanoch Empire. We should investigate.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
We contacted the Chicuat Elders and told them about Jochik Kaan's possible intention to obtain a particular Progenitor object. They have given us intel about a criminal organization that deals with Progenitor objects within the Tanoch Empire. We should investigate.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t4
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&1;Tags&Epic_T4up;Mode&Generated

### qe_tanWin_2023_day20_t4: While Gideon S'jet is researching the data set of Progenitor objects, the Chicuat Elders have informed us of a resurgance of Tecuban activity within their territory. We should support the defensive efforts.

<color=#FBB03F>Some Tanoch fleets have broken away from the Tanoch empire to pursue their own agenda. These renegades can be found in signals, prowling Yaot space to continue ancient feuds.</color>
While Gideon S'jet is researching the data set of Progenitor objects, the Chicuat Elders have informed us of a resurgance of Tecuban activity within their territory. We should support the defensive efforts.

<color=#FBB03F>Some Tanoch fleets have broken away from the Tanoch empire to pursue their own agenda. These renegades can be found in signals, prowling Yaot space to continue ancient feuds.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t4
	* Goals:	Statistic,0
	* GoalParameters:	Ids&ShipsDestroyedTanochT4;Amount&10

### qe_tanWin_2023_day21_t4: Gideon S'jet's research into the data set of Progenitor objects turned out more difficult than expected. He asked us to support him to accelerate the process.

<color=#FBB03F>Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.</color>
Gideon S'jet's research into the data set of Progenitor objects turned out more difficult than expected. He asked us to support him to accelerate the process.

<color=#FBB03F>Research points are produced and collected in the on-ship laboratories, or in the starbase laboratories.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t4
	* Goals:	GainItem,0
	* GoalParameters:	Id&RP;Amount&200;ExcludedSources&SellItem_BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_tanWin_2023_day22_t4: We finally learned Jochik Kaan's intentions. He sparked the flames of war to weaken the Chicuat defenses and steal the Baetyl from Tlapallan Academy, one of their key centers of learning. We must travel there at once, before it is too late.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
We finally learned Jochik Kaan's intentions. He sparked the flames of war to weaken the Chicuat defenses and steal the Baetyl from Tlapallan Academy, one of their key centers of learning. We must travel there at once, before it is too late.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
	* Type:	Event
	* EventId:	event_tanochWinter_2023_t4
	* MailsOnCompletion:	m_tanWin_2023_d22_log
	* Goals:	CompleteMission,0
	* GoalParameters:	Id&event_tanWin2023_Academy_t4

## ql_event_YaotSpring_2024_t1

### qe_yaoSpr_2024_day01_t1: There are rumors circulating in the Empty Quarter about an increase in Cangacian pirate activity. Fleet Command asks us to gather intel from our contacts with the Iyatequa traders. We should gain some favors to bargain for information.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
There are rumors circulating in the Empty Quarter about an increase in Cangacian pirate activity. Fleet Command asks us to gather intel from our contacts with the Iyatequa traders. We should gain some favors to bargain for information.

<color=#FBB03F>There are different types of assignments available in your assignment log.</color>
	* Type:	Event
	* EventId:	event_yaotSpring_2024_t1
	* Goals:	CompleteQuest,0
	* GoalParameters:	Amount&5;Tags&T1up

### qe_yaoSpr_2024_day02_t1: The Iyatequa traders are involved with pirates attacking Yaot pilgrims in the Empty Quarter. We might get more information through selling equipment and arms on the open market.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
The Iyatequa traders are involved with pirates attacking Yaot pilgrims in the Empty Quarter. We might get more information through selling equipment and arms on the open market.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
	* Type:	Event
	* EventId:	event_yaotSpring_2024_t1
	* Goals:	GainItem,0
	* GoalParameters:	Id&CR;Amount&1250;ExcludedSources&BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

### qe_yaoSpr_2024_day03_t1: To learn more about the pirate raids, we should get in contact with the Yaot pilgrims. They appear to be hiding after recent attacks. We have no other option than to perform reconnaissance in the nearby systems.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
To learn more about the pirate raids, we should get in contact with the Yaot pilgrims. They appear to be hiding after recent attacks. We have no other option than to perform reconnaissance in the nearby systems.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
	* Type:	Event
	* EventId:	event_yaotSpring_2024_t1
	* Goals:	Scan,0
	* GoalParameters:	Tags&InSystem_T1up;Amount&5;Analyzed&True

### qe_yaoSpr_2024_day04_t1: In our search for the Yaot pilgrims we have encountered intense pirate activity. We should hunt down some of their ships and see if we can gather any additional clues.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
In our search for the Yaot pilgrims we have encountered intense pirate activity. We should hunt down some of their ships and see if we can gather any additional clues.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
	* Type:	Event
	* EventId:	event_yaotSpring_2024_t1
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Salvage_T1up;Amount&5;ExcludedSources&MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_OpenContainer

### qe_yaoSpr_2024_day05_t1: Some Yaot survivors in our medical ward are ready to be questioned. If we manage to prove our good intentions they might help us find the Yaot pilgrimage.

<color=#FBB03F>Prestige is earned through each player level-up and by completing daily and weekly assignments.</color>
Some Yaot survivors in our medical ward are ready to be questioned. If we manage to prove our good intentions they might help us find the Yaot pilgrimage.

<color=#FBB03F>Prestige is earned through each player level-up and by completing daily and weekly assignments.</color>
	* Type:	Event
	* EventId:	event_yaotSpring_2024_t1
	* Goals:	GainItem,0
	* GoalParameters:	Id&LP;Amount&10;ExcludedSources&BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem

### qe_yaoSpr_2024_day06_t1: The Yaot have accepted our offer to support their pilgrimage. Requests have come in from ships needing spares and replacement parts for repairs. If we provide these, we might learn more about why the pirates are after these ships.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
The Yaot have accepted our offer to support their pilgrimage. Requests have come in from ships needing spares and replacement parts for repairs. If we provide these, we might learn more about why the pirates are after these ships.

<color=#FBB03F>Small items such as strike craft, modules and parts can be built in the fabricator. Larger items such as escort ships and flagships must be constructed at shipyards provided at larger stations.</color>
	* Type:	Event
	* EventId:	event_yaotSpring_2024_t1
	* Goals:	Craft,0
	* GoalParameters:	Category&Crafting;Tags&T1up;Amount&1

### qe_yaoSpr_2024_day07_t1: Even though pirates are still swarming the area, Chocoan and the Yaot pilgrims are adamant about continuing their travels to see the astral conjunction events. In order to deter any further attacks on the civilian ships, we should patrol and clear the systems of any significant hostile forces.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
Even though pirates are still swarming the area, Chocoan and the Yaot pilgrims are adamant about continuing their travels to see the astral conjunction events. In order to deter any further attacks on the civilian ships, we should patrol and clear the systems of any significant hostile forces.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
	* Type:	Event
	* EventId:	event_yaotSpring_2024_t1
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&1;Tags&Rare_T1up;Mode&Generated

### qe_yaoSpr_2024_day08_t1: Even the Fleet of Rams are after the Yaot pilgrim's supposed treasure. If we hope to protect them, we must first convince somebody to give us more information. We should try to make friends with the pilgrims and get somebody to talk.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from dismissing officers and are earned through completing signals.</color>
Even the Fleet of Rams are after the Yaot pilgrim's supposed treasure. If we hope to protect them, we must first convince somebody to give us more information. We should try to make friends with the pilgrims and get somebody to talk.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from dismissing officers and are earned through completing signals.</color>
	* Type:	Event
	* EventId:	event_yaotSpring_2024_t1
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Insignia_T1up;Amount&50;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_yaoSpr_2024_day09_t1: After talking to Chocoan we suspect there is more to the Yaot pilgrimage than the religious travels to astral conjunction events. We might be able to get more information from the Yaot Federation if we do some favors.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
After talking to Chocoan, we suspect there is more to the Yaot pilgrimage than the religious travels to astral conjunction events. We might be able to get more information from the Yaot Federation if we do some favors.

<color=#FBB03F>There are different types of assignments available in your assignment log.</color>
	* Type:	Event
	* EventId:	event_yaotSpring_2024_t1
	* Goals:	CompleteQuest,0
	* GoalParameters:	Amount&5;Tags&T1up

### qe_yaoSpr_2024_day10_t1: We’ve reached a dead end on collecting intelligence on the Yaot, but our source within the Tanoch Empire has offered to provide more information. We should bring an adequate gift for compensation.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
We’ve reached a dead end on collecting intelligence on the Yaot, but our source within the Tanoch Empire has offered to provide more information. We should bring an adequate gift for compensation.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
	* Type:	Event
	* EventId:	event_yaotSpring_2024_t1
	* Goals:	Pay,0
	* GoalParameters:	Id&questItem_progenitorRelic_t1;Amount&1

### qe_yaoSpr_2024_day11_t1: While we still don't know what kind of treasure the pilgrims could have aboard their vessels, Chocoan wants to move on to another astral conjunction event. He has requested our assistance in clearing out the area from any hostile threats.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
While we still don't know what kind of treasure the pilgrims could have aboard their vessels, Chocoan wants to move on to another astral conjunction event. He has requested our assistance in clearing out the area from any hostile threats.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
	* Type:	Event
	* EventId:	event_yaotSpring_2024_t1
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&1;Tags&Rare_T1up;Mode&Generated

### qe_yaoSpr_2024_day12_t1: The report on the pilgrim's procedure has been fully analyzed. Usually the pilgrim's convoy moves in a tight line formation towards the optimal conjunction points where they perform their religious rituals. However, a few ships regularly diverge from the common path and move into nearby asteroid fields. We should investigate the latest conjunction site and see if we can find anything of interest.

<color=#FBB03F>Ore can be mined from asteroids in asteroid fields. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
The report on the pilgrim's procedure has been fully analyzed. Usually the pilgrim's convoy moves in a tight line formation towards the optimal conjunction points where they perform their religious rituals. However, a few ships regularly diverge from the common path and move into nearby asteroid fields. We should investigate the latest conjunction site and see if we can find anything of interest.

<color=#FBB03F>Ore can be mined from asteroids in asteroid fields. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
	* Type:	Event
	* EventId:	event_yaotSpring_2024_t1
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Asteroid_Crud_T1up;Amount&1000;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_yaoSpr_2024_day13_t1: Chocoan has informed us that the next astral conjunction site will be inside the Cangacian territories. We convinced him to take part in the operation ourselves to ensure security in this hostile area of the Empty Quarter. Maybe we will be able to both protect the pilgrims and find out more about the suspected secret agenda. We should make sure the crew is properly prepared and ready for any eventualities.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
Chocoan has informed us that the next astral conjunction site will be inside the Cangacian territories. We convinced him to take part in the operation ourselves to ensure security in this hostile area of the Empty Quarter. Maybe we will be able to both protect the pilgrims and find out more about the suspected secret agenda. We should make sure the crew is properly prepared and ready for any eventualities.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
	* Type:	Event
	* EventId:	event_yaotSpring_2024_t1
	* Goals:	UpgradeOfficer,0
	* GoalParameters:	Amount&1

### qe_yaoSpr_2024_day14_t1: Chocoan has provided the coordinates to the next astral conjunction event. Strong hostile forces are to be expected in this system. Our goal is to both protect the civilian pilgrims and find out more about the suspected secret agenda of the Yaot Elders.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
Chocoan has provided the coordinates to the next astral conjunction event. Strong hostile forces are to be expected in this system. Our goal is to both protect the civilian pilgrims and find out more about the suspected secret agenda of the Yaot Elders.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
	* Type:	Event
	* EventId:	event_yaotSpring_2024_t1
	* Goals:	CompleteMission,0
	* GoalParameters:	Id&event_yaoSpr2024_Conjunction_t1

## ql_event_YaotSpring_2024_t2

### qe_yaoSpr_2024_day01_t2: There are rumors circulating in the Empty Quarter about an increase in Cangacian pirate activity. Fleet Command asks us to gather intel from our contacts with the Iyatequa traders. We should gain some favors to bargain for information.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
There are rumors circulating in the Empty Quarter about an increase in Cangacian pirate activity. Fleet Command asks us to gather intel from our contacts with the Iyatequa traders. We should gain some favors to bargain for information.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
	* Type:	Event
	* EventId:	event_yaotSpring_2024_t2
	* Goals:	CompleteQuest,0
	* GoalParameters:	Amount&5;Tags&Faction_Tr1_T2up

### qe_yaoSpr_2024_day02_t2: The Iyatequa traders are involved with pirates attacking Yaot pilgrims in the Empty Quarter. We might get more information through selling equipment and arms on the open market.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
The Iyatequa traders are involved with pirates attacking Yaot pilgrims in the Empty Quarter. We might get more information through selling equipment and arms on the open market.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
	* Type:	Event
	* EventId:	event_yaotSpring_2024_t2
	* Goals:	GainItem,0
	* GoalParameters:	Id&CR;Amount&2500;ExcludedSources&BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

### qe_yaoSpr_2024_day03_t2: To learn more about the pirate raids, we should get in contact with the Yaot pilgrims. They appear to be hiding after recent attacks. We have no other option than to perform reconnaissance in the nearby systems.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
To learn more about the pirate raids, we should get in contact with the Yaot pilgrims. They appear to be hiding after recent attacks. We have no other option than to perform reconnaissance in the nearby systems.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
	* Type:	Event
	* EventId:	event_yaotSpring_2024_t2
	* Goals:	Scan,0
	* GoalParameters:	Tags&InSystem_T2up;Amount&5;Analyzed&True

### qe_yaoSpr_2024_day04_t2: In our search for the Yaot pilgrims we have encountered intense pirate activity. We should hunt down some of their ships and see if we can gather any additional clues.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
In our search for the Yaot pilgrims we have encountered intense pirate activity. We should hunt down some of their ships and see if we can gather any additional clues.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
	* Type:	Event
	* EventId:	event_yaotSpring_2024_t2
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Salvage_T2up;Amount&5;ExcludedSources&MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_OpenContainer

### qe_yaoSpr_2024_day05_t2: Some Yaot survivors in our medical ward are ready to be questioned. If we manage to prove our good intentions they might help us find the Yaot pilgrimage.

<color=#FBB03F>Prestige is earned through each player level-up and by completing daily and weekly assignments.</color>
Some Yaot survivors in our medical ward are ready to be questioned. If we manage to prove our good intentions they might help us find the Yaot pilgrimage.

<color=#FBB03F>Prestige is earned through each player level-up and by completing daily and weekly assignments.</color>
	* Type:	Event
	* EventId:	event_yaotSpring_2024_t2
	* Goals:	GainItem,0
	* GoalParameters:	Id&LP;Amount&10;ExcludedSources&BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem

### qe_yaoSpr_2024_day06_t2: The Yaot have accepted our offer to support their pilgrimage. Requests have come in from ships needing spares and replacement parts for repairs. If we provide these, we might learn more about why the pirates are after these ships.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
The Yaot have accepted our offer to support their pilgrimage. Requests have come in from ships needing spares and replacement parts for repairs. If we provide these, we might learn more about why the pirates are after these ships.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
	* Type:	Event
	* EventId:	event_yaotSpring_2024_t2
	* Goals:	Craft,0
	* GoalParameters:	Category&Crafting;Tags&Part_T2up;Amount&100

### qe_yaoSpr_2024_day07_t2: Even though pirates are still swarming the area, Chocoan and the Yaot pilgrims are adamant about continuing their travels to see the astral conjunction events. In order to deter any further attacks on the civilian ships, we should patrol and clear the systems of any significant hostile forces.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
Even though pirates are still swarming the area, Chocoan and the Yaot pilgrims are adamant about continuing their travels to see the astral conjunction events. In order to deter any further attacks on the civilian ships, we should patrol and clear the systems of any significant hostile forces.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
	* Type:	Event
	* EventId:	event_yaotSpring_2024_t2
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&1;Tags&Epic_T2up;Mode&Generated

### qe_yaoSpr_2024_day08_t2: Even the Fleet of Rams are after the Yaot pilgrim's supposed treasure. If we hope to protect them, we must first convince somebody to give us more information. We should try to make friends with the pilgrims and get somebody to talk.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from dismissing officers and are earned through completing signals.</color>
Even the Fleet of Rams are after the Yaot pilgrim's supposed treasure. If we hope to protect them, we must first convince somebody to give us more information. We should try to make friends with the pilgrims and get somebody to talk.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from dismissing officers and are earned through completing signals.</color>
	* Type:	Event
	* EventId:	event_yaotSpring_2024_t2
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Insignia_T2up;Amount&50;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_yaoSpr_2024_day09_t2: After talking to Chocoan we suspect there is more to the Yaot pilgrimage than the religious travels to astral conjunction events. We might be able to get more information from the Yaot Federation if we do some favors.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
After talking to Chocoan we suspect there is more to the Yaot pilgrimage than the religious travels to astral conjunction events. We might be able to get more information from the Yaot Federation if we do some favors.

<color=#FBB03F>There are different types of assignments available in your assignment log.</color>
	* Type:	Event
	* EventId:	event_yaotSpring_2024_t2
	* Goals:	CompleteQuest,0
	* GoalParameters:	Amount&5;Tags&T2up

### qe_yaoSpr_2024_day10_t2: We’ve reached a dead end on collecting intelligence on the Yaot, but our source within the Tanoch Empire has offered to provide more information. We should bring an adequate gift for compensation.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
We’ve reached a dead end on collecting intelligence on the Yaot, but our source within the Tanoch Empire has offered to provide more information. We should bring an adequate gift for compensation.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
	* Type:	Event
	* EventId:	event_yaotSpring_2024_t2
	* Goals:	Pay,0
	* GoalParameters:	Id&questItem_progenitorRelic_t2;Amount&1

### qe_yaoSpr_2024_day11_t2: While we still don't know what kind of treasure the pilgrims could have aboard their vessels, Chocoan wants to move on to another astral conjunction event. He has requested our assistance in clearing out the area from any hostile threats.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
While we still don't know what kind of treasure the pilgrims could have aboard their vessels, Chocoan wants to move on to another astral conjunction event. He has requested our assistance in clearing out the area from any hostile threats.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
	* Type:	Event
	* EventId:	event_yaotSpring_2024_t2
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&1;Tags&Epic_T2up;Mode&Generated

### qe_yaoSpr_2024_day12_t2: The report on the pilgrim's procedure has been fully analyzed. Usually the pilgrim's convoy moves in a tight line formation towards the optimal conjunction points where they perform their religious rituals. However, a few ships regularly diverge from the common path and move into nearby asteroid fields. We should investigate the latest conjunction site and see if we can find anything of interest.

<color=#FBB03F>Ore can be mined from asteroids in asteroid fields. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
The report on the pilgrim's procedure has been fully analyzed. Usually the pilgrim's convoy moves in a tight line formation towards the optimal conjunction points where they perform their religious rituals. However, a few ships regularly diverge from the common path and move into nearby asteroid fields. We should investigate the latest conjunction site and see if we can find anything of interest.

<color=#FBB03F>Ore can be mined from asteroids in asteroid fields. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
	* Type:	Event
	* EventId:	event_yaotSpring_2024_t2
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Asteroid_Crud_T2up;Amount&1200;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_yaoSpr_2024_day13_t2: Chocoan has informed us that the next astral conjunction site will be inside the Cangacian territories. We convinced him to take part in the operation ourselves to ensure security in this hostile area of the Empty Quarter. Maybe we will be able to both protect the pilgrims and find out more about the suspected secret agenda. We should make sure the crew is properly prepared and ready for any eventualities.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
Chocoan has informed us that the next astral conjunction site will be inside the Cangacian territories. We convinced him to take part in the operation ourselves to ensure security in this hostile area of the Empty Quarter. Maybe we will be able to both protect the pilgrims and find out more about the suspected secret agenda. We should make sure the crew is properly prepared and ready for any eventualities.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
	* Type:	Event
	* EventId:	event_yaotSpring_2024_t2
	* Goals:	UpgradeOfficer,0
	* GoalParameters:	Amount&2

### qe_yaoSpr_2024_day14_t2: Chocoan has provided the coordinates to the next astral conjunction event. Strong hostile forces are to be expected in this system. Our goal is to both protect the civilian pilgrims and find out more about the suspected secret agenda of the Yaot Elders.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
Chocoan has provided the coordinates to the next astral conjunction event. Strong hostile forces are to be expected in this system. Our goal is to both protect the civilian pilgrims and find out more about the suspected secret agenda of the Yaot Elders.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
	* Type:	Event
	* EventId:	event_yaotSpring_2024_t2
	* Goals:	CompleteMission,0
	* GoalParameters:	Id&event_yaoSpr2024_Conjunction_t2

## ql_event_YaotSpring_2024_t3

### qe_yaoSpr_2024_day01_t3: There are rumors circulating in the Empty Quarter about an increase in Cangacian pirate activity. Fleet Command asks us to gather intel from our contacts with the Iyatequa traders. We should gain some favors to bargain for information.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
There are rumors circulating in the Empty Quarter about an increase in Cangacian pirate activity. Fleet Command asks us to gather intel from our contacts with the Iyatequa traders. We should gain some favors to bargain for information.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
	* Type:	Event
	* EventId:	event_yaotSpring_2024_t3
	* Goals:	CompleteQuest,0
	* GoalParameters:	Amount&5;Tags&Faction_Tr1_T3up

### qe_yaoSpr_2024_day02_t3: The Iyatequa traders are involved with pirates attacking Yaot pilgrims in the Empty Quarter. We might get more information through selling equipment and arms on the open market.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
The Iyatequa traders are involved with pirates attacking Yaot pilgrims in the Empty Quarter. We might get more information through selling equipment and arms on the open market.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
	* Type:	Event
	* EventId:	event_yaotSpring_2024_t3
	* Goals:	GainItem,0
	* GoalParameters:	Id&CR;Amount&5000;ExcludedSources&BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

### qe_yaoSpr_2024_day03_t3: To learn more about the pirate raids, we should get in contact with the Yaot pilgrims. They appear to be hiding after recent attacks. We have no other option than to perform reconnaissance in the nearby systems.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
To learn more about the pirate raids, we should get in contact with the Yaot pilgrims. They appear to be hiding after recent attacks. We have no other option than to perform reconnaissance in the nearby systems.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
	* Type:	Event
	* EventId:	event_yaotSpring_2024_t3
	* Goals:	Scan,0
	* GoalParameters:	Tags&InSystem_T3up;Amount&5;Analyzed&True

### qe_yaoSpr_2024_day04_t3: In our search for the Yaot pilgrims we have encountered intense pirate activity. We should hunt down some of their ships and see if we can gather any additional clues.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
In our search for the Yaot pilgrims we have encountered intense pirate activity. We should hunt down some of their ships and see if we can gather any additional clues.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
	* Type:	Event
	* EventId:	event_yaotSpring_2024_t3
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Salvage_T3up;Amount&5;ExcludedSources&MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_OpenContainer

### qe_yaoSpr_2024_day05_t3: Some Yaot survivors in our medical ward are ready to be questioned. If we manage to prove our good intentions they might help us find the Yaot pilgrimage.

<color=#FBB03F>Prestige is earned through each player level-up and by completing daily and weekly assignments.</color>
Some Yaot survivors in our medical ward are ready to be questioned. If we manage to prove our good intentions they might help us find the Yaot pilgrimage.

<color=#FBB03F>Prestige is earned through each player level-up and by completing daily and weekly assignments.</color>
	* Type:	Event
	* EventId:	event_yaotSpring_2024_t3
	* Goals:	GainItem,0
	* GoalParameters:	Id&LP;Amount&10;ExcludedSources&BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem

### qe_yaoSpr_2024_day06_t3: The Yaot have accepted our offer to support their pilgrimage. Requests have come in from ships needing spares and replacement parts for repairs. If we provide these, we might learn more about why the pirates are after these ships.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
The Yaot have accepted our offer to support their pilgrimage. Requests have come in from ships needing spares and replacement parts for repairs. If we provide these, we might learn more about why the pirates are after these ships.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
	* Type:	Event
	* EventId:	event_yaotSpring_2024_t3
	* Goals:	Craft,0
	* GoalParameters:	Category&Crafting;Tags&Part_T3up;Amount&100

### qe_yaoSpr_2024_day07_t3: Even though pirates are still swarming the area, Chocoan and the Yaot pilgrims are adamant about continuing their travels to see the astral conjunction events. In order to deter any further attacks on the civilian ships, we should patrol and clear the systems of any significant hostile forces.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
Even though pirates are still swarming the area, Chocoan and the Yaot pilgrims are adamant about continuing their travels to see the astral conjunction events. In order to deter any further attacks on the civilian ships, we should patrol and clear the systems of any significant hostile forces.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
	* Type:	Event
	* EventId:	event_yaotSpring_2024_t3
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&1;Tags&Epic_T3up;Mode&Generated

### qe_yaoSpr_2024_day08_t3: Even the Fleet of Rams are after the Yaot pilgrim's supposed treasure. If we hope to protect them, we must first convince somebody to give us more information. We should try to make friends with the pilgrims and get somebody to talk.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from dismissing officers and are earned through completing signals.</color>
Even the Fleet of Rams are after the Yaot pilgrim's supposed treasure. If we hope to protect them, we must first convince somebody to give us more information. We should try to make friends with the pilgrims and get somebody to talk.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from dismissing officers and are earned through completing signals.</color>
	* Type:	Event
	* EventId:	event_yaotSpring_2024_t3
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Insignia_T3up;Amount&50;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_yaoSpr_2024_day09_t3: After talking to Chocoan we suspect there is more to the Yaot pilgrimage than the religious travels to astral conjunction events. We might be able to get more information from the Yaot Federation if we do some favors.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
After talking to Chocoan we suspect there is more to the Yaot pilgrimage than the religious travels to astral conjunction events. We might be able to get more information from the Yaot Federation if we do some favors.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
	* Type:	Event
	* EventId:	event_yaotSpring_2024_t3
	* Goals:	CompleteQuest,0
	* GoalParameters:	Amount&5;Tags&Faction_Yaot_T3up

### qe_yaoSpr_2024_day10_t3: We’ve reached a dead end on collecting intelligence on the Yaot, but our source within the Tanoch Empire has offered to provide more information. We should bring an adequate gift for compensation.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
We’ve reached a dead end on collecting intelligence on the Yaot, but our source within the Tanoch Empire has offered to provide more information. We should bring an adequate gift for compensation.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
	* Type:	Event
	* EventId:	event_yaotSpring_2024_t3
	* Goals:	Pay,0
	* GoalParameters:	Id&questItem_progenitorRelic_t3;Amount&1

### qe_yaoSpr_2024_day11_t3: While we still don't know what kind of treasure the pilgrims could have aboard their vessels, Chocoan wants to move on to another astral conjunction event. He has requested our assistance in clearing out the area from any hostile threats.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
While we still don't know what kind of treasure the pilgrims could have aboard their vessels, Chocoan wants to move on to another astral conjunction event. He has requested our assistance in clearing out the area from any hostile threats.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
	* Type:	Event
	* EventId:	event_yaotSpring_2024_t3
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&1;Tags&Epic_T3up;Mode&Generated

### qe_yaoSpr_2024_day12_t3: The report on the pilgrim's procedure has been fully analyzed. Usually the pilgrim's convoy moves in a tight line formation towards the optimal conjunction points where they perform their religious rituals. However, a few ships regularly diverge from the common path and move into nearby asteroid fields. We should investigate the latest conjunction site and see if we can find anything of interest.

<color=#FBB03F>Ore can be mined from asteroids in asteroid fields. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
The report on the pilgrim's procedure has been fully analyzed. Usually the pilgrim's convoy moves in a tight line formation towards the optimal conjunction points where they perform their religious rituals. However, a few ships regularly diverge from the common path and move into nearby asteroid fields. We should investigate the latest conjunction site and see if we can find anything of interest.

<color=#FBB03F>Ore can be mined from asteroids in asteroid fields. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
	* Type:	Event
	* EventId:	event_yaotSpring_2024_t3
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Asteroid_Crud_T3up;Amount&1400;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_yaoSpr_2024_day13_t3: Chocoan has informed us that the next astral conjunction site will be inside the Cangacian territories. We convinced him to take part in the operation ourselves to ensure security in this hostile area of the Empty Quarter. Maybe we will be able to both protect the pilgrims and find out more about the suspected secret agenda. We should make sure the crew is properly prepared and ready for any eventualities.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
Chocoan has informed us that the next astral conjunction site will be inside the Cangacian territories. We convinced him to take part in the operation ourselves to ensure security in this hostile area of the Empty Quarter. Maybe we will be able to both protect the pilgrims and find out more about the suspected secret agenda. We should make sure the crew is properly prepared and ready for any eventualities.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
	* Type:	Event
	* EventId:	event_yaotSpring_2024_t3
	* Goals:	UpgradeOfficer,0
	* GoalParameters:	Amount&3

### qe_yaoSpr_2024_day14_t3: Chocoan has provided the coordinates to the next astral conjunction event. Strong hostile forces are to be expected in this system. Our goal is to both protect the civilian pilgrims and find out more about the suspected secret agenda of the Yaot Elders.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
Chocoan has provided the coordinates to the next astral conjunction event. Strong hostile forces are to be expected in this system. Our goal is to both protect the civilian pilgrims and find out more about the suspected secret agenda of the Yaot Elders.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
	* Type:	Event
	* EventId:	event_yaotSpring_2024_t3
	* Goals:	CompleteMission,0
	* GoalParameters:	Id&event_yaoSpr2024_Conjunction_t3

## ql_event_YaotSpring_2024_t4

### qe_yaoSpr_2024_day01_t4: There are rumors circulating in the Empty Quarter about an increase in Cangacian pirate activity. Fleet Command asks us to gather intel from our contacts with the Iyatequa traders. We should gain some favors to bargain for information.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
There are rumors circulating in the Empty Quarter about an increase in Cangacian pirate activity. Fleet Command asks us to gather intel from our contacts with the Iyatequa traders. We should gain some favors to bargain for information.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
	* Type:	Event
	* EventId:	event_yaotSpring_2024_t4
	* Goals:	CompleteQuest,0
	* GoalParameters:	Amount&5;Tags&Faction_Tr1_T4up

### qe_yaoSpr_2024_day02_t4: The Iyatequa traders are involved with pirates attacking Yaot pilgrims in the Empty Quarter. We might get more information through selling equipment and arms on the open market.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
The Iyatequa traders are involved with pirates attacking Yaot pilgrims in the Empty Quarter. We might get more information through selling equipment and arms on the open market.

<color=#FBB03F>Items and resources can be sold for credits in the market at stations.</color>
	* Type:	Event
	* EventId:	event_yaotSpring_2024_t4
	* Goals:	GainItem,0
	* GoalParameters:	Id&CR;Amount&10000;ExcludedSources&BuyItem_QuestReward_MissionReward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer

### qe_yaoSpr_2024_day03_t4: To learn more about the pirate raids, we should get in contact with the Yaot pilgrims. They appear to be hiding after recent attacks. We have no other option than to perform reconnaissance in the nearby systems.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
To learn more about the pirate raids, we should get in contact with the Yaot pilgrims. They appear to be hiding after recent attacks. We have no other option than to perform reconnaissance in the nearby systems.

<color=#FBB03F>Scannable objects, such as signals, can be found through scanning. A better or upgraded sensor module increases the chances of success.</color>
	* Type:	Event
	* EventId:	event_yaotSpring_2024_t4
	* Goals:	Scan,0
	* GoalParameters:	Tags&InSystem_T4up;Amount&5;Analyzed&True

### qe_yaoSpr_2024_day04_t4: In our search for the Yaot pilgrims we have encountered intense pirate activity. We should hunt down some of their ships and see if we can gather any additional clues.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
In our search for the Yaot pilgrims we have encountered intense pirate activity. We should hunt down some of their ships and see if we can gather any additional clues.

<color=#FBB03F>When you destroy an enemy vessel, there is a chance that you will gain salvage from that ship. This salvage can be opened in your storage for additional rewards.</color>
	* Type:	Event
	* EventId:	event_yaotSpring_2024_t4
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Salvage_T4up;Amount&5;ExcludedSources&MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_OpenContainer

### qe_yaoSpr_2024_day05_t4: Some Yaot survivors in our medical ward are ready to be questioned. If we manage to prove our good intentions they might help us find the Yaot pilgrimage.

<color=#FBB03F>Prestige is earned through each player level-up and by completing daily and weekly assignments.</color>
Some Yaot survivors in our medical ward are ready to be questioned. If we manage to prove our good intentions they might help us find the Yaot pilgrimage.

<color=#FBB03F>Prestige is earned through each player level-up and by completing daily and weekly assignments.</color>
	* Type:	Event
	* EventId:	event_yaotSpring_2024_t4
	* Goals:	GainItem,0
	* GoalParameters:	Id&LP;Amount&10;ExcludedSources&BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_DismissOfficer_OpenContainer_ClaimMail_DismantleItem

### qe_yaoSpr_2024_day06_t4: The Yaot have accepted our offer to support their pilgrimage. Requests have come in from ships needing spares and replacement parts for repairs. If we provide these, we might learn more about why the pirates are after these ships.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
The Yaot have accepted our offer to support their pilgrimage. Requests have come in from ships needing spares and replacement parts for repairs. If we provide these, we might learn more about why the pirates are after these ships.

<color=#FBB03F>Parts are needed to craft most items, such as ships and modules, in T2 and higher. Except for the Tier 2 ones, parts are fabricated from the previous Tier.</color>
	* Type:	Event
	* EventId:	event_yaotSpring_2024_t4
	* Goals:	Craft,0
	* GoalParameters:	Category&Crafting;Tags&Part_T4up;Amount&100

### qe_yaoSpr_2024_day07_t4: Even though pirates are still swarming the area, Chocoan and the Yaot pilgrims are adamant about continuing their travels to see the astral conjunction events. In order to deter any further attacks on the civilian ships, we should patrol and clear the systems of any significant hostile forces.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
Even though pirates are still swarming the area, Chocoan and the Yaot pilgrims are adamant about continuing their travels to see the astral conjunction events. In order to deter any further attacks on the civilian ships, we should patrol and clear the systems of any significant hostile forces.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
	* Type:	Event
	* EventId:	event_yaotSpring_2024_t4
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&1;Tags&Epic_T4up;Mode&Generated

### qe_yaoSpr_2024_day08_t4: Even the Fleet of Rams are after the Yaot pilgrim's supposed treasure. If we hope to protect them, we must first convince somebody to give us more information. We should try to make friends with the pilgrims and get somebody to talk.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from dismissing officers and are earned through completing signals.</color>
Even the Fleet of Rams are after the Yaot pilgrim's supposed treasure. If we hope to protect them, we must first convince somebody to give us more information. We should try to make friends with the pilgrims and get somebody to talk.

<color=#FBB03F>Insignias are used to level up and promote officers. They can be gained from dismissing officers and are earned through completing signals.</color>
	* Type:	Event
	* EventId:	event_yaotSpring_2024_t4
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Insignia_T4up;Amount&50;ExcludedSources&SellItem_BuyItem_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_yaoSpr_2024_day09_t4: After talking to Chocoan we suspect there is more to the Yaot pilgrimage than the religious travels to astral conjunction events. We might be able to get more information from the Yaot Federation if we do some favors.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
After talking to Chocoan we suspect there is more to the Yaot pilgrimage than the religious travels to astral conjunction events. We might be able to get more information from the Yaot Federation if we do some favors.

<color=#FBB03F>Completing liaison assignments for a faction increases your reputation level for that faction. Liaison assignments are posted in the liaison office.</color>
	* Type:	Event
	* EventId:	event_yaotSpring_2024_t4
	* Goals:	CompleteQuest,0
	* GoalParameters:	Amount&5;Tags&Faction_Yaot_T4up

### qe_yaoSpr_2024_day10_t4: We’ve reached a dead end on collecting intelligence on the Yaot, but our source within the Tanoch Empire has offered to provide more information. We should bring an adequate gift for compensation.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
We’ve reached a dead end on collecting intelligence on the Yaot, but our source within the Tanoch Empire has offered to provide more information. We should bring an adequate gift for compensation.

<color=#FBB03F>Progenitor relics can be found in relic signature signals.</color>
	* Type:	Event
	* EventId:	event_yaotSpring_2024_t4
	* Goals:	Pay,0
	* GoalParameters:	Id&questItem_progenitorRelic_t4;Amount&1

### qe_yaoSpr_2024_day11_t4: While we still don't know what kind of treasure the pilgrims could have aboard their vessels, Chocoan wants to move on to another astral conjunction event. He has requested our assistance in clearing out the area from any hostile threats.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
While we still don't know what kind of treasure the pilgrims could have aboard their vessels, Chocoan wants to move on to another astral conjunction event. He has requested our assistance in clearing out the area from any hostile threats.

<color=#FBB03F>Signals of higher rarities are hard to find and the enemies are much stronger, but the rewards are better than that of regular signals.</color>
	* Type:	Event
	* EventId:	event_yaotSpring_2024_t4
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&1;Tags&Epic_T4up;Mode&Generated

### qe_yaoSpr_2024_day12_t4: The report on the pilgrim's procedure has been fully analyzed. Usually the pilgrim's convoy moves in a tight line formation towards the optimal conjunction points where they perform their religious rituals. However, a few ships regularly diverge from the common path and move into nearby asteroid fields. We should investigate the latest conjunction site and see if we can find anything of interest.

<color=#FBB03F>Ore can be mined from asteroids in asteroid fields. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
The report on the pilgrim's procedure has been fully analyzed. Usually the pilgrim's convoy moves in a tight line formation towards the optimal conjunction points where they perform their religious rituals. However, a few ships regularly diverge from the common path and move into nearby asteroid fields. We should investigate the latest conjunction site and see if we can find anything of interest.

<color=#FBB03F>Ore can be mined from asteroids in asteroid fields. Collectors of a lower tier than the asteroids they are mining will yield less ore.</color>
	* Type:	Event
	* EventId:	event_yaotSpring_2024_t4
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Asteroid_Crud_T4up;Amount&1600;ExcludedSources&PayGoal_QuestReward_MissionReward_BuyItem_SellItem_OpenContainer_ClaimMail_DismantleItem_LevelUpPlayer_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

### qe_yaoSpr_2024_day13_t4: Chocoan has informed us that the next astral conjunction site will be inside the Cangacian territories. We convinced him to take part in the operation ourselves to ensure security in this hostile area of the Empty Quarter. Maybe we will be able to both protect the pilgrims and find out more about the suspected secret agenda. We should make sure the crew is properly prepared and ready for any eventualities.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
Chocoan has informed us that the next astral conjunction site will be inside the Cangacian territories. We convinced him to take part in the operation ourselves to ensure security in this hostile area of the Empty Quarter. Maybe we will be able to both protect the pilgrims and find out more about the suspected secret agenda. We should make sure the crew is properly prepared and ready for any eventualities.

<color=#FBB03F>Each officer level increases an attribute of that officer by a certain amount. When an officer reaches a new rank, their skill increases or they might even gain a second skill.</color>
	* Type:	Event
	* EventId:	event_yaotSpring_2024_t4
	* Goals:	UpgradeOfficer,0
	* GoalParameters:	Amount&5

### qe_yaoSpr_2024_day14_t4: Chocoan has provided the coordinates to the next astral conjunction event. Strong hostile forces are to be expected in this system. Our goal is to both protect the civilian pilgrims and find out more about the suspected secret agenda of the Yaot Elders.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
Chocoan has provided the coordinates to the next astral conjunction event. Strong hostile forces are to be expected in this system. Our goal is to both protect the civilian pilgrims and find out more about the suspected secret agenda of the Yaot Elders.

<color=#FBB03F>This mission can be played in a party. Invite your friends to help you if you are struggling with it. To create a party, open the social panel in the upper right corner. Then tap on the fourth tab from the top on the right.</color>
	* Type:	Event
	* EventId:	event_yaotSpring_2024_t4
	* Goals:	CompleteMission,0
	* GoalParameters:	Id&event_yaoSpr2024_Conjunction_t4

## ql_test

### qt_001: No header for quest qt_001
No description for quest qt_001
	* Type:	Side
	* MailsOnCompletion:	m_qt_001
	* Goals:	Pay,0, Pay,0
	* GoalParameters:	Id&1A;Amount&500, Id&1B;Amount&250

## ql_test2

### qt_002: No header for quest qt_002
No description for quest qt_002
	* Type:	Side
	* Goals:	CompleteMission,0
	* GoalParameters:	Ids&story_A02_WiracodaGate|story_A03_GulfTaln

## ql_test3

### qt_003: No header for quest qt_003
No description for quest qt_003
	* Type:	Side
	* Goals:	GainItem,0
	* GoalParameters:	Id&CR;Amount&100;ExcludedSources&Shop_Reward_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash

## ql_test4

### qt_004: No header for quest qt_004
No description for quest qt_004
	* Type:	Side
	* Goals:	CompleteMission,0
	* GoalParameters:	Amount&3;Mode&Faction;Tags&Tanoch_T3up

## ql_testQuestDialog

### qm_testQuestDialog: No header for quest qm_testQuestDialog
No description for quest qm_testQuestDialog
	* Type:	Main
	* Goals:	Goto,0, Goto,1, Goto,2, Goto,2
	* GoalParameters:	Target&[-1785, -690], Target&[-1844, -690], Target&[-1785, -690], Target&[-1844, -690]

## ql_testDismissOfficers

### qt_testDismissOfficers: No header for quest qt_testDismissOfficers
No description for quest qt_testDismissOfficers
	* Type:	Side
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Insignia;Amount&1;ExcludedSources&OpenContainer_QuestReward_MissionReward_ClaimMail_MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_BuyItem_SellItem

## ql_test_strike_13

### qt_test_strike_13: No header for quest qt_test_strike_13
No description for quest qt_test_strike_13
	* Type:	Main
	* Goals:	CompleteQuest,0
	* GoalParameters:	Ids&qr_013

## ql_test_strike_16

### qt_test_strike_16: No header for quest qt_test_strike_16
No description for quest qt_test_strike_16
	* Type:	Main
	* Goals:	CompleteQuest,0
	* GoalParameters:	Ids&qr_016

## ql_test_strike_14

### qt_test_strike_14: No header for quest qt_test_strike_14
No description for quest qt_test_strike_14
	* Type:	Main
	* Goals:	CompleteQuest,0
	* GoalParameters:	Ids&qr_014

## ql_test_strike_17

### qt_test_strike_17: No header for quest qt_test_strike_17
No description for quest qt_test_strike_17
	* Type:	Main
	* Goals:	CompleteQuest,0
	* GoalParameters:	Ids&qr_017

## ql_test_strike_21

### qt_test_strike_21: No header for quest qt_test_strike_21
No description for quest qt_test_strike_21
	* Type:	Main
	* Goals:	CompleteQuest,0
	* GoalParameters:	Ids&qr_021

## ql_test_strike_15

### qt_test_strike_15: No header for quest qt_test_strike_15
No description for quest qt_test_strike_15
	* Type:	Main
	* Goals:	CompleteQuest,0
	* GoalParameters:	Ids&qr_015

## ql_test_strike_18

### qt_test_strike_18: No header for quest qt_test_strike_18
No description for quest qt_test_strike_18
	* Type:	Main
	* Goals:	CompleteQuest,0
	* GoalParameters:	Ids&qr_018

## ql_test_strike_22

### qt_test_strike_22: No header for quest qt_test_strike_22
No description for quest qt_test_strike_22
	* Type:	Main
	* Goals:	CompleteQuest,0
	* GoalParameters:	Ids&qr_022

## ql_test_strike_19

### qt_test_strike_19: No header for quest qt_test_strike_19
No description for quest qt_test_strike_19
	* Type:	Main
	* Goals:	CompleteQuest,0
	* GoalParameters:	Ids&qr_019

## ql_test_strike_20

### qt_test_strike_20: No header for quest qt_test_strike_20
No description for quest qt_test_strike_20
	* Type:	Main
	* Goals:	CompleteQuest,0
	* GoalParameters:	Ids&qr_020

## ql_a_001

### qa_001: No header for quest qa_001
No description for quest qa_001
	* Type:	Achievement
	* Goals:	Statistic,0
	* GoalParameters:	Id&Mined1A;Total&3000

### qa_002: No header for quest qa_002
No description for quest qa_002
	* Type:	Achievement
	* Goals:	Statistic,0
	* GoalParameters:	Id&Upgrade;Amount&5

## ql_test_ggf_story

### qs_s2_01_sijinLighthouse: Sijin Lighthouse
We detected a possible signal from the missing Khar-Kalaad.
	* Type:	Side
	* FollowUps:	ql_raid_019
	* Goals:	CompleteMission,0
	* GoalParameters:	Id&story_D01_SijinLighthouse

### qs_s2_01_iliyinLighthouse: Iliyin Lighthouse
We have arrived at another lighthouse in uncharted territory. Be prepared for anything.
	* Type:	Side
	* Goals:	CompleteMission,0
	* GoalParameters:	Id&story_D02_IliyinLighthouse

### qs_s2_01_bTemple: Bright Temple
The Amassari here may have answers about the nature of the Progenitor observer.
	* Type:	Side
	* Goals:	CompleteMission,0
	* GoalParameters:	Id&story_D03_BrightTemple

### qs_s2_01_hataldan: Hataldan
The fallen capital of the Amassari, and last known position of the Observer.
	* Type:	Side
	* FollowUps:	ql_raid_020
	* Goals:	CompleteMission,0
	* GoalParameters:	Id&story_D04_Hataldan

## ql_compensation_lvlup

### q_compensation_lvl_10: Fame and Honor (Lvl 10)
Player XP can be gained from completing missions and assignments and from destroying enemy units.
	* Type:	Event
	* EventId:	event_levelUpCompensationQuests
	* Goals:	Statistic,0
	* GoalParameters:	Id&PlayerXP;Total&12600

### q_compensation_lvl_20: Fame and Honor (Lvl 20)
Player XP can be gained from completing missions and assignments and from destroying enemy units.
	* Type:	Event
	* EventId:	event_levelUpCompensationQuests
	* Goals:	Statistic,0
	* GoalParameters:	Id&PlayerXP;Total&36100

### q_compensation_lvl_35: Fame and Honor (Lvl 35)
Player XP can be gained from completing missions and assignments and from destroying enemy units.
	* Type:	Event
	* EventId:	event_levelUpCompensationQuests
	* Goals:	Statistic,0
	* GoalParameters:	Id&PlayerXP;Total&90100

### q_compensation_lvl_50: Fame and Honor (Lvl 50)
Player XP can be gained from completing missions and assignments and from destroying enemy units.
	* Type:	Event
	* EventId:	event_levelUpCompensationQuests
	* Goals:	Statistic,0
	* GoalParameters:	Id&PlayerXP;Total&166600

### q_compensation_lvl_75: Fame and Honor (Lvl 75)
Player XP can be gained from completing missions and assignments and from destroying enemy units.
	* Type:	Event
	* EventId:	event_levelUpCompensationQuests
	* Goals:	Statistic,0
	* GoalParameters:	Id&PlayerXP;Total&344100

### q_compensation_lvl_100: Fame and Honor (Lvl 100)
Player XP can be gained from completing missions and assignments and from destroying enemy units.
	* Type:	Event
	* EventId:	event_levelUpCompensationQuests
	* Goals:	Statistic,0
	* GoalParameters:	Id&PlayerXP;Total&584100

### q_compensation_lvl_150: Fame and Honor (Lvl 150)
Player XP can be gained from completing missions and assignments and from destroying enemy units.
	* Type:	Event
	* EventId:	event_levelUpCompensationQuests
	* Goals:	Statistic,0
	* GoalParameters:	Id&PlayerXP;Total&1251600

### q_compensation_lvl_200: Fame and Honor (Lvl 200)
Player XP can be gained from completing missions and assignments and from destroying enemy units.
	* Type:	Event
	* EventId:	event_levelUpCompensationQuests
	* Goals:	Statistic,0
	* GoalParameters:	Id&PlayerXP;Total&2169100

### q_compensation_lvl_300: Fame and Honor (Lvl 300)
Player XP can be gained from completing missions and assignments and from destroying enemy units.
	* Type:	Event
	* EventId:	event_levelUpCompensationQuests
	* Goals:	Statistic,0
	* GoalParameters:	Id&PlayerXP;Total&4754100

## q_test_yao_spring

### q_test_yaoSpr_2024_day04_t4: No header for quest q_test_yaoSpr_2024_day04_t4
No description for quest q_test_yaoSpr_2024_day04_t4
	* Type:	Side
	* Goals:	GainItem,0
	* GoalParameters:	Tags&Salvage_T4up;Amount&5;ExcludedSources&MoveToUser_RemoveFromInventory_MoveToStash_RetrieveFromStash_OpenContainer
