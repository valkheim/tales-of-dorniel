import random
import utils

class Perso:
    def __init__(self, name = None):
        if name is None: # http://patorjk.com/software/taag/#p=display&f=Bloody&t=Dorniel
            utils.game_init()
            self.name = utils.pinput("  Mais au fait, quel est ton nom ? ")
        else:
            self.name = name

        self.race = self.__class__.__name__

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

    def __str__(self):
        return """
            Race:
                %s
            Skills:
                Attaque (ATK): %d
                Défense (DFE): %d
                Force (STR): %d
                Armure (ARM): %d
                Intelligence (INT): %d
                Archerie (ARC): %d
                Invocation (INV): %d
                Destruciton (DES): %d
                Potions (POT): %d
                Guérison (HEA): %d""" % (self.race, self.attack, self.defense, self.strength, self.armour, self.intelligence, self.archery, self.invocation, self.defense, self.potion, self.heal)

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
