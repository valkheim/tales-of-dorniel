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

def pblock(s):
    pheader()
    pbody(s)
    pfooter()
    input()

def game_init():
    input()
    pblock(gf("acts/intro/1"))
    pblock(gf("acts/intro/2"))
    pblock(gf("acts/intro/3"))
    pblock(gf("acts/intro/4"))

def game_over():
    print(gf("draw/gameover"))

def pheader():
    print(' ╔' + '═' * 76 + '╗ ')

def pbody(s = None):
    if s is None:
        print(' ║ ' + ' ' * 74 + ' ║ ')
    else:
        ls = s.split('\n\n')
        for l in ls:
            l = l.replace('\n', ' ').strip()
            if l != '':
                for w in textwrap.wrap(l, 74):
                    print(' ║ ' + w + ' ' * (80 - len(w) - 3 * 2) + ' ║ ')

def phr():
    print(' ║ ' + "┄" * 74 + ' ║ ')

def pinput(s = "", displayShortcuts = True):
    s = s.strip()
    if displayShortcuts:
        shortcuts = '[M]enu'
        print(' ║ ' + s +  (80 - (len(s) + 6 + len(shortcuts))) * ' ' + shortcuts + ' ║ ')
    else:
        pheader()
        print(' ║ ' + s +  (80 - len(s) - 6) * ' ' + ' ║ ')
    return input(' ╚═ ')

def pfooter():
    print(' ╚' + '═' * 76 + '╝ ')

def ptiles(*tiles, dx=None, dy=None):
    # Get matrix size
    (mx, my) = (0, 0)
    for t in tiles:
        (tx, ty) = t[0]
        if tx > mx:
            mx = tx
        if ty > my:
            my = ty
    # Force matrix size
    if dx is not None:
        mx = dx
    if dy is not None:
        my = dy
    # Init default matrix
    m = [[' ' for x in range(mx)] for y in range(my)]
    # Fill matrix
    for t in tiles:
        (tx, ty) = t[0]
        tile = t[1]
        for c in tile:
            if c == '\n':
                ty += 1
                (tx, _) = t[0]
            else:
                m[ty - 1][tx - 1] = c
                tx += 1
    # Print matrix
    for y in range(my):
        print(' ║ ' + "".join(m[y]) + ' ║ ')

def az(s): # add zero(s)
    return '0'*(3-len(str(s)))+str(s)
