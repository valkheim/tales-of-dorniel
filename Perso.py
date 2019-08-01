import random
import Quests
import utils

class Perso:
    def __init__(self, name = None):
        if name is None: # http://patorjk.com/software/taag/#p=display&f=Bloody&t=Dorniel
            utils.game_init()
            self.name = utils.pinput("  Mais au fait, quel est ton nom ? ", False)
        else:
            self.name = name

        self.race = self.getRace(self.__class__.__name__)
        self.quests = Quests.Quests()

        # Base points
        self.life = 100
        self.stamina = 100
        self.magic = 100

        # Base skills
        self.attack = 10
        self.defense = 10

        # Dwarf skills
        self.strength = 10
        self.armour = 10

        # Elf skills
        self.intelligence = 10
        self.archery = 10

        # Wizard skills
        self.invocation = 10
        self.destruction = 10
        self.potion = 10
        self.heal = 10

    def getRace(self, race):
        if race == "Dwarf":
            return "Nain"
        elif race == "Elf":
            return "Elfe"
        elif race == "Wizard":
            return "Magicien"

    def addQuest(self, q):
        return self.quests.add(q)

    def getQuests(self):
        return self.quests.get()

    def __str__(self):
        return """
            Race
            ┈┈┈┈ %s
            Talents
            ┈┈┈┈ (ATQ) Attaque :       %d
            ┈┈┈┈ (DEF) Défense :       %d
            ┈┈┈┈ (FOR) Force :         %d
            ┈┈┈┈ (ARM) Armure :        %d
            ┈┈┈┈ (INT) Intelligence :  %d
            ┈┈┈┈ (ARC) Archerie :      %d
            ┈┈┈┈ (INV) Invocation :    %d
            ┈┈┈┈ (DES) Destruciton :   %d
            ┈┈┈┈ (POT) Potions :       %d
            ┈┈┈┈ (GUE) Guérison :      %d""" % (self.race, self.attack, self.defense, self.strength, self.armour, self.intelligence, self.archery, self.invocation, self.defense, self.potion, self.heal)

LOW = 2
HIGH = 5

class Dwarf(Perso):
    def __init__(self, name):
        self.perso = Perso.__init__(self, name)

        self.life -= random.randint(LOW * 1.5, HIGH * 3)
        self.defense += random.randint(LOW, HIGH)
        self.strength += random.randint(LOW, HIGH)
        self.armour += random.randint(LOW, HIGH)

        self.intelligence -= random.randint(LOW, HIGH)
        self.invocation -= random.randint(LOW, HIGH)
        self.destruction -= random.randint(LOW, HIGH)
        self.potion -= random.randint(LOW, HIGH)


class Elf(Perso):
    def __init__(self, name):
        self.perso = Perso.__init__(self, name)

        self.life += random.randint(LOW * 1.5, HIGH * 3)
        self.intelligence += random.randint(LOW, HIGH)
        self.archery += random.randint(LOW, HIGH)
        self.heal += random.randint(LOW, HIGH)

        self.defense -= random.randint(LOW, HIGH)
        self.invocation -= random.randint(LOW, HIGH)
        self.destruction -= random.randint(LOW, HIGH)
        self.potion -= random.randint(LOW, HIGH)

class Wizard(Perso):
    def __init__(self, name):
        self.perso = Perso.__init__(self, name)

        self.invocation += random.randint(LOW, HIGH)
        self.destruction += random.randint(LOW, HIGH)
        self.potion += random.randint(LOW, HIGH)
        self.heal += random.randint(LOW, HIGH)

        self.strength -= random.randint(LOW, HIGH)
        self.armour -= random.randint(LOW, HIGH)
