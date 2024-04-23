from flask import Flask, render_template, request, redirect, url_for
import sqlite3

# local vars
# ===========================================================================================================
app = Flask(__name__)
db_url = "database.db"
chara_table_name = "characterCfg"
tool_table_name = "itemCollectionCfg"
actor_table_name = "actorTechnology"
buff_table_name = "buff"
passive_table_name = "passiveSkill"
active_table_name = "activeSkill"
aim_table_name = "aimTable"
skill_table_name = "skillDamageTable"

# helper funcs
# ===========================================================================================================

# routing
# ===========================================================================================================

# 0) home
# ----------------------------------------------------------------------------------------------------------
@app.route("/", methods=["GET"])
def main():
    
    return render_template("home.html")

# 1) characters
# ----------------------------------------------------------------------------------------------------------
@app.route("/characters", methods=["GET"])
def characters():
    if request.method == "GET":
        with sqlite3.connect(db_url) as conn:
            cur = conn.cursor()
            cur.execute('SELECT * FROM ' + chara_table_name + " ORDER BY chara_id ASC")
            chara_data = cur.fetchall()
    
        return render_template("chara_main.html", dataset=chara_data)
    
@app.route("/chara_add", methods=["GET"])
def chara_add():
    if request.method == "GET":
        char_id = request.args.get("id")
        char_data = []
        if char_id == 'null':
            with sqlite3.connect(db_url) as con:
                cur = con.cursor()
                cur.execute('SELECT * FROM ' + chara_table_name + " ORDER BY chara_id DESC LIMIT 1")
                res = cur.fetchone()
                if not res:
                    res = [-1]
                char_data =  [str(int(res[0])+1), "", "", "", "", "", "", "", "", "", ""]
                
        else:
            with sqlite3.connect(db_url) as con:
                cur = con.cursor()
                cur.execute('SELECT * FROM ' + chara_table_name + " WHERE chara_id = " + char_id)
                char_data = cur.fetchone()
                

        # fetch the data of  the chara
        res_data = []
        for i in range(11):
            res_data.append(char_data[i])
        

        return render_template("chara_add.html", metadata=res_data)

@app.route("/chara_mod", methods=["POST"])
def chara_mod():
    if request.method == "POST":
        res = request.form
        dct = res.to_dict()
        #print(res)
        
        with sqlite3.connect(db_url) as con:
            #try:
                cur = con.cursor()
                # delete
                cur.execute("DELETE FROM " + chara_table_name + " WHERE chara_id = " + str(dct["id"]))
                

                # insert
                insert_data = "(" + dct['id'] + ", '" + dct['race'] + "', '" + dct['name'] + "', '" + dct['avatar'] + "', '" + dct['lihui'] + "', '" + dct['danju'] +  "', " + dct['hp'] + ", " + dct['atk'] + ", " + dct['spd'] + ", " + dct['rarity'] + ", " + dct["frag"] + ")"  
                cur.execute("INSERT INTO " + chara_table_name + " VALUES " + insert_data)

                con.commit()
            #except:
            #    con.rollback()

        # check if data alr in db
        return redirect(url_for("characters"))
    
@app.route("/chara_del", methods=["POST"])
def chara_del():
    if request.method == 'POST':
        char_id = request.args.get("id")
        with sqlite3.connect(db_url) as con:
                cur = con.cursor()
                cur.execute('DELETE FROM ' + chara_table_name + " WHERE chara_id = " + char_id)
                con.commit()
        
        return redirect(url_for('characters'))

# 2) tools
# ----------------------------------------------------------------------------------------------------------
@app.route("/tools", methods=["GET"])
def tools():
    if request.method == "GET":
        with sqlite3.connect(db_url) as conn:
            cur = conn.cursor()
            cur.execute('SELECT * FROM ' + tool_table_name + ' ORDER BY item_id ASC')
            tool_data = cur.fetchall()
    
        return render_template("tool_main.html", dataset=tool_data)
    
@app.route("/tool_add", methods=["GET"])
def tool_add():
    if request.method == "GET":
        tool_id = request.args.get("id")
        tool_data = []
        if tool_id == 'null':
            with sqlite3.connect(db_url) as con:
                cur = con.cursor()
                cur.execute('SELECT * FROM ' + tool_table_name + " ORDER BY item_id DESC LIMIT 1")
                res = cur.fetchone()
                if not res:
                    res = [-1]
                tool_data =  [str(int(res[0])+1), "", "", ""]
                
        else:
            with sqlite3.connect(db_url) as con:
                cur = con.cursor()
                cur.execute('SELECT * FROM ' + tool_table_name + " WHERE item_id = " + tool_id)
                tool_data = cur.fetchone()
                

        # fetch the data of  the chara
        res_data = []
        for i in range(4):
            res_data.append(tool_data[i])
        

        return render_template("tool_add.html", metadata=res_data)

@app.route("/tool_mod", methods=["POST"])
def tool_mod():
    if request.method == "POST":
        res = request.form
        dct = res.to_dict()
        #print(res)
        
        with sqlite3.connect(db_url) as con:
            #try:
                cur = con.cursor()
                # delete
                cur.execute("DELETE FROM " + tool_table_name + " WHERE item_id = " + str(dct["id"]))
                

                # insert
                insert_data = "(" + dct['id'] + ", '" + dct['name'] + "', '" + dct['item_desc'] + "', '" + dct['item_url'] + "')"  
                cur.execute("INSERT INTO " + tool_table_name + " VALUES " + insert_data)

                con.commit()
            #except:
            #    con.rollback()

        # check if data alr in db
        return redirect(url_for("tools"))
    
@app.route("/tool_del", methods=["POST"])
def tool_del():
    if request.method == 'POST':
        tool_id = request.args.get("id")
        with sqlite3.connect(db_url) as con:
                cur = con.cursor()
                cur.execute('DELETE FROM ' + tool_table_name + " WHERE item_id = " + tool_id)
                con.commit()
        
        return redirect(url_for('tools'))

# 3) actorTech
# ----------------------------------------------------------------------------------------------------------
@app.route("/actors", methods=["GET"])
def actors():
    if request.method == "GET":
        with sqlite3.connect(db_url) as conn:
            cur = conn.cursor()
            cur.execute('SELECT * FROM ' + actor_table_name + ' ORDER BY skill_id ASC')
            tool_data = cur.fetchall()
    
        return render_template("actor_main.html", dataset=tool_data)
    
@app.route("/actor_add", methods=["GET"])
def actor_add():
    if request.method == "GET":
        actor_id = request.args.get("id")
        actor_data = []
        if actor_id == 'null':
            with sqlite3.connect(db_url) as con:
                cur = con.cursor()
                cur.execute('SELECT * FROM ' + actor_table_name + " ORDER BY skill_id DESC LIMIT 1")
                res = cur.fetchone()
                if not res:
                    res = [-1]
                actor_data =  ["", "", "", "", "", str(int(res[0])+1)]
                
        else:
            with sqlite3.connect(db_url) as con:
                cur = con.cursor()
                cur.execute('SELECT * FROM ' + actor_table_name + " WHERE skill_id = " + actor_id)
                actor_data = cur.fetchone()
                

        # fetch the data of  the chara
        res_data = []
        for i in range(6):
            res_data.append(actor_data[i])
        

        return render_template("actor_add.html", metadata=res_data)

@app.route("/actor_mod", methods=["POST"])
def actor_mod():
    if request.method == "POST":
        res = request.form
        dct = res.to_dict()
        #print(res)
        
        with sqlite3.connect(db_url) as con:
            #try:
                cur = con.cursor()
                # delete
                cur.execute("DELETE FROM " + actor_table_name + " WHERE skill_id = " + str(dct["skill_id"]))
                

                # insert
                insert_data = "(" + dct['chara_id'] + ", " + dct['rarity'] + ", " + dct['skill_slot'] + ", " + dct['upgrade_id'] + ", " + dct['upgrade_cost'] + ", " + dct['skill_id'] + ")"  
                cur.execute("INSERT INTO " + actor_table_name + " VALUES " + insert_data)

                con.commit()
            #except:
            #    con.rollback()

        # check if data alr in db
        return redirect(url_for("actors"))
    
@app.route("/actor_del", methods=["POST"])
def actor_del():
    if request.method == 'POST':
        skill_id = request.args.get("id")
        with sqlite3.connect(db_url) as con:
                cur = con.cursor()
                cur.execute('DELETE FROM ' + actor_table_name + " WHERE skill_id = " + skill_id)
                con.commit()
        
        return redirect(url_for('actors'))
    


# 4) buff
# ----------------------------------------------------------------------------------------------------------
@app.route("/buffs", methods=["GET"])
def buffs():
    if request.method == "GET":
        with sqlite3.connect(db_url) as conn:
            cur = conn.cursor()
            cur.execute('SELECT * FROM ' + buff_table_name + ' ORDER BY buff_id ASC')
            buff_data = cur.fetchall()
    
        return render_template("buff_main.html", dataset=buff_data)
    
@app.route("/buff_add", methods=["GET"])
def buff_add():
    if request.method == "GET":
        buff_id = request.args.get("id")
        buff_data = []
        print("buff ID: " + buff_id)
        if buff_id == 'null':
            with sqlite3.connect(db_url) as con:
                cur = con.cursor()
                cur.execute('SELECT * FROM ' + buff_table_name + " ORDER BY buff_id DESC LIMIT 1")
                res = cur.fetchone()
                if not res:
                    res = [-1]
                buff_data =  [str(int(res[0])+1), "", "", "", "", ""]
                
        else:
            with sqlite3.connect(db_url) as con:
                cur = con.cursor()
                cur.execute('SELECT * FROM ' + buff_table_name + " WHERE buff_id = " + buff_id)
                buff_data = cur.fetchone()
                

        # fetch the data of  the chara
        res_data = []
        for i in range(6):
            res_data.append(buff_data[i])
        

        return render_template("buff_add.html", metadata=res_data)

@app.route("/buff_mod", methods=["POST"])
def buff_mod():
    if request.method == "POST":
        res = request.form
        dct = res.to_dict()
        #print(res)
        
        with sqlite3.connect(db_url) as con:
            #try:
                cur = con.cursor()
                # delete
                cur.execute("DELETE FROM " + buff_table_name + " WHERE buff_id = " + str(dct["buff_id"]))
                

                # insert
                insert_data = "(" + dct['buff_id'] + ", '" + dct['buff_name'] + "', '" + dct['file_addr'] + "', " + dct['duration'] + ", " + dct['target_limit'] + ", '" + dct['effect_type']+"')"  
                cur.execute("INSERT INTO " + buff_table_name + " VALUES " + insert_data)

                con.commit()
            #except:
            #    con.rollback()

        # check if data alr in db
        return redirect(url_for("buffs"))
    
@app.route("/buff_del", methods=["POST"])
def buff_del():
    if request.method == 'POST':
        buff_id = request.args.get("id")
        with sqlite3.connect(db_url) as con:
                cur = con.cursor()
                cur.execute('DELETE FROM ' + buff_table_name + " WHERE buff_id = " + buff_id)
                con.commit()
        
        return redirect(url_for('buffs'))
    

# 5) passive
# ----------------------------------------------------------------------------------------------------------
@app.route("/passive", methods=["GET"])
def passive():
    if request.method == "GET":
        with sqlite3.connect(db_url) as conn:
            cur = conn.cursor()
            cur.execute('SELECT * FROM ' + passive_table_name + ' ORDER BY passive_id ASC')
            passive_data = cur.fetchall()
    
        return render_template("passive_main.html", dataset=passive_data)
    
@app.route("/passive_add", methods=["GET"])
def passive_add():
    if request.method == "GET":
        passive_id = request.args.get("id")
        passive_data = []
        if passive_id == 'null':
            with sqlite3.connect(db_url) as con:
                cur = con.cursor()
                cur.execute('SELECT * FROM ' + passive_table_name + " ORDER BY passive_id DESC LIMIT 1")
                
                res = cur.fetchone()
                if not res:
                    res = [-1]
                passive_data =  [str(int(res[0])+1), "", "", "", "", "", "", "", "", "", "", ""]
                
        else:
            with sqlite3.connect(db_url) as con:
                cur = con.cursor()
                cur.execute('SELECT * FROM ' + passive_table_name + " WHERE passive_id = " + passive_id)
                passive_data = cur.fetchone()
                

        # fetch the data of  the chara
        res_data = []
        for i in range(12):
            res_data.append(passive_data[i])
        

        return render_template("passive_add.html", metadata=res_data)

@app.route("/passive_mod", methods=["POST"])
def passive_mod():
    if request.method == "POST":
        res = request.form
        dct = res.to_dict()
        #print(res)
        
        with sqlite3.connect(db_url) as con:
            #try:
                cur = con.cursor()
                # delete
                cur.execute("DELETE FROM " + passive_table_name + " WHERE passive_id = " + str(dct["passive_id"]))
                

                # insert
                insert_data = "(" + dct['passive_id'] + ", '" + dct['passive_name'] + "', '" + dct['trigger'] + "', " + dct['cd'] +  ", '" + dct['usage_target'] + "', "  + dct['trigger_chance'] + ", " + dct['buff_id_one'] + ", " + dct['buff_one_trigger'] + ", " + dct['buff_id_two'] + ", " + dct['buff_two_trigger'] + ", " + dct['buff_id_three'] + ", " + dct['buff_three_trigger'] + ")"  
                #print(insert_data)
                cur.execute("INSERT INTO " + passive_table_name + " VALUES " + insert_data)

                con.commit()
            #except:
            #    con.rollback()

        # check if data alr in db
        return redirect(url_for("passive"))
    
@app.route("/passive_del", methods=["POST"])
def passive_del():
    if request.method == 'POST':
        passive_id = request.args.get("id")
        with sqlite3.connect(db_url) as con:
                cur = con.cursor()
                cur.execute('DELETE FROM ' + passive_table_name + " WHERE passive_id = " + passive_id)
                con.commit()
        
        return redirect(url_for('passive'))
    

# 6) active
# ----------------------------------------------------------------------------------------------------------
@app.route("/active", methods=["GET"])
def active():
    if request.method == "GET":
        with sqlite3.connect(db_url) as conn:
            cur = conn.cursor()
            cur.execute('SELECT * FROM ' + active_table_name + ' ORDER BY active_id ASC')
            active_data = cur.fetchall()
    
        return render_template("active_main.html", dataset=active_data)
    
@app.route("/active_add", methods=["GET"])
def active_add():
    if request.method == "GET":
        active_id = request.args.get("id")
        active_data = []
        if active_id == 'null':
            with sqlite3.connect(db_url) as con:
                cur = con.cursor()
                cur.execute('SELECT * FROM ' + active_table_name + " ORDER BY active_id DESC LIMIT 1")
                res = cur.fetchone()
                if not res:
                    res = [-1]
                active_data =  [str(int(res[0])+1), "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",  "", ""]
                
        else:
            with sqlite3.connect(db_url) as con:
                cur = con.cursor()
                cur.execute('SELECT * FROM ' + active_table_name + " WHERE active_id = " + active_id)
                active_data = cur.fetchone()
                

        # fetch the data of  the chara
        res_data = []
        for i in range(19):
            res_data.append(active_data[i])
        

        return render_template("active_add.html", metadata=res_data)

@app.route("/active_mod", methods=["POST"])
def active_mod():
    if request.method == "POST":
        res = request.form
        dct = res.to_dict()
        #print(res)
        
        with sqlite3.connect(db_url) as con:
            #try:
                cur = con.cursor()
                # delete
                cur.execute("DELETE FROM " + active_table_name + " WHERE active_id = " + str(dct["active_id"]))
                

                # insert
                insert_data = ""

                insert_data += "(" + dct['active_id'] + ", '" + dct['active_name'] + "', '" + dct['skill_url'] + "', '" + dct['release_method'] + "', " + dct['aim_id'] + ", '" + dct['active_file_addr'] + "', " + dct['cd'] + ", "
                insert_data += dct['buff_id_one'] + ", " + dct['buff_one_trigger'] + ", " + dct['buff_id_two'] + ", " + dct['buff_two_trigger'] + ", " + dct['buff_id_three'] + ", " + dct['buff_three_trigger'] + ", "
                insert_data += dct['skill_eff_one_rate'] + ", " + dct['skill_one_id'] + ", " + dct['skill_eff_two_rate'] + ", " + dct['skill_two_id'] + ", " + dct['skill_eff_three_rate'] + ", " + dct['skill_three_id'] + ") "
                print(insert_data)
                cur.execute("INSERT INTO " + active_table_name + " VALUES " + insert_data)

                con.commit()
            #except:
            #    con.rollback()

        # check if data alr in db
        return redirect(url_for("active"))
    
@app.route("/active_del", methods=["POST"])
def active_del():
    if request.method == 'POST':
        active_id = request.args.get("id")
        with sqlite3.connect(db_url) as con:
                cur = con.cursor()
                cur.execute('DELETE FROM ' + active_table_name + " WHERE active_id = " + active_id)
                con.commit()
        
        return redirect(url_for('active'))
    

# 7) aim table
# ----------------------------------------------------------------------------------------------------------
@app.route("/aim", methods=["GET"])
def aim():
    if request.method == "GET":
        with sqlite3.connect(db_url) as conn:
            cur = conn.cursor()
            cur.execute('SELECT * FROM ' + aim_table_name + ' ORDER BY aim_id ASC')
            aim_data = cur.fetchall()
    
        return render_template("aim_main.html", dataset=aim_data)
    
@app.route("/aim_add", methods=["GET"])
def aim_add():
    if request.method == "GET":
        aim_id = request.args.get("id")
        aim_data = []
        if aim_id == 'null':
            with sqlite3.connect(db_url) as con:
                cur = con.cursor()
                cur.execute('SELECT * FROM ' + aim_table_name + " ORDER BY aim_id DESC LIMIT 1")
                res = cur.fetchone()
                if not res:
                    res = [-1]
                aim_data =  [str(int(res[0])+1), "", "", "", ""]
                
        else:
            with sqlite3.connect(db_url) as con:
                cur = con.cursor()
                cur.execute('SELECT * FROM ' + aim_table_name + " WHERE aim_id = " + aim_id)
                aim_data = cur.fetchone()
                

        # fetch the data of  the chara
        res_data = []
        for i in range(5):
            res_data.append(aim_data[i])
        

        return render_template("aim_add.html", metadata=res_data)

@app.route("/aim_mod", methods=["POST"])
def aim_mod():
    if request.method == "POST":
        res = request.form
        dct = res.to_dict()
        #print(res)
        
        with sqlite3.connect(db_url) as con:
            #try:
                cur = con.cursor()
                # delete
                cur.execute("DELETE FROM " + aim_table_name + " WHERE aim_id = " + str(dct["aim_id"]))
                

                # insert
                insert_data = "(" + dct['aim_id'] + ", " + dct['aim_range'] + ", " + dct['show_wire'] + ", " + dct['search_teammates'] + ", " + dct['ignore_block'] + ")"
                cur.execute("INSERT INTO " + aim_table_name + " VALUES " + insert_data)

                con.commit()
            #except:
            #    con.rollback()

        # check if data alr in db
        return redirect(url_for("aim"))
    
@app.route("/aim_del", methods=["POST"])
def aim_del():
    if request.method == 'POST':
        aim_id = request.args.get("id")
        with sqlite3.connect(db_url) as con:
                cur = con.cursor()
                cur.execute('DELETE FROM ' + aim_table_name + " WHERE aim_id = " + aim_id)
                con.commit()
        
        return redirect(url_for('aim'))



# 8) skill dmg table
# ----------------------------------------------------------------------------------------------------------
@app.route("/skill", methods=["GET"])
def skill():
    if request.method == "GET":
        with sqlite3.connect(db_url) as conn:
            cur = conn.cursor()
            cur.execute('SELECT * FROM ' + skill_table_name + ' ORDER BY skillDmg_id ASC')
            skill_data = cur.fetchall()
    
        return render_template("skill_main.html", dataset=skill_data)
    
@app.route("/skill_add", methods=["GET"])
def skill_add():
    if request.method == "GET":
        skill_id = request.args.get("id")
        skill_data = []
        if skill_id == 'null':
            with sqlite3.connect(db_url) as con:
                cur = con.cursor()
                cur.execute('SELECT * FROM ' + skill_table_name + " ORDER BY skillDmg_id DESC LIMIT 1")
                res = cur.fetchone()
                if not res:
                    res = [-1]
                skill_data =  [str(int(res[0])+1), "", "", ""]
                
        else:
            with sqlite3.connect(db_url) as con:
                cur = con.cursor()
                cur.execute('SELECT * FROM ' + skill_table_name + " WHERE skillDmg_id = " + skill_id)
                skill_data = cur.fetchone()
                

        # fetch the data of  the chara
        res_data = []
        for i in range(4):
            res_data.append(skill_data[i])
        

        return render_template("skill_add.html", metadata=res_data)

@app.route("/skill_mod", methods=["POST"])
def skill_mod():
    if request.method == "POST":
        res = request.form
        dct = res.to_dict()
        #print(res)
        
        with sqlite3.connect(db_url) as con:
            #try:
                cur = con.cursor()
                # delete
                cur.execute("DELETE FROM " + skill_table_name + " WHERE skillDmg_id = " + str(dct["skillDmg_id"]))
                

                # insert
                insert_data = "(" + dct['skillDmg_id'] + ", '" + dct['skillDmg_name'] + "', " + dct['dmg'] + ", '" + dct['sfx_addr'] + "')"
                cur.execute("INSERT INTO " + skill_table_name + " VALUES " + insert_data)

                con.commit()
            #except:
            #    con.rollback()

        # check if data alr in db
        return redirect(url_for("skill"))
    
@app.route("/skill_del", methods=["POST"])
def skill_del():
    if request.method == 'POST':
        skill_id = request.args.get("id")
        with sqlite3.connect(db_url) as con:
                cur = con.cursor()
                cur.execute('DELETE FROM ' + skill_table_name + " WHERE skillDmg_id = " + skill_id)
                con.commit()
        
        return redirect(url_for('skill'))


# run webapp
# ===========================================================================================================
if __name__ == "__main__":
    app.run()