from random import randint

d6 = lambda: randint(1,6)
dd6 = lambda: randint(1,6) + randint(1, 6)
xd6 = lambda x: [d6() for i in range(0,x)]

class Batalion():
    def __init__(self, initative=0, morale=0, companies=[]):
        self.initative = initative
        self.morale = morale
        self.companies = companies


class Company():
    def _init__(self, platoons=[]):
        self.platoons = platoons

    def shoot(self, target):
        for platoon in self.platoons:
            platoon.shoot(target)

    def isShotAt(self):
        pass

class Platoon():
    def __init__(self, shootStat, hitPoints):
        self.shootStat = shootStat
        self.hitPoints = hitPoints

    def shoot(self, target):
        pass
