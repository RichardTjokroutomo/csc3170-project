import sqlite3

#Open database
conn = sqlite3.connect('database.db')

#conn.execute('''DROP TABLE characterCfg''')


## CREATE TABLES
# ============================================================================================================

# create character
conn.execute('DROP TABLE IF EXISTS characterCfg;')
conn.execute(''' CREATE TABLE characterCfg
        (chara_id INTEGER PRIMARY KEY,
        race INT, -- CHANGED
        chara_name VARCHAR(50),
        avatar VARCHAR(255),
        lihui VARCHAR(255),
        danju VARCHAR(255),
        hp INT,
        atk INT,
        spd INT,
        rarity INT,
        fragment_id INT
        
        )''')


# create tool
conn.execute('DROP TABLE IF EXISTS itemCollectionCfg;')
conn.execute(''' CREATE TABLE itemCollectionCfg
        (       
                item_id INT PRIMARY KEY,
                item_name VARCHAR(255),
                item_desc VARCHAR(255),
                item_url VARCHAR(255)
        
        )''')



# create actor tech
conn.execute('DROP TABLE IF EXISTS actorTechnology;')
conn.execute(''' CREATE TABLE actorTechnology
        (       
                chara_id INT,
                rarity INT,
                skill_slot INT,
                upgrade_id INT,
                upgrade_cost INT,
                skill_id INT 
        
        )''')



# create buff
conn.execute('DROP TABLE IF EXISTS buff;')
conn.execute(''' CREATE TABLE buff
        (       
                buff_id INT PRIMARY KEY,
                buff_name VARCHAR(255),
                file_addr VARCHAR(255),
                duration INT,
                target_limit INT,
                effect_type INT -- CHANGED
        
        )''')


# create passive
conn.execute('DROP TABLE IF EXISTS passiveSkill;')
conn.execute(''' CREATE TABLE passiveSkill
        (       
                passive_id INT,
                passive_name VARCHAR(255),
                trigger INT, -- CHANGED
                cd INT,
                usage_target INT, -- CHANGED
                trigger_chance INT,
                buff_id_one INT,
                buff_one_trigger INT,
                buff_id_two INT,
                buff_two_trigger INT,
                buff_id_three INT,
                buff_three_trigger INT
        
        )''')



# create active
conn.execute('DROP TABLE IF EXISTS activeSkill;')
conn.execute(''' CREATE TABLE activeSkill
        (       
                active_id INT PRIMARY KEY,
                active_name VARCHAR(255),
                skill_url VARCHAR(255),
                skill_slot INT, -- ADDED
                release_method INT, -- CHANGED
                aim_id INT,
                active_file_addr VARCHAR(255),
                cd INT,  -- 7
                buff_one_name VARCHAR(255), -- ADDED
                buff_id_one INT,
                buff_one_trigger INT,  -- 10
                buff_two_name VARCHAR(255), -- ADDED
                buff_id_two INT,
                buff_two_trigger INT,  -- 13
                buff_three_name VARCHAR(255), -- ADDED
                buff_id_three INT,
                buff_three_trigger INT,  -- 16
                eff_one_name VARCHAR(255), -- ADDED
                skill_eff_one_rate INT,  -- 18
                skill_one_id INT,
                eff_two_name VARCHAR(255), -- ADDED
                skill_eff_two_rate INT,  -- 21
                skill_two_id INT,
                eff_three_name VARCHAR(255), -- ADDED
                skill_eff_three_rate INT,  -- 24
                skill_three_id INT
        
        )''')




# create aim table
conn.execute('DROP TABLE IF EXISTS aimTable;')
conn.execute(''' CREATE TABLE aimTable
        (       
                aim_id INT PRIMARY KEY,
                aim_range INT,
                show_wire INT,
                search_teammates INT,
                ignore_block INT
        
        )''')

# create skill dmg table
conn.execute('DROP TABLE IF EXISTS skillDamageTable;')
conn.execute(''' CREATE TABLE skillDamageTable
        (       
                skilldmg_id INT PRIMARY KEY,
                skilldmg_name VARCHAR(255),
                dmg INT,
                sfx_addr VARCHAR(255)
        
        )''')

conn.commit()





## INSERT DATA
# ============================================================================================================


conn.execute('''INSERT INTO actorTechnology VALUES
(1, 3, 1, 21000001, 500, 16103001),
(1, 3, 2, 21000001, 500, 16100101),
(1, 3, 3, 21000001, 1000, 66007001),
(1, 3, 4, 21000002, 2, 66008001),
(2, 2, 1, 21000001, 450, 17103001),
(2, 2, 2, 21000001, 450, 17100101),
(2, 2, 3, 21000001, 900, 67007001),
(2, 2, 4, 21000002, 2, 67008001),
(3, 4, 1, 21000001, 550, 18103001),
(3, 4, 2, 21000001, 550, 18100101),
(3, 4, 3, 21000001, 1100, 68007001),
(3, 4, 4, 21000002, 3, 68008001),
(4, 1, 1, 21000001, 400, 19103001),
(4, 1, 2, 21000001, 400, 19100101),
(4, 1, 3, 21000001, 800, 69007001),
(4, 1, 4, 21000002, 1, 69008001),
(5, 5, 1, 21000001, 600, 20103001),
(5, 5, 2, 21000001, 600, 20100101),
(5, 5, 3, 21000001, 1200, 70007001),
(5, 5, 4, 21000002, 4, 70008001),
(6, 3, 1, 21000001, 500, 21103001),
(6, 3, 2, 21000001, 500, 21100101),
(6, 3, 3, 21000001, 1000, 71007001),
(6, 3, 4, 21000002, 2, 71008001);''')


conn.execute('''Insert INTO activeSkill  VALUES
(16103001, 'Explosive Missile', 'UT_ID_MemberSkill/Udarnik_Spitfire_4', 1, 0, 61030, 'AGEAction/Player/Skill/Udarnik_1', 5000, 'Vulnerability', 1000, 160010010, NULL, NULL, NULL, NULL, NULL, NULL, 'Spiral Missile Damage', 1000, 161030010, NULL, NULL, NULL, NULL, NULL, NULL),
(16100101, 'Grenade', 'UT_ID_MemberSkill/Udarnik_Spitfire_1', 2, 1, 61031, 'AGEAction/Player/Skill/Udarnik_2', 7000, 'Dizziness', 1000, 160010011, NULL, NULL, NULL, NULL, NULL, NULL, 'Grenade Damage', 1000, 161030011, NULL, NULL, NULL, NULL, NULL, NULL),
(17103001, 'Wrath of Nature', 'UT_ID_MemberSkill/Ranger_WrathfulNature_4', 1, 0, 61030, 'AGEAction/Player/Skill/Ranger_1', 5000, 'Vulnerability', 1000, 160010010, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(17100101, 'Arrow Rain', 'UT_ID_MemberSkill/Ranger_ArrowRain_1', 2, 1, 61031, 'AGEAction/Player/Skill/Ranger_2', 7000, 'Forest Shelter', 1000, 160010014, NULL, NULL, NULL, NULL, NULL, NULL, 'Arrow Rain Damage', 1000, 161030013, NULL, NULL, NULL, NULL, NULL, NULL),
(18103001, 'Brutal Charge', 'UT_ID_MemberSkill/Berserker_Rushing_4', 1, 0, 61031, 'AGEAction/Player/Skill/Berserker_1', 5000, 'Beastial Fury', 1000, 160010015, 'Silence', 1000, 160010031, NULL, NULL, NULL, 'Charge Damage', 1000, 161030014, NULL, NULL, NULL, NULL, NULL, NULL),
(18100101, 'Whirlwind Slash', 'UT_ID_MemberSkill/Berserker_Whirlwind_1', 2, 1, 61030, 'AGEAction/Player/Skill/Berserker_2', 7000, 'Attack Enhancement', 1000, '160010022', NULL, NULL, NULL, NULL, NULL, NULL, 'Whirlwind Slash Damage', 1000, 161030015, NULL, NULL, NULL, NULL, NULL, NULL),
(19103001, 'Magma Eruption', 'UT_ID_MemberSkill/Tinker_Magma_4', 1, 0, 61030, 'AGEAction/Player/Skill/Tinker_1', 5000, 'Burning', 1000, 160010026, 'Dwarven Resilience',  1000, 160010016, NULL, NULL, NULL, 'Lava Damage', 1000, 161030016, NULL, NULL, NULL, NULL, NULL, NULL),
(19100101, 'Mechanical Guard', 'UT_ID_MemberSkill/Tinker_MachineElf_1', 2, 1, 61031, 'AGEAction/Player/Skill/Tinker_2',	7000, 'Dizziness', 1000, 160010011, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(20103001,	'Electromagnetic Pulse', 'UT_ID_MemberSkill/Scout_EMP_4', 1, 0, 61031, 'AGEAction/Player/Skill/Scout_1', 5000, 'Dizziness', 1000, 160010011, 'Mechanical Invisibility', 1000, 160010017, NULL, NULL, NULL, 'Electromagnetic Pulse Damage', 1000, 161030017, NULL, NULL, NULL, NULL, NULL, NULL),
(20100101, 'Stealth', 'UT_ID_MemberSkill/Scout_Stealth_1', 2, 1, 61030, 'AGEAction/Player/Skill/Scout_2', 7000, 'Invisibility',	1000, 160010030, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(21103001, 'Plague Outbreak', 'UT_ID_MemberSkill/Necromancer_Plague_4', 1, 0, 61031, 'AGEAction/Player/Skill/Necromancer_1', 10000, 'Poisoning', 1000, 160010025, 'Magic Immunity', 1000, 160010024, NULL, NULL, NULL, 'Poison Damage', 1000, 161030018, NULL, NULL, NULL, NULL, NULL, NULL),
(21100101, 'Summon the Dead', 'UT_ID_MemberSkill/Necromancer_Summon_1', 2, 1, 61030, 'AGEAction/Player/Skill/Necromancer_2', 15000, 'Necromancy Summon', 1000, 160010018, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
''')

conn.execute('''INSERT INTO buff VALUES
(160010010, 'Vulnerability', 'AGEAction/Player/Buff/Udarnik_1_Yishang', 3500, 1, 2),
(160010011, 'Dizziness', 'AGEAction/Player/Buff/Udarnik_2_Xuanyun', 1000, 1, 2),
(160010012, 'Damage Reduction', 'AGEAction/Player/Buff/Udarnik_3_Jianshang', -1, 3, 1),
(160010013, 'Increased Fire Rate', 'AGEAction/Player/Buff/Udarnik_4_Shesu', 1000, 3, 1),
(160010014, 'Forest Shelter', 'AGEAction/Player/Buff/ForestGuard_Protection', 3000, 2, 1),
(160010015, 'Beastial Fury', 'AGEAction/Player/Buff/OrcWarrior_Rage', 5000, 3, 1),
(160010016, 'Dwarven Resilience', 'AGEAction/Player/Buff/DwarfCraftsman_Resilience', 8000, 3, 1),
(160010017, 'Mechanical Invisibility', 'AGEAction/Player/Buff/MechScout_Invis', 1500, 3, 1),
(160010018, 'Necromancer Summoning', 'AGEAction/Player/Buff/ZombieSummon', 2000, 4, 3),
(160010019, 'Force Shield', 'AGEAction/Player/Buff/ForceField', -1, 2, 1),
(160010020, 'Speed Boost', 'AGEAction/Player/Buff/SpeedBoost', 2000, 3, 1),
(160010021, 'Health Regeneration', 'AGEAction/Player/Buff/HealthRegen', 5000, 2, 1),
(160010022, 'Attack Enhancement', 'AGEAction/Player/Buff/AttackEnhancement', 3000, 3, 1),
(160010023, 'Shield', 'AGEAction/Player/Buff/Shield', 3000, 2, 1),
(160010024, 'Magic Immunity', 'AGEAction/Player/Buff/MagicImmunity', 1000, 3, 1),
(160010025, 'Poisoning', 'AGEAction/Player/Debuff/Poison', 4000, 1, 2),
(160010026, 'Burning', 'AGEAction/Player/Debuff/Burning', 3000, 1, 2),
(160010027, 'Freezing', 'AGEAction/Player/Debuff/Freeze', 1500, 1, 2),
(160010028, 'Fear', 'AGEAction/Player/Debuff/Fear', 2000, 1, 2),
(160010029, 'Weakening', 'AGEAction/Player/Debuff/Weakening', 3000, 1, 2),
(160010030, 'Invisibility', 'AGEAction/Player/Status/Invisibility', 2500, 3, 3),
(160010031, 'Silence', 'AGEAction/Player/Status/Silence', 2000, 1, 3);
''')

conn.execute('''INSERT INTO aimTable  VALUES
(61030, 20, 1, 0, 0),
(61031, 10, 0, 0, 0);
''')

conn.execute('''INSERT INTO characterCfg  VALUES
(1, 1, 'Blaster', 'Arthub/Player/MemberHead_1', 'Arthub/Player/Body_1', 'Arthub/Player/Skin_1', 100, 90, 80, 3, 24500175),
(2, 4, 'Forest Guardian', 'Arthub/Player/MemberHead_2', 'Arthub/Player/Body_2', 'Arthub/Player/Skin_2', 120, 70, 60, 2, 24500176),
(3, 5, 'Orc Warrior', 'Arthub/Player/MemberHead_3', 'Arthub/Player/Body_3', 'Arthub/Player/Skin_3', 150, 110, 50, 4, 24500177),
(4, 3, 'Dwarf Artisan', 'Arthub/Player/MemberHead_4', 'Arthub/Player/Body_4', 'Arthub/Player/Skin_4', 90, 60, 40, 1, 24500178),
(5, 2, 'Mechanical Scout', 'Arthub/Player/MemberHead_5', 'Arthub/Player/Body_5', 'Arthub/Player/Skin_5', 80, 100, 100, 5, 24500179),
(6, 6, 'Zombie Sorcerer', 'Arthub/Player/MemberHead_6', 'Arthub/Player/Body_6', 'Arthub/Player/Skin_6', 130, 80, 30, 3, 24500180);
''')

conn.execute('''INSERT INTO itemCollectionCfg  VALUES
(24500175,	'Blaster Activation Card',	'Hero activation card, used to activate the Blaster.',	'Arthub/Item/Card_1'),
(24500176,	'Forest Guardian Activation Card', 'Hero activation card, used to activate the Forest Guardian.', 'Arthub/Item/Card_2'),
(24500177,	' Orc Warrior Activation Card',	'Hero activation card, used to activate the Orc Warrior.', 'Arthub/Item/Card_3'),
(24500178,	'Dwarf Artisan Activation Card', 'Hero activation card, used to activate the Dwarf Artisan.', 'Arthub/Item/Card_4'),
(24500179,	'Mechanical Scout Activation Card',	'Hero activation card, used to activate the Mechanical Scout.', 'Arthub/Item/Card_5'),
(24500180,	'Zombie Sorcerer Activation Card', 'Hero activation card, used to activate the Zombie Sorcerer.', 'Arthub/Item/Card_6'),
(21000001,	'Gold Coin', 'Common currency made of precious metal, with a long history.', 'Arthub/Item/Coin'),
(21000002,	'Diamond',	'Precious stones, crystal clear.', 'Arthub/Item/Diamond');
''')

conn.execute('''INSERT INTO passiveSkill VALUES
(66007001, 'Permanent Damage Reduction', 6, -1, 1, 1000, 160010012, 0, 0, 0, 0, 0),
(66008001, 'Increased Fire Rate When Switching Weapons', 5, 2000, 1, 1000, 160010013, 0, 0, 0, 0, 0),
(67007001, 'Archery Mastery', 6, -1, 1, 1000, 160010013, 0, 0, 0, 0, 0),
(67008001, 'Natural Affinity', 6, 7500, 1, 1000, 160010024, 0, 0, 0, 0, 0),
(68007001, 'Barbaric Strength', 6,	-1,	1, 1000, 160010012, 0, 0, 0, 0, 0),
(68008001, 'Bloodlust', 2, 5000, 1, 1000, 160010021, 0, 0, 0, 0, 0),
(69007001, 'Dwarven Bloodline', 6, 8000, 1, 1000, 160010019, 0, 0, 0, 0, 0),
(69008001, 'Mechanical Affinity', 6, 12000, 1, 1000, 160010017, 0, 0, 0, 0, 0),
(70007001, ' Mechanical Body', 6, 10000, 1, 1000, 160010023, 0, 0, 0, 0, 0),
(70008001, 'Scouting Mastery', 6, 7000, 2, 1000, 160010020, 0, 0, 0, 0, 0),
(71007001, 'Affinity with the Dead', 6, 7000, 3, 1000, 160010029, 0, 0, 0, 0, 0),
(71008001, 'Heart of the Undead', 6, 7000, 3, 1000, 160010028, 0, 0, 0, 0, 0);
''')

conn.execute('''INSERT INTO skillDamageTable VALUES
(161030010,	'Spiral Missile Damage', 'ageaction/hitaction/Udarnik_1_Hit', 500),
(161030011,	'Grenade Damage',	'ageaction/hitaction/Udarnik_2_Hit', 900),
(161030012,	'Explosive Burning Damage', 'ageaction/hitaction/Udarnik_3_Hit', 400),
(161030013,	'Arrow Rain Damage', 'ageaction/hitaction/Udarnik_4_Hit', 700),
(161030014,	'Imapct Damage',	'ageaction/hitaction/Udarnik_5_Hit', 600),
(161030015,	'Whirlwind Slash Damage', 'ageaction/hitaction/Udarnik_6_Hit', 800),
(161030016,	'Lava Damage', 'ageaction/hitaction/Udarnik_7_Hit', 600),
(161030017,	'Electromagnetic Pulse Damage', 'ageaction/hitaction/Udarnik_8_Hit', 500),
(161030018,	'Poison Damage', 'ageaction/hitaction/Udarnik_9_Hit', 500);
''')
conn.commit()


