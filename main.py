from flask import Flask, redirect, url_for, render_template, request
from characters import Character, skeleton, wraith, goblin, end
import random
import csv
import json

app = Flask(__name__)

hero = Character(0,"Empty", 1, True, 1, 1, 1, 1, 1, 1, 1, 1, "Empty",0)
userid = 0
userid += 1
lvldict = {"lvl0": 0, "lvl1":1, 'lvl2': 300, 'lvl3': 1000, 'lvl4':2000, 'lvl5':5000,'lvl6':8000,'lvl7':12000}
enemylist = [skeleton, goblin, wraith, end]
enemyline = 0
enemy = enemylist[enemyline]





def write_to_file(data):
    with open('database.txt', mode='r+') as database:
        global userid
        userid += len(database.readlines())
        data['userid'] = userid
        username = data["warriorname"]
        password = data["password"]
        charactername = data["username"]
        userage = data['age']
        data['useralive'] = True
        data['userhp'] = 30
        data['userac'] = 6
        data['userxp'] = 1
        data['userlvl'] = 1
        data['userammo'] = 6
        data['userstr'] =(random.randint(3, 18))
        data['userdex'] = (random.randint(3, 18))
        data['usercon'] = (random.randint(3, 18))
        data['userofd'] = data['objectOfDesire']
        data['userpotion'] = 5
        file = database.write(json.dumps(data))
        file = database.write('\n')
        userid -= 1


def write_to_csv(data):
    with open('database.csv', newline='',mode='r+') as database2:
        global userid
        userid += len(database2.readlines())
        username = data["warriorname"]
        password = data["password"]
        charactername = data["username"]
        userage = data['age']
        useralive = True
        userhp = 30
        userac = 6
        userxp = 1
        userlvl = 1
        userammo = 6
        userstr = (random.randint(3, 18))
        userdex = (random.randint(3, 18))
        usercon = (random.randint(3, 18))
        userofd = data['objectOfDesire']
        userpotion = 5
        csv_writer = csv.writer(database2,delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([userid,username,password,charactername,userage,useralive,userhp,userac,userxp,userlvl,userammo,userstr,userdex,usercon,userofd, userpotion])

def checkregistry(data):
    with open('database.txt', mode='r') as database:
        if data["warriorname"] and data["password"] in database:
            print('already exists')
            return redirect("/signin.html")
        else:
            write_to_file(data)
            write_to_csv(data)
            global userid
            userid += len(database.readlines())
            username = data["warriorname"]
            password = data["password"]
            charactername = data["username"]
            userage = data['age']
            useralive = True
            userhp = 30
            userac = 6
            userxp = 1
            userlvl = 1
            userammo = 6
            userstr = (random.randint(3, 18))
            userdex = (random.randint(3, 18))
            usercon = (random.randint(3, 18))
            userofd = data['objectOfDesire']
            userpotion = 5
            print('wrote to file')
            global hero
            hero = Character(userid,charactername, userage, useralive, userhp, userac, userxp, userlvl, userammo, userstr, userdex, usercon, userofd, userpotion)
            print(hero.name)


def signinfunc(data):
    with open('database.txt', mode='r') as database:
        for line in database.readlines():
            hgrab = json.loads(line)
            if data["warriorname"] == hgrab["warriorname"] and data["password"] == hgrab["password"]:
                print('character found')
                global hero
                hero = Character(hgrab["userid"],hgrab["username"],hgrab["age"],hgrab["useralive"],hgrab["userhp"],hgrab["userac"],hgrab["userxp"],hgrab["userlvl"],hgrab["userammo"],hgrab["userstr"],hgrab["userdex"],hgrab["usercon"],hgrab["userofd"],hgrab["userpotion"])
            else:
                print('character not found')



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
        return render_template('character.html', name=hero.name, obj=hero.ofd, hero=hero)
    else:
        return 'something went wrong'

@app.route("/signcheck", methods=["POST", "GET"])
def signcheck():
    if request.method == 'POST':
        global data
        data = request.form.to_dict()
        signinfunc(data)
        return render_template('character.html', name=hero.name, obj=hero.ofd, hero=hero)
    else:
        return 'something went wrong'





@app.route("/index", methods=["POST", "GET"])
def home():
    return render_template("index.html")

@app.route("/character", methods=["POST", "GET"])
def character():
    return render_template("character.html", name = username, obj= userofd, hero=hero)

@app.route('/arena', methods=["POST", "GET"])
def arena():
    while enemy.alive == True and hero.alive == True:
        # enemyattack
        strike = (random.randint(1, 20))
        if strike < hero.ac:
            combatmessage = "The beast slashes with it's claws but barely misses!"
            break
        else:
            e1damage = (random.randint(1, 8))
            hero.hp -= e1damage
            combatmessage = (f"\nThe beast's claws rip into your flesh for {e1damage} damage! ")
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
                combatmessage = (f"\nThe beast's claws rip into your flesh for {e1damage} damage! ")
                if hero.hp <= 0:
                    hero.alive = False
                    return render_template("dead.html", combatmessage = combatmessage)
                    break
                else:
                    break
        else:
            agestrike = (random.randint(1, 23))
            if agestrike < hero.con:
                combatmessage = "It's eyes probe deep but you look away just in time!"
                break
            else:
                e1damage = (random.randint(1, 10))
                ageint = int(hero.age)
                ageint -= e1damage
                hero.age = str(ageint)
                combatmessage = (f"\nThe Wraith's eyes probe deep in your soul and take away {e1damage} years! ")
                if ageint <= 0:
                    hero.alive = False
                    return render_template("dead.html", combatmessage=combatmessage)
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
                combatmessage = "The beast slashes with it's claws but barely misses!"
                break
            else:
                e1damage = (random.randint(1, 8))
                hero.hp -= e1damage
                combatmessage = (f"\nThe beast's claws rip into your flesh for {e1damage} damage! ")
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
            # combatmessage = "Test"
            # enemy = wraith
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
            heromessage = (f"You slash into the beast for {dagger_damage} damage!")
            if enemy.hp < 0:
                enemy.alive = False
                hero.xp += enemy.xp
                if hero.xp >= lvldict[f"lvl{hero.lvl + 1}"]:
                    hero.lvlup()
                    heromessage = (f"\nYour dagger slashs deep and the bastard falls to the dust. The crowd chants the\nname of their champion: {hero.name}!"
                                   f"\nYou've leveled up! You are now level {hero.lvl}".upper())
                else:
                    heromessage = (f"\nYour dagger slashs deep and the bastard falls to the dust. The crowd chants the\nname of their champion: {hero.name}!".upper())
                    pass
                heromessage= (f"\nYour dagger slashs deep and the bastard falls to the dust. The crowd chants the\nname of their champion: {hero.name}!".upper())
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
                        heromessage = (f"\nThe stone lands with a sickening thud and the bastard falls to the dust. The crowd chants the\nname of their champion: {hero.name}!"
                                       f"\nYou've leveled up! You are now level {hero.lvl}".upper())

                    else:
                        heromessage = (f"\nThe stone lands with a sickening thud and the bastard falls to the dust. The crowd chants the\nname of their champion: {hero.name}!".upper())
                        pass
                    enemyline += 1
                    enemy = enemylist[enemyline]
                    return render_template("enemydead.html", heromessage=heromessage, enemy= enemy, hero=hero)
                else:
                    break
    # heromessage="Not working on stone page goblin?"
    # ammomessage="Not working on stone page goblin?"
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
    # global enemy
    # global enemyline
    # for i in enemylist:
    #     i.alive == True
    # enemy = enemylist[0]
    return render_template("dead.html",heromessage = heromessage, enemy = enemy, hero = hero )

@app.route("/gameover", methods=["POST","GET"])
def gameover():
    # global enemy
    # global enemyline
    # for i in enemylist:
    #     i.alive == True
    # enemy = enemylist[0]
    return render_template("gameover.html")

if __name__ == "__main__":
    app.run(debug=True)