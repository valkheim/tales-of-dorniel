import Perso
import Quests
import utils as u
import acts as Acts

class Scenario():
    def __init__(self, perso, act):
        self.perso = perso
        self.choice(act)

    def displayQuests(self):
        u.clear()
        u.pheader()
        u.pbody(" Journal des quêtes :")
        print(' ║ ' + "┄" * 74 + ' ║ ')
        for q in self.perso.getQuests():
            u.pbody(repr(q))
        u.pfooter()
        input()

    def displayMap(self):
        u.clear()
        print(u.gf("draw/map"))
        input()

    def displayHelp(self):
        u.clear()
        u.pheader()
        u.pbody(" Aide du jeu :")
        print(' ║ ' + "┄" * 74 + ' ║ ')
        u.pbody("Raccourcis :")
        u.pbody("? : afficher cette aide mais vous l'aurez compris")
        u.pbody("X : quitter le jeu")
        u.pbody("J : ouvrir le journal des quêtes")
        u.pbody("C : afficher la carte")
        u.pfooter()
        input()


    def quit(self):
        # save
        u.clear()
        print("À bientôt")
        return False

    def choice(self, act):
        while "invalid choice":
            acts = Acts.acts(self)
            u.clear()
            u.pheader()
            u.pbody(acts[act][0])
            u.pbody()
            for i, interaction in enumerate(acts[act][1]):
                u.pbody("%d. %s" % (i + 1, interaction[0]))
            choice = u.pinput()
            if choice == "X":
                return self.quit()
            elif choice == "J":
                self.displayQuests()
            elif choice == "C":
                self.displayMap()
            elif choice == "?":
                self.displayHelp()
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
            self.perso.addQuest(Quests.MainQuest)
        else:
            pass
            pass
