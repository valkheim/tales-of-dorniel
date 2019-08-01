import Perso
import utils
import acts as Acts

class Scenario():
    def __init__(self, perso, act):
        self.perso = perso
        self.choice(act)

    def displayQuests(self):
        utils.pheader()
        utils.pbody(" Journal des quêtes :")
        print(' ║ ' + "┄" * 74 + ' ║ ')
        utils.pbody("[ ] Trouver le trésor du roi")
        utils.pfooter()

    def displayMap(self):
        utils.clear()
        print(utils.gf("draw/map"))
        input()

    def choice(self, act):
        while "invalid choice":
            acts = Acts.acts(self)
            utils.clear()
            utils.pheader()
            utils.pbody(acts[act][0])
            utils.pbody()
            for i, interaction in enumerate(acts[act][1]):
                utils.pbody("%d. %s" % (i + 1, interaction[0]))
            choice = utils.pinput()
            if choice == "X":
                return False
            elif choice == "J":
                self.displayQuests()
                return True
            elif choice == "M":
                self.displayMap()
            try:
                choice = int(choice)
            except:
                continue
            if choice in range(1, len(acts[act][1]) + 1):
                self.update(choice, act)
                act = acts[act][1][choice - 1][1]

    def update(self, choice, act):
        if act == 0:
            if choice == 1:
                self.perso = Perso.Dwarf(self.perso.name)
            elif choice == 2:
                self.perso = Perso.Elf(self.perso.name)
            else:
                self.perso = Perso.Wizard(self.perso.name)
        elif act == 1:
            pass
