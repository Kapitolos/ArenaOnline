import random

name= input("What is your name Warrior? ")
ammo = 6
strength=(random.randint(3,18))
dexterity=(random.randint(3,18))
constitution=(random.randint(3,18))
print(f"{name}, your random attributes are: ST:{strength}, DX:{dexterity},CN:{constitution}")
test = 0
intro= f"""

YOU, {name.upper()}, MUST FIGHT FOR YOUR PITIFUL LIFE!

                                WELCOME TO
                                   THE
                           __ _ _ __ ___ _ __   __
                         / _` | '__/ _ \ '_ \ / _` |
                        | (_| | | |  __/ | | | (_| |
                         \__,_|_|  \___|_| |_|\__,_|



Before you stands the Serpantman!



                                 """
print(intro)
serpantpic="""
        ,^.__.>--"~~'_.--~_)~^.
       _L^~   ~    (~ _.-~ \. |
    ,-~    __    __,^"/\_A_/ /'
  _/    ,-"  "~~" __) \  ~_,^   /
 //    /  ,-~\ x~"  \._"-~     ~ _Y
 Y'   Y. (__.//     /  " , "\_r ' ]
 J-.__l_>---r{      ~    \__/ \_ _/
(_ (   (~  (  ~"---   _.-~ `\ / \ !
 (_"~--^----^--------"  _.-c Y  /Y'
  l~---v----.,______.--"  /  !_/ |
   \.__!.____./~-.      _/  /  \ !
    `x._\_____\__,>---"~___Y\__/Y'
        ~     ~(_~~(_)"~___)/ /\|
               (_~~   ~~___)  \_t
               (_~~   ~~___)\_/ |
               (_~~   ~~___)\_/ |
               { ~~   ~~   }/ \ l
               """
print(serpantpic)



heroxp = (0)
lvl2 = 300
lvl3 = 600
enemy1 = True
enemy2 = True
enemy3 = True
hero = True
heroac = 15
enemy1ac = 12
enemy1hp = 6
enemy2ac=13
enemy2hp=10
enemy3ac = 10
enemy3hp = 20
herohp = 20
print(f"You are {name}, you have {herohp} hitpoints and {heroxp} experience points.")
while enemy1 == True and hero ==True:
    #enemyattack
    strike=(random.randint(1,20))
    if strike<heroac:
        print("\nThe beast slashes with it's claws but barely misses!")
    else:
        e1damage=(random.randint(1,8))
        herohp -=e1damage
        print(f"\nThe beast's claws rip into your flesh for {e1damage} damage! ")
        if herohp<=0:
            hero=False
            print("You are dead.")
            break
    #my attack
    action=input("Will you use (d)agger or (s)tone? ")
    if "dagger" in action or "Dagger" in action or "d" in action:
        ha = (random.randint(1,18))
        if ha < enemy1ac:
          print("You missed!")
        else:
          dagger_damage = (random.randint(1,8))
          enemy1hp -= dagger_damage
          print(f"You slash into the beast for {dagger_damage} damage!")
          if enemy1hp < 0:
            enemy1 = False
            print(f"\nYour dagger slashs deep and the bastard falls to the dust. The crowd chants the\nname of their champion: {name}!".upper())
    elif "stone" in action or "Stone" in action or "s" in action:
        if ammo<=0:
            print("You are out of stones!")
        else:
            ha = (random.randint(1,19))
            ammo -= 1
            print(f"You now have {ammo} stones left!")
            if ha < enemy1ac:
              print("You missed!")
            else:
                stone_damage = (random.randint(1,8))
                enemy1hp -= stone_damage
                print(f"Your stone sails true for {stone_damage} damage!")
                if enemy1hp < 0:
                    enemy1 = False
                    print(f"\nThe stone lands with a sickening thud and the bastard falls to the dust. The crowd chants the\nname of their champion: {name}!".upper())
    else:
        print("Has your mind faded so far?")
#end of encounter
if enemy1 ==False:
    heroxp+=300
    print(f"You now have {heroxp} experience points!")
if heroxp>=lvl2:
    herohp+=7
    heroac+=1
    print("You feel stronger!")
if heroxp>=lvl3:
    herohp+=9
    heroac+=1
    print("You further your skills...")

#encounter 2
enc2dis = """
The crowd screams in anticipation as you turn to see
the rushing silver footsteps of the armoured undead king of Rainikai!

      _,.
    ,` -.)
   ( _/-  -._
  /,|`--._,-^|            ,
  \_| |`-._/||          ,'|
    |  `-, / |         /  /
    |     || |        /  /
     `r-._||/   __   /  /
 __,-<_     )`-/  `./  /
'  \   `---'   \   /  /
    |           |./  /
    /           //  /
\_/' \         |/  /
 |    |   _,^-'/  /
 |    , ``  (\/  /_
  \,.->._    \X-=/^
  (  /   `-._//^`
   `Y-.____(__}
    |     {__)
          ()


YOU MUST CONTINUE THE FIGHT!!

"""
print(enc2dis)
print(f"You are {name}, you have {herohp} hitpoints and {heroxp} experience points.")
while enemy2 == True and hero ==True:
    #enemyattack
    strike=(random.randint(1,20))
    if strike<heroac:
        print("\nThe dead kings blade sours past and misses!")
    else:
        e2damage = (random.randint(1,8))
        herohp -= e2damage
        print(f"\nThe kings cold blade sinks into your soul for {e2damage} damage!")
        if herohp<=0:
            hero=False
            print("You are dead.")
            break
    #my attack
    action=input("Will you use (d)agger or (s)tone? ")
    if "dagger" in action or "Dagger" in action or "d" in action:
        ha = (random.randint(1,18))
        if ha < enemy2ac:
          print("You missed!")
        else:
          dagger_damage = (random.randint(1,8))
          enemy2hp -= dagger_damage
          print(f"Your blade sneaks past his guard for {dagger_damage} damage!")
          if enemy2hp < 0:
            enemy2 = False
            print(f"Your dagger pierces his dead heart and sends him back to his fallen land.\n The crowd chants the name of their champion: {name}!".upper())

    elif "stone" in action or "Stone" in action or "s" in action:
        if ammo<=0:
            print("You are out of stones!")
        else:
            ha = (random.randint(1,19))
            ammo -= 1
            print(f"You now have {ammo} stones left!")
            if ha < enemy2ac:
              print("You missed!")
            else:
              stone_damage = (random.randint(1,8))
              enemy2hp -= stone_damage
              print(f"Your stone sails true for {stone_damage} damage!")
              if enemy2hp < 0:
                enemy2 = False
                print(f"\nThe stone crushes in crown and skull. \nThe crowd chants the name of their champion: {name}!".upper())
    else:
        print("Has your mind faded so far?")

#end of encounter2
if enemy2 ==False:
    heroxp+=300
    print(f"\nYou now have {heroxp} experience points!")
if heroxp>=lvl2 and heroxp!=lvl3:
    herohp+=7
    heroac+=1
    print("You feel stronger!")
if heroxp>=lvl3:
    herohp+=9
    heroac+=1
    print("You further your skills...")
print("You pick up the dead Kings sword of souls!")

#encounter3
enc3dis= """
The arena falls silent. Your final foe emerges from thin air before your very eyes:

The Wraith of Ammagon!
            .--,
           /  (
          /
         /
        /  0  0
((()   |    ()    |   ()))
\  ()  (  .____.  )  ()  /
 |` \_/ \  `""`  / \_/ `|
 |       `.'--'.`       |
  \        `""`        /
   \                  /
    `.              .'    ,
     |`             |  _.'|
     |              `-'  /
     \                 .'
      `.____________.-'

"""

print(enc3dis)
print(f"You are {name}, you have {herohp} hitpoints and {heroxp} experience points.")
while enemy3 == True and hero == True:
    #enemyattack
    strike=(random.randint(1,20))
    if strike<heroac:
        print("\nThe Wraiths whispery fingers slip past your face!")
    else:
        e3damage = (random.randint(1,10))
        herohp -=e3damage
        print(f"\nThe Wraths icey voice enters your mind for {e3damage} damage!")
        if herohp<=0:
            hero=False
            print("You are dead.")
            break
    #my attack
    action=input("Will you use (d)agger, (s)tone or (K)ingsblade!? ")
    if "dagger" in action or "Dagger" in action or "d" in action:
        ha = (random.randint(1,18))
        if ha < enemy3ac:
          print("You missed!")
        else:
          dagger_damage = (random.randint(1,8))
          enemy3hp -= dagger_damage
          print(f"Your blade sneaks past his guard for {dagger_damage} damage!")
          if enemy3hp <=0:
            enemy3 = False
            print(f"\nYour dagger slashs the soul to shreds.\n The crowd chants the name of their champion: {name}!".upper())
    elif "stone" in action or "Stone" in action or "s" in action:
        if ammo<=0:
            print("You are out of stones!")
        else:
            ha = (random.randint(1,19))
            ammo -= 1
            print(f"You now have {ammo} stones left!")
            if ha < enemy2ac:
              print("You missed!")
            else:
               stone_damage = (random.randint(1,8))
               enemy3hp -= stone_damage
               print(f"Your stone sails true for {stone_damage} damage!")
               if enemy3hp <=0:
                enemy3 = False
                print(f"\nThe stone disperses the Wraith to nothingness.\n The crowd chants the name of their champion: {name}!".upper())
    elif "K" in action or "k" in action or "Kingsblade" in action or "kingsblade" in action:
        ha = (random.randint(3,20))
        if ha < enemy3ac:
            print("The royal blade misses!")
        else:
            kings_damage=(random.randint(3,10))
            enemy3hp -=kings_damage
            print(f"The cold blade burns his wretched soul for {kings_damage} damage!")
            if enemy3hp<=0:
                enemy3=False
                print("\nThe blade dissolves the Wraiths soul as it cries our in FINAL AGONY!")

    else:
        print("Has your mind faded so far?")

if enemy3 == False:
    heroxp+=300
    print(f"\nYou now have {heroxp} experience points!")
if heroxp>=lvl2 and heroxp<=lvl3:
    herohp+=7
    print("You feel stronger!")
if heroxp>=lvl3:
    herohp+=9
    print("You further your skills...")
endingbad="""
The crowd laughs at your death.

"""
if hero == False:
    print(endingbad)
ending=f"""

You are {name} and you have defeated every foe the Arena has to offer with {herohp} hitpoints remaining.
  /
  | |
  |.|
  |.|
  |:|      __
,_|:|_,   /  )
  (Oo    / _I_
   +\ \  || __|
      \ \||___|
        \ /.:.\-
         |.:. /-----
         |___|::oOo::|
         /   |:<_T_>:|
        |_____\ ::: /
         | |  \ \:/
         | |   | |
         \ /   | \___
         / |   \_____
Now you return to the darkness... """
if enemy3 == False and hero == True:
    print(ending)
