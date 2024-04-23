import sqlite3

#Open database
conn = sqlite3.connect('csc3170/database.db')

#conn.execute('''DROP TABLE characterCfg''')


# create character
conn.execute(''' CREATE TABLE characterCfg
        (chara_id INTEGER PRIMARY KEY,
        race VARCHAR(255),
        chara_name VARCHAR(255),
        avatar VARCHAR(1024),
        lihui VARCHAR(255),
        danju VARCHAR(255),
        hp INT,
        atk INT,
        spd INT,
        rarity INT,
        fragment_id INT
        
        )''')


conn.execute(''' 
INSERT INTO characterCfg 
VALUES
             (0, "Fire", "Politis", '/static/pic/demo_pic/chara/politis.jpeg', 'C:/xxx', 'C:/yyy', 6969, 690, 108, 5, 2),
             (1, "Ice", "Diene", '/static/pic/demo_pic/chara/diene.jpeg', 'C:/xxx', 'C:/zzz', 5400, 1000, 114, 5, 3),
             (2, "Ice", "Angelica", '/static/pic/demo_pic/chara/angelica.jpeg', 'C:/xxx', 'C:/axe', 7469, 900, 125, 4, 4)
''')


# create tool
conn.execute(''' CREATE TABLE itemCollectionCfg
        (       
                item_id INT PRIMARY KEY,
                item_name VARCHAR(255),
                item_desc VARCHAR(1024),
                item_url VARCHAR(512)
        
        )''')


conn.execute(''' 
INSERT INTO itemCollectionCfg
VALUES
             (0, "pickaxe", "a pickaxe. ", "/static/pic/demo_pic/pickaxe.png"),
             (1, "axe", "now this is an axe. you use it to cut tree. ", "/static/pic/demo_pic/axe.png")
''')

# create actor tech
conn.execute(''' CREATE TABLE actorTechnology
        (       
                chara_id INT,
                rarity INT,
                skill_slot INT,
                upgrade_id INT,
                upgrade_cost INT,
                skill_id INT PRIMARY KEY
        
        )''')


conn.execute(''' 
INSERT INTO actorTechnology 
VALUES
             (0, 5, 6, 1, 0, 0),
             (1, 5, 2, 3, 4, 1)
''')

# create buff
conn.execute(''' CREATE TABLE buff
        (       
                buff_id INT PRIMARY KEY,
                buff_name VARCHAR(50),
                file_addr VARCHAR(512),
                duration INT,
                target_limit INT,
                effect_type VARCHAR(50)
        
        )''')


conn.execute(''' 
INSERT INTO buff
VALUES
             (0, "continuous heal", "C:/xxx/xxx", 5, 1, "heal"),
             (1, "attack up", "C:/xyx/xyz", 7, 2, "offense"),
             (2, "defense_up", "C:/aaa/bbb", 4, 3, "defense")
''')

# create passive
conn.execute(''' CREATE TABLE passiveSkill
        (       
                passive_id INT PRIMARY KEY,
                passive_name VARCHAR(50),
                trigger VARCHAR(512),
                cd INT,
                usage_target VARCHAR(256),
                trigger_chance INT,
                buff_id_one INT,
                buff_one_trigger INT,
                buff_id_two INT,
                buff_two_trigger INT,
                buff_id_three INT,
                buff_three_trigger INT
        
        )''')


conn.execute(''' 
INSERT INTO passiveSkill
VALUES
             (0, "ultimate_skill", "???", 5, "all", 75, 0, 25, 1, 50, 2, 30)
''')


# create active
conn.execute(''' CREATE TABLE activeSkill
        (       
                active_id INT PRIMARY KEY,
                active_name VARCHAR(50),
                skill_url VARCHAR(512),
                release_method VARCHAR(50),
                aim_id INT,
                active_file_addr VARCHAR(512),
                cd INT,
                buff_id_one INT,
                buff_one_trigger INT,
                buff_id_two INT,
                buff_two_trigger INT,
                buff_id_three INT,
                buff_three_trigger INT,
                skill_eff_one_rate INT,
                skill_one_id INT,
                skill_eff_two_rate INT,
                skill_two_id INT,
                skill_eff_three_rate INT,
                skill_three_id INT
        
        )''')


conn.execute(''' 
INSERT INTO activeSkill
VALUES
             (0, "attack attack", "http://sss.com/aaa", "???", 0, "C:/xxx/aa", 3, 0, 10, 1, 25, 2, 50, 75, 0, 50, 1, 100, 2)
''')


# create aim table
conn.execute(''' CREATE TABLE aimTable
        (       
                aim_id INT PRIMARY KEY,
                aim_range INT,
                show_wire INT,
                search_teammates INT,
                ignore_block INT
        
        )''')


conn.execute(''' 
INSERT INTO aimTable
VALUES
             (0, 25, 1, 0, 1),
             (1, 30, 1, 1, 1),
             (2, 45, 1, 1, 1)
''')

# create skill dmg table
conn.execute(''' CREATE TABLE skillDamageTable
        (       
                skilldmg_id INT PRIMARY KEY,
                skilldmg_name VARCHAR(255),
                dmg INT,
                sfx_addr VARCHAR(512)
        
        )''')


conn.execute(''' 
INSERT INTO skillDamageTable
VALUES
             (0, "normal hit", 100, "C:/aaa/bbb"),
             (1, "moderate hit", 150, "C:/baa/bbb"),
             (2, "notable hit", 250, "C:/acc/bbb"),
             (3, "serious hit", 1000000000, "C:/aassa/bbb")
            
''')


conn.commit()