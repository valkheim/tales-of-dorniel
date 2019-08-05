import Perso
import Quests
import Menu
import utils as u
import acts as Acts

class Scenario():
    def __init__(self, perso, act):
        self.perso = perso
        self.menu = Menu.Menu(perso)
        self.loopActs(act)

    def displayMenu(self):
        self.menu.display()

    def handleChoice(self, acts, act):
        u.pheader()
        for i, interaction in enumerate(acts[act][1]):
            u.pbody("[%d]  %s" % (i + 1, interaction[0]))
        choice = u.pinput()
        if choice == "M":
            self.displayMenu()
        elif choice == "C":
            self.menu.displayMap()
        elif choice == "J":
            self.menu.displayQuests()
        elif choice == "P":
            self.perso.display()
        elif choice == "?":
            self.menu.displayHelp()
        try:
            choice = int(choice)
        except:
            return act
        if choice in range(1, len(acts[act][1]) + 1):
            self.update(choice, act)
            act = acts[act][1][choice - 1][1]
            return act

    def loopActs(self, act):
        while "invalid choice":
            acts = Acts.acts(self)
            u.clear()
            for i, scenario in enumerate(acts[act][0]): # Loop act texts
                txt = scenario[0]
                fmt = scenario[1]
                if fmt:
                    u.pheader()
                    u.pbody(txt)
                else:
                    print(txt)
                if i == len(acts[act][0]): # last text in act
                    if fmt: u.pbody()
                else:
                    if fmt: u.pfooter()
                    input()
            if acts[act][1][0][0] is not None: # Act has questions
                act = self.handleChoice(acts, act)
            else:
                act = acts[act][1][0][1]

    def update(self, choice, act):
        if act == 0:
            if choice == 1:
                self.perso = Perso.Dwarf(self.perso.name)
            elif choice == 2:
                self.perso = Perso.Elf(self.perso.name)
            else:
                self.perso = Perso.Wizard(self.perso.name)
            self.menu = Menu.Menu(self.perso)
        elif act == 1:
            self.perso.addQuest(Quests.MainQuest)
        else:
            pass
