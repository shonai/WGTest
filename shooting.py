from random import randint

""" Rolling functions"""
d6 = lambda: randint(1,6)
dd6 = lambda: randint(1,6) + randint(1, 6)
xd6 = lambda x: [d6() for i in range(0,x)]

""" CONSTANTS """
PLATOON_HIT_POINTS = 6
PLATOON_DEAD = "Platoon is dead"
PLATOON_SHAKEN = "Platoon is SHAKEN"
PLATOON_OK = "Platoon is OK"

COMPANY_DEAD = "Company is dead"
COMPANY_SHAKEN = "Company is shaken"
COMPANY_OK = "Company is OK"

BATALION_DEAD = "Batalion is dead"
BATALION_SHAKEN = "Batalion is shaken"
BATALION_FLEEING = "Batalion is fleeing"
BATALION_OK = "Batalion is OK"
""" END CONSTANTS """


class Batalion():
    def __init__(self, initative=0, morale=0, companies=[]):
        self.initative = initative
        self.morale = morale
        self.companies = companies


class Company():
    def _init__(self, platoons=[]):
        self.platoons = platoons


    def shoot(self, target, range):
        for platoon in self.platoons:
            platoon.shoot(target)

    def isShotAt(self):
        pass
        self.checkState()

    def checkState(self):
        pass
        for platoon in self.platoons:
            platoonState = platoon.checkState()

class Platoon():
    def __init__(self, shootStat, hitPoints):
        self.shootStat = shootStat
        self.hitPoints = hitPoints
        self.state = PLATOON_OK

    def shoot(self, target, range):
        pass

    def isShotAt(self):
        pass
        self.checkState()

    def checkState(self):
        if self.hitPoints <= 0:
            self.state = PLATOON_DEAD
