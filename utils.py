import os
import textwrap

import pprint
import itertools


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def gf(filename):
    with open('./resources/'+filename, 'r') as f:
        return f.read()
def splash():
    print(gf("draw/splash"))

def game_init():
    input()
    pheader()
    pbody("""
      Bonjour jeune aventurier ! Tu pars en quête d'un trésor fabuleux.
      Dérobé à notre bon roi, tu devras le retrouver ainsi que son larcineur.
      Il sera puni dans les règles et tu te verras récompensé.

      Durant cette aventure, tu auras de nombreux choix à faire, à toi de
      faire les bons pour t'en sortir.
    """)
    pfooter()
    input()
    pheader()
    pbody("Bonne chance, Nous croyons en toi.")
    pfooter()
    input()

def game_over():
    print(gf("draw/gameover"))

def pheader():
    print(' ╔' + '═' * 76 + '╗ ')

def pbody(s = None):
    if s is None:
        print(' ║ ' + ' ' * 74 + ' ║ ')
    else:
        ls = s.split('\n')
        for l in ls:
            l = l.strip()
            if l != '':
                if len(l) < 74:
                    print(' ║ ' + l + ' ' * (80 - len(l) - 3 * 2) + ' ║ ')
                else:
                    pbody(textwrap.fill(l, 74))

def pinput(s = "", displayShortcuts = True):
    s = s.strip()
    if displayShortcuts:
        shortcuts = '?,X,J,C'
        print(' ║ ' + s +  (80 - (len(s) + 6 + len(shortcuts))) * ' ' + shortcuts + ' ║ ')
    else:
        pheader()
        print(' ║ ' + s +  (80 - len(s) - 6) * ' ' + ' ║ ')
    return input(' ╚═ ')

def pfooter():
    print(' ╚' + '═' * 76 + '╝ ')
