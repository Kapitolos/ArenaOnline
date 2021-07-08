import random

class Character:
    def __init__(self,id, name, alive, hp, ac, xp, lvl, ammo, str, dex, con, potion):
        self.id = id
        self.name = name
        self.alive = alive
        self.hp = hp
        self.ac = ac
        self.xp = xp
        self.lvl = lvl
        self.ammo = ammo
        self.str = str
        self.dex = dex
        self.con = con
        self.potion = potion

    def lvlup(self):
        self.lvl += 1
        self.hp += 5 + self.lvl
        self.ac += 1 + self.lvl
        self.str += 1
        self.dex += 1
        self.con += 1






skeleton = Character(0,"Skeleton", True, 10, 7, 300, 1, 0, 14, 14, 14, 0)
wraith = Character(0,"Wraith", True, 10, 10, 750, 3, 0, 16, 17, 14, 0)
goblin = Character(0,"Goblin", True, 10, 7, 300, 1, 0, 14, 14, 14, 0)
end = Character(0,"gameover", True, 10, 10, 750, 3, 0, 16, 17, 14, 0)