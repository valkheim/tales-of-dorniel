import utils as u

class Menu():
    choices = [
        'J. Journal des quêtes',
        'P. Personnage',
        'C. Carte(s)',
        'S. Sauvegarder',
        '?. Aide',
        'Q. Quitter'
    ]

    def __init__(self, perso):
        self.perso = perso

    def display(self):
        u.clear()
        u.pheader()
        u.pbody("Menu principal")
        u.phr()
        for c in self.choices:
            u.pbody(c)
        u.pfooter()
        c = input()
        if c == "3" or c == "C":
            self.displayMap()
        elif c == "2" or c == "S":
            print("sauvegarder")
        elif c == "1" or c == "J":
            self.displayQuests()
        elif c == "2" or c == "P":
            self.perso.display()
        elif c == "5" or c == "?":
            self.displayHelp()
        elif c == "6" or c == "Q":
            self.quit()

    def quit(self):
        u.clear()
        print("À bientôt")
        quit()

    def displayQuests(self):
        u.clear()
        u.pheader()
        u.pbody(" Journal des quêtes :")
        u.phr()
        for q in self.perso.getQuests():
            u.pbody(repr(q))
        u.pfooter()
        input()

    def displayMap(self):
        u.clear()
        print(u.gf("draw/maps/world"))
        input()

    def displayHelp(self):
        u.clear()
        u.pheader()
        u.pbody(" Aide du jeu :")
        u.phr()
        u.pbody("Raccourcis :")
        u.pbody("? : afficher cette aide mais vous l'aurez compris")
        u.pbody("M : ouvrir le menu principal")
        u.pbody("C : ouvrir la carte")
        u.pbody("P : voir le personnage")
        u.pbody("J : consulter le journal des quêtes")
        u.pfooter()
        input()

