from flask import Flask, redirect, url_for, render_template, request
from characters import Character, skeleton, wraith, goblin, end
import random
import csv
import json
import psycopg2
import os

DB_host =  os.environ.get('DB_host')
DB_user = os.environ.get('DB_user')
DB_password = os.environ.get('DB_password')
DB_name= os.environ.get('DB_name')

app = Flask(__name__)

hero = Character(0,"Empty", True, 1, 1, 1, 1, 1, 1, 1, 1, 0)
userid = 0
lvldict = {"lvl0": 0, "lvl1":1, 'lvl2': 300, 'lvl3': 1000, 'lvl4':2000, 'lvl5':5000,'lvl6':8000,'lvl7':12000}
enemylist = [skeleton, goblin, wraith, end]
enemyline = 0
enemy = enemylist[enemyline]
combatmessage = ''

def write_to_db(data):
    conn = psycopg2.connect(dbname=DB_name, user=DB_user, password=DB_password, host=DB_host)
    cur = conn.cursor()
    cur.execute("SELECT * FROM players;")
    db_users = cur.fetchall()
    userid = (len(db_users))
    print(userid)
    username = data["username"]
    password = data["password"]
    useralive = True
    userhp = 30
    userac = 6
    userxp = 1
    userlvl = 1
    userammo = 6
    userstr = (random.randint(3, 18))
    userdex = (random.randint(3, 18))
    usercon = (random.randint(3, 18))
    userpotion = 5
    cur.execute("""
    INSERT INTO players (username, password, userid, useralive, userhp, userac, userxp, userlvl, userammo,userstr,userdex,usercon,userpotion)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);
    """,
    (username, password, userid, useralive, userhp, userac, userxp, userlvl, userammo, userstr, userdex, usercon, userpotion))
    conn.commit()
    global hero
    hero = Character(userid, username, useralive, userhp, userac, userxp, userlvl, userammo, userstr, userdex, usercon, userpotion)
    cur.close()
    conn.close()


def checkregistry(data):
    conn = psycopg2.connect(dbname=DB_name, user=DB_user, password=DB_password, host=DB_host)
    cur = conn.cursor()
    cur.execute("SELECT * FROM players;")
    db_users = cur.fetchall()
    isin = False
    for i in db_users:
        if data["username"] and data["password"] in i:
            isin = True
            break
        else:
            isin = False
    if isin == False:
        cur.close()
        conn.close()
        write_to_db(data)
        print("wrote to file")

    else:
        print('pre-exisiting name and password. Attempting to route to Sign In Page')
        signin()
            # break


def signinfunc(data):
    print('signinfunc')
    conn = psycopg2.connect(dbname=DB_name, user=DB_user, password=DB_password, host=DB_host)
    cur = conn.cursor()
    cur.execute("SELECT * FROM players;")
    db_users = cur.fetchall()
    isin = False
    for i in db_users:
        if data["username"] and data["password"] in i:
            global hero
            test=(json.dumps(i))
            test2 = json.loads(test)
            print(test2)
            hero = Character(test2[2],test2[2],test2[6],test2[7],test2[8],test2[9],test2[10],test2[11],test2[12],test2[13],test2[14],test2[15])
            isin = True
        else:
            print("not found")
    if isin == False:
        return render_template("characternotfound.html")
    else:
        return render_template('character.html', name=hero.name, hero=hero)




@app.route("/", methods=["POST", "GET"])
def signin():
    return render_template("signin.html")

@app.route('/characternotfound', methods=["POST","GET"])
def characternotfound():
    return render_template("characternotfound.html")

@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        checkregistry(data)
        return render_template('character.html', name=hero.name, hero=hero)
    else:
        return 'something went wrong'


@app.route("/signcheck", methods=["POST", "GET"])
def signcheck():
    if request.method == 'POST':
        global data
        data = request.form.to_dict()
        print(data)
        return signinfunc(data)
    else:
        return 'something went wrong. Check if method was POST.'





@app.route("/index", methods=["POST", "GET"])
def home():
    return render_template("index.html")

@app.route("/character", methods=["POST", "GET"])
def character():
    return render_template("character.html", name = hero.name, hero=hero)

@app.route('/arena', methods=["POST", "GET"])
def arena():
    while enemy.alive == True and hero.alive == True:
        # enemyattack
        strike = (random.randint(1, 20))
        if strike < hero.ac:
            combatmessage = "The enemy attacks but barely misses!"
            break
        else:
            e1damage = (random.randint(1, 8))
            hero.hp -= e1damage
            combatmessage = (f"\nThe enemy hits you for {e1damage} damage! ")
            if hero.hp <= 0:
                hero.alive = False
                return render_template("dead.html")
                break
            else:
                break
    if enemy.name == 'Wraith':
        if enemy.alive == False:
            return render_template("gameover.html")
    else:
        pass
    return render_template("arena.html", enemy= enemy, hero=hero, combatmessage=combatmessage)

@app.route('/Wraith', methods=["POST", "GET"])
def wraithfight():
    global enemy
    enemy = wraith
    while enemy.alive == True and hero.alive == True:
        attacktyperoll = (random.randint(1, 10))
        if attacktyperoll <= 5:
            strike = (random.randint(1, 20))
            if strike < hero.ac:
                combatmessage = "The beast slashes with it's claws but barely misses!"
                break
            else:
                e1damage = (random.randint(1, 8))
                hero.hp -= e1damage
                combatmessage = (f"\nThe beast's claws hit you for {e1damage} damage! ")
                if hero.hp <= 0:
                    hero.alive = False
                    return render_template("dead.html", combatmessage = combatmessage)
                    break
                else:
                    break

    if enemy.name == 'Wraith':
        if enemy.alive == False:
            return render_template("gameover.html")
    else:
        pass

    return render_template("Wraith.html", enemy= enemy, hero=hero, combatmessage=combatmessage)

@app.route('/Goblin', methods=["POST", "GET"])
def goblinfight():
    global enemy
    enemy = goblin
    while enemy.alive == True and hero.alive == True:
        attacktyperoll = (random.randint(1, 10))
        if attacktyperoll <= 5:
            strike = (random.randint(1, 20))
            if strike < hero.ac:
                combatmessage = "The Goblin slashes with it's claws but barely misses!"
                break
            else:
                e1damage = (random.randint(1, 8))
                hero.hp -= e1damage
                combatmessage = (f"\nThe Goblins claws hit you for {e1damage} damage! ")
                if hero.hp <= 0:
                    hero.alive = False
                    return render_template("dead.html", combatmessage = combatmessage)
                    break
                else:
                    break
        else:
            stealstrike = (random.randint(1, 23))
            if stealstrike < hero.dex:
                combatmessage = "The little bugger goes for your pockets but misses!"
                break
            else:
                hero.potion -= 1
                goblin.hp += (random.randint(1, 10))
                combatmessage = (f"\nThe Goblin steals a potion and gulps it down! ")

    if enemy.name == 'Goblin':
        if enemy.alive == False:
            return render_template("enemydead.html", enemy= enemy, hero=hero, combatmessage=combatmessage)
    else:
        pass

    return render_template("Goblin.html", enemy= enemy, hero=hero, combatmessage=combatmessage)


@app.route('/arenadagger', methods=["POST", "GET"])
def arenadagger():
        # my attack
    global enemy
    global enemyline
    while enemy.alive == True and hero.alive == True:
        ha = (random.randint(1, 18))
        if ha < enemy.ac:
            heromessage = "You missed!"
            break
        else:
            dagger_damage = (random.randint(1, 8))
            enemy.hp -= dagger_damage
            heromessage = (f"You hit the beast for {dagger_damage} damage!")
            if enemy.hp < 0:
                enemy.alive = False
                hero.xp += enemy.xp
                if hero.xp >= lvldict[f"lvl{hero.lvl + 1}"]:
                    hero.lvlup()
                    heromessage = (f"\nYour enmey falls to the dust. The crowd chants the\nname of their champion: {hero.name}!"
                                   f"\nYou've leveled up! You are now level {hero.lvl}".upper())
                else:
                    heromessage = (f"\nYour enmey falls to the dust. The crowd chants the\nname of their champion: {hero.name}!".upper())
                    pass
                heromessage= (f"\nYour enmey falls to the dust. The crowd chants the\nname of their champion: {hero.name}!".upper())
                enemyline += 1
                enemy = enemylist[enemyline]
                return render_template("enemydead.html", heromessage=heromessage, enemy= enemy, hero=hero)
            else:
                break
    return render_template("arenadagger.html", heromessage=heromessage, enemy= enemy, hero=hero)

@app.route('/arenastone', methods=["POST", "GET"])
def arenastone():
    global enemy
    global enemyline
    while enemy.alive == True and hero.alive == True:
        if hero.ammo<=0:
            heromessage = ("You are out of stones!")
            break
        else:
            ha = (random.randint(1,19))
            hero.ammo -= 1
            ammomessage = (f"\nYou now have {hero.ammo} stones left!")
            if ha < enemy.ac:
              heromessage = "You missed!"
              break
            else:
                stone_damage = (random.randint(1,8))
                enemy.hp -= stone_damage
                heromessage = (f"\nYour stone sails true for {stone_damage} damage!")
                if enemy.hp < 0:
                    enemy.alive = False
                    hero.xp += enemy.xp
                    if hero.xp >= lvldict[f"lvl{hero.lvl + 1}"]:
                        hero.lvlup()
                        heromessage = (f"\nThe stone lands and the enemy falls to the dust. The crowd chants the\nname of their champion: {hero.name}!"
                                       f"\nYou've leveled up! You are now level {hero.lvl}".upper())

                    else:
                        heromessage = (f"\nThe stone lands and your enemy falls to the dust. The crowd chants the\nname of their champion: {hero.name}!".upper())
                        pass
                    enemyline += 1
                    enemy = enemylist[enemyline]
                    return render_template("enemydead.html", heromessage=heromessage, enemy= enemy, hero=hero)
                else:
                    break
    return render_template("arenastone.html" ,heromessage=heromessage, enemy= enemy, hero=hero, ammomessage=ammomessage )

@app.route("/arenapotion", methods=["POST","GET"])
def drinkpotion():
    if hero.potion >= 1:
        potion = (random.randint(1, 10))
        hero.hp += potion
        hero.potion -= 1
        heromessage = (f"\nYou drink deeply of the healing vial and recieve {potion} hit points!")
    else:
        heromessage = ("You are out of potions!")
    return render_template("arenapotion.html", heromessage=heromessage, hero=hero, enemy=enemy)


@app.route("/enemydead", methods=["POST","GET"])
def enemydead():
    return render_template("enemydead.html",heromessage = heromessage, enemy = enemy, hero = hero, ammomessage=ammomessage)

@app.route("/dead", methods=["POST","GET"])
def dead():
    return render_template("dead.html",heromessage = heromessage, enemy = enemy, hero = hero )

@app.route("/gameover", methods=["POST","GET"])
def gameover():
    return render_template("gameover.html")

if __name__ == "__main__":
    app.run(debug=True)
