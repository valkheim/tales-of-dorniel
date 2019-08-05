import random
import textwrap
import Quests
import utils as u

class Perso:
    def __init__(self, name = None):
        if name is None: # http://patorjk.com/software/taag/#p=display&f=Bloody&t=Dorniel
            self.name = u.pinput("Mais au fait, il te faut un nom de Héros ! Lequel choisis-tu ? (Baldur)", False)
            if self.name == "":
                self.name = "Baldur"
        else:
            self.name = name

        self.race = self.getRace(self.__class__.__name__)
        self.quests = Quests.Quests()
        self.age = 20

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

    def display(self):
        u.clear()
        u.pheader()
        around = int((74 - len(self.name)) / 2) * ' '
        if len(self.name) % 2:
            name = self.name + ' '
        else:
            name = self.name
        print(' ║ ' + around + name + around + ' ║ ')
        u.phr()
        portrait = [(3,2), u.gf('draw/races/'+self.__class__.__name__.lower())]
        characteristics = [(40, 2), u.gf("draw/skills").format(
            u.az(self.life),
            u.az(self.stamina),
            u.az(self.magic),
            u.az(self.attack),
            u.az(self.defense),
            u.az(self.strength),
            u.az(self.armour),
            u.az(self.intelligence),
            u.az(self.archery),
            u.az(self.invocation),
            u.az(self.defense),
            u.az(self.potion),
            u.az(self.heal)
        )]
        u.pbody(u.ptiles(portrait, characteristics, dx=74, dy=30))
        u.pfooter()
        input()

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
