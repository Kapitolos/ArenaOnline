from flask import Flask, redirect, url_for, render_template, request
from characters import Character, skeleton, wraith
import random
import csv
import json

app = Flask(__name__)

enemy = skeleton
hero = Character(0,"Empty", 1, True, 1, 1, 1, 1, 1, 1, 1, 1, "Empty")
found = True
userid = 0
userid += 1
print(userid)
with open('database.txt', mode='r') as database:
    print(len(database.readlines()))
    # print(database.readlines(1))


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
        # dictfile = {'userid': useridstr,'username': username,'password': password,'charactername':charactername,'userage': userage, 'useralive': useralive, "userhp":userhp, 'userac': userac, 'userxp':userxp, 'userlvl':userlvl, 'userammo': userammo,'userstr': userstr, 'userdex': userdex, 'usercon': usercon, 'userofd':userofd}
        # file =database.write(f'\n{userid},{username},{password},{charactername},{userage},{useralive},{userhp},{userac},{userxp},{userlvl},{userammo},{userstr},{userdex},{usercon},{userofd}')
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
        csv_writer = csv.writer(database2,delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([userid,username,password,charactername,userage,useralive,userhp,userac,userxp,userlvl,userammo,userstr,userdex,usercon,userofd])

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
            print('wrote to file')
            global hero
            hero = Character(userid,charactername, userage, useralive, userhp, userac, userxp, userlvl, userammo, userstr, userdex, usercon, userofd)
            print(hero.name)
            return render_template('character.html', name = hero.name, obj= hero.ofd, hero=hero)


def signinfunc(data):
    print('got to here')
    with open('database.txt', mode='r') as database:
        for line in database.readlines():
            hgrab = json.loads(line)
            # print(line)
            print(hgrab["warriorname"])
            print(data["warriorname"])
            if data["warriorname"] == hgrab["warriorname"] and data["password"] == hgrab["password"]:
                print('character found')
                global hero
                hero = Character(hgrab["userid"],hgrab["username"],hgrab["age"],hgrab["useralive"],hgrab["userhp"],hgrab["userac"],hgrab["userxp"],hgrab["userlvl"],hgrab["userammo"],hgrab["userstr"],hgrab["userdex"],hgrab["usercon"],hgrab["userofd"])
                print(hero.age)
                # return render_template('character.html', name=hero.name, obj=hero.ofd, hero=hero)
                # global hero
                # for i in grabhero:
                #     print(i)
                    # print(dir(hero))
                    # print([a for a in dir(hero) if not a.startswith('__')])
                    # for e in i:
                    #     hero = Character(e)
                # print(hero.name)
                # hero = Character(charactername, userage, useralive, userhp, userac, userxp, userlvl, userammo, userstr, userdex, usercon, userofd)
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
        # try:
        data = request.form.to_dict()
            # data = request.form
        print(data)
        checkregistry(data)
        return render_template('character.html', name=hero.name, obj=hero.ofd, hero=hero)
        # except Exception as e:
        #     print(e)
        #     return 'Did not save to database'
    else:
        return 'something went wrong'

@app.route("/signcheck", methods=["POST", "GET"])
def signcheck():
    if request.method == 'POST':
        # try:
        global data
        data = request.form.to_dict()
        signinfunc(data)
        return render_template('character.html', name=hero.name, obj=hero.ofd, hero=hero)
        # if found == True:
        #     return render_template('character.html', name=data["warriorname"], obj=data["password"])
        # else:
        #     print("Character Not Found")
        #     return render_template("characternotfound.html")
        # except Exception as e :
        #     print(e)
        # return 'function did not work'
    else:
        return 'something went wrong'





@app.route("/index", methods=["POST", "GET"])
def home():
    return render_template("index.html")

@app.route("/character", methods=["POST", "GET"])
def character():
    # username = request.form['username']
    # userage = request.form['age']
    # useralive = True
    # userhp = 30
    # userac = 6
    # userxp = 1
    # userlvl = 1
    # userammo = 6
    # userstr = (random.randint(3,18))
    # userdex = (random.randint(3,18))
    # usercon = (random.randint(3,18))
    # userofd = request.form['objectOfDesire']
    # global hero
    # hero = Character(username,userage, useralive, userhp, userac, userxp, userlvl, userammo, userstr, userdex, usercon, userofd )
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
    return render_template("arena.html", enemy= enemy, hero=hero, combatmessage=combatmessage)

@app.route('/wraith', methods=["POST", "GET"])
def wraithfight():
    global enemy
    enemy = wraith
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
                return render_template("dead.html", combatmessage = combatmessage)
                break
            else:
                break
    return render_template("wraith.html", enemy= enemy, hero=hero, combatmessage=combatmessage)

@app.route('/arenadagger', methods=["POST", "GET"])
def arenadagger():
        # my attack
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
                heromessage= (f"\nYour dagger slashs deep and the bastard falls to the dust. The crowd chants the\nname of their champion: {hero.name}!".upper())
                # return redirect("/enemydead", heromessage=heromessage, enemy= enemy, hero=hero)
                return render_template("enemydead.html", heromessage=heromessage, enemy= enemy, hero=hero)
            else:
                break
    return render_template("arenadagger.html", heromessage=heromessage, enemy= enemy, hero=hero)

@app.route('/arenastone', methods=["POST", "GET"])
def arenastone():
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
                    heromessage = (f"\nThe stone lands with a sickening thud and the bastard falls to the dust. The crowd chants the\nname of their champion: {hero.name}!".upper())
                    # return redirect("/enemydead", heromessage=heromessage, enemy= enemy, hero=hero)
                    return render_template("enemydead.html", heromessage=heromessage, enemy= enemy, hero=hero)
                #don't want redirect, but to route?
                else:
                    break

    return render_template("arenastone.html" ,heromessage=heromessage, enemy= enemy, hero=hero, ammomessage=ammomessage )

@app.route("/enemydead", methods=["POST","GET"])
def enemydead():
    return render_template("enemydead.html",heromessage = heromessage, enemy = enemy, hero = hero, ammomessage=ammomessage)

if __name__ == "__main__":
    app.run(debug=True)